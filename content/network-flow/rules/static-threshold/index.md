<p>A static threshold rule monitors your network traffic against a fixed threshold you define, measured in bits or packets per second. Network Flow (formerly Magic Network Monitoring) compares total traffic across all IP prefixes and addresses in the rule against this threshold. If traffic exceeds the threshold for the configured duration, Network Flow sends an alert.</p>
<p>To use static threshold rules, you must send NetFlow or sFlow data to Cloudflare.</p>
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
<td align="left">threshold</td>
</tr>
<tr>
<td align="left"><strong>Rule threshold type</strong></td>
<td align="left">Can be defined in either bits per second or packets per second.</td>
</tr>
<tr>
<td align="left"><strong>Rule threshold</strong></td>
<td align="left">The number of bits per second or packets per second for the rule alert. When this value is exceeded for the rule duration, an alert notification is sent. Minimum of <code>1</code> and no maximum.</td>
</tr>
<tr>
<td align="left"><strong>Rule duration</strong></td>
<td align="left">The amount of time in minutes the rule threshold must exceed to send an alert notification. Choose from the following values: <code>1</code>, <code>5</code>, <code>10</code>, <code>15</code>, <code>20</code>, <code>30</code>, <code>45</code>, or <code>60</code> minutes.</td>
</tr>
<tr>
<td align="left"><strong>Auto-advertisement</strong></td>
<td align="left">If you are a Magic Transit On Demand customer, you can enable this feature to automatically enable Magic Transit if the rule alert is triggered. Network Flow (formerly Magic Network Monitoring) supports Magic Transit's supernet capability. To learn more refer to <a href="#rule-auto-advertisement">Auto-Advertisement section</a>.</td>
</tr>
<tr>
<td align="left"><strong>Rule IP prefix</strong></td>
<td align="left">The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as <code>160.168.0.1/24</code>. Max is 5,000 unique CIDR entries. To learn more, refer to <a href="#rule-ip-prefixes">Rule IP prefixes</a>.</td>
</tr>
</tbody>
</table>
<h2 id="api-documentation">API documentation</h2>
<p>To review an example static threshold rule, go to the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Rules</a> section in the Network Flow API documentation.</p>
<h2 id="recommended-rule-configuration">Recommended rule configuration</h2>
<p>Follow the guidelines in <a href="#rule-ip-prefixes">Rule IP prefixes</a>, <a href="#rule-threshold">Rule threshold</a>, and <a href="#rule-duration">Rule duration</a> to create appropriate Network Flow rules and set accurate thresholds.</p>
<h3 id="rule-ip-prefixes">Rule IP prefixes</h3>
<p>Cloudflare recommends starting with one Network Flow rule for each public <code>/24</code> IP prefix in your network. Including the range of the <code>/24</code> prefix in the rule name makes it easier to find and filter in Network Flow analytics.</p>
<p>As you become more familiar with traffic patterns across each prefix, create more specific rules with IP prefixes smaller or larger than <code>/24</code> depending on your needs. You can also combine multiple IP prefixes in a single rule.</p>
<h3 id="rule-threshold">Rule threshold</h3>
<p>Follow the steps in <a href="#initial-rule-configuration">Initial rule configuration</a> and <a href="#setting-the-appropriate-threshold">Setting the appropriate threshold</a> to configure appropriate rule thresholds.</p>
<h4 id="initial-rule-configuration">Initial rule configuration</h4>
<p>When you first configure Network Flow, you may not know the typical traffic patterns for each IP prefix. Set an initial threshold high enough that it is unlikely to trigger during setup — Cloudflare recommends 10 Gbps or 10 Mpps.</p>
<p>This lets you collect baseline traffic data without receiving alerts. After configuring your initial rules, monitor for alerts and review traffic in Network Flow Analytics. Over time, update each rule's threshold based on historical traffic data.</p>
<table>
<thead>
<tr>
<th align="left">Threshold type</th>
<th align="left">Recommended rule threshold to collect initial data</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Bits</td>
<td align="left">10 Gbps (10,000,000,000 bits per second)</td>
</tr>
<tr>
<td align="left">Packets</td>
<td align="left">10 Mpps (10,000,000 packets per second)</td>
</tr>
</tbody>
</table>
<h4 id="setting-the-appropriate-threshold">Setting the appropriate threshold</h4>
<p>After creating the initial set of rules to monitor your network traffic, you should collect 14-30 days of historical traffic volume data for each rule.</p>
<p>Cloudflare recommends that you set a rule threshold that is two times larger than the maximum non-attack traffic observed for a one minute time interval within a Network Flow rule.</p>
<p>To find the maximum non-attack traffic for a one minute time interval over the past 14-30 days, filter for the specific rule you want to analyze:</p>
<ol>
<li>Go to the <strong>Network flow</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add filter</strong>.</li>
<li>In <strong>New filter</strong>, use the drop-down menus to create the following filter:</li>
</ol>
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Operator</th>
<th align="left">Rule name</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><em>Monitoring Rule</em></td>
<td align="left"><em>equals</em></td>
<td align="left"><code>&lt;RULE_NAME&gt;</code></td>
</tr>
</tbody>
</table>
<p>Once the rule filter is selected in Network Flow Analytics, you can check the historical traffic volume data for the rule over the selected time period. Cloudflare recommends reviewing historical data in seven-day increments, since that is the largest window that shows one-hour time intervals. To select a custom seven-day range, go to the top right corner of Network Flow analytics, open the time window drop-down menu, and select <strong>Custom range</strong>.</p>
<p>You should review the selected seven-day time range and identify the largest traffic volume peak. Then, click and drag on the largest traffic peak to view the traffic volume data for a smaller time window. Continue until you are viewing the traffic volume data in one-minute intervals.</p>
<p>Record the largest traffic volume peak for the rule in a spreadsheet, then repeat this process across 14-30 days of data. The rule threshold should be updated to be two times the largest traffic spike for a one minute time interval across 14-30 days of data. You should go through this process to set the threshold for each Network Flow rule.</p>
<h3 id="rule-duration">Rule duration</h3>
<p>Your IP prefixes may experience inconsistent spikes across one-minute intervals. Set a rule duration of at least two minutes to reduce false positive alerts from short-term non-malicious traffic spikes. A two-minute duration means traffic must stay above the threshold for two minutes before an alert fires.</p>
<h3 id="adjusting-rules-over-time">Adjusting rules over time</h3>
<p>After updating your first set of thresholds based on historical data, monitor for Network Flow alerts to verify the thresholds are appropriate. Adjust thresholds and duration over time to find the right alert sensitivity for your network environment.</p>
