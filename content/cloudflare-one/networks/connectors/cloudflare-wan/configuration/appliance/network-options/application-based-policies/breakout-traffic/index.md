<p>Breakout traffic allows you to define which applications should bypass Cloudflare's security filtering, and go directly to the Internet. It works via DNS requests inspection. This means that if your network is caching DNS requests, Breakout traffic will only take effect after you cache entries expire and your client issues a new DNS request that Cloudflare One Appliance (formerly Magic WAN Connector) can detect. This can take several minutes.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5806.md")
</aside>
<pre class="mermaid">&#10;&#10;	{`&#10;	flowchart LR&#10;	accTitle: Breakout traffic flow&#10;	accDescr: Applications 1 and 2 are configured to bypass Cloudflare's security filtering, and go straight to the Internet.&#10;	a(Cloudflare One Appliance) --> b(Cloudflare) -->|Filtered traffic|c(Internet)&#10;&#10;	a-- Breakout traffic ---d(Application1) & e(Application2) --> c&#10;&#10;	classDef orange fill:#f48120,color: black&#10;	class a,b orange&#10;	`}&#10;&#10;</pre>
<p><em>In the graph above, Applications 1 and 2 are configured to bypass Cloudflare's security filtering, and go straight to the Internet.</em></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5807.md")
</aside>
<h2 id="add-an-application-to-your-account">Add an application to your account</h2>
<p>Before you can add or remove Breakout traffic applications to your Cloudflare One Appliance, you need to create an account-level list with the applications that you want to configure. Currently, adding to or modifying this list is only possible via API, through the <a href="/api/resources/magic_transit/subresources/apps/methods/create/"><code>managed_app_id</code></a> endpoint.</p>
<p>To add applications to your account:</p>
<p>Send a <code>POST</code> request to add new apps to your account.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/apps \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;managed_app_id&quot;: &quot;&lt;APP_ID&gt;&quot;,&#10;  &quot;name&quot;: &quot;&lt;APP_NAME&gt;&quot;,&#10;  &quot;type&quot;: &quot;&lt;APP_TYPE&gt;&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;account_app_id&quot;: &quot;eb09v665c0784618a3e4ba9809258fd4&quot;,&#10;		&quot;name&quot;: &quot;&lt;APP_NAME&gt;&quot;,&#10;		&quot;type&quot;: &quot;&lt;APP_TYPE&gt;&quot;,&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You can now add this new app to the Breakout traffic list in your Cloudflare One Appliance.</p>
<h3 id="add-an-application-to-cloudflare-one-appliance">Add an application to Cloudflare One Appliance</h3>
<p>You need to configure Breakout traffic applications for each of your existing sites, as this is a per-site configuration.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5810.md")
</div></div>
<h3 id="delete-an-application-from-cloudflare-one-appliance">Delete an application from Cloudflare One Appliance</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5813.md")
</div></div>
<h2 id="designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</h2>
<p>You can pin applications to a specific WAN port in Cloudflare One Appliance when you need control over which WAN port your applications egress from the device. In case your preferred WAN port goes down, Cloudflare One Appliance automatically fails over to a standard configured WAN port priority.</p>
<p>With this preferred breakout port, customers have direct control over their local Internet breakout traffic. You can designate a specific WAN uplink as the primary path for your critical applications configured to bypass the Cloudflare network. This provides the predictability and control needed for performance-sensitive applications, ensuring your critical traffic always takes the path you choose.</p>
<p>To pin applications to a WAN port:</p>
<ol>
<li>
<p>Log in to the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, and go to <strong>Networks</strong>.</p>
</li>
<li>
<p>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong> &gt; <strong>Profiles</strong>.</p>
</li>
<li>
<p>Select the Cloudflare One Appliance you want to configure &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>In <strong>Traffic steering</strong> &gt; <strong>Breakout Traffic</strong> find the application you want to pin to a WAN port.</p>
</li>
<li>
<p>Select the three dots next to it &gt; <strong>Edit application traffic</strong>.</p>
</li>
<li>
<p>From the <strong>Preferred breakout port</strong> drop-down menu, select the WAN port you want to assign to the applications.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="netflow-exports-from-cloudflare-one-appliance-to-network-flow">NetFlow exports from Cloudflare One Appliance to Network Flow</h2>
<p>You can configure your Cloudflare One Appliance (formerly Magic WAN Connector) to export Netflow statistics for local breakout traffic to <a href="/network-flow">Network Flow</a> (formerly Magic Network Monitoring). This provides insights into traffic that leaves your site directly, bypassing the Cloudflare network.</p>
<p>The Cloudflare One Appliance uses NetFlow v9 to export flow data for breakout traffic only. You can enable and configure this export by setting the Netflow configuration for the associated site via the Cloudflare API.</p>
<h3 id="enable-netflow-exports">Enable NetFlow exports</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5803.md")
</aside>
<ol>
<li>Send a <code>PUT</code> request to the Netflow configuration endpoint for your site.</li>
<li>In the JSON body request, you must include the <code>collector_ip</code> parameter. To export traffic statistics to Network Flow, use the IP address <code>162.159.65.1</code>. This is the only field required to enable the feature.</li>
</ol>
<p>Minimal configuration example:</p>
<pre><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/netflow_config</code></pre>
<ol start="3">
<li>You can customize the configuration by adding optional fields to the JSON payload. These fields include:</li>
</ol>
<ul>
<li><code>collector_port</code>: The UDP port for the collector. The default is <code>2055</code>.</li>
<li><code>sampling_rate</code>: The rate at which packets are sampled.</li>
<li><code>active_timeout</code>: The timeout for active flows in seconds.</li>
<li><code>inactive_timeout</code>: The timeout for inactive flows in seconds.</li>
</ul>
<p>Full configuration example:</p>
<pre><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/netflow_config</code></pre>
<p>Your Cloudflare One Appliance will now begin exporting Netflow data for its breakout traffic, which will be ingested and displayed within your Network Flow dashboard. You can retrieve the current settings by sending a <code>GET</code> request, or disable the export by sending a <code>DELETE</code> request to the same endpoint.</p>
<h2 id="cloudflare-one-client-traffic">Cloudflare One Client traffic</h2>
<p>If you have Cloudflare One Appliance (formerly Magic WAN Connector) and Cloudflare One Clients deployed in your premises, Cloudflare One Appliance automatically routes Cloudflare One Client traffic to the Internet rather than Cloudflare WAN IPsec tunnels. This prevents traffic from being encapsulated twice.</p>
<p>You may need to configure your firewall to allow this new traffic. Make sure to allow the following IPs and ports:</p>
<ul>
<li><strong>Destination IPs</strong>: <code>162.159.193.0/24</code>, <code>162.159.197.0/24</code></li>
<li><strong>Destination ports</strong>: <code>443</code>, <code>500</code>, <code>1701</code>, <code>2408</code>, <code>4443</code>, <code>4500</code>, <code>8095</code>, <code>8443</code></li>
</ul>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> for more information on this topic.</p>
