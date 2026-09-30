<p><a href="https://www.stagehand.dev/">Stagehand</a> is an open-source, AI-powered browser automation library. Stagehand lets you combine code with natural-language instructions powered by AI, eliminating the need to dictate exact steps or specify selectors. With Stagehand, your agents are more resilient to website changes and easier to maintain, helping you build more reliably and flexibly.</p>
<p>This guide shows you how to deploy a <a href="/workers/">Worker</a> that uses Stagehand, Browser Run, and <a href="/workers-ai/">Workers AI</a> to automate a web task.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1401.md")
</aside>
<h2 id="use-stagehand-in-a-worker-with-workers-ai">Use Stagehand in a Worker with Workers AI</h2>
<p>In this example, you will use Stagehand to search for a movie on this <a href="https://demo.playwright.dev/movies">example movie directory</a>, extract its details (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.</p>
<details class="nb-details"><summary>See a video of this example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1402.md")
</div></details>
<p>If instead you want to skip the steps and get started right away, select <strong>Deploy to Cloudflare</strong> below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/playwright/tree/main/packages/playwright-cloudflare/examples/stagehand"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>After you deploy, you can interact with the Worker using this URL pattern:</p>
<pre><code>https://&lt;your-worker&gt;.workers.dev&#10;</code></pre>
<h3 id="1-set-up-your-project"><ol>
<li>Set up your project</li>
</ol></h3>
<p>Install the necessary dependencies:</p>
<pre><code class="language-bash">npm ci&#10;</code></pre>
<h3 id="2-configure-your-worker"><ol start="2">
<li>Configure your Worker</li>
</ol></h3>
<p>Update your Wrangler configuration file to include the bindings for Browser Run and <a href="/workers-ai/">Workers AI</a>:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1400.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1403.md")
</div>
<p>If you are using the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>, you need to include the following <a href="https://vite.dev/config/shared-options.html#resolve-alias">alias</a> in <code>vite.config.ts</code>:</p>
<pre><code class="language-ts">export default defineConfig({&#10;	// ...&#10;	resolve: {&#10;		alias: {&#10;			playwright: &quot;@cloudflare/playwright&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>If you are not using the Cloudflare Vite plugin, you need to include the following <a href="https://developers.cloudflare.com/workers/wrangler/configuration/#module-aliasing">module alias</a> to the wrangler configuration:</p>
<pre><code class="language-jsonc">{&#10;	// ...&#10;	&quot;alias&quot;: {&#10;		&quot;playwright&quot;: &quot;@cloudflare/playwright&quot;,&#10;	},&#10;}&#10;</code></pre>
<h3 id="3-write-the-worker-code"><ol start="3">
<li>Write the Worker code</li>
</ol></h3>
<p>Copy <a href="https://github.com/cloudflare/playwright/blob/main/packages/playwright-cloudflare/examples/stagehand/src/worker/workersAIClient.ts">workersAIClient.ts</a> to your project.</p>
<p>Then, in your Worker code, import the <code>workersAIClient.ts</code> file and use it to configure a new <code>Stagehand</code> instance:</p>
<pre><code class="language-ts">import { Stagehand } from &quot;@browserbasehq/stagehand&quot;;&#10;import { z } from &quot;zod&quot;;&#10;import { endpointURLString } from &quot;@cloudflare/playwright&quot;;&#10;import { WorkersAIClient } from &quot;./workersAIClient&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		if (new URL(request.url).pathname !== &quot;/&quot;)&#10;			return new Response(&quot;Not found&quot;, { status: 404 });&#10;&#10;		const stagehand = new Stagehand({&#10;			env: &quot;LOCAL&quot;,&#10;			localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;			llmClient: new WorkersAIClient(env.AI),&#10;			verbose: 1,&#10;		});&#10;&#10;		await stagehand.init();&#10;		const page = stagehand.page;&#10;&#10;		await page.goto(&quot;https://demo.playwright.dev/movies&quot;);&#10;&#10;		// if search is a multi-step action, stagehand will return an array of actions it needs to act on&#10;		const actions = await page.observe(&#x27;Search for &quot;Furiosa&quot;&#x27;);&#10;		for (const action of actions) await page.act(action);&#10;&#10;		await page.act(&quot;Click the search result&quot;);&#10;&#10;		// normal playwright functions work as expected&#10;		await page.waitForSelector(&quot;.info-wrapper .cast&quot;);&#10;&#10;		let movieInfo = await page.extract({&#10;			instruction: &quot;Extract movie information&quot;,&#10;			schema: z.object({&#10;				title: z.string(),&#10;				year: z.number(),&#10;				rating: z.number(),&#10;				genres: z.array(z.string()),&#10;				duration: z.number().describe(&quot;Duration in minutes&quot;),&#10;			}),&#10;		});&#10;&#10;		await stagehand.close();&#10;&#10;		return Response.json(movieInfo);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1399.md")
</aside>
<h3 id="4-build-the-project"><ol start="4">
<li>Build the project</li>
</ol></h3>
<pre><code class="language-bash">npm run build&#10;</code></pre>
<h3 id="5-deploy-to-cloudflare-workers"><ol start="5">
<li>Deploy to Cloudflare Workers</li>
</ol></h3>
<p>After you deploy, you can interact with the Worker using this URL pattern:</p>
<pre><code>https://&lt;your-worker&gt;.workers.dev&#10;</code></pre>
<pre><code class="language-bash">npm run deploy&#10;</code></pre>
<h2 id="use-cloudflare-ai-gateway-with-workers-ai">Use Cloudflare AI Gateway with Workers AI</h2>
<p><a href="/ai-gateway/">AI Gateway</a> is a service that adds observability to your AI applications. By routing your requests through AI Gateway, you can monitor and debug your AI applications.</p>
<p>To use AI Gateway with a third-party model, first create a gateway in the <strong>AI Gateway</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>In this example, we've named the gateway <code>stagehand-example-gateway</code>.</p>
<pre><code class="language-typescript">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl },&#10;	llmClient: new WorkersAIClient(env.AI, {&#10;		gateway: {&#10;			id: &quot;stagehand-example-gateway&quot;,&#10;		},&#10;	}),&#10;});&#10;</code></pre>
<h2 id="use-a-third-party-model">Use a third-party model</h2>
<p>If you want to use a model outside of Workers AI, you can configure Stagehand to use models from supported <a href="https://docs.stagehand.dev/configuration/models#supported-providers">third-party providers</a>, including OpenAI and Anthropic, by providing your own credentials.</p>
<p>In this example, you will configure Stagehand to use <a href="https://openai.com/">OpenAI</a>. You will need an OpenAI API key. Cloudflare recommends storing your API key as a <a href="/workers/configuration/secrets/">secret</a>.</p>
<pre><code class="language-bash">npx wrangler secret put OPENAI_API_KEY&#10;</code></pre>
<p>Then, configure Stagehand with your provider, model, and API key.</p>
<pre><code class="language-typescript">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;	modelName: &quot;openai/gpt-4.1&quot;,&#10;	modelClientOptions: {&#10;		apiKey: env.OPENAI_API_KEY,&#10;	},&#10;});&#10;</code></pre>
<h2 id="use-cloudflare-ai-gateway-with-a-third-party-model">Use Cloudflare AI Gateway with a third-party model</h2>
<p><a href="/ai-gateway/">AI Gateway</a> is a service that adds observability to your AI applications. By routing your requests through AI Gateway, you can monitor and debug your AI applications.</p>
<p>To use AI Gateway with a third-party model, first create a gateway in the <strong>AI Gateway</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>In this example, we are using <a href="/ai-gateway/usage/providers/openai/">OpenAI with AI Gateway</a>. Make sure to add the <code>baseURL</code> as shown below, with your own Account ID and Gateway ID.</p>
<p>You must specify the <code>apiKey</code> in the <code>modelClientOptions</code>:</p>
<pre><code class="language-typescript">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;	modelName: &quot;openai/gpt-4.1&quot;,&#10;	modelClientOptions: {&#10;		apiKey: env.OPENAI_API_KEY,&#10;		baseURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai`,&#10;	},&#10;});&#10;</code></pre>
<p>If you are using an authenticated AI Gateway, follow the instructions in <a href="/ai-gateway/configuration/authentication/">AI Gateway authentication</a> and include <code>cf-aig-authorization</code> as a header.</p>
<h2 id="stagehand-api">Stagehand API</h2>
<p>For the full list of Stagehand methods and capabilities, refer to the official <a href="https://docs.stagehand.dev/first-steps/introduction">Stagehand API documentation</a>.</p>
