# Dark theme

Flex provides a light (default) and a dark theme.
Optionally, Reflex can automatically detect the color theme preference set by the user's browser/OS and can allow the user to switch the theme manually.

## Configuration overview

* `THEME_COLOR` (either `"light"` (default) or `"dark"`): the default theme to use when the user/browser/OS does not override it.
* `THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE` (`bool`): set to `True` if you want Reflex to auto-detect the user's browser/OS color scheme preference and use the appropriate theme.
* `THEME_COLOR_ENABLE_USER_OVERRIDE` (`bool`): set to `True` if you want Reflex to provide links in the footer of the page for the user to override the theme.
* `PYGMENTS_STYLE_DARK` (`str`, fallback to `PYGMENTS_STYLE` or `monokai`): select a Pygments style to use in dark mode.

## Example configuration

This config will make Reflex use the dark theme by default, but will respect the browser/OS color scheme preference, and allow the user to override the theme.
It will also use the `emacs` Pygments theme in light mode, but the `monokai` theme in dark mode.

```python
THEME_COLOR = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = "emacs"
PYGMENTS_STYLE_DARK = "monokai"
```

Example of site that is using this configuration: [sumnerevans.com](https://sumnerevans.com).

## Browser Support

* The `THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE` setting relies on the `prefers-color-scheme` media query.
All major browsers now support this, except for Internet Explorer.
Check [Can I use](https://caniuse.com/#feat=mdn-css_at-rules_media_prefers-color-scheme).
* JavaScript is *not* required for the `THEME_COLOR`, `THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE`, and `PYGMENTS_STYLE` settings to work.
Only the media query is used.
* JavaScript *is* required for the `THEME_COLOR_ENABLE_USER_OVERRIDE` to work.
