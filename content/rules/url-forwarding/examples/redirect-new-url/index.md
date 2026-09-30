<p class="article-summary">Create a redirect rule to redirect visitors from `/contact-us/` to the page&#x27;s new path `/contacts/`.</p>
<p>This example static redirect for zone <code>example.com</code> will redirect visitors requesting the <code>/contact-us/</code> page to the new page URL <code>/contacts/</code>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13199.md")
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
<td><code>example.com/contact-us/</code></td>
<td><code>example.com/contacts/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/contact-us/?state=TX</code></td>
<td><code>example.com/contacts/?state=TX</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/team/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
