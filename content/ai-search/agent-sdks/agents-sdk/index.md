<p>The <a href="/agents/">Cloudflare Agents SDK</a> lets you build stateful AI agents that run on Workers. This guide builds a chat agent that provisions its own AI Search instance, indexes a document, and then searches that content with a tool before it answers.</p>
<p>This guide uses the recommended agent pattern, exposing AI Search's <code>search()</code> to the model as a tool. For more on this pattern, refer to <a href="/agents/tools/ai-search/">AI Search as an agent tool</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3062.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>ai-search-agent</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- ai-search-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- ai-search-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare ai-search-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare ai-search-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest ai-search-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest ai-search-agent" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd ai-search-agent&#10;</code></pre>
<h2 id="2-install-the-agents-sdk-packages"><ol start="2">
<li>Install the Agents SDK packages</li>
</ol></h2>
<p>Install the Agents SDK, the AI SDK, and the Workers AI provider:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents @cloudflare/ai-chat ai workers-ai-provider zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents @cloudflare/ai-chat ai workers-ai-provider zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents @cloudflare/ai-chat ai workers-ai-provider zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents @cloudflare/ai-chat ai workers-ai-provider zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents @cloudflare/ai-chat ai workers-ai-provider zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents @cloudflare/ai-chat ai workers-ai-provider zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents @cloudflare/ai-chat ai workers-ai-provider zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents @cloudflare/ai-chat ai workers-ai-provider zod" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-bind-your-worker-to-ai-search"><ol start="3">
<li>Bind your Worker to AI Search</li>
</ol></h2>
<p>Replace your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> with the following. This adds a <a href="/ai-search/concepts/namespaces/">namespace binding</a> for AI Search, a Workers AI binding for response generation, and the Durable Object that stores chat history for the agent.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3063.md")
</div>
<p>The namespace binding (<code>ai_search_namespaces</code>), not the single-instance <code>ai_search</code> binding, is required because the agent calls <code>create()</code> at runtime. The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instance, since AI Search does not run locally. <code>AIChatAgent</code> persists messages to SQLite, so its class must be listed in <code>new_sqlite_classes</code>.</p>
<h2 id="4-write-the-agent"><ol start="4">
<li>Write the agent</li>
</ol></h2>
<p>Create <code>src/server.ts</code>. The agent provisions an AI Search instance with <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a> enabled the first time it runs, seeds it with a document, and exposes two tools: <code>search_knowledge_base</code> retrieves content, and <code>save_resolution</code> writes new content back.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3064.md")
</div>
<p><code>this.env.AI_SEARCH.get(INSTANCE_NAME)</code> is synchronous and resolves lazily. It does not create the instance, so <code>ensureInstance</code> creates it first. To search several instances in one call, use a namespace-level search with <code>ai_search_options.instance_ids</code>. Refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h3 id="how-the-tools-work">How the tools work</h3>
<p>The <code>search_knowledge_base</code> tool calls <code>search()</code> on the instance. Because the instance indexes both vectors and keywords, retrieval uses hybrid search by default.</p>
<p>The <code>save_resolution</code> tool calls <code>items.upload()</code>, which uploads a document to built-in storage and queues it for indexing. The call returns quickly, and the content becomes searchable once background indexing finishes. Uploading a file with the same name overwrites and re-indexes it.</p>
<h2 id="5-test-it-locally"><ol start="5">
<li>Test it locally</li>
</ol></h2>
<p>Generate types and start the development server:</p>
<pre><code class="language-sh">npx wrangler types&#10;npm run dev&#10;</code></pre>
<p><code>AIChatAgent</code> speaks its chat protocol over a WebSocket, so drive it from a chat client rather than a plain <code>curl</code> request. The quickest way is to point a UI built with the Agents SDK <a href="/agents/communication-channels/chat/chat-agents/"><code>useAgentChat</code></a> hook at your local server.</p>
<p>Send a message such as <code>How do I get started?</code>. On the first message, the agent creates and seeds the instance, so the first response can take a minute or two while the seed document indexes.</p>
<p>You know the integration works when:</p>
<ul>
<li>The <code>wrangler dev</code> logs show a request to <code>/agents/search-agent/&lt;name&gt;</code>, followed by the <code>search_knowledge_base</code> tool running before the reply.</li>
<li>The agent's answer is grounded in the seeded content and cites it, rather than answering generically.</li>
</ul>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<p>Log in with your Cloudflare account:</p>
<pre><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>Deploy your Worker to make it accessible on the Internet:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/tools/ai-search/"><h3 id="card-ai-search-as-an-agent-tool-agents-tools-ai-search">AI Search as an agent tool</h3><p>The agent-side reference for retrieving content with AI Search.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/indexing/hybrid-search/"><h3 id="card-hybrid-search-ai-search-configuration-indexing-hybrid-search">Hybrid search</h3><p>Combine vector and keyword search with configurable fusion.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/how-to/per-tenant-search/"><h3 id="card-per-tenant-search-ai-search-how-to-per-tenant-search">Per-tenant search</h3><p>Give each tenant or agent its own isolated instance.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/instances/workers-binding/"><h3 id="card-instances-workers-binding-ai-search-api-instances-workers-binding">Instances Workers binding</h3><p>Full reference for create, update, list, and delete.</p></a></p>
