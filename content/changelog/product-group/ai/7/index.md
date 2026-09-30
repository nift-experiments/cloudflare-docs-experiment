---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/ai/7/
  description: '2025-04-23'
  full_title: AI changelog - page 7 | Cloudflare Docs
  head_html: <title>AI changelog - page 7 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-04-23"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/ai/7/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI changelog - page 7"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-04-23"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/ai/7/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/ai/7/#page","headline":"AI changelog - page 7 | Cloudflare Docs","description":"2025-04-23","url":"https://developers.cloudflare.com/changelog/product-group/ai/7/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/ai/7/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="metadata-filtering-and-multitenancy-support-in-autorag"><a href="/changelog/post/2025-04-23-autorag-metadata-filtering/">Metadata filtering and multitenancy support in AutoRAG</a></h2>
<p><em>2025-04-23</em></p>
<p>You can now filter <a href="/ai-search/">AutoRAG</a> search results by <code>folder</code> and <code>timestamp</code> using <a href="/ai-search/configuration/indexing/metadata/">metadata filtering</a> to narrow down the scope of your query.</p>
<p>This makes it easy to build <a href="/ai-search/how-to/per-tenant-search/">multitenant experiences</a> where each user can only access their own data. By organizing your content into per-tenant folders and applying a <code>folder</code> filter at query time, you ensure that each tenant retrieves only their own documents.</p>
<p><strong>Example folder structure:</strong></p>
<pre tabindex="0"><code class="language-bash">customer-a/logs/&#10;customer-a/contracts/&#10;customer-b/contracts/&#10;</code></pre>
<p><strong>Example query:</strong></p>
<pre tabindex="0"><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;When did I sign my agreement contract?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;folder&quot;,&#10;		value: &quot;customer-a/contracts/&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select <strong>Sync index</strong>. Metadata filtering is available for all data indexed on or after <strong>April 21, 2025</strong>.</p>
<p>If you are new to AutoRAG, get started with the <a href="/ai-search/get-started/">Get started AutoRAG guide</a>.</p>


<h2 id="workers-ai-for-developer-week-faster-inference-new-models-async-batch-api-expanded-lora-support"><a href="/changelog/post/2025-04-11-new-models-faster-inference/">Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support</a></h2>
<p><em>2025-04-11</em></p>
<p>Happy Developer Week 2025! Workers AI is excited to announce a couple of new features and improvements available today. Check out our <a href="https://blog.cloudflare.com/workers-ai-improvements">blog</a> for all the announcement details.</p>
<h4 id="2025-04-11-new-models-faster-inference-faster-inference-new-models">Faster inference + New models</h4>
<p>We’re rolling out some in-place improvements to our models that can help speed up inference by 2-4x! Users of the models below will enjoy an automatic speed boost starting today:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a> gets a speed boost of 2-4x, leveraging techniques like speculative decoding, prefix caching, and an updated inference backend.</li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a>, <a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a>, <a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a> get an updated back end, which should improve inference times by 2x.
<ul>
<li>With the <code>bge</code> models, we’re also announcing a new parameter called <code>pooling</code> which can take <code>cls</code> or <code>mean</code> as options. We highly recommend using <code>pooling: cls</code> which will help generate more accurate embeddings. However, embeddings generated with cls pooling are not backwards compatible with mean pooling. For this to not be a breaking change, the default remains as mean pooling. Please specify <code>pooling: cls</code> to enjoy more accurate embeddings going forward.</li>
</ul>
</li>
</ul>
<p>We’re also excited to launch a few new models in our catalog to help round out your experience with Workers AI. We’ll be deprecating some older models in the future, so stay tuned for a deprecation announcement. Today’s new models include:</p>
<ul>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a>: a 24B parameter model achieving state-of-the-art capabilities comparable to larger models, with support for vision and tool calling.</li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a>: well-suited for a variety of text generation and image understanding tasks, including question answering, summarization and reasoning, with a 128K context window, and multilingual support in over 140 languages.</li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a>: a medium-sized reasoning model, which is capable of achieving competitive performance against state-of-the-art reasoning models, e.g., DeepSeek-R1, o1-mini.</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a>: the current state-of-the-art open-source code LLM, with its coding abilities matching those of GPT-4o.</li>
</ul>
<h4 id="2025-04-11-new-models-faster-inference-batch-inference">Batch Inference</h4>
<p>Introducing a new batch inference feature that allows you to send us an array of requests, which we will fulfill as fast as possible and send them back as an array. This is really helpful for large workloads such as summarization, embeddings, etc. where you don’t have a human-in-the-loop. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if we don’t have enough capacity at a given time.</p>
<p>Check out the <a href="/workers-ai/features/batch-api/">tutorial</a> to get started! Models that support batch inference today include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-m3/"><code>@cf/baai/bge-m3</code></a></li>
<li><a href="/workers-ai/models/m2m100-1.2b/"><code>@cf/meta/m2m100-1.2b</code></a></li>
</ul>
<h4 id="2025-04-11-new-models-faster-inference-expanded-lora-support">Expanded LoRA support</h4>
<p>We’ve upgraded our LoRA experience to include 8 newer models, and can support ranks of up to 32 with a 300MB safetensors file limit (previously limited to rank of 8 and 100MB safetensors) Check out our <a href="/workers-ai/features/fine-tunes/loras/">LoRAs page</a> to get started. Models that support LoRAs now include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.2-11b-vision-instruct/"><code>@cf/meta/llama-3.2-11b-vision-instruct</code></a></li>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a></li>
<li><a href="/workers-ai/models/llama-3.1-8b-instruct-fast/"><code>@cf/meta/llama-3.1-8b-instruct-fast</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/deepseek-r1-distill-qwen-32b/"><code>@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a></li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a></li>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a></li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a></li>
</ul>


