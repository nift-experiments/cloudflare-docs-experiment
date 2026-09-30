<p class="article-summary">Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths.</p>
<p>In this example, all website visitors from the United Kingdom will be redirected to a different domain, but maintaining current functionality in the same paths.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13203.md")
</div>
<p>This configuration will perform the following redirects for UK visitors:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>URL after redirect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/</code></td>
<td><code>https://example.co.uk/</code></td>
</tr>
<tr>
<td><code>https://example.com/my/path/to/page.htm</code></td>
<td><code>https://example.co.uk/my/path/to/page.htm</code></td>
</tr>
<tr>
<td><code>https://example.com/search?q=term</code></td>
<td><code>https://example.co.uk/search?q=term</code></td>
</tr>
</tbody>
</table>
