---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/ai/6/
  description: '2025-10-21'
  full_title: AI changelog - page 6 | Cloudflare Docs
  head_html: <title>AI changelog - page 6 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-10-21"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/ai/6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI changelog - page 6"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-10-21"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/ai/6/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/ai/6/#page","headline":"AI changelog - page 6 | Cloudflare Docs","description":"2025-10-21","url":"https://developers.cloudflare.com/changelog/product-group/ai/6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/ai/6/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-robots-txt-tab-for-tracking-crawler-compliance"><a href="/changelog/post/2025-10-21-track-robots-txt/">New Robots.txt tab for tracking crawler compliance</a></h2>
<p><em>2025-10-21</em></p>
<p>AI Crawl Control now includes a <strong>Robots.txt</strong> tab that provides insights into how AI crawlers interact with your <code>robots.txt</code> files.</p>
<h4 id="2025-10-21-track-robots-txt-what-s-new">What's new</h4>
<p>The Robots.txt tab allows you to:</p>
<ul>
<li>Monitor the health status of <code>robots.txt</code> files across all your hostnames, including HTTP status codes, and identify hostnames that need a <code>robots.txt</code> file.</li>
<li>Track the total number of requests to each <code>robots.txt</code> file, with breakdowns of successful versus unsuccessful requests.</li>
<li>Check whether your <code>robots.txt</code> files contain <a href="https://contentsignals.org/">Content Signals</a> directives for AI training, search, and AI input.</li>
<li>Identify crawlers that request paths explicitly disallowed by your <code>robots.txt</code> directives, including the crawler name, operator, violated path, specific directive, and violation count.</li>
<li>Filter <code>robots.txt</code> request data by crawler, operator, category, and custom time ranges.</li>
</ul>
<h4 id="2025-10-21-track-robots-txt-take-action">Take action</h4>
<p>When you identify non-compliant crawlers, you can:</p>
<ul>
<li>Block the crawler in the <a href="/ai-crawl-control/features/manage-ai-crawlers/">Crawlers tab</a></li>
<li>Create custom <a href="/waf/">WAF rules</a> for path-specific security</li>
<li>Use <a href="/rules/url-forwarding/">Redirect Rules</a> to guide crawlers to appropriate areas of your site</li>
</ul>
<p>To get started, go to <strong>AI Crawl Control</strong> &gt; <strong>Robots.txt</strong> in the Cloudflare dashboard. Learn more in the <a href="/ai-crawl-control/features/track-robots-txt/">Track robots.txt documentation</a>.</p>


<h2 id="enhanced-ai-crawl-control-metrics-with-new-drilldowns-and-filters"><a href="/changelog/post/2025-10-14-enhanced-metrics-drilldowns/">Enhanced AI Crawl Control metrics with new drilldowns and filters</a></h2>
<p><em>2025-10-14</em></p>
<p>AI Crawl Control now provides enhanced metrics and CSV data exports to help you better understand AI crawler activity across your sites.</p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-what-s-new">What's new</h4>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-track-crawler-requests-over-time">Track crawler requests over time</h4>
<p>Visualize crawler activity patterns over time, and group data by different dimensions:</p>
<ul>
<li><strong>By Crawler</strong> — Track activity from individual AI crawlers (GPTBot, ClaudeBot, Bytespider)</li>
<li><strong>By Category</strong> — Analyze crawler purpose or type</li>
<li><strong>By Operator</strong> — Discover which companies (OpenAI, Anthropic, ByteDance) are crawling your site</li>
<li><strong>By Host</strong> — Break down activity across multiple subdomains</li>
<li><strong>By Status Code</strong> — Monitor HTTP response codes to crawlers (200s, 300s, 400s, 500s)</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-requests-over-time.png" alt="AI Crawl Control requests over time chart with grouping tabs" title="Interactive chart showing crawler requests over time with filterable dimensions" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-analyze-referrer-data-paid-plans">Analyze referrer data (Paid plans)</h4>
<p>Identify traffic sources with referrer analytics:</p>
<ul>
<li>View top referrers driving traffic to your site</li>
<li>Understand discovery patterns and content popularity from AI operators</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-top-referrers.png" alt="AI Crawl Control top referrers breakdown" title="Bar chart showing top referrers and their respective traffic volumes" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-export-data">Export data</h4>
<p>Download your filtered view as a CSV:</p>
<ul>
<li>Includes all applied filters and groupings</li>
<li>Useful for custom reporting and deeper analysis</li>
</ul>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong>.</li>
<li>Use the grouping tabs to explore different views of your data.</li>
<li>Apply filters to focus on specific crawlers, time ranges, or response codes.</li>
<li>Select <strong>Download CSV</strong> to export your filtered data for further analysis.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control">AI Crawl Control</a>.</p>


