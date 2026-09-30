<p>An sFlow DDoS attack rule (beta) alerts you when a DDoS attack is detected in your network traffic. Network Flow (formerly Magic Network Monitoring) uses the same DDoS detection rules that protect Cloudflare's global network to identify these attacks.</p>
<p>To use sFlow DDoS attack rules, you must send sFlow data to Cloudflare. You can only configure these rules through the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Network Flow Rules API</a> — they are not available in the dashboard.</p>
<h2 id="send-sflow-data-from-your-network-to-cloudflare">Send sFlow data from your network to Cloudflare</h2>
<p>To send sFlow data to Cloudflare, your router must support sFlow exports. Refer to <a href="/network-flow/routers/supported-routers/">Supported routers</a> to verify compatibility, and <a href="/network-flow/routers/sflow-config/">Configure sFlow</a> for setup instructions.</p>
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
<td align="left">advanced_ddos</td>
</tr>
<tr>
<td align="left"><strong>Prefix Match</strong></td>
<td align="left">The field <code>prefix_match</code> determines how IP matches are handled. <br/><br/><strong>Subnet</strong> (recommended): Automatically advertise if the attacked IPs are within a subnet of a public IP prefix that can be advertised by Magic Transit.<br/><br/><strong>Exact</strong>: Automatically advertise if the attacked IPs are an exact match with a public IP prefix that can be advertised by Magic Transit.<br/><br/><strong>Supernet</strong>: Automatically advertise if the attacked IPs are a supernet of a public IP prefix that can be advertised by Magic Transit.</td>
</tr>
<tr>
<td align="left"><strong>Auto-advertisement</strong></td>
<td align="left">If you are a <a href="/magic-transit/on-demand">Magic Transit On Demand</a> customer, you can enable this feature to automatically enable Magic Transit if the rule's dynamic threshold is triggered. To learn more, refer to <a href="/network-flow/rules/#rule-auto-advertisement">Auto-advertisement</a>.</td>
</tr>
<tr>
<td align="left"><strong>Rule IP prefix</strong></td>
<td align="left">The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as <code>160.168.0.1/24</code>. The maximum is 5,000 unique CIDR entries. To learn more and see an example, refer to <a href="/network-flow/rules/#rule-ip-prefixes">Rule IP prefixes</a>.</td>
</tr>
</tbody>
</table>
<h2 id="api-documentation">API documentation</h2>
<p>Refer to the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Rules API documentation</a> to review an example API configuration call using CURL and the expected output for a successful response.</p>
<h2 id="tune-the-sflow-ddos-alert-thresholds">Tune the sFlow DDoS alert thresholds</h2>
<p>You can tune the thresholds of your sFlow DDoS alerts in the dashboard and via the Cloudflare API by following the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a> guide.</p>
