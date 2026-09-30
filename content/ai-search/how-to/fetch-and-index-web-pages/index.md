<p>This guide builds a Worker that fetches a single web page's rendered HTML with the <a href="/browser-run/">Browser Run</a> <a href="/browser-run/quick-actions/content-endpoint/"><code>/content</code> endpoint</a> and uploads it to an <a href="/ai-search/">AI Search</a> instance's <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a> using the <a href="/ai-search/api/items/workers-binding/">Items API</a>. AI Search then indexes the page so it is searchable, the same as any other uploaded document. The Worker also exposes a <code>/search</code> endpoint that queries the indexed pages, so one service both indexes and searches.</p>
<h2 id="when-to-use-this-pattern">When to use this pattern</h2>
<p>Use this pattern to index one page, or a small hand-picked set of pages, on demand. To crawl and continuously index an entire site, use the AI Search <a href="/ai-search/configuration/data-source/website/">website data source</a> instead.</p>
<p>Both Browser Run and the AI Search instance are reached through bindings, so a single Worker can fetch a page and index it without a public endpoint in between.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3026.md")
</div></details>
<p>You also need an AI Search instance to upload to. To create one, refer to <a href="/ai-search/get-started/">Get started</a>. This guide uploads to the instance's built-in storage, so the instance does not need an external data source.</p>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>fetch-and-index</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- fetch-and-index</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- fetch-and-index" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare fetch-and-index</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare fetch-and-index" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest fetch-and-index</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest fetch-and-index" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd fetch-and-index&#10;</code></pre>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure Wrangler</li>
</ol></h2>
<p>Add both bindings to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>: a <a href="/browser-run/reference/wrangler/#bindings">browser binding</a> for Browser Run and an <a href="/ai-search/api/items/workers-binding/">AI Search namespace binding</a> for uploads. The <code>/content</code> endpoint runs through the browser binding, so you do not need to install Puppeteer or any other package.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3027.md")
</div>
<p>The browser binding's <code>quickAction</code> method requires a compatibility date of <code>2026-03-24</code> or later, and is not supported in local development without remote mode. Setting <code>remote = true</code> on the browser binding enables remote mode for <code>wrangler dev</code>. The <code>remote</code> option on the AI Search binding proxies uploads to your deployed instance, since AI Search does not run locally.</p>
<h2 id="3-add-the-worker-code"><ol start="3">
<li>Add the Worker code</li>
</ol></h2>
<p>Update <code>src/index.ts</code>. This Worker has two routes: a request with a <code>?url=</code> parameter fetches that page's rendered HTML and indexes it, and a request to <code>/search?q=</code> queries the indexed content. Replace <code>my-instance</code> with the name of your instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3028.md")
</div>
<p>The <code>.html</code> item key tells AI Search to run the content through <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a>, which strips boilerplate such as the header and footer before indexing.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3025.md")
</aside>
<h2 id="4-attach-metadata-for-filtering"><ol start="4">
<li>Attach metadata for filtering</li>
</ol></h2>
<p>This step is optional. Because this Worker controls the upload, you can enrich each page with structured <a href="/ai-search/configuration/indexing/metadata/">metadata</a>, such as its title and section, and then <a href="/ai-search/configuration/retrieval/filtering/">filter searches</a> by those fields. This is something the built-in crawler cannot do on its own.</p>
<p>First, define the custom metadata fields on your instance. If you are creating the instance now, pass them to <code>create</code>:</p>
<pre><code class="language-sh">npx wrangler ai-search create my-instance --type builtin --custom-metadata title:text --custom-metadata section:text&#10;</code></pre>
<p>To add fields to an existing instance, use the dashboard under <strong>Settings</strong>, or the <a href="/ai-search/api/instances/workers-binding/#update"><code>update()</code></a> binding method. An instance supports up to five custom fields, and each field can be a <code>text</code>, <code>number</code>, <code>boolean</code>, or <code>datetime</code> type. Changing the schema re-indexes existing documents.</p>
<p>Next, use the Browser Run <a href="/browser-run/quick-actions/json-endpoint/"><code>/json</code> endpoint</a> to extract those fields from the same page. It runs through the same browser binding and returns structured JSON that matches a schema you provide. In the <code>fetch</code> handler from step 3, after you have the rendered <code>html</code> and before the upload, add:</p>
<pre><code class="language-ts">// Extract structured metadata from the page with the /json endpoint.&#10;// response_format constrains the model to the fields you defined above.&#10;// Treat extraction as best-effort: if it fails, index the page without metadata.&#10;const metadata: Record&lt;string, string&gt; = {};&#10;try {&#10;	const jsonResponse = await env.BROWSER.quickAction(&quot;json&quot;, {&#10;		url: pageUrl.toString(),&#10;		prompt: &quot;Extract the page title and its top-level section.&quot;,&#10;		response_format: {&#10;			type: &quot;json_schema&quot;,&#10;			json_schema: {&#10;				type: &quot;object&quot;,&#10;				properties: {&#10;					title: { type: &quot;string&quot; },&#10;					section: { type: &quot;string&quot; },&#10;				},&#10;				required: [&quot;title&quot;],&#10;			},&#10;		},&#10;	});&#10;&#10;	const extracted = (await jsonResponse.json()) as {&#10;		result?: Record&lt;string, unknown&gt;;&#10;	};&#10;&#10;	// Metadata values must be strings, so coerce each value and drop empty ones.&#10;	for (const [key, value] of Object.entries(extracted.result ?? {})) {&#10;		if (value) metadata[key] = String(value);&#10;	}&#10;} catch {&#10;	// Ignore extraction errors and index the page without metadata.&#10;}&#10;</code></pre>
<p>Then pass <code>metadata</code> in the upload options:</p>
<pre><code class="language-ts">const item = await env.AI_SEARCH.get(INSTANCE_NAME).items.uploadAndPoll(&#10;	itemKey(pageUrl),&#10;	html,&#10;	{ timeoutMs: 60_000, metadata },&#10;);&#10;</code></pre>
<p>Once indexed, you can restrict queries to pages in a given section, for example. Refer to <a href="/ai-search/configuration/retrieval/filtering/">Filtering</a> for the query syntax.</p>
<h2 id="5-run-and-deploy"><ol start="5">
<li>Run and deploy</li>
</ol></h2>
<p>Start a local development server. Because <code>remote = true</code> is set on the browser binding, <code>wrangler dev</code> runs the <code>/content</code> endpoint in remote mode:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Index a page by passing its URL:</p>
<pre><code class="language-sh">curl &quot;http://localhost:8787/?url=https://example.com/&quot;&#10;</code></pre>
<p>The response contains the item key and its status (<code>completed</code> once indexed):</p>
<pre><code class="language-json">{ &quot;key&quot;: &quot;example-com.html&quot;, &quot;status&quot;: &quot;completed&quot; }&#10;</code></pre>
<p>Then query the indexed content through the same Worker's <code>/search</code> endpoint:</p>
<pre><code class="language-sh">curl &quot;http://localhost:8787/search?q=what+is+this+domain+for&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;query&quot;: &quot;what is this domain for&quot;,&#10;	&quot;results&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;example-com.html&quot;,&#10;			&quot;score&quot;: 0.75,&#10;			&quot;text&quot;: &quot;# Example Domain\nThis domain is for use in documentation examples...&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Log in with your Cloudflare account, then deploy your Worker to make it accessible on the Internet:</p>
<pre><code class="language-sh">npx wrangler login&#10;npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/browser-run/quick-actions/content-endpoint/"><h3 id="card-browser-run-content-endpoint-browser-run-quick-actions-content-endpoint">Browser Run /content endpoint</h3><p>Fetch the fully rendered HTML of a page after JavaScript runs, with options for load behavior and blocking.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/items/workers-binding/"><h3 id="card-items-workers-binding-ai-search-api-items-workers-binding">Items Workers binding</h3><p>Full reference for uploading, listing, and deleting documents in built-in storage.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/data-source/website/"><h3 id="card-website-data-source-ai-search-configuration-data-source-website">Website data source</h3><p>Crawl and index a domain you own automatically, following its sitemap.</p></a></p>
