---
cp9:
  canonical: https://developers.cloudflare.com/kv/platform/pricing/
  description: Workers KV pricing for read, write, delete, and list operations, plus storage costs and billing FAQ.
  full_title: Pricing · Cloudflare Workers KV docs
  head_html: <title>Pricing · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers KV pricing for read, write, delete, and list operations, plus storage costs and billing FAQ."><link rel="canonical" href="https://developers.cloudflare.com/kv/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers KV pricing for read, write, delete, and list operations, plus storage costs and billing FAQ."><meta property="og:url" content="https://developers.cloudflare.com/kv/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Workers KV docs","description":"Workers KV pricing for read, write, delete, and list operations, plus storage costs and billing FAQ.","url":"https://developers.cloudflare.com/kv/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/platform/pricing/
  schema: 1
---
<p>Workers KV is included in both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free plan<sup>1</sup></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Keys read</td>
<td>100,000 / day</td>
<td>10 million/month, + $0.50/million</td>
</tr>
<tr>
<td>Keys written</td>
<td>1,000 / day</td>
<td>1 million/month, + $5.00/million</td>
</tr>
<tr>
<td>Keys deleted</td>
<td>1,000 / day</td>
<td>1 million/month, + $5.00/million</td>
</tr>
<tr>
<td>List requests</td>
<td>1,000 / day</td>
<td>1 million/month, + $5.00/million</td>
</tr>
<tr>
<td>Stored data</td>
<td>1 GB</td>
<td>1 GB, + $0.50/ GB-month</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> The Workers Free plan includes limited Workers KV usage. All limits
reset daily at 00:00 UTC. If you exceed any one of these limits, further
operations of that type will fail with an error.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9497.md")
</aside>
<h2 id="pricing-faq">Pricing FAQ</h2>
<h4 id="when-writing-via-kv-s-rest-api-api-resources-kv-subresources-namespaces-subresources-keys-methods-bulk-update-how-are-writes-charged">When writing via KV's <a href="/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update/">REST API</a>, how are writes charged?</h4>
<p>Each key-value pair in the <code>PUT</code> request is counted as a single write, identical to how each call to <code>PUT</code> in the Workers API counts as a write. Writing 5,000 keys via the REST API incurs the same write costs as making 5,000 <code>PUT</code> calls in a Worker.</p>
<h4 id="do-queries-i-issue-from-the-dashboard-or-wrangler-the-cli-count-as-billable-usage">Do queries I issue from the dashboard or wrangler (the CLI) count as billable usage?</h4>
<p>Yes, any operations via the Cloudflare dashboard or wrangler, including updating (writing) keys, deleting keys, and listing the keys in a namespace count as billable KV usage.</p>
<h4 id="does-workers-kv-charge-for-data-transfer-egress">Does Workers KV charge for data transfer / egress?</h4>
<p>No.</p>
<h4 id="what-operations-incur-operations-charges">What operations incur operations charges?</h4>
<p>All operations incur charges, including fetches for non-existent keys that return a <code>null</code> (Workers API) or <code>HTTP 404</code> (REST API). These operations still traverse KV's infrastructure.</p>
