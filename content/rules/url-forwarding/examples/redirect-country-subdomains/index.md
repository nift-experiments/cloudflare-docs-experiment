<p class="article-summary">Create a redirect rule to redirect United Kingdom and France visitors from the `example.com` website&#x27;s  root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.</p>
<p>This example single redirect for zone <code>example.com</code> will redirect United Kingdom and France visitors requesting the website's root path (<code>/</code>) to their localized subdomains <code>https://gb.example.com</code> and <code>https://fr.example.com</code>, respectively.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13200.md")
</div>
<p>For example, the redirect rule would perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Visitor country</th>
<th>Request URL</th>
<th>Target URL</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td>United Kingdom</td>
<td><code>example.com</code></td>
<td><code>https://gb.example.com</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td>France</td>
<td><code>example.com</code></td>
<td><code>https://fr.example.com</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td>United States</td>
<td><code>example.com</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
