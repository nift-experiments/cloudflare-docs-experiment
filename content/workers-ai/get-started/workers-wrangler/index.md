<p>This guide will instruct you through setting up and deploying your first Workers AI project. You will use <a href="/workers/">Workers</a>, a Workers AI binding, and a large language model (LLM) to deploy your first AI-powered application on the Cloudflare global network.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15809.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>You will create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>hello-ai</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- hello-ai</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- hello-ai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare hello-ai</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare hello-ai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest hello-ai</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest hello-ai" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Running <code>npm create cloudflare@latest</code> will prompt you to install the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code> package</a>, and lead you through setup. C3 will also install <a href="/workers/wrangler/">Wrangler</a>, the Cloudflare Developer Platform CLI.</p>
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
<li>A <code>&quot;Hello World&quot;</code> <a href="/workers/get-started/guide/#3-write-code">Worker</a> at <code>src/index.ts</code>.</li>
<li>A <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file.</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd hello-ai&#10;</code></pre>
<h2 id="2-connect-your-worker-to-workers-ai"><ol start="2">
<li>Connect your Worker to Workers AI</li>
</ol></h2>
<p>You must create an AI binding for your Worker to connect to Workers AI. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to interact with resources, like Workers AI, on the Cloudflare Developer Platform.</p>
<p>To bind Workers AI to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15810.md")
</div>
<p>Your binding is <a href="/workers/reference/migrate-to-module-workers/#bindings-in-es-modules-format">available in your Worker code</a> on <a href="/workers/runtime-apis/handlers/fetch/"><code>env.AI</code></a>.</p>
<p>You can also bind Workers AI to a Pages Function. For more information, refer to <a href="/pages/functions/bindings/#workers-ai">Functions Bindings</a>.</p>
<h2 id="3-run-an-inference-task-in-your-worker"><ol start="3">
<li>Run an inference task in your Worker</li>
</ol></h2>
<p>You are now ready to run an inference task in your Worker. In this case, you will use an LLM, <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>gemma-4-26b-a4b-it</code></a>, to answer a question.</p>
<p>Update the <code>index.ts</code> file in your <code>hello-ai</code> application directory with the following code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15811.md")
</div>
<p>Up to this point, you have created an AI binding for your Worker and configured your Worker to execute the Gemma 4 26B A4B model with reasoning disabled. You can now test your project locally before you deploy globally.</p>
<h2 id="4-develop-locally-with-wrangler"><ol start="4">
<li>Develop locally with Wrangler</li>
</ol></h2>
<p>While in your project directory, test Workers AI locally by running <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-local-development-usage-charges">Workers AI local development usage charges</h3>
@markup("md", "content/.markup/bodies/15808.md")
</aside>
<p>You will be prompted to log in after you run <code>wrangler dev</code>. When you run <code>npx wrangler dev</code>, Wrangler will give you a URL (most likely <code>localhost:8787</code>) to review your Worker. After you go to the URL Wrangler provides, the response will have a shape similar to the following example:</p>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;generated id&gt;&quot;,&#10;	&quot;object&quot;: &quot;chat.completion&quot;,&#10;	&quot;created&quot;: 0,&#10;	&quot;model&quot;: &quot;@cf/google/gemma-4-26b-a4b-it&quot;,&#10;	&quot;choices&quot;: [&#10;		{&#10;			&quot;index&quot;: 0,&#10;			&quot;message&quot;: {&#10;				&quot;role&quot;: &quot;assistant&quot;,&#10;				&quot;content&quot;: &quot;&lt;generated response&gt;&quot;,&#10;				&quot;refusal&quot;: null&#10;			},&#10;			&quot;finish_reason&quot;: &quot;stop&quot;,&#10;			&quot;logprobs&quot;: null&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="5-deploy-your-ai-worker"><ol start="5">
<li>Deploy your AI Worker</li>
</ol></h2>
<p>Before deploying your AI Worker globally, log in with your Cloudflare account by running:</p>
<pre><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>You will be directed to a web page asking you to log in to the Cloudflare dashboard. After you have logged in, you will be asked if Wrangler can make changes to your Cloudflare account. Scroll down and select <strong>Allow</strong> to continue.</p>
<p>Finally, deploy your Worker to make your project accessible on the Internet. To deploy your Worker, run:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<pre><code class="language-sh">https://hello-ai.&lt;YOUR_SUBDOMAIN&gt;.workers.dev&#10;</code></pre>
<p>Your Worker will be deployed to your custom <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> subdomain. You can now visit the URL to run your AI Worker.</p>
<p>By finishing this tutorial, you have created a Worker, connected it to Workers AI through an AI binding, and run an inference task using the Gemma 4 26B A4B model.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://discord.cloudflare.com">Cloudflare Developers community on Discord</a> - Submit feature requests, report bugs, and share your feedback directly with the Cloudflare team by joining the Cloudflare Discord server.</li>
<li><a href="/workers-ai/models/">Models</a> - Browse the Workers AI models catalog.</li>
<li><a href="/workers-ai/configuration/ai-sdk">AI SDK</a> - Learn how to integrate with an AI model.</li>
</ul>
