<h1 id="ip-src-continent">ip.src.continent</h1>

**Data type:** String

<p>The continent code associated with the client IP address.</p>

<p>Values:</p>
<ul>
<li><code>&quot;AF&quot;</code>: Africa</li>
<li><code>&quot;AN&quot;</code>: Antarctica</li>
<li><code>&quot;AS&quot;</code>: Asia</li>
<li><code>&quot;EU&quot;</code>: Europe</li>
<li><code>&quot;NA&quot;</code>: North America</li>
<li><code>&quot;OC&quot;</code>: Oceania</li>
<li><code>&quot;SA&quot;</code>: South America</li>
<li><code>&quot;T1&quot;</code>: Tor network</li>
</ul>
<p>This field has the same value as the <code>ip.geoip.continent</code> field, which is deprecated. The <code>ip.geoip.continent</code> field is still available for new and existing rules, but you should use the <code>ip.src.continent</code> field instead.</p>
<p><em>GeoIP is the registered trademark of MaxMind, Inc.</em></p>

<h2 id="categories">Categories</h2>

- Request
- Geolocation

**Keywords:** request, location, geolocation, ip.geoip.continent, client, visitor