<h2 id="build-mcp-servers-with-the-agents-sdk"><a href="/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/">Build MCP servers with the Agents SDK</a></h2>
<p><em>2025-04-07</em></p>
<p>The Agents SDK now includes built-in support for building remote MCP (Model Context Protocol) servers directly as part of your Agent. This allows you to easily create and manage MCP servers, without the need for additional infrastructure or configuration.</p>
<p>The SDK includes a new <code>MCPAgent</code> class that extends the <code>Agent</code> class and allows you to expose resources and tools over the MCP protocol, as well as authorization and authentication to enable remote MCP servers.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17623.md")</div>
<p>See <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp">the example</a> for the full code and as the basis for building your own MCP servers, and the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client">client example</a> for how to build an Agent that acts as an MCP client.</p>
<p>To learn more, review the <a href="https://blog.cloudflare.com/building-ai-agents-with-mcp-authn-authz-and-durable-objects">announcement blog</a> as part of Developer Week 2025.</p>
<h4 id="2025-04-07-mcp-servers-agents-sdk-updates-agents-sdk-updates">Agents SDK updates</h4>
<p>We've made a number of improvements to the <a href="/agents/">Agents SDK</a>, including:</p>
<ul>
<li>Support for building MCP servers with the new <code>MCPAgent</code> class.</li>
<li>The ability to export the current agent, request and WebSocket connection context using <code>import { context } from &quot;agents&quot;</code>, allowing you to minimize or avoid direct dependency injection when calling tools.</li>
<li>Fixed a bug that prevented query parameters from being sent to the Agent server from the <code>useAgent</code> React hook.</li>
<li>Automatically converting the <code>agent</code> name in <code>useAgent</code> or <code>useAgentChat</code> to kebab-case to ensure it matches the naming convention expected by <a href="/agents/runtime/communication/routing/"><code>routeAgentRequest</code></a>.</li>
</ul>
<p>To install or update the Agents SDK, run <code>npm i agents@latest</code> in an existing project, or explore the <code>agents-starter</code> project:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest -- --template cloudflare/agents-starter&#10;</code></pre>
<p>See the full release notes and changelog <a href="https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md">on the Agents SDK repository</a> and</p>


<h2 id="create-fully-managed-rag-pipelines-for-your-ai-applications-with-autorag"><a href="/changelog/post/2025-04-07-autorag-open-beta/">Create fully-managed RAG pipelines for your AI applications with AutoRAG</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/ai-search/">AutoRAG</a> is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to <a href="/r2/get-started/">R2</a>, and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.</p>
<p>With AutoRAG, you can:</p>
<ul>
<li><strong>Customize your pipeline:</strong> Choose from <a href="/workers-ai">Workers AI</a> models, configure chunking strategies, edit system prompts, and more.</li>
<li><strong>Instant setup:</strong> AutoRAG provisions everything you need from <a href="/vectorize">Vectorize</a>, <a href="/ai-gateway">AI gateway</a>, to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.</li>
<li><strong>Keep your index fresh:</strong> AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.</li>
<li><strong>Ask questions:</strong> Query your data and receive grounded responses via a <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">API</a>.</li>
</ul>
<p>Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.</p>
<p>Get started in the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a> or check out the <a href="/ai-search/get-started/">guide</a> for instructions on how to build your RAG pipeline today.</p>


