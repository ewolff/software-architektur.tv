# Software-Architektur.tv

Eberhard Wolff's Software Architektur im Stream - Jekyll-based website.

## Development

### Local Development Server

**Recommended**: Use the provided server script for local development:

```bash
./server.sh
```

This script starts Jekyll with optimal settings for local development. The site will be available at `http://localhost:4000`.

### Manual Jekyll Commands

If you prefer manual control:

```bash
# Install dependencies
bundle install

# Build the site
bundle exec jekyll build

# Serve with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build --destination _site
```

## Features

### Guest-List

The website includes a comprehensive Guest-List feature showcasing all stream guests with interactive filtering and search capabilities.

**Key Features:**
- ✅ 159+ guests from all episodes with working episode links
- ✅ Smart tag categorization (AI, Code Quality, Team Dynamics, etc.)
- ✅ Interactive search and filtering
- ✅ Responsive design for all devices
- ✅ Direct links to stream episodes

**Usage:**
- Visit `/guests/` to explore all stream guests
- Filter by expertise tags or search by name
- Click on episodes to watch the streams

**Data Management:**
- Guest data is stored in `_data/guests.yml` (YAML format)
- YAML was chosen over Markdown for structured data to enable:
  - Easy programmatic filtering and sorting
  - Consistent data validation
  - Better integration with Jekyll's data processing
  - Simplified maintenance of large datasets (100+ guests)

## Deployment

The site is automatically deployed via GitHub Pages when changes are pushed to the main branch.

## Contributing

1. Test locally with `./server.sh`
2. Ensure all links work correctly
3. Verify responsive design
4. Submit pull requests for review

---

*For detailed Guest-List maintenance instructions, see `Guest-List/README.md`*