Title: Reflex 3.1.0
Date: 2026-02-18 14:00
Category: News
Tags: pelican,python,theme
Slug: reflex-3.1.0

Reflex 3.1.0 includes various enhancements:

- Accessibility improvements:
  - Underline links inside main content, to make them recognizable without color.
  - Improve contrast of link colors
  - Add ARIA names to sidebar social icons.
- Add pre-commit hooks for code quality:
  - djlint for Jinja2 templates
  - Trailing whitespace
  - JSON/YAML checker
  - Assets build
- Move `static/`, `templates/`, and `translations/` directories back to root to make it easier to use the theme from source code (e.g. a `git clone`). Reflex remains installable via PyPI with the same interface.
- Upgrade Isso to 0.13.0.
- Highlight Isso comments made by the page author.
- Refactor footer templates.
- Remove Flex-inherited Google Analytics config.
- Mark AddThis as defunct in README (will be removed in Reflex 4.0.0).
