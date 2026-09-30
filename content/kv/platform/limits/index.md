---
cp9:
  canonical: https://developers.cloudflare.com/kv/platform/limits/
  description: Workers KV account and namespace limits for reads, writes, key size, value size, and storage.
  full_title: Limits · Cloudflare Workers KV docs
  head_html: <title>Limits · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers KV account and namespace limits for reads, writes, key size, value size, and storage."><link rel="canonical" href="https://developers.cloudflare.com/kv/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers KV account and namespace limits for reads, writes, key size, value size, and storage."><meta property="og:url" content="https://developers.cloudflare.com/kv/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Workers KV docs","description":"Workers KV account and namespace limits for reads, writes, key size, value size, and storage.","url":"https://developers.cloudflare.com/kv/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/platform/limits/
  schema: 1
---
<table>
<thead>
<tr>
<th>Feature</th>
<th>Free</th>
<th>Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reads</td>
<td>100,000 reads per day</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Writes to different keys</td>
<td>1,000 writes per day</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Writes to same key</td>
<td>1 per second</td>
<td>1 per second</td>
</tr>
<tr>
<td>Operations/Worker invocation <sup><a href="#footnote-1">1</a></sup></td>
<td>1000</td>
<td>1000</td>
</tr>
<tr>
<td>Namespaces per account</td>
<td>1,000</td>
<td>1,000</td>
</tr>
<tr>
<td>Storage/account</td>
<td>1 GB</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Storage/namespace</td>
<td>1 GB</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Keys/namespace</td>
<td>Unlimited</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Key size</td>
<td>512 bytes</td>
<td>512 bytes</td>
</tr>
<tr>
<td>Key metadata</td>
<td>1024 bytes</td>
<td>1024 bytes</td>
</tr>
<tr>
<td>Value size</td>
<td>25 MiB</td>
<td>25 MiB</td>
</tr>
<tr>
<td>Minimum <a href="/kv/api/read-key-value-pairs/#cachettl-parameter"><code>cacheTtl</code></a> <sup><a href="#footnote-2">2</a></sup></td>
<td>30 seconds</td>
<td>30 seconds</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/9500.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="free-versus-paid-plan-pricing">Free versus Paid plan pricing</h3>
@markup("md", "content/.markup/bodies/9499.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-kv-rest-api-limits">Workers KV REST API limits</h3>
@markup("md", "content/.markup/bodies/9498.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Within a single invocation, a Worker can make up to 1,000 operations to external services (for example, 500 Workers KV reads and 500 R2 reads). A bulk request to Workers KV counts for 1 request to an external service.</li>
<li id="footnote-2">The maximum value is [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER).</li></ol></section>
