<p class="article-summary">Create a redirect rule to redirect all requests for `smallshop.example.com` to a different hostname using HTTPS, keeping the original path and query string.</p>
<p>This example single redirect will redirect all requests for <code>smallshop.example.com</code> to a different hostname <code>globalstore.example.net</code> using HTTPS, keeping the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13201.md")
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
<td><code>http://smallshop.example.com/</code></td>
<td><code>https://globalstore.example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://smallshop.example.com/admin/?logged_out=true</code></td>
<td><code>https://globalstore.example.net/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://smallshop.example.com/?all_items=1</code></td>
<td><code>https://globalstore.example.net/?all_items=1</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://example.com/about/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
