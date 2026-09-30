<p>By default, Cloudflare servers send <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5694.md")
</div> to each <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5695.md")
</div>, Cloudflare Network Interconnect (CNI), or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5696.md")
</div> tunnel endpoint you configure to receive traffic from Cloudflare WAN.
<p>For Cloudflare One Appliance (formerly Magic WAN Connector), Cloudflare sends health checks to IPsec tunnel endpoints.</p>
<p>You can configure the health check frequency through the dashboard or <a href="/api/resources/magic_transit/subresources/gre_tunnels/methods/update/">the API</a> to suit your use case. For example, if you are connecting a lower-traffic site that does not need immediate failover and you prefer a lower volume of health check traffic, set the frequency to <code>low</code>. On the other hand, if you are connecting a site that is extremely sensitive to any issues and you want proactive failover at the earliest sign of a potential problem, set this to <code>high</code>.</p>
<p>Available options are <code>low</code>, <code>mid</code>, and <code>high</code>.</p>
<p>To configure health checks frequency in Cloudflare One Appliance, refer to <a href="#configure-connector">Configure Connector</a></p>
<h2 id="manual-configuration">Manual configuration</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5699.md")
</div></div>
<h2 id="configure-connector">Configure Connector</h2>
<ol>
<li>
<p>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Networks</strong>.</p>
</li>
<li>
<p>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong>.</p>
</li>
<li>
<p>In <strong>Profiles</strong>, find the Connector profile you want to edit &gt; select the three dots &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>In <strong>Network Configuration</strong> &gt; <strong>WAN configuration</strong> &gt; select your WAN &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>Change the <strong>Health check rate</strong> to your desired rate.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5693.md")
</aside>
