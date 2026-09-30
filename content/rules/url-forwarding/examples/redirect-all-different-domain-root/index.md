<p class="article-summary">Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.</p>
<p>In this example, an old website was discontinued and replaced by a new one in a different domain. The functionality is different, and all URLs should now point to the root of the new domain. The same applies to any subdomains of the old domain.</p>
<p><a href="/rules/url-forwarding/single-redirects/create-dashboard/">Create a redirect rule</a> with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13202.md")
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
<td><code>http://example.com/</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://subdomain.example.com/</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/my/path/to/page.htm</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/search?q=term</code></td>
<td><code>https://example.net/</code></td>
<td><code>301</code></td>
</tr>
</tbody>
</table>
