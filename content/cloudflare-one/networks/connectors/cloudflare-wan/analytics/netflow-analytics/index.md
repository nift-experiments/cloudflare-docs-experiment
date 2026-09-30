<h2 id="netflow-exports-from-cloudflare-one-appliance-to-network-flow">NetFlow exports from Cloudflare One Appliance to Network Flow</h2>
<p>You can configure your Cloudflare One Appliance (formerly Magic WAN Connector) to export Netflow statistics for <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">local breakout traffic</a> to <a href="/network-flow">Network Flow</a> (formerly Magic Network Monitoring). This provides insights into traffic that leaves your site directly, bypassing the Cloudflare network.</p>
<p>The Cloudflare One Appliance uses NetFlow v9 to export flow data for breakout traffic only. You can enable and configure this export by setting the Netflow configuration for the associated site via the Cloudflare API.</p>
<h3 id="enable-netflow-exports">Enable NetFlow exports</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5591.md")
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
