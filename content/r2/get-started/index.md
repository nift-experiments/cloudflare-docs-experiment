---
cp9:
  canonical: https://developers.cloudflare.com/r2/get-started/
  description: Create your first R2 bucket and store objects using the dashboard, S3-compatible tools, or Workers.
  full_title: Get started · Cloudflare R2 docs
  head_html: <title>Get started · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Create your first R2 bucket and store objects using the dashboard, S3-compatible tools, or Workers."><link rel="canonical" href="https://developers.cloudflare.com/r2/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create your first R2 bucket and store objects using the dashboard, S3-compatible tools, or Workers."><meta property="og:url" content="https://developers.cloudflare.com/r2/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="R2,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/get-started/#page","headline":"Get started \u00b7 Cloudflare R2 docs","description":"Create your first R2 bucket and store objects using the dashboard, S3-compatible tools, or Workers.","url":"https://developers.cloudflare.com/r2/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/get-started/
  schema: 1
---
<p>Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>You need a Cloudflare account with an R2 subscription. If you do not have one:</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a>.</li>
<li>Select <strong>Storage &amp; databases &gt; R2 &gt; Overview</strong></li>
<li>Complete the checkout flow to add an R2 subscription to your account.</li>
</ol>
<p>R2 is free to get started with included free monthly usage. You are billed for your usage on a monthly basis. Refer to <a href="/r2/pricing/">Pricing</a> for details.</p>
<div class="nb-dash-button"></div>
<h2 id="choose-how-to-access-r2">Choose how to access R2</h2>
<p>R2 supports multiple access methods, so you can choose the one that fits your use case best:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/r2/get-started/workers-api/">Workers API</a></td>
<td>You are building an application on Cloudflare Workers that needs to read or write from R2</td>
</tr>
<tr>
<td><a href="/r2/get-started/s3/">S3</a></td>
<td>You want to use S3-compatible SDKs to interact with R2 in your existing applications</td>
</tr>
<tr>
<td><a href="/r2/get-started/cli/">CLI tools</a></td>
<td>You want to upload, download, or manage objects from your terminal</td>
</tr>
<tr>
<td><a href="https://dash.cloudflare.com/?to=/:account/r2/overview">Dashboard</a></td>
<td>You want to quickly view and manage buckets and objects in the browser</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-workers-api-r2-get-started-workers-api"><a href="/r2/get-started/workers-api/">Workers API</a></h3><p>Use R2 from Cloudflare Workers.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-s3-r2-get-started-s3"><a href="/r2/get-started/s3/">S3</a></h3><p>Use R2 with S3-compatible SDKs.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cli-r2-get-started-cli"><a href="/r2/get-started/cli/">CLI</a></h3><p>Use R2 from the command line.</p></div>
