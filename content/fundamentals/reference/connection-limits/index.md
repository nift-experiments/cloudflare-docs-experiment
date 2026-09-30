---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/connection-limits/
  description: Review TCP and HTTP connection timeouts between clients, Cloudflare, and origin servers, including keep-alive and request limits.
  full_title: Connection limits · Cloudflare Fundamentals docs
  head_html: <title>Connection limits · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Review TCP and HTTP connection timeouts between clients, Cloudflare, and origin servers, including keep-alive and request limits."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/connection-limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/connection-limits/index.md"><meta property="og:title" content="Connection limits · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review TCP and HTTP connection timeouts between clients, Cloudflare, and origin servers, including keep-alive and request limits."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/connection-limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/connection-limits/#page","headline":"Connection limits \u00b7 Cloudflare Fundamentals docs","description":"Review TCP and HTTP connection timeouts between clients, Cloudflare, and origin servers, including keep-alive and request limits.","url":"https://developers.cloudflare.com/fundamentals/reference/connection-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/connection-limits/
  schema: 1
---
<p>When HTTP/HTTPS traffic is <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">proxied through Cloudflare</a>, there are often two established <a href="/fundamentals/reference/tcp-connections/">TCP connections</a>: the first is between the requesting client to Cloudflare and the second is between Cloudflare and the origin server. Each connection has their own set of TCP and HTTP limits, which are documented below.</p>
<h2 id="between-client-and-cloudflare">Between client and Cloudflare</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Limit (seconds)</th>
<th>HTTP status code at limit</th>
<th>Configurable</th>
</tr>
</thead>
<tbody>
<tr>
<td>Connection Keep-Alive HTTP/1.1</td>
<td>400</td>
<td>TCP connection closed</td>
<td>No</td>
</tr>
<tr>
<td>Connection Idle HTTP/2</td>
<td>400</td>
<td>TCP connection closed</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="between-cloudflare-and-origin-server">Between Cloudflare and origin server</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8798.md")
</aside>
<table>
<thead>
<tr>
<th>Type</th>
<th>Limit (seconds)</th>
<th>HTTP status code at limit</th>
<th><a href="/fundamentals/reference/connection-limits/#configurable-limits">Configurable</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="nb-glossary-tooltip" title="TCP three-way handshake">Complete TCP Connection</span></td>
<td>19</td>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/">522</a></td>
<td>No</td>
</tr>
<tr>
<td><span class="nb-glossary-tooltip" title="ACK (Acknowledge)">TCP ACK</span> Timeout</td>
<td>90</td>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/">522</a></td>
<td>No</td>
</tr>
<tr>
<td><span class="nb-glossary-tooltip" title="TCP Keep-Alive">TCP Keep-Alive</span> Interval</td>
<td>30</td>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520</a></td>
<td>No</td>
</tr>
<tr>
<td><span class="nb-glossary-tooltip" title="idle connection">Proxy Idle</span> Timeout</td>
<td>900</td>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520</a></td>
<td>No</td>
</tr>
<tr>
<td><span class="nb-glossary-tooltip" title="proxy read timeout">Proxy Read Timeout</span></td>
<td>125</td>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524</a></td>
<td><a href="/api/resources/zones/subresources/settings/methods/edit/">Yes, for Enterprise zones</a></td>
</tr>
<tr>
<td><span class="nb-glossary-tooltip" title="proxy write timeout">Proxy Write Timeout</span></td>
<td>30</td>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524</a></td>
<td>No</td>
</tr>
<tr>
<td>HTTP/2 Pings to Origin</td>
<td>Off</td>
<td>-</td>
<td>Yes</td>
</tr>
<tr>
<td><span class="nb-glossary-tooltip" title="idle connection">HTTP/2 Connection Idle</span></td>
<td>900</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="configurable-limits">Configurable limits</h2>
<p>Some TCP connections can be customized for Enterprise customers. Reach out to your account team for more details.</p>
<h2 id="keep-alives">Keep-Alives</h2>
<p>Cloudflare maintains keep-alive connections to improve performance and reduce cost of recurring TCP connects in the request transaction as Cloudflare proxies customer traffic from its global network to the site's origin server.</p>
<p>Ensure HTTP keep-alive connections are enabled on your origin. Cloudflare reuses open TCP connections up to the <code>Proxy Idle Timeout</code> limit after the last HTTP request. Origin web servers close TCP connections if too many are open. HTTP keep-alive helps avoid connection resets for requests proxied by Cloudflare.</p>
<h2 id="request-limits">Request limits</h2>
<p>URLs have a limit of 16 KB. Request headers have a total limit of 128 KB.</p>
<h2 id="response-limits">Response limits</h2>
<p>Response headers observe a total limit of 128 KB.</p>
<h2 id="cache-limits">Cache limits</h2>
<p>Refer to the <a href="/cache/concepts/default-cache-behavior/#customization-options-and-limits">Cache documentation</a> for more details about the max upload size and the cacheable file size limits.</p>
