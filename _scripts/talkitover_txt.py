#!/usr/bin/env python3
"""Write transcriptions/<id>.txt for the TalkItOver button.

The file bundles everything an LLM needs to talk an episode over with
a reader: a note for the LLM, title and description from the post,
summary, bullet points and transcript. The layout folge.html shows the
button only for episodes that have such a file.

Usage, from the repository root:

    python3 _scripts/talkitover_txt.py          # all episodes with a transcript
    python3 _scripts/talkitover_txt.py 341 342  # only these episodes

Run it again whenever a post, summary, bullet points or transcript changes.
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE_URL = "https://software-architektur.tv"

NOTE_DE = """> **Hinweis für das LLM:** Die Leserin oder der Leser möchte über diese Folge von
> Software Architektur im Stream sprechen. Gib zuerst in zwei, drei Sätzen eine Orientierung,
> frag dann, was sie oder ihn interessiert, und biete ein paar Einstiege an.
>
> Stütze dich auf diese Datei. Halte drei Quellen auseinander und sag, woher eine Antwort
> stammt: aus dieser Folge, aus anderen Quellen oder aus deinem eigenen Wissen. Zusammenfassung,
> Stichpunkte und Transkript wurden mit KI erstellt und können Fehler enthalten; maßgeblich ist
> das Video. Schreib niemandem eine Aussage zu, die er nicht gemacht hat. Nennt das Transkript
> keine Sprecher, rate nicht, wer etwas gesagt hat. Hat eine KI an der Folge teilgenommen, gib
> ihre Beiträge nicht als Meinung der Menschen aus. Behandelt die Folge eine Frage nicht, sag
> das zuerst."""

NOTE_EN = """> **Note for the LLM:** The reader wants to talk about this episode of Software Architektur
> im Stream. Start with two or three sentences of orientation, then ask what they would like to
> explore, and offer a few entry points.
>
> Base your answers on this file. Keep three sources apart and say which one an answer comes
> from: this episode, other sources you looked at, and your own knowledge. Summary, bullet points
> and transcript were created with AI and may contain errors; the video is the authoritative
> source. Never attribute a statement to someone who did not make it. If the transcript has no
> speaker labels, don't guess who said what. If an AI took part in the episode, don't present
> its contributions as the view of the humans. If the episode does not cover a question, say so
> first."""

LABELS_DE = ("Folge", "Seite", "Über die Folge", "Zusammenfassung", "Stichpunkte", "Transkript")
LABELS_EN = ("episode", "Page", "About the episode", "Summary", "Bullet points", "Transcript")

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)
ZEITLINK = re.compile(r"\{%-?\s*include\s+zeitlinks\.html\s+s=(\d+)\s*-?%\}")
LIQUID = re.compile(r"\{%.*?%\}|\{\{.*?\}\}", re.S)


def read_post(path):
    front, body = FRONT_MATTER.match(path.read_text(encoding="utf-8")).groups()
    return yaml.safe_load(front), body


def clean(text):
    """Turn timestamp includes into [h:mm:ss], drop any other Liquid."""
    def stamp(m):
        s = int(m.group(1))
        return f"[{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}]"
    return LIQUID.sub("", ZEITLINK.sub(stamp, text)).strip()


def demote(text):
    """Nest the headings of an included file one level deeper."""
    return re.sub(r"^(#+) ", r"#\1 ", text, flags=re.M)


def page_url(path, post):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.*)\.md\Z", path.name)
    year, month, day, name = m.groups()
    return f"{SITE_URL}/{year}/{month}/{day}/{post.get('slug') or name}.html", f"{year}-{month}-{day}"


def build(episode_id, post_path):
    post, body = read_post(post_path)
    english = "English" in (post.get("tags") or [])
    note, labels = (NOTE_EN, LABELS_EN) if english else (NOTE_DE, LABELS_DE)
    url, date = page_url(post_path, post)
    lines = [f"# {post['title']}", ""]
    lines.append(f"Software Architektur im Stream, {labels[0]} {episode_id}, {date}.")
    if post.get("description"):
        lines.append(str(post["description"]).strip())
    lines.append(f"{labels[1]}: {url}")
    if post.get("video"):
        lines.append(f"YouTube: https://www.youtube.com/watch?v={post['video']}")
    if post.get("peertube"):
        lines.append("PeerTube: " + post["peertube"].replace("videos/embed/", "w/"))
    if post.get("mp3"):
        lines.append(f"MP3: {post['mp3']}")
    lines += ["", note, "", f"## {labels[2]}", "", clean(body)]
    for label, folder in zip(labels[3:], ("zusammenfassung", "stichpunkte", "transcriptions")):
        source = ROOT / folder / f"{episode_id}.md"
        if source.exists():
            lines += ["", f"## {label}", "", demote(clean(source.read_text(encoding="utf-8")))]
    return "\n".join(lines) + "\n"


def posts_by_episode():
    result = {}
    for path in sorted((ROOT / "_posts").glob("*.md")):
        episode_id = read_post(path)[0].get("episode_id")
        if episode_id is not None:
            result[str(episode_id)] = path
    return result


def main(wanted):
    posts = posts_by_episode()
    ids = wanted or sorted(p.stem for p in (ROOT / "transcriptions").glob("*.md"))
    for episode_id in ids:
        if episode_id not in posts:
            print(f"{episode_id}: no post, skipped", file=sys.stderr)
            continue
        target = ROOT / "transcriptions" / f"{episode_id}.txt"
        target.write_text(build(episode_id, posts[episode_id]), encoding="utf-8")
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])
