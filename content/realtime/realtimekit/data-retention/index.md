---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/data-retention/
  description: Review how long RealtimeKit stores meeting chat, recordings, analytics, and webhook logs.
  full_title: Data retention · Cloudflare Realtime docs
  head_html: <title>Data retention · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Review how long RealtimeKit stores meeting chat, recordings, analytics, and webhook logs."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/data-retention/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/data-retention/index.md"><meta property="og:title" content="Data retention · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review how long RealtimeKit stores meeting chat, recordings, analytics, and webhook logs."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/data-retention/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/data-retention/#page","headline":"Data retention \u00b7 Cloudflare Realtime docs","description":"Review how long RealtimeKit stores meeting chat, recordings, analytics, and webhook logs.","url":"https://developers.cloudflare.com/realtime/realtimekit/data-retention/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/data-retention/
  schema: 1
---
<p>RealtimeKit retains data for the following periods:</p>
<table>
<thead>
<tr>
<th>Data type</th>
<th>Retention period</th>
</tr>
</thead>
<tbody>
<tr>
<td>Meeting and participant records</td>
<td>Indefinitely</td>
</tr>
<tr>
<td>Meeting chat with <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/#(resource)%20realtime_kit.meetings%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20persist_chat%20%3E%20(schema)"><code>persist_chat</code></a></td>
<td>Indefinitely</td>
</tr>
<tr>
<td>Meeting chat without <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/#(resource)%20realtime_kit.meetings%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20persist_chat%20%3E%20(schema)"><code>persist_chat</code></a></td>
<td>7 days</td>
</tr>
<tr>
<td>Composite recordings</td>
<td>7 days</td>
</tr>
<tr>
<td>Track recordings</td>
<td>7 days</td>
</tr>
<tr>
<td>Transcripts</td>
<td>7 days</td>
</tr>
<tr>
<td>Call analytics</td>
<td>6 months</td>
</tr>
<tr>
<td>Webhook logs</td>
<td>1 month</td>
</tr>
</tbody>
</table>
