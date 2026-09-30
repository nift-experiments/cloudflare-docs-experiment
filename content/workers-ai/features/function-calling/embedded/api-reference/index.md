---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/
  description: Reference for the runWithTools and autoTrimTools methods in embedded function calling.
  full_title: API Reference - Embedded function calling · Cloudflare Workers AI docs
  head_html: <title>API Reference - Embedded function calling · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for the runWithTools and autoTrimTools methods in embedded function calling."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/index.md"><meta property="og:title" content="API Reference - Embedded function calling · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for the runWithTools and autoTrimTools methods in embedded function calling."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/#page","headline":"API Reference - Embedded function calling \u00b7 Cloudflare Workers AI docs","description":"Reference for the runWithTools and autoTrimTools methods in embedded function calling.","url":"https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/function-calling/embedded/api-reference/
  schema: 1
---
<p>Learn more about the API reference for <a href="/workers-ai/features/function-calling/embedded">embedded function calling</a>.</p>
<h2 id="runwithtools">runWithTools</h2>
<p>This wrapper method enables you to do embedded function calling. You pass it the AI binding, model, inputs (<code>messages</code> array and <code>tools</code> array), and optional configurations.</p>
<ul>
<li><code>AI Binding</code>Ai
<ul>
<li>The AI binding, such as <code>env.AI</code>.</li>
</ul>
</li>
<li><code>model</code>BaseAiTextGenerationModels
<ul>
<li>The ID of the model that supports function calling. For example, <code>@hf/nousresearch/hermes-2-pro-mistral-7b</code>.</li>
</ul>
</li>
<li><code>input</code>Object
<ul>
<li><code>messages</code>RoleScopedChatInput[]</li>
<li><code>tools</code>AiTextGenerationToolInputWithFunction[]</li>
</ul>
</li>
<li><code>config</code>Object
<ul>
<li><code>streamFinalResponse</code>boolean optional</li>
<li><code>maxRecursiveToolRuns</code>number optional</li>
<li><code>strictValidation</code>boolean optional</li>
<li><code>verbose</code>boolean optional</li>
<li><code>trimFunction</code>boolean optional - For the <code>trimFunction</code>, you can pass it <code>autoTrimTools</code>, which is another helper method we've devised to automatically choose the correct tools (using an LLM) before sending it off for inference. This means that your final inference call will have fewer input tokens.</li>
</ul>
</li>
</ul>
<h2 id="createtoolsfromopenapispec">createToolsFromOpenAPISpec</h2>
<p>This method lets you automatically create tool schemas based on OpenAPI specs, so you don't have to manually write or hardcode the tool schemas. You can pass the OpenAPI spec for any API in JSON or YAML format.</p>
<p><code>createToolsFromOpenAPISpec</code> has a config input that allows you to perform overrides if you need to provide headers like Authentication or User-Agent.</p>
<ul>
<li><code>spec</code>string
<ul>
<li>The OpenAPI specification in either JSON or YAML format, or a URL to a remote OpenAPI specification.</li>
</ul>
</li>
<li><code>config</code>Config optional - Configuration options for the createToolsFromOpenAPISpec function
<ul>
<li><code>overrides</code>ConfigRule[] optional</li>
<li><code>matchPatterns</code>RegExp[] optional</li>
<li><code>options</code> Object optional {
<code>verbose</code> boolean optional
}</li>
</ul>
</li>
</ul>