<h2 id="new-deepgram-flux-model-available-on-workers-ai"><a href="/changelog/post/2025-10-02-deepgram-flux/">New Deepgram Flux model available on Workers AI</a></h2>
<p><em>2025-10-02</em></p>
<p>Deepgram's newest Flux model <a href="/workers-ai/models/flux/"><code>@cf/deepgram/flux</code></a> is now available on Workers AI, hosted directly on Cloudflare's infrastructure. We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out <a href="https://deepgram.com/flux">Deepgram's blog</a> for more details on the release.</p>
<p>The Flux model can be used in conjunction with Deepgram's speech-to-text model <a href="/workers-ai/models/nova-3/"><code>@cf/deepgram/nova-3</code></a> and text-to-speech model <a href="/workers-ai/models/aura-1/"><code>@cf/deepgram/aura-1</code></a> to build end-to-end voice agents. Having Deepgram on Workers AI takes advantage of our edge GPU infrastructure, for ultra low latency voice AI applications.</p>
<h4 id="2025-10-02-deepgram-flux-promotional-pricing">Promotional Pricing</h4>
For the month of October 2025, Deepgram's Flux model will be free to use on Workers AI. Official pricing will be announced soon and charged after the promotional pricing period ends on October 31, 2025. Check out the [model page](/workers-ai/models/flux/) for pricing details in the future.
<h4 id="2025-10-02-deepgram-flux-example-usage">Example Usage</h4>
<p>The new Flux model is WebSocket only as it requires live bi-directional streaming in order to recognize speech activity.</p>
<ol>
<li>Create a worker that establishes a websocket connection with <code>@cf/deepgram/flux</code></li>
</ol>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;    const resp = await env.AI.run(&quot;@cf/deepgram/flux&quot;, {&#10;      encoding: &quot;linear16&quot;,&#10;      sample_rate: &quot;16000&quot;&#10;    }, {&#10;      websocket: true&#10;    });&#10;    return resp;&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<ol start="2">
<li>Deploy your worker</li>
</ol>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<ol start="3">
<li>Write a client script to connect to your worker and start sending random audio bytes to it</li>
</ol>
<pre tabindex="0"><code class="language-js">const ws = new WebSocket(&#x27;wss://&lt;your-worker-url.com&gt;&#x27;);&#10;&#10;ws.onopen = () =&gt; {&#10;  console.log(&#x27;Connected to WebSocket&#x27;);&#10;&#10;  // Generate and send random audio bytes&#10;  // You can replace this part with a function&#10;  // that reads from your mic or other audio source&#10;  const audioData = generateRandomAudio();&#10;  ws.send(audioData);&#10;  console.log(&#x27;Audio data sent&#x27;);&#10;};&#10;&#10;ws.onmessage = (event) =&gt; {&#10;  // Transcription will be received here&#10;  // Add your custom logic to parse the data&#10;  console.log(&#x27;Received:&#x27;, event.data);&#10;};&#10;&#10;ws.onerror = (error) =&gt; {&#10;  console.error(&#x27;WebSocket error:&#x27;, error);&#10;};&#10;&#10;ws.onclose = () =&gt; {&#10;  console.log(&#x27;WebSocket closed&#x27;);&#10;};&#10;&#10;// Generate random audio data (1 second of noise at 44.1kHz, mono)&#10;function generateRandomAudio() {&#10;  const sampleRate = 44100;&#10;  const duration = 1;&#10;  const numSamples = sampleRate * duration;&#10;  const buffer = new ArrayBuffer(numSamples * 2);&#10;  const view = new Int16Array(buffer);&#10;&#10;  for (let i = 0; i &lt; numSamples; i++) {&#10;    view[i] = Math.floor(Math.random() * 65536 - 32768);&#10;  }&#10;&#10;  return buffer;&#10;}&#10;</code></pre>


<h2 id="browser-rendering-playwright-ga-stagehand-support-beta-and-higher-limits"><a href="/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/">Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits</a></h2>
<p><em>2025-09-25T12:00:00+00:00</em></p>
<p>We’re shipping three updates to Browser Rendering:</p>
<ul>
<li>Playwright support is now Generally Available and synced with <a href="https://playwright.dev/docs/release-notes#version-155">Playwright v1.55</a>, giving you a stable foundation for critical automation and AI-agent workflows.</li>
<li>We’re also adding <a href="/browser-run/stagehand/">Stagehand support (Beta)</a> so you can combine code with natural language instructions to build more resilient automations.</li>
<li>Finally, we’ve tripled <a href="/browser-run/limits/#workers-paid">limits</a> for paid plans across both the <a href="/browser-run/quick-actions/">REST API</a> and <a href="/browser-run/#integration-methods">Browser Sessions</a> to help you scale.</li>
</ul>
<p>To get started with Stagehand, refer to the <a href="/browser-run/stagehand/">Stagehand</a> example that uses Stagehand and <a href="/workers-ai/">Workers AI</a> to search for a movie on this <a href="https://demo.playwright.dev/movies">example movie directory</a>, extract its details using natural language (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.</p>
<pre tabindex="0"><code class="language-ts">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;	llmClient: new WorkersAIClient(env.AI),&#10;	verbose: 1,&#10;});&#10;&#10;await stagehand.init();&#10;const page = stagehand.page;&#10;&#10;await page.goto(&quot;https://demo.playwright.dev/movies&quot;);&#10;&#10;// if search is a multi-step action, stagehand will return an array of actions it needs to act on&#10;const actions = await page.observe(&#x27;Search for &quot;Furiosa&quot;&#x27;);&#10;for (const action of actions) await page.act(action);&#10;&#10;await page.act(&quot;Click the search result&quot;);&#10;&#10;// normal playwright functions work as expected&#10;await page.waitForSelector(&quot;.info-wrapper .cast&quot;);&#10;&#10;let movieInfo = await page.extract({&#10;	instruction: &quot;Extract movie information&quot;,&#10;	schema: z.object({&#10;		title: z.string(),&#10;		year: z.number(),&#10;		rating: z.number(),&#10;		genres: z.array(z.string()),&#10;		duration: z.number().describe(&quot;Duration in minutes&quot;),&#10;	}),&#10;});&#10;&#10;await stagehand.close();&#10;</code></pre>
<p><img src="/images/browser-run/speedystagehand.gif" alt="Stagehand video" /></p>


<h2 id="ai-search-formerly-autorag-now-with-more-models-to-choose-from"><a href="/changelog/post/2025-09-25-ai-search-more-models/">AI Search (formerly AutoRAG) now with More Models To Choose From</a></h2>
<p><em>2025-09-25</em></p>
<p>AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.</p>
<p>With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.</p>
<p>To use AI Search with other <a href="/ai-search/configuration/models/">model providers</a>:</p>
<ol>
<li><strong>Add provider keys to AI Gateway</strong>
<ol>
<li>Go to AI &gt; AI Gateway in the dashboard.</li>
<li>Select or create an AI gateway.</li>
<li>In Provider Keys, choose your provider, click Add, and enter the key.</li>
</ol>
</li>
<li><strong>Connect a gateway to AI Search</strong>: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.</li>
<li><strong>Select models</strong>: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.</li>
</ol>
<p>Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a <code>/ai-search</code> request:</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;  async fetch(request, env) {&#10;    &#10;    // Query your AI Search instance with a natural language question to an OpenAI model&#10;    const result = await env.AI.autorag(&quot;my-ai-search&quot;).aiSearch({&#10;      query: &quot;What&#x27;s new for Cloudflare Birthday Week?&quot;,&#10;      model: &quot;openai/gpt-5&quot;&#10;    });&#10;&#10;    // Return only the generated answer as plain text&#10;    return new Response(result.response, {&#10;      headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the <a href="/changelog/product/ai-search/">AI Search Changelog</a> and <a href="https://discord.cloudflare.com/">Discord</a> for more updates!</p>


<h2 id="new-metrics-view-in-autorag"><a href="/changelog/post/2025-09-19-autorag-metrics/">New Metrics View in AutoRAG</a></h2>
<p><em>2025-09-19</em></p>
<p><a href="/ai-search/">AutoRAG</a> now includes a <strong>Metrics</strong> tab that shows how your data is indexed and searched. Get a clear view of the health of your indexing pipeline, compare usage between <code>ai-search</code> and <code>search</code>, and see which files are retrieved most often.</p>
<p><img src="/assets/upstream/images/ai-search/metrics.png" alt="Metrics" /></p>
<p>You can find these metrics within each AutoRAG instance:</p>
<ul>
<li>Indexing: Track how files are ingested and see status changes over time.</li>
<li>Search breakdown: Compare usage between <code>ai-search</code> and <code>search</code> endpoints.</li>
<li>Top file retrievals: Identify which files are most frequently retrieved in a given period.</li>
</ul>
<p>Try it today in <a href="/ai-search/get-started/">AutoRAG</a>.</p>


<h2 id="agents-sdk-v0-1-0-and-workers-ai-provider-v2-0-0-with-ai-sdk-v5-support"><a href="/changelog/post/2025-09-03-agents-sdk-beta-v5/">Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</a></h2>
<p><em>2025-09-10</em></p>
<p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v5</a> and introducing automatic message migration that handles all legacy formats transparently.</p>
<p>This release includes improved streaming and tool support, tool confirmation detection (for &quot;human in the loop&quot; systems), enhanced React hooks with automatic tool resolution, improved error handling for streaming responses, and seamless migration utilities that work behind the scenes.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable message handling across SDK versions — all while maintaining backward compatibility.</p>
<p>Additionally, we've updated workers-ai-provider v2.0.0, the official provider for Cloudflare Workers AI models, to be compatible with AI SDK v5.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v5 capabilities.</p>
<pre tabindex="0"><code class="language-ts">// Basic chat setup&#10;const { messages, sendMessage, addToolResult } = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	tools,&#10;});&#10;&#10;// With custom tool confirmation&#10;const chat = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	toolsRequiringConfirmation: [&quot;dangerousOperation&quot;],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-tool-resolution">Automatic Tool Resolution</h4>
<p>Tools are automatically categorized based on their configuration:</p>
<pre tabindex="0"><code class="language-ts">const tools = {&#10;	// Auto-executes (has execute function)&#10;	getLocalTime: {&#10;		description: &quot;Get current local time&quot;,&#10;		inputSchema: z.object({}),&#10;		execute: async () =&gt; new Date().toLocaleString(),&#10;	},&#10;&#10;	// Requires confirmation (no execute function)&#10;	deleteFile: {&#10;		description: &quot;Delete a file from the system&quot;,&#10;		inputSchema: z.object({&#10;			filename: z.string(),&#10;		}),&#10;	},&#10;&#10;	// Server-executed (no client confirmation)&#10;	analyzeData: {&#10;		description: &quot;Analyze dataset on server&quot;,&#10;		inputSchema: z.object({ data: z.array(z.number()) }),&#10;		serverExecuted: true,&#10;	},&#10;} satisfies Record&lt;string, AITool&gt;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-message-handling">Message Handling</h4>
<p>Send messages using the new v5 format with parts array:</p>
<pre tabindex="0"><code class="language-ts">// Text message&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [{ type: &quot;text&quot;, text: &quot;Hello, assistant!&quot; }],&#10;});&#10;&#10;// Multi-part message with file&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{ type: &quot;image&quot;, image: imageData },&#10;	],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>Simplified logic for detecting pending tool confirmations:</p>
<pre tabindex="0"><code class="language-ts">const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolResult({&#10;		toolCallId: part.toolCallId,&#10;		tool: getToolName(part),&#10;		output: &quot;User approved the action&quot;,&#10;	});&#10;}&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-message-migration">Automatic Message Migration</h4>
<p>Seamlessly handle legacy message formats without code changes.</p>
<pre tabindex="0"><code class="language-ts">// All these formats are automatically converted:&#10;&#10;// Legacy v4 string content&#10;const legacyMessage = {&#10;	role: &quot;user&quot;,&#10;	content: &quot;Hello world&quot;,&#10;};&#10;&#10;// Legacy v4 with tool calls&#10;const legacyWithTools = {&#10;	role: &quot;assistant&quot;,&#10;	content: &quot;&quot;,&#10;	toolInvocations: [&#10;		{&#10;			toolCallId: &quot;123&quot;,&#10;			toolName: &quot;weather&quot;,&#10;			args: { city: &quot;SF&quot; },&#10;			state: &quot;result&quot;,&#10;			result: &quot;Sunny, 72°F&quot;,&#10;		},&#10;	],&#10;};&#10;&#10;// Automatically becomes v5 format:&#10;// {&#10;//   role: &quot;assistant&quot;,&#10;//   parts: [{&#10;//     type: &quot;tool-call&quot;,&#10;//     toolCallId: &quot;123&quot;,&#10;//     toolName: &quot;weather&quot;,&#10;//     args: { city: &quot;SF&quot; },&#10;//     state: &quot;result&quot;,&#10;//     result: &quot;Sunny, 72°F&quot;&#10;//   }]&#10;// }&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-definition-updates">Tool Definition Updates</h4>
<p>Migrate tool definitions to use the new <code>inputSchema</code> property.</p>
<pre tabindex="0"><code class="language-ts">// Before (AI SDK v4)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		parameters: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;&#10;// After (AI SDK v5)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		inputSchema: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-cloudflare-workers-ai-integration">Cloudflare Workers AI Integration</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v2.0.0.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre tabindex="0"><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v2.0.0 - same API, enhanced v5 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v5 file handling with automatic conversion:</p>
<pre tabindex="0"><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre tabindex="0"><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages,&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-import-updates">Import Updates</h4>
<p>Update your imports to use the new v5 types:</p>
<pre tabindex="0"><code class="language-ts">// Before (AI SDK v4)&#10;import type { Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;ai/react&quot;;&#10;&#10;// After (AI SDK v5)&#10;import type { UIMessage } from &quot;ai&quot;;&#10;// or alias for compatibility&#10;import type { UIMessage as Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;@ai-sdk/react&quot;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v5.md">Migration Guide</a> - Comprehensive migration documentation</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0">AI SDK v5 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://github.com/cloudflare/agents-starter/pull/105">An Example PR showing the migration from AI SDK v4 to v5</a></li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-09-03-agents-sdk-beta-v5-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade process?</li>
<li><strong>Tool confirmation workflow</strong> - Does the new automatic detection work as expected?</li>
<li><strong>Message format handling</strong> - Any edge cases with legacy message conversion?</li>
</ul>


<h2 id="introducing-embeddinggemma-from-google-on-workers-ai"><a href="/changelog/post/2025-09-05-embeddinggemma/">Introducing EmbeddingGemma from Google on Workers AI</a></h2>
<p><em>2025-09-05</em></p>
<p>We're excited to be a launch partner alongside <a href="https://developers.googleblog.com/en/introducing-embeddinggemma/">Google</a> to bring their newest embedding model, <strong>EmbeddingGemma</strong>, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.</p>
<p><a href="/workers-ai/models/embeddinggemma-300m/"><code>@cf/google/embeddinggemma-300m</code></a> is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.</p>
<p><strong>Using EmbeddingGemma in AI Search:</strong>
Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.</p>
<p>To use EmbeddingGemma for your AI Search projects:</p>
<ol>
<li>Go to <strong>Create</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/ai/ai-search">AI Search dashboard</a></li>
<li>Follow the setup flow for your new RAG instance</li>
<li>In the <strong>Generate Index</strong> step, open up <strong>More embedding models</strong> and select <code>@cf/google/embeddinggemma-300m</code> as your embedding model</li>
<li>Complete the setup to create an AI Search</li>
</ol>
<p>Try it out and let us know what you think!</p>


<h2 id="enhanced-crawler-insights-and-custom-402-responses"><a href="/changelog/post/2025-08-27-ai-crawl-control-launch/">Enhanced crawler insights and custom 402 responses</a></h2>
<p><em>2025-08-27</em></p>
<p>We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.</p>
<p><strong>Enhanced Crawlers tab:</strong></p>
<ul>
<li>View total allowed and blocked requests for each AI crawler</li>
<li>Trend charts show crawler activity over your selected time range per crawler</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-table.png" alt="Updated AI Crawl Control table showing request counts and trend charts" /></p>
<p><strong>Custom block responses (paid plans):</strong>
You can now return HTTP 402 &quot;Payment Required&quot; responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.</p>
<p>For users on paid plans, when blocking AI crawlers you can configure:</p>
<ul>
<li><strong>Response code:</strong> Choose between 403 Forbidden or 402 Payment Required</li>
<li><strong>Response body:</strong> Add a custom message with your licensing contact information</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-block-response.png" alt="AI Crawl Control block response configuration interface" /></p>
<p>Example 402 response:</p>
<pre tabindex="0"><code class="language-http">HTTP 402 Payment Required&#10;Date: Mon, 24 Aug 2025 12:56:49 GMT&#10;Content-type: application/json&#10;Server: cloudflare&#10;Cf-Ray: 967e8da599d0c3fa-EWR&#10;Cf-Team: 2902f6db750000c3fa1e2ef400000001&#10;&#10;{&#10;  &quot;message&quot;: &quot;Please contact the site owner for access.&quot;&#10;}&#10;</code></pre>


<h2 id="deepgram-and-leonardo-partner-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-27-partner-models/">Deepgram and Leonardo partner models now available on Workers AI</a></h2>
<p><em>2025-08-27</em></p>
<p>New state-of-the-art models have landed on Workers AI! This time, we're introducing new <strong>partner models</strong> trained by our friends at <a href="https://deepgram.com">Deepgram</a> and <a href="https://leonardo.ai">Leonardo</a>, hosted on Workers AI infrastructure.</p>
<p>As well, we're introuding a new turn detection model that enables you to detect when someone is done speaking — useful for building voice agents!</p>
<p>Read the <a href="https://blog.cloudflare.com/workers-ai-partner-models">blog</a> for more details and check out some of the new models on our platform:</p>
<ul>
<li><a href="/workers-ai/models/aura-1"><code>@cf/deepgram/aura-1</code></a> is a text-to-speech model that allows you to input text and have it come to life in a customizable voice</li>
<li><a href="/workers-ai/models/nova-3"><code>@cf/deepgram/nova-3</code></a> is speech-to-text model that transcribes multilingual audio at a blazingly fast speed</li>
<li><a href="/workers-ai/models/smart-turn-v2"><code>@cf/pipecat-ai/smart-turn-v2</code></a> helps you detect when someone is done speaking</li>
<li><a href="/workers-ai/models/lucid-origin"><code>@cf/leonardo/lucid-origin</code></a> is a text-to-image model that generates images with sharp graphic design, stunning full-HD renders, or highly specific creative direction</li>
<li><a href="/workers-ai/models/phoenix-1.0"><code>@cf/leonardo/phoenix-1.0</code></a> is a text-to-image model with exceptional prompt adherence and coherent text</li>
</ul>
<p>You can filter out new partner models with the <code>Partner</code> capability on our <a href="/workers-ai/models">Models</a> page.</p>
<p>As well, we're introducing WebSocket support for some of our audio models, which you can filter though the <code>Realtime</code> capability on our <a href="/workers-ai/models">Models</a> page. WebSockets allows you to create a bi-directional connection to our inference server with low latency — perfect for those that are building voice agents.</p>
<p>An example python snippet on how to use WebSockets with our new Aura model:</p>
<pre tabindex="0"><code>import json&#10;import os&#10;import asyncio&#10;import websockets&#10;&#10;uri = f&quot;wss://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/deepgram/aura-1&quot;&#10;&#10;input = [&#10;    &quot;Line one, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line two, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line three, out of three lines that will be provided to the aura model. This is a last line.&quot;,&#10;]&#10;&#10;&#10;async def text_to_speech():&#10;    async with websockets.connect(uri, additional_headers={&quot;Authorization&quot;: os.getenv(&quot;CF_TOKEN&quot;)}) as websocket:&#10;        print(&quot;connection established&quot;)&#10;        for line in input:&#10;            print(f&quot;sending `{line}`&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Speak&quot;, &quot;text&quot;: line}))&#10;&#10;            print(&quot;line was sent, flushing&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Flush&quot;}))&#10;            print(&quot;flushed, recving&quot;)&#10;            resp = await websocket.recv()&#10;            print(f&quot;response received {resp}&quot;)&#10;&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    asyncio.run(text_to_speech())&#10;</code></pre>


<h2 id="list-all-vectors-in-a-vectorize-index-with-the-new-list-vectors-operation"><a href="/changelog/post/2025-08-26-vectorize-list-vectors/">List all vectors in a Vectorize index with the new list-vectors operation</a></h2>
<p><em>2025-08-26</em></p>
<p>You can now list all vector identifiers in a Vectorize index using the new <code>list-vectors</code> operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.</p>
<p>The operation is available via Wrangler CLI and REST API. Refer to the <a href="/vectorize/best-practices/list-vectors/">list-vectors best practices guide</a> for detailed usage guidance.</p>


<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre tabindex="0"><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="agents-sdk-adds-mcp-elicitation-support-http-streamable-support-task-queues-email-integration-and-more"><a href="/changelog/post/2025-08-05-agents-MCP-update/">Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</a></h2>
<p><em>2025-08-05</em></p>
<p>The latest releases of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:</p>
<h4 id="2025-08-05-agents-MCP-update-mcp-elicitation-support">MCP elicitation support</h4>
<p>MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.</p>
<pre tabindex="0"><code class="language-ts">// Request user confirmation via elicitation&#10;const confirmation = await this.elicitInput({&#10;	message: `Are you sure you want to increment the counter by ${amount}?`,&#10;	requestedSchema: {&#10;		type: &quot;object&quot;,&#10;		properties: {&#10;			confirmed: {&#10;				type: &quot;boolean&quot;,&#10;				title: &quot;Confirm increment&quot;,&#10;				description: &quot;Check to confirm the increment&quot;,&#10;			},&#10;		},&#10;		required: [&quot;confirmed&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Check out our <a href="https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo">demo</a> to see elicitation in action.</p>
<h4 id="2025-08-05-agents-MCP-update-http-streamable-transport-for-mcp">HTTP streamable transport for MCP</h4>
<p>MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:</p>
<ul>
<li><strong>Better performance</strong>: More efficient data streaming and reduced overhead</li>
<li><strong>Improved reliability</strong>: Enhanced connection stability and error recover- <strong>Automatic fallback</strong>: If streamable transport is not available, it gracefully falls back to SSE</li>
</ul>
<pre tabindex="0"><code class="language-ts">export default MyMCP.serve(&quot;/mcp&quot;, {&#10;	binding: &quot;MyMCP&quot;,&#10;});&#10;</code></pre>
<p>The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.</p>
<h4 id="2025-08-05-agents-MCP-update-enhanced-mcp-connectivity">Enhanced MCP connectivity</h4>
<p>Significant improvements to MCP server connections and transport reliability:</p>
<ul>
<li><strong>Auto transport selection</strong>: Automatically determines the best transport method, falling back from streamable-http to SSE as needed</li>
<li><strong>Improved error handling</strong>: Better connection state management and error reporting for MCP servers</li>
<li><strong>Reliable prop updates</strong>: Centralized agent property updates ensure consistency across different contexts</li>
</ul>
<h4 id="2025-08-05-agents-MCP-update-lightweight-queue-for-fast-task-deferral">Lightweight .queue for fast task deferral</h4>
<p>You can use <code>.queue()</code> to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.</p>
<pre tabindex="0"><code class="language-ts">class MyAgent extends Agent {&#10;	doSomethingExpensive(payload) {&#10;		// a long running process that you want to run in the background&#10;	}&#10;&#10;	queueSomething() {&#10;		await this.queue(&quot;doSomethingExpensive&quot;, somePayload); // this will NOT block further execution, and runs in the background&#10;		await this.queue(&quot;doSomethingExpensive&quot;, someOtherPayload); // the callback will NOT run until the previous callback is complete&#10;		// ... call as many times as you want&#10;	}&#10;}&#10;</code></pre>
<p>Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.</p>
<h4 id="2025-08-05-agents-MCP-update-new-email-adapter">New email adapter</h4>
<p>Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.</p>
<pre tabindex="0"><code class="language-ts">export class EmailAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		const raw = await email.getRaw();&#10;		const parsed = await PostalMime.parse(raw);&#10;&#10;		// create a response based on the email contents&#10;		// and then send a reply&#10;&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;Email Agent&quot;,&#10;			body: `Thanks for your email! You&#x27;ve sent us &quot;${parsed.subject}&quot;. We&#x27;ll process it shortly.`,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>You route incoming mail like this:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async email(email, env) {&#10;		await routeAgentEmail(email, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;EmailAgent&quot;),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can find a full example <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">here</a>.</p>
<h4 id="2025-08-05-agents-MCP-update-automatic-context-wrapping-for-custom-methods">Automatic context wrapping for custom methods</h4>
<p>Custom methods are now automatically wrapped with the agent's context, so calling <code>getCurrentAgent()</code> should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.</p>
<pre tabindex="0"><code class="language-ts">export class MyAgent extends Agent {&#10;	async suggestReply(message) {&#10;		// getCurrentAgent() now correctly works, even when called inside an RPC method&#10;		const { agent } = getCurrentAgent()!;&#10;		return generateText({&#10;			prompt: `Suggest a reply to: &quot;${message}&quot; from &quot;${agent.name}&quot;`,&#10;			tools: [replyWithEmoji],&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>Try it out and tell us what you build!</p>


<h2 id="cloudflare-sandbox-sdk-adds-streaming-code-interpreter-git-support-process-control-and-more"><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</a></h2>
<p><em>2025-08-05</em></p>
<p>We’ve shipped a major release for the <a href="https://github.com/cloudflare/sandbox-sdk">@cloudflare/sandbox</a> SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.</p>
<p>This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.</p>
<p>This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-code-interpreter-python-js-ts">Code interpreter (Python, JS, TS)</h4>
<p>Create persistent code contexts with support for rich visual + structured outputs.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-createcodecontext-options">createCodeContext(options)</h4>
<p>Creates a new code execution context with persistent state.</p>
<pre tabindex="0"><code class="language-ts">// Create a Python context&#10;const pythonCtx = await sandbox.createCodeContext({ language: &quot;python&quot; });&#10;&#10;// Create a JavaScript context&#10;const jsCtx = await sandbox.createCodeContext({ language: &quot;javascript&quot; });&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-runcode-code-options">runCode(code, options)</h4>
<p>Executes code with optional streaming callbacks.</p>
<pre tabindex="0"><code class="language-ts">// Simple execution&#10;const execution = await sandbox.runCode(&#x27;print(&quot;Hello World&quot;)&#x27;, {&#10;	context: pythonCtx,&#10;});&#10;&#10;// With streaming callbacks&#10;await sandbox.runCode(&#10;	`&#10;for i in range(5):&#10;    print(f&quot;Step {i}&quot;)&#10;    time.sleep(1)&#10;`,&#10;	{&#10;		context: pythonCtx,&#10;		onStdout: (output) =&gt; console.log(&quot;Real-time:&quot;, output.text),&#10;		onResult: (result) =&gt; console.log(&quot;Result:&quot;, result),&#10;	},&#10;);&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-real-time-streaming-output">Real-time streaming output</h4>
<p>Returns a streaming response for real-time processing.</p>
<pre tabindex="0"><code class="language-ts">const stream = await sandbox.runCodeStream(&#10;	&quot;import time; [print(i) for i in range(10)]&quot;,&#10;);&#10;// Process the stream as needed&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-rich-output-handling">Rich output handling</h4>
<p>Interpreter outputs are auto-formatted and returned in multiple formats:</p>
<ul>
<li>text</li>
<li>html (e.g., Pandas tables)</li>
<li>png, svg (e.g., Matplotlib charts)</li>
<li>json (structured data)</li>
<li>chart (parsed visualizations)</li>
</ul>
<pre tabindex="0"><code class="language-ts">const result = await sandbox.runCode(&#10;	`&#10;import seaborn as sns&#10;import matplotlib.pyplot as plt&#10;&#10;data = sns.load_dataset(&quot;flights&quot;)&#10;pivot = data.pivot(&quot;month&quot;, &quot;year&quot;, &quot;passengers&quot;)&#10;sns.heatmap(pivot, annot=True, fmt=&quot;d&quot;)&#10;plt.title(&quot;Flight Passengers&quot;)&#10;plt.show()&#10;&#10;pivot.to_dict()&#10;`,&#10;	{ context: pythonCtx },&#10;);&#10;&#10;if (result.png) {&#10;	console.log(&quot;Chart output:&quot;, result.png);&#10;}&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-preview-urls-from-exposed-ports">Preview URLs from Exposed Ports</h4>
<p>Start background processes and expose them with live URLs.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const preview = await sandbox.exposePort(8000);&#10;&#10;console.log(&quot;Live preview at:&quot;, preview.url);&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-full-process-lifecycle-control">Full process lifecycle control</h4>
<p>Start, inspect, and terminate long-running background processes.</p>
<pre tabindex="0"><code class="language-ts">const process = await sandbox.startProcess(&quot;node server.js&quot;);&#10;console.log(`Started process ${process.id} with PID ${process.pid}`);&#10;&#10;// Monitor the process&#10;const logStream = await sandbox.streamProcessLogs(process.id);&#10;for await (const log of parseSSEStream&lt;LogEvent&gt;(logStream)) {&#10;	console.log(`Server: ${log.data}`);&#10;}&#10;</code></pre>
<ul>
<li>listProcesses() - List all running processes</li>
<li>getProcess(id) - Get detailed process status</li>
<li>killProcess(id, signal) - Terminate specific processes</li>
<li>killAllProcesses() - Kill all processes</li>
<li>streamProcessLogs(id, options) - Stream logs from running processes</li>
<li>getProcessLogs(id) - Get accumulated process output</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-git-integration">Git integration</h4>
<p>Clone Git repositories directly into the sandbox.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.gitCheckout(&quot;https://github.com/user/repo&quot;, {&#10;	branch: &quot;main&quot;,&#10;	targetDir: &quot;my-project&quot;,&#10;});&#10;</code></pre>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>


<h2 id="openai-open-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-05-openai-open-models/">OpenAI open models now available on Workers AI</a></h2>
<p><em>2025-08-05</em></p>
<p>We're thrilled to be a Day 0 partner with <a href="http://openai.com/index/introducing-gpt-oss">OpenAI</a> to bring their <a href="https://openai.com/index/gpt-oss-model-card/">latest open models</a> to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).</p>
<p>Get started with the new models at <code>@cf/openai/gpt-oss-120b</code> and <code>@cf/openai/gpt-oss-20b</code>.
Check out the <a href="https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai">blog</a> for more details about the new models, and the <a href="/workers-ai/models/gpt-oss-120b"><code>gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b"><code>gpt-oss-20b</code></a> model pages for more information about pricing and context windows.</p>
<h4 id="2025-08-05-openai-open-models-responses-api">Responses API</h4>
If you call the model through:
- Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
- REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
- REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
- REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`
<pre tabindex="0"><code>curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/ai/v1/responses \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_KEY&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;@cf/openai/gpt-oss-120b&quot;,&#10;    &quot;reasoning&quot;: {&quot;effort&quot;: &quot;medium&quot;},&#10;    &quot;input&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What are the benefits of open-source models?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;&#10;</code></pre>
<h4 id="2025-08-05-openai-open-models-code-interpreter">Code Interpreter</h4>
The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK](https://github.com/cloudflare/sandbox-sdk) and [Containers](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.
<h4 id="2025-08-05-openai-open-models-web-search-coming-soon">Web Search (coming soon)</h4>
We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.


<h2 id="introducing-pricing-for-the-browser-rendering-api-0-09-per-browser-hour"><a href="/changelog/post/2025-07-28-br-pricing/">Introducing pricing for the Browser Rendering API — $0.09 per browser hour</a></h2>
<p><em>2025-07-28T12:00:00+00:00</em></p>
<p>We’ve launched pricing for <a href="/browser-run/">Browser Rendering</a>, including a free tier and a pay-as-you-go model that scales with your needs. Starting <strong>August 20, 2025</strong>, Cloudflare will begin billing for Browser Rendering.</p>
<p>There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:</p>
<ul>
<li><a href="/browser-run/quick-actions/"><strong>REST API</strong></a>: Charged for <strong>Duration</strong> only ($/browser hour)</li>
<li><a href="/browser-run/#integration-methods"><strong>Browser Sessions</strong></a>: Charged for both <strong>Duration</strong> and <strong>Concurrency</strong> ($/browser hour and # of concurrent browsers)</li>
</ul>
<p>Included usage and pricing by plan</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Included duration</th>
<th>Included concurrency</th>
<th>Price (beyond included)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>10 minutes per day</td>
<td>3 concurrent browsers</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 hours per month</td>
<td>10 concurrent browsers (averaged monthly)</td>
<td><strong>1. REST API</strong>: $0.09 per additional browser hour <br /><strong>2. Workers Bindings</strong>: $0.09 per additional browser hour <br /> $2.00 per additional concurrent browser</td>
</tr>
</tbody>
</table>
<p>What you need to know:</p>
<ul>
<li><strong>Workers Free Plan:</strong> 10 minutes of browser usage per day with 3 concurrent browsers at no charge.</li>
<li><strong>Workers Paid Plan:</strong> 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.</li>
</ul>
<p>You can monitor usage via the <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">Cloudflare dashboard</a>. Go to <strong>Compute</strong> &gt; <strong>Browser Run</strong>.</p>
<p><img src="/assets/upstream/images/browser-run/dashboard.png" alt="Browser Rendering dashboard" /></p>
<p>If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's <a href="/browser-run/pricing/">included usage</a>. To estimate costs, take a look at these <a href="/browser-run/pricing/#examples-of-workers-paid-pricing">example pricing scenarios</a>.</p>


<h2 id="browser-rendering-now-supports-local-development"><a href="/changelog/post/2025-07-22-br-local-dev/">Browser Rendering now supports local development</a></h2>
<p><em>2025-07-22T11:00:00+00:00</em></p>
<p>You can now run your Browser Rendering locally using <code>npx wrangler dev</code>, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.</p>
<p>Get started with this <a href="/browser-run/how-to/deploy-worker/">example guide</a> that shows how to use Cloudflare's <a href="/browser-run/puppeteer/">fork of Puppeteer</a> (you can also use <a href="/browser-run/playwright/">Playwright</a>) to take screenshots of webpages and store the results in <a href="/kv/">Workers KV</a>.</p>


<h2 id="faster-indexing-and-new-jobs-view-in-autorag"><a href="/changelog/post/2025-07-08-autorag-jobs-view/">Faster indexing and new Jobs view in AutoRAG</a></h2>
<p><em>2025-07-08</em></p>
<p>You can now expect <strong>3-5× faster indexing</strong> in AutoRAG, and with it, a brand new <strong>Jobs view</strong> to help you monitor indexing progress.</p>
<p>With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the <a href="/api/resources/ai-search/subresources/rags/">Sync API</a> or by clicking “Sync index” in the dashboard.</p>
<p>With the new jobs observability, you can now:</p>
<ul>
<li>View the status, job ID, source, start time, duration and last sync time for each indexing job</li>
<li>Inspect real-time logs of job events (e.g. <code>Starting indexing data source...</code>)</li>
<li>See a history of past indexing jobs under the Jobs tab of your AutoRAG</li>
</ul>
<p>This makes it easier to understand what’s happening behind the scenes.</p>
<p><strong>Coming soon:</strong> We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.</p>
<p>Try it out today on the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a>.</p>


<h2 id="introducing-pay-per-crawl-private-beta"><a href="/changelog/post/2025-07-01-pay-per-crawl/">Introducing Pay Per Crawl (private beta)</a></h2>
<p><em>2025-07-01</em></p>
<p>We are introducing a new feature of <a href="/ai-crawl-control/">AI Crawl Control</a> — Pay Per Crawl. <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl</a> enables site owners to require payment from AI crawlers every time the crawlers access their content, thereby fostering a fairer Internet by enabling site owners to control and monetize how their content gets used by AI.</p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/pay-per-crawl.png" alt="Pay per crawl" /></p>
<p><strong>For Site Owners:</strong></p>
<ul>
<li>Set pricing and select which crawlers to charge for content access</li>
<li>Manage payments via Stripe</li>
<li>Monitor analytics on successful content deliveries</li>
</ul>
<p><strong>For AI Crawler Owners:</strong></p>
<ul>
<li>Use HTTP headers to request and accept pricing</li>
<li>Receive clear confirmations on charges for accessed content</li>
</ul>
<p>Learn more in the <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl documentation</a>.</p>


<h2 id="ai-crawl-control-refresh"><a href="/changelog/post/2025-07-01-refresh/">AI Crawl Control refresh</a></h2>
<p><em>2025-07-01</em></p>
<p>We redesigned the AI Crawl Control dashboard to provide more intuitive and granular control over AI crawlers.</p>
<ul>
<li>From the new <strong>AI Crawlers</strong> tab: block specific AI crawlers.</li>
<li>From the new <strong>Metrics</strong> tab: view AI Crawl Control metrics.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/manage-ai-crawlers.png" alt="Block AI crawlers" /></p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/analyze-metrics.png" alt="Analyze AI crawler activity" /></p>
<p>To get started, explore:</p>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a>.</li>
</ul>


<h2 id="run-ai-generated-code-on-demand-with-code-sandboxes-new"><a href="/changelog/post/2025-06-24-announcing-sandboxes/">Run AI-generated code on-demand with Code Sandboxes (new)</a></h2>
<p><em>2025-06-25</em></p>
<p>AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing <a href="https://www.npmjs.com/package/@cloudflare/sandbox">Sandboxes</a>, which let your Worker run actual processes in a secure, container-based environment.</p>
<pre tabindex="0"><code class="language-ts">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;		return sandbox.exec(&quot;ls&quot;, [&quot;-la&quot;]);&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-06-24-announcing-sandboxes-methods">Methods</h4>
<ul>
<li><code>exec(command: string, args: string[], options?: { stream?: boolean })</code>:Execute a command in the sandbox.</li>
<li><code>gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })</code>: Checkout a git repository in the sandbox.</li>
<li><code>mkdir(path: string, options: { recursive?: boolean; stream?: boolean })</code>: Create a directory in the sandbox.</li>
<li><code>writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })</code>: Write content to a file in the sandbox.</li>
<li><code>readFile(path: string, options: { encoding?: string; stream?: boolean })</code>: Read content from a file in the sandbox.</li>
<li><code>deleteFile(path: string, options?: { stream?: boolean })</code>: Delete a file from the sandbox.</li>
<li><code>renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })</code>: Rename a file in the sandbox.</li>
<li><code>moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })</code>: Move a file from one location to another in the sandbox.</li>
<li><code>ping()</code>: Ping the sandbox.</li>
</ul>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
<p>You can try it today from your Worker, with just a few lines of code. Let us know what you build.</p>


<h2 id="view-custom-metadata-in-responses-and-guide-ai-search-with-context-in-autorag"><a href="/changelog/post/2025-06-19-autorag-custom-metadata-and-context/">View custom metadata in responses and guide AI-search with context in AutoRAG</a></h2>
<p><em>2025-06-19</em></p>
<p>In <a href="/ai-search/">AutoRAG</a>, you can now view your object's custom metadata in the response from <a href="/ai-search/api/search/workers-binding/"><code>/search</code></a> and <a href="/ai-search/api/search/workers-binding/"><code>/ai-search</code></a>, and optionally add a <code>context</code> field in the custom metadata of an object to provide additional guidance for AI-generated answers.</p>
<p>You can add <a href="/r2/api/workers/workers-api-reference/#r2putoptions">custom metadata</a> to an object when uploading it to your R2 bucket.</p>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-object-s-custom-metadata-in-search-responses">Object's custom metadata in search responses</h4>
<p>When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside <code>attributes</code> then <code>file</code> , and can be used for downstream processing.</p>
<p>For example, the <code>attributes</code> section of your search response may look like:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;attributes&quot;: {&#10;		&quot;timestamp&quot;: 1750001460000,&#10;		&quot;folder&quot;: &quot;docs/&quot;,&#10;		&quot;filename&quot;: &quot;launch-checklist.md&quot;,&#10;		&quot;file&quot;: {&#10;			&quot;url&quot;: &quot;https://wiki.company.com/docs/launch-checklist&quot;,&#10;			&quot;context&quot;: &quot;A checklist for internal launch readiness, including legal, engineering, and marketing steps.&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-add-a-context-field-to-guide-llm-answers">Add a <code>context</code> field to guide LLM answers</h4>
<p>When you include a custom metadata field named <code>context</code>, AutoRAG attaches that value to each chunk of the file. When you run an <code>/ai-search</code> query, this <code>context</code> is passed to the LLM and can be used as additional input when generating an answer.</p>
<p>We recommend using the <code>context</code> field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the <code>context</code> string.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;context&quot;: &quot;summary: &#x27;Checklist for internal product launch readiness, including legal, engineering, and marketing steps.&#x27;; url: &#x27;https://wiki.company.com/docs/launch-checklist&#x27;&quot;&#10;}&#10;</code></pre>
<p>This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="filter-your-autorag-search-by-file-name"><a href="/changelog/post/2025-06-19-autorag-filename-filter/">Filter your AutoRAG search by file name</a></h2>
<p><em>2025-06-19</em></p>
<p>In <a href="/ai-search/">AutoRAG</a>, you can now <a href="/ai-search/configuration/indexing/metadata/">filter</a> by an object's file name using the <code>filename</code> attribute, giving you more control over which files are searched for a given query.</p>
<p>This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.</p>
<p>For example, your search query may look like:</p>
<pre tabindex="0"><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;what is the project deadline?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;filename&quot;,&#10;		value: &quot;project-alpha-roadmap.md&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="ai-gateway-adds-openai-compatible-endpoint"><a href="/changelog/post/2025-06-03-aig-openai-compatible-endpoint/">AI Gateway adds OpenAI compatible endpoint</a></h2>
<p><em>2025-06-03</em></p>
<p>Users can now use an <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.</p>
<p>To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the <code>model</code> and <code>apiKey</code> parameters.</p>
<pre tabindex="0"><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;const client = new OpenAI({&#10;	apiKey: &quot;YOUR_PROVIDER_API_KEY&quot;, // Provider API key&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat&quot;,&#10;});&#10;&#10;const response = await client.chat.completions.create({&#10;	model: &quot;google-ai-studio/gemini-2.0-flash&quot;,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;&#10;console.log(response.choices[0].message.content);&#10;</code></pre>
<p>Additionally, the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> can be combined with our <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!</p>
<p>Learn more in the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatibility</a> documentation.</p>


<h2 id="playwright-mcp-server-is-now-compatible-with-browser-rendering"><a href="/changelog/post/2025-05-28-playwright-mcp/">Playwright MCP server is now compatible with Browser Rendering</a></h2>
<p><em>2025-05-28</em></p>
<p>We're excited to share that you can now use the <a href="https://github.com/cloudflare/playwright-mcp">Playwright MCP</a> server with Browser Rendering.</p>
<p>Once you <a href="/browser-run/playwright/playwright-mcp/#deploying">deploy the server</a>, you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.</p>
<p><img src="/assets/upstream/images/browser-run/playground-ai-screenshot.png" alt="Access Analytics" /></p>
<p>Playwright MCP is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright-mcp"><code>@cloudflare/playwright-mcp</code></a>. To install it, type:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Deploying the server is then as easy as:</p>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createMcpAgent } from &quot;@cloudflare/playwright-mcp&quot;;&#10;&#10;export const PlaywrightMCP = createMcpAgent(env.BROWSER);&#10;export default PlaywrightMCP.mount(&quot;/sse&quot;);&#10;</code></pre>
<p>Check out the full code at <a href="https://github.com/cloudflare/playwright-mcp">GitHub</a>.</p>
<p>Learn more about Playwright MCP in our <a href="/browser-run/playwright/playwright-mcp/">documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/ai/5/">Previous</a><span>Page 6 of 7</span><a class="pagination-next" rel="next" href="/changelog/product-group/ai/7/">Next</a></nav>
