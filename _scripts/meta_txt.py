#!/usr/bin/env python3
"""Write episoden.txt, the overview of all episodes for the TalkItOver
button on the home page.

The file lets an LLM recommend episodes by their content. Each entry
names number, date, title, language, guests, the episode page and
whether there is a transcript, with the link to the episode text in
transcriptions/<id>.txt. The content block is the profile from
profile/<id>.md, otherwise the summary from zusammenfassung/<id>.md
shortened to similar length, otherwise the post text before its first
heading or the description, whichever is longer.

Usage, from the repository root:

    python3 _scripts/meta_txt.py

Run it again whenever posts, summaries or profiles change. The profiles
are not built into the site (published: false); they only feed this file.
"""
import html
import re
import sys

sys.dont_write_bytecode = True  # keep _scripts/ free of __pycache__
from talkitover_txt import ROOT, SITE_URL, clean, page_url, read_post

TARGET = ROOT / "episoden.txt"
MAX_WORDS = 160

HEADER = """# Software-Architektur im Stream: alle Folgen

Software-Architektur im Stream ist ein wöchentlicher Live-Stream mit Eberhard Wolff, Lisa
Schäfer, Ralf D. Müller und Lucas Dohmen, oft mit Gästen, seit 2020. Diese Datei listet alle
Folgen, die neuesten zuerst. Startseite: {site}

> **Hinweis für das LLM:** Die Leserin oder der Leser sucht Folgen zu einem Thema oder einer
> Frage. Frag nach, wenn das Anliegen unklar ist. Such dann in dieser Datei nach dem Inhalt der
> Folgen, nicht nur nach Wörtern im Titel, und nenn mehrere passende Folgen, jeweils mit einem
> Satz, warum sie passt, und dem Link auf die Folgenseite. Bevorzuge bei zeitkritischen Themen
> wie KI-Werkzeugen, Cloud-Angeboten oder Regulierung die neueren Folgen und sag dazu, von wann
> eine Folge ist.
>
> Steht bei einer Folge „Transkript: ja“, kannst du die verlinkte Textdatei nachladen, um die
> Folge genauer zu beschreiben; sie enthält Zusammenfassung und Transkript. Kannst du nicht
> nachladen, gib den Link weiter: Auf der Folgenseite gibt es einen eigenen Knopf, um die Folge
> mit einer KI zu besprechen. Steht dort „Transkript: nein“, beschreibt die Inhaltsangabe nur,
> was vor der Sendung angekündigt war, nicht, was tatsächlich besprochen wurde. Sag das dazu,
> wenn du eine solche Folge empfiehlst.
>
> Stütze dich auf diese Datei und erfinde nichts über eine Folge, was hier oder im nachgeladenen
> Text nicht steht. Die Inhaltsangaben wurden mit KI erstellt und können Fehler enthalten;
> maßgeblich ist das Video. Englische Folgen sind auf Deutsch beschrieben; antworte in der
> Sprache der Leserin oder des Lesers. Findest du keine passende Folge, sag das.
"""

LANGUAGE = {"de": "Deutsch", "en": "Englisch"}
MD_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
TAG = re.compile(r"<[^>]+>")
SENTENCE_END = re.compile(r"(?<=[.!?…])\s+")


def plain(text):
    """Markdown and HTML to one line of plain text, without headings."""
    text = clean(text)
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
    text = TAG.sub(" ", MD_LINK.sub(r"\1", text))
    text = re.sub(r"[*_`]", "", html.unescape(text))
    return " ".join(text.split())


def shorten(text, limit=MAX_WORDS):
    """Whole sentences up to about limit words."""
    result, count = [], 0
    for sentence in SENTENCE_END.split(text):
        words = len(sentence.split())
        if result and count + words > limit:
            break
        result.append(sentence)
        count += words
    return " ".join(result)


def intro(body):
    """The post text before its first heading, usually the announcement."""
    for chunk in re.split(r"^#+ .*$", clean(body), flags=re.M):
        text = plain(chunk)
        if text:
            return text
    return ""


def load_profiles():
    """profile/<id>.md: topics, guests etc. in the front matter, text below."""
    profiles = {}
    for path in (ROOT / "profile").glob("*.md"):
        profile, body = read_post(path)
        profile["profil"] = body.strip()
        profiles[path.stem] = profile
    return profiles


def entry(post_path, post, body, profile, stats):
    episode_id = post.get("episode_id")
    episode_id = str(episode_id) if episode_id is not None else None
    url, date = page_url(post_path, post)
    title = str(post["title"]).strip()
    heading = f"## Folge {episode_id}: {title}" if episode_id else f"## Sonderfolge: {title}"
    language = "en" if "English" in (post.get("tags") or []) else "de"
    if profile:
        language = profile.get("sprache", language)
    facts = [f"Datum: {date}", f"Sprache: {LANGUAGE.get(language, language)}"]
    if profile and profile.get("gaeste"):
        facts.append("Gäste: " + ", ".join(profile["gaeste"]))
    lines = [heading, "", " · ".join(facts), f"Seite: {url}"]
    transcript = episode_id and (ROOT / "transcriptions" / f"{episode_id}.txt").exists()
    if profile and profile.get("themen"):
        lines.append("Themen: " + ", ".join(profile["themen"]))
    if profile and profile.get("hinweis"):
        lines.append(profile["hinweis"])

    summary = ROOT / "zusammenfassung" / f"{episode_id}.md"
    if profile and profile.get("profil"):
        content, source = profile["profil"].strip(), "profil"
    elif episode_id and summary.exists():
        content, source = shorten(plain(summary.read_text(encoding="utf-8"))), "zusammenfassung"
    else:
        description = plain(str(post.get("description") or ""))
        announcement = intro(body)
        if len(announcement.split()) > len(description.split()):
            content, source = shorten(announcement), "beitragstext"
        else:
            content, source = shorten(description), "beschreibung"
    stats[source] = stats.get(source, 0) + 1
    if transcript:
        lines.append(f"Transkript: ja – Text: {SITE_URL}/transcriptions/{episode_id}.txt")
    elif source == "beschreibung":
        lines.append("Transkript: nein – Inhaltsangabe aus der Kurzbeschreibung vor der Sendung")
    else:
        lines.append("Transkript: nein – Inhaltsangabe aus der Ankündigung vor der Sendung")
    if content:
        lines += ["", content]
    return "\n".join(lines)


def main():
    profiles = load_profiles()
    stats, entries = {}, []
    for path in sorted((ROOT / "_posts").glob("*.md"), reverse=True):
        post, body = read_post(path)
        if not post.get("title"):
            continue
        profile = profiles.get(str(post.get("episode_id")))
        entries.append(entry(path, post, body, profile, stats))
    text = HEADER.format(site=SITE_URL) + "\n" + "\n\n".join(entries) + "\n"
    TARGET.write_text(text, encoding="utf-8")
    words = len(text.split())
    print(f"{TARGET.relative_to(ROOT)}: {len(entries)} Folgen, {words} Wörter, "
          f"ca. {round(words * 1.4)} Token")
    print(", ".join(f"{k}: {v}" for k, v in sorted(stats.items())))


if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.exit(__doc__)
    main()
