---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/
  description: Set up and deploy your first Workers AI project with embedded function calling.
  full_title: Get Started · Cloudflare Workers AI docs
  head_html: <title>Get Started · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and deploy your first Workers AI project with embedded function calling."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/index.md"><meta property="og:title" content="Get Started · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and deploy your first Workers AI project with embedded function calling."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/#page","headline":"Get Started \u00b7 Cloudflare Workers AI docs","description":"Set up and deploy your first Workers AI project with embedded function calling.","url":"https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/function-calling/embedded/get-started/
  schema: 1
---
<p>This guide will instruct you through setting up and deploying your first Workers AI project with embedded function calling. You will use Workers, a Workers AI binding, the <a href="https://github.com/cloudflare/ai-utils"><code>ai-utils package</code></a>, and a large language model (LLM) to deploy your first AI-powered application on the Cloudflare global network with embedded function calling.</p>
<h2 id="1-create-a-worker-project-with-workers-ai"><ol>
<li>Create a Worker project with Workers AI</li>
</ol></h2>
<p>Follow the <a href="/workers-ai/get-started/workers-wrangler/">Workers AI Get Started Guide</a> until step 2.</p>
<h2 id="2-install-additional-npm-package"><ol start="2">
<li>Install additional npm package</li>
</ol></h2>
<p>Next, run the following command in your project repository to install the Worker AI utilities package.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-add-workers-ai-embedded-function-calling"><ol start="3">
<li>Add Workers AI Embedded function calling</li>
</ol></h2>
<p>Update the <code>index.ts</code> file in your application directory with the following code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15831.md")
</div>
<p>This example imports the utils with <code>import { runWithTools} from &quot;@cloudflare/ai-utils&quot;</code> and follows the API reference below.</p>
<p>Moreover, in this example we define and describe a list of tools that the LLM can leverage to respond to the user query. Here, the list contains of only one tool, the <code>sum</code> function.</p>
<p>Abstracted by the <code>runWithTools</code> function, the following steps occur:</p>
<pre tabindex="0"><code class="language-mermaid">sequenceDiagram&#10;    participant Worker as Worker&#10;    participant WorkersAI as Workers AI&#10;&#10;    Worker-&gt;&gt;+WorkersAI: Send messages, function calling prompt, and available tools&#10;    WorkersAI-&gt;&gt;+Worker: Select tools and arguments for function calling&#10;    Worker--&gt;&gt;-Worker: Execute function&#10;    Worker--&gt;&gt;+WorkersAI: Send messages, function calling prompt and function result&#10;    WorkersAI--&gt;&gt;-Worker: Send response incorporating function output&#10;</code></pre>
<p>The <code>ai-utils package</code> is also open-sourced on <a href="https://github.com/cloudflare/ai-utils">Github</a>.</p>
<h2 id="4-local-development-deployment"><ol start="4">
<li>Local development &amp; deployment</li>
</ol></h2>
<p>Follow steps 4 and 5 of the <a href="/workers-ai/get-started/workers-wrangler/">Workers AI Get Started Guide</a> for local development and deployment.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-embedded-function-calling-charges">Workers AI Embedded Function Calling charges</h3>
@markup("md", "content/.markup/bodies/15830.md")
</aside>
<h2 id="api-reference">API reference</h2>
<p>For more details, refer to <a href="/workers-ai/features/function-calling/embedded/api-reference/">API reference</a>.</p>
