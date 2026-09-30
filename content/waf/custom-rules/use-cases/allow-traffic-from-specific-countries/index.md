<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests based on country code using the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.country/"><code>ip.src.country</code></a> field, only allowing requests from two countries: United States and Mexico.</p>
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
<td>is not in</td>
<td><code>Mexico</code>, <code>United States</code></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(not ip.src.country in {&quot;US&quot; &quot;MX&quot;})</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/block-by-geographical-location/">Use case: Block traffic by geographical location</a></li>
<li><a href="/waf/custom-rules/use-cases/block-traffic-from-specific-countries/">Use case: Block traffic from specific countries</a></li>
</ul>
