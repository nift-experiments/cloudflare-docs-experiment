---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/
  description: Create a tunnel (API) in Zero Trust networking.
  full_title: Create a tunnel (API) · Cloudflare One docs
  head_html: <title>Create a tunnel (API) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a tunnel (API) in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/index.md"><meta property="og:title" content="Create a tunnel (API) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a tunnel (API) in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#page","headline":"Create a tunnel (API) \u00b7 Cloudflare One docs","description":"Create a tunnel (API) in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/
  schema: 1
---
<p>Follow this guide to set up a Cloudflare Tunnel using the API.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5298.md")
</aside>
<h2 id="create-an-api-token">Create an API token</h2>
<p><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> with the following permissions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Item</th>
<th>Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account</td>
<td>Cloudflare Tunnel</td>
<td>Edit</td>
</tr>
<tr>
<td>Zone</td>
<td>DNS</td>
<td>Edit</td>
</tr>
</tbody>
</table>
<h2 id="2-create-a-tunnel"><ol start="2">
<li>Create a tunnel</li>
</ol></h2>
<p>Make a <code>POST</code> request to the <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/create/">Cloudflare Tunnel</a> endpoint:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/cfd_tunnel \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;api-tunnel&quot;,&#10;  &quot;config_src&quot;: &quot;cloudflare&quot;&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-sh">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa&quot;,&#10;    &quot;account_tag&quot;: &quot;699d98642c564d2e855e9661899b7252&quot;,&#10;    &quot;created_at&quot;: &quot;2025-02-18T22:41:43.534395Z&quot;,&#10;    &quot;deleted_at&quot;: null,&#10;    &quot;name&quot;: &quot;example-tunnel&quot;,&#10;    &quot;connections&quot;: [],&#10;    &quot;conns_active_at&quot;: null,&#10;    &quot;conns_inactive_at&quot;: &quot;2025-02-18T22:41:43.534395Z&quot;,&#10;    &quot;tun_type&quot;: &quot;cfd_tunnel&quot;,&#10;    &quot;metadata&quot;: {},&#10;    &quot;status&quot;: &quot;inactive&quot;,&#10;    &quot;remote_config&quot;: true,&#10;    &quot;credentials_file&quot;: {&#10;      &quot;AccountTag&quot;: &quot;699d98642c564d2e855e9661899b7252&quot;,&#10;      &quot;TunnelID&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa&quot;,&#10;      &quot;TunnelName&quot;: &quot;api-tunnel&quot;,&#10;      &quot;TunnelSecret&quot;: &quot;bTSquyUGwLQjYJn8cI8S1h6M6wUc2ajIeT7JotlxI7TqNqdKFhuQwX3O8irSnb==&quot;&#10;    },&#10;    &quot;token&quot;: &quot;eyJhIjoiNWFiNGU5Z...&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Copy the <code>id</code> and <code>token</code> values shown in the output. You will need these values to configure and run the tunnel.</p>
<p>The next steps depend on whether you want to <a href="#3a-publish-an-application">publish an application to the Internet</a> or <a href="#3b-connect-a-network">connect a private network</a>.</p>
<h2 id="3a-publish-an-application">3a. Publish an application</h2>
<p>Before you publish an application through your tunnel, you must:</p>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a>.</li>
<li><a href="/dns/zone-setups/full-setup/setup/">Change your domain nameservers to Cloudflare</a>.</li>
</ul>
<p>Follow these steps to publish an application to the Internet. If you are looking to connect a private resource, skip to the <a href="#3b-connect-a-network">Connect a network</a> section.</p>
<ol>
<li>Make a <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/methods/update/"><code>PUT</code> request</a> to route your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/">local service URL</a> to a public hostname. For example,</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;config&quot;: {&#10;    &quot;ingress&quot;: [&#10;      {&#10;        &quot;hostname&quot;: &quot;app.example.com&quot;,&#10;        &quot;service&quot;: &quot;http://localhost:8001&quot;,&#10;        &quot;originRequest&quot;: {}&#10;      },&#10;      {&#10;        &quot;service&quot;: &quot;http_status:404&quot;&#10;      }&#10;    ]&#10;  }&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5297.md")
</aside>
<p>Your ingress rules must include a catch-all rule at the end. In this example, <code>cloudflared</code> will respond with a 404 status code when the request does not match any of the previous hostnames.</p>
<ol start="2">
<li><a href="/api/resources/dns/subresources/records/methods/create/">Create a DNS record</a> for your application:</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;CNAME&quot;,&#10;  &quot;proxied&quot;: true,&#10;  &quot;name&quot;: &quot;app.example.com&quot;,&#10;  &quot;content&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa.cfargotunnel.com&quot;&#10;}&#x27;</code></pre>
<p>This DNS record allows Cloudflare to proxy <code>app.example.com</code> traffic to your Cloudflare Tunnel (<code>&lt;tunnel-id&gt;.cfargotunnel.com</code>).</p>
<p>This application will be publicly available on the Internet once you <a href="#4-install-and-run-the-tunnel">run the tunnel</a>. To allow or block specific users, <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">create an Access application</a>.</p>
<h2 id="3b-connect-a-network">3b. Connect a network</h2>
<p>To connect a private network through your tunnel, <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/">add a tunnel route</a>:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/teamnet/routes \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;network&quot;: &quot;172.16.0.0/16&quot;,&#10;  &quot;tunnel_id&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa&quot;,&#10;  &quot;comment&quot;: &quot;Example private network route&quot;&#10;}&#x27;</code></pre>
<p><code>cloudflared</code> can now route traffic to these destination IPs. To configure Zero Trust policies and connect as a user, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Connect private networks</a>.</p>
<h2 id="4-install-and-run-the-tunnel"><ol start="4">
<li>Install and run the tunnel</li>
</ol></h2>
<p>Install <code>cloudflared</code> on your server and run the tunnel using the <code>token</code> value obtained in <a href="#2-create-a-tunnel">2. Create a tunnel</a>. You can also get the tunnel token using the <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/token/methods/get/">Cloudflare Tunnel token</a> endpoint.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5303.md")
</div></div>
<h2 id="5-verify-tunnel-status"><ol start="5">
<li>Verify tunnel status</li>
</ol></h2>
<p>To check if the tunnel is serving traffic:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/cfd_tunnel/{tunnel_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-sh">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa&quot;,&#10;    &quot;account_tag&quot;: &quot;699d98642c564d2e855e9661899b7252&quot;,&#10;    &quot;created_at&quot;: &quot;2025-02-18T22:41:43.534395Z&quot;,&#10;    &quot;deleted_at&quot;: null,&#10;    &quot;name&quot;: &quot;example-tunnel&quot;,&#10;    &quot;connections&quot;: [&#10;      {&#10;        &quot;colo_name&quot;: &quot;bos01&quot;,&#10;        &quot;uuid&quot;: &quot;2xz99mfm-a59e-4924-gyh9-z9vafaw6k0i2&quot;,&#10;        &quot;id&quot;: &quot;2xz99mfm-a59e-4924-gyh9-z9vafaw6k0i2&quot;,&#10;        &quot;is_pending_reconnect&quot;: false,&#10;        &quot;origin_ip&quot;: &quot;10.1.0.137&quot;,&#10;        &quot;opened_at&quot;: &quot;2025-02-19T19:11:12.101642Z&quot;,&#10;        &quot;client_id&quot;: &quot;4xh4eb3f-cz0j-2aso-hu6i-36207018771a&quot;,&#10;        &quot;client_version&quot;: &quot;2025.2.0&quot;&#10;      },&#10;      {&#10;        &quot;colo_name&quot;: &quot;phl01&quot;,&#10;        &quot;uuid&quot;: &quot;axe2socu-2fb5-3akx-b860-898zyes3cs9q&quot;,&#10;        &quot;id&quot;: &quot;axe2socu-2fb5-3akx-b860-898zyes3cs9q&quot;,&#10;        &quot;is_pending_reconnect&quot;: false,&#10;        &quot;origin_ip&quot;: &quot;10.1.0.137&quot;,&#10;        &quot;opened_at&quot;: &quot;2025-02-19T19:11:12.006297Z&quot;,&#10;        &quot;client_id&quot;: &quot;4xh4eb3f-cz0j-2aso-hu6i-36207018771a&quot;,&#10;        &quot;client_version&quot;: &quot;2025.2.0&quot;&#10;      },&#10;      {&#10;        &quot;colo_name&quot;: &quot;phl01&quot;,&#10;        &quot;uuid&quot;: &quot;9b5y0wm9-ca7f-ibq6-8ff4-sm53xekfyym1&quot;,&#10;        &quot;id&quot;: &quot;9b5y0wm9-ca7f-ibq6-8ff4-sm53xekfyym1&quot;,&#10;        &quot;is_pending_reconnect&quot;: false,&#10;        &quot;origin_ip&quot;: &quot;10.1.0.137&quot;,&#10;        &quot;opened_at&quot;: &quot;2025-02-19T19:11:12.004721Z&quot;,&#10;        &quot;client_id&quot;: &quot;4xh4eb3f-cz0j-2aso-hu6i-36207018771a&quot;,&#10;        &quot;client_version&quot;: &quot;2025.2.0&quot;&#10;      },&#10;      {&#10;        &quot;colo_name&quot;: &quot;bos01&quot;,&#10;        &quot;uuid&quot;: &quot;g6cdeiz1-80f5-3akx-b18b-3y0ggktoxwkd&quot;,&#10;        &quot;id&quot;: &quot;g6cdeiz1-80f5-3akx-b18b-3y0ggktoxwkd&quot;,&#10;        &quot;is_pending_reconnect&quot;: false,&#10;        &quot;origin_ip&quot;: &quot;10.1.0.137&quot;,&#10;        &quot;opened_at&quot;: &quot;2025-02-19T19:11:12.110765Z&quot;,&#10;        &quot;client_id&quot;: &quot;4xh4eb3f-cz0j-2aso-hu6i-36207018771a&quot;,&#10;        &quot;client_version&quot;: &quot;2025.2.0&quot;&#10;      }&#10;    ],&#10;    &quot;conns_active_at&quot;: &quot;2025-02-19T19:11:12.004721Z&quot;,&#10;    &quot;conns_inactive_at&quot;: null,&#10;    &quot;tun_type&quot;: &quot;cfd_tunnel&quot;,&#10;    &quot;metadata&quot;: {},&#10;    &quot;status&quot;: &quot;healthy&quot;,&#10;    &quot;remote_config&quot;: true&#10;  }&#10;}&#10;</code></pre>
<p>A healthy tunnel will have four connections to Cloudflare's network.</p>
