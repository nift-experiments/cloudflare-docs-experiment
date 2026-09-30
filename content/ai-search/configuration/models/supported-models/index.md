---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/models/supported-models/
  description: View all AI models supported by AI Search, including text generation, embedding, and reranking models.
  full_title: Supported models · Cloudflare AI Search docs
  head_html: <title>Supported models · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="View all AI models supported by AI Search, including text generation, embedding, and reranking models."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/models/supported-models/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/models/supported-models/index.md"><meta property="og:title" content="Supported models · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View all AI models supported by AI Search, including text generation, embedding, and reranking models."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/models/supported-models/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/models/supported-models/#page","headline":"Supported models \u00b7 Cloudflare AI Search docs","description":"View all AI models supported by AI Search, including text generation, embedding, and reranking models.","url":"https://developers.cloudflare.com/ai-search/configuration/models/supported-models/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/models/supported-models/
  schema: 1
---
<p>This page lists all models supported by AI Search and their lifecycle status.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="request-model-support">Request model support</h3>
@markup("md", "content/.markup/bodies/3079.md")
</aside>
<h2 id="production-models">Production models</h2>
<p>Production models are the actively supported and recommended models that are stable and fully available.</p>
<h3 id="text-generation">Text generation</h3>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Alias</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Anthropic</strong></td>
<td><code>anthropic/claude-3-7-sonnet</code></td>
<td>200,000</td>
</tr>
<tr>
<td></td>
<td><code>anthropic/claude-sonnet-4</code></td>
<td>200,000</td>
</tr>
<tr>
<td></td>
<td><code>anthropic/claude-opus-4</code></td>
<td>200,000</td>
</tr>
<tr>
<td></td>
<td><code>anthropic/claude-3-5-haiku</code></td>
<td>200,000</td>
</tr>
<tr>
<td><strong>Cerebras</strong></td>
<td><code>cerebras/gpt-oss-120b</code></td>
<td>131,072</td>
</tr>
<tr>
<td></td>
<td><code>cerebras/gemma-4-31b</code></td>
<td>131,072</td>
</tr>
<tr>
<td><strong>Google AI Studio</strong></td>
<td><code>google-ai-studio/gemini-2.5-flash</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td></td>
<td><code>google-ai-studio/gemini-2.5-pro</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><strong>Grok (x.ai)</strong></td>
<td><code>grok/grok-4</code></td>
<td>256,000</td>
</tr>
<tr>
<td><strong>Groq</strong></td>
<td><code>groq/llama-3.3-70b-versatile</code></td>
<td>131,072</td>
</tr>
<tr>
<td></td>
<td><code>groq/llama-3.1-8b-instant</code></td>
<td>131,072</td>
</tr>
<tr>
<td><strong>OpenAI</strong></td>
<td><code>openai/gpt-5</code></td>
<td>400,000</td>
</tr>
<tr>
<td></td>
<td><code>openai/gpt-5-mini</code></td>
<td>400,000</td>
</tr>
<tr>
<td></td>
<td><code>openai/gpt-5-nano</code></td>
<td>400,000</td>
</tr>
<tr>
<td><strong>Workers AI</strong></td>
<td><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></td>
<td>24,000</td>
</tr>
<tr>
<td></td>
<td><code>@cf/meta/llama-3.1-8b-instruct-fast</code></td>
<td>60,000</td>
</tr>
<tr>
<td></td>
<td><code>@cf/meta/llama-3.1-8b-instruct-fp8</code></td>
<td>32,000</td>
</tr>
<tr>
<td></td>
<td><code>@cf/meta/llama-4-scout-17b-16e-instruct</code></td>
<td>131,000</td>
</tr>
<tr>
<td></td>
<td><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td></td>
<td><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td></td>
<td><code>@cf/openai/gpt-oss-120b</code></td>
<td>128,000</td>
</tr>
<tr>
<td></td>
<td><code>@cf/openai/gpt-oss-20b</code></td>
<td>128,000</td>
</tr>
<tr>
<td></td>
<td><code>@cf/qwen/qwen3.8-27b</code></td>
<td>262,144</td>
</tr>
<tr>
<td></td>
<td><code>@cf/moonshotai/kimi-k2.7-code</code></td>
<td>262,144</td>
</tr>
<tr>
<td></td>
<td><code>@cf/zai-org/glm-4.7-flash</code></td>
<td>131,072</td>
</tr>
<tr>
<td></td>
<td><code>@cf/zai-org/glm-5.3-flash</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td></td>
<td><code>@cf/qwen/qwen3-30b-a3b-fp8</code></td>
<td>32,000</td>
</tr>
</tbody>
</table>
<h3 id="embedding">Embedding</h3>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Alias</th>
<th>Vector dims</th>
<th>Input tokens</th>
<th>Metric</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Google AI Studio</strong></td>
<td><code>google-ai-studio/gemini-embedding-001</code></td>
<td>1,536</td>
<td>2048</td>
<td>cosine</td>
</tr>
<tr>
<td><strong>OpenAI</strong></td>
<td><code>openai/text-embedding-3-small</code></td>
<td>1,536</td>
<td>8192</td>
<td>cosine</td>
</tr>
<tr>
<td></td>
<td><code>openai/text-embedding-3-large</code></td>
<td>1,536</td>
<td>8192</td>
<td>cosine</td>
</tr>
<tr>
<td><strong>Workers AI</strong></td>
<td><code>@cf/baai/bge-m3</code></td>
<td>1,024</td>
<td>512</td>
<td>cosine</td>
</tr>
<tr>
<td></td>
<td><code>@cf/baai/bge-large-en-v1.5</code></td>
<td>1,024</td>
<td>512</td>
<td>cosine</td>
</tr>
<tr>
<td></td>
<td><code>@cf/qwen/qwen3-embedding-0.6b</code></td>
<td>1,024</td>
<td>8,192</td>
<td>cosine</td>
</tr>
<tr>
<td></td>
<td><code>@cf/google/embeddinggemma-300m</code></td>
<td>768</td>
<td>512</td>
<td>cosine</td>
</tr>
</tbody>
</table>
<h3 id="reranking">Reranking</h3>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Alias</th>
<th>Input tokens</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers AI</strong></td>
<td><code>@cf/baai/bge-reranker-base</code></td>
<td>512</td>
</tr>
</tbody>
</table>
<h2 id="transition-models">Transition models</h2>
<p>There are currently no models marked for end-of-life.</p>
