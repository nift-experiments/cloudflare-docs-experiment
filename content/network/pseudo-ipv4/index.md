---
cp9:
  canonical: https://developers.cloudflare.com/network/pseudo-ipv4/
  description: Map IPv6 addresses to IPv4 for legacy origin servers.
  full_title: Pseudo IPv4 · Cloudflare Network settings docs
  head_html: <title>Pseudo IPv4 · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Map IPv6 addresses to IPv4 for legacy origin servers."><link rel="canonical" href="https://developers.cloudflare.com/network/pseudo-ipv4/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/pseudo-ipv4/index.md"><meta property="og:title" content="Pseudo IPv4 · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Map IPv6 addresses to IPv4 for legacy origin servers."><meta property="og:url" content="https://developers.cloudflare.com/network/pseudo-ipv4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/pseudo-ipv4/#page","headline":"Pseudo IPv4 \u00b7 Cloudflare Network settings docs","description":"Map IPv6 addresses to IPv4 for legacy origin servers.","url":"https://developers.cloudflare.com/network/pseudo-ipv4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network/pseudo-ipv4/
  schema: 1
---
<p>Cloudflare customers can use <strong>Pseudo IPv4</strong> if their origin web server only understands IPv4 formatted IP addresses (meaning it would not support Cloudflare's default <a href="/network/ipv6-compatibility/">IPv6 compatibility</a>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/668.md")
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
<h2 id="background">Background</h2>
<p>Some older origin server analytics and fraud detection software expect IP addresses in an IPv4 format and do not support IPv6 addresses.</p>
<p><strong>Pseudo IPv4</strong> uses the <a href="https://tools.ietf.org/html/rfc1112#section-4">Class E IPv4 address space</a> to provide as many unique IPv4 addresses corresponding to IPv6 addresses as possible.</p>
<ul>
<li>Example Class E IPv4 address: <code>240.16.0.1</code></li>
<li>Example IPv6 address: <code>2400:cb00:f00d:dead:beef:1111:2222:3333</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/667.md")
</aside>
<h2 id="configure-pseudo-ipv4">Configure Pseudo IPv4</h2>
<p>Cloudflare offers three options for configuring <strong>Pseudo IPv4</strong>:</p>
<ul>
<li><strong>Off</strong>: Default value.</li>
<li><strong>Add Header</strong>: Cloudflare automatically adds the <code>Cf-Pseudo-IPv4</code> header with a Class E IPv4 address hashed from the original IPv6 address.</li>
<li><strong>Overwrite Headers</strong>:
If <strong>Pseudo IPv4</strong> is set to <code>Overwrite Headers</code> - Cloudflare overwrites the existing <code>Cf-Connecting-IP</code> and <code>X-Forwarded-For</code> headers with a pseudo IPv4 address while preserving the real IPv6 address in <code>CF-Connecting-IPv6</code> header.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/666.md")
</aside>
<p>To configure <strong>Pseudo IPv4</strong>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/671.md")
</div></div>
