<p>Cloudflare Network Firewall rules are performed after Cloudflare's DDoS mitigations have been applied. The two systems are independent, and therefore, permitting traffic inside Cloudflare Network Firewall does not allow it within our DDoS mitigations. Traffic can still be blocked by DDoS mitigations that are applied first in the flow through Cloudflare's systems.</p>
<p>By default, Cloudflare Network Firewall policies allow all traffic until explicitly blocked by a rule. If no policy is configured, all traffic is permitted after DDoS mitigations have been applied.</p>
<h2 id="security-policy">Security policy</h2>
<p>You have two options for configuring a security policy:</p>
<ul>
<li>Enforce a positive security model, which blocks everything and creates allow rules for specific required traffic.</li>
<li>Begin with a minimal ruleset to block specific traffic and, by default, everything else is permitted.</li>
</ul>
<p>Traffic is matched in order of the configured rules. As soon as traffic is matched by an enabled rule, it is no longer validated against the later rules. Disabled rules are skipped entirely — traffic is not evaluated against them. In the dashboard under <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>, rule order begins from the top and flows down your list of rules.</p>
<p>For example, permitting all TCP traffic in a rule #4 would mean all TCP traffic is permitted. A rule #5 to block traffic for IP address <code>x.x.x.x</code> would not be checked.</p>
<p>For best practices when configuring your security policy, refer to <a href="/cloudflare-network-firewall/best-practices/">Best practices</a>.</p>
<h2 id="packet-filtering-policies-and-magic-transit-endpoint-health-checks">Packet filtering policies and Magic Transit endpoint health checks</h2>
<p>Cloudflare-sourced traffic is also subject to the Cloudflare Network Firewall rules you configure. If you block all ICMP traffic, you will also block Cloudflare's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6409.md")
</div>. When blocking ICMP traffic, ensure your rules first allow ICMP sourced from Cloudflare public IPs to your prefix endpoint IPs before applying a block ICMP rule.
<p>For a list of Cloudflare's public IPs, refer to <a href="https://www.cloudflare.com/ips/">IP Ranges</a>.</p>
<h2 id="cloudflare-network-firewall-phases">Cloudflare Network Firewall phases</h2>
<p>Traffic is processed in two phases: first against your Custom rules, then against Cloudflare's Managed rules.</p>
<h3 id="custom-phase-ruleset">Custom phase ruleset</h3>
<p>The Custom phase is a set of rules you define and control. You can customize the expression, order, and actions of these rules.</p>
<p>Cloudflare Network Firewall evaluates custom policies before managed policies in the order of precedence. Therefore, if traffic meets the conditions from a custom policy first, that is the action Cloudflare Network Firewall will take.</p>
<p>The actions available for a custom rule are <strong>Block</strong> or <strong>Skip</strong> (allow).</p>
<h3 id="managed-phase-ruleset">Managed phase ruleset</h3>
<p>Managed phase rulesets are maintained by Cloudflare and contain rules based on best practices, known malicious patterns, and other threat intelligence.</p>
<p>Cloudflare maintains the expressions and order of execution for rules in the Managed phase. You can enable, disable, or set individual rules to log matching packets.</p>
<p>Refer to <a href="/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/">Enable managed rulesets</a> for more information.</p>
