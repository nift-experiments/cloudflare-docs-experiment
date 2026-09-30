<p>The <a href="https://sdk.vercel.ai/">Vercel AI SDK</a> is a TypeScript toolkit for building applications with large language models. The <a href="https://www.npmjs.com/package/ai-search-provider"><code>ai-search-provider</code></a> package connects AI Search to the AI SDK, so you can generate responses grounded in your indexed content, retrieve chunks, and manage documents from the same API.</p>
<p>This guide builds a Worker that creates an AI Search instance, uploads and indexes a document, and then queries it with the AI SDK.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3054.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>ai-search-ai-sdk</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- ai-search-ai-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- ai-search-ai-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare ai-search-ai-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare ai-search-ai-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest ai-search-ai-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest ai-search-ai-sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd ai-search-ai-sdk&#10;</code></pre>
<h2 id="2-install-the-ai-sdk-and-provider"><ol start="2">
<li>Install the AI SDK and provider</li>
</ol></h2>
<p>Install the AI SDK and the AI Search provider. The provider requires AI SDK v6 (<code>ai@^6</code>):</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i ai ai-search-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i ai ai-search-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add ai ai-search-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add ai ai-search-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add ai ai-search-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add ai ai-search-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add ai ai-search-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add ai ai-search-provider" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-bind-your-worker-to-ai-search"><ol start="3">
<li>Bind your Worker to AI Search</li>
</ol></h2>
<p>Create a binding between your Worker and AI Search. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Worker to interact with resources on the Cloudflare Developer Platform.</p>
<p>Add the following to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3055.md")
</div>
<p>This binds the <code>default</code> <a href="/ai-search/concepts/namespaces/">namespace</a> to <code>env.AI_SEARCH</code>. The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instance, since AI Search does not run locally. The <code>ai_search_namespaces</code> binding requires a <code>compatibility_date</code> of <code>2026-03-27</code> or later, which new C3 projects already satisfy.</p>
<h2 id="4-create-an-instance-and-index-content"><ol start="4">
<li>Create an instance and index content</li>
</ol></h2>
<p>Add a <code>/setup</code> route that creates an instance and uploads a document. Enable <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a> at creation by setting <code>index_method</code> to index both vectors and keywords.</p>
<p>The <code>create()</code> method is on the namespace binding (<code>env.AI_SEARCH</code>), not on the provider client. Creating an instance that already exists throws, so the following code creates it and, on the next run, updates it instead.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3056.md")
</div>
<p><code>AiSearchNamespace</code> is an ambient type available after you run <code>wrangler types</code>.</p>
<h2 id="5-query-your-instance"><ol start="5">
<li>Query your instance</li>
</ol></h2>
<p>There are three ways to query your instance from the AI SDK. Pick the one that fits your application:</p>
<ul>
<li><a href="#generate-a-response">Generate a response</a> returns the complete answer in one call.</li>
<li><a href="#stream-a-response">Stream a response</a> sends tokens as they are generated, which suits long answers and chat interfaces.</li>
<li><a href="#search-as-a-tool">Search as a tool</a> lets the model decide when to search, which is what you want in an agent.</li>
</ul>
<h3 id="generate-a-response">Generate a response</h3>
<p>Pass <code>instance.chat()</code> to <code>generateText</code>, and AI Search retrieves relevant content and generates a response in one call.</p>
<p>Replace the query placeholder in your <code>fetch</code> handler with the following:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3057.md")
</div>
<p>AI Search returns the retrieved chunks as AI SDK source parts in <code>sources</code>, so you can cite them alongside the generated text. Because the instance indexes both vectors and keywords, <code>retrieval_type: &quot;hybrid&quot;</code> uses both.</p>
<h3 id="stream-a-response">Stream a response</h3>
<p>For longer responses, use <code>streamText</code> instead of <code>generateText</code>. AI Search emits the retrieved chunks as source parts before the first text part.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3058.md")
</div>
<p><code>toTextStreamResponse()</code> sends the generated text and drops the sources. To stream the retrieved chunks as well, return a UI message stream with <code>sendSources</code> enabled, or read <code>result.fullStream</code> directly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3059.md")
</div>
<h3 id="search-as-a-tool">Search as a tool</h3>
<p>With <code>chat()</code>, AI Search searches your instance on every request. To let the model decide when to search instead, expose <code>instance.search()</code> as an AI SDK <a href="https://sdk.vercel.ai/docs/foundations/tools">tool</a> and pass it to a model that supports function calling, such as a <a href="/workers-ai/">Workers AI</a> model. This is the pattern to use in an agent, where the model chooses between searching and other tools.</p>
<p>Install the Workers AI provider and Zod. Use version 3 of <code>workers-ai-provider</code>: the latest version 4 requires AI SDK v7, but <code>ai-search-provider</code> requires v6, so npm fails to install them together.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i workers-ai-provider@^3 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i workers-ai-provider@^3 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add workers-ai-provider@^3 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add workers-ai-provider@^3 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add workers-ai-provider@^3 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add workers-ai-provider@^3 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add workers-ai-provider@^3 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add workers-ai-provider@^3 zod" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add a Workers AI binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3060.md")
</div>
<p>Then define a search tool. The model calls it when it needs to retrieve content:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3061.md")
</div>
<h2 id="6-test-it-locally"><ol start="6">
<li>Test it locally</li>
</ol></h2>
<p>Before you deploy, confirm the whole flow works against your instance with <code>wrangler dev</code>, which proxies the remote AI Search binding. The output below is from the <a href="#generate-a-response">generate a response</a> option.</p>
<p>Start a local development server:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>First, index the sample document by visiting <code>/setup</code>:</p>
<pre><code class="language-sh">curl http://localhost:8787/setup&#10;</code></pre>
<p>The first <code>/setup</code> can take a minute or two while the document indexes. When it finishes, you get back the item key and a <code>completed</code> status:</p>
<pre><code class="language-json">{ &quot;key&quot;: &quot;caching.md&quot;, &quot;status&quot;: &quot;completed&quot; }&#10;</code></pre>
<p>Then query the instance:</p>
<pre><code class="language-sh">curl &quot;http://localhost:8787/?q=How+does+caching+work%3F&quot;&#10;</code></pre>
<p>A working integration returns generated <code>text</code> grounded in your document, along with a <code>sources</code> array referencing the file it retrieved (fields trimmed):</p>
<pre><code class="language-json">{&#10;	&quot;text&quot;: &quot;Cloudflare caches static assets at the edge...&quot;,&#10;	&quot;sources&quot;: [{ &quot;sourceType&quot;: &quot;url&quot;, &quot;url&quot;: &quot;caching.md&quot; }]&#10;}&#10;</code></pre>
<p>If <code>sources</code> comes back empty, the document has not finished indexing yet. Run <code>/setup</code> again, then retry the query.</p>
<h2 id="7-deploy"><ol start="7">
<li>Deploy</li>
</ol></h2>
<p>Log in with your Cloudflare account:</p>
<pre><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>Deploy your Worker to make it accessible on the Internet:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="considerations">Considerations</h2>
<ul>
<li>The chat model is text-only. File and image message parts are not supported.</li>
<li>Generation options such as <code>temperature</code> and <code>maxOutputTokens</code> are passed through to the instance's generation model. <code>maxOutputTokens</code> truncates the response and sets <code>finishReason</code> to <code>&quot;length&quot;</code>. If a model ignores an option, the result's <code>warnings</code> array stays empty, so an unsupported option fails silently.</li>
<li>AI Search uses the generation model configured on the instance by default. Pass <code>instance.chat({ model: &quot;...&quot; })</code> to override it per request.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/indexing/hybrid-search/"><h3 id="card-hybrid-search-ai-search-configuration-indexing-hybrid-search">Hybrid search</h3><p>Combine vector and keyword search with configurable fusion.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/instances/workers-binding/"><h3 id="card-instances-workers-binding-ai-search-api-instances-workers-binding">Instances Workers binding</h3><p>Full reference for create, update, list, and delete.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/search/workers-binding/"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding">Search Workers binding</h3><p>Full reference for searching and chatting from a Worker.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/agent-sdks/agents-sdk/"><h3 id="card-agents-sdk-ai-search-agent-sdks-agents-sdk">Agents SDK</h3><p>Build a stateful chat agent that searches your instance.</p></a></p>
