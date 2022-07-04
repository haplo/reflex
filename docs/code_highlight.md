# Code highlightning

Reflex uses [Pygments](http://pygments.org/) for code highlight and has a lot of styles ready to use.
You just need to pick one from [here](../static/pygments) and set it in your `pelicanconf.py`.

Example:

```python
PYGMENTS_STYLE = "monokai"
```

Remember to remove *.min.css* from the file name.

Most of the styles look like the ones at the [Pygments demo](https://pygments.org/demo/).

## How to add new Styles?

Except for `github` all other styles are built-in from Pygments.
If you want to add a new one, you need to find a Python package that is what you want or you can [create your own](http://pygments.org/docs/styles/#creating-own-styles).

After this, you can run [this tool](../pygments) to generate all Pygments CSS files and run `gulp` to minify.
