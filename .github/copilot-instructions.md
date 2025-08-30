# software-architektur.tv

Software-architektur.tv is a German podcast and live stream website about software architecture hosted by Eberhard Wolff. This is a Jekyll-based static website that generates podcast episode pages with embedded videos, audio podcasts, transcripts, and blog posts. The site is deployed to GitHub Pages.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Bootstrap and Dependencies
**CRITICAL**: Install Ruby and bundler before any Jekyll operations:
- `ruby --version` (should be 3.2+)
- `gem install bundler --user-install`
- `export PATH="$HOME/.local/share/gem/ruby/3.2.0/bin:$PATH"`
- `cd /home/runner/work/software-architektur.tv/software-architektur.tv`
- `bundle config set path 'vendor/bundle'`
- `bundle install` -- takes about 30 seconds. Dependencies include Jekyll 3.9.5 and github-pages gem.

### Build the Site
**NETWORK LIMITATION**: Building requires GitHub API access and will fail in restricted network environments:
- `bundle exec jekyll build` -- **FAILS due to DNS monitoring proxy blocking GitHub API access**
- The build fails because Jekyll tries to fetch GitHub repository metadata for feed generation
- **Error**: `GET https://api.github.com/repos/ewolff/software-architektur.tv: 403 - Blocked by DNS monitoring proxy`

### Run Development Server
**WORKAROUND FOR NETWORK ISSUES**: Use skip-initial-build flag:
- `bundle exec jekyll serve --host 0.0.0.0 --port 4000 --skip-initial-build`
- Server starts successfully at http://localhost:4000 
- **NEVER CANCEL**: Server may take 30-60 seconds to start fully. Set timeout to 120+ seconds.
- **NOTE**: `./server.sh` script fails in restricted environments because it doesn't use `--skip-initial-build`

### Build Times and Timeouts
- **Bundle install**: ~25 seconds for fresh install (already installed: ~1 second)
- **Jekyll serve**: 30-60 seconds to start. NEVER CANCEL. Set timeout to 120+ seconds.
- **Jekyll build**: Would take 2-5 minutes if network access worked. NEVER CANCEL builds.

## Validation

### Manual Testing Scenarios
**ALWAYS test these scenarios after making changes:**

1. **Server startup test**:
   ```bash
   cd /home/runner/work/software-architektur.tv/software-architektur.tv
   export PATH="$HOME/.local/share/gem/ruby/3.2.0/bin:$PATH"
   bundle exec jekyll serve --skip-initial-build --host 0.0.0.0 --port 4000
   ```
   - Should start without errors and show "Server running..." message
   - Wait at least 30 seconds for full startup

2. **Episode page validation**:
   - Navigate to http://localhost:4000/ in browser
   - Click on any episode link (e.g., "Folge 179")
   - Verify page loads with proper layout, video embeds, and content

3. **Homepage functionality**:
   - Verify main page loads at http://localhost:4000/
   - Check that upcoming episode information displays correctly
   - Verify navigation links work

4. **Content rendering test**:
   - Create a test episode file in `_posts/` with proper frontmatter
   - Jekyll should auto-regenerate and include the new episode
   - Verify the episode appears in the site

### Content Validation
- **Episode structure**: Each episode post should have frontmatter with video, peertube, mp3, and thumbnail fields
- **Transcript integration**: Episodes with transcripts should automatically include blog posts, summaries, and full transcripts from `_includes/transcriptions/`
- **Media embedding**: Verify YouTube and PeerTube video embeds work correctly

### Network Considerations
- **Development works offline**: Jekyll serve works without internet when using `--skip-initial-build`
- **Full build requires internet**: GitHub Pages deployment needs GitHub API access for metadata
- **Content is self-contained**: All episode content, transcripts, and media references are in the repository

## Repository Structure

### Key Directories and Files
- `_posts/` -- 274+ episode markdown files (format: `YYYY-MM-DD-folgeXXX.md`)
- `_layouts/` -- Jekyll layouts including `folge.html` for episode pages
- `_includes/` -- Reusable template parts and transcription content
- `_includes/transcriptions/` -- AI-generated episode transcripts, summaries, and blog posts
- `_data/summaries.yml` -- Configuration for which episodes have transcriptions
- `thumbnails/` -- Episode thumbnail images
- `css/` -- Styling for the website
- `_config.yml` -- Jekyll configuration (title, author, plugins)

