<p>After onboarding your IP prefixes to Magic Transit, verify that your DDoS protection layers are active and correctly configured. Magic Transit includes multiple mitigation systems that work together. For a description of each layer and the execution order, refer to <a href="/magic-transit/ddos/">DDoS protection</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, make sure you have completed the following:</p>
<ul>
<li><a href="/magic-transit/get-started/">Onboarded your IP prefixes</a> to Magic Transit.</li>
<li><a href="/magic-transit/how-to/advertise-prefixes/">Advertised your prefixes</a> to Cloudflare.</li>
</ul>
<h2 id="verify-ddos-managed-rulesets">Verify DDoS managed rulesets</h2>
<p>The <a href="/ddos-protection/managed-rulesets/network/">network-layer DDoS managed ruleset</a> is always enabled on IP prefixes onboarded to Magic Transit. You cannot turn it off, but you can customize the sensitivity level and action for individual rules.</p>
<p>To review your current configuration:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>L3/4 DDoS protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Network-layer DDoS Protection</strong> tab.</li>
</ol>
<p>If you have not deployed any overrides, the managed ruleset runs with default settings (High sensitivity, DDoS Dynamic action). This is the recommended configuration for most deployments.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10653.md")
</aside>
<h2 id="verify-advanced-tcp-and-dns-protection">Verify Advanced TCP and DNS Protection</h2>
<p>Advanced TCP Protection and Advanced DNS Protection are automatically enabled in monitoring mode for new Magic Transit customers. In monitoring mode, the systems learn your traffic patterns and show what they would have mitigated without affecting live traffic.</p>
<p>To check the status of Advanced DDoS systems:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>L3/4 DDoS protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Advanced Protection</strong> &gt; <strong>General settings</strong>.</li>
<li>Verify that the system is turned on and that your prefixes are listed.</li>
</ol>
<p>To review individual protection rules:</p>
<ul>
<li>For Advanced TCP Protection, go to <strong>Advanced Protection</strong> &gt; <strong>Advanced TCP Protection</strong>. Check that SYN Flood Protection and Out-of-state TCP Protection rules exist and are set to the expected mode.</li>
<li>For Advanced DNS Protection, go to <strong>Advanced Protection</strong> &gt; <strong>Advanced DNS Protection</strong>. Check that a DNS Protection rule exists.</li>
</ul>
<h3 id="switch-from-monitoring-to-mitigation-mode">Switch from monitoring to mitigation mode</h3>
<p>After your Advanced DDoS systems have collected at least seven days of traffic data, Cloudflare calculates protection thresholds based on the 95th percentile of your traffic over that period. Thresholds are recalculated every 10 minutes.</p>
<p>To switch from monitoring to mitigation:</p>
<ol>
<li>Review your traffic in <a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> to confirm the systems are correctly identifying normal versus anomalous traffic.</li>
<li>Go to the rule you want to update (SYN Flood, Out-of-state TCP, or DNS Protection).</li>
<li>Change the rule mode from <strong>Monitoring</strong> to <strong>Mitigation (Enabled)</strong>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10652.md")
</aside>
<h2 id="set-up-alerts">Set up alerts</h2>
<p>Configure DDoS alerts so you are notified when attacks are detected and mitigated:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong>.</li>
<li>Select <strong>Layer 3/4 DDoS Attack Alert</strong>. Enterprise accounts can select <strong>Advanced Layer 3/4 DDoS Attack Alert</strong> for additional filtering support.</li>
<li>Configure your delivery method (email, webhook, or PagerDuty).</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10651.md")
</aside>
<p>Magic Transit and Spectrum BYOIP customers automatically receive a weekly DDoS summary report by email every Tuesday. The report covers the previous Monday-to-Sunday period and includes total attacks, the largest attack by packets per second and bits per second, and total bytes mitigated.</p>
<h2 id="monitor-with-network-analytics">Monitor with Network Analytics</h2>
<p><a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> is the primary dashboard for monitoring DDoS activity on your Magic Transit prefixes. It shows traffic entering and leaving the Cloudflare network, including traffic blocked by DDoS rules and Network Firewall rules.</p>
<p>To review DDoS activity:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Filter by mitigations applied to isolate traffic blocked by DDoS managed rulesets or Network Firewall rules.</li>
</ol>
<p>You can also query DDoS analytics programmatically using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<h2 id="test-your-ddos-protection">Test your DDoS protection</h2>
<p>You can simulate DDoS attacks against your own Magic Transit-protected IP prefixes to verify that detection and mitigation work as expected. You do not need permission from Cloudflare to test against your own properties.</p>
<p>For guidance on testing, refer to <a href="/ddos-protection/reference/simulate-ddos-attack/">Simulate test DDoS attacks</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10650.md")
</aside>
