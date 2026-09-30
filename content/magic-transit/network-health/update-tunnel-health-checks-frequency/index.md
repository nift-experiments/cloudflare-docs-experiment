<p>By default, Cloudflare servers send <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10632.md")
</div> to each <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/10633.md")
</div>, Cloudflare Network Interconnect (CNI), or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/10634.md")
</div> tunnel endpoint you configure to receive traffic from Magic Transit.
<p>You can configure the health check frequency through the dashboard or <a href="/api/resources/magic_transit/subresources/gre_tunnels/methods/update/">the API</a> to suit your use case. For example, if you are connecting a lower-traffic site that does not need immediate failover and you prefer a lower volume of health check traffic, set the frequency to <code>low</code>. On the other hand, if you are connecting a site that is extremely sensitive to any issues and you want proactive failover at the earliest sign of a potential problem, set this to <code>high</code>.</p>
<p>Available options are <code>low</code>, <code>mid</code>, and <code>high</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10637.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10631.md")
</aside>
