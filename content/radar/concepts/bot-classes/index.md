---
cp9:
  canonical: https://developers.cloudflare.com/radar/concepts/bot-classes/
  description: Cloudflare Radar classifies traffic as likely automated or likely human based on bot score ranges.
  full_title: Bot classes · Cloudflare Radar docs
  head_html: <title>Bot classes · Cloudflare Radar docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Radar classifies traffic as likely automated or likely human based on bot score ranges."><link rel="canonical" href="https://developers.cloudflare.com/radar/concepts/bot-classes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/radar/concepts/bot-classes/index.md"><meta property="og:title" content="Bot classes · Cloudflare Radar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Radar classifies traffic as likely automated or likely human based on bot score ranges."><meta property="og:url" content="https://developers.cloudflare.com/radar/concepts/bot-classes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Radar"><meta name="algolia_product_filter" content="Radar"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Radar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/radar/concepts/bot-classes/#page","headline":"Bot classes \u00b7 Cloudflare Radar docs","description":"Cloudflare Radar classifies traffic as likely automated or likely human based on bot score ranges.","url":"https://developers.cloudflare.com/radar/concepts/bot-classes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /radar/concepts/bot-classes/
  schema: 1
---
<p>A bot class in Radar is a grouping of <a href="/bots/concepts/bot-score">bot scores</a>.</p>
<p>Scores between 1 and 29 are classified as bot traffic. Scores equal or above 30 are classified as non-bot/human traffic.</p>
<table>
<thead>
<tr>
<th>Class</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Likely automated</strong></td>
<td>Bot scores of 1 through 29.</td>
</tr>
<tr>
<td><strong>Likely human</strong></td>
<td>Bot scores of 30 through 99.</td>
</tr>
</tbody>
</table>