<h2 id="browser-rendering-rest-api-is-generally-available-with-new-endpoints-and-a-free-tier"><a href="/changelog/post/2025-04-07-br-free-ga-playwright/">Browser Rendering REST API is Generally Available, with new endpoints and a free tier</a></h2>
<p><em>2025-04-07</em></p>
<p>We’re excited to announce Browser Rendering is now available on the <a href="https://www.cloudflare.com/plans/developer-platform/">Workers Free plan</a>, making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.</p>
<p>The Browser Rendering <strong><a href="/browser-run/quick-actions/">REST API</a> is now Generally Available</strong>, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:</p>
<ul>
<li><strong>Extract structured data</strong> – Use <code>/json</code> to retrieve structured data from a webpage.</li>
<li><strong>Retrieve links</strong> – Use <code>/links</code> to pull all links from a webpage.</li>
<li><strong>Convert to Markdown</strong> – Use <code>/markdown</code> to convert webpage content into Markdown format.</li>
</ul>
<p>For example, to fetch the Markdown representation of a webpage:</p>
<pre tabindex="0"><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of endpoints, check out our <a href="/browser-run/quick-actions/">REST API documentation</a>. You can also interact with Browser Rendering via the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare TypeScript SDK</a>.</p>
<p>We also recently landed support for <a href="/browser-run/playwright/">Playwright</a> in Browser Rendering for browser automation from Cloudflare <a href="/workers/">Workers</a>, in addition to <a href="/browser-run/puppeteer/">Puppeteer</a>, giving you more flexibility to test across different browser environments.</p>
<p>Visit the <a href="/browser-run/">Browser Rendering docs</a> to learn more about how to use headless browsers in your applications.</p>


<h2 id="playwright-for-browser-rendering-now-available"><a href="/changelog/post/2025-04-04-playwright-beta/">Playwright for Browser Rendering now available</a></h2>
<p><em>2025-04-04</em></p>
<p>We're excited to share that you can now use Playwright's browser automation <a href="https://playwright.dev/docs/api/class-playwright">capabilities</a> from Cloudflare <a href="/workers/">Workers</a>.</p>
<p><a href="https://playwright.dev/">Playwright</a> is an open-source package developed by Microsoft that can do browser automation tasks; it's commonly used to write software tests, debug applications, create screenshots, and crawl pages. Like <a href="/browser-run/puppeteer/">Puppeteer</a>, we <a href="https://github.com/cloudflare/playwright">forked</a> Playwright and modified it to be compatible with Cloudflare Workers and <a href="/browser-run/">Browser Rendering</a>.</p>
<p>Below is an example of how to use Playwright with Browser Rendering to test a TODO application using assertions:</p>
<pre tabindex="0"><code class="language-ts">import { launch, type BrowserWorker } from &quot;@cloudflare/playwright&quot;;&#10;import { expect } from &quot;@cloudflare/playwright/test&quot;;&#10;&#10;interface Env {&#10;	MYBROWSER: BrowserWorker;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const browser = await launch(env.MYBROWSER);&#10;		const page = await browser.newPage();&#10;&#10;		await page.goto(&quot;https://demo.playwright.dev/todomvc&quot;);&#10;&#10;		const TODO_ITEMS = [&#10;			&quot;buy some cheese&quot;,&#10;			&quot;feed the cat&quot;,&#10;			&quot;book a doctors appointment&quot;,&#10;		];&#10;&#10;		const newTodo = page.getByPlaceholder(&quot;What needs to be done?&quot;);&#10;		for (const item of TODO_ITEMS) {&#10;			await newTodo.fill(item);&#10;			await newTodo.press(&quot;Enter&quot;);&#10;		}&#10;&#10;		await expect(page.getByTestId(&quot;todo-title&quot;)).toHaveCount(TODO_ITEMS.length);&#10;&#10;		await Promise.all(&#10;			TODO_ITEMS.map((value, index) =&gt;&#10;				expect(page.getByTestId(&quot;todo-title&quot;).nth(index)).toHaveText(value),&#10;			),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>Playwright is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright"><code>@cloudflare/playwright</code></a> and the code is at <a href="https://github.com/cloudflare/playwright">GitHub</a>.</p>
<p>Learn more in our <a href="/browser-run/playwright/">documentation</a>.</p>


