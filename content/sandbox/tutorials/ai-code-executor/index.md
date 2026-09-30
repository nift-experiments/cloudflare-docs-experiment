<p>Build an AI-powered code execution system using Sandbox SDK and Claude. Turn natural language questions into Python code, execute it securely, and return results.</p>
<p><strong>Time to complete:</strong> 20 minutes</p>
<h2 id="what-you-ll-build">What you'll build</h2>
<p>An API that accepts questions like &quot;What's the 100th Fibonacci number?&quot;, uses Claude to generate Python code, executes it in an isolated sandbox, and returns the results.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13341.md")
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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div></div>
<pre><code class="language-sh">cd ai-code-executor&#10;</code></pre>
<h2 id="2-install-dependencies"><ol start="2">
<li>Install dependencies</li>
</ol></h2>
<p>Install the Anthropic SDK:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @anthropic-ai/sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @anthropic-ai/sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-build-your-code-executor"><ol start="3">
<li>Build your code executor</li>
</ol></h2>
<p>Replace the contents of <code>src/index.ts</code>:</p>
<pre><code class="language-typescript">import { getSandbox, type Sandbox } from &#x27;@cloudflare/sandbox&#x27;;&#10;import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;export { Sandbox } from &#x27;@cloudflare/sandbox&#x27;;&#10;&#10;interface Env {&#10;	Sandbox: DurableObjectNamespace&lt;Sandbox&gt;;&#10;	ANTHROPIC_API_KEY: string;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		if (request.method !== &#x27;POST&#x27; || new URL(request.url).pathname !== &#x27;/execute&#x27;) {&#10;			return new Response(&#x27;POST /execute with { &quot;question&quot;: &quot;your question&quot; }&#x27;);&#10;		}&#10;&#10;		try {&#10;			const { question } = await request.json();&#10;&#10;			if (!question) {&#10;				return Response.json({ error: &#x27;Question is required&#x27; }, { status: 400 });&#10;			}&#10;&#10;			// Use Claude to generate Python code&#10;			const anthropic = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });&#10;			const codeGeneration = await anthropic.messages.create({&#10;				model: &#x27;claude-sonnet-4-5&#x27;,&#10;				max_tokens: 1024,&#10;				messages: [{&#10;					role: &#x27;user&#x27;,&#10;					content: `Generate Python code to answer: &quot;${question}&quot;&#10;&#10;Requirements:&#10;&#45; Use only Python standard library&#10;&#45; Print the result using print()&#10;&#45; Keep code simple and safe&#10;&#10;Return ONLY the code, no explanations.`&#10;				}],&#10;			});&#10;&#10;			const generatedCode = codeGeneration.content[0]?.type === &#x27;text&#x27;&#10;				? codeGeneration.content[0].text&#10;				: &#x27;&#x27;;&#10;&#10;			if (!generatedCode) {&#10;				return Response.json({ error: &#x27;Failed to generate code&#x27; }, { status: 500 });&#10;			}&#10;&#10;			// Strip markdown code fences if present&#10;			const cleanCode = generatedCode&#10;				.replace(/^```python?\n?/, &#x27;&#x27;)&#10;				.replace(/\n?```\s*$/, &#x27;&#x27;)&#10;				.trim();&#10;&#10;			// Execute the code in a sandbox&#10;			const sandbox = getSandbox(env.Sandbox, &#x27;demo-user&#x27;);&#10;			await sandbox.writeFile(&#x27;/tmp/code.py&#x27;, cleanCode);&#10;			const result = await sandbox.exec(&#x27;python /tmp/code.py&#x27;);&#10;&#10;			return Response.json({&#10;				success: result.success,&#10;				question,&#10;				code: generatedCode,&#10;				output: result.stdout,&#10;				error: result.stderr&#10;			});&#10;&#10;		} catch (error: any) {&#10;			return Response.json(&#10;				{ error: &#x27;Internal server error&#x27;, message: error.message },&#10;				{ status: 500 }&#10;			);&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p><strong>How it works:</strong></p>
<ol>
<li>Receives a question via POST to <code>/execute</code></li>
<li>Uses Claude to generate Python code</li>
<li>Writes code to <code>/tmp/code.py</code> in the sandbox</li>
<li>Executes with <code>sandbox.exec('python /tmp/code.py')</code></li>
<li>Returns both the code and execution results</li>
</ol>
<h2 id="4-set-up-local-environment-variables"><ol start="4">
<li>Set up local environment variables</li>
</ol></h2>
<p>Create a <code>.dev.vars</code> file in your project root for local development:</p>
<pre><code class="language-sh">echo &quot;ANTHROPIC_API_KEY=your_api_key_here&quot; &gt; .dev.vars&#10;</code></pre>
<p>Replace <code>your_api_key_here</code> with your actual API key from the <a href="https://console.anthropic.com/">Anthropic Console</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13340.md")
</aside>
<h2 id="5-test-locally"><ol start="5">
<li>Test locally</li>
</ol></h2>
<p>Start the development server:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13339.md")
</aside>
<p>Test with curl:</p>
<pre><code class="language-sh">curl -X POST http://localhost:8787/execute \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;question&quot;: &quot;What is the 10th Fibonacci number?&quot;}&#x27;&#10;</code></pre>
<p>Response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;question&quot;: &quot;What is the 10th Fibonacci number?&quot;,&#10;  &quot;code&quot;: &quot;def fibonacci(n):\n    if n &lt;= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nprint(fibonacci(10))&quot;,&#10;  &quot;output&quot;: &quot;55\n&quot;,&#10;  &quot;error&quot;: &quot;&quot;&#10;}&#10;</code></pre>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Then set your Anthropic API key as a production secret:</p>
<pre><code class="language-sh">npx wrangler secret put ANTHROPIC_API_KEY&#10;</code></pre>
<p>Paste your API key from the <a href="https://console.anthropic.com/">Anthropic Console</a> when prompted.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13338.md")
</aside>
<h2 id="7-test-your-deployment"><ol start="7">
<li>Test your deployment</li>
</ol></h2>
<p>Try different questions:</p>
<pre><code class="language-sh">&#35; Factorial&#10;curl -X POST https://ai-code-executor.YOUR_SUBDOMAIN.workers.dev/execute \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;question&quot;: &quot;Calculate the factorial of 5&quot;}&#x27;&#10;&#10;&#35; Statistics&#10;curl -X POST https://ai-code-executor.YOUR_SUBDOMAIN.workers.dev/execute \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;question&quot;: &quot;What is the mean of [10, 20, 30, 40, 50]?&quot;}&#x27;&#10;&#10;&#35; String manipulation&#10;curl -X POST https://ai-code-executor.YOUR_SUBDOMAIN.workers.dev/execute \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;question&quot;: &quot;Reverse the string \&quot;Hello World\&quot;&quot;}&#x27;&#10;</code></pre>
<h2 id="what-you-built">What you built</h2>
<p>You created an AI code execution system that:</p>
<ul>
<li>Accepts natural language questions</li>
<li>Generates Python code with Claude</li>
<li>Executes code securely in isolated sandboxes</li>
<li>Returns results with error handling</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/sandbox/tutorials/workers-ai-code-interpreter/">Code interpreter with Workers AI</a> - Use Cloudflare's native AI models with official packages</li>
<li><a href="/sandbox/tutorials/analyze-data-with-ai/">Analyze data with AI</a> - Add pandas and matplotlib for data analysis</li>
<li><a href="/sandbox/api/interpreter/">Code Interpreter API</a> - Use the built-in code interpreter instead of exec</li>
<li><a href="/sandbox/guides/streaming-output/">Streaming output</a> - Show real-time execution progress</li>
<li><a href="/sandbox/api/">API reference</a> - Explore all available methods</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://docs.anthropic.com/">Anthropic Claude documentation</a></li>
<li><a href="/workers-ai/">Workers AI</a> - Use Cloudflare's built-in models</li>
<li><a href="https://github.com/cloudflare/ai/tree/main/packages/workers-ai-provider">workers-ai-provider package</a> - Official Workers AI integration</li>
</ul>
