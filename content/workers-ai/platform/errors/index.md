---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/platform/errors/
  description: Reference table of Workers AI error codes, HTTP statuses, and descriptions.
  full_title: Errors · Cloudflare Workers AI docs
  head_html: <title>Errors · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference table of Workers AI error codes, HTTP statuses, and descriptions."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/platform/errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/platform/errors/index.md"><meta property="og:title" content="Errors · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference table of Workers AI error codes, HTTP statuses, and descriptions."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/platform/errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/platform/errors/#page","headline":"Errors \u00b7 Cloudflare Workers AI docs","description":"Reference table of Workers AI error codes, HTTP statuses, and descriptions.","url":"https://developers.cloudflare.com/workers-ai/platform/errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/platform/errors/
  schema: 1
---
<p>Below is a list of Workers AI errors.</p>
<table>
<thead>
<tr>
<th><strong>Name</strong></th>
<th><strong>Internal Code</strong></th>
<th><strong>HTTP Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>No such model</td>
<td><code>5007</code></td>
<td><code>400</code></td>
<td>No such model <code>${model}</code> or task</td>
</tr>
<tr>
<td>Invalid data</td>
<td><code>5004</code></td>
<td><code>400</code></td>
<td>Invalid data type for base64 input: <code>${type}</code></td>
</tr>
<tr>
<td>Finetune missing required files</td>
<td><code>3039</code></td>
<td><code>400</code></td>
<td>Finetune is missing required files <code>(model.safetensors and config.json) </code></td>
</tr>
<tr>
<td>Incomplete request</td>
<td><code>3003</code></td>
<td><code>400</code></td>
<td>Request is missing headers or body: <code>{what}</code></td>
</tr>
<tr>
<td>Account not allowed for private model</td>
<td><code>5018</code></td>
<td><code>403</code></td>
<td>The account is not allowed to access this model</td>
</tr>
<tr>
<td>Model agreement</td>
<td><code>5016</code></td>
<td><code>403</code></td>
<td>User has not agreed to Llama3.2 model terms</td>
</tr>
<tr>
<td>Account blocked</td>
<td><code>3023</code></td>
<td><code>403</code></td>
<td>Service unavailable for account</td>
</tr>
<tr>
<td>Account not allowed for private model</td>
<td><code>3041</code></td>
<td><code>403</code></td>
<td>The account is not allowed to access this model</td>
</tr>
<tr>
<td>Model requires Workers Paid plan</td>
<td><code>5035</code></td>
<td><code>403</code></td>
<td>This model requires a Workers Paid plan. See <a href="/workers-ai/platform/pricing/">pricing</a> for details.</td>
</tr>
<tr>
<td>Deprecated SDK version</td>
<td><code>5019</code></td>
<td><code>405</code></td>
<td>Request trying to use deprecated SDK version</td>
</tr>
<tr>
<td>LoRa unsupported</td>
<td><code>5005</code></td>
<td><code>405</code></td>
<td>The model <code>${this.model}</code> does not support LoRa inference</td>
</tr>
<tr>
<td>Invalid model ID</td>
<td><code>3042</code></td>
<td><code>404</code></td>
<td>The model name is invalid</td>
</tr>
<tr>
<td>Request too large</td>
<td><code>3006</code></td>
<td><code>413</code></td>
<td>Request is too large</td>
</tr>
<tr>
<td>Timeout</td>
<td><code>3007</code></td>
<td><code>408</code></td>
<td>Request timeout</td>
</tr>
<tr>
<td>Aborted</td>
<td><code>3008</code></td>
<td><code>408</code></td>
<td>Request was aborted</td>
</tr>
<tr>
<td>Account limited</td>
<td><code>3036</code></td>
<td><code>429</code></td>
<td>You have used up your daily free allocation of 10,000 neurons. Please upgrade to Cloudflare's Workers Paid plan if you would like to continue usage.</td>
</tr>
<tr>
<td>Out of capacity</td>
<td><code>3040</code></td>
<td><code>429</code></td>
<td><code>Capacity temporarily exceeded, please try again.</code> Also returned when <code>rejectIfBusy</code> rejects a request because capacity is unavailable.</td>
</tr>
</tbody>
</table>
