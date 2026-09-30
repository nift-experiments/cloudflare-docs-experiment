<h2 id="error-code-reference">Error code reference</h2>
<table>
<thead>
<tr>
<th>Code</th>
<th>HTTP status</th>
<th>Message</th>
<th>Likely cause</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1002</code></td>
<td>400</td>
<td>Invalid set payload</td>
<td>Request body is malformed or missing required fields</td>
<td>Verify the body is valid JSON with <code>resource_type</code>, <code>resource_id</code>, and <code>tags</code></td>
</tr>
<tr>
<td><code>1003</code></td>
<td>400</td>
<td><code>resource_type</code> and <code>resource_id</code> are required</td>
<td>Missing query parameters</td>
<td>Include both <code>resource_type</code> and <code>resource_id</code> in the query string</td>
</tr>
<tr>
<td><code>1006</code></td>
<td>400</td>
<td>Invalid resource type</td>
<td>Unsupported resource type</td>
<td>Use a <a href="/resource-tagging/reference/resource-types/">supported resource type</a></td>
</tr>
<tr>
<td><code>1007</code></td>
<td>400</td>
<td>tag parameter must be in format...</td>
<td>Tag filter syntax is incorrect</td>
<td>Refer to <a href="/resource-tagging/how-to/filter-resources/">tag filtering syntax</a></td>
</tr>
<tr>
<td><code>1009</code></td>
<td>400</td>
<td><code>tag_key</code> is required</td>
<td>Missing <code>tag_key</code> parameter</td>
<td>Include the <code>tag_key</code> path parameter</td>
</tr>
<tr>
<td><code>1010</code></td>
<td>400</td>
<td>too many tag filters (maximum 20)</td>
<td>More than 20 <code>tag</code> query parameters</td>
<td>Reduce filters to 20 or fewer, or split across multiple requests</td>
</tr>
<tr>
<td><code>1011</code></td>
<td>400</td>
<td>tag key too long (maximum 256 characters)</td>
<td>Tag key exceeds 256 characters</td>
<td>Shorten the tag key</td>
</tr>
<tr>
<td><code>1012</code></td>
<td>400</td>
<td>tag value too long (maximum 1024 characters)</td>
<td>Tag value exceeds 1,024 characters</td>
<td>Shorten the tag value</td>
</tr>
<tr>
<td><code>1013</code></td>
<td>400</td>
<td>too many OR values in tag filter (maximum 10)</td>
<td>More than 10 comma-separated values in a single filter</td>
<td>Split into multiple filters</td>
</tr>
<tr>
<td><code>1014</code></td>
<td>400</td>
<td>Invalid tag key</td>
<td>Key contains invalid characters</td>
<td>Use only letters, digits, <code>_</code>, <code>.</code>, <code>-</code></td>
</tr>
<tr>
<td><code>1015</code></td>
<td>400</td>
<td>Invalid delete payload</td>
<td>Delete request body is malformed</td>
<td>Verify the body includes <code>resource_type</code> and <code>resource_id</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="error-1007-note">Error 1007 note</h3>
@markup("md", "content/.markup/bodies/12766.md")
</aside>
<h2 id="resource-not-found-behavior">Resource not found behavior</h2>
<p>In the current beta, <code>GET /accounts/{account_id}/tags</code> returns <code>500 Internal Server Error</code> for resources that do not exist or have never been tagged:</p>
<pre><code>&quot;resource not found: type={resource_type} id={resource_id}&quot;&#10;</code></pre>
<p>List endpoints (<code>/tags/resources</code>, <code>/tags/keys</code>, <code>/tags/values/{key}</code>) return <code>200 OK</code> with an empty result array when no matches are found -- this is expected, not an error.</p>
<p>This <code>500</code> behavior is a known beta limitation and may change to <code>404</code> in a future release.</p>
