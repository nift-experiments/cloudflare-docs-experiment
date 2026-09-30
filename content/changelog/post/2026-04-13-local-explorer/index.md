<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 13, 2026</time><h2 id="post-title">Local Explorer for local resource data</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Local Explorer is a browser-based interface and REST API for viewing and editing local resource data during development. It removes the need to write throwaway scripts or dig through <code>.wrangler/state</code> to understand what data your Worker has stored locally.</p>
<p>Local Explorer is available in Wrangler 4.82.1+ and the Cloudflare Vite plugin 1.32.0+. Start a local development session and press <code>e</code> in your terminal, or navigate to <code>/cdn-cgi/local/explorer</code> on your local dev server.</p>
<h4 id="supported-resources">Supported resources</h4>
<p>Local Explorer supports five resource types and works across multiple workers running locally:</p>
<ul>
<li><strong><a href="/kv/">KV</a></strong> — Browse keys, view values and metadata, create, update, and delete key-value pairs.</li>
<li><strong><a href="/r2/">R2</a></strong> — List objects, view metadata, upload files, and delete objects. Supports directory views and multi-select.</li>
<li><strong><a href="/d1/">D1</a></strong> — Browse tables and rows, run arbitrary SQL queries, and edit schemas in a full data studio.</li>
<li><strong><a href="/durable-objects/">Durable Objects</a></strong> (SQLite storage) — Browse individual object SQLite tables, run SQL queries, and edit schemas.</li>
<li><strong><a href="/workflows/">Workflows</a></strong> — List instances, view status and step history, trigger new runs, and pause, resume, restart, or terminate instances.</li>
</ul>
<h4 id="openapi-powered-rest-api">OpenAPI-powered REST API</h4>
<p>Local Explorer exposes a REST API at <code>/cdn-cgi/local/explorer/api</code> that provides programmatic access to the same operations available in the browser. The root endpoint returns an <a href="https://www.openapis.org/">OpenAPI specification</a> describing all available endpoints, parameters, and response formats.</p>
<pre><code class="language-sh">curl http://localhost:8787/cdn-cgi/local/explorer/api&#10;</code></pre>
<p>Point an AI coding agent at <code>/cdn-cgi/local/explorer/api</code> and it can discover and interact with your local resources without manual setup. This enables iterative development loops where an agent can populate test data in KV or D1, inspect Durable Object state, trigger Workflow runs, or upload files to R2.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>
</div></article></div>
