---
cp9:
  canonical: https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/
  description: Understand why Bot Management does not score certain requests.
  full_title: Bot Management skips · Cloudflare bot solutions docs
  head_html: <title>Bot Management skips · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand why Bot Management does not score certain requests."><link rel="canonical" href="https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/index.md"><meta property="og:title" content="Bot Management skips · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand why Bot Management does not score certain requests."><meta property="og:url" content="https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/#page","headline":"Bot Management skips \u00b7 Cloudflare bot solutions docs","description":"Understand why Bot Management does not score certain requests.","url":"https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/troubleshooting/bot-management-skips/
  schema: 1
---
<p>There are instances in which Bot Management does not run and certain fields, such as the <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3/JA4 field</a>, are not populated because it has been determined that running Bot Management would not be necessary.</p>
<p>Refer to <span class="nb-glossary-tooltip" title="bot score">bot scores</span> for more information about why a request is not scored.</p>
<h2 id="common-reasons-for-bot-management-to-not-score-a-request">Common reasons for Bot Management to not score a request</h2>
<h3 id="requests-to-internal-endpoints">Requests to internal endpoints</h3>
<p>Requests such as <code>/cdn-cgi/</code> are handled individually and will never receive a Bot Management score. Email Obfuscation, Web Analytics, Trace Requests, Challenge Pages, and JavaScript Detections do not receive bot scores. Refer to the table below for some examples of internal endpoints.</p>
<table>
<thead>
<tr>
<th>Route</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/cdn-cgi/rum</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/script_monitor/report</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/trace</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/challenge-platform/…</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js</code></td>
</tr>
</tbody>
</table>
<h3 id="purge-requests">Purge requests</h3>
<p>All HTTP purge requests will not receive a bot score.</p>
<h3 id="early-hints-cache-requests">Early hints cache requests</h3>
<p>Early hints cache requests will not receive a bot score.</p>
