<h2 id="create-cipa-policy">Create CIPA policy</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Create a policy to block using the CIPA filter:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td>in</td>
<td><em>CIPA Filter</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>In <strong>Logs</strong> &gt; <strong>Gateway</strong> &gt; <strong>DNS</strong>, verify that you see the blocked domain.</li>
</ol>
<p>Your environment is now protected against all of the subcategories listed in <a href="/fundamentals/reference/policies-compliances/cybersafe/#configuration">Configuration</a>.</p>
