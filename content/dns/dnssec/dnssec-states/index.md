---
cp9:
  canonical: https://developers.cloudflare.com/dns/dnssec/dnssec-states/
  description: Possible DNSSEC states and their meanings.
  full_title: DNSSEC states · Cloudflare DNS docs
  head_html: <title>DNSSEC states · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Possible DNSSEC states and their meanings."><link rel="canonical" href="https://developers.cloudflare.com/dns/dnssec/dnssec-states/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dnssec/dnssec-states/index.md"><meta property="og:title" content="DNSSEC states · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Possible DNSSEC states and their meanings."><meta property="og:url" content="https://developers.cloudflare.com/dns/dnssec/dnssec-states/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dnssec/dnssec-states/#page","headline":"DNSSEC states \u00b7 Cloudflare DNS docs","description":"Possible DNSSEC states and their meanings.","url":"https://developers.cloudflare.com/dns/dnssec/dnssec-states/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dnssec/dnssec-states/
  schema: 1
---
<p>This page describes different DNSSEC states and how they relate to the responses you get from the <a href="/api/resources/dns/subresources/dnssec/methods/get/">DNSSEC details API endpoint</a>.</p>
<table>
<thead>
<tr>
<th>State</th>
<th>API response</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pending</td>
<td><code>&quot;status&quot;:&quot;pending&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been enabled but the Cloudflare DS record has not been added at the registrar.</td>
</tr>
<tr>
<td>Active</td>
<td><code>&quot;status&quot;:&quot;active&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been enabled and the Cloudflare DS record is present at the registrar.</td>
</tr>
<tr>
<td>Pending-disabled</td>
<td><code>&quot;status&quot;:&quot;pending-disabled&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been disabled but the Cloudflare DS record is still added at the registrar.</td>
</tr>
<tr>
<td>Disabled</td>
<td><code>&quot;status&quot;:&quot;disabled&quot;</code><br /> <code>&quot;modified_on&quot;:&lt;TIME_STAMP&gt;</code></td>
<td>DNSSEC has been disabled and the Cloudflare DS record has been removed from the registrar.</td>
</tr>
<tr>
<td>Deleted</td>
<td><code>&quot;status&quot;:&quot;disabled&quot;</code><br /> <code>&quot;modified_on&quot;: null</code></td>
<td>DNSSEC has never been enabled for the zone or DNSSEC has been disabled and then deleted using the <a href="/api/resources/dns/subresources/dnssec/methods/delete/">Delete DNSSEC records endpoint</a>.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7693.md")
</aside>
<p>In both <code>pending</code> and <code>active</code> states, Cloudflare signs the zone and responds with RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY record types.</p>
<p>In <code>pending-disabled</code> and <code>disabled</code> states, Cloudflare still signs the zone and serves RRSIG, NSEC, and DNSKEY record types, but the CDS and CDNSKEY records are set to zero (<a href="https://www.rfc-editor.org/rfc/rfc8078.html#section-4">RFC 8078</a>), signaling to the registrar that DNSSEC should be disabled.</p>
<p>In <code>deleted</code> state, Cloudflare does <strong>not</strong> sign the zone and does <strong>not</strong> respond with RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY record types.</p>
<p>Refer to <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">How DNSSEC works</a> to learn more about the authentication process and records involved.</p>
