<p class="article-summary">Create a redirect rule to redirect requests for the administration area of `store.example.com` to HTTPS, keeping the original path and query string.</p>
<p>This example single redirect for zone <code>example.com</code> will redirect requests for the administration area of a specific subdomain (<code>store.example.com</code>) to HTTPS, keeping the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13205.md")
</div>
<p>For example, the redirect rule would perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>Target URL</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>http://store.example.com/admin/products/</code></td>
<td><code>https://store.example.com/admin/products/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://store.example.com/admin/products/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>http://store.example.com/admin/?logged_out=true</code></td>
<td><code>https://store.example.com/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://store.example.com/?all_items=true</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>http://example.com/admin/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
