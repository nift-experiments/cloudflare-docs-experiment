---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/
  description: New updates and improvements at Cloudflare.
  full_title: Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025 · Changelog
  head_html: <title>Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/#page","headline":"Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 2, 2025</time><h2 id="post-title">Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Starting <strong>December 1, 2025</strong>, list endpoints for the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.</p>
<p>No action is required if you already explicitly set <code>is_deleted=false</code> or if you only need to list active resources.</p>
<p>This change affects the following API endpoints:</p>
<ul>
<li>List all tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/methods/list/"><code>GET /accounts/{account_id}/tunnels</code></a></li>
<li>List <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a></li>
<li>List <a href="/mesh/">WARP Connector</a> tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a></li>
<li>List tunnel routes: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/"><code>GET /accounts/{account_id}/teamnet/routes</code></a></li>
<li>List subnets: <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/"><code>GET /accounts/{account_id}/zerotrust/subnets</code></a></li>
<li>List virtual networks: <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/"><code>GET /accounts/{account_id}/teamnet/virtual_networks</code></a></li>
</ul>
<h4 id="what-is-changing">What is changing?</h4>
<p>The default behavior of the <code>is_deleted</code> query parameter will be updated.</p>
<table>
<thead>
<tr>
<th align="left">Scenario</th>
<th align="left">Previous behavior (before December 1, 2025)</th>
<th align="left">New behavior (from December 1, 2025)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>is_deleted</code> parameter is omitted</td>
<td align="left">Returns <strong>active &amp; deleted</strong> tunnels, routes, subnets and virtual networks</td>
<td align="left">Returns <strong>only active</strong> tunnels, routes, subnets and virtual networks</td>
</tr>
</tbody>
</table>
<h4 id="action-required">Action required</h4>
<p>If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the <code>is_deleted</code> parameter before <strong>December 1, 2025</strong>.</p>
<p>To get a list of only deleted resources, you must now explicitly add the <code>is_deleted=true</code> query parameter to your request:</p>
<pre tabindex="0"><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>
</div></article></div>