### Important Files
- `Gemfile` -- Ruby dependencies including github-pages ~231, minima theme
- `server.sh` -- Development server startup script
- `index.md` -- Homepage with live stream info and upcoming episodes
- `podcast.md` -- Podcast feed information page

### Content Structure
Episode posts follow this structure:
```markdown
---
title: Folge XXX - Episode Title
layout: folge
video: YouTube_video_ID
peertube: https://tube.tchncs.de/videos/embed/VIDEO_ID
mp3: https://podcast-url.com/episode.mp3
embedded-mp3: https://embedded-player-url.com
description: Episode description
thumbnail: folgeXXX.png
tags:
- Tag1 
- Tag2
---

Episode content in markdown...
```

## Common Tasks

### Adding a New Episode
1. Copy the template: `cp _posts/template.md _posts/YYYY-MM-DD-folgeXXX.md`
2. Edit the new file and update all frontmatter fields:
   - `title`: Episode title
   - `video`: YouTube video ID
   - `peertube`: PeerTube embed URL
   - `mp3`: Direct link to MP3 file
   - `embedded-mp3`: Embedded player URL
   - `description`: Episode description
   - `thumbnail`: Thumbnail filename (in `/thumbnails/` directory)
   - `tags`: List of relevant tags
3. Add episode content in markdown below the frontmatter
4. If transcripts exist, add episode ID to `_data/summaries.yml`
5. Place transcript files in `_includes/transcriptions/folgeXXX/`

### Working with Transcripts
- Transcripts are automatically included if episode ID exists in `_data/summaries.yml`
- Each episode can have: `blog_post.md`, `summary.md`, `transcript_structured.md`
- Files go in `_includes/transcriptions/[episode_id]/`

### Updating Site Configuration
- Edit `_config.yml` for site-wide settings
- Edit `index.md` for homepage content and upcoming episode info

### Development Workflow
1. Always run `bundle install` first after cloning
2. Start server with `bundle exec jekyll serve --skip-initial-build`
3. Make changes to content files (markdown, layouts, etc.)
4. Jekyll auto-regenerates pages (watch mode enabled by default)
5. Test changes by viewing in browser at localhost:4000
6. **Important**: Do not commit build artifacts - `.gitignore` excludes `_site/`, `vendor/`, and cache directories

### File Editing Guidelines
- Episode files: Edit in `_posts/` directory
- Layout changes: Edit files in `_layouts/` 
- Shared content: Edit files in `_includes/`
- Site configuration: Edit `_config.yml`
- Homepage content: Edit `index.md`

## Troubleshooting

### "Bundle command not found"
- Run `gem install bundler --user-install`
- Add gem bin directory to PATH: `export PATH="$HOME/.local/share/gem/ruby/3.2.0/bin:$PATH"`

### "Permission denied" during gem install
- Use `--user-install` flag: `gem install bundler --user-install`
- Configure bundle path: `bundle config set path 'vendor/bundle'`

### Build fails with GitHub API errors
- Use `--skip-initial-build` flag for development
- Full builds require unrestricted internet access
- This is expected behavior in restricted network environments

### Server won't start
- Check that port 4000 is available
- Use `--host 0.0.0.0` to bind to all interfaces
- Wait at least 60 seconds before considering it failed

## Repository Output Examples

### Repository root listing
```
.
├── _config.yml
├── _data/
├── _includes/
├── _layouts/
├── _posts/          # 274+ episode files
├── css/
├── Gemfile
├── Gemfile.lock
├── index.md
├── podcast.md
├── server.sh
├── thumbnails/
└── vendor/bundle/   # Installed gems
```

### Sample episode frontmatter
```yaml
---
title: Folge 179 - Software-Architektur = Abhängigkeiten Managen?
layout: folge
video: kmV0r5_oUh0
peertube: https://tube.tchncs.de/videos/embed/fcc9d18b-1695-479f-aaa2-ec94df22c005
embedded-mp3: https://www.podcaster.de/simpleplayer/?id=show~1evriw~...
mp3: https://1evriw.podcaster.de/software-architektur-im-stream/media/...
description: Was sind Abhängigkeiten überhaupt? Sind sie wirklich so zentral?
thumbnail: folge179.png
tags:
- Abhängigkeiten
- Grundlagen
---
```

### Episode template file
Use `_posts/template.md` as a starting point for new episodes:
```yaml
---
title: Folge - 
layout: folge
video: Hex Code You Tube
peertube: PeerTube URL
sketchnote-video: Hex Code You Tube
embedded-mp3: link
mp3: link
description: 
thumbnail: OOP.jpg
tags:
- English
---
```