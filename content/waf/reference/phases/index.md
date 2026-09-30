<p>The Web Application Firewall provides the following <a href="/ruleset-engine/about/phases/">phases</a> where you can create rulesets and rules:</p>
<ul>
<li><code>http_request_firewall_custom</code></li>
<li><code>http_ratelimit</code></li>
<li><code>http_request_firewall_managed</code></li>
</ul>
<p>These phases exist both at the account level and at the zone level. Considering the available phases and the two different levels, rules will be evaluated in the following order:</p>
<table>
<thead>
<tr>
<th>Security feature</th>
<th>Scope</th>
<th>Phase</th>
<th>Ruleset kind</th>
<th>Location in the dashboard</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/waf/account/custom-rulesets/">Custom rulesets</a><br/></td>
<td>Account</td>
<td><code>http_request_firewall_custom</code></td>
<td><code>custom</code> (create)<br/><code>root</code> (deploy)</td>
<td><span class="nb-dash-button"></span> &gt; <strong>Custom rulesets</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/custom-rules/">Custom rules</a></td>
<td>Zone</td>
<td><code>http_request_firewall_custom</code></td>
<td><code>zone</code></td>
<td><span class="nb-dash-button"></span></td>
</tr>
<tr>
<td><a href="/waf/account/rate-limiting-rulesets/">Rate limiting rulesets</a></td>
<td>Account</td>
<td><code>http_ratelimit</code></td>
<td><code>root</code></td>
<td><span class="nb-dash-button"></span> &gt; <strong>Rate limiting rulesets</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></td>
<td>Zone</td>
<td><code>http_ratelimit</code></td>
<td><code>zone</code></td>
<td><span class="nb-dash-button"></span></td>
</tr>
<tr>
<td><a href="/waf/account/managed-rulesets/">Managed rulesets</a></td>
<td>Account</td>
<td><code>http_request_firewall_managed</code></td>
<td><code>root</code></td>
<td><span class="nb-dash-button"></span> &gt; <strong>Managed rulesets</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/managed-rules/">Managed rules</a></td>
<td>Zone</td>
<td><code>http_request_firewall_managed</code></td>
<td><code>zone</code></td>
<td><span class="nb-dash-button"></span></td>
</tr>
</tbody>
</table>
<p>To learn more about phases, refer to <a href="/ruleset-engine/about/phases/">Phases</a> in the Ruleset Engine documentation.</p>
