<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests by autonomous system number (ASN), continent, or country of origin.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>AS Num</td>
<td>equals</td>
<td><code>131279</code></td>
<td>Or</td>
</tr>
<tr>
<td>Continent</td>
<td>equals</td>
<td><code>Asia</code></td>
<td>Or</td>
</tr>
<tr>
<td>Country</td>
<td>equals</td>
<td><code>Korea, North</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.asnum eq 131279) or (ip.src.continent eq &quot;AS&quot;) or (ip.src.country eq &quot;KP&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/block-traffic-from-specific-countries/">Use case: Block traffic from specific countries</a></li>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/">Use case: Allow traffic from specific countries only</a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/?field-category=Geolocation">Fields reference: Geolocation</a></li>
</ul>
