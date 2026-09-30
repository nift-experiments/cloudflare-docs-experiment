<p>By default, AI Search uses a Workers AI model to generate responses. To use a model outside of Workers AI, use AI Search for <code>search</code> and pass the retrieved content to a different model for generation. This guide uses an OpenAI model.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3036.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3037.md")
</div></details>
<p>You also need:</p>
<ul>
<li>An AI Search instance that already contains indexed content. To create one and add content, refer to <a href="/ai-search/get-started/">Get started</a>.</li>
<li>An <a href="https://platform.openai.com/api-keys">OpenAI API key</a>.</li>
</ul>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>byo-model</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- byo-model</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- byo-model" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare byo-model</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare byo-model" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest byo-model</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest byo-model" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd byo-model&#10;</code></pre>
<h2 id="2-install-the-ai-sdk-and-openai-provider"><ol start="2">
<li>Install the AI SDK and OpenAI provider</li>
</ol></h2>
<p>Install the <a href="https://sdk.vercel.ai/">AI SDK</a> and its OpenAI provider:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-bind-your-worker-and-set-your-api-key"><ol start="3">
<li>Bind your Worker and set your API key</li>
</ol></h2>
<p>Add the AI Search binding to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3038.md")
</div>
<p>Store your OpenAI API key as a <a href="/workers/configuration/secrets/">secret</a>:</p>
<pre><code class="language-sh">npx wrangler secret put OPENAI_API_KEY&#10;</code></pre>
<p>For local development, add the key to a <code>.dev.vars</code> file in your project root instead:</p>
<pre><code class="language-txt">OPENAI_API_KEY=&quot;&lt;YOUR_OPENAI_API_KEY&gt;&quot;&#10;</code></pre>
<h2 id="4-add-the-code"><ol start="4">
<li>Add the code</li>
</ol></h2>
<p>Update <code>src/index.ts</code>. This Worker searches your instance, formats the retrieved chunks, and passes them to OpenAI to generate an answer. Replace <code>my-instance</code> with the name of your instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3039.md")
</div>
<h2 id="5-run-and-deploy"><ol start="5">
<li>Run and deploy</li>
</ol></h2>
<p>Start a local development server, then query it at <code>/?query=your+search+terms</code>:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Log in with your Cloudflare account, then deploy your Worker to make it accessible on the Internet:</p>
<pre><code class="language-sh">npx wrangler login&#10;npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/models/"><h3 id="card-models-ai-search-configuration-models">Models</h3><p>Use third-party models natively through AI Gateway.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/search/workers-binding/"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding">Search Workers binding</h3><p>Full reference for searching and chatting from a Worker.</p></a></p>
