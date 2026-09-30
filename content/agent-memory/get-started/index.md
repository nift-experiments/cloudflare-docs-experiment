<p>Add Agent Memory to an agent so it can recall durable context across conversations.</p>
<p>This guide uses the <a href="/agents/">Agents SDK</a> and its <a href="/agents/runtime/lifecycle/sessions/">Session API</a> to expose memory recall as a model-callable tool. The same pattern applies if you use another agent framework: store memories with <code>ingest()</code> or <code>remember()</code>, expose <code>recall()</code> through one of your agent's tools, and use the system prompt to tell the model when to search memory.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1729.md")
</div></details>
<p>You also need access to Agent Memory.</p>
<h2 id="how-agent-memory-works">How agent memory works</h2>
<p>Use <code>recall()</code> when the model needs relevant memory to answer or act. Use <code>ingest()</code> when you have conversation messages and want Agent Memory to extract durable memories automatically. Use <code>remember()</code> when your agent already knows the exact memory to store.</p>
<p>Do not call <code>ingest()</code> after every model turn. Instead, batch ingestion after the user goes idle, when a conversation is compacted, or at another natural checkpoint.</p>
<h2 id="1-create-a-project"><ol>
<li>Create a project</li>
</ol></h2>
<p>Create a Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- memory-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- memory-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare memory-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare memory-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest memory-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest memory-agent" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Move into the project directory:</p>
<pre><code class="language-sh">cd memory-agent&#10;</code></pre>
<p>Install the dependencies used by this guide:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="2-create-a-namespace"><ol start="2">
<li>Create a namespace</li>
</ol></h2>
<p>A <a href="/agent-memory/concepts/namespaces-profiles/">namespace</a> scopes the memory profiles for your application. Create one with Wrangler:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler agent-memory namespace create my-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler agent-memory namespace create my-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler agent-memory namespace create my-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler agent-memory namespace create my-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler agent-memory namespace create my-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler agent-memory namespace create my-agent" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You will use the namespace name, <code>my-agent</code>, in your Worker binding.</p>
<h2 id="3-configure-bindings"><ol start="3">
<li>Configure bindings</li>
</ol></h2>
<p>Add an <code>agent_memory</code> binding to your Wrangler configuration. If you use the Agents SDK, also register your agent Durable Object.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1730.md")
</div>
<p>Generate local TypeScript types for your bindings:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="4-add-memory-recall-as-a-tool"><ol start="4">
<li>Add memory recall as a tool</li>
</ol></h2>
<p>The model cannot use memory just because your application has a memory binding. You need to expose recall through a tool and instruct the model when to call it.</p>
<p>With the Agents SDK <a href="/agents/runtime/lifecycle/sessions/">Session API</a>, add a searchable context provider. Session turns the provider's <code>search()</code> method into a <code>search_context</code> tool for the model.</p>
<p>Create <code>src/server.ts</code> and add the recall setup:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1731.md")
</div>
<p>The system prompt is as important as the tool. It tells the model when to call <code>search_context</code>, when not to call it, and how to treat recalled memory.</p>
<h2 id="5-extract-memories-from-conversation"><ol start="5">
<li>Extract memories from conversation</li>
</ol></h2>
<p>Next, give your agent a way to add durable memories. In a chat agent, the usual path is to store the conversation in Session, then call <code>ingest()</code> after the user goes idle.</p>
<p>Change the <code>agents</code> import and add the AI SDK imports. Keep the <code>Session</code> import from step 4.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1732.md")
</div>
<p>Add the ingestion delay near the top of the file, below the imports:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1733.md")
</div>
<p>Then update <code>ChatAgent</code> with the following shape. The comment marks where to keep the Session setup from step 4.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1734.md")
</div>
<p>Replace the default export with a small test endpoint. Each <code>conversationId</code> maps to a separate Agent instance with its own Session history.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1735.md")
</div>
<p>The ingestion path is <code>scheduleIngest()</code> and <code>runIngest()</code>. Each user message cancels the previous pending ingest and schedules a new one, so Agent Memory processes the conversation after the user goes idle instead of after every agent turn.</p>
<p><code>runIngest()</code> uses a cursor so each batch only includes messages that have not already been ingested. The <code>sessionId</code> groups memories by conversation inside the shared memory profile.</p>
<p>This demo uses one Agent Memory profile, <code>demo-user</code>, across multiple conversations. In production, choose profile names that match your application scope, such as users, teams, tenants, or organizations.</p>
<p>You can also call the ingestion logic from a Session compaction hook. The important constraint is to ingest in batches at natural checkpoints, not after every agent turn. In production, choose an ingest delay that matches your application's user experience.</p>
<h2 id="6-optional-store-explicit-memories-when-needed"><ol start="6">
<li>(Optional) Store explicit memories when needed</li>
</ol></h2>
<p>Automatic ingestion is enough for most apps. If you want the model to store a specific memory immediately, add a server-side tool whose execute function calls <code>remember()</code>.</p>
<p>Use this when the agent already knows the exact memory to store. For example, the model might call a <code>rememberMemory</code> tool after the user says: &quot;Remember that I prefer concise answers.&quot;</p>
<p>If the model can call a memory-write tool, add system prompt instructions that define what is worth remembering and when to ask for confirmation. For many agents, automatic conversation ingestion is simpler and safer than giving the model a direct memory-write tool.</p>
<h2 id="7-test-the-app"><ol start="7">
<li>Test the app</li>
</ol></h2>
<p>Start local development:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Ask the first conversation to remember a durable preference:</p>
<pre><code class="language-bash">curl -X POST &quot;http://localhost:8787/chat&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;conversationId&quot;:&quot;first-chat&quot;,&quot;message&quot;:&quot;I prefer TypeScript examples and concise answers.&quot;}&#x27;&#10;</code></pre>
<p>Wait at least 30 seconds before sending the next request. The code schedules ingestion to run 10 seconds after the user goes idle, and Agent Memory then needs additional time to extract, classify, and index the memories before they are available for recall.</p>
<p>Ask a different conversation a question that depends on durable memory. This request uses a different Session history but the same Agent Memory profile.</p>
<pre><code class="language-bash">curl -X POST &quot;http://localhost:8787/chat&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;conversationId&quot;:&quot;second-chat&quot;,&quot;message&quot;:&quot;What do you know or remember about me and my preferences?&quot;}&#x27;&#10;</code></pre>
<p>The model should call <code>search_context</code>, receive recalled memory from Agent Memory, and use that context in its response. The second conversation has no shared Session history with the first, so any knowledge of user preferences comes from Agent Memory.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agent-memory/concepts/how-agent-memory-works/"><h3 id="card-how-agent-memory-works-agent-memory-concepts-how-agent-memory-works">How Agent Memory works</h3><p>Learn how Agent Memory extracts, stores, and retrieves durable memories.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agent-memory/concepts/namespaces-profiles/"><h3 id="card-namespaces-and-profiles-agent-memory-concepts-namespaces-profiles">Namespaces and profiles</h3><p>Design memory scopes for users, teams, tenants, or organizations.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agent-memory/api/workers-api/"><h3 id="card-workers-api-agent-memory-api-workers-api">Workers API</h3><p>Use <code>ingest()</code>, <code>remember()</code>, <code>recall()</code>, and <code>getSummary()</code> from Workers.</p></a></p>
