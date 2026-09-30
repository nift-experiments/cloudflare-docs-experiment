<p>The following limits apply to accounts, indexes, and vectors:</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/15262.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Current Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Indexes per account</td>
<td>50,000 (Workers Paid) / 100 (Free)</td>
</tr>
<tr>
<td>Maximum dimensions per vector</td>
<td>1536 dimensions, 32 bits precision</td>
</tr>
<tr>
<td>Precision per vector dimension</td>
<td>32 bits (float32)</td>
</tr>
<tr>
<td>Maximum vector ID length</td>
<td>64 bytes</td>
</tr>
<tr>
<td>Metadata per vector</td>
<td>10KiB</td>
</tr>
<tr>
<td>Maximum returned results (<code>topK</code>) with values or metadata</td>
<td>50</td>
</tr>
<tr>
<td>Maximum returned results (<code>topK</code>) without values and metadata</td>
<td>100</td>
</tr>
<tr>
<td>Maximum upsert batch size (per batch)</td>
<td>1000 (Workers) / 5000 (HTTP API)</td>
</tr>
<tr>
<td>Maximum vectors in a list-vectors page</td>
<td>1000</td>
</tr>
<tr>
<td>Maximum index name length</td>
<td>64 bytes</td>
</tr>
<tr>
<td>Maximum vectors per index</td>
<td>20,000,000</td>
</tr>
<tr>
<td>Maximum namespaces per index</td>
<td>50,000 (Workers Paid) / 1000 (Free)</td>
</tr>
<tr>
<td>Maximum namespace name length</td>
<td>64 bytes</td>
</tr>
<tr>
<td>Maximum vectors upload size</td>
<td>100 MB</td>
</tr>
<tr>
<td>Maximum metadata indexes per Vectorize index</td>
<td>10</td>
</tr>
<tr>
<td>Maximum indexed data per metadata index per vector</td>
<td>64 bytes</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>Limits for V1 indexes (deprecated)</summary><div class="nb-details-body">
@input("content/.markup/bodies/15263.md")
</div></details>
