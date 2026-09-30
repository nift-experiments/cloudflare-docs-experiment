<p>Define overrides for the Network-layer DDoS Attack Protection managed ruleset to change the action applied to a given attack or modify the sensitivity level of the detection mechanism. You can <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">define overrides in the Cloudflare dashboard</a> or <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/">define overrides via Rulesets API</a>.</p>
<p>The available parameters are the following:</p>
<ul>
<li>Action</li>
<li>Sensitivity Level</li>
</ul>
<h2 id="action">Action</h2>
<p>API property name: <code>&quot;action&quot;</code>.</p>
<p>The action performed for packets that match specific rules of Cloudflare's DDoS mitigation services. The available actions are:</p>
<ul>
<li>
<p><strong>Log</strong></p>
<ul>
<li>API value: <code>&quot;log&quot;</code>.</li>
<li>Only available on Enterprise plans. Logs requests that match the expression of a rule detecting network layer DDoS attacks. Recommended for validating a rule before committing to a more severe action.
Refer to the <a href="/analytics/network-analytics/configure/displayed-data/#view-logged-or-monitored-traffic">Analytics documentation</a> for more information on how to view logged or monitored traffic.</li>
</ul>
</li>
<li>
<p><strong>Block</strong></p>
<ul>
<li>API value: <code>&quot;block&quot;</code>.</li>
<li>Blocks IP packets that match the rule expression given the sensitivity levels.</li>
</ul>
</li>
<li>
<p><strong>DDoS Dynamic</strong></p>
<ul>
<li>API value: <em>N/A</em> (internal rule action that you cannot use in overrides).</li>
<li>Performs a specific action according to a set of internal guidelines defined by Cloudflare. The executed action can be <em>Block</em> or an undisclosed mitigation action.</li>
</ul>
</li>
</ul>
<h2 id="sensitivity-level">Sensitivity Level</h2>
<p>API property name: <code>&quot;sensitivity_level&quot;</code>.</p>
<p>Defines how sensitive a rule is. Affects the thresholds used to determine if an attack should be mitigated. A higher sensitivity level means having a lower threshold, while a lower sensitivity level means having a higher threshold.</p>
<p>The available sensitivity levels are:</p>
<table>
<thead>
<tr>
<th>UI value</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>High</em></td>
<td><code>&quot;default&quot;</code></td>
</tr>
<tr>
<td><em>Medium</em></td>
<td><code>&quot;medium&quot;</code></td>
</tr>
<tr>
<td><em>Low</em></td>
<td><code>&quot;low&quot;</code></td>
</tr>
<tr>
<td><em>Essentially Off</em></td>
<td><code>&quot;eoff&quot;</code></td>
</tr>
</tbody>
</table>
<p>The default sensitivity level is <em>High</em>.</p>
<p>In most cases, when you select the <em>Essentially Off</em> sensitivity level the rule will not trigger for any of the selected actions, including <em>Log</em>. However, if the attack is extremely large, Cloudflare's protection systems will still trigger the rule's mitigation action to protect Cloudflare's network.</p>
<p><em>Essentially Off</em> means that we have set an exceptionally low sensitivity level so in most cases traffic will not be mitigated for you. However, attack traffic will be mitigated at exceptional levels to ensure the safety and stability of the Cloudflare network.</p>
<p><strong>Log</strong> means that requests will not be mitigated but only logged and shown on the dashboard. However, attack traffic will be mitigated at exceptional levels to ensure the safety and stability of the Cloudflare network.</p>
