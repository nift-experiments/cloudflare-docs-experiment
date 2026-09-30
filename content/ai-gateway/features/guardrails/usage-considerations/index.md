---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/
  description: Understand latency, availability, language support, and Workers AI usage when enabling AI Gateway Guardrails.
  full_title: Usage considerations · Cloudflare AI Gateway docs
  head_html: <title>Usage considerations · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand latency, availability, language support, and Workers AI usage when enabling AI Gateway Guardrails."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/index.md"><meta property="og:title" content="Usage considerations · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand latency, availability, language support, and Workers AI usage when enabling AI Gateway Guardrails."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/#page","headline":"Usage considerations \u00b7 Cloudflare AI Gateway docs","description":"Understand latency, availability, language support, and Workers AI usage when enabling AI Gateway Guardrails.","url":"https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/features/guardrails/usage-considerations/
  schema: 1
---
<p>Guardrails currently uses <a href="https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/">Llama Guard 3 8B</a> on <a href="/workers-ai/">Workers AI</a> to perform content evaluations. The underlying model may be updated in the future, and we will reflect those changes within Guardrails.</p>
<p>Since Guardrails runs on Workers AI, enabling it incurs usage on Workers AI. You can monitor usage through the Workers AI Dashboard.</p>
<h2 id="hazard-categories">Hazard categories</h2>
<p>Guardrails evaluate content against the following hazard categories. Each category is identified by a code that appears in your Guardrail configuration and in AI Gateway Logs. You can independently set each category to <strong>Flag</strong>, <strong>Ignore</strong>, or <strong>Block</strong> for prompts and responses.</p>
<p>Guardrails evaluate categories <code>S1</code> through <code>S13</code>, a subset of the <a href="https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/">Llama Guard 3 ↗</a> hazard categories, using the <a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a> model on Workers AI. The Llama Guard 3 category <code>S14</code> (Code interpreter abuse) is not evaluated by Guardrails. Category <code>P1</code> is prompt injection, evaluated separately by the <code>@cf/meta/prompt-guard-2-86m</code> model.</p>
<p>These codes also appear in the <code>guardrails</code> property of the AI Gateway REST API, where you configure each category's action programmatically. See the <a href="/api/resources/ai_gateway/methods/create/"><code>create</code></a> and <a href="/api/resources/ai_gateway/methods/update/"><code>update</code></a> methods.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Category</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>S1</code></td>
<td>Violent Crimes</td>
</tr>
<tr>
<td><code>S2</code></td>
<td>Non-Violent Crimes</td>
</tr>
<tr>
<td><code>S3</code></td>
<td>Sex-Related Crimes</td>
</tr>
<tr>
<td><code>S4</code></td>
<td>Child Sexual Exploitation</td>
</tr>
<tr>
<td><code>S5</code></td>
<td>Defamation</td>
</tr>
<tr>
<td><code>S6</code></td>
<td>Specialized Advice</td>
</tr>
<tr>
<td><code>S7</code></td>
<td>Privacy</td>
</tr>
<tr>
<td><code>S8</code></td>
<td>Intellectual Property</td>
</tr>
<tr>
<td><code>S9</code></td>
<td>Indiscriminate Weapons</td>
</tr>
<tr>
<td><code>S10</code></td>
<td>Hate</td>
</tr>
<tr>
<td><code>S11</code></td>
<td>Suicide &amp; Self-Harm</td>
</tr>
<tr>
<td><code>S12</code></td>
<td>Sexual Content</td>
</tr>
<tr>
<td><code>S13</code></td>
<td>Elections</td>
</tr>
<tr>
<td><code>P1</code></td>
<td>Prompt Injection</td>
</tr>
</tbody>
</table>
<h2 id="additional-considerations">Additional considerations</h2>
<ul>
<li><strong>Model availability</strong>: If at least one hazard category is set to <code>block</code>, but AI Gateway is unable to receive a response from Workers AI, the request will be blocked. Conversely, if a hazard category is set to <code>flag</code> and AI Gateway cannot obtain a response from Workers AI, the request will proceed without evaluation. This approach prioritizes availability, allowing requests to continue even when content evaluation is not possible.</li>
<li><strong>Latency impact</strong>: Enabling Guardrails introduces additional latency to requests. Typically, evaluations using Llama Guard 3 8B on Workers AI add approximately 500 milliseconds per request. However, larger requests may experience increased latency, though this increase is not linear. Consider this when balancing safety and performance.</li>
<li><strong>Handling long content</strong>: When evaluating long prompts or responses, Guardrails automatically segments the content into smaller chunks, processing each through separate Guardrail requests. This approach ensures comprehensive moderation but may result in increased latency for longer inputs.</li>
<li><strong>Supported languages</strong>: Llama Guard 3.3 8B supports content safety classification in the following languages: English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai.</li>
</ul>
<h3 id="streaming-behavior">Streaming behavior</h3>
<p>Guardrails does not support streaming (<code>stream: true</code>) requests. Prompts are still evaluated and enforced, but response behavior depends on the API surface.</p>
<p>On the REST API (<code>api.cloudflare.com/*</code>), Guardrails evaluates the response and logs the result, but does not enforce it — the client receives the full streaming response regardless of what Guardrails would have flagged. On the gateway endpoints (<code>gateway.ai.cloudflare.com/v1/*</code>), Guardrails buffers the full response, evaluates it, and returns a single non-streamed payload — the request no longer streams.</p>
<p>For non-streaming (<code>stream: false</code>) requests, both prompts and responses are evaluated and enforced.</p>
<p>Guardrails evaluates response payload text, including URL strings in image generation model responses. It does not retrieve or evaluate referenced images. Embedding and unknown model types bypass response evaluation regardless of streaming mode.</p>
<p>For more information, refer to <a href="/ai-gateway/features/guardrails/supported-model-types/">Supported model types</a>.</p>
<p>Full Guardrails support for streaming requests is on our roadmap.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2891.md")
</aside>
