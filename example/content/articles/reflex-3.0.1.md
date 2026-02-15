Title: Reflex 3.0.1
Date: 2026-02-15
Category: News
Tags: pelican,python,theme
Slug: reflex-3.0.1

Reflex 3.0.1 is a bugfix release.

It fixes the Python package structure, which was buggy and made it unusable.
I also upgraded all NPM dependencies to latest versions, but that is only relevant for theme developers.

Reflex is now available on PyPI as [pelican-theme-reflex](https://pypi.org/project/pelican-theme-reflex/).
It can be installed as a normal package:

```
pip install pelican-theme-reflex
```

And then it can be used in *pelicanconf.py* like this:

```python
from pelican.themes import reflex
THEME = reflex.path()
```

Now that Reflex is published I will try to get it included in [pelican-themes](https://github.com/getpelican/pelican-themes).
