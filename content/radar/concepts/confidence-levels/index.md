<p>The <code>result.meta.confidenceInfo.level</code> in the response provides an indication of how much confidence Cloudflare has in the data. Confidence levels can be affected either by internal issues affecting data quality or by not having a lot of data for a given location (like Antarctica) or Autonomous System (AS).</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>There is not enough data in this time range and/or for this location or Autonomous System. Data also exhibits an erratic pattern, possibly due to the reasons previously mentioned.</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>There is not enough data in this timerange and/or in this location or Autonomous System.</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Data exhibits an erratic pattern but is not affected by known data issues (like pipeline issues).</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Unassigned.</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td>No known data quality issues.</td>
</tr>
</tbody>
</table>
