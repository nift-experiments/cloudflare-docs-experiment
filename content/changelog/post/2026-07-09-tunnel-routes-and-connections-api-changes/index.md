---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
  description: New updates and improvements at Cloudflare.
  full_title: Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026 · Changelog
  head_html: <title>Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/#page","headline":"Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 9, 2026</time><h2 id="post-title">Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span><span>mesh</span></div><div class="changelog-body"><p>On <strong>October 5, 2026</strong>, two changes take effect across the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>: the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the <code>connections</code> field. If you manage private network routes or read tunnel connection details through the API, <code>cloudflared</code>, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.</p>
<h4 id="route-endpoints">Route endpoints</h4>
<p>The CIDR-encoded route endpoints are deprecated in favor of the standard, <code>route_id</code>-based endpoints that already exist today. Both sets of endpoints route a private network through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or <a href="/mesh/">Cloudflare Mesh</a> (the API still refers to Mesh nodes as <code>warp_connector</code>) — only the request shape changes.</p>
<p><strong>Deprecated endpoints (removed October 5, 2026):</strong></p>
<ul>
<li>Create a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Update a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Delete a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
</ul>
<p><strong>Replacement endpoints:</strong></p>
<ul>
<li>Create a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes</code></a></li>
<li>Update a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
<li>Delete a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
</ul>
<h4 id="what-is-changing">What is changing</h4>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Deprecated (CIDR-encoded path)</th>
<th align="left">Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Route identifier</td>
<td align="left">URL-encoded CIDR in the path (<code>/network/{ip_network_encoded}</code>)</td>
<td align="left"><code>route_id</code> in the path (<code>network</code> moves to the request body on create)</td>
</tr>
<tr>
<td align="left">Create</td>
<td align="left"><code>POST .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>POST .../teamnet/routes</code> with <code>network</code> and <code>tunnel_id</code> in the body</td>
</tr>
<tr>
<td align="left">Update</td>
<td align="left"><code>PATCH .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>PATCH .../teamnet/routes/{route_id}</code></td>
</tr>
<tr>
<td align="left">Delete</td>
<td align="left"><code>DELETE .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>DELETE .../teamnet/routes/{route_id}</code></td>
</tr>
</tbody>
</table>
<h4 id="action-required">Action required</h4>
<ol>
<li>Capture each route's <code>route_id</code> by calling <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List tunnel routes</a>, or read it from the response the first time you create a route with the replacement endpoint.</li>
<li>Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.</li>
<li>If you manage routes with the <code>cloudflared tunnel route ip add | delete</code> commands, upgrade <code>cloudflared</code> to the <a href="https://github.com/cloudflare/cloudflared/releases">latest version</a>.</li>
<li>If you manage routes with Terraform, make sure you are on a current version of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route"><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></a> resource and the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</li>
</ol>
<pre tabindex="0"><code class="language-bash">&#35; Before: create a route by URL-encoding the CIDR into the path&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: create a route with the network in the request body&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;network&quot;: &quot;172.16.0.0/16&quot;, &quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: update or delete a route using its route_id&#10;curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;comment&quot;: &quot;Updated comment for this route.&quot;}&#x27;&#10;&#10;curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="cloudflare-tunnel-and-cloudflare-mesh-connections">Cloudflare Tunnel and Cloudflare Mesh connections</h4>
<p>Starting the same day, the <code>connections</code> array is removed from list and get responses for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> nodes (the <code>cfd_tunnel</code> and <code>warp_connector</code> API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.</p>
<p>This affects:</p>
<ul>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
</ul>
<h4 id="action-required-1">Action required</h4>
<p>Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections</code></a>. For Cloudflare Mesh, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections</code></a>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Before: read connections off the tunnel object&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;&#35; After: query connections directly&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Update any dashboards, monitoring scripts, or automation that parses <code>connections</code> from the tunnel list or get response. <code>cloudflared</code> and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.</p>
<h4 id="why-we-are-making-these-changes">Why we are making these changes</h4>
<ul>
<li><strong>Smaller, faster responses.</strong> Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.</li>
<li><strong>A single way to identify a route.</strong> Consolidating on <code>route_id</code> removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.</li>
<li><strong>Consistency across the API.</strong> Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.</li>
</ul>
<p>To learn more, refer to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a>, the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>, and <a href="/cloudflare-one/networks/routes/">Routes</a> documentation.</p>
</div></article></div>
