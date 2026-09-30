<p>This guide will walk you through setting up and deploying a Workers AI project. You will use <a href="/workers/">Workers</a>, an AI Gateway binding, and a large language model (LLM), to deploy your first AI-powered application on the Cloudflare global network.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2811.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker Project</li>
</ol></h2>
<p>You will create a new Worker project using the create-Cloudflare CLI (C3). C3 is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>hello-ai</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- hello-ai</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- hello-ai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare hello-ai</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare hello-ai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest hello-ai</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest hello-ai" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Running <code>npm create cloudflare@latest</code> will prompt you to install the create-cloudflare package and lead you through setup. C3 will also install <a href="/workers/wrangler/">Wrangler</a>, the Cloudflare Developer Platform CLI.</p>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new <code>hello-ai</code> directory. Your new <code>hello-ai</code> directory will include:</p>
<ul>
<li>A &quot;Hello World&quot; Worker at <code>src/index.ts</code>.</li>
<li>A <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-bash">cd hello-ai&#10;</code></pre>
<h2 id="2-connect-your-worker-to-workers-ai"><ol start="2">
<li>Connect your Worker to Workers AI</li>
</ol></h2>
<p>You must create an AI binding for your Worker to connect to Workers AI. Bindings allow your Workers to interact with resources, like Workers AI, on the Cloudflare Developer Platform.</p>
<p>To bind Workers AI to your Worker, add the following to the end of your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2812.md")
</div>
<p>Your binding is <a href="/workers/reference/migrate-to-module-workers/#bindings-in-es-modules-format">available in your Worker code</a> on <a href="/workers/runtime-apis/handlers/fetch/"><code>env.AI</code></a>.</p>
<p>You can use <code>&quot;default&quot;</code> as the gateway ID in the next step. AI Gateway automatically creates a default gateway on the first authenticated request. Alternatively, you can <a href="/ai-gateway/get-started/">create a gateway manually</a> and use its ID.</p>
<h2 id="3-run-an-inference-task-containing-ai-gateway-in-your-worker"><ol start="3">
<li>Run an inference task containing AI Gateway in your Worker</li>
</ol></h2>
<p>You are now ready to run an inference task in your Worker. In this case, you will use an LLM, <a href="/workers-ai/models/llama-3.1-8b-instruct-fast/"><code>llama-3.1-8b-instruct-fast</code></a>, to answer a question.</p>
<p>Update the <code>index.ts</code> file in your <code>hello-ai</code> application directory with the following code:</p>
<pre><code class="language-typescript">export interface Env {&#10;	// If you set another name in the [Wrangler configuration file](/workers/wrangler/configuration/) as the value for &#x27;binding&#x27;,&#10;	// replace &quot;AI&quot; with the variable name you defined.&#10;	AI: Ai;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		// Specify the gateway label and other options here&#10;		const response = await env.AI.run(&#10;			&quot;@cf/meta/llama-3.1-8b-instruct-fast&quot;,&#10;			{&#10;				prompt: &quot;What is the origin of the phrase Hello, World&quot;,&#10;			},&#10;			{&#10;				gateway: {&#10;					id: &quot;default&quot;, // Uses the default gateway, or replace with your gateway ID&#10;					skipCache: true, // Optional: Skip cache if needed&#10;				},&#10;			},&#10;		);&#10;&#10;		// Return the AI response as a JSON object&#10;		return new Response(JSON.stringify(response), {&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Up to this point, you have created an AI binding for your Worker and configured your Worker to be able to execute the Llama 3.1 model. You can now test your project locally before you deploy globally.</p>
<h2 id="4-develop-locally-with-wrangler"><ol start="4">
<li>Develop locally with Wrangler</li>
</ol></h2>
<p>While in your project directory, test Workers AI locally by running <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>:</p>
<pre><code class="language-bash">npx wrangler dev&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-local-development-usage-charges">Workers AI local development usage charges</h3>
@markup("md", "content/.markup/bodies/2810.md")
</aside>
<p>You will be prompted to log in after you run <code>wrangler dev</code>. When you run <code>npx wrangler dev</code>, Wrangler will give you a URL (most likely <code>localhost:8787</code>) to review your Worker. After you go to the URL Wrangler provides, you will see a message that resembles the following example:</p>
<pre><code class="language-json">{&#10;  &quot;response&quot;: &quot;A fascinating question!\n\nThe phrase \&quot;Hello, World!\&quot; originates from a simple computer program written in the early days of programming. It is often attributed to Brian Kernighan, a Canadian computer scientist and a pioneer in the field of computer programming.\n\nIn the early 1970s, Kernighan, along with his colleague Dennis Ritchie, were working on the C programming language. They wanted to create a simple program that would output a message to the screen to demonstrate the basic structure of a program. They chose the phrase \&quot;Hello, World!\&quot; because it was a simple and recognizable message that would illustrate how a program could print text to the screen.\n\nThe exact code was written in the 5th edition of Kernighan and Ritchie&#x27;s book \&quot;The C Programming Language,\&quot; published in 1988. The code, literally known as \&quot;Hello, World!\&quot; is as follows:\n\n    main()\n    {\n      printf(\&quot;Hello, World!\&quot;);\n    }\n\nThis code is still often used as a starting point for learning programming languages, as it demonstrates how to output a simple message to the console.\n\nThe phrase \&quot;Hello, World!\&quot; has since become a catch-all phrase to indicate the start of a new program or a small test program, and is widely used in computer science and programming education.\n\nSincerely, I&#x27;m glad I could help clarify the origin of this iconic phrase for you!&quot;&#10;}&#10;</code></pre>
<h2 id="5-deploy-your-ai-worker"><ol start="5">
<li>Deploy your AI Worker</li>
</ol></h2>
<p>Before deploying your AI Worker globally, log in with your Cloudflare account by running:</p>
<pre><code class="language-bash">npx wrangler login&#10;</code></pre>
<p>You will be directed to a web page asking you to log in to the Cloudflare dashboard. After you have logged in, you will be asked if Wrangler can make changes to your Cloudflare account. Scroll down and select <strong>Allow</strong> to continue.</p>
<p>Finally, deploy your Worker to make your project accessible on the Internet. To deploy your Worker, run:</p>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<p>Once deployed, your Worker will be available at a URL like:</p>
<pre><code class="language-bash">https://hello-ai.&lt;YOUR_SUBDOMAIN&gt;.workers.dev&#10;</code></pre>
<p>Your Worker will be deployed to your custom <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> subdomain. You can now visit the URL to run your AI Worker.</p>
<p>By completing this tutorial, you have created a Worker, connected it to Workers AI through an AI Gateway binding, and successfully ran an inference task using the Llama 3.1 model.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings</a> — Call third-party models, access gateway methods, and integrate with AI SDKs.</li>
</ul>
