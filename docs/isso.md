# Isso Comment Server

Reflex has an integration with the [Isso](https://posativ.org/isso/) comment server.

Assumming you already have a [working Isso installation](https://posativ.org/isso/docs/install/), add the following to your `pelicanconf.py`:

```python
ISSO_URL = "//comments.example.com"
```

Replace `comments.example.com` with your comment server domain.

## Optional parameters

The settings are optional to configure the integration:

| Parameter | What does it do? |
|:---------:|------------------|
| `ISSO_EMBED_JS_PATH` | Path to the `embed.min.js` or `embed.dev.js` file for Isso. The default is to use the `isso.min.js` in `static/isso`. |
| `ISSO_OPTIONS` | Dictionary of Isso options to values. The option is automatically prepended with `data-isso-`. See https://posativ.org/isso/docs/configuration/client/ for all of the options. |

### Example configuration

```python
# Isso settings
ISSO_URL = '//comments.sumnerevans.com'
ISSO_EMBED_JS_PATH = '/static/javascript/isso-dev.min.js'
ISSO_OPTIONS = {
    'avatar': 'false',
    'gravatar': 'true',
    'reply-to-self': 'true',
    'reply-notifications': 'true',
}
```
