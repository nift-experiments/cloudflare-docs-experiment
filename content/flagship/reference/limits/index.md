<p>Flagship enforces the following limits.</p>
<h2 id="platform-limits">Platform limits</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Apps per account</td>
<td>10,000</td>
</tr>
<tr>
<td>Flags per app</td>
<td>5,000</td>
</tr>
<tr>
<td>Flag, app, and variant keys</td>
<td>64 chars</td>
</tr>
<tr>
<td>Condition attribute names</td>
<td>64 chars</td>
</tr>
<tr>
<td>Condition string values</td>
<td>256 chars</td>
</tr>
<tr>
<td>Variant value size</td>
<td>10 KB</td>
</tr>
<tr>
<td>Condition nesting depth</td>
<td>5 levels</td>
</tr>
<tr>
<td>Flag description</td>
<td>512 chars</td>
</tr>
<tr>
<td>Flag configuration size per app</td>
<td>25 MB</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8730.md")
</aside>
<h2 id="notes">Notes</h2>
<ul>
<li>Condition nesting depth counts from the top-level condition group. A flat list of conditions (no nesting) has a depth of 1.</li>
<li>Flag keys, app names, condition set names, and variant keys can contain letters, numbers, hyphens, and underscores.</li>
<li>All variants on a flag must use the same value type: boolean, string, number, or JSON.</li>
<li>Flag configuration size refers to the total serialized size of all flags within a single app, including their variants and rules.</li>
</ul>
