<p>Your router <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10838.md")
</div> the traffic that passes through it to create <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/10839.md")
</div> or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/10840.md")
</div> data. The sampling rate determines how frequently your router captures a packet — for example, a rate of 1 in 100 means your router captures one out of every 100 packets.
<p>Sampling more frequently (lower ratios like 1 in 100) produces more accurate flow data but uses more router memory and CPU. Sampling less frequently (higher ratios like 1 in 4,000) reduces resource usage and is suitable for networks with larger traffic volumes.</p>
<p>The following table provides general recommendations based on your traffic volume. Test different sampling rates to find the best option for your network.</p>
<table>
<thead>
<tr>
<th>Traffic Volume</th>
<th>Router sampling recommendation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Low</td>
<td>Between 1 in 100 packets - 1 in 500 packets</td>
</tr>
<tr>
<td>Medium</td>
<td>Between 1 in 1,000 - 1 in 2,000 packets</td>
</tr>
<tr>
<td>High</td>
<td>Between 1 in 2,000 - 1 in 4,000 packets</td>
</tr>
</tbody>
</table>
<p>As a general rule, you may notice a loss in data accuracy (depending on your network volume) when your network flow sampling rate exceeds 1 in 5,000 packets.</p>
