<p>Managed rulesets are preconfigured rulesets provided by Cloudflare that you can deploy. Only Cloudflare can modify these rulesets.</p>
<p>The rules in a managed ruleset have a default configuration. However, you can define <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> that change this default configuration.</p>
<p>Several Cloudflare products include managed rulesets:</p>
<ul>
<li><a href="/waf/managed-rules/">Web Application Firewall (WAF)</a></li>
<li><a href="/ddos-protection/managed-rulesets/">DDoS Protection</a></li>
<li><a href="/cloudflare-network-firewall/how-to/enable-managed-rulesets/">Cloudflare Network Firewall</a></li>
</ul>
<p>Check each product's documentation for details on the available managed rulesets.</p>
<h2 id="more-resources">More resources</h2>
<p>To view available managed rulesets, refer to <a href="/ruleset-engine/basic-operations/view-rulesets/">View rulesets</a>.</p>
<p>To deploy a managed ruleset to a phase, refer to <a href="/ruleset-engine/managed-rulesets/deploy-managed-ruleset/">Deploy a managed ruleset</a>.</p>
<p>To adjust the behavior of a managed ruleset, do one of the following:</p>
<ul>
<li>Customize the behavior of one or more rules by using <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a>.</li>
<li>Skip one or more managed rules by adding <a href="/ruleset-engine/managed-rulesets/create-exception/">exceptions</a>.</li>
</ul>
<p>Exceptions (only supported by the WAF) have priority over overrides.</p>
