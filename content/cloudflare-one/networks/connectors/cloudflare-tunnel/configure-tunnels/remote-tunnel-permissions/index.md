---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/
  description: Manage tunnel tokens and control who can run your remotely-managed tunnels.
  full_title: Tunnel permissions · Cloudflare One docs
  head_html: <title>Tunnel permissions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage tunnel tokens and control who can run your remotely-managed tunnels."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/index.md"><meta property="og:title" content="Tunnel permissions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage tunnel tokens and control who can run your remotely-managed tunnels."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="CLI,Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/#page","headline":"Tunnel permissions \u00b7 Cloudflare One docs","description":"Manage tunnel tokens and control who can run your remotely-managed tunnels.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CLI","Terraform"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/
  schema: 1
---
<p>A remotely-managed tunnel only requires the tunnel token to run. Anyone with access to the token will be able to run the tunnel.</p>
<h2 id="get-the-tunnel-token">Get the tunnel token</h2>
<p>To get the token for a remotely-managed tunnel:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5364.md")
</div></div>
<h2 id="rotate-a-token-without-service-disruption">Rotate a token without service disruption</h2>
<p>Cloudflare recommends rotating the tunnel token at a regular cadence to reduce the risk of token compromise. You can rotate a token with minimal disruption to users as long as the tunnel is served by at least two <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas</a>. To ensure service availability, we recommend performing token rotations outside of working hours or in a maintenance window.</p>
<p>To rotate a tunnel token:</p>
<ol>
<li>Refresh the token on Cloudflare:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5367.md")
</div></div>
<pre tabindex="0"><code>After refreshing the token, `cloudflared` can no longer establish new connections to Cloudflare using the old token. However, existing connectors will remain active and the tunnel will continue serving traffic.&#10;</code></pre>
<ol start="2">
<li>On half of your <code>cloudflared</code> replicas, reinstall the <code>cloudflared</code> service with the new token. For example, on a Linux host:</li>
</ol>
<pre tabindex="0"><code class="language-sh">	 sudo cloudflared service uninstall&#10;sudo cloudflared service install &lt;NEW_TOKEN&gt;&#10;</code></pre>
<ol start="3">
<li>Confirm that the service started correctly:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo systemctl status cloudflared&#10;</code></pre>
<p>While these replicas are connecting to Cloudflare with the new token, traffic will automatically route through the other replicas.</p>
<ol start="5">
<li>
<p>Wait 10 minutes for traffic to route through the new connectors.</p>
</li>
<li>
<p>Repeat steps 2, 3, and 4 for the second half of the replicas.</p>
</li>
</ol>
<p>The tunnel token is now fully rotated. The old token is no longer in use.</p>
<h2 id="rotate-a-compromised-token">Rotate a compromised token</h2>
<p>If your tunnel token is compromised, we recommend taking the following steps:</p>
<ol>
<li>Refresh the token using the dashboard or API. Refer to Step 1 of <a href="#rotate-a-token-without-service-disruption">Rotate a token without service disruption</a>.</li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/connections/methods/delete/">Delete all connections</a> between <code>cloudflared</code> and Cloudflare:</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>This will clean up any unauthorized connections and prevent users from connecting to your network.</p>
<ol start="3">
<li>On each <code>cloudflared</code> replica, update <code>cloudflared</code> to use the new token. For example, on a Linux host:</li>
</ol>
<pre tabindex="0"><code class="language-sh">	 sudo cloudflared service uninstall&#10;sudo cloudflared service install &lt;NEW_TOKEN&gt;&#10;</code></pre>
<ol start="4">
<li>Confirm that the service started correctly:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo systemctl status cloudflared&#10;</code></pre>
<p>The tunnel token is now fully rotated. The old token is no longer in use.</p>
<h2 id="account-scoped-roles">Account-scoped roles</h2>
<p>Minimum permissions needed to create, delete, and configure tunnels for an account:</p>
<ul>
<li><a href="/cloudflare-one/roles-permissions/">Cloudflare Access</a></li>
</ul>
<p>Additional permissions needed to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">route traffic to a public hostname</a> and to be able to perform <code>cloudflared login</code>:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/">DNS</a></li>
<li><a href="/fundamentals/manage-members/roles/">Load Balancer</a></li>
</ul>
<h2 id="resource-scoped-permissions">Resource-scoped permissions</h2>
<p>You can also scope permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances instead of granting account-wide access. Refer to <a href="/cloudflare-one/networks/connectors/granular-permissions/">Granular permissions for Tunnels and Mesh nodes</a>.</p>
