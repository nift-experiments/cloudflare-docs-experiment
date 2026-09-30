---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/
  description: '@cf/moondream/moondream3.1-9B-A2B'
  full_title: '@cf/moondream/moondream3.1-9B-A2B · Cloudflare Workers AI docs'
  head_html: <title>@cf/moondream/moondream3.1-9B-A2B · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/moondream/moondream3.1-9B-A2B"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/moondream/moondream3.1-9B-A2B · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/moondream/moondream3.1-9B-A2B"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/#page","headline":"@cf/moondream/moondream3.1-9B-A2B \u00b7 Cloudflare Workers AI docs","description":"@cf/moondream/moondream3.1-9B-A2B","url":"https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/moondream3.1-9B-A2B/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="moondream3-1-9b-a2b">moondream3.1-9B-A2B</h1>

<p><code>@cf/moondream/moondream3.1-9B-A2B</code></p>

Moondream 3 is a fast, efficient 9B mixture-of-experts vision language model (2B active parameters) that delivers frontier-level visual reasoning for tasks like object detection, pointing, OCR, and structured output.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Text</td></tr>
<tr><th>Terms</th><td><a href="https://moondream.ai/licenses/model/1.0">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.3 per M input tokens, USD 1 per M output tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/moondream/moondream3.1-9B-A2B&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/moondream/moondream3.1-9B-A2B&quot;, { image_to_text: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/moondream/moondream3.1-9B-A2B -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>task</code></td><td>string</td><td>Which Moondream skill to run. Default: query; Values: query, caption, point, detect</td></tr><tr><td><code>image</code></td><td>string</td><td>Input image as a public HTTPS URL or base64 data URI. Optional for `query`; required for `caption`, `point`, and `detect`.</td></tr><tr><td><code>question</code></td><td>string</td><td>Question for the `query` task. Default: What's in this image?</td></tr><tr><td><code>caption_length</code></td><td>string</td><td>Caption length for the `caption` task. Default: normal; Values: short, normal, long</td></tr><tr><td><code>target</code></td><td>string</td><td>Object phrase to locate for `point` and `detect` tasks (e.g. 'person wearing a red shirt'). Default: person</td></tr><tr><td><code>reasoning</code></td><td>boolean</td><td>Enable reasoning trace for the `query` task. Default: True</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Sampling temperature. Default: 0.2; Minimum: 0; Maximum: 2</td></tr><tr><td><code>top_p</code></td><td>number</td><td>Top-p (nucleus) sampling. Default: 0.9; Minimum: 0; Maximum: 1</td></tr><tr><td><code>max_tokens</code></td><td>integer</td><td>Max tokens to generate for `query` and `caption`. Default: 8192; Minimum: 1; Maximum: 28672</td></tr><tr><td><code>max_objects</code></td><td>integer</td><td>Max objects to return for `point` and `detect`. Default: 150; Minimum: 1; Maximum: 500</td></tr><tr><td><code>stream</code></td><td>boolean</td><td>Return incremental tokens for `query` and `caption`. `point` and `detect` do not support streaming. Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>finish_reason</code></td><td>string</td><td>Required. Reason the generation finished.</td></tr><tr><td><code>metrics</code></td><td>object</td><td>Required.</td></tr><tr><td><code>metrics.input_tokens</code></td><td>integer</td><td>Required. Number of input tokens consumed.</td></tr><tr><td><code>metrics.output_tokens</code></td><td>integer</td><td>Required. Number of output tokens generated.</td></tr><tr><td><code>metrics.prefill_time_ms</code></td><td>number</td><td>Required. Prefill time in milliseconds.</td></tr><tr><td><code>metrics.decode_time_ms</code></td><td>number</td><td>Required. Decode time in milliseconds.</td></tr><tr><td><code>metrics.ttft_ms</code></td><td>number</td><td>Required. Time to first token in milliseconds.</td></tr><tr><td><code>answer</code></td><td>string</td><td>Answer text for the `query` task. Null for other tasks.</td></tr><tr><td><code>caption</code></td><td>string</td><td>Caption text for the `caption` task. Null for other tasks.</td></tr><tr><td><code>points</code></td><td>array</td><td>Located points for the `point` task. Null for other tasks.</td></tr><tr><td><code>points[].x</code></td><td>number</td><td>Required. X coordinate.</td></tr><tr><td><code>points[].y</code></td><td>number</td><td>Required. Y coordinate.</td></tr><tr><td><code>objects</code></td><td>array</td><td>Detected bounding boxes for the `detect` task. Null for other tasks.</td></tr><tr><td><code>objects[].x_min</code></td><td>number</td><td>Required. Minimum X coordinate.</td></tr><tr><td><code>objects[].y_min</code></td><td>number</td><td>Required. Minimum Y coordinate.</td></tr><tr><td><code>objects[].x_max</code></td><td>number</td><td>Required. Maximum X coordinate.</td></tr><tr><td><code>objects[].y_max</code></td><td>number</td><td>Required. Maximum Y coordinate.</td></tr><tr><td><code>reasoning</code></td><td>object</td><td>Reasoning trace for the `query` task when reasoning=true. Null otherwise.</td></tr><tr><td><code>reasoning.text</code></td><td>string</td><td>Required. Reasoning text.</td></tr><tr><td><code>reasoning.grounding</code></td><td>array</td><td>Grounding information.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/moondream3.1-9B-A2B/schema-input.json)
- [Output schema](/workers-ai/models/moondream3.1-9B-A2B/schema-output.json)

