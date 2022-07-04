# Google AdSense

Reflex allows you to place ads in six places.

All banners are responsive.
When you create a new banner on AdSense always choose the responsive one.

```python
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-1234567890',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}
```

Google AdSense may take a while to display in the first time.
Usually 24 hours.
