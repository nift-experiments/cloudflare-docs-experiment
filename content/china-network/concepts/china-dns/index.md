---
cp9:
  canonical: https://developers.cloudflare.com/china-network/concepts/china-dns/
  description: Resolve DNS queries in Mainland China to improve Time to First Byte performance.
  full_title: China Authoritative DNS · Cloudflare China Network docs
  head_html: <title>China Authoritative DNS · Cloudflare China Network docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve DNS queries in Mainland China to improve Time to First Byte performance."><link rel="canonical" href="https://developers.cloudflare.com/china-network/concepts/china-dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/china-network/concepts/china-dns/index.md"><meta property="og:title" content="China Authoritative DNS · Cloudflare China Network docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve DNS queries in Mainland China to improve Time to First Byte performance."><meta property="og:url" content="https://developers.cloudflare.com/china-network/concepts/china-dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="China Network"><meta name="algolia_product_filter" content="China Network"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="China Network"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/china-network/concepts/china-dns/#page","headline":"China Authoritative DNS \u00b7 Cloudflare China Network docs","description":"Resolve DNS queries in Mainland China to improve Time to First Byte performance.","url":"https://developers.cloudflare.com/china-network/concepts/china-dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /china-network/concepts/china-dns/
  schema: 1
---
<p>By default, Cloudflare China Network resolves each DNS request at the data center closest to the client. For clients outside of Mainland China, the closest global Cloudflare data center handles the request. For clients in Mainland China, a JD Cloud data center handles the request.</p>
<h2 id="in-china-nameserver">In-China Nameserver</h2>
<p>Cloudflare can deploy DNS service in Mainland China to improve Time to First Byte (TTFB) performance. With this option enabled, DNS queries resolve at data centers in Mainland China instead of at global DNS servers.</p>
<h2 id="when-to-use">When to use</h2>
<p>Before you enable China Authoritative DNS, confirm that the majority (over 90%) of your traffic comes from Mainland China.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3955.md")
</aside>
<h2 id="comparison">Comparison</h2>
<p>The following table compares the default DNS offering with the In-China Nameserver option.</p>
<table>
<thead>
<tr>
<th>DNS option</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Default</td>
<td>Uses the DNS server closest to the end user.</td>
</tr>
<tr>
<td>In-China DNS</td>
<td>Uses only DNS in China, operated by JD Cloud.</td>
</tr>
</tbody>
</table>
<h2 id="general-setup">General setup</h2>
<p>After you <a href="/china-network/get-started/">enable the Cloudflare China Network service</a>, do the following:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3958.md")
</div>
<p>For further assistance, contact your account team.</p>
