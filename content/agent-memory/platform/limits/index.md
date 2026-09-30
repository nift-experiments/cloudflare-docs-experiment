---
cp9:
  canonical: https://developers.cloudflare.com/agent-memory/platform/limits/
  description: Review Agent Memory platform limits, including message sizes, naming constraints, and API pagination limits.
  full_title: Limits · Cloudflare Agent Memory docs
  head_html: <title>Limits · Cloudflare Agent Memory docs</title><meta name="generator" content="Nift"><meta name="description" content="Review Agent Memory platform limits, including message sizes, naming constraints, and API pagination limits."><link rel="canonical" href="https://developers.cloudflare.com/agent-memory/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agent-memory/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Agent Memory docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review Agent Memory platform limits, including message sizes, naming constraints, and API pagination limits."><meta property="og:url" content="https://developers.cloudflare.com/agent-memory/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agent Memory"><meta name="algolia_product_filter" content="Agent Memory"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agent Memory"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agent-memory/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Agent Memory docs","description":"Review Agent Memory platform limits, including message sizes, naming constraints, and API pagination limits.","url":"https://developers.cloudflare.com/agent-memory/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agent-memory/platform/limits/
  schema: 1
---
<p>The following limits apply to Agent Memory operations.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Messages per <code>ingest()</code> call</td>
<td>500</td>
</tr>
<tr>
<td>Message content size</td>
<td>32 KB (32,768 bytes UTF-8)</td>
</tr>
<tr>
<td>Recall query size</td>
<td>1 KB (1,024 bytes UTF-8)</td>
</tr>
<tr>
<td>Session ID length</td>
<td>64 characters</td>
</tr>
<tr>
<td>Profile name length</td>
<td>100 characters</td>
</tr>
<tr>
<td>Namespace name length</td>
<td>32 characters</td>
</tr>
<tr>
<td>List API page size</td>
<td>1 to 1,000 (default: 20)</td>
</tr>
</tbody>
</table>
