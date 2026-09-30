---
cp9:
  canonical: https://developers.cloudflare.com/spectrum/reference/settings-by-plan/
  description: Spectrum API fields and settings available by Cloudflare plan.
  full_title: Settings by plan · Cloudflare Spectrum docs
  head_html: <title>Settings by plan · Cloudflare Spectrum docs</title><meta name="generator" content="Nift"><meta name="description" content="Spectrum API fields and settings available by Cloudflare plan."><link rel="canonical" href="https://developers.cloudflare.com/spectrum/reference/settings-by-plan/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/spectrum/reference/settings-by-plan/index.md"><meta property="og:title" content="Settings by plan · Cloudflare Spectrum docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Spectrum API fields and settings available by Cloudflare plan."><meta property="og:url" content="https://developers.cloudflare.com/spectrum/reference/settings-by-plan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Spectrum"><meta name="algolia_product_filter" content="Spectrum"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Spectrum"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/spectrum/reference/settings-by-plan/#page","headline":"Settings by plan \u00b7 Cloudflare Spectrum docs","description":"Spectrum API fields and settings available by Cloudflare plan.","url":"https://developers.cloudflare.com/spectrum/reference/settings-by-plan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /spectrum/reference/settings-by-plan/
  schema: 1
---
<p>Certain fields in Spectrum request and response bodies require an Enterprise plan. To upgrade your plan, contact your account team.</p>
<p>Spectrum properties requiring an Enterprise plan:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>origin_dns</code></td>
<td>object</td>
<td>Method and parameters used to discover the origin server address via DNS. Valid record types are <code>A</code>, <code>AAAA</code>, <code>SRV</code> and empty (both <code>A</code> and <code>AAA</code>).<br />A request must contain either an <code>origin_dns</code> parameter or an <code>origin_direct</code> parameter. When both are specified the service returns an <code>HTTP 400 Bad Request</code>.</td>
<td><code>origin_dns: {type: A, name: mqtt.example.com, ttl: 1200}</code></td>
</tr>
<tr>
<td><code>origin_port</code></td>
<td>integer</td>
<td>The destination port at the origin.</td>
<td><code>22</code></td>
</tr>
<tr>
<td><code>proxy_protocol</code></td>
<td>string</td>
<td>Enables Proxy Protocol to the origin. Spectrum supports <code>v1</code>, <code>v2</code>, and <code>simple</code> proxy protocols. Refer to <a href="/spectrum/how-to/enable-proxy-protocol/">Proxy Protocol</a> for more details.</td>
<td><code>off</code></td>
</tr>
<tr>
<td><code>ip_firewall</code></td>
<td>boolean</td>
<td>Enables IP Access rules for this application.</td>
<td><code>true</code></td>
</tr>
<tr>
<td><code>tls</code></td>
<td>string</td>
<td>Type of TLS termination for the application. Options are <code>off</code> (default, also known as Passthrough), <code>flexible</code>, <code>full</code>, and <code>strict</code>. Refer to <a href="/spectrum/reference/configuration-options/">Configuration Options</a> for descriptions of each.</td>
<td><code>full</code></td>
</tr>
<tr>
<td><code>argo_smart_routing</code></td>
<td>boolean</td>
<td>Enables Argo Smart Routing for the application. Note that it is only available for TCP applications with traffic_type set to <code>direct</code>.</td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<p>Review the <a href="/api/resources/spectrum/subresources/apps/methods/list/">Spectrum API documentation</a> for example API requests.</p>
