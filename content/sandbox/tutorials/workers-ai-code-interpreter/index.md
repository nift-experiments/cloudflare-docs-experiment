---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/
  description: Build a code interpreter using Workers AI GPT-OSS model with the official workers-ai-provider package.
  full_title: Code interpreter with Workers AI · Cloudflare Sandbox SDK docs
  head_html: <title>Code interpreter with Workers AI · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a code interpreter using Workers AI GPT-OSS model with the official workers-ai-provider package."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/index.md"><meta property="og:title" content="Code interpreter with Workers AI · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a code interpreter using Workers AI GPT-OSS model with the official workers-ai-provider package."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Sandbox SDK,Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/#page","headline":"Code interpreter with Workers AI \u00b7 Cloudflare Sandbox SDK docs","description":"Build a code interpreter using Workers AI GPT-OSS model with the official workers-ai-provider package.","url":"https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/tutorials/workers-ai-code-interpreter/
  schema: 1
---
<p>Build a powerful code interpreter that gives the <a href="/workers-ai/models/gpt-oss-120b/">gpt-oss model</a> on Workers AI the ability to execute Python code using the Cloudflare Sandbox SDK.</p>
<p><strong>Time to complete:</strong> 15 minutes</p>
<h2 id="what-you-ll-build">What you'll build</h2>
<p>A Cloudflare Worker that accepts natural language prompts, uses GPT-OSS to decide when Python code execution is needed, runs the code in isolated sandboxes, and returns results with AI-powered explanations.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13303.md")
</div></details>
<p>You'll also need:</p>
<ul>
<li><a href="https://www.docker.com/">Docker</a> running locally</li>
</ul>
<h2 id="1-create-your-project"><ol>
<li>Create your project</li>
</ol></h2>
<p>Create a new Sandbox SDK project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- workers-ai-interpreter --template=cloudflare/sandbox-sdk/examples/code-interpreter</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- workers-ai-interpreter --template=cloudflare/sandbox-sdk/examples/code-interpreter" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare workers-ai-interpreter --template=cloudflare/sandbox-sdk/examples/code-interpreter</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare workers-ai-interpreter --template=cloudflare/sandbox-sdk/examples/code-interpreter" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest workers-ai-interpreter --template=cloudflare/sandbox-sdk/examples/code-interpreter</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest workers-ai-interpreter --template=cloudflare/sandbox-sdk/examples/code-interpreter" aria-label="Copy to clipboard">Copy</button></div></div>
<pre tabindex="0"><code class="language-sh">cd workers-ai-interpreter&#10;</code></pre>
<h2 id="2-review-the-implementation"><ol start="2">
<li>Review the implementation</li>
</ol></h2>
<p>The template includes a complete implementation using the latest best practices. Let's examine the key components:</p>
<pre tabindex="0"><code class="language-typescript">// src/index.ts&#10;import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;import { generateText, stepCountIs, tool } from &quot;ai&quot;;&#10;import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;const MODEL = &quot;@cf/openai/gpt-oss-120b&quot; as const;&#10;&#10;async function handleAIRequest(input: string, env: Env): Promise&lt;string&gt; {&#10;	const workersai = createWorkersAI({ binding: env.AI });&#10;&#10;	const result = await generateText({&#10;		model: workersai(MODEL),&#10;		messages: [{ role: &quot;user&quot;, content: input }],&#10;		tools: {&#10;			execute_python: tool({&#10;				description: &quot;Execute Python code and return the output&quot;,&#10;				inputSchema: z.object({&#10;					code: z.string().describe(&quot;The Python code to execute&quot;),&#10;				}),&#10;				execute: async ({ code }) =&gt; {&#10;					return executePythonCode(env, code);&#10;				},&#10;			}),&#10;		},&#10;		stopWhen: stepCountIs(5),&#10;	});&#10;&#10;	return result.text || &quot;No response generated&quot;;&#10;}&#10;</code></pre>
<p><strong>Key improvements over direct REST API calls:</strong></p>
<ul>
<li><strong>Official packages</strong>: Uses <code>workers-ai-provider</code> instead of manual API calls</li>
<li><strong>Vercel AI SDK</strong>: Leverages <code>generateText()</code> and <code>tool()</code> for clean function calling</li>
<li><strong>No API keys</strong>: Uses native AI binding instead of environment variables</li>
<li><strong>Type safety</strong>: Full TypeScript support with proper typing</li>
</ul>
<h2 id="3-check-your-configuration"><ol start="3">
<li>Check your configuration</li>
</ol></h2>
<p>The template includes the proper Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13304.md")
</div>
<p><strong>Configuration highlights:</strong></p>
<ul>
<li><strong>AI binding</strong>: Enables direct access to Workers AI models</li>
<li><strong>Container setup</strong>: Configures sandbox container with Dockerfile</li>
<li><strong>Durable Objects</strong>: Provides persistent sandboxes with state management</li>
</ul>
<h2 id="4-test-locally"><ol start="4">
<li>Test locally</li>
</ol></h2>
<p>Start the development server:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13302.md")
</aside>
<p>Test with curl:</p>
<pre tabindex="0"><code class="language-sh">&#35; Simple calculation&#10;curl -X POST http://localhost:8787/run \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;input&quot;: &quot;Calculate 5 factorial using Python&quot;}&#x27;&#10;&#10;&#35; Complex operations&#10;curl -X POST http://localhost:8787/run \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;input&quot;: &quot;Use Python to find all prime numbers under 20&quot;}&#x27;&#10;&#10;&#35; Data analysis&#10;curl -X POST http://localhost:8787/run \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;input&quot;: &quot;Create a list of the first 10 squares and calculate their sum&quot;}&#x27;&#10;</code></pre>
<h2 id="5-deploy"><ol start="5">
<li>Deploy</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13301.md")
</aside>
<h2 id="6-test-your-deployment"><ol start="6">
<li>Test your deployment</li>
</ol></h2>
<p>Try more complex queries:</p>
<pre tabindex="0"><code class="language-sh">&#35; Data visualization preparation&#10;curl -X POST https://workers-ai-interpreter.YOUR_SUBDOMAIN.workers.dev/run \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;input&quot;: &quot;Generate sample sales data for 12 months and calculate quarterly totals&quot;}&#x27;&#10;&#10;&#35; Algorithm implementation&#10;curl -X POST https://workers-ai-interpreter.YOUR_SUBDOMAIN.workers.dev/run \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;input&quot;: &quot;Implement a binary search function and test it with a sorted array&quot;}&#x27;&#10;&#10;&#35; Mathematical computation&#10;curl -X POST https://workers-ai-interpreter.YOUR_SUBDOMAIN.workers.dev/run \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;input&quot;: &quot;Calculate the standard deviation of [2, 4, 4, 4, 5, 5, 7, 9]&quot;}&#x27;&#10;</code></pre>
<h2 id="how-it-works">How it works</h2>
<ol>
<li><strong>User input</strong>: Send natural language prompts to the <code>/run</code> endpoint</li>
<li><strong>AI decision</strong>: GPT-OSS receives the prompt with an <code>execute_python</code> tool available</li>
<li><strong>Smart execution</strong>: Model decides whether Python code execution is needed</li>
<li><strong>Sandbox isolation</strong>: Code runs in isolated Cloudflare Sandbox containers</li>
<li><strong>AI explanation</strong>: Results are integrated back into the AI's response for final output</li>
</ol>
<h2 id="what-you-built">What you built</h2>
<p>You deployed a sophisticated code interpreter that:</p>
<ul>
<li><strong>Native Workers AI integration</strong>: Uses the official <code>workers-ai-provider</code> package for seamless integration</li>
<li><strong>Function calling</strong>: Leverages Vercel AI SDK for clean tool definitions and execution</li>
<li><strong>Secure execution</strong>: Runs Python code in isolated sandbox containers</li>
<li><strong>Intelligent responses</strong>: Combines AI reasoning with code execution results</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/sandbox/tutorials/analyze-data-with-ai/">Analyze data with AI</a> - Add pandas and matplotlib for advanced data analysis</li>
<li><a href="/sandbox/api/interpreter/">Code Interpreter API</a> - Use the built-in code interpreter with structured outputs</li>
<li><a href="/sandbox/guides/streaming-output/">Streaming output</a> - Show real-time execution progress</li>
<li><a href="/sandbox/api/">API reference</a> - Explore all available sandbox methods</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers-ai/">Workers AI</a> - Learn about Cloudflare's AI platform</li>
<li><a href="https://github.com/cloudflare/ai/tree/main/packages/workers-ai-provider">workers-ai-provider package</a> - Official Workers AI integration</li>
<li><a href="https://sdk.vercel.ai/">Vercel AI SDK</a> - Universal toolkit for AI applications</li>
<li><a href="/workers-ai/models/gpt-oss-120b/">GPT-OSS model documentation</a> - Model details and capabilities</li>
</ul>
