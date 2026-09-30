<p class="article-summary">Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80).</p>
<p>In this example the original domain was replaced with a different domain. All functionality was maintained, except for the HTTP service (port 80) which was discontinued.</p>
<p><a href="/rules/url-forwarding/single-redirects/create-dashboard/">Create a redirect rule</a> with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13204.md")
</div>
<p>This configuration will perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>URL after redirect</th>
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
<td><code>https://example.com/my/path/to/page.htm</code></td>
<td><code>https://example.net/my/path/to/page.htm</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://example.com/search?q=term</code></td>
<td><code>https://example.net/search?q=term</code></td>
<td><code>301</code></td>
</tr>
</tbody>
</table>
