---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/platform/limits/
  description: Review Artifacts platform limits.
  full_title: Limits · Cloudflare Artifacts docs
  head_html: <title>Limits · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Review Artifacts platform limits."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review Artifacts platform limits."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Artifacts docs","description":"Review Artifacts platform limits.","url":"https://developers.cloudflare.com/artifacts/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/platform/limits/
  schema: 1
---
<p>Limits that apply to creating, importing, cloning, and pushing Artifacts are detailed below.</p>
<p>These limits cover naming rules, storage, and request rates for control-plane and Git operations.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Control-plane request rate</td>
<td>2,000 requests per 10 seconds per Artifacts namespace</td>
</tr>
<tr>
<td>Git request rate, per artifact</td>
<td>2,000 requests per 10 seconds per artifact</td>
</tr>
<tr>
<td>Maximum storage per repository</td>
<td>10 GB</td>
</tr>
<tr>
<td>Maximum storage per account</td>
<td>1 TB (can be raised on request)</td>
</tr>
<tr>
<td>Maximum number of repositories</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Maximum number of namespaces</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Namespace and repo names</td>
<td>Start with a letter or digit. Remaining characters may include letters, digits, <code>.</code>, <code>_</code>, and <code>-</code>.</td>
</tr>
</tbody>
</table>
