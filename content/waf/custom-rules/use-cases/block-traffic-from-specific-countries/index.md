<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests based on country code using the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.country/"><code>ip.src.country</code></a> field.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Country</td>
<td>is in</td>
<td><code>Korea, North</code>, <code>Syria</code></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.country in {&quot;KP&quot; &quot;SY&quot;})</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/block-by-geographical-location/">Use case: Block traffic by geographical location</a></li>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/">Use case: Allow traffic from specific countries only</a></li>
</ul>
