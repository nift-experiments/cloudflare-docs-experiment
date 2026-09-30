---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/
  description: Restrict admin area access to known IP addresses.
  full_title: Require known IP addresses in site admin area · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Require known IP addresses in site admin area · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict admin area access to known IP addresses."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/index.md"><meta property="og:title" content="Require known IP addresses in site admin area · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict admin area access to known IP addresses."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/#page","headline":"Require known IP addresses in site admin area \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Restrict admin area access to known IP addresses.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/site-admin-only-known-ips/
  schema: 1
---
<p>If an attack compromises the administrative area of your website, the consequences can be severe. With custom rules, you can protect your site's admin area by blocking requests for access to admin paths that do not come from a known IP address.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> limits access to the WordPress admin area, <code>/wp-admin/</code>, by blocking requests that do not originate from a specified set of IP addresses:</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Source Address</td>
<td>is not in</td>
<td><code>10.20.30.40</code> <code>192.168.1.0/24</code></td>
<td>And</td>
</tr>
<tr>
<td>URI Path</td>
<td>wildcard</td>
<td><code>/wp-admin/*</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(not ip.src in {10.20.30.40 192.168.1.0/24} and http.request.uri.path wildcard &quot;/wp-admin/*&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/">Use case: Allow traffic from IP addresses in allowlist only</a></li>
</ul>
