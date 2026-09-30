---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/platform/limits/
  description: Rate limits for Workers AI inference requests, organized by task type and model.
  full_title: Limits · Cloudflare Workers AI docs
  head_html: <title>Limits · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Rate limits for Workers AI inference requests, organized by task type and model."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Rate limits for Workers AI inference requests, organized by task type and model."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Workers AI docs","description":"Rate limits for Workers AI inference requests, organized by task type and model.","url":"https://developers.cloudflare.com/workers-ai/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/platform/limits/
  schema: 1
---
<p>Workers AI is now Generally Available. We've updated our rate limits to reflect this.</p>
<p>Note that model inferences in local mode using Wrangler will also count towards these limits. Beta models may have lower rate limits while we work on performance and scale.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-requirements">Custom requirements</h3>
@markup("md", "content/.markup/bodies/15806.md")
</aside>
<p>Rate limits are default per task type, with some per-model limits defined as follows:</p>
<h2 id="rate-limits-by-task-type">Rate limits by task type</h2>
<h3 id="automatic-speech-recognition-workers-ai-models"><a href="/workers-ai/models/">Automatic Speech Recognition</a></h3>
<ul>
<li>720 requests per minute</li>
</ul>
<h3 id="image-classification-workers-ai-models"><a href="/workers-ai/models/">Image Classification</a></h3>
<ul>
<li>3000 requests per minute</li>
</ul>
<h3 id="image-to-text-workers-ai-models"><a href="/workers-ai/models/">Image-to-Text</a></h3>
<ul>
<li>720 requests per minute</li>
</ul>
<h3 id="object-detection-workers-ai-models"><a href="/workers-ai/models/">Object Detection</a></h3>
<ul>
<li>3000 requests per minute</li>
</ul>
<h3 id="summarization-workers-ai-models"><a href="/workers-ai/models/">Summarization</a></h3>
<ul>
<li>1500 requests per minute</li>
</ul>
<h3 id="text-classification-workers-ai-models"><a href="/workers-ai/models/">Text Classification</a></h3>
<ul>
<li>2000 requests per minute</li>
</ul>
<h3 id="text-embeddings-workers-ai-models"><a href="/workers-ai/models/">Text Embeddings</a></h3>
<ul>
<li>3000 requests per minute</li>
<li><a href="/workers-ai/models/bge-large-en-v1.5/">@cf/baai/bge-large-en-v1.5</a> is 1500 requests per minute</li>
</ul>
<h3 id="text-generation-workers-ai-models"><a href="/workers-ai/models/">Text Generation</a></h3>
<ul>
<li>300 requests per minute, unless the model requires the Workers Paid plan</li>
</ul>
<h4 id="paid-models">Paid models</h4>
<p>The following limits apply per account, per model to any model that requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> — each model page states whether it does. These models are the only models that do not receive the default limit:</p>
<table>
<thead>
<tr>
<th>Billing</th>
<th>Rate limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard Workers AI billing</td>
<td>20 requests per minute</td>
</tr>
<tr>
<td>Prepaid AI Gateway credits</td>
<td>50 requests per minute</td>
</tr>
</tbody>
</table>
<p>To receive the elevated limit, load <a href="/ai-gateway/features/unified-billing/">prepaid AI Gateway credits</a> and set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.</p>
<h3 id="text-to-image-workers-ai-models"><a href="/workers-ai/models/">Text-to-Image</a></h3>
<ul>
<li>720 requests per minute</li>
<li><a href="/workers-ai/models/stable-diffusion-v1-5-img2img/">@cf/runwayml/stable-diffusion-v1-5-img2img</a> is 1500 requests per minute</li>
</ul>
<h3 id="translation-workers-ai-models"><a href="/workers-ai/models/">Translation</a></h3>
<ul>
<li>720 requests per minute</li>
</ul>
