---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/
  description: Clone repositories, analyze code with Claude, and post review comments to GitHub PRs.
  full_title: Build a code review bot · Cloudflare Sandbox SDK docs
  head_html: <title>Build a code review bot · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Clone repositories, analyze code with Claude, and post review comments to GitHub PRs."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/index.md"><meta property="og:title" content="Build a code review bot · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Clone repositories, analyze code with Claude, and post review comments to GitHub PRs."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/#page","headline":"Build a code review bot \u00b7 Cloudflare Sandbox SDK docs","description":"Clone repositories, analyze code with Claude, and post review comments to GitHub PRs.","url":"https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/tutorials/code-review-bot/
  schema: 1
---
<p>Build a GitHub bot that responds to pull requests, clones the repository in a sandbox, uses Claude to analyze code changes, and posts review comments.</p>
<p><strong>Time to complete</strong>: 30 minutes</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13327.md")
</div></details>
<p>You'll also need:</p>
<ul>
<li>A <a href="https://github.com/">GitHub account</a> and <a href="https://github.com/settings/personal-access-tokens/new">fine-grained personal access token</a> with the following permissions:
<ul>
<li><strong>Repository access</strong>: Select the specific repository you want to test with</li>
<li><strong>Permissions</strong> &gt; <strong>Repository permissions</strong>:
<ul>
<li><strong>Metadata</strong>: Read-only (required)</li>
<li><strong>Contents</strong>: Read-only (required to clone the repository)</li>
<li><strong>Pull requests</strong>: Read and write (required to post review comments)</li>
</ul>
</li>
</ul>
</li>
<li>An <a href="https://console.anthropic.com/">Anthropic API key</a> for Claude</li>
<li>A GitHub repository for testing</li>
</ul>
<h2 id="1-create-your-project"><ol>
<li>Create your project</li>
</ol></h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- code-review-bot --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- code-review-bot --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare code-review-bot --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare code-review-bot --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest code-review-bot --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest code-review-bot --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div></div>
<pre tabindex="0"><code class="language-sh">cd code-review-bot&#10;</code></pre>
<h2 id="2-install-dependencies"><ol start="2">
<li>Install dependencies</li>
</ol></h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @anthropic-ai/sdk @octokit/rest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @anthropic-ai/sdk @octokit/rest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @anthropic-ai/sdk @octokit/rest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @anthropic-ai/sdk @octokit/rest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @anthropic-ai/sdk @octokit/rest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @anthropic-ai/sdk @octokit/rest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @anthropic-ai/sdk @octokit/rest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @anthropic-ai/sdk @octokit/rest" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-build-the-webhook-handler"><ol start="3">
<li>Build the webhook handler</li>
</ol></h2>
<p>Replace <code>src/index.ts</code>:</p>
<pre tabindex="0"><code class="language-typescript">import { getSandbox, proxyToSandbox, type Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;import { Octokit } from &quot;@octokit/rest&quot;;&#10;import Anthropic from &quot;@anthropic-ai/sdk&quot;;&#10;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;interface Env {&#10;	Sandbox: DurableObjectNamespace&lt;Sandbox&gt;;&#10;	GITHUB_TOKEN: string;&#10;	ANTHROPIC_API_KEY: string;&#10;	WEBHOOK_SECRET: string;&#10;}&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		const proxyResponse = await proxyToSandbox(request, env);&#10;		if (proxyResponse) return proxyResponse;&#10;&#10;		const url = new URL(request.url);&#10;&#10;		if (url.pathname === &quot;/webhook&quot; &amp;&amp; request.method === &quot;POST&quot;) {&#10;			const signature = request.headers.get(&quot;x-hub-signature-256&quot;);&#10;			const contentType = request.headers.get(&quot;content-type&quot;) || &quot;&quot;;&#10;			const body = await request.text();&#10;&#10;			// Verify webhook signature&#10;			if (&#10;				!signature ||&#10;				!(await verifySignature(body, signature, env.WEBHOOK_SECRET))&#10;			) {&#10;				return Response.json({ error: &quot;Invalid signature&quot; }, { status: 401 });&#10;			}&#10;&#10;			const event = request.headers.get(&quot;x-github-event&quot;);&#10;&#10;			// Parse payload (GitHub can send as JSON or form-encoded)&#10;			let payload;&#10;			if (contentType.includes(&quot;application/json&quot;)) {&#10;				payload = JSON.parse(body);&#10;			} else {&#10;				// Handle form-encoded payload&#10;				const params = new URLSearchParams(body);&#10;				payload = JSON.parse(params.get(&quot;payload&quot;) || &quot;{}&quot;);&#10;			}&#10;&#10;			// Handle opened and reopened PRs&#10;			if (&#10;				event === &quot;pull_request&quot; &amp;&amp;&#10;				(payload.action === &quot;opened&quot; || payload.action === &quot;reopened&quot;)&#10;			) {&#10;				console.log(`Starting review for PR #${payload.pull_request.number}`);&#10;				// Use waitUntil to ensure the review completes even after response is sent&#10;				ctx.waitUntil(&#10;					reviewPullRequest(payload, env).catch(console.error),&#10;				);&#10;				return Response.json({ message: &quot;Review started&quot; });&#10;			}&#10;&#10;			return Response.json({ message: &quot;Event ignored&quot; });&#10;		}&#10;&#10;		return new Response(&#10;			&quot;Code Review Bot\n\nConfigure GitHub webhook to POST /webhook&quot;,&#10;		);&#10;	},&#10;};&#10;&#10;async function verifySignature(&#10;	payload: string,&#10;	signature: string,&#10;	secret: string,&#10;): Promise&lt;boolean&gt; {&#10;	const encoder = new TextEncoder();&#10;	const key = await crypto.subtle.importKey(&#10;		&quot;raw&quot;,&#10;		encoder.encode(secret),&#10;		{ name: &quot;HMAC&quot;, hash: &quot;SHA-256&quot; },&#10;		false,&#10;		[&quot;sign&quot;],&#10;	);&#10;&#10;	const signatureBytes = await crypto.subtle.sign(&#10;		&quot;HMAC&quot;,&#10;		key,&#10;		encoder.encode(payload),&#10;	);&#10;	const expected =&#10;		&quot;sha256=&quot; +&#10;		Array.from(new Uint8Array(signatureBytes))&#10;			.map((b) =&gt; b.toString(16).padStart(2, &quot;0&quot;))&#10;			.join(&quot;&quot;);&#10;&#10;	return signature === expected;&#10;}&#10;&#10;async function reviewPullRequest(payload: any, env: Env): Promise&lt;void&gt; {&#10;	const pr = payload.pull_request;&#10;	const repo = payload.repository;&#10;	const octokit = new Octokit({ auth: env.GITHUB_TOKEN });&#10;	const sandbox = getSandbox(env.Sandbox, `review-${pr.number}`);&#10;&#10;	try {&#10;		// Post initial comment&#10;		console.log(&quot;Posting initial comment...&quot;);&#10;		await octokit.issues.createComment({&#10;			owner: repo.owner.login,&#10;			repo: repo.name,&#10;			issue_number: pr.number,&#10;			body: &quot;Code review in progress...&quot;,&#10;		});&#10;		// Clone repository&#10;		console.log(&quot;Cloning repository...&quot;);&#10;		const cloneUrl = `https://${env.GITHUB_TOKEN}@github.com/${repo.owner.login}/${repo.name}.git`;&#10;		await sandbox.exec(&#10;			`git clone --depth=1 --branch=${pr.head.ref} ${cloneUrl} /workspace/repo`,&#10;		);&#10;&#10;		// Get changed files&#10;		console.log(&quot;Fetching changed files...&quot;);&#10;		const comparison = await octokit.repos.compareCommits({&#10;			owner: repo.owner.login,&#10;			repo: repo.name,&#10;			base: pr.base.sha,&#10;			head: pr.head.sha,&#10;		});&#10;&#10;		const files = [];&#10;		for (const file of (comparison.data.files || []).slice(0, 5)) {&#10;			if (file.status !== &quot;removed&quot;) {&#10;				const content = await sandbox.readFile(&#10;					`/workspace/repo/${file.filename}`,&#10;				);&#10;				files.push({&#10;					path: file.filename,&#10;					patch: file.patch || &quot;&quot;,&#10;					content: content.content,&#10;				});&#10;			}&#10;		}&#10;&#10;		// Generate review with Claude&#10;		console.log(`Analyzing ${files.length} files with Claude...`);&#10;		const anthropic = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });&#10;		const response = await anthropic.messages.create({&#10;			model: &quot;claude-sonnet-4-5&quot;,&#10;			max_tokens: 2048,&#10;			messages: [&#10;				{&#10;					role: &quot;user&quot;,&#10;					content: `Review this PR:&#10;&#10;Title: ${pr.title}&#10;&#10;Changed files:&#10;${files.map((f) =&gt; `File: ${f.path}\nDiff:\n${f.patch}\n\nContent:\n${f.content.substring(0, 1000)}`).join(&quot;\n\n&quot;)}&#10;&#10;Provide a brief code review focusing on bugs, security, and best practices.`,&#10;				},&#10;			],&#10;		});&#10;&#10;		const review =&#10;			response.content[0]?.type === &quot;text&quot;&#10;				? response.content[0].text&#10;				: &quot;No review generated&quot;;&#10;&#10;		// Post review comment&#10;		console.log(&quot;Posting review...&quot;);&#10;		await octokit.issues.createComment({&#10;			owner: repo.owner.login,&#10;			repo: repo.name,&#10;			issue_number: pr.number,&#10;			body: `## Code Review\n\n${review}\n\n---\n*Generated by Claude*`,&#10;		});&#10;		console.log(&quot;Review complete!&quot;);&#10;	} catch (error: any) {&#10;		console.error(&quot;Review failed:&quot;, error);&#10;		await octokit.issues.createComment({&#10;			owner: repo.owner.login,&#10;			repo: repo.name,&#10;			issue_number: pr.number,&#10;			body: `Review failed: ${error.message}`,&#10;		});&#10;	} finally {&#10;		await sandbox.destroy();&#10;	}&#10;}&#10;</code></pre>
<h2 id="4-set-up-local-environment-variables"><ol start="4">
<li>Set up local environment variables</li>
</ol></h2>
<p>Create a <code>.dev.vars</code> file in your project root for local development:</p>
<pre tabindex="0"><code class="language-sh">cat &gt; .dev.vars &lt;&lt; EOF&#10;GITHUB_TOKEN=your_github_token_here&#10;ANTHROPIC_API_KEY=your_anthropic_key_here&#10;WEBHOOK_SECRET=your_webhook_secret_here&#10;EOF&#10;</code></pre>
<p>Replace the placeholder values with:</p>
<ul>
<li><code>GITHUB_TOKEN</code>: Your GitHub personal access token with repo permissions</li>
<li><code>ANTHROPIC_API_KEY</code>: Your API key from the <a href="https://console.anthropic.com/">Anthropic Console</a></li>
<li><code>WEBHOOK_SECRET</code>: A random string (for example: <code>openssl rand -hex 32</code>)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13326.md")
</aside>
<h2 id="5-expose-local-server-with-cloudflare-tunnel"><ol start="5">
<li>Expose local server with Cloudflare Tunnel</li>
</ol></h2>
<p>To test with real GitHub webhooks locally, use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> to expose your local development server.</p>
<p>Start the development server:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<p>In a separate terminal, create a tunnel to your local server:</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel --url http://localhost:8787&#10;</code></pre>
<p>This will output a public URL (for example, <code>https://example.trycloudflare.com</code>). Copy this URL for the next step.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13325.md")
</aside>
<h2 id="6-configure-github-webhook-for-local-testing"><ol start="6">
<li>Configure GitHub webhook for local testing</li>
</ol></h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/13324.md")
</aside>
<ol>
<li>Navigate to your test repository on GitHub</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Webhooks</strong> &gt; <strong>Add webhook</strong></li>
<li>Set <strong>Payload URL</strong>: Your Cloudflare Tunnel URL from Step 5 with <code>/webhook</code> appended (for example, <code>https://example.trycloudflare.com/webhook</code>)</li>
<li>Set <strong>Content type</strong>: <code>application/json</code></li>
<li>Set <strong>Secret</strong>: Same value you used for <code>WEBHOOK_SECRET</code> in your <code>.dev.vars</code> file</li>
<li>Select <strong>Let me select individual events</strong> → Check <strong>Pull requests</strong></li>
<li>Click <strong>Add webhook</strong></li>
</ol>
<h2 id="7-test-locally-with-a-pull-request"><ol start="7">
<li>Test locally with a pull request</li>
</ol></h2>
<p>Create a test PR:</p>
<pre tabindex="0"><code class="language-sh">git checkout -b test-review&#10;echo &quot;console.log(&#x27;test&#x27;);&quot; &gt; test.js&#10;git add test.js&#10;git commit -m &quot;Add test file&quot;&#10;git push origin test-review&#10;</code></pre>
<p>Open the PR on GitHub. The bot should post a review comment within a few seconds.</p>
<h2 id="8-deploy-to-production"><ol start="8">
<li>Deploy to production</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Then set your production secrets:</p>
<pre tabindex="0"><code class="language-sh">&#35; GitHub token (needs repo permissions)&#10;npx wrangler secret put GITHUB_TOKEN&#10;&#10;&#35; Anthropic API key&#10;npx wrangler secret put ANTHROPIC_API_KEY&#10;&#10;&#35; Webhook secret (use the same value from .dev.vars)&#10;npx wrangler secret put WEBHOOK_SECRET&#10;</code></pre>
<h2 id="9-update-webhook-for-production"><ol start="9">
<li>Update webhook for production</li>
</ol></h2>
<ol>
<li>Go to your repository <strong>Settings</strong> &gt; <strong>Webhooks</strong></li>
<li>Click on your existing webhook</li>
<li>Update <strong>Payload URL</strong> to your deployed Worker URL: <code>https://code-review-bot.YOUR_SUBDOMAIN.workers.dev/webhook</code></li>
<li>Click <strong>Update webhook</strong></li>
</ol>
<p>Your bot is now running in production and will review all new pull requests automatically.</p>
<h2 id="what-you-built">What you built</h2>
<p>A GitHub code review bot that:</p>
<ul>
<li>Receives webhook events from GitHub</li>
<li>Clones repositories in isolated sandboxes</li>
<li>Uses Claude to analyze code changes</li>
<li>Posts review comments automatically</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/sandbox/api/files/#gitcheckout">Git operations</a> - Advanced repository handling</li>
<li><a href="/sandbox/api/sessions/">Sessions API</a> - Manage long-running sandbox operations</li>
<li><a href="https://docs.github.com/en/apps">GitHub Apps</a> - Build a proper GitHub App</li>
</ul>
