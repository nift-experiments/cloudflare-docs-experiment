<p><a href="/magic-transit/on-demand/">Magic Transit On Demand</a> allows you to keep Magic Transit disabled during normal operations and activate it only when you need DDoS protection. Network Flow monitors your traffic while Magic Transit is off and detects attacks. When an attack is detected, you can enable Magic Transit automatically or manually.</p>
<p>You can create Network Flow rules that monitor specific IP <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/708.md")
</div> for DDoS attacks. When an attack is detected, Cloudflare notifies you by email, [webhook](/notifications/get-started/configure-webhooks/), or [PagerDuty](/notifications/get-started/configure-pagerduty/).
<p>If you enable <a href="#activate-ip-auto-advertisement">auto-advertisement</a> on a rule, Magic Transit activates automatically to protect the targeted prefixes. You can enable auto-advertisement for individual Network Flow rules through the dashboard or API.</p>
<p>After Magic Transit activates and your traffic flows through Cloudflare, Cloudflare blocks malicious DDoS traffic. Your origin servers receive only clean traffic through IPsec or GRE tunnels.</p>
<p>The following diagrams illustrate this process:</p>
<div class="nb-width">
@markup("md", "content/.markup/bodies/709.md")
</div>
<div class="nb-width">
@markup("md", "content/.markup/bodies/710.md")
</div>
<div class="nb-width">
@markup("md", "content/.markup/bodies/711.md")
</div>
<h2 id="activate-ip-auto-advertisement">Activate IP auto-advertisement</h2>
<p>Before a rule can automatically activate Magic Transit, you must enable IP advertisement for the relevant prefixes. You can do this through the dashboard or the API.</p>
<h3 id="dashboard">Dashboard</h3>
<p>To activate IP advertisement through the Cloudflare dashboard, refer to <a href="/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement">Configure dynamic advertisement</a>.</p>
<h3 id="api">API</h3>
<p>To activate IP advertisement through the API, refer to the <a href="/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/">IP Address Management Dynamic Advertisement API</a>.</p>
<h2 id="network-flow-rules">Network Flow rules</h2>
<p>To create Network Flow rules with auto-advertisement, refer to <a href="/network-flow/rules/#rule-auto-advertisement">Rule Auto-Advertisement</a>.</p>
