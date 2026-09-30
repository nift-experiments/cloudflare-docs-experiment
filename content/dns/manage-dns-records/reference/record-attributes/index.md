<p>Use DNS record comments and tags to categorize and clarify the purpose of DNS records within Cloudflare.</p>
<p>Comments provide a unique descriptions for specific records, whereas tags group similar records into categories.</p>
<p>These attributes are particularly useful when:</p>
<ul>
<li>Multiple teams are managing DNS records within the same zone.</li>
<li>Your zone contains a large number of DNS records.</li>
<li>You want to filter your DNS records based on matching attributes (for example, when they are managed by the same team or used for the same application).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7794.md")
</aside>
<hr />
<h2 id="availability">Availability</h2>
<p>Comments and tags are only supported for <a href="/dns/zone-setups/full-setup/">primary zones (full setup)</a> and <a href="/dns/zone-setups/partial-setup/">partial zones (CNAME setup)</a>.</p>
<h3 id="record-comments">Record comments</h3>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Character limit</td>
<td>100</td>
<td>500</td>
<td>500</td>
<td>500</td>
</tr>
<tr>
<td>Comments per record</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table>
<h3 id="record-tags">Record tags</h3>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Name character limit (everything before the colon)</td>
<td>N/A</td>
<td>32</td>
<td>32</td>
<td>32</td>
</tr>
<tr>
<td>Value character limit (everything after the colon)</td>
<td>N/A</td>
<td>100</td>
<td>100</td>
<td>100</td>
</tr>
<tr>
<td>Tags per record</td>
<td>N/A</td>
<td>20</td>
<td>20</td>
<td>20</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="add-or-edit-record-attributes">Add or edit record attributes</h2>
<p>Create or edit record attributes just like any other aspect of DNS records, whether through the <a href="/dns/manage-dns-records/how-to/create-dns-records/">dashboard</a> or <a href="/api/resources/dns/subresources/records/methods/create/">API</a>.</p>
<p>You can also add or edit attributes by <a href="/dns/manage-dns-records/how-to/import-and-export/#dns-record-attributes">exporting and re-importing</a> your records, or using the <a href="/dns/manage-dns-records/how-to/batch-record-changes/#use-the-api">Batch record changes API</a>.</p>
<p>When exporting and importing, special tags starting by <code>cf-</code> allow you to control specific Cloudflare configurations. On export, these tags are automatically added to reflect the current configuration for each record on your zone. Refer to <a href="/dns/manage-dns-records/how-to/import-and-export/#reserved-cf--tags">reserved cf- tags</a> for details.</p>
<hr />
<h2 id="reference">Reference</h2>
<h3 id="comments">Comments</h3>
<p>Comments are treated as <a href="https://en.wikipedia.org/wiki/Graphic_character">graphic Unicode characters</a>, meaning that they are case-sensitive and do not have any character limitations. However, comments do not support newline (<code>\n</code>) or carriage return (<code>\r</code>) characters.</p>
<h3 id="tags">Tags</h3>
<p>Tags are treated as an array of <code>name:value</code> pairs, meaning that tag names are not case-sensitive and can only contain letters, numbers, <code>-</code>, and <code>_</code>. For tag values, the same character restrictions apply as for comments.</p>