<h2 id="ai-gateway-launches-realtime-websockets-api"><a href="/changelog/post/2025-03-20-websockets/">AI Gateway launches Realtime WebSockets API</a></h2>
<p><em>2025-03-21</em></p>
<p>We are excited to announce that <a href="/ai-gateway/">AI Gateway</a> now supports real-time AI interactions with the new <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a>.</p>
<p>This new capability allows developers to establish persistent, low-latency connections between their applications and AI models, enabling natural, real-time conversational AI experiences, including speech-to-speech interactions.</p>
<p>The Realtime WebSockets API works with the <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI Realtime API</a>, <a href="https://ai.google.dev/gemini-api/docs/multimodal-live">Google Gemini Live API</a>, and supports real-time text and speech interactions with models from <a href="https://docs.cartesia.ai/api-reference/tts/tts">Cartesia</a>, and <a href="https://elevenlabs.io/docs/conversational-ai/api-reference/conversational-ai/websocket">ElevenLabs</a>.</p>
<p>Here's how you can connect AI Gateway to <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI's Realtime API</a> using WebSockets:</p>
<pre tabindex="0"><code class="language-javascript">import WebSocket from &quot;ws&quot;;&#10;&#10;const url =&#10;	&quot;wss://gateway.ai.cloudflare.com/v1/&lt;account_id&gt;/&lt;gateway&gt;/openai?model=gpt-4o-realtime-preview-2024-12-17&quot;;&#10;const ws = new WebSocket(url, {&#10;	headers: {&#10;		&quot;cf-aig-authorization&quot;: process.env.CLOUDFLARE_API_KEY,&#10;		Authorization: &quot;Bearer &quot; + process.env.OPENAI_API_KEY,&#10;		&quot;OpenAI-Beta&quot;: &quot;realtime=v1&quot;,&#10;	},&#10;});&#10;&#10;ws.on(&quot;open&quot;, () =&gt; console.log(&quot;Connected to server.&quot;));&#10;ws.on(&quot;message&quot;, (message) =&gt; console.log(JSON.parse(message.toString())));&#10;&#10;ws.send(&#10;	JSON.stringify({&#10;		type: &quot;response.create&quot;,&#10;		response: { modalities: [&quot;text&quot;], instructions: &quot;Tell me a joke&quot; },&#10;	}),&#10;);&#10;</code></pre>
<p>Get started by checking out the <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a> documentation.</p>


<h2 id="markdown-conversion-in-workers-ai"><a href="/changelog/post/2025-03-20-markdown-conversion/">Markdown conversion in Workers AI</a></h2>
<p><em>2025-03-20</em></p>
<p>Document conversion plays an important role when designing and developing AI applications and agents. Workers AI now provides the <code>toMarkdown</code> utility method that developers can use to for quick, easy, and convenient conversion and summary of documents in multiple formats to Markdown language.</p>
<p>You can call this new tool using a binding by calling <code>env.AI.toMarkdown()</code> or the using the <a href="/api/resources/ai/">REST API</a> endpoint.</p>
<p>In this example, we fetch a PDF document and an image from R2 and feed them both to <code>env.AI.toMarkdown()</code>. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.</p>
<pre tabindex="0"><code class="language-typescript">import { Env } from &quot;./env&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf&#10;		const pdf = await env.R2.get(&quot;somatosensory.pdf&quot;);&#10;&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg&#10;		const cat = await env.R2.get(&quot;cat.jpeg&quot;);&#10;&#10;		return Response.json(&#10;			await env.AI.toMarkdown([&#10;				{&#10;					name: &quot;somatosensory.pdf&quot;,&#10;					blob: new Blob([await pdf.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;				{&#10;					name: &quot;cat.jpeg&quot;,&#10;					blob: new Blob([await cat.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;			]),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>This is the result:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;name&quot;: &quot;somatosensory.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;# somatosensory.pdf\n## Metadata\n- PDFFormatVersion=1.4\n- IsLinearized=false\n- IsAcroFormPresent=false\n- IsXFAPresent=false\n- IsCollectionPresent=false\n- IsSignaturesPresent=false\n- Producer=Prince 20150210 (www.princexml.com)\n- Title=Anatomy of the Somatosensory System\n\n## Contents\n### Page 1\nThis is a sample document to showcase...&quot;&#10;	},&#10;	{&#10;		&quot;name&quot;: &quot;cat.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;The image is a close-up photograph of Grumpy Cat, a cat with a distinctive grumpy expression and piercing blue eyes. The cat has a brown face with a white stripe down its nose, and its ears are pointed upright. Its fur is light brown and darker around the face, with a pink nose and mouth. The cat&#x27;s eyes are blue and slanted downward, giving it a perpetually grumpy appearance. The background is blurred, but it appears to be a dark brown color. Overall, the image is a humorous and iconic representation of the popular internet meme character, Grumpy Cat. The cat&#x27;s facial expression and posture convey a sense of displeasure or annoyance, making it a relatable and entertaining image for many people.&quot;&#10;	}&#10;]&#10;</code></pre>
<p>See <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> for more information on supported formats, REST API and pricing.</p>


