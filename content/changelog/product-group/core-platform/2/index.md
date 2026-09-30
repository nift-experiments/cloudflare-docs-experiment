---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/core-platform/2/
  description: '2026-07-16'
  full_title: Core platform changelog - page 2 | Cloudflare Docs
  head_html: <title>Core platform changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-07-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/core-platform/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Core platform changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-07-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/core-platform/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/2/#page","headline":"Core platform changelog - page 2 | Cloudflare Docs","description":"2026-07-16","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/core-platform/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="bot-management-fields-and-asn-support-in-cache-rules"><a href="/changelog/post/2026-07-16-cache-rules-bot-fields-asn/">Bot management fields and ASN support in Cache Rules</a></h2>
<p><em>2026-07-16</em></p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-bot-management-fields-and-asn-support-in-cache-rules">Bot management fields and ASN support in Cache Rules</h4>
<p>Cache Rules now supports bot management fields and the <code>ip.src.asnum</code> field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).</p>
<p>This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.</p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-new-fields">New fields</h4>
<p>The following fields are now available in Cache Rules expressions:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.bot_management.score</code></td>
<td>Number</td>
<td>Bot score from <code>1</code> to <code>99</code>, where a lower value indicates a higher likelihood that the request originates from a bot.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja3_hash</code></td>
<td>String</td>
<td>JA3 fingerprint of the request, which helps identify the client making the connection.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja4</code></td>
<td>String</td>
<td>JA4 fingerprint of the request, which provides a more detailed client identification than JA3.</td>
</tr>
<tr>
<td><code>cf.bot_management.verified_bot</code></td>
<td>Boolean</td>
<td>Whether the request originates from a verified bot, such as a search engine crawler.</td>
</tr>
<tr>
<td><code>cf.bot_management.static_resource</code></td>
<td>Boolean</td>
<td>Whether the request is for a static resource and therefore exempt from bot detection.</td>
</tr>
<tr>
<td><code>cf.bot_management.js_detection.passed</code></td>
<td>Boolean</td>
<td>Whether the browser passed JavaScript detection when the feature is enabled.</td>
</tr>
<tr>
<td><code>cf.bot_management.detection_ids</code></td>
<td>Array&lt;Number&gt;</td>
<td>List of IDs that correspond to Bot Management heuristic detections made on the request.</td>
</tr>
<tr>
<td><code>cf.bot_management.tags</code></td>
<td>Array&lt;String&gt;</td>
<td>List of tags associated with the bot traffic, such as <code>API</code>, <code>GOOGLE</code>, or <code>BING</code>. Match a tag with an expression such as <code>any(cf.bot_management.tags[*] eq &quot;API&quot;)</code>.</td>
</tr>
<tr>
<td><code>cf.bot_management.signed_agent</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known agent that identifies itself with Web Bot Auth.</td>
</tr>
<tr>
<td><code>cf.bot_management.corporate_proxy</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known corporate proxy.</td>
</tr>
<tr>
<td><code>ip.src.asnum</code></td>
<td>Number</td>
<td>The autonomous system number (ASN) of the incoming request's IP address.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17750.md")</aside>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-example">Example</h4>
<p>Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:</p>
<pre tabindex="0"><code class="language-txt">(http.request.uri.path contains &quot;/api/&quot; and cf.bot_management.score lt 30)&#10;or&#10;(http.request.uri.path contains &quot;/api/&quot; and not ip.src.asnum in {12345 67890})&#10;</code></pre>
<p>To learn more, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a> and the <a href="/ruleset-engine/rules-language/fields/">Fields reference</a>.</p>


<h2 id="origin-content-signals-for-markdown-for-agents"><a href="/changelog/post/2026-07-13-markdown-for-agents-header-preservation/">Origin Content Signals for Markdown for Agents</a></h2>
<p><em>2026-07-13</em></p>
<p><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:</p>
<ul>
<li>Markdown for Agents preserves security headers such as <code>Strict-Transport-Security</code> (HSTS), <code>Content-Security-Policy</code> (CSP), <code>X-Frame-Options</code>, <code>Set-Cookie</code>, and CORS headers (for example, <code>Access-Control-Allow-Origin</code>) on the converted response.</li>
<li>Caching headers (<code>Cache-Control</code>, <code>Expires</code>, <code>Age</code>) continue to pass through.</li>
</ul>
<p>Your origin's <a href="https://contentsignals.org/">Content Signals</a> policy is now authoritative. If your origin sets a <code>content-signal</code> header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default <code>Content-Signal: ai-train=yes, search=yes, ai-input=yes</code>.</p>
<p>This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as <code>../page/</code> could resolve one path segment too high and return a <code>404</code>. Links are now resolved correctly per <a href="https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3">RFC 3986</a>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>


