<p>Caching levels determine how much of your website’s static content Cloudflare should cache. Cloudflare’s CDN caches static content according to the levels below.</p>
<ul>
<li><strong>No Query String</strong>: Delivers resources from cache when there is no query string. Example URL: <code>example.com/pic.jpg</code></li>
<li><strong>Ignore Query String</strong>: Delivers the same resource to everyone independent of the query string. Example URL: <code>example.com/pic.jpg?ignore=this-query-string</code></li>
<li><strong>Standard (Default)</strong>: Delivers a different resource each time the query string changes. Example URL: <code>example.com/pic.jpg?with=query</code></li>
</ul>
<p>You can adjust the caching level from the dashboard under <strong>Caching</strong> &gt; <strong>Configuration</strong> &gt; <strong>Caching level</strong>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3810.md")
</aside>
<h2 id="api-caching-level-values">API Caching level values</h2>
<p>If you are using the API to change the cache level, the values will differ from those shown in the dashboard. Refer to the table below to see how the API values map to the values shown in the dashboard.</p>
<table>
<thead>
<tr>
<th>Dashboard</th>
<th>API</th>
</tr>
</thead>
<tbody>
<tr>
<td>No Query String</td>
<td>Basic</td>
</tr>
<tr>
<td>Ignore Query String</td>
<td>Simplified</td>
</tr>
<tr>
<td>Standard (Default)</td>
<td>Aggressive</td>
</tr>
</tbody>
</table>
