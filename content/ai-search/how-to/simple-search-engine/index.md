<p>This guide builds a search engine that returns the file names matching a query, using the <code>search()</code> method on the <a href="/ai-search/api/search/workers-binding/">Workers binding</a>. You can adapt it to use the <a href="/ai-search/api/search/rest-api/">REST API</a> instead.</p>
<p>For the best results with this pattern:</p>
<ul>
<li>Disable query rewriting so the original user query is matched directly.</li>
<li>Configure your AI Search instance with small chunk sizes (256 tokens is usually enough).</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3003.md")
</div></details>
<p>You also need an AI Search instance that already contains indexed content. To create one and add content, refer to <a href="/ai-search/get-started/">Get started</a>.</p>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>search-engine</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- search-engine</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- search-engine" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare search-engine</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare search-engine" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest search-engine</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest search-engine" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd search-engine&#10;</code></pre>
<h2 id="2-bind-your-worker-to-ai-search"><ol start="2">
<li>Bind your Worker to AI Search</li>
</ol></h2>
<p>Add the following to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3004.md")
</div>
<p>This binds the <code>default</code> <a href="/ai-search/concepts/namespaces/">namespace</a> to <code>env.AI_SEARCH</code>. The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instance, since AI Search does not run locally.</p>
<h2 id="3-add-the-search-code"><ol start="3">
<li>Add the search code</li>
</ol></h2>
<p>Update <code>src/index.ts</code>. This Worker reads a query from the URL, searches your instance, and returns the file name of each matching chunk. Replace <code>my-instance</code> with the name of your instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3005.md")
</div>
<h2 id="4-run-and-deploy"><ol start="4">
<li>Run and deploy</li>
</ol></h2>
<p>Start a local development server, then query it at <code>/?query=your+search+terms</code>:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Log in with your Cloudflare account, then deploy your Worker to make it accessible on the Internet:</p>
<pre><code class="language-sh">npx wrangler login&#10;npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/api/search/workers-binding/"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding">Search Workers binding</h3><p>Full reference for searching and chatting from a Worker.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/query-rewriting/"><h3 id="card-query-rewriting-ai-search-configuration-retrieval-query-rewriting">Query rewriting</h3><p>Control whether AI Search rewrites the query before searching.</p></a></p>
