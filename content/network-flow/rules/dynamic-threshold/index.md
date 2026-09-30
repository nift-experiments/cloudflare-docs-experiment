<p>A dynamic threshold rule (beta) monitors your network traffic patterns and automatically adjusts the Distributed Denial of Service (DDoS) threshold based on traffic history. Network Flow (formerly Magic Network Monitoring) compares total traffic across all IP prefixes and addresses in the rule against the dynamic threshold, measured in bits or packets per second. If traffic exceeds the threshold, Network Flow sends an alert.</p>
<p>To use dynamic threshold rules, you must send NetFlow or sFlow data to Cloudflare. You can only configure dynamic threshold rules through the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Network Flow Rules API</a> — they are not available in the dashboard.</p>
<h2 id="rule-configuration-fields">Rule configuration fields</h2>
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Rule name</strong></td>
<td align="left">Must be unique and cannot contain spaces. Supports characters <code>A-Z</code>, <code>a-z</code>, <code>0-9</code>, underscore (<code>_</code>), dash (<code>-</code>), period (<code>.</code>), and tilde (<code>~</code>). Maximum of 256 characters.</td>
</tr>
<tr>
<td align="left"><strong>Rule type</strong></td>
<td align="left">zscore</td>
</tr>
<tr>
<td align="left"><strong>Target</strong></td>
<td align="left">Can be defined in either bits per second or packets per second.</td>
</tr>
<tr>
<td align="left"><strong>Sensitivity</strong></td>
<td align="left">Controls how easily traffic anomalies trigger alerts. Available values: low, medium, and high. Higher sensitivity triggers alerts on smaller deviations from normal traffic.</td>
</tr>
<tr>
<td align="left"><strong>Auto-advertisement</strong></td>
<td align="left">If you are a <a href="/magic-transit/on-demand">Magic Transit On Demand</a> customer, you can enable this feature to automatically enable Magic Transit if the rule's dynamic threshold is triggered. Network Flow supports Magic Transit's supernet capability. To learn more refer to <a href="/network-flow/rules/#rule-auto-advertisement">Auto-Advertisement section</a>.</td>
</tr>
<tr>
<td align="left"><strong>Rule IP prefix</strong></td>
<td align="left">The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as <code>160.168.0.1/24</code>. The maximum is 5,000 unique CIDR entries. To learn more and review an example, refer to the <a href="/network-flow/rules/#rule-ip-prefixes">Rule IP prefixes</a> section.</td>
</tr>
</tbody>
</table>
<h2 id="api-documentation">API documentation</h2>
<p>To review an example API configuration call using CURL and the expected output for a successful response, go to the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Rules</a> section in the Network Flow API documentation.</p>
<h2 id="how-the-dynamic-rule-threshold-is-calculated">How the dynamic rule threshold is calculated</h2>
<p>Z-score compares short-term traffic patterns (five-minute window) against long-term baselines (four-hour window) to detect anomalies. The threshold adjusts automatically as your traffic history grows.</p>
<p>Z-Score is calculated by using the following formula:</p>
<pre><code class="language-txt">Z = (X - μ) / σ&#10;</code></pre>
<ul>
<li><code>X</code> = Current traffic value.</li>
<li><code>μ</code> = Mean traffic value over the long window.</li>
<li><code>σ</code> = Standard deviation over the long window.</li>
</ul>
