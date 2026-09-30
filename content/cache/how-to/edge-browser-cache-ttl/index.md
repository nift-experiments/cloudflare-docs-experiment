<h2 id="edge-cache-ttl">Edge Cache TTL</h2>
<p>Edge Cache TTL (Time to Live) specifies the maximum time to cache a resource in the Cloudflare global network. Edge Cache TTL is not visible in response headers and the minimum Edge Cache TTL depends on plan type.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Minimum Edge Cache TTL</td>
<td>2 hours</td>
<td>1 hour</td>
<td>1 second</td>
<td>1 second</td>
</tr>
</tbody>
</table>
<p>For more information on how to set up Edge Cache TTL, refer to <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Cache rules</a>.</p>
<h2 id="browser-cache-ttl">Browser Cache TTL</h2>
<p>The Browser Cache TTL sets the expiration for resources cached in a visitor’s browser. By default, Cloudflare honors the cache expiration set in your <code>Expires</code> and <code>Cache-Control</code> headers but overrides those headers if:</p>
<ul>
<li>The value of the <code>Expires</code> or <code>Cache-Control</code> header from the origin web server is less than the Browser Cache TTL Cloudflare setting.</li>
<li>The origin web server does not send a <code>Cache-Control</code> or an <code>Expires</code> header.</li>
</ul>
<p>Unless specifically set in a cache rule, Cloudflare does not override or insert <code>Cache-Control</code> headers if you set <strong>Browser Cache TTL</strong> to <strong>Respect Existing Headers</strong>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3875.md")
</aside>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Minimum Browser Cache TTL (Page Rules)</td>
<td>2 minutes</td>
<td>2 minutes</td>
<td>2 minutes</td>
<td>30 seconds</td>
</tr>
<tr>
<td>Minimum Browser Cache TTL</td>
<td>1 second</td>
<td>1 second</td>
<td>1 second</td>
<td>1 second</td>
</tr>
<tr>
<td>Default Browser Cache TTL</td>
<td>4 hours</td>
<td>4 hours</td>
<td>4 hours</td>
<td>4 hours</td>
</tr>
</tbody>
</table>
<p>For more information on setting the Browser Cache TTL, refer to <a href="/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/">Set Browser Cache TTL</a>.</p>
