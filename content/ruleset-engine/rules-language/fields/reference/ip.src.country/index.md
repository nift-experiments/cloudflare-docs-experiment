<h1 id="ip-src-country">ip.src.country</h1>

**Data type:** String

<p>The 2-letter country code in <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format.</p>

<p>For more information on the ISO 3166-1 Alpha 2 format, refer to <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 Alpha 2</a> on Wikipedia.</p>
<p>This field has the same value as the <code>ip.geoip.country</code> field, which is deprecated. The <code>ip.geoip.country</code> field is still available for new and existing rules, but you should use the <code>ip.src.country</code> field instead.</p>
<p><em>GeoIP is the registered trademark of MaxMind, Inc.</em></p>

**Example value:**

```txt
"GB"
```

<h2 id="categories">Categories</h2>

- Request
- Geolocation

**Keywords:** request, location, geolocation, ip.geoip.country, client, visitor

