<p>Cloudflare <a href="/ddos-protection/">DDoS protection</a> automatically detects and mitigates DDoS attacks using the <a href="/ddos-protection/about/components/#autonomous-edge">Autonomous Edge</a>. Magic Transit customers get multiple layers of protection, from always-on managed rulesets to advanced systems that you can configure for your specific traffic patterns.</p>
<h2 id="mitigation-layers">Mitigation layers</h2>
<h3 id="ddos-managed-rulesets">DDoS managed rulesets</h3>
<p>The <a href="/ddos-protection/managed-rulesets/network/">network-layer DDoS managed ruleset</a> provides pre-configured rules that detect and mitigate L3/L4 DDoS attacks. The ruleset is always enabled and cannot be turned off. Magic Transit and Spectrum Enterprise customers can <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">customize the ruleset behavior</a> by adjusting the action and sensitivity level for individual rules or groups of rules.</p>
<h3 id="advanced-tcp-protection">Advanced TCP Protection</h3>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> detects and mitigates SYN flood attacks and out-of-state TCP attacks. It uses <code>flowtrackd</code> to learn your normal TCP traffic patterns and identify anomalous flows. You can create rules scoped globally, by region, or by data center, and set each rule to monitoring or mitigation mode.</p>
<h3 id="advanced-dns-protection">Advanced DNS Protection</h3>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> detects and mitigates DNS-over-UDP DDoS attacks. Like Advanced TCP Protection, it uses <code>flowtrackd</code> to build a traffic profile and identify volumetric DNS anomalies. You can create rules with configurable burst, rate, and profile sensitivity levels.</p>
<h3 id="programmable-flow-protection">Programmable Flow Protection</h3>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> lets you write custom eBPF programs to inspect UDP payloads at the packet level. It is designed for custom or standardized L7 UDP-based protocols such as gaming, VoIP, financial services, and streaming. Programmable Flow Protection is available as an add-on for Magic Transit customers.</p>
<h3 id="network-firewall">Network Firewall</h3>
<p><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> lets you create custom packet-level firewall rules to filter traffic by protocol, port, IP address, packet length, and other attributes. Network Firewall is included with Magic Transit.</p>
<h2 id="automatic-activation">Automatic activation</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/783.md")
</aside>
<p>After the initial monitoring period, review your traffic in <a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> to observe what would have been mitigated, then switch your rules from monitoring to mitigation mode. For more information, refer to <a href="/ddos-protection/advanced-ddos-systems/overview/">Advanced DDoS Systems general settings</a>.</p>
<h2 id="execution-order">Execution order</h2>
<p>When traffic enters the Cloudflare network, it passes through mitigation systems in the following order:</p>
<ol>
<li><a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a></li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a></li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a></li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a></li>
</ol>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> operates within the Advanced DDoS Protection layer for UDP-based protocols.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/magic-transit/how-to/verify-ddos-protection/">Verify your DDoS protection</a>: Confirm that your DDoS mitigation layers are active and correctly configured.</li>
<li><a href="/ddos-protection/">DDoS Protection overview</a>: Learn about Cloudflare DDoS Protection across all products.</li>
<li><a href="/ddos-protection/best-practices/proactive-defense/">Best practices for DDoS protection</a>: Review proactive defense recommendations, including steps specific to Magic Transit.</li>
</ul>
