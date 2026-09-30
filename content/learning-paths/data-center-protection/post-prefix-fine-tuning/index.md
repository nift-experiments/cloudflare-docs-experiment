<p>On this page, you can find suggestions to monitor your prefix advertisements and fine-tune them.</p>
<h2 id="ddos-managed-rules">DDOS Managed Rules</h2>
<h3 id="adaptive-ddos-rules">Adaptive DDOS rules</h3>
<p><a href="/ddos-protection/managed-rulesets/adaptive-protection/">These rules</a> are based on a seven-day rolling window. We recommend reviewing the logs from these adaptive rules in Network Analytics seven days after your last prefix advertisement.</p>
<p>If you see matches for legitimate traffic, consider lowering the sensitivity of the rule and then review the logs again. Once you are satisfied that legitimate traffic is not being flagged, <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/#create-a-ddos-override">create a DDoS override</a> for this rule with action as <code>DDOS Dynamic</code> or <code>Block</code>.</p>
<h3 id="advanced-tcp-protection-and-advanced-dns-protection">Advanced TCP Protection and Advanced DNS Protection</h3>
<p>For both <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> and <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a>, your Cloudflare account team will need to configure manual thresholds for your account, based on your ingress traffic.</p>
<p>Once all your prefixes are advertised and/or once all your expected traffic is cut over to the Magic Transit prefixes, reach out to your Cloudflare account team to have the thresholds configured.</p>
<p>You can then change the mode on your Advanced TCP and DNS protections from <code>monitoring</code> to <code>mitigation</code>. You can also create a filter for <code>monitoring</code> mode for any traffic flows for which you see false positives. Try to keep this specific so that the protection is enabled for other inbound traffic flows.</p>
<h2 id="cloudflare-network-firewall-rules">Cloudflare Network Firewall rules</h2>
<p>We strongly encourage you to ensure you have a Cloudflare Network Firewall ruleset configured and customized to your environment to help stop unwanted and attack traffic.</p>
<p>You can configure Cloudflare Network Firewall rules and keep them in <code>disabled</code> mode to review the traffic that would have matched, using <code>verdict = drop</code> and the rule ID within Network Analytics. Once you are satisfied that the rule is blocking/permitting the intended traffic, you can change the mode to <code>enabled</code>.</p>
<p>Refer to Cloudflare Network Firewall's <a href="/cloudflare-network-firewall/best-practices/">best practices</a> for configuration guidance and suggestions.</p>
<h2 id="alerts-for-magic-tunnel-health-checks-and-ddos">Alerts for Magic Tunnel health checks and DDoS</h2>
<ul>
<li>Ensure all teams/members needing to receive these are getting the alerts.</li>
<li>Check the Tunnel Health Check Alert configuration for Sensitivity and Alert interval and tunnels in-scope.</li>
<li>Refer to <a href="/learning-paths/data-center-protection/enable-notifications/#set-up-tunnel-health-alerts">Set up tunnel health alerts</a> and <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more details.</li>
</ul>
<h2 id="optional">Optional</h2>
<ul>
<li>Enable <a href="/logs/logpush/">Logpush</a> to your Security Information and Event Management (SIEM).</li>
<li>Enable Cloudflare Network Firewall's <a href="/cloudflare-network-firewall/about/ids/">Intrusion Detection System (IDS)</a>. Requires Logpush and is only available for accounts with <a href="/cloudflare-network-firewall/plans/#advanced-features">Cloudflare Advanced Network Firewall</a>.</li>
<li>Use <a href="/network-flow/">Network Flow</a> (formerly Magic Network Monitoring) for visibility into traffic on your non-Magic Transit prefixes, using NetFlow or sFlow from your CPEs.</li>
</ul>
