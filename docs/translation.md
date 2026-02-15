# Translation

Reflex theme supports translations (i18n) of all messages used in the theme to different languages.

## Available translations

Messages may not be fully translated, please check the *Contribute* section below if you can help.

| Language | Code | Since |
|----------|:----:|:-----:|
| German :de:                       | de    | 2.0 |
| Spanish :es:                      | es    | 2.2 |
| Spanish (Spain) :es:              | es_ES | 2.2 |
| Estonian :estonia:                | et    | 2.2 |
| Persian (Iran) :iran:             | fa_IR | 2.2 |
| French :fr:                       | fr    | 2.0 |
| Hungarian :hungary:               | hu_HU | 2.1 |
| Italian :it:                      | it    | 2.1 |
| Dutch (Netherlands) :netherlands: | nl_NL | 2.2 |
| Polish (Poland) :poland:          | pl_PL | 2.2 |
| Portuguese (Brazil) :brazil:      | pt_BR | 2.0 |
| Russian :ru:                      | ru    | 2.1 |
| Turkish (Turkey) :tr:             | tr_TR | 2.2 |
| Chinese (Simplified, China) :cn:  | zh_CN | 2.2 |

English :us: is the default language.

## Enable translations

Skip this if you will use only English.

To enable a custom translation you need to enable i18n and choose your language.

### How to enable translations

At first clone the [pelican-plugins](https://github.com/getpelican/pelican-plugins/) repository and enable i18n for your pelican site by adding the following code to your `pelicanconf.py`:

```python
# Path to Plugins
PLUGIN_PATHS = ['/path/to/pelican-plugins']
# Enable i18n plugin, probably you already have some others here.
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
```

With this done you can use the theme with texts in the English language as usual.

### Changing to another language

The step above only enables i18n, but it won't translate anything away from English.

If you want to translate to another language you need to change `DEFAULT_LANG` and `I18N_TEMPLATES_LANG` in your  `pelicanconf.py`.
You should change `LOCALE` and `OG_LOCALE` to match your new configuration too.

*IMPORTANT: `I18N_TEMPLATES_LANG` must **not** be set to the language in which you want to translate your site, but to the **original** language in which templates are written (in this case, `en`).*

For example:

```python
# Default theme language.
I18N_TEMPLATES_LANG = "en"

# Your language.
DEFAULT_LANG = "de_DE"

# Match languages for other configs.
OG_LOCALE = "de_DE"
LOCALE = ("de_DE", "de_DE.utf8")
```

Now the site will be translated into German.

Language code (`de_DE` in the example above) must exist in [translations directory](../translations) for it to work.

## Supporting multiple translations (i18n_subsites)

Use the [i18n_subsites plugin](https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites) if you want a single site that supports multiple languages.

You can find more info in the project documentation.

Look at [blog.fidelramos.net's source code](https://github.com/haplo/blog.fidelramos.net) for a fully working example.

## Contribute

To contribute a translation you will need to [git clone](https://github.com/git-guides/git-clone) reflex's repository.

Translations are hold in the [translations directory](../translations).
Each translation has its own directory with the language code and, optionally, a region subcode (e.g. `es_ES` is Spanish [Spain], but `es_CO` is Spanish [Colombia]).

The generation and compilation of translation files is handled by [Babel](https://babel.pocoo.org/).
Install it with `pip` or [`pipx`](https://pypa.github.io/pipx/).

### Usage of translate.sh

Command-line parameters:

    new [language]  create a new translation.
    compile         compile all PO files into MO files.
    update          update all translations based on POT file.
    extract         extract all messages from templates and create the POT file.

### Creating a new translation

Let's translate to Spanish for example:

``` shell
./translate.sh new es
```

This will create the translation file in `translations/es/LC_MESSAGES/messages.po`

### Updating translations

When new text is introduced in the theme's templates or existing text changes, the translation catalogs need to be updated to include it.
To update all existing catalogs run:

``` shell
./translate.sh update
```

After this the `.po` files should have been updated to include the new/changed text.

### Editing a translation

Translating is simply a matter of writing the translation in the `msgstr` string.
For example this section:

``` gettext-catalog
#: templates/base.html:161
msgid "Search..."
msgstr ""
```

The Spanish translation catalog would then set `msgstr "Buscar..."`.

When translation catalogs change they need to be compiled from PO to MO files.
For than run:

``` shell
./translate.sh compile
```

This will create the compiled translation file in:

`translations/es/LC_MESSAGES/messages.mo`

### Submitting the translation

Once you have created or updated a translation, and compiled the changes, you need to submit the request.

1. [Commit your changes to git](https://github.com/git-guides/git-commit).
2. [Push your changes to GitHub](https://github.com/git-guides/git-push)
3. [Create a pull request](https://github.com/haplo/python-theme-reflex/pull/new).
