---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/models/
  description: Configure which AI models AI Search uses for embedding, generation, reranking, and query rewriting.
  full_title: Models · Cloudflare AI Search docs
  head_html: <title>Models · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure which AI models AI Search uses for embedding, generation, reranking, and query rewriting."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/models/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/models/index.md"><meta property="og:title" content="Models · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure which AI models AI Search uses for embedding, generation, reranking, and query rewriting."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/models/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/models/#page","headline":"Models \u00b7 Cloudflare AI Search docs","description":"Configure which AI models AI Search uses for embedding, generation, reranking, and query rewriting.","url":"https://developers.cloudflare.com/ai-search/configuration/models/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/models/
  schema: 1
---
<p>AI Search uses models at multiple stages. You can configure which models are used, or let AI Search automatically select a smart default for you.</p>
<h2 id="models-usage">Models usage</h2>
<p>AI Search leverages Workers AI models in the following stages:</p>
<ul>
<li>Image to markdown conversion (if images are in data source): Converts image content to Markdown using object detection and captioning models.</li>
<li>Embedding: Transforms your documents and queries into vector representations for semantic search.</li>
<li>Query rewriting (optional): Reformulates the user’s query to improve retrieval accuracy.</li>
<li>Reranking (optional): Reorders retrieved results by semantic relevance using a cross-encoder model.</li>
<li>Generation: Produces the final response from retrieved context.</li>
</ul>
<h2 id="model-providers">Model providers</h2>
<p>All AI Search instances support models from <a href="/workers-ai">Workers AI</a>. You can use other providers (such as OpenAI or Anthropic) in AI Search by adding their API keys to an <a href="/ai-gateway">AI Gateway</a> and connecting that gateway to your AI Search.</p>
<p>To use AI Search with other model providers:</p>
<ol>
<li>
<p>Add provider keys to <a href="/ai-gateway/configuration/bring-your-own-keys/">AI Gateway</a>.</p>
</li>
<li>
<p>Connect the gateway to AI Search.</p>
<ul>
<li>When creating a new AI Search, select the AI Gateway with your provider keys.</li>
<li>For an existing AI Search, go to <strong>Settings</strong> and switch to a gateway that has your keys under <strong>Resources</strong>.</li>
</ul>
</li>
<li>
<p>Select models</p>
<ul>
<li>Embedding model: Only available to be changed when creating a new AI Search.</li>
<li>Generation model: Can be selected when creating a new AI Search and can be changed at any time in <strong>Settings</strong>.</li>
</ul>
</li>
</ol>
<p>AI Search supports a subset of models that have been selected to provide the best experience. Refer to the list of <a href="/ai-search/configuration/models/supported-models/">supported models</a>.</p>
<h3 id="smart-default">Smart default</h3>
<p>If you choose <strong>Smart Default</strong> in your model selection, then AI Search will select a Cloudflare recommended model and will update it automatically for you over time. You can switch to explicit model configuration at any time by visiting <strong>Settings</strong>.</p>
<h3 id="per-request-generation-model-override">Per-request generation model override</h3>
<p>While the generation model can be set globally at the AI Search instance level, you can also override it on a per-request basis in the <a href="/ai-search/api/search/rest-api/#chat-completions">AI Search API</a>. This is useful when you need dynamic selection of generation models based on context or user preferences.</p>
<h2 id="model-deprecation">Model deprecation</h2>
<p>AI Search may deprecate support for a given model in order to provide support for better-performing models with improved capabilities. When a model is being deprecated, we announce the change and provide an end-of-life date after which the model will no longer be accessible. Applications that depend on AI Search may therefore require occasional updates to continue working reliably.</p>
<h3 id="model-lifecycle">Model lifecycle</h3>
<p>AI Search models follow a defined lifecycle to ensure stability and predictable deprecation:</p>
<ol>
<li><strong>Production:</strong> The model is actively supported and recommended for use. It is included in Smart Defaults and receives ongoing updates and maintenance.</li>
<li><strong>Announcement &amp; Transition:</strong> The model remains available but has been marked for deprecation. An end-of-life date is communicated through documentation, release notes, and other official channels. During this phase, users are encouraged to migrate to the recommended replacement model.</li>
<li><strong>Automatic Upgrade (if applicable):</strong> If you have selected the Smart Default option, AI Search will automatically upgrade requests to a recommended replacement.</li>
<li><strong>End of life:</strong> The model is no longer available. Any requests to the retired model return a clear error message, and the model is removed from documentation and Smart Defaults.</li>
</ol>
<p>Learn more about models and their lifecycle status in <a href="/ai-search/configuration/models/supported-models/">supported models</a>.</p>
<h3 id="best-practices">Best practices</h3>
<ul>
<li>Regularly check the <a href="/ai-search/platform/release-note/">release note</a> for updates.</li>
<li>Plan migration efforts according to the communicated end-of-life date.</li>
<li>Migrate and test the recommended replacement models before the end-of-life date.</li>
</ul>
