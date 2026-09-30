---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/
  description: Upload CSV files, generate analysis code with Claude, and return visualizations.
  full_title: Analyze data with AI · Cloudflare Sandbox SDK docs
  head_html: <title>Analyze data with AI · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload CSV files, generate analysis code with Claude, and return visualizations."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/index.md"><meta property="og:title" content="Analyze data with AI · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload CSV files, generate analysis code with Claude, and return visualizations."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/#page","headline":"Analyze data with AI \u00b7 Cloudflare Sandbox SDK docs","description":"Upload CSV files, generate analysis code with Claude, and return visualizations.","url":"https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/tutorials/analyze-data-with-ai/
  schema: 1
---
<p>Build an AI-powered data analysis system that accepts CSV uploads, uses Claude to generate Python analysis code, executes it in sandboxes, and returns visualizations.</p>
<p><strong>Time to complete</strong>: 25 minutes</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13337.md")
</div></details>
<p>You'll also need:</p>
<ul>
<li>An <a href="https://console.anthropic.com/">Anthropic API key</a> for Claude</li>
<li><a href="https://www.docker.com/">Docker</a> running locally</li>
</ul>
<h2 id="1-create-your-project"><ol>
<li>Create your project</li>
</ol></h2>
<p>Create a new Sandbox SDK project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- analyze-data --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- analyze-data --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare analyze-data --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare analyze-data --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest analyze-data --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest analyze-data --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div></div>
<pre tabindex="0"><code class="language-sh">cd analyze-data&#10;</code></pre>
<h2 id="2-install-dependencies"><ol start="2">
<li>Install dependencies</li>
</ol></h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-build-the-analysis-handler"><ol start="3">
<li>Build the analysis handler</li>
</ol></h2>
<p>Replace <code>src/index.ts</code>:</p>
<pre tabindex="0"><code class="language-typescript">import { getSandbox, proxyToSandbox, type Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;import Anthropic from &quot;@anthropic-ai/sdk&quot;;&#10;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;interface Env {&#10;	Sandbox: DurableObjectNamespace&lt;Sandbox&gt;;&#10;	ANTHROPIC_API_KEY: string;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const proxyResponse = await proxyToSandbox(request, env);&#10;		if (proxyResponse) return proxyResponse;&#10;&#10;		if (request.method !== &quot;POST&quot;) {&#10;			return Response.json(&#10;				{ error: &quot;POST CSV file and question&quot; },&#10;				{ status: 405 },&#10;			);&#10;		}&#10;&#10;		try {&#10;			const formData = await request.formData();&#10;			const csvFile = formData.get(&quot;file&quot;) as File;&#10;			const question = formData.get(&quot;question&quot;) as string;&#10;&#10;			if (!csvFile || !question) {&#10;				return Response.json(&#10;					{ error: &quot;Missing file or question&quot; },&#10;					{ status: 400 },&#10;				);&#10;			}&#10;&#10;			// Upload CSV to sandbox&#10;			const sandbox = getSandbox(env.Sandbox, `analysis-${Date.now()}`);&#10;			const csvPath = &quot;/workspace/data.csv&quot;;&#10;			await sandbox.writeFile(csvPath, await csvFile.text());&#10;&#10;			// Analyze CSV structure&#10;			const structure = await sandbox.exec(&#10;				`python3 -c &quot;import pandas as pd; df = pd.read_csv(&#x27;${csvPath}&#x27;); print(f&#x27;Rows: {len(df)}&#x27;); print(f&#x27;Columns: {list(df.columns)[:5]}&#x27;)&quot;`,&#10;			);&#10;&#10;			if (!structure.success) {&#10;				return Response.json(&#10;					{ error: &quot;Failed to read CSV&quot;, details: structure.stderr },&#10;					{ status: 400 },&#10;				);&#10;			}&#10;&#10;			// Generate analysis code with Claude&#10;			const code = await generateAnalysisCode(&#10;				env.ANTHROPIC_API_KEY,&#10;				csvPath,&#10;				question,&#10;				structure.stdout,&#10;			);&#10;&#10;			// Write and execute the analysis code&#10;			await sandbox.writeFile(&quot;/workspace/analyze.py&quot;, code);&#10;			const result = await sandbox.exec(&quot;python /workspace/analyze.py&quot;);&#10;&#10;			if (!result.success) {&#10;				return Response.json(&#10;					{ error: &quot;Analysis failed&quot;, details: result.stderr },&#10;					{ status: 500 },&#10;				);&#10;			}&#10;&#10;			async function streamToBase64(stream) {&#10;			  const blob = await new Response(stream).blob();&#10;			  const buffer = await blob.arrayBuffer();&#10;			  const bytes = new Uint8Array(buffer);&#10;&#10;			  // Convert to base64&#10;			  let binary = &#x27;&#x27;;&#10;			  for (let i = 0; i &lt; bytes.length; i++) {&#10;			    binary += String.fromCharCode(bytes[i]);&#10;			  }&#10;			  return btoa(binary);&#10;			}&#10;&#10;			// Check for generated chart&#10;			let chart = null;&#10;			try {&#10;				const { content, mimeType } = await sandbox.readFile(&quot;/workspace/chart.png&quot;, {&#10;					encoding: &quot;none&quot;&#10;				});&#10;				chart = `data:${mimeType};base64,${await streamToBase64(content)}`;&#10;			} catch {&#10;				// No chart generated&#10;			}&#10;&#10;			await sandbox.destroy();&#10;&#10;			return Response.json({&#10;				success: true,&#10;				output: result.stdout,&#10;				chart,&#10;				code,&#10;			});&#10;		} catch (error: any) {&#10;			return Response.json({ error: error.message }, { status: 500 });&#10;		}&#10;	},&#10;};&#10;&#10;async function generateAnalysisCode(&#10;	apiKey: string,&#10;	csvPath: string,&#10;	question: string,&#10;	csvStructure: string,&#10;): Promise&lt;string&gt; {&#10;	const anthropic = new Anthropic({ apiKey });&#10;&#10;	const response = await anthropic.messages.create({&#10;		model: &quot;claude-sonnet-4-5&quot;,&#10;		max_tokens: 2048,&#10;		messages: [&#10;			{&#10;				role: &quot;user&quot;,&#10;				content: `CSV at ${csvPath}:&#10;${csvStructure}&#10;&#10;Question: &quot;${question}&quot;&#10;&#10;Generate Python code that:&#10;&#45; Reads CSV with pandas&#10;&#45; Answers the question&#10;&#45; Saves charts to /workspace/chart.png if helpful&#10;&#45; Prints findings to stdout&#10;&#10;Use pandas, numpy, matplotlib.`,&#10;			},&#10;		],&#10;		tools: [&#10;			{&#10;				name: &quot;generate_python_code&quot;,&#10;				description: &quot;Generate Python code for data analysis&quot;,&#10;				input_schema: {&#10;					type: &quot;object&quot;,&#10;					properties: {&#10;						code: { type: &quot;string&quot;, description: &quot;Complete Python code&quot; },&#10;					},&#10;					required: [&quot;code&quot;],&#10;				},&#10;			},&#10;		],&#10;	});&#10;&#10;	for (const block of response.content) {&#10;		if (block.type === &quot;tool_use&quot; &amp;&amp; block.name === &quot;generate_python_code&quot;) {&#10;			return (block.input as { code: string }).code;&#10;		}&#10;	}&#10;&#10;	throw new Error(&quot;Failed to generate code&quot;);&#10;}&#10;</code></pre>
<h2 id="4-set-up-local-environment-variables"><ol start="4">
<li>Set up local environment variables</li>
</ol></h2>
<p>Create a <code>.dev.vars</code> file in your project root for local development:</p>
<pre tabindex="0"><code class="language-sh">echo &quot;ANTHROPIC_API_KEY=your_api_key_here\nSANDBOX_TRANSPORT=rpc&quot; &gt; .dev.vars&#10;</code></pre>
<p>Replace <code>your_api_key_here</code> with your actual API key from the <a href="https://console.anthropic.com/">Anthropic Console</a>.</p>
<p>The <code>SANDBOX_TRANSPORT</code> is required to use the new file streaming APIs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13336.md")
</aside>
<h2 id="5-test-locally"><ol start="5">
<li>Test locally</li>
</ol></h2>
<p>Download a sample CSV:</p>
<pre tabindex="0"><code class="language-sh">&#35; Create a test CSV&#10;echo &quot;year,rating,title&#10;2020,8.5,Movie A&#10;2021,7.2,Movie B&#10;2022,9.1,Movie C&quot; &gt; test.csv&#10;</code></pre>
<p>Start the dev server:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<p>Test with curl:</p>
<pre tabindex="0"><code class="language-sh">curl -X POST http://localhost:8787 \&#10;  &#45;F &quot;file=@test.csv&quot; \&#10;  &#45;F &quot;question=What is the average rating by year?&quot;&#10;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;output&quot;: &quot;Average ratings by year:\n2020: 8.5\n2021: 7.2\n2022: 9.1&quot;,&#10;	&quot;chart&quot;: &quot;data:image/png;base64,...&quot;,&#10;	&quot;code&quot;: &quot;import pandas as pd\nimport matplotlib.pyplot as plt\n...&quot;&#10;}&#10;</code></pre>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Then set your Anthropic API key as a production secret:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put ANTHROPIC_API_KEY&#10;</code></pre>
<p>Paste your API key from the <a href="https://console.anthropic.com/">Anthropic Console</a> when prompted.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13335.md")
</aside>
<h2 id="what-you-built">What you built</h2>
<p>An AI data analysis system that:</p>
<ul>
<li>Uploads CSV files to sandboxes</li>
<li>Uses Claude's tool calling to generate analysis code</li>
<li>Executes Python with pandas and matplotlib</li>
<li>Returns text output and visualizations</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/sandbox/api/interpreter/">Code Interpreter API</a> - Use the built-in code interpreter</li>
<li><a href="/sandbox/guides/manage-files/">File operations</a> - Advanced file handling</li>
<li><a href="/sandbox/guides/streaming-output/">Streaming output</a> - Real-time progress updates</li>
</ul>
