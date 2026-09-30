<h2 id="mode-transition-behavior">Mode transition behavior</h2>
<p>Advanced TCP Protection rules have three execution modes: <strong>Disabled</strong>, <strong>Monitoring</strong> (logs only, no drops), and <strong>Mitigation (Enabled)</strong> (active mitigation).</p>
<p>Always transition from Monitoring mode to Mitigation (Enabled) mode. Do not switch directly from Disabled to Mitigation (Enabled).</p>
<p>When you switch directly from Disabled to Mitigation (Enabled), Advanced TCP Protection begins a learning period to observe existing connection state. Long-lived connections that pre-date this learning period may be dropped because they have no state in the tracker.</p>
<p><strong>Recommended procedure:</strong></p>
<ol>
<li>Set to <strong>Monitoring</strong> mode for at least 4 hours (longer if your network has long-lived connections).</li>
<li>Review the Monitoring mode logs in <a href="/analytics/network-analytics/">Network Analytics</a> to confirm legitimate traffic patterns.</li>
<li>Switch to <strong>Mitigation (Enabled)</strong> mode.</li>
</ol>
<h2 id="legitimate-traffic-is-being-dropped-false-positives">Legitimate traffic is being dropped (false positives)</h2>
<p>Check the <strong>Mitigation reason</strong> field in the <strong>Advanced TCP Protection</strong> tab of <a href="/analytics/network-analytics/">Network Analytics</a> and use the reason to identify the cause:</p>
<table>
<thead>
<tr>
<th>Mitigation reason</th>
<th>Likely cause</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Not found</strong></td>
<td>Learning period was incomplete, or long-lived connections pre-date ATP activation</td>
<td>Set to Monitoring mode for 4+ hours, then switch to Mitigation (Enabled)</td>
</tr>
<tr>
<td><strong>Unexpected</strong></td>
<td>ECMP rehashing — packets from the same flow arriving at different Cloudflare data centers</td>
<td>Set to Monitoring mode; increase burst sensitivity threshold for affected colos; escalate if persistent</td>
</tr>
<tr>
<td><strong>Out of sequence</strong></td>
<td>Packet reordering or packet loss in the network path</td>
<td>Increase burst sensitivity threshold for the affected colo</td>
</tr>
<tr>
<td>Drops during traffic spikes only</td>
<td>Burst sensitivity threshold too low</td>
<td>Increase burst sensitivity (keep rate sensitivity the same)</td>
</tr>
</tbody>
</table>
<p><strong>Threshold tuning:</strong> Adjust burst sensitivity before rate sensitivity. Burst sensitivity handles momentary spikes; rate sensitivity controls sustained packet rates.</p>
<h2 id="traffic-from-known-sources-is-being-challenged">Traffic from known sources is being challenged</h2>
<p>The ATP allowlist allows you to bypass mitigation for specific source IP prefixes. However:</p>
<ul>
<li>The allowlist supports approximately <strong>200 IP addresses per allowlist expression</strong>. For more information, refer to <a href="/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/">Add an IP or prefix to the allowlist</a>.</li>
<li>The allowlist is <strong>not a security control</strong> — it is bypass-by-IP-address, which is vulnerable to IP address spoofing. Do not add large IP ranges (for example, entire data center IP blocks) to the allowlist.</li>
<li>For large-scale legitimate traffic sources, prefer adjusting rule sensitivities rather than adding broad allowlist entries.</li>
</ul>
<h2 id="known-limitations">Known limitations</h2>
<ul>
<li><strong>TCP only:</strong> Advanced TCP Protection covers TCP traffic. UDP and ICMP flood attacks are handled by <a href="/ddos-protection/managed-rulesets/">HTTP DDoS Attack Protection managed rulesets</a> or <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> rules.</li>
<li><strong>ECMP &quot;shifty flows&quot;:</strong> When packets from the same TCP flow arrive at different Cloudflare data centers (due to ECMP load balancing upstream), ATP loses connection state and may drop packets with the <strong>Unexpected</strong> mitigation reason. This is a known architecture constraint. Mitigation: reduce burst sensitivity or adjust per-colo thresholds for affected colos.</li>
</ul>
<h2 id="attacks-not-being-blocked-false-negatives">Attacks not being blocked (false negatives)</h2>
<ol>
<li>Confirm the rule mode is <strong>Mitigation (Enabled)</strong>, not <strong>Monitoring</strong> — Monitoring mode logs but does not drop.</li>
<li>Check that rule sensitivities are set appropriately for the attack traffic volume. Lower sensitivity means more traffic must exceed the threshold before mitigation triggers.</li>
<li>For distributed attacks spread across many source IPs and colos: adjust per-colo thresholds for the top-traffic colos.</li>
<li>Confirm filters are not bypassing the mitigation — a filter that matches attack traffic will override the rule's execution mode.</li>
</ol>
