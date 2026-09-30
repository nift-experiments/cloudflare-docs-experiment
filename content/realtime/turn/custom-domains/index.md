---
cp9:
  canonical: https://developers.cloudflare.com/realtime/turn/custom-domains/
  description: Use custom domains with Cloudflare Realtime TURN via CNAME DNS records.
  full_title: Custom TURN domains · Cloudflare Realtime docs
  head_html: <title>Custom TURN domains · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Use custom domains with Cloudflare Realtime TURN via CNAME DNS records."><link rel="canonical" href="https://developers.cloudflare.com/realtime/turn/custom-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/turn/custom-domains/index.md"><meta property="og:title" content="Custom TURN domains · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use custom domains with Cloudflare Realtime TURN via CNAME DNS records."><meta property="og:url" content="https://developers.cloudflare.com/realtime/turn/custom-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/turn/custom-domains/#page","headline":"Custom TURN domains \u00b7 Cloudflare Realtime docs","description":"Use custom domains with Cloudflare Realtime TURN via CNAME DNS records.","url":"https://developers.cloudflare.com/realtime/turn/custom-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/turn/custom-domains/
  schema: 1
---
<p>Cloudflare Realtime TURN service supports using custom domains for UDP, and TCP - but not TLS protocols. Custom domains do not affect any of the performance of Cloudflare Realtime TURN and is set up via a simple CNAME DNS record on your domain.</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Custom domains</th>
<th>Primary port</th>
<th>Alternate port</th>
</tr>
</thead>
<tbody>
<tr>
<td>STUN over UDP</td>
<td>✅</td>
<td>3478/udp</td>
<td></td>
</tr>
<tr>
<td>TURN over UDP</td>
<td>✅</td>
<td>3478/udp</td>
<td></td>
</tr>
<tr>
<td>TURN over TCP</td>
<td>✅</td>
<td>3478/tcp</td>
<td>80/tcp</td>
</tr>
<tr>
<td>TURN over TLS</td>
<td>No</td>
<td>5349/tcp</td>
<td>443/tcp</td>
</tr>
</tbody>
</table>
<h2 id="setting-up-a-cname-record">Setting up a CNAME record</h2>
<p>To use custom domains for TURN, you must create a CNAME DNS record pointing to <code>turn.cloudflare.com</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11570.md")
</aside>
<p>Any DNS provider, including Cloudflare DNS can be used to set up a CNAME for custom domains.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11569.md")
</aside>
<p>There is no additional charge to using a custom hostname with Cloudflare Realtime TURN.</p>
