---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/platform/limits/
  description: Account, index, and vector limits for Vectorize on Free and Paid plans.
  full_title: Limits · Cloudflare Vectorize docs
  head_html: <title>Limits · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Account, index, and vector limits for Vectorize on Free and Paid plans."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Account, index, and vector limits for Vectorize on Free and Paid plans."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Vectorize docs","description":"Account, index, and vector limits for Vectorize on Free and Paid plans.","url":"https://developers.cloudflare.com/vectorize/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/platform/limits/
  schema: 1
---
<p>The following limits apply to accounts, indexes, and vectors:</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/15262.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Current Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Indexes per account</td>
<td>50,000 (Workers Paid) / 100 (Free)</td>
</tr>
<tr>
<td>Maximum dimensions per vector</td>
<td>1536 dimensions, 32 bits precision</td>
</tr>
<tr>
<td>Precision per vector dimension</td>
<td>32 bits (float32)</td>
</tr>
<tr>
<td>Maximum vector ID length</td>
<td>64 bytes</td>
</tr>
<tr>
<td>Metadata per vector</td>
<td>10KiB</td>
</tr>
<tr>
<td>Maximum returned results (<code>topK</code>) with values or metadata</td>
<td>50</td>
</tr>
<tr>
<td>Maximum returned results (<code>topK</code>) without values and metadata</td>
<td>100</td>
</tr>
<tr>
<td>Maximum upsert batch size (per batch)</td>
<td>1000 (Workers) / 5000 (HTTP API)</td>
</tr>
<tr>
<td>Maximum vectors in a list-vectors page</td>
<td>1000</td>
</tr>
<tr>
<td>Maximum index name length</td>
<td>64 bytes</td>
</tr>
<tr>
<td>Maximum vectors per index</td>
<td>20,000,000</td>
</tr>
<tr>
<td>Maximum namespaces per index</td>
<td>50,000 (Workers Paid) / 1000 (Free)</td>
</tr>
<tr>
<td>Maximum namespace name length</td>
<td>64 bytes</td>
</tr>
<tr>
<td>Maximum vectors upload size</td>
<td>100 MB</td>
</tr>
<tr>
<td>Maximum metadata indexes per Vectorize index</td>
<td>10</td>
</tr>
<tr>
<td>Maximum indexed data per metadata index per vector</td>
<td>64 bytes</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>Limits for V1 indexes (deprecated)</summary><div class="nb-details-body">
@input("content/.markup/bodies/15263.md")
</div></details>
