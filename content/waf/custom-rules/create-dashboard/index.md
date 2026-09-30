<div class="nb-steps">
@markup("md", "content/.markup/bodies/15395.md")
</div>
<h2 id="configure-a-custom-response-for-blocked-requests">Configure a custom response for blocked requests</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15394.md")
</aside>
<p>When you select the <em>Block</em> action in a rule you can optionally define a custom response.</p>
<p>The custom response has three settings:</p>
<ul>
<li><strong>With response type</strong>: Choose a content type or the default WAF block response from the list. The available custom response types are the following:</li>
</ul>
<table>
<thead>
<tr>
<th>Dashboard value</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Custom HTML</td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td>Custom Text</td>
<td><code>&quot;text/plain&quot;</code></td>
</tr>
<tr>
<td>Custom JSON</td>
<td><code>&quot;application/json&quot;</code></td>
</tr>
<tr>
<td>Custom XML</td>
<td><code>&quot;text/xml&quot;</code></td>
</tr>
</tbody>
</table>
<ul>
<li>
<p><strong>With response code</strong>: Choose an HTTP status code for the response, in the range 400-499. The default response code is 403.</p>
</li>
<li>
<p><strong>Response body</strong>: The body of the response. Configure a valid body according to the response type you selected. The maximum field size is 2 KB.</p>
</li>
</ul>
