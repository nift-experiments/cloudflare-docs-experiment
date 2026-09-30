<p>The <a href="/waf/detections/attack-score/">attack score</a> helps identify variations of known attacks and their malicious payloads.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests based on country code (<a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format), from requests with an attack score lower than 20. For more information, refer to <a href="/waf/detections/attack-score/">WAF attack score</a>.</p>
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
<td>Country</td>
<td>is in</td>
<td><code>China</code>, <code>Taiwan</code>, <code>United Kingdom</code>, <code>United States</code></td>
<td>And</td>
</tr>
<tr>
<td>WAF Attack Score</td>
<td>less than</td>
<td><code>20</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.country in {&quot;CN&quot; &quot;TW&quot; &quot;US&quot; &quot;GB&quot;} and cf.waf.score lt 20)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
