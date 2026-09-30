<p>Cloudflare Radar does not normally return raw values. Instead, values are returned as percentages or normalized using min-max.</p>
<p>Refer to the <code>result.meta.normalization</code> property in the response to check which post-processing method was applied to the raw values, if any.</p>
<h2 id="method">Method</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>PERCENTAGE</code></td>
<td>Values represent percentages.</td>
</tr>
<tr>
<td><code>PERCENTAGE_CHANGE</code></td>
<td>Values represent a <a href="https://en.wikipedia.org/wiki/Relative_change_and_difference#Percentage_change">percentage change</a> from a baseline period.</td>
</tr>
<tr>
<td><code>OVERLAPPED_PERCENTAGE</code></td>
<td>Values represent percentages that exceed 100% due to overlap.</td>
</tr>
<tr>
<td><code>MIN_MAX</code></td>
<td>Values have been normalized using <a href="https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)">min-max</a>.</td>
</tr>
<tr>
<td><code>MIN0_MAX</code></td>
<td>Values have been normalized using min-max, but setting the minimum value to <code>0</code>. Equivalent to a proportion of the maximum value in the entire response, scaled between 0 and 1.</td>
</tr>
<tr>
<td><code>RAW_VALUES</code></td>
<td>Values are raw and have not been changed.</td>
</tr>
</tbody>
</table>
<p>If you want to compare values across locations/time ranges/etc., in endpoints that normalize values using min-max, you must do so in the same request. This is done by asking for multiple series. All values will then be normalized using the same minimum and maximum value and can safely be compared against each other. Refer to <a href="/radar/get-started/making-comparisons/">Make comparisons</a> for more information.</p>
