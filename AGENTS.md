# AGENTS.md - Development Guide for Reflex Pelican Theme

## Project Overview

Reflex is a minimalist Pelican theme using Jinja2 templates, LESS stylesheets, and JavaScript. It uses Gulp for asset compilation.

## Build Commands

### Node.js/Gulp (Asset Compilation)

```bash
# Install dependencies
npm install

# Build all assets (CSS, JS, fonts, pygments)
npm run build
# or: gulp default

# Watch for changes and rebuild automatically
npm run watch
# or: gulp watch

# Individual gulp tasks:
gulp less        # Compile LESS to CSS
gulp uglify      # Minify JS
gulp cp          # Copy font-awesome assets
gulp pygments    # Minify pygments CSS
```

### Python/Pelican (Testing)

```bash
# Build docs (test the theme)
pelican -s docs/pelicanconf.py
```

### Example Site (in example/ directory)

```bash
cd example/

# Generate site
make html

# Serve locally
make serve PORT=8000

# Development server with auto-regeneration
make devserver PORT=8000

# Clean build
make clean

# Publish (production settings)
make publish
```

## Code Style Guidelines

### Jinja2 Templates

- Use 2-space indentation
- Use snake_case for variables
- Use double quotes for HTML attributes
- Include spaces inside Jinja2 delimiters: `{{ var }}` not `{{var}}`
- Use `-` for whitespace control in macros: `{%- macro -%}`
- Place template comments on their own line: `{# comment #}`
- Use `{% include %}` with quotes: `{% include "partial/sidebar.html" %}`
- Check for plugin availability before including: `{% if PLUGINS and 'plugin_name' in PLUGINS %}`

### LESS/CSS

- Use 2-space indentation
- Place opening brace on same line: `selector {`
- Use lowercase with hyphens for class names: `.dark-theme`
- Import variables at top: `@import "variables.less";`
- Use variables from variables.less for colors and fonts
- Add trailing semicolons
- Group related properties together

### JavaScript

- Use 2-space indentation
- Use semicolons
- Use camelCase for variables and functions
- Use PascalCase for constructor functions
- Prefer single quotes for strings
- Add spaces around operators: `var x = a + b;`
- Document functions with inline comments

### File Naming

- Templates: lowercase with hyphens (e.g., `base.html`, `dark-theme.less`)
- Partials: place in `templates/partial/` directory
- Stylesheets: use `.less` extension for source, `.min.css` for compiled
- JavaScript: use `.js` extension for source, `.min.js` for minified

## Project Structure

```
.
├── static/               # Static assets
│   ├── stylesheet/       # LESS/CSS files
│   ├── dark-theme/       # Dark theme JS
│   ├── pygments/         # Code highlighting styles
│   └── font-awesome/     # Font Awesome assets
├── templates/            # Jinja2 templates
│   ├── partial/          # Reusable template partials
│   ├── base.html         # Base template
│   ├── article.html      # Article page
│   └── index.html        # Index page
├── docs/                 # Documentation
├── example/              # Example Pelican site
├── gulpfile.js           # Gulp build configuration
└── package.json          # Node.js dependencies
```

## Testing

- Tests build the docs/ site as a smoke test
- No unit tests - testing is done by building the theme

## Dependencies

### Node.js (package.json)

- gulp: ^4.0.2
- gulp-cssnano: ^2.1.3
- gulp-less: ^4.0.1
- gulp-rename: ^2.0.0
- gulp-uglify: ^3.0.2

### Python (for testing)

- pelican
- Dependencies in docs/requirements.txt

## Common Tasks

### Adding a New Template Partial

1. Create file in `templates/partial/`
2. Include in base.html or relevant template
3. Follow 2-space indentation
4. Use existing partials as reference

### Adding New Styles

1. Edit appropriate `.less` file in `static/stylesheet/`
2. Use variables from `variables.less`
3. Run `gulp less` or `npm run watch` to compile
4. Test in both light and dark themes

### Adding JavaScript

1. Edit source file in `static/dark-theme/`
2. Run `gulp uglify` to minify
3. Ensure minified version is referenced in templates

## Notes

- Always rebuild assets (`npm run build`) before committing
- The theme supports both light and dark modes
- Font Awesome is copied from node_modules to static/
- Pygments styles are minified but kept as separate files
- No linting tools are configured - follow existing code style
