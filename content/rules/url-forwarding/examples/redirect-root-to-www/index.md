<p class="article-summary">Create a redirect rule to forward HTTPS requests from the root (also known as the “apex” or “naked” domain) to the WWW subdomain.</p>
<p>This example creates a redirect rule that forwards HTTPS requests from the root domain (<code>example.com</code>) to the WWW subdomain (<code>www.example.com</code>), while retaining the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13198.md")
</div>
<p>This rule ensures that only HTTPS requests from the root domain are redirected to the WWW subdomain, leaving other requests (such as HTTP or requests to other subdomains) unchanged.</p>
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
<td><code>https://example.com/products/</code></td>
<td><code>https://www.example.com/products/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://store.example.com/products/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>https://example.com/admin/?logged_out=true</code></td>
<td><code>https://www.example.com/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://example.com/?all_items=true</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>http://www.example.com/admin/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
<p>Make sure to replace <code>example.com</code> with your actual hostname before deploying your rule.</p>
