# Shynet tracking

[Shynet](https://github.com/milesmcc/shynet) is a simple self-hosted web analytics tool.
Integration requires adding a snippet on every page to be tracked:

``` html
+<noscript>
+  <img src="https://shynet.example.com/pixel.gif">
+</noscript>
+<script defer src="https://shynet.example.com/script.js"></script>
```

Reflex supports Shynet out-of-the-box, just set the `SHYNET_URL` setting in `pelicanconf.py` pointing to the base URL for the service as provided by Shynet.
For the example above the setting would be:

``` python
SHYNET_URL = "https://shynet.example.com"
```
