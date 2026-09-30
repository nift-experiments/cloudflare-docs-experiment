<p>APO cache by device type provides all of the same benefits of Cloudflare's cache while targeting visitors with content appropriate to their device. Cloudflare evaluates the <code>User-Agent</code> header in the HTTP request to identify the device type. Cloudflare then identifies each device type with a case insensitive match to the regex below:</p>
<ul>
<li><strong>Mobile</strong>: <code>(?:phone|windows\s+phone|ipod|blackberry|(?:android|bb\d+|meego|silk|googlebot) .+? mobile|palm|windows\s+ce|opera mini|avantgo|mobilesafari|docomo|kaios)</code></li>
<li><strong>Tablet</strong>: <code>(?:ipad|playbook|(?:android|bb\d+|meego|silk)(?! .+? mobile))</code></li>
<li><strong>Desktop</strong>: Everything else not matched above.</li>
</ul>
<p>To enable caching by device type, enable the setting from the Cloudflare dashboard's APO card or from the WordPress plugin version 4.4.0 or later.</p>
<p>Once enabled, Cloudflare sends a <code>CF-Device-Type</code> HTTP header to your origin with a value of either <code>mobile</code>, <code>tablet</code>, <code>desktop</code> for every request to specify the visitor’s device type. If your origin responds with the appropriate content for that device type, Cloudflare only caches the resource for that specific device type.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3343.md")
</aside>
<p>The Cloudflare for WordPress plugin automatically purges all cache variations for updated pages.</p>
<p>Cloudflare recommends that you use plugins that support cache by device type, which you may have to enable on the plugin. You will still need to test your plugins to make sure they behave as expected.</p>