<h2 id="npm-i-agents"><a href="/changelog/post/2025-03-18-npm-i-agents/">npm i agents</a></h2>
<p><em>2025-03-18</em></p>
<img src="/assets/upstream/images/agents/npm-i-agents.apng" alt="npm i agents" width="1000" height="541" />
<h4 id="2025-03-18-npm-i-agents-agents-sdk-agents"><code>agents-sdk</code> -&gt; <code>agents</code> <span class="nb-badge">Updated</span></h4>
<p>📝 <strong>We've renamed the Agents package to <code>agents</code></strong>!</p>
<p>If you've already been building with the Agents SDK, you can update your dependencies to use the new package name, and replace references to <code>agents-sdk</code> with <code>agents</code>:</p>
<pre tabindex="0"><code class="language-sh">&#35; Install the new package&#10;npm i agents&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Remove the old (deprecated) package&#10;npm uninstall agents-sdk&#10;&#10;&#35; Find instances of the old package name in your codebase&#10;grep -r &#x27;agents-sdk&#x27; .&#10;&#35; Replace instances of the old package name with the new one&#10;&#35; (or use find-replace in your editor)&#10;sed -i &#x27;s/agents-sdk/agents/g&#x27; $(grep -rl &#x27;agents-sdk&#x27; .)&#10;</code></pre>
<p>All future updates will be pushed to the new <code>agents</code> package, and the older package has been marked as deprecated.</p>
<h4 id="2025-03-18-npm-i-agents-agents-sdk-updates">Agents SDK updates <span class="nb-badge">New</span></h4>
<p>We've added a number of big new features to the Agents SDK over the past few weeks, including:</p>
<ul>
<li>You can now set <code>cors: true</code> when using <code>routeAgentRequest</code> to return permissive default CORS headers to Agent responses.</li>
<li>The regular client now syncs state on the agent (just like the React version).</li>
<li><code>useAgentChat</code> bug fixes for passing headers/credentials, including properly clearing cache on unmount.</li>
<li>Experimental <code>/schedule</code> module with a prompt/schema for adding scheduling to your app (with evals!).</li>
<li>Changed the internal <code>zod</code> schema to be compatible with the limitations of Google's Gemini models by removing the discriminated union, allowing you to use Gemini models with the scheduling API.</li>
</ul>
<p>We've also fixed a number of bugs with state synchronization and the React hooks.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17621.md")</div>
<h4 id="2025-03-18-npm-i-agents-call-agent-methods-from-your-client-code">Call Agent methods from your client code <span class="nb-badge">New</span></h4>
<p>We've added a new <a href="/agents/runtime/agents-api/"><code>@unstable_callable()</code></a> decorator for defining methods that can be called directly from clients. This allows you call methods from within your client code: you can call methods (with arguments) and get native JavaScript objects back.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17622.md")</div>
<h4 id="2025-03-18-npm-i-agents-agents-starter">agents-starter <span class="nb-badge">Updated</span></h4>
<p>We've fixed a number of small bugs in the <a href="https://github.com/cloudflare/agents-starter"><code>agents-starter</code></a> project — a real-time, chat-based example application with tool-calling &amp; human-in-the-loop built using the Agents SDK. The starter has also been upgraded to use the latest <a href="/changelog/2025-03-13-wrangler-v4/">wrangler v4</a> release.</p>
<p>If you're new to Agents, you can install and run the <code>agents-starter</code> project in two commands:</p>
<pre tabindex="0"><code class="language-sh">&#35; Install it&#10;$ npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; Run it&#10;$ npm run start&#10;</code></pre>
<p>You can use the starter as a template for your own Agents projects: open up <code>src/server.ts</code> and <code>src/client.tsx</code> to see how the Agents SDK is used.</p>
<h4 id="2025-03-18-npm-i-agents-more-documentation">More documentation <span class="nb-badge">Updated</span></h4>
<p>We've heard your feedback on the Agents SDK documentation, and we're shipping more API reference material and usage examples, including:</p>
<ul>
<li>Expanded <a href="/agents/runtime/">API reference documentation</a>, covering the methods and properties exposed by the Agents SDK, as well as more usage examples.</li>
<li>More <a href="/agents/runtime/agents-api/#client-api">Client API</a> documentation that documents <code>useAgent</code>, <code>useAgentChat</code> and the new <code>@unstable_callable</code> RPC decorator exposed by the SDK.</li>
<li>New documentation on how to <a href="/agents/runtime/communication/routing/">route requests to agents</a> and (optionally) authenticate clients before they connect to your Agents.</li>
</ul>
<p>Note that the Agents SDK is continually growing: the type definitions included in the SDK will always include the latest APIs exposed by the <code>agents</code> package.</p>
<p>If you're still wondering what Agents are, <a href="https://blog.cloudflare.com/build-ai-agents-on-cloudflare/">read our blog on building AI Agents on Cloudflare</a> and/or visit the <a href="/agents/">Agents documentation</a> to learn more.</p>


