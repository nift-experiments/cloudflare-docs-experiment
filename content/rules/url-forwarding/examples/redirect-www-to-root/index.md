<p class="article-summary">Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the “apex” or “naked” domain).</p>
<p>This example creates a redirect rule that forwards HTTPS requests from the WWW subdomain (<code>www.example.com</code>) to the root domain (<code>example.com</code>), while retaining the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13197.md")
</div>
<p>This rule ensures that only HTTPS requests from <code>www.</code> subdomains are redirected to the root domain, leaving other requests (such as HTTP or non-WWW) unchanged.</p>
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
<td><code>https://www.example.com/products/</code></td>
<td><code>https://example.com/products/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://www.store.example.com/products/</code></td>
<td><code>https://store.example.com/products/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://store.example.com/products/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>https://www.example.com/admin/?logged_out=true</code></td>
<td><code>https://example.com/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://www.example.com/?all_items=true</code></td>
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
