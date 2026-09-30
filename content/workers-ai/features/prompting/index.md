---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/prompting/
  description: Structure prompts for Workers AI text generation models using system, user, and assistant message roles.
  full_title: Prompting · Cloudflare Workers AI docs
  head_html: <title>Prompting · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Structure prompts for Workers AI text generation models using system, user, and assistant message roles."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/prompting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/prompting/index.md"><meta property="og:title" content="Prompting · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Structure prompts for Workers AI text generation models using system, user, and assistant message roles."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/prompting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers AI"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/prompting/#page","headline":"Prompting \u00b7 Cloudflare Workers AI docs","description":"Structure prompts for Workers AI text generation models using system, user, and assistant message roles.","url":"https://developers.cloudflare.com/workers-ai/features/prompting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/prompting/
  schema: 1
---
<p>messages: [
{ role: &quot;system&quot;, content: &quot;you are a very funny comedian and you like emojis&quot; },
{ role: &quot;user&quot;, content: &quot;tell me a joke about cloudflare&quot; },
],
};`;</p>
<p>messages: [
{ role: &quot;system&quot;, content: &quot;you are a professional computer science assistant&quot; },
{ role: &quot;user&quot;, content: &quot;what is WASM?&quot; },
{ role: &quot;assistant&quot;, content: &quot;WASM (WebAssembly) is a binary instruction format that is designed to be a platform-agnostic&quot; },
{ role: &quot;user&quot;, content: &quot;does Python compile to WASM?&quot; },
{ role: &quot;assistant&quot;, content: &quot;No, Python does not directly compile to WebAssembly&quot; },
{ role: &quot;user&quot;, content: &quot;what about Rust?&quot; },
],
};`;</p>
<p>prompt: &quot;tell me a joke about cloudflare&quot;;
}`;</p>
<p>prompt: &quot;<s>[INST]comedian[/INST]</s>\n[INST]tell me a joke about cloudflare[/INST]&quot;,
raw: true
};`;</p>
<p>Part of getting good results from text generation models is asking questions correctly. LLMs are usually trained with specific predefined templates, which should then be used with the model's tokenizer for better results when doing inference tasks.</p>
<p>There are two ways to prompt text generation models with Workers AI:</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15816.md")
</aside>
<h3 id="scoped-prompts">Scoped Prompts</h3>
<p>This is the <strong>recommended</strong> method. With scoped prompts, Workers AI takes the burden of knowing and using different chat templates for different models and provides a unified interface to developers when building prompts and creating text generation tasks.</p>
<p>Scoped prompts are a list of messages. Each message defines two keys: the role and the content.</p>
<p>Typically, the role can be one of three options:</p>
<ul>
<li><strong>system</strong> - System messages define the AI's personality. You can
use them to set rules and how you expect the AI to behave.</li>
<li><strong>user</strong> - User messages are where you actually query the AI by
providing a question or a conversation.</li>
<li><strong>assistant</strong> - Assistant messages hint to the AI about the
desired output format. Not all models support this role.</li>
</ul>
<p>OpenAI has a <a href="https://platform.openai.com/docs/guides/text-generation#messages-and-roles">good explanation</a> of how they use these roles with their GPT models. Even though chat templates are flexible, other text generation models tend to follow the same conventions.</p>
<p>Here's an input example of a scoped prompt using system and user roles:</p>
<pre tabindex="0"><code class="language-js">{&#10;  messages: [&#10;    { role: &quot;system&quot;, content: &quot;you are a very funny comedian and you like emojis&quot; },&#10;    { role: &quot;user&quot;, content: &quot;tell me a joke about cloudflare&quot; },&#10;  ],&#10;};</code></pre>
<p>Here's a better example of a chat session using multiple iterations between the user and the assistant.</p>
<pre tabindex="0"><code class="language-js">{&#10;  messages: [&#10;    { role: &quot;system&quot;, content: &quot;you are a professional computer science assistant&quot; },&#10;    { role: &quot;user&quot;, content: &quot;what is WASM?&quot; },&#10;    { role: &quot;assistant&quot;, content: &quot;WASM (WebAssembly) is a binary instruction format that is designed to be a platform-agnostic&quot; },&#10;    { role: &quot;user&quot;, content: &quot;does Python compile to WASM?&quot; },&#10;    { role: &quot;assistant&quot;, content: &quot;No, Python does not directly compile to WebAssembly&quot; },&#10;    { role: &quot;user&quot;, content: &quot;what about Rust?&quot; },&#10;  ],&#10;};</code></pre>
<p>Note that different LLMs are trained with different templates for different use cases. While Workers AI tries its best to abstract the specifics of each LLM template from the developer through a unified API, you should always refer to the model documentation for details. For example, instruct models like Codellama are fine-tuned to respond to a user-provided instruction, while chat models expect fragments of dialogs as input.</p>
<h3 id="unscoped-prompts">Unscoped Prompts</h3>
<p>You can use unscoped prompts to send a single question to the model without worrying about providing any context. Workers AI will automatically convert your <code>prompt</code> input to a reasonable default scoped prompt internally so that you get the best possible prediction.</p>
<pre tabindex="0"><code class="language-js">{&#10;  prompt: &quot;tell me a joke about cloudflare&quot;;&#10;}</code></pre>
<p>You can also use unscoped prompts to construct the model chat template manually. In this case, you can use the raw parameter. Here's an input example of a <a href="https://docs.mistral.ai/models/#chat-template">Mistral</a> chat template prompt:</p>
<pre tabindex="0"><code class="language-js">{&#10;  prompt: &quot;&lt;s&gt;[INST]comedian[/INST]&lt;/s&gt;\n[INST]tell me a joke about cloudflare[/INST]&quot;,&#10;  raw: true&#10;};</code></pre>