<h2 id="new-models-in-workers-ai"><a href="/changelog/post/2025-03-17-new-workers-ai-models/">New models in Workers AI</a></h2>
<p><em>2025-03-17</em></p>
<p>Workers AI is excited to add 4 new models to the catalog, including 2 brand new classes of models with a text-to-speech and reranker model. Introducing:</p>
<ul>
<li><a href="/workers-ai/models/bge-m3/">@cf/baai/bge-m3</a> - a multi-lingual embeddings model that supports over 100 languages. It can also simultaneously perform dense retrieval, multi-vector retrieval, and sparse retrieval, with the ability to process inputs of different granularities.</li>
<li><a href="/workers-ai/models/bge-reranker-base/">@cf/baai/bge-reranker-base</a> - our first reranker model! Rerankers are a type of text classification model that takes a query and context, and outputs a similarity score between the two. When used in RAG systems, you can use a reranker after the initial vector search to find the most relevant documents to return to a user by reranking the outputs.</li>
<li><a href="/workers-ai/models/whisper-large-v3-turbo/">@cf/openai/whisper-large-v3-turbo</a> - a faster, more accurate speech-to-text model. This model was added earlier but is graduating out of beta with pricing included today.</li>
<li><a href="/workers-ai/models/melotts/">@cf/myshell-ai/melotts</a> - our first text-to-speech model that allows users to generate an MP3 with voice audio from inputted text.</li>
</ul>
<p>Pricing is available for each of these models on the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<p>This docs update includes a few minor bug fixes to the model schema for llama-guard, llama-3.2-1b, which you can review on the <a href="/workers-ai/changelog/">product changelog</a>.</p>
<p>Try it out and let us know what you think! Stay tuned for more models in the coming days.</p>


<h2 id="new-rest-api-is-in-open-beta"><a href="/changelog/post/2025-02-27-br-rest-api-beta/">New REST API is in open beta!</a></h2>
<p><em>2025-02-27</em></p>
<p>We've released a new REST API for <a href="/browser-run/">Browser Rendering</a> in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.</p>
<p>With the <strong>REST API</strong> you can:</p>
<ul>
<li><strong>Capture screenshots</strong> – Use <code>/screenshot</code> to take a screenshot of a webpage from provided URL or HTML.</li>
<li><strong>Generate PDFs</strong> – Use <code>/pdf</code> to convert web pages into PDFs.</li>
<li><strong>Extract HTML content</strong> – Use <code>/content</code> to retrieve the full HTML from a page.
<strong>Snapshot (HTML + Screenshot)</strong> – Use <code>/snapshot</code> to capture both the page's HTML and a screenshot in one request</li>
<li><strong>Scrape Web Elements</strong> – Use <code>/scrape</code> to extract specific elements from a page.</li>
</ul>
<p>For example, to capture a screenshot:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;Hello World!&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;      &quot;type&quot;: &quot;webp&quot;,&#10;      &quot;omitBackground&quot;: true&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.webp&quot;&#10;</code></pre>
<p>Learn more in our <a href="/browser-run/quick-actions/">documentation</a>.</p>


<h2 id="introducing-guardrails-in-ai-gateway"><a href="/changelog/post/2025-02-26-guardrails/">Introducing Guardrails in AI Gateway</a></h2>
<p><em>2025-02-26</em></p>
<p><a href="/ai-gateway/">AI Gateway</a> now includes <a href="/ai-gateway/features/guardrails/">Guardrails</a>, to help you monitor your AI apps for harmful or inappropriate content and deploy safely.</p>
<p>Within the AI Gateway settings, you can configure:</p>
<ul>
<li><strong>Guardrails</strong>: Enable or disable content moderation as needed.</li>
<li><strong>Evaluation scope</strong>: Select whether to moderate user prompts, model responses, or both.</li>
<li><strong>Hazard categories</strong>: Specify which categories to monitor and determine whether detected inappropriate content should be blocked or flagged.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/Guardrails.png" alt="Guardrails in AI Gateway" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/guardrails-in-ai-gateway/">blog</a> or our <a href="/ai-gateway/features/guardrails/">documentation</a>.</p>


