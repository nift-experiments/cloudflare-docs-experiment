<p>Cloudflare Network Firewall (formerly Magic Firewall) rules are performed after Cloudflare's DDoS mitigations have been applied. The two systems are independent, and therefore, permitting traffic inside Cloudflare Network Firewall does not allow it within our DDoS mitigations. Traffic can still be blocked by DDoS mitigations that are applied first in the flow through Cloudflare's systems.</p>
<p>By default, Cloudflare Network Firewall permits all traffic until explicitly blocked by a rule. If no rules are configured, all traffic is permitted after Cloudflare's DDoS mitigations have been applied.</p>
<h2 id="security-policy">Security policy</h2>
<p>You have two options for configuring a security policy:</p>
<ul>
<li>Enforce a positive security model and only permit required traffic and block everything else.</li>
<li>Begin with a minimal ruleset to block specific traffic and, by default, everything else is permitted.</li>
</ul>
<p>Traffic is matched in order of the configured rules. As soon as traffic is matched by an enabled rule, it is no longer validated against the later rules, and traffic will pass through disabled rules. In the dashboard under <strong>Cloudflare Network Firewall</strong>, rule order begins from the top and flows down your list of rules.</p>
<p>For example, permitting all TCP traffic in a rule #4 would mean all TCP traffic is permitted. A rule #5 to block traffic for IP address <code>x.x.x.x</code> would not be checked.</p>
<p>For best practices when configuring your security policy, refer to <a href="/cloudflare-network-firewall/best-practices/">Best practices</a>.</p>
<h2 id="cloudflare-network-firewall-rules-and-magic-transit-endpoint-health-checks">Cloudflare Network Firewall rules and Magic Transit endpoint health checks</h2>
<p>Cloudflare-sourced traffic is also subject to the Cloudflare Network Firewall rules you configure. If you block all ICMP traffic, you will also block Cloudflare's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4276.md")
</div>. When blocking ICMP traffic, ensure your rules first allow ICMP sourced from Cloudflare public IPs to your prefix endpoint IPs before applying a block ICMP rule.
<p>For a list of Cloudflare's public IPs, refer to <a href="https://www.cloudflare.com/ips/">IP Ranges</a>.</p>
<h2 id="cloudflare-network-firewall-phases">Cloudflare Network Firewall phases</h2>
<p>Cloudflare Network Firewall processes traffic in two phases: in the first phase, Cloudflare Network Firewall matches packets against rules in the Custom phase. In the second phase, Cloudflare Network Firewall matches packets against rules in the Managed phase.</p>
<h3 id="custom-phase-ruleset">Custom phase ruleset</h3>
<p>The Cloudflare Network Firewall Custom phase is a set of rules defined by the user. The expression, order, and actions of those rules can be customized by the user.</p>
<p>Additionally, users can add a rule in this custom phase to override the behavior of a rule in the Managed phase.</p>
<h3 id="managed-phase-ruleset">Managed phase ruleset</h3>
<p>Managed phase rulesets are updated and maintained by Cloudflare, and Cloudflare creates these rules based on best practices, known malicious patterns, and other criteria.</p>
<p>Cloudflare maintains the expressions and order of execution for rules in the Managed phase. Rules
can be enabled, disabled, or made to log matching packets.</p>
<p>Refer to <a href="/cloudflare-network-firewall/how-to/enable-managed-rulesets/">Enable managed rulesets</a> for more information.</p>
