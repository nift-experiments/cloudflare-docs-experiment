<h1 id="ip-src-subdivision-1-iso-code">ip.src.subdivision_1_iso_code</h1>

**Data type:** String

<p>The ISO 3166-2 code for the first-level region associated with the IP address.</p>

<p>When the actual value is not available, this field contains an empty string.</p>
<p>Requires a Cloudflare Business or Enterprise plan.</p>
<p>For more information on the ISO 3166-2 standard and the available regions, refer to <a href="https://en.wikipedia.org/wiki/ISO_3166-2">ISO 3166-2</a> on Wikipedia.</p>
<p>This field has the same value as the <code>ip.geoip.subdivision_1_iso_code</code> field, which is deprecated. The <code>ip.geoip.subdivision_1_iso_code</code> field is still available for new and existing rules, but you should use the <code>ip.src.subdivision_1_iso_code</code> field instead.</p>
<p><em>GeoIP is the registered trademark of MaxMind, Inc.</em></p>

**Example value:**

```txt
"GB-ENG"
```

<h2 id="categories">Categories</h2>

- Request
- Geolocation

**Keywords:** request, location, geolocation, ip.geoip.subdivision_1_iso_code, region, client, visitor