<h2 id="introducing-the-agents-sdk"><a href="/changelog/post/2025-02-25-agents-sdk/">Introducing the Agents SDK</a></h2>
<p><em>2025-02-25</em></p>
<p>We've released the <a href="http://blog.cloudflare.com/build-ai-agents-on-cloudflare/">Agents SDK</a>, a package and set of tools that help you build and ship AI Agents.</p>
<p>You can get up and running with a <a href="https://github.com/cloudflare/agents-starter">chat-based AI Agent</a> (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; open up README.md and follow the instructions&#10;</code></pre>
<p>You can also add an Agent to any existing Workers application by installing the <code>agents</code> package directly</p>
<pre tabindex="0"><code class="language-sh">npm i agents&#10;</code></pre>
<p>... and then define your first Agent:</p>
<pre tabindex="0"><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;export class YourAgent extends Agent&lt;Env&gt; {&#10;	// Build it out&#10;	// Access state on this.state or query the Agent&#x27;s database via this.sql&#10;	// Handle WebSocket events with onConnect and onMessage&#10;	// Run tasks on a schedule with this.schedule&#10;	// Call AI models&#10;	// ... and/or call other Agents.&#10;}&#10;</code></pre>
<p>Head over to the <a href="/agents/">Agents documentation</a> to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.</p>


<h2 id="workers-ai-now-supports-structured-json-outputs"><a href="/changelog/post/2025-02-25-json-mode/">Workers AI now supports structured JSON outputs.</a></h2>
<p><em>2025-02-25</em></p>
<p>Workers AI now supports structured JSON outputs with <a href="/workers-ai/features/json-mode/">JSON mode</a>, which allows you to request a structured output response when interacting with AI models.</p>
<p>This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.</p>
<p>JSON mode in Workers AI is compatible with the OpenAI SDK's <a href="https://platform.openai.com/docs/guides/structured-outputs">structured outputs</a> <code>response_format</code> API, which can be used directly in a Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17816.md")</div>
<p>To learn more about JSON mode and structured outputs, visit the <a href="/workers-ai/features/json-mode/">Workers AI documentation</a>.</p>


<h2 id="workers-ai-larger-context-windows"><a href="/changelog/post/2025-02-24-context-windows/">Workers AI larger context windows</a></h2>
<p><em>2025-02-24</em></p>
<p>We've updated the Workers AI text generation models to include context windows and limits definitions and changed our APIs to estimate and validate the number of tokens in the input prompt, not the number of characters.</p>
<p>This update allows developers to use larger context windows when interacting with Workers AI models, which can lead to better and more accurate results.</p>
<p>Our <a href="/workers-ai/models/">catalog page</a> provides more information about each model's supported context window.</p>


<h2 id="workers-ai-updated-pricing"><a href="/changelog/post/2025-02-20-updated-pricing-docs/">Workers AI updated pricing</a></h2>
<p><em>2025-02-20</em></p>
<p>We've updated the Workers AI <a href="/workers-ai/platform/pricing/">pricing</a> to include the latest models and how model usage maps to Neurons.</p>
<ul>
<li>Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale</li>
<li>Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.</li>
<li>You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.</li>
</ul>
<p>Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the <a href="/workers-ai/platform/pricing/">Workers AI pricing</a> page to learn more about Workers AI pricing.</p>


<h2 id="build-ai-agents-with-example-prompts"><a href="/changelog/post/2025-02-14-example-ai-prompts/">Build AI Agents with Example Prompts</a></h2>
<p><em>2025-02-14</em></p>
<p>We've added an <a href="/workers/get-started/prompting/">example prompt</a> to help you get started with building AI agents and applications on Cloudflare <a href="/workers/">Workers</a>, including <a href="/workflows/">Workflows</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/kv/">Workers KV</a>.</p>
<p>You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the <code>&lt;user_prompt&gt;&lt;/user_prompt&gt;</code> tags.</p>
<pre tabindex="0"><code class="language-sh">{paste_prompt_here}&#10;&lt;user_prompt&gt;&#10;user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label &#x27;help&#x27; or &#x27;bug&#x27;, and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.&#10;&lt;/user_prompt&gt;&#10;</code></pre>
<p>This prompt is still experimental, but we encourage you to try it out and <a href="https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml">provide feedback</a>.</p>


<h2 id="request-timeouts-and-retries-with-ai-gateway"><a href="/changelog/post/2025-02-05-aig-request-handling/">Request timeouts and retries with AI Gateway</a></h2>
<p><em>2025-02-06</em></p>
<p>AI Gateway adds additional ways to handle requests - <a href="/ai-gateway/configuration/request-handling/#request-timeouts">Request Timeouts</a> and <a href="/ai-gateway/configuration/request-handling/#request-retries">Request Retries</a>, making it easier to keep your applications responsive and reliable.</p>
<p>Timeouts and retries can be used on both the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> or directly to a <a href="/ai-gateway/usage/providers/">supported provider</a>.</p>
<p><strong>Request timeouts</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-timeouts">request timeout</a> allows you to trigger <a href="/ai-gateway/configuration/fallbacks/">fallbacks</a> or a retry if a provider takes too long to respond.</p>
<p>To set a request timeout directly to a provider, add a <code>cf-aig-request-timeout</code> header.</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \&#10; &#45;-header &#x27;Authorization: Bearer {cf_api_token}&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-header &#x27;cf-aig-request-timeout: 5000&#x27;&#10; &#45;-data &#x27;{&quot;prompt&quot;: &quot;What is Cloudflare?&quot;}&#x27;&#10;</code></pre>
<p><strong>Request retries</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-retries">request retry</a> automatically retries failed requests, so you can recover from temporary issues without intervening.</p>
<p>To set up request retries directly to a provider, add the following headers:</p>
<ul>
<li>cf-aig-max-attempts (number)</li>
<li>cf-aig-retry-delay (number)</li>
<li>cf-aig-backoff (&quot;constant&quot; | &quot;linear&quot; | &quot;exponential)</li>
</ul>


<h2 id="ai-gateway-adds-cerebras-elevenlabs-and-cartesia-as-new-providers"><a href="/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/">AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers</a></h2>
<p><em>2025-02-05</em></p>
<p><a href="/ai-gateway/">AI Gateway</a> has added three new providers: <a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a>, <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a>, and <a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a>, giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a> provides text-to-speech models that produce natural-sounding speech with low latency.</li>
<li><a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.</li>
<li><a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a> offers text-to-speech models with human-like voices in 32 languages.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/cerebras2.png" alt="Example of Cerebras log in AI Gateway" /></p>
<p>To get started with AI Gateway, just update the base URL. Here's how you can send a request to <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> using cURL:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer CEREBRAS_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;llama-3.3-70b&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>


<h2 id="ai-gateway-introduces-new-worker-binding-methods"><a href="/changelog/post/2025-01-26-worker-binding-methods/">AI Gateway Introduces New Worker Binding Methods</a></h2>
<p><em>2025-01-30</em></p>
<p>We have released new <a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings API methods</a>, allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.</p>
<p>To add an AI binding to your Worker, include the following in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<p><img src="/assets/upstream/images/ai-gateway/add-binding.png" alt="Add an AI binding to your Worker." /></p>
<p>With the new AI Gateway binding methods, you can now:</p>
<ul>
<li>Send feedback and update metadata with <code>patchLog</code>.</li>
<li>Retrieve detailed log information using <code>getLog</code>.</li>
<li>Execute <a href="/ai-gateway/usage/universal/">universal requests</a> to any AI Gateway provider with <code>run</code>.</li>
</ul>
<p>For example, to send feedback and update metadata using <code>patchLog</code>:</p>
<p><img src="/assets/upstream/images/ai-gateway/send-feedback.png" alt="Send feedback and update metadata using patchLog:" /></p>


<h2 id="increased-browser-rendering-limits"><a href="/changelog/post/2025-01-30-browser-rendering-more-instances/">Increased Browser Rendering limits!</a></h2>
<p><em>2025-01-30</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports 10 concurrent browser instances per account <em>and</em> 10 new instances per minute, up from the previous limits of 2.</p>
<p>This allows you to launch more browser tasks from <a href="/workers">Cloudflare Workers</a>.</p>
<p>To manage concurrent browser sessions, you can use <a href="/queues/">Queues</a> or <a href="/workflows/">Workflows</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17693.md")</div>


<h2 id="ai-gateway-adds-deepseek-as-a-provider"><a href="/changelog/post/2025-01-07-aig-provider-deepseek/">AI Gateway adds DeepSeek as a Provider</a></h2>
<p><em>2025-01-02</em></p>
<p><a href="/ai-gateway/"><strong>AI Gateway</strong></a> now supports <a href="/ai-gateway/usage/providers/deepseek/"><strong>DeepSeek</strong></a>, including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or <a href="/workers-ai/">Workers AI</a>, AI Gateway empowers you to:</p>
<ul>
<li><strong>Monitor</strong>: Gain actionable insights with analytics and logs.</li>
<li><strong>Control</strong>: Implement caching, rate limiting, and fallbacks.</li>
<li><strong>Optimize</strong>: Improve performance with feedback and evaluations.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/deepseek.png" alt="AI Gateway adds DeepSeek as a provider" /></p>
<p>To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>For detailed setup instructions, see our <a href="/ai-gateway/usage/providers/deepseek/">DeepSeek provider documentation</a>.</p>


<h2 id="ai-crawl-control"><a href="/changelog/post/2024-09-23-ai-audit-launch/">AI Crawl Control</a></h2>
<p><em>2024-09-23</em></p>
<p>Every site on Cloudflare now has access to <a href="/ai-crawl-control/"><strong>AI Audit</strong></a>, which summarizes the crawling behavior of popular and known AI services.</p>
<p>You can use this data to:</p>
<ul>
<li>Understand how and how often crawlers access your site (and which content is the most popular).</li>
<li>Block specific AI bots accessing your site.</li>
<li>Use Cloudflare to enforce your <code>robots.txt</code> policy via an automatic WAF rule.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview.png" alt="View AI bot activity with AI Audit" /></p>
<p>To get started, explore <a href="/ai-crawl-control/">AI audit</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/ai/6/">Previous</a><span>Page 7 of 7</span></nav>
