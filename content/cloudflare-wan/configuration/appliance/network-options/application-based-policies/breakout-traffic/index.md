---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/
  description: Breakout traffic allows you to define which applications should bypass Cloudflare's security filtering.
  full_title: Breakout traffic · Cloudflare WAN docs
  head_html: <title>Breakout traffic · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Breakout traffic allows you to define which applications should bypass Cloudflare&#x27;s security filtering."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/index.md"><meta property="og:title" content="Breakout traffic · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Breakout traffic allows you to define which applications should bypass Cloudflare&#x27;s security filtering."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#page","headline":"Breakout traffic \u00b7 Cloudflare WAN docs","description":"Breakout traffic allows you to define which applications should bypass Cloudflare's security filtering.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/
  schema: 1
---
<p>Breakout traffic allows you to define which applications should bypass Cloudflare's security filtering, and go directly to the Internet. It works via DNS requests inspection. This means that if your network is caching DNS requests, Breakout traffic will only take effect after you cache entries expire and your client issues a new DNS request that Cloudflare One Appliance (formerly Magic WAN Connector) can detect. This can take several minutes.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7049.md")
</aside>
<pre tabindex="0" class="mermaid">&#10;&#10;	{`&#10;	flowchart LR&#10;	accTitle: Breakout traffic flow&#10;	accDescr: Applications 1 and 2 are configured to bypass Cloudflare's security filtering, and go straight to the Internet.&#10;	a(Cloudflare One Appliance) --> b(Cloudflare) -->|Filtered traffic|c(Internet)&#10;&#10;	a-- Breakout traffic ---d(Application1) & e(Application2) --> c&#10;&#10;	classDef orange fill:#f48120,color: black&#10;	class a,b orange&#10;	`}&#10;&#10;</pre>
<p><em>In the graph above, Applications 1 and 2 are configured to bypass Cloudflare's security filtering, and go straight to the Internet.</em></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7050.md")
</aside>
<h2 id="add-an-application-to-your-account">Add an application to your account</h2>
<p>Before you can add or remove Breakout traffic applications to your Cloudflare One Appliance, you need an account-level list with the applications that you want to configure. This list contains two kinds of applications:</p>
<ul>
<li><strong>Cloudflare-managed applications</strong> — Cloudflare's built-in catalog of recognized applications. These already exist in your account and do not need to be created. Select them directly when assigning application traffic.</li>
<li><strong>Custom applications</strong> — applications you define by <strong>hostname</strong>, <strong>IP subnet</strong>, and/or <strong>source subnet</strong>. You can create, edit, and delete custom applications directly from the dashboard or through the <a href="/api/resources/magic_transit/subresources/apps/methods/create/">Create an account app</a> endpoint.</li>
</ul>
<h3 id="create-edit-or-delete-a-custom-application">Create, edit, or delete a custom application</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7053.md")
</div></div>
<h3 id="add-an-application-to-cloudflare-one-appliance">Add an application to Cloudflare One Appliance</h3>
<p>You need to configure Breakout traffic applications for each of your existing sites, as this is a per-site configuration.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7056.md")
</div></div>
<h3 id="delete-an-application-from-cloudflare-one-appliance">Delete an application from Cloudflare One Appliance</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7059.md")
</div></div>
<h2 id="designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</h2>
<p>You can pin applications to a specific WAN port in Cloudflare One Appliance when you need control over which WAN port your applications egress from the device. In case your preferred WAN port goes down, Cloudflare One Appliance automatically fails over to a standard configured WAN port priority.</p>
<p>With this preferred breakout port, customers have direct control over their local Internet breakout traffic. You can designate a specific WAN uplink as the primary path for your critical applications configured to bypass the Cloudflare network. This provides the predictability and control needed for performance-sensitive applications, ensuring your critical traffic always takes the path you choose.</p>
<p>To pin applications to a WAN port:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</p>
</li>
<li>
<p>Select your Appliance &gt; <strong>Edit</strong>.</p>
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
@markup("md", "content/.markup/bodies/7046.md")
</aside>
<ol>
<li>Send a <code>PUT</code> request to the Netflow configuration endpoint for your site.</li>
<li>In the JSON body request, you must include the <code>collector_ip</code> parameter. To export traffic statistics to Network Flow, use the IP address <code>162.159.65.1</code>. This is the only field required to enable the feature.</li>
</ol>
<p>Minimal configuration example:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/netflow_config</code></pre>
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
<pre tabindex="0"><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/netflow_config</code></pre>
<p>Your Cloudflare One Appliance will now begin exporting Netflow data for its breakout traffic, which will be ingested and displayed within your Network Flow dashboard. You can retrieve the current settings by sending a <code>GET</code> request, or disable the export by sending a <code>DELETE</code> request to the same endpoint.</p>
<h2 id="cloudflare-one-client-traffic">Cloudflare One Client traffic</h2>
<p>If you have Cloudflare One Appliance (formerly Magic WAN Connector) and Cloudflare One Clients deployed in your premises, Cloudflare One Appliance automatically routes Cloudflare One Client traffic to the Internet rather than Cloudflare WAN IPsec tunnels. This prevents traffic from being encapsulated twice.</p>
<p>You may need to configure your firewall to allow this new traffic. Make sure to allow the following IPs and ports:</p>
<ul>
<li><strong>Destination IPs</strong>: <code>162.159.193.0/24</code>, <code>162.159.197.0/24</code></li>
<li><strong>Destination ports</strong>: <code>443</code>, <code>500</code>, <code>1701</code>, <code>2408</code>, <code>4443</code>, <code>4500</code>, <code>8095</code>, <code>8443</code></li>
</ul>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> for more information on this topic.</p>
<h2 id="breakout-by-source">Breakout by source</h2>
<p>In addition to matching by destination application, you can define breakout rules that match by <strong>source</strong> — by source LAN interface, source VLAN, or source IP address / CIDR block. This is useful for breaking out an entire guest VLAN or a specific subnet to the local Internet without enumerating destination applications.</p>
<h3 id="match-criteria">Match criteria</h3>
<table>
<thead>
<tr>
<th>Criterion</th>
<th>Behavior</th>
<th>Configuration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source LAN interface</td>
<td>All traffic originating on the selected LAN is broken out. Any VLAN attached to that LAN is included automatically.</td>
<td>API and Terraform.</td>
</tr>
<tr>
<td>Source IPv4 CIDR</td>
<td>All traffic with a source IP in the specified CIDR block is broken out.</td>
<td>Dashboard (<strong>Source subnets</strong> field on a <a href="#create-edit-or-delete-a-custom-application">custom application</a>), API, and Terraform.</td>
</tr>
<tr>
<td>Source IP address or range</td>
<td>All traffic with a source IP matching the specified address or range is broken out.</td>
<td>API and Terraform.</td>
</tr>
</tbody>
</table>
<p>The same criteria can be used to mark traffic as <strong>prioritized</strong> instead of broken out. Refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a> for details.</p>
<p>Source-based and destination-based (managed app or custom app) rules can co-exist on the same appliance and are evaluated independently. If a flow matches both a source-based breakout rule and a destination-based breakout rule, the appliance breaks it out.</p>