<h2 id="zero-trust-networks-route-endpoints-and-cloudflare-tunnel-connections-field-retiring-on-october-5-2026"><a href="/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/">Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</a></h2>
<p><em>2026-07-09</em></p>
<p>On <strong>October 5, 2026</strong>, two changes take effect across the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>: the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the <code>connections</code> field. If you manage private network routes or read tunnel connection details through the API, <code>cloudflared</code>, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-route-endpoints">Route endpoints</h4>
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
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-what-is-changing">What is changing</h4>
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
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required">Action required</h4>
<ol>
<li>Capture each route's <code>route_id</code> by calling <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List tunnel routes</a>, or read it from the response the first time you create a route with the replacement endpoint.</li>
<li>Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.</li>
<li>If you manage routes with the <code>cloudflared tunnel route ip add | delete</code> commands, upgrade <code>cloudflared</code> to the <a href="https://github.com/cloudflare/cloudflared/releases">latest version</a>.</li>
<li>If you manage routes with Terraform, make sure you are on a current version of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route"><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></a> resource and the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</li>
</ol>
<pre tabindex="0"><code class="language-bash">&#35; Before: create a route by URL-encoding the CIDR into the path&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: create a route with the network in the request body&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;network&quot;: &quot;172.16.0.0/16&quot;, &quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: update or delete a route using its route_id&#10;curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;comment&quot;: &quot;Updated comment for this route.&quot;}&#x27;&#10;&#10;curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-cloudflare-tunnel-and-cloudflare-mesh-connections">Cloudflare Tunnel and Cloudflare Mesh connections</h4>
<p>Starting the same day, the <code>connections</code> array is removed from list and get responses for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> nodes (the <code>cfd_tunnel</code> and <code>warp_connector</code> API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.</p>
<p>This affects:</p>
<ul>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required-1">Action required</h4>
<p>Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections</code></a>. For Cloudflare Mesh, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections</code></a>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Before: read connections off the tunnel object&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;&#35; After: query connections directly&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Update any dashboards, monitoring scripts, or automation that parses <code>connections</code> from the tunnel list or get response. <code>cloudflared</code> and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-why-we-are-making-these-changes">Why we are making these changes</h4>
<ul>
<li><strong>Smaller, faster responses.</strong> Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.</li>
<li><strong>A single way to identify a route.</strong> Consolidating on <code>route_id</code> removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.</li>
<li><strong>Consistency across the API.</strong> Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.</li>
</ul>
<p>To learn more, refer to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a>, the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>, and <a href="/cloudflare-one/networks/routes/">Routes</a> documentation.</p>


<h2 id="new-websocket-analytics-logpush-dataset"><a href="/changelog/post/2026-07-07-websocket-analytics-dataset/">New WebSocket Analytics Logpush dataset</a></h2>
<p><em>2026-07-07</em></p>
<p>Enterprise customers can now push per-connection WebSocket analytics to any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a> using the new <code>websocket_analytics</code> dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.</p>
<p>Key fields include:</p>
<ul>
<li><strong><code>ConnectionCloseReason</code></strong> — why the connection ended: <code>peerReset</code>, <code>peerNoError</code>, <code>timedOut</code>, <code>upstreamReset</code>, <code>protocolViolation</code>, <code>unspecifiedError</code>, or <code>none</code>.</li>
<li><strong><code>ConnectionCloseSource</code></strong> — which side initiated the close: <code>upstream</code>, <code>downstream</code>, <code>me</code>, or <code>both</code>.</li>
<li><strong><code>ConnectionTransportCloseCode</code></strong> — the TLS alert code or TCP-level close code for additional precision.</li>
<li><strong><code>RayID</code></strong> — correlate WebSocket connection events with your existing HTTP Request logs.</li>
</ul>
<p>The dataset also includes directional byte counts (<code>BytesSentClient</code>, <code>BytesReceivedClient</code>, <code>BytesSentOrigin</code>, <code>BytesReceivedOrigin</code>), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.</p>
<p>This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (<code>ConnectionCloseReason == &quot;peerReset&quot;</code>) grouped by host and data center — directly in your existing log analysis tools.</p>
<p>For the full list of available fields, refer to <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics</a>.</p>


<h2 id="updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-07-02-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-07-02</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-07-02-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Gateway DNS</strong> (added): <code>AppliedMaxTTL</code> and <code>UpstreamRecordTTLs</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>Warnings</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>CacheLockWaitedMs</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="new-permissions-and-roles-for-gateway-policies-and-lists"><a href="/changelog/post/2026-06-30-gateway-granular-permissions/">New permissions and roles for Gateway policies and lists</a></h2>
<p><em>2026-06-30</em></p>
<p>You can now assign granular, resource-scoped roles for <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> firewall policies and <a href="/cloudflare-one/reusable-components/lists/">Zero Trust lists</a>. Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.</p>
<h4 id="2026-06-30-gateway-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the following resource-scoped roles are now available:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zero Trust Gateway Firewall Policies Admin</td>
<td>Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway DNS Policies Admin</td>
<td>Can view and edit Gateway DNS policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway HTTP Policies Admin</td>
<td>Can view and edit Gateway HTTP policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Network Policies Admin</td>
<td>Can view and edit Gateway Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Egress Policies Admin</td>
<td>Can view and edit Gateway Egress policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Resolver Policies Admin</td>
<td>Can view and edit Gateway Resolver policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Admin</td>
<td>Can view and edit all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Read</td>
<td>Can view all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Read Only</td>
<td>Can view all Gateway resources.</td>
</tr>
<tr>
<td>Zero Trust DNS Locations Admin</td>
<td>Can view and edit DNS locations.</td>
</tr>
<tr>
<td>Zero Trust Proxy Endpoints Admin</td>
<td>Can view and edit Gateway Proxy Endpoints.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Admin</td>
<td>Can view and edit all Gateway and Access lists.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Read</td>
<td>Can view all Gateway and Access lists.</td>
</tr>
</tbody>
</table>
<p>These roles allow you to:</p>
<ul>
<li>Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.</li>
<li>Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.</li>
<li>Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.</li>
</ul>
<p>You can also now assign <em>Resource-scoped roles</em>. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. <strong>Existing account-level roles continue to work.</strong> A member with the <code>Cloudflare Gateway</code> or <code>Cloudflare Zero Trust</code> role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.</p>
<h4 id="2026-06-30-gateway-granular-permissions-get-started">Get started</h4>
<ul>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
<li>Learn how to <a href="/fundamentals/manage-members/policies/">create permission policies</a> that use these roles.</li>
</ul>


<h2 id="account-scoped-firewall-events-dataset-in-logpush"><a href="/changelog/post/2026-06-30-account-level-firewall-events/">Account-scoped firewall events dataset in Logpush</a></h2>
<p><em>2026-06-30</em></p>
<p>Cloudflare Logpush now supports <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">firewall events as an account-scoped dataset</a>. Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.</p>
<p>The dataset includes a new <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename"><code>ZoneName</code></a> field so you can identify which zone each event came from when consuming logs in your downstream pipeline.</p>
<h4 id="2026-06-30-account-level-firewall-events-what-s-available">What's available</h4>
<ul>
<li>A new account-scoped <code>firewall_events</code> dataset, configurable via the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a> or the Cloudflare dashboard.</li>
<li>The same fields and filter expressions supported by the existing <a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">zone-scoped firewall events dataset</a>, plus the new <code>ZoneName</code> field.</li>
<li>Support for all existing Logpush destinations.</li>
</ul>


<h2 id="search-api-tokens-by-name"><a href="/changelog/post/2026-06-25-api-token-search/">Search API tokens by name</a></h2>
<p><em>2026-06-25</em></p>
<p>You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.</p>
<h4 id="2026-06-25-api-token-search-what-s-new">What's new</h4>
<ul>
<li><strong>Dashboard search</strong>: Both <a href="https://dash.cloudflare.com/?to=/:account/account-api-tokens">account API tokens</a> and <a href="https://dash.cloudflare.com/profile/api-tokens">user API tokens</a> pages now include a search bar. Type a name to filter results.</li>
<li><strong>API search support</strong>: The <a href="/api/resources/user/subresources/tokens/methods/list/"><code>/user/tokens</code></a> and <a href="/api/resources/accounts/subresources/tokens/methods/list/"><code>/accounts/{account_id}/tokens</code></a> endpoints now accept a <code>name</code> query parameter to filter tokens by name.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/get-started/create-token/">Create an API token</a> and <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a>.</p>


<h2 id="audit-logs-v2-organization-level-audit-logs-in-cloudflare-dashboard"><a href="/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/">Audit Logs v2 — Organization-level audit logs in Cloudflare dashboard</a></h2>
<p><em>2026-06-24</em></p>
<p>You can now, as an <a href="/fundamentals/organizations/">Organization</a> Super Administrator, view organization-level <a href="/fundamentals/account/account-security/audit-logs/">audit logs</a> in the Cloudflare dashboard, in addition to the existing <a href="/fundamentals/account/account-security/audit-logs/#organization-activity-logs">API access</a>.</p>
<p>Organization audit logs help you monitor activity across your organization. You can see who performed an action, what changed, when it happened, how it was performed, and whether it succeeded or failed.</p>
<p>You can filter and search logs by actor, action, result, resource, request details, and timestamp. Use these logs to troubleshoot changes, investigate unexpected access, and support security or compliance workflows.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_organization_dashboard.png" alt="Organization audit logs in the Cloudflare dashboard" /></p>
<p>If you are viewing account-level audit logs and the account belongs to an organization where you are an Organization Super Administrator, select <strong>View Organization Audit Logs</strong> to open the parent organization's audit logs.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_view_organization_button.png" alt="View Organization Audit Logs button" /></p>
<p>To get started, go to <strong>Organizations</strong>, select your organization, then go to <strong>Manage Organization</strong> &gt; <strong>Audit Logs</strong>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


<h2 id="new-websocket-analytics-logpush-dataset-and-updated-fields"><a href="/changelog/post/2026-06-24-log-fields-updated/">New WebSocket Analytics Logpush dataset and updated fields</a></h2>
<p><em>2026-06-24</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-24-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>WebSocket Analytics</strong>: A new dataset with fields including <code>BytesReceivedClient</code>, <code>BytesReceivedOrigin</code>, <code>BytesSentClient</code>, <code>BytesSentOrigin</code>, <code>ClientASN</code>, <code>ClientIP</code>, <code>ClientRequestHost</code>, <code>ClientRequestPath</code>, <code>ClientRequestUserAgent</code>, <code>ColoCode</code>, <code>ConnectionCloseReason</code>, <code>ConnectionCloseSource</code>, <code>ConnectionID</code>, <code>ConnectionTransportCloseCode</code>, <code>EdgeEndTimestamp</code>, <code>EdgeStartTimestamp</code>, and <code>RayID</code>.</li>
</ul>
<h4 id="2026-06-24-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>ZoneName</code>. The Firewall events dataset is now also available for <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">account-scope Logpush</a>, in addition to the existing zone scope.</li>
<li><strong>Email Security Alerts</strong> (added): <code>BCC</code>, <code>DKIMResult</code>, <code>DMARCPolicy</code>, <code>DMARCResult</code>, and <code>SPFResult</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="manage-all-your-routes-from-one-page-in-the-dashboard"><a href="/changelog/post/2026-06-19-unified-routes-page/">Manage all your routes from one page in the dashboard</a></h2>
<p><em>2026-06-19</em></p>
<p>The <strong>Routes</strong> page in the Cloudflare dashboard now shows the routes across all of your connectors — <a href="/mesh/">Cloudflare Mesh</a> and <a href="/tunnel/">Cloudflare Tunnel</a> routes alongside <a href="/cloudflare-wan/">Cloudflare WAN</a> and <a href="/magic-transit/">Magic Transit</a> static routes — in a single table, instead of a separate routes view per product.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-06-19-unified-routes.gif" alt="The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table" /></p>
<p>From the unified Routes page you can:</p>
<ul>
<li><strong>Visualize your network with an interactive map</strong> that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.</li>
<li><strong>See every route in one table</strong>, with its destination, type, connector, priority, and source, and filter or sort to find what you need.</li>
<li><strong>Create, edit, and delete routes</strong> of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by <strong>connector name</strong> instead of typing its IP.</li>
<li><strong>Manage <a href="/cloudflare-one/networks/virtual-networks/">virtual networks</a></strong> from a dedicated tab.</li>
<li><strong>Test a route</strong> to see which connector and next hop a destination resolves to before you commit a change.</li>
</ul>
<p>To find it, go to <strong>Networking</strong> &gt; <strong>Routes</strong> in the dashboard sidebar.</p>
<div class="nb-dash-button"></div>
<p>Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to <a href="/cloudflare-one/networks/routes/add-routes/">add routes</a> and <a href="/cloudflare-one/networks/virtual-networks/">manage virtual networks</a>.</p>


<h2 id="pay-per-crawl-advanced-configuration"><a href="/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/">Pay Per Crawl advanced configuration</a></h2>
<p><em>2026-06-16</em></p>
<p>You can now configure advanced Pay Per Crawl settings for your zone, including:</p>
<ul>
<li><strong>Disable Pay Per Crawl by URI pattern</strong> using <a href="/rules/configuration-rules/">Configuration Rules</a> to offer free access to specific pages while charging for others.</li>
<li><strong>Dynamic pricing</strong> by having your origin return a <code>crawler-price</code> response header, or by using a <a href="/workers/">Cloudflare Worker</a> to set prices based on request properties.</li>
</ul>
<p>When dynamic pricing is enabled, Pay Per Crawl adds a <code>cf-pay-per-crawl</code> request header to origin requests so your origin or Worker can determine the appropriate price.</p>
<p>Refer to the <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration documentation</a> for details.</p>


<h2 id="terraform-v5-20-0-now-available"><a href="/changelog/post/2026-06-12-terraform-v5.20.0-provider/">Terraform v5.20.0 now available</a></h2>
<p><em>2026-06-12</em></p>
<p>Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 weeks</a> to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-new-resources">New resources</h4>
<ul>
<li><strong>cloudflare_ai_search_namespace:</strong> Manage AI Search namespaces</li>
<li><strong>cloudflare_custom_csr:</strong> Manage custom certificate signing requests</li>
<li><strong>cloudflare_dls_prefix_binding:</strong> Manage DLS regional service prefix bindings</li>
<li><strong>cloudflare_flagship_app:</strong> Manage Flagship feature flag apps</li>
<li><strong>cloudflare_flagship_flag:</strong> Manage Flagship feature flags</li>
<li><strong>cloudflare_google_tag_gateway:</strong> Manage Google Tag Gateway</li>
<li><strong>cloudflare_load_balancer_monitor_group:</strong> Manage load balancer monitor groups</li>
<li><strong>cloudflare_oauth_client:</strong> Manage IAM OAuth clients</li>
<li><strong>cloudflare_origin_cloud_region:</strong> Manage origin cloud regions (v2 endpoints)</li>
<li><strong>cloudflare_secrets_store:</strong> Manage Secrets Store instances</li>
<li><strong>cloudflare_secrets_store_secret:</strong> Manage Secrets Store secrets</li>
<li><strong>cloudflare_share:</strong> Manage resource shares</li>
<li><strong>cloudflare_share_recipient:</strong> Manage share recipients</li>
<li><strong>cloudflare_share_resource:</strong> Manage shared resources</li>
<li><strong>cloudflare_zero_trust_device_deployment_groups:</strong> Manage Zero Trust device deployment groups</li>
<li><strong>cloudflare_zero_trust_dlp_data_class:</strong> Manage DLP data classes</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag:</strong> Manage DLP data tags</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag_category:</strong> Manage DLP data tag categories</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_group:</strong> Manage DLP sensitivity groups</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level:</strong> Manage DLP sensitivity levels</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level_order:</strong> Manage DLP sensitivity level ordering</li>
<li><strong>cloudflare_zero_trust_resource_library_application:</strong> Manage Zero Trust resource library applications</li>
<li><strong>cloudflare_zero_trust_resource_library_category:</strong> Manage Zero Trust resource library categories</li>
<li><strong>cloudflare_zero_trust_tunnel_warp_connector_config:</strong> Manage WARP connector tunnel configurations</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-features">Features</h4>
<ul>
<li><strong>cache:</strong> add create (POST) method for smart_tiered_cache</li>
<li><strong>cache:</strong> update OPCR config to v2 endpoints</li>
<li><strong>dlp:</strong> promote classification Stainless config to main</li>
<li><strong>dlp:</strong> add custom prompt topics endpoint</li>
<li><strong>email_security_block_sender:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_impersonation_registry:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_trusted_domains:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>snippets:</strong> add Terraform <code>id_property</code> annotations for snippet and snippet_rules</li>
<li>bump Go SDK to cloudflare-go v7</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_member:</strong> missing upgrade path from v5.0–v5.15</li>
<li><strong>authenticated_origin_pulls_settings:</strong> nil pointer panic</li>
<li><strong>bot_management:</strong> restore <code>content_bots_protection</code> handling in model.go</li>
<li><strong>dns_record:</strong> prevent FQDN normalization from swallowing name shortening changes</li>
<li><strong>list:</strong> nullify empty nested objects to prevent inconsistent result after apply</li>
<li><strong>load_balancer_pool:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>load_balancer_pool:</strong> add <code>UseStateForUnknown</code> for <code>load_shedding</code> attribute to prevent drift</li>
<li><strong>r2_custom_domain:</strong> restore degraded-response handling in resource.go</li>
<li><strong>regional_hostname:</strong> update cloudflare-go imports from v6 to v7</li>
<li><strong>secrets_store:</strong> fix model/schema parity and guard acceptance tests</li>
<li><strong>spectrum_application:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>worker:</strong> preserve <code>observability.traces.propagation_policy</code> across reads</li>
<li><strong>worker:</strong> add <code>propagation_policy</code> to observability defaults</li>
<li><strong>worker_version:</strong> restore handwritten D1 <code>database_id</code> handling</li>
<li><strong>workers_custom_domain:</strong> missing <code>CertId</code> field in state migration</li>
<li><strong>workers_script:</strong> restore annotations Read workaround stripped by codegen</li>
<li><strong>zero_trust_access_identity_provider:</strong> change <code>read_only</code> from computed to optional</li>
<li><strong>zero_trust_access_identity_provider:</strong> add <code>UseStateForUnknown</code> to SAML-only config fields</li>
<li><strong>zero_trust_access_identity_provider:</strong> use <code>UseNonNullStateForUnknown</code> on scim_config fields</li>
<li><strong>zero_trust_access_policy:</strong> populate <code>account_id</code> when migrating zone-scoped v4 state</li>
<li><strong>zero_trust_access_policy:</strong> missing <code>common_names</code> transform in migration</li>
<li>gracefully handle nil pointer dereference when config has <code>attributes_flat</code> during migration</li>
<li>set initial schema version to 500 for all new resources</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-refactors">Refactors</h4>
<p>Extracted <code>MoveState</code> nil guard into shared helper</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="introducing-self-managed-oauth-clients"><a href="/changelog/post/2026-06-03-public-oauth-clients/">Introducing self-managed OAuth clients</a></h2>
<p><em>2026-06-03</em></p>
<p>Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.</p>
<p>OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.</p>
<h4 id="2026-06-03-public-oauth-clients-what-is-new">What is new</h4>
<p>Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.</p>
<h4 id="2026-06-03-public-oauth-clients-create-an-application">Create an application</h4>
<p>To create an application, go to <strong>Manage account</strong> &gt; <strong>OAuth clients</strong> in your account on the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<h4 id="2026-06-03-public-oauth-clients-select-limited-scopes">Select limited scopes</h4>
<p>If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.</p>
<p>Users can review the requested scopes before they consent.</p>
<h4 id="2026-06-03-public-oauth-clients-apps-for-both-private-and-public-use">Apps for both private and public use</h4>
<p>Applications start with <code>private</code> visibility. Private applications can only be used by members of the account where the application was created.</p>
<p>To make an application available to any Cloudflare user, complete the prerequisites for <code>public</code> visibility.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients">client visibility</a>.</p>
<h4 id="2026-06-03-public-oauth-clients-client-domain-verification">Client domain verification</h4>
<p>Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.</p>
<p>After verification, users see a verified badge on the consent page.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification">domain verification</a>.</p>
<h4 id="2026-06-03-public-oauth-clients-learn-more">Learn more</h4>
<p>For more information, refer to <a href="/fundamentals/oauth/">OAuth clients</a>.</p>


<h2 id="new-turnstile-events-logpush-dataset-in-cloudflare-logs"><a href="/changelog/post/2026-06-01-log-fields-updated/">New Turnstile Events Logpush dataset in Cloudflare Logs</a></h2>
<p><em>2026-06-01</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-01-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Turnstile Events</strong>: A new dataset with fields including <code>ASN</code>, <code>Action</code>, <code>BrowserMajor</code>, <code>BrowserName</code>, <code>ClientIP</code>, <code>CountryCode</code>, <code>EventType</code>, <code>Hostname</code>, <code>OSMajor</code>, <code>OSName</code>, <code>Sitekey</code>, <code>Timestamp</code>, and <code>UserAgent</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs-1"><a href="/changelog/post/2026-05-29-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-05-29</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-29-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>DEX Device State Events</strong> (added): <code>DeviceRegistrationProfileID</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>AddedHeaders</code>, <code>DeletedHeaders</code>, and <code>SetHeaders</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>MatchedRules</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="cloudflare-tunnel-now-runs-connectivity-pre-checks-at-startup"><a href="/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/">Cloudflare Tunnel now runs connectivity pre-checks at startup</a></h2>
<p><em>2026-05-27</em></p>
<p>Starting with <a href="https://github.com/cloudflare/cloudflared/releases"><code>cloudflared</code> version 2026.5.2</a>, <a href="/tunnel/">Cloudflare Tunnel</a> automates the entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">connectivity pre-checks workflow</a> directly inside the binary. Previously, customers had to install <code>dig</code> and <code>netcat</code> and run those commands by hand to verify their environment. Now <code>cloudflared</code> does it natively at startup — and surfaces actionable remediation when something is blocked.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/cloudflared-connectivity-prechecks.gif" alt="cloudflared connectivity pre-checks output" /></p>
<p>On every <code>cloudflared tunnel run</code> (and <code>cloudflared tunnel diag</code>), the binary now natively checks:</p>
<ul>
<li><strong>DNS resolution</strong> — <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code> resolve to valid Cloudflare IPs.</li>
<li><strong>Transport connectivity</strong> — outbound <code>UDP (QUIC)</code> and <code>TCP (HTTP/2)</code> on port <code>7844</code>.</li>
<li><strong>Management API</strong> — outbound <code>TCP/443</code> to <code>api.cloudflare.com</code> for software updates.</li>
</ul>
<p>Results are printed in a scannable CLI table with three states:</p>
<ul>
<li>✅ <strong>Pass</strong> — the check succeeded.</li>
<li>⚠️ <strong>Warn</strong> — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.</li>
<li>❌ <strong>Fail</strong> — a blocking issue, with a specific remediation hint (for example, <code>Allow outbound UDP on port 7844</code>).</li>
</ul>
<p>If DNS is unresolvable, or <strong>both</strong> UDP and TCP fail on port 7844, <code>cloudflared</code> exits early with the failure rather than looping on opaque <code>failed to dial</code> errors.</p>
<p>Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.</p>
<p>To get the new behavior, upgrade <code>cloudflared</code> to version <code>2026.5.2</code> or later. For more details, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">Connectivity pre-checks documentation</a>.</p>


<h2 id="modernized-billing-profile-with-new-payment-options"><a href="/changelog/post/2026-05-21-modernised-billing-profile/">Modernized Billing Profile with new payment options</a></h2>
<p><em>2026-05-21</em></p>
<p>The <a href="/billing/get-started/update-billing-info/">Billing Profile</a> now has a modern UI and a single space that unifies billing information, payment method management and an enhanced subscriptions view under a single <strong>Subscriptions</strong> tab.</p>
<h4 id="2026-05-21-modernised-billing-profile-what-changed">What changed</h4>
<p>The <strong>Subscriptions</strong> tab brings billing information, payment method management, and your subscriptions together in one place. The payment management and <strong>Pay overdue balances</strong> flows now use the latest checkout as product purchase flows, so you can pay with Apple Pay, Google Pay, Link, and <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a> alongside cards and PayPal.</p>
<p>New cards complete 3D Secure authentication when the issuer requires it — for example, the EU under PSD2 and India under RBI.</p>
<p><img src="/assets/upstream/images/changelog/billing/2026-05-21-modernised-billing-profile.png" alt="Modernized Billing Profile with the Subscriptions tab" /></p>
<p>For details, refer to the <a href="/billing/">Billing Home</a> documentation.</p>


<h2 id="granular-permissions-for-cloudflare-tunnel-and-cloudflare-mesh"><a href="/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a></h2>
<p><em>2026-05-21</em></p>
<p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the resource picker now lists <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes as scopable resource types. You can:</p>
<ul>
<li>Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.</li>
<li>Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.</li>
<li>Scope a single policy to one or many Tunnels and Mesh nodes at once.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-how-it-works">How it works</h4>
<p>Granular permissions are a parallel layer to existing account-level roles — they do not replace them.</p>
<ul>
<li><strong>Existing account-level roles continue to work.</strong> A member with <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.</li>
<li><strong>Granular permissions are additive.</strong> For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong> the account-level role <strong>or</strong> a granular permission for that resource.</li>
<li><strong>Resource enumeration is authorization-aware.</strong> Listing endpoints (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-get-started">Get started</h4>
<ul>
<li>Configure <a href="/tunnel/guides/granular-permissions/">granular permissions for Cloudflare Tunnel</a>.</li>
<li>Configure <a href="/cloudflare-one/networks/connectors/granular-permissions/">granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a>.</li>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
</ul>


<h2 id="new-logpush-datasets-and-updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-05-13-log-fields-updated/">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-05-13</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-13-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Email Security Post-Delivery Events</strong>: A new dataset with fields including <code>AlertID</code>, <code>CompletedAt</code>, <code>Destination</code>, <code>FinalDisposition</code>, <code>Folder</code>, <code>From</code>, <code>FromName</code>, <code>MessageID</code>, <code>MessageTimestamp</code>, <code>MicrosoftTenantID</code>, <code>Operation</code>, <code>PostfixID</code>, <code>Reasons</code>, <code>Recipient</code>, <code>RequestedAt</code>, <code>RequestedBy</code>, <code>RequestedDisposition</code>, <code>Status</code>, <code>Subject</code>, <code>Success</code>, and <code>To</code>.</li>
<li><strong>Magic Network Monitoring Flow Logs</strong>: A new dataset with fields including <code>AWSVPCFlowJSON</code>, <code>Bits</code>, <code>DestinationAS</code>, <code>DestinationAddress</code>, <code>DestinationPort</code>, <code>DeviceID</code>, <code>EgressBits</code>, <code>EgressPackets</code>, <code>Ethertype</code>, <code>FlowProtocol</code>, <code>FlowTimestamp</code>, <code>NumFlows</code>, <code>PacketID</code>, <code>Packets</code>, <code>Protocol</code>, <code>RuleIDs</code>, <code>SampleRate</code>, <code>SampleRateType</code>, <code>SamplerAddress</code>, <code>SourceAS</code>, <code>SourceAddress</code>, <code>SourcePort</code>, <code>TcpFlags</code>, and <code>Timestamp</code>.</li>
</ul>
<h4 id="2026-05-13-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, and <code>AISecurityUnsafeTopicCategories</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, <code>AISecurityUnsafeTopicCategories</code>, and <code>Subrequests</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="keyboard-shortcuts-for-the-cloudflare-dashboard"><a href="/changelog/post/2026-05-04-keyboard-shortcuts/">Keyboard shortcuts for the Cloudflare dashboard</a></h2>
<p><em>2026-05-04</em></p>
<p>You can now navigate, switch context, and take common actions in the Cloudflare dashboard without leaving your keyboard. Press <code>?</code> anywhere to see the full list. Keyboard shortcuts can be disabled by visiting your <a href="https://dash.cloudflare.com/profile/settings">profile settings</a>.</p>
<h4 id="2026-05-04-keyboard-shortcuts-navigate">Navigate</h4>
<table>
<thead>
<tr>
<th>Shortcut</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>g h</code></td>
<td>Go to Home</td>
</tr>
<tr>
<td><code>g a</code></td>
<td>Go to account overview</td>
</tr>
<tr>
<td><code>g z</code></td>
<td>Go to zone overview</td>
</tr>
<tr>
<td><code>g p</code></td>
<td>Go to your profile</td>
</tr>
<tr>
<td><code>g w</code></td>
<td>Go to Workers &amp; Pages</td>
</tr>
<tr>
<td><code>g o</code></td>
<td>Go to Zero Trust</td>
</tr>
<tr>
<td><code>g b</code></td>
<td>Go to billing</td>
</tr>
<tr>
<td><code>g 1</code> – <code>g 5</code></td>
<td>Go to a recent or pinned item (by position in sidebar)</td>
</tr>
<tr>
<td><code>t →</code></td>
<td>Move to the next tab</td>
</tr>
<tr>
<td><code>t ←</code></td>
<td>Move to the previous tab</td>
</tr>
<tr>
<td><code>p →</code></td>
<td>Move to the next page of a table</td>
</tr>
<tr>
<td><code>p ←</code></td>
<td>Move to the previous page of a table</td>
</tr>
</tbody>
</table>
<h4 id="2026-05-04-keyboard-shortcuts-take-action">Take action</h4>
<table>
<thead>
<tr>
<th>Shortcut</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td>Open quick search</td>
</tr>
<tr>
<td><code>?</code></td>
<td>Show keyboard shortcuts</td>
</tr>
<tr>
<td><code>s a</code></td>
<td>Switch account</td>
</tr>
<tr>
<td><code>s z</code></td>
<td>Switch zone</td>
</tr>
<tr>
<td><code>s .</code></td>
<td>Star or unstar the current zone</td>
</tr>
<tr>
<td><code>p .</code></td>
<td>Pin or unpin the current page</td>
</tr>
<tr>
<td><code>t s</code></td>
<td>Toggle the sidebar open or closed</td>
</tr>
<tr>
<td><code>t m</code></td>
<td>Expand or collapse all sidebar menus</td>
</tr>
<tr>
<td><code>t a</code></td>
<td>Toggle Ask AI sidebar</td>
</tr>
<tr>
<td><code>d .</code></td>
<td>Toggle dark mode</td>
</tr>
<tr>
<td><code>c u</code></td>
<td>Copy the current URL</td>
</tr>
<tr>
<td><code>c d</code></td>
<td>Copy a deep link URL</td>
</tr>
</tbody>
</table>


<h2 id="go-sdk-v7-0-0-released"><a href="/changelog/post/2026-04-30-go-sdk-v7.0.0/">Go SDK v7.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0">v6.10.0...v7.0.0</a></p>
<p>This is a major version release that includes breaking changes to three packages: <code>ai_search</code>, <code>email_security</code>, and <code>workers</code>. These changes reflect upstream API specification updates that improve type correctness and consistency.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">v7.0.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-searchforagents-metadata-removed">AI Search - SearchForAgents Metadata Removed</h4>
<p>The <code>SearchForAgents</code> nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.</p>
<p><strong>Removed Types:</strong></p>
<ul>
<li><code>InstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>InstanceListResponseMetadataSearchForAgents</code></li>
<li><code>InstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>InstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>InstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceListResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateParamsMetadataSearchForAgents</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-path-parameter-type-changes">Email Security - Path Parameter Type Changes</h4>
<p>Multiple Email Security settings sub-resources have changed their path parameter types from <code>int64</code> to <code>string</code>:</p>
<ul>
<li><code>AllowPolicies</code> (<code>policyID int64</code> -&gt; <code>policyID string</code>)</li>
<li><code>BlockSenders</code> (<code>patternID int64</code> -&gt; <code>patternID string</code>)</li>
<li><code>Domains</code> (<code>domainID int64</code> -&gt; <code>domainID string</code>)</li>
<li><code>ImpersonationRegistry</code> (<code>displayNameID int64</code> -&gt; <code>impersonationRegistryID string</code>)</li>
<li><code>TrustedDomains</code> (<code>trustedDomainID int64</code> -&gt; <code>trustedDomainID string</code>)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-parameter-rename">Email Security - Investigate Parameter Rename</h4>
<p>The <code>Investigate.Get</code>, <code>Investigate.Move.New</code>, and <code>Investigate.Reclassify.New</code> methods now use <code>investigateID</code> instead of <code>postfixID</code> as the path parameter name.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-domains-bulkdelete-method-removed">Email Security - Domains BulkDelete Method Removed</h4>
<p>The <code>SettingDomainService.BulkDelete</code> method and its associated types have been removed:</p>
<ul>
<li><code>SettingDomainBulkDeleteResponse</code></li>
<li><code>SettingDomainBulkDeleteParams</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-trusteddomains-return-type-change">Email Security - TrustedDomains Return Type Change</h4>
<p><code>SettingTrustedDomainService.New</code> now returns <code>*SettingTrustedDomainNewResponse</code> instead of <code>*SettingTrustedDomainNewResponseUnion</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-move-return-type-change">Email Security - Investigate.Move Return Type Change</h4>
<p><code>InvestigateMoveService.New</code> now returns <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code> instead of <code>*[]InvestigateMoveNewResponse</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-workers-observability-telemetry-filter-restructuring">Workers - Observability Telemetry Filter Restructuring</h4>
<p>The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:</p>
<ul>
<li><code>ObservabilityTelemetryKeysParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code> (was <code>[]interface\{\}</code>)</li>
<li><code>ObservabilityTelemetryQueryParams.Parameters.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
<li><code>ObservabilityTelemetryValuesParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
</ul>
<p>New types include <code>FiltersObjectFiltersObject</code> (for group filters with <code>FilterCombination</code>) and <code>FiltersWorkersObservabilityFilterLeaf</code> (for leaf filters with typed <code>Operation</code>, <code>Type</code>, and <code>Value</code> fields).</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-features">Features</h4>
<h4 id="2026-04-30-go-sdk-v7.0.0-organizations-audit-logs-client-organizations-logs-audit">Organizations - Audit Logs (<code>client.Organizations.Logs.Audit</code>)</h4>
<p><strong>NEW SERVICE:</strong> Query organization audit logs with cursor-based pagination.</p>
<ul>
<li><code>List()</code> - Retrieve audit logs</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-browser-rendering-client-browserrendering">Browser Rendering (<code>client.BrowserRendering</code>)</h4>
<ul>
<li><code>client.BrowserRendering.Devtools.Browser.Targets.Close()</code> - Close a specific browser target (tab, page) by ID</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-queues-client-queues">Queues (<code>client.Queues</code>)</h4>
<ul>
<li><code>client.Queues.GetMetrics()</code> - Retrieve queue metrics for a specific queue</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-client-aisearch">AI Search (<code>client.AISearch</code>)</h4>
<ul>
<li>Added <code>WaitForCompletion</code> parameter to <code>NamespaceInstanceItemNewOrUpdateParams</code> and <code>NamespaceInstanceItemSyncParams</code> for synchronous indexing confirmation</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>Magic Transit</strong>: <code>ConnectorService.List</code> parameter name corrected from <code>query</code> to <code>params</code> (non-functional, affects generated documentation only)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0">Download Go SDK v7.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">Migration Guide</a></li>
</ul>


<h2 id="cloudflare-python-sdk-v5-0-0-released"><a href="/changelog/post/2026-04-30-cloudflare-python-v5.0.0/">Cloudflare Python SDK v5.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0">v4.3.1...v5.0.0</a></p>
<p>This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.</p>
<p><strong>Please review the breaking changes below before upgrading.</strong> A migration guide is available at <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a>.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-breaking-changes">Breaking Changes</h4>
<ul>
<li><strong>Python 3.8 is no longer supported.</strong> The minimum required version is now Python 3.9.</li>
<li><strong><code>typing-extensions</code> minimum version bumped</strong> from <code>&gt;=4.10</code> to <code>&gt;=4.14</code>.</li>
</ul>
<p>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a> for detailed migration instructions.</p>
<ul>
<li><code>abusereports</code></li>
<li><code>acm.totaltls</code></li>
<li><code>apigateway.configurations</code></li>
<li><code>cloudforceone.threatevents</code></li>
<li><code>d1.database</code></li>
<li><code>intel.indicatorfeeds</code></li>
<li><code>logpush.edge</code></li>
<li><code>origintlsclientauth.hostnames</code></li>
<li><code>queues.consumers</code></li>
<li><code>radar.bgp</code></li>
<li><code>rulesets.rules</code></li>
<li><code>schemavalidation.schemas</code></li>
<li><code>snippets</code></li>
<li><code>zerotrust.dlp</code></li>
<li><code>zerotrust.networks</code></li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-features">Features</h4>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-aiohttp-backend-support">aiohttp Backend Support</h4>
<p>The async client now supports an optional <code>aiohttp</code> HTTP backend for improved concurrency performance. Install with <code>pip install cloudflare[aiohttp]</code> and use <code>DefaultAioHttpClient()</code> as the <code>http_client</code> parameter.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-python-3-13-and-3-14-support">Python 3.13 and 3.14 Support</h4>
<p>Python 3.13 and 3.14 are now tested and supported.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-services">New Services</h4>
<p>The following top-level resources are new in this release:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>aisearch</code></td>
<td>AI-powered search capabilities</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>connectivity</code></td>
<td>Connectivity testing and diagnostics</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>email_sending</code></td>
<td>Email send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>fraud</code></td>
<td>Fraud detection and prevention</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>google_tag_gateway</code></td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>organizations</code></td>
<td>Organization audit logs and management</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>r2_data_catalog</code></td>
<td>R2 Data Catalog operations</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>realtime_kit</code></td>
<td>Realtime communication (Calls/TURN)</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>resource_tagging</code></td>
<td>Resource tagging and labeling</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>token_validation</code></td>
<td>Token validation configuration and rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>vulnerability_scanner</code></td>
<td>Vulnerability scanning, credential sets, and target environments</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-endpoints-on-existing-services">New Endpoints on Existing Services</h4>
<ul>
<li><strong>api_gateway</strong>: Labels endpoints</li>
<li><strong>billing</strong>: Billable usage PayGo endpoint</li>
<li><strong>brand_protection</strong>: v2 endpoints</li>
<li><strong>browser_rendering</strong>: DevTools methods</li>
<li><strong>cache</strong>: Origin cloud regions resource</li>
<li><strong>custom_origin_trust_store</strong>: Custom origin trust store</li>
<li><strong>dns</strong>: <code>dns_records/usage</code> endpoints</li>
<li><strong>email_security</strong>: Phishguard reports endpoint</li>
<li><strong>iam</strong>: User groups and user group members resources</li>
<li><strong>radar</strong>: Botnet Threat Feed and Post-Quantum endpoints</li>
<li><strong>workers</strong>: Observability Destinations resources</li>
<li><strong>zero_trust</strong>: Access Users, DEX rules, Device IP Profile, Device Subnet, WARP Connector connections and failover, WARP Subnet, Gateway PAC files</li>
<li><strong>zones</strong>: Zone environments endpoints</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Fixed <code>polymorphic_serialization</code> parameter in <code>model_dump</code> overrides</li>
<li>Added <code>BaseModel</code> base to response <code>SchemaFieldStruct</code>/<code>SchemaFieldList</code> stubs in Pipelines</li>
<li>Added missing <code>model_rebuild</code>/<code>update_forward_refs</code> for <code>SharedEntryCustomEntry</code> classes in DLP</li>
<li>Made <code>RunQueryParametersNeedleValue</code> a <code>BaseModel</code> with <code>arbitrary_types_allowed</code> in Workers</li>
<li>Removed duplicate <code>notification_url</code> field in webhook response types for Stream</li>
<li>Resolved pre-existing codegen type errors</li>
<li>Fixed <code>type: ignore[call-arg]</code> placement for mypy compatibility in Radar</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-deprecations">Deprecations</h4>
<p>Resources with <code>@deprecated</code> annotations on some methods include: <code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0">Download Python SDK v5.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/python/">Python SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">Migration Guide</a></li>
</ul>


<h2 id="cloudflare-typescript-sdk-v6-0-0-released"><a href="/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/">Cloudflare TypeScript SDK v6.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0">v6.0.0-beta.2...v6.0.0</a></p>
<p>This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-breaking-changes">Breaking Changes</h4>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-sdk-infrastructure">SDK Infrastructure</h4>
<ul>
<li><strong>Retry-After handling changed</strong>: The SDK now respects any server-specified <code>Retry-After</code> value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.</li>
<li><strong>Empty response handling</strong>: Responses with <code>content-length: 0</code> now return <code>undefined</code> instead of attempting to parse the body.</li>
<li><strong>Environment variable reading</strong>: Empty string env vars (for example, <code>CLOUDFLARE_API_TOKEN=&quot;&quot;</code>) are now treated as unset.</li>
<li><strong>Path query parameter merging</strong>: URL search params embedded in endpoint paths are now extracted and merged into the query object.</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-endpoints-17">Removed Endpoints (17)</h4>
<p>17 HTTP endpoints were removed from the SDK, affecting <code>abuse-reports</code>, <code>cloudforce-one</code>, <code>dlp/profiles/predefined</code>, <code>email-security/investigate</code>, <code>email-security/settings</code>, and <code>intel/ip-list</code>.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-method-signature-changes">Method Signature Changes</h4>
<ul>
<li><code>client.ai.toMarkdown.transform(file, \{ ...params \})</code> -&gt; <code>client.ai.toMarkdown.transform(\{ ...params \})</code> -- <code>file</code> moved from positional arg into params body</li>
<li><code>client.radar.ai.toMarkdown.create(body, \{ ...params \})</code> -&gt; <code>client.radar.ai.toMarkdown.create(\{ ...params \})</code> -- <code>body</code> moved from positional arg into params</li>
<li><code>client.abuseReports.create(reportType, \{ ...params \})</code> -&gt; <code>client.abuseReports.create(reportParam, \{ ...params \})</code> -- positional arg renamed</li>
<li><code>client.iam.userGroups.members.create(userGroupId, [ ...body ])</code> -&gt; <code>client.iam.userGroups.members.create(userGroupId, [ ...members ])</code> -- body array param renamed</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-renamed-client-paths">Renamed Client Paths</h4>
<ul>
<li><code>client.originTLSClientAuth.hostnames.certificates</code> -&gt; <code>client.originTLSClientAuth.zoneCertificates</code></li>
<li><code>client.radar.netflows</code> -&gt; <code>client.radar.netFlows</code> (casing change)</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-return-type-changes-179">Return Type Changes (179)</h4>
<ul>
<li><strong>133 methods now return <code>null</code></strong> instead of a typed response object. This primarily affects delete operations across <code>accounts</code>, <code>cache</code>, <code>d1</code>, <code>filters</code>, <code>firewall</code>, <code>hyperdrive</code>, <code>iam</code>, <code>kv</code>, <code>logpush</code>, <code>logs</code>, <code>r2</code>, <code>stream</code>, <code>workers</code>, <code>zero-trust</code>, <code>zones</code>, and others.</li>
<li><strong>17 methods changed pagination type</strong> (for example, <code>KeysCursorPaginationAfter</code> -&gt; <code>KeysCursorLimitPagination</code>).</li>
<li><strong>29 methods changed to a different named type</strong> (for example, <code>CloudflaredCreateResponse</code> -&gt; <code>CloudflareTunnel</code>).</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-types-43">Removed Types (43)</h4>
<p>24 shared types removed from root namespace (<code>ASN</code>, <code>AuditLog</code>, <code>Member</code>, <code>Permission</code>, <code>Role</code>, <code>Subscription</code>, <code>Token</code>, etc.). 19 response types consolidated or renamed.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-resource-restructuring">Resource Restructuring</h4>
<p>19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-top-level-resources">New Top-Level Resources</h4>
<p>11 entirely new resources added to the client:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>client.aiSearch</code></td>
<td>46</td>
<td>Instances, namespaces, tokens, and items</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>client.connectivity</code></td>
<td>5</td>
<td>Directory service APIs</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>client.emailSending</code></td>
<td>7</td>
<td>Send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>client.fraud</code></td>
<td>2</td>
<td>Fraud detection API</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>client.googleTagGateway</code></td>
<td>2</td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>client.organizations</code></td>
<td>8</td>
<td>Organization profiles and audit logs</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>client.r2DataCatalog</code></td>
<td>11</td>
<td>R2 Data Catalog routes</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>client.realtimeKit</code></td>
<td>54</td>
<td>Realtime Kit APIs</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>client.resourceTagging</code></td>
<td>9</td>
<td>Resource tagging routes</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>client.tokenValidation</code></td>
<td>13</td>
<td>Token validation rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>client.vulnerabilityScanner</code></td>
<td>21</td>
<td>Vulnerability scanning</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-sub-resources-on-existing-resources">New Sub-Resources on Existing Resources</h4>
<ul>
<li><strong>browser-rendering</strong>: <code>crawl</code>, <code>devtools</code> - Crawl endpoints and DevTools methods</li>
<li><strong>cache</strong>: <code>origin-cloud-regions</code> - Origin cloud regions resource</li>
<li><strong>dns</strong>: <code>usage</code> - DNS records usage endpoints</li>
<li><strong>d1</strong>: <code>time-travel</code> - Time travel get_bookmark and restore</li>
<li><strong>email-security</strong>: <code>phishguard</code> - Phishguard reports endpoint</li>
<li><strong>pipelines</strong>: <code>sinks</code>, <code>streams</code> - Pipelines restructure</li>
<li><strong>radar</strong>: <code>agent-readiness</code>, <code>geolocations</code>, <code>post-quantum</code> - New analytics endpoints</li>
<li><strong>workers</strong>: <code>observability</code> - Observability destinations</li>
<li><strong>zones</strong>: <code>environments</code> - Zone environments endpoints</li>
<li><strong>api-gateway</strong>: <code>labels</code> - Labels endpoints</li>
<li><strong>brand-protection</strong>: <code>v2</code> - V2 endpoints</li>
<li><strong>alerting</strong>: <code>silences</code> - Alert silencing API</li>
<li><strong>billing</strong>: <code>usage</code> - Billable usage PayGo endpoint</li>
<li><strong>iam</strong>: <code>sso</code> - SSO Connectors resource</li>
<li><strong>queues</strong>: <code>getMetrics</code> method - Queues metrics endpoint</li>
<li><strong>registrar</strong>: <code>registration-status</code>, <code>update-status</code> - Registrar API convergence</li>
<li><strong>zero-trust</strong>: DLP settings, DEX rules, Access Users, WARP Connector, WARP Subnets, Gateway PAC files, Gateway tenants</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Resolved type errors from codegen overwriting manual fixes</li>
<li>Fixed <code>post()</code> usage for to-markdown endpoints to resolve async type error</li>
<li>Added least-privilege permissions to all workflow jobs</li>
<li>Reverted erroneous removal of rulesets resource methods and types</li>
<li>Resolved prettier formatting errors in codegen output</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-deprecations">Deprecations</h4>
<p>The following resources now include <code>@deprecated</code> annotations on some methods:</p>
<p><code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>custom-nameservers</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>keyless-certificates</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>page-shield</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0">Download TypeScript SDK v6.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/typescript/">TypeScript SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md">Full Changelog</a></li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/">Previous</a><span>Page 2 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/3/">Next</a></nav>
