---
cp9:
  canonical: https://developers.cloudflare.com/network/grpc-connections/
  description: Protect gRPC APIs on proxied endpoints with Cloudflare.
  full_title: gRPC connections · Cloudflare Network settings docs
  head_html: <title>gRPC connections · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Protect gRPC APIs on proxied endpoints with Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/network/grpc-connections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/grpc-connections/index.md"><meta property="og:title" content="gRPC connections · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect gRPC APIs on proxied endpoints with Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/network/grpc-connections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/grpc-connections/#page","headline":"gRPC connections \u00b7 Cloudflare Network settings docs","description":"Protect gRPC APIs on proxied endpoints with Cloudflare.","url":"https://developers.cloudflare.com/network/grpc-connections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network/grpc-connections/
  schema: 1
---
<p>Cloudflare offers support for gRPC to protect your APIs on any <a href="/dns/proxy-status/">proxied gRPC endpoints</a>. The gRPC protocol helps build efficient APIs with smaller payloads for reduced bandwidth usage, decreased latency, and faster implementations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/692.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Charges may occur for gRPC traffic over add-on products such as <a href="/argo-smart-routing/">Argo Smart Routing</a>, <a href="/waf/">WAF</a>, and <a href="/bots/">Bot Management</a>.</p>
<h2 id="limitations">Limitations</h2>
<p>Running gRPC traffic on Cloudflare is compatible with most Cloudflare products.</p>
<p>However, the following products have limited capabilities with gRPC requests:</p>
<ul>
<li>The <a href="/waf/">Cloudflare WAF</a> will only run for header inspection during the connection phase. WAF Managed Rules will not run on the content of a gRPC stream.</li>
<li></li>
</ul>
<p>Cloudflare Tunnel supports gRPC traffic via <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private subnet routing</a>. Public hostname deployments are not currently supported.</p>
<ul>
<li><a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> does not support gRPC traffic sent through Cloudflare’s reverse proxy. gRPC traffic will be ignored by Access if gRPC is enabled in Cloudflare. We recommend disabling gRPC for any sensitive origin servers protected by Access or enabling another means of authenticating gRPC traffic to your origin servers.</li>
</ul>
<h2 id="enable-grpc">Enable gRPC</h2>
<h3 id="requirements">Requirements</h3>
<ul>
<li>Your gRPC endpoint must listen on port 443.</li>
<li>Your gRPC endpoint must support TLS and HTTP/2.</li>
<li>HTTP/2 must be advertised over ALPN.</li>
<li>Use <code>application/grpc</code> or <code>application/grpc+&lt;message type</code> (for example: <code>application/grpc+proto</code>) for the <strong>Content-Type</strong> header of gRPC requests.</li>
<li>Make sure that the hostname that hosts your gRPC endpoint:
<ul>
<li>Is set to <a href="/dns/proxy-status/">proxied</a></li>
<li>Uses at least the <a href="/ssl/origin-configuration/ssl-modes/full/">Full SSL/TLS encryption mode</a>.</li>
</ul>
</li>
</ul>
<h3 id="procedure">Procedure</h3>
<p>To change the <strong>gRPC</strong> setting in the dashboard:</p>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com">Cloudflare account</a> and go to a specific domain.</li>
<li>Go to <strong>Network</strong>.</li>
<li>For <strong>gRPC</strong>, switch the toggle to <strong>On</strong>.</li>
</ol>
