---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/get-started/rest-api/
  description: Use the Cloudflare Workers AI REST API to deploy a large language model (LLM).
  full_title: Get started - REST API · Cloudflare Workers AI docs
  head_html: <title>Get started - REST API · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Cloudflare Workers AI REST API to deploy a large language model (LLM)."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/get-started/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/get-started/rest-api/index.md"><meta property="og:title" content="Get started - REST API · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Cloudflare Workers AI REST API to deploy a large language model (LLM)."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/get-started/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/get-started/rest-api/#page","headline":"Get started - REST API \u00b7 Cloudflare Workers AI docs","description":"Use the Cloudflare Workers AI REST API to deploy a large language model (LLM).","url":"https://developers.cloudflare.com/workers-ai/get-started/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/get-started/rest-api/
  schema: 1
---
<p>This guide will instruct you through setting up and deploying your first Workers AI project. You will use the Workers AI REST API to experiment with a large language model (LLM).</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</p>
<h2 id="1-get-api-token-and-account-id"><ol>
<li>Get API token and Account ID</li>
</ol></h2>
<p>You need your API token and Account ID to use the REST API.</p>
<p>To get these values:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers AI</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Use REST API</strong>.</li>
<li>Get your API token:
<ol>
<li>Select <strong>Create a Workers AI API Token</strong>.</li>
<li>Review the prefilled information.</li>
<li>Select <strong>Create API Token</strong>.</li>
<li>Select <strong>Copy API Token</strong>.</li>
<li>Save that value for future use. This token will be visible <a href="/fundamentals/api/get-started/create-token/">on your profile</a>.</li>
</ol>
</li>
<li>For <strong>Get Account ID</strong>, copy the value for <strong>Account ID</strong>. Save that value for future use.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15812.md")
</aside>
<h2 id="2-run-a-model-via-api"><ol start="2">
<li>Run a model via API</li>
</ol></h2>
<p>After creating your API token, authenticate and make requests to the API using your API token in the request.</p>
<p>You will use the <a href="/api/resources/ai/methods/run/">Execute AI model</a> endpoint to run the <a href="/workers-ai/models/llama-3.1-8b-instruct/"><code>@cf/meta/llama-3.1-8b-instruct</code></a> model:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;d &#x27;{ &quot;prompt&quot;: &quot;Where did the phrase Hello World come from&quot; }&#x27;&#10;</code></pre>
<p>Replace the values for <code>{ACCOUNT_ID}</code> and <code>{API_TOKEN}</code>.</p>
<p>The API response will look like the following:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;response&quot;: &quot;Hello, World first appeared in 1974 at Bell Labs when Brian Kernighan included it in the C programming language example. It became widely used as a basic test program due to simplicity and clarity. It represents an inviting greeting from a program to the world.&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>This example execution uses the <code>@cf/meta/llama-3.1-8b-instruct</code> model, but you can use any of the models in the <a href="/workers-ai/models/">Workers AI models catalog</a>. If using another model, you will need to replace <code>{model}</code> with your desired model name.</p>
<p>By completing this guide, you have created a Cloudflare account (if you did not have one already) and an API token that grants Workers AI read permissions to your account. You executed the <a href="/workers-ai/models/llama-3.1-8b-instruct/"><code>@cf/meta/llama-3.1-8b-instruct</code></a> model using a cURL command from the terminal and received an answer to your prompt in a JSON response.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers-ai/models/">Models</a> - Browse the Workers AI models catalog.</li>
<li><a href="/workers-ai/configuration/ai-sdk">AI SDK</a> - Learn how to integrate with an AI model.</li>
</ul>
