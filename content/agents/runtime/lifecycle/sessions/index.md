---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/
  description: Persistent conversation storage with tree-structured messages, context blocks, compaction, full-text search, and AI-controllable tools.
  full_title: Sessions · Cloudflare Agents docs
  head_html: <title>Sessions · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Persistent conversation storage with tree-structured messages, context blocks, compaction, full-text search, and AI-controllable tools."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/index.md"><meta property="og:title" content="Sessions · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Persistent conversation storage with tree-structured messages, context blocks, compaction, full-text search, and AI-controllable tools."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/#page","headline":"Sessions \u00b7 Cloudflare Agents docs","description":"Persistent conversation storage with tree-structured messages, context blocks, compaction, full-text search, and AI-controllable tools.","url":"https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/lifecycle/sessions/
  schema: 1
---
<p>The Session API provides persistent conversation storage for agents, with tree-structured messages (inspired by <a href="https://pi.dev">Pi</a>), context blocks, compaction, full-text search, and AI-controllable tools. By default, it uses Durable Object SQLite. External Postgres storage is also available for apps that need shared database access, analytics, or cross-Durable Object queries.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="experimental">Experimental</h3>
@markup("md", "content/.markup/bodies/2365.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2366.md")
</div>
<h2 id="creating-a-session">Creating a session</h2>
<h3 id="builder-api-recommended">Builder API (recommended)</h3>
<p>Use <code>Session.create(agent)</code> with a chainable builder. Context providers without an explicit <code>provider</code> option are auto-wired to SQLite.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2367.md")
</div>
<h3 id="direct-constructor">Direct constructor</h3>
<p>For full control over providers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2368.md")
</div>
<h3 id="builder-methods">Builder methods</h3>
<p>All builder methods return <code>this</code> for chaining. Order does not matter — providers are resolved lazily on first use.</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Session.create(agent)</code></td>
<td>Static factory. <code>agent</code> is any object with a <code>sql</code> tagged template method (your Agent or Durable Object).</td>
</tr>
<tr>
<td><code>.forSession(sessionId)</code></td>
<td>Namespace this session by ID. Required for multi-session isolation when not using <code>SessionManager</code>.</td>
</tr>
<tr>
<td><code>.withContext(label, options?)</code></td>
<td>Add a context block. Refer to <a href="#context-blocks">Context blocks</a>.</td>
</tr>
<tr>
<td><code>.withCachedPrompt(provider?)</code></td>
<td>Enable system prompt persistence. The prompt is frozen on first use and survives hibernation and eviction.</td>
</tr>
<tr>
<td><code>.onCompaction(fn)</code></td>
<td>Register a compaction function. Refer to <a href="#compaction">Compaction</a>.</td>
</tr>
<tr>
<td><code>.compactAfter(tokenThreshold, options?)</code></td>
<td>Auto-compact when estimated token count exceeds the threshold. Requires <code>.onCompaction()</code>. Pass <code>{ tokenCounter }</code> to control how the threshold is measured.</td>
</tr>
<tr>
<td><code>.onCompactionError(handler)</code></td>
<td>Handle errors from automatic compaction. Handler failures are swallowed so message writes remain non-fatal.</td>
</tr>
</tbody>
</table>
<h2 id="messages">Messages</h2>
<p>Messages use the <code>SessionMessage</code> type — a minimal shape with <code>id</code>, <code>role</code>, <code>parts</code>, and optional <code>createdAt</code>. The AI SDK's <code>UIMessage</code> is structurally compatible and can be passed directly. The session stores messages in a tree structure via <code>parent_id</code>, enabling branching conversations.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2369.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2364.md")
</aside>
<h3 id="reading-history">Reading history</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2370.md")
</div>
<h3 id="branching">Branching</h3>
<p>Messages form a tree. When you <code>appendMessage</code> with a <code>parentId</code> that already has children, you create a branch. Use <code>getBranches()</code> to get all child messages branching from a given point:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2371.md")
</div>
<p>This powers features like response regeneration — pass the user message ID to get both the original and regenerated responses. <code>getHistory(leafId)</code> walks the chosen path.</p>
<h2 id="search">Search</h2>
<p>Full-text search over the conversation history using SQLite FTS5:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2372.md")
</div>
<p>SQLite-backed sessions use FTS5 with porter stemming and unicode tokenization. Postgres-backed sessions use the provider's Postgres full-text index. <code>search()</code> throws if the session provider does not support search.</p>
<h2 id="context-blocks">Context blocks</h2>
<p>Context blocks are persistent key-value sections injected into the system prompt. Each block has a <strong>label</strong>, optional <strong>description</strong>, and a <strong>provider</strong> that determines its behavior.</p>
<h3 id="provider-types">Provider types</h3>
<p>There are four provider types, detected by duck-typing:</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Interface</th>
<th>Behavior</th>
<th>AI tool</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ContextProvider</strong></td>
<td><code>get()</code></td>
<td>Read-only block in system prompt</td>
<td>—</td>
</tr>
<tr>
<td><strong>WritableContextProvider</strong></td>
<td><code>get()</code> + <code>set()</code></td>
<td>Writable via AI</td>
<td><code>set_context</code></td>
</tr>
<tr>
<td><strong>SkillProvider</strong></td>
<td><code>get()</code> + <code>load()</code> + <code>set?()</code></td>
<td>On-demand keyed documents. <code>get()</code> returns a metadata listing; <code>load(key)</code> fetches full content.</td>
<td><code>load_context</code>, <code>unload_context</code>, <code>set_context</code></td>
</tr>
<tr>
<td><strong>SearchProvider</strong></td>
<td><code>get()</code> + <code>search()</code> + <code>set?()</code></td>
<td>Full-text searchable entries. <code>get()</code> returns a summary; <code>search(query)</code> runs FTS5.</td>
<td><code>search_context</code>, <code>set_context</code></td>
</tr>
</tbody>
</table>
<h3 id="built-in-providers">Built-in providers</h3>
<p><strong><code>AgentContextProvider</code></strong> — SQLite-backed writable context. This is the default when using the builder without an explicit provider.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2373.md")
</div>
<p><strong><code>R2SkillProvider</code></strong> — Cloudflare R2 bucket for on-demand document loading. Skills are listed in the system prompt as metadata; the model loads full content on demand via <code>load_context</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2374.md")
</div>
<p><strong><code>AgentSearchProvider</code></strong> — SQLite FTS5 searchable context. Entries are indexed and searchable by the model via <code>search_context</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2375.md")
</div>
<h3 id="adding-and-removing-context-at-runtime">Adding and removing context at runtime</h3>
<p>Blocks can be added and removed dynamically after initialization:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2376.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2363.md")
</aside>
<h3 id="reading-and-writing-context">Reading and writing context</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2377.md")
</div>
<h3 id="system-prompt">System prompt</h3>
<p>The system prompt is built from all context blocks with headers and metadata:</p>
<pre tabindex="0"><code class="language-txt">══════════════════════════════════════════════&#10;SOUL (Identity) [readonly]&#10;══════════════════════════════════════════════&#10;You are a helpful assistant.&#10;&#10;══════════════════════════════════════════════&#10;MEMORY (Learned facts) [45% — 495/1100 tokens]&#10;══════════════════════════════════════════════&#10;User likes coffee.&#10;User prefers dark roast.&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2378.md")
</div>
<p>The frozen prompt survives Durable Object hibernation and eviction when <code>withCachedPrompt()</code> is enabled.</p>
<h2 id="ai-tools">AI tools</h2>
<p>Session automatically generates tools based on the provider types of your context blocks. Pass these to your LLM alongside your own tools.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2379.md")
</div>
<h3 id="set-context">set_context</h3>
<p>Generated when any writable block exists. Writes to regular blocks, skill blocks (keyed), or search blocks (keyed). Enforces <code>maxTokens</code> limits.</p>
<h3 id="load-context">load_context</h3>
<p>Generated when any skill block exists. Loads full content by key from a <code>SkillProvider</code>.</p>
<h3 id="unload-context">unload_context</h3>
<p>Generated alongside <code>load_context</code>. Frees context space by unloading a previously loaded skill. The skill remains available for re-loading.</p>
<h3 id="search-context">search_context</h3>
<p>Generated when any search block exists. Full-text search within a searchable context block. Returns top 10 results by FTS5 rank.</p>
<h3 id="session-search">session_search</h3>
<p>Available on <code>SessionManager</code> only. Searches across all sessions.</p>
<h2 id="compaction">Compaction</h2>
<p>Compaction summarizes older messages to keep conversations within token limits. Original messages are preserved in SQLite — the summary is a non-destructive overlay applied at read time.</p>
<h3 id="setup">Setup</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2380.md")
</div>
<h3 id="how-compaction-works">How compaction works</h3>
<ol>
<li><strong>Protect head</strong> — first N messages are never compacted (default 3)</li>
<li><strong>Protect tail</strong> — walk backward from the end, accumulating tokens up to a budget (default 20K tokens)</li>
<li><strong>Align boundaries</strong> — shift boundaries to avoid splitting tool call/result pairs</li>
<li><strong>Summarize middle</strong> — send the middle section to an LLM with a structured format (Topic, Key Points, Current State, Open Items)</li>
<li><strong>Store overlay</strong> — saved in the <code>assistant_compactions</code> table, keyed by <code>fromMessageId</code> and <code>toMessageId</code></li>
<li><strong>Iterative</strong> — on subsequent compactions, the existing summary is passed to the LLM to update rather than replace</li>
</ol>
<p>When <code>getHistory()</code> is called, compaction overlays are applied transparently — the compacted range is replaced by a synthetic summary message.</p>
<h3 id="manual-compaction">Manual compaction</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2381.md")
</div>
<h3 id="auto-compaction">Auto-compaction</h3>
<p>When <code>.compactAfter(threshold)</code> is set, <code>appendMessage()</code> checks the estimated token count after each write. If it exceeds the threshold, <code>compact()</code> is called automatically. Auto-compaction failure is non-fatal — the message is already saved.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2362.md")
</aside>
<p>By default, the estimate includes stored message parts plus the Session-managed frozen system prompt, so context blocks and cached prompts managed by <code>Session</code> contribute to the threshold. It does not include framework-specific prompt additions or tool schema serialization that happen outside <code>Session</code>.</p>
<p>There are two token-counting decisions:</p>
<ul>
<li><code>.compactAfter(threshold, { tokenCounter })</code> controls <strong>when</strong> automatic compaction is triggered after writes.</li>
<li><code>createCompactFunction({ tokenCounter })</code> controls <strong>which</strong> tail messages are protected from summarization. Use this when tool-heavy histories are much larger than the Workers-safe heuristic can estimate.</li>
</ul>
<p>You usually only need to configure one counter. The <code>.compactAfter()</code> counter also flows into <code>createCompactFunction</code>'s boundary walk (via <code>CompactContext</code>) when no explicit <code>createCompactFunction({ tokenCounter })</code> is given, so a single counter drives both &quot;should we compact?&quot; and &quot;what should we compact?&quot;.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2361.md")
</aside>
<p>Use a custom counter when you have model-reported usage or your own tokenizer:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2382.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2360.md")
</aside>
<h2 id="sessionmanager">SessionManager</h2>
<p><code>SessionManager</code> is a registry for multiple named sessions within a single Durable Object. It provides lifecycle management, convenience methods, and cross-session search.</p>
<h3 id="creating-a-sessionmanager">Creating a SessionManager</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2383.md")
</div>
<p>Context blocks, prompt caching, and compaction settings are propagated to all sessions created through the manager. Provider keys are automatically namespaced by session ID.</p>
<h3 id="builder-methods-1">Builder methods</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SessionManager.create(agent)</code></td>
<td>Static factory.</td>
</tr>
<tr>
<td><code>.withContext(label, options?)</code></td>
<td>Add context block template for all sessions.</td>
</tr>
<tr>
<td><code>.withCachedPrompt(provider?)</code></td>
<td>Enable prompt persistence for all sessions.</td>
</tr>
<tr>
<td><code>.onCompaction(fn)</code></td>
<td>Register compaction function for all sessions.</td>
</tr>
<tr>
<td><code>.compactAfter(tokenThreshold, options?)</code></td>
<td>Auto-compact threshold for all sessions. Supports the same <code>tokenCounter</code> option as <code>Session</code>.</td>
</tr>
<tr>
<td><code>.onCompactionError(handler)</code></td>
<td>Handle automatic compaction errors for managed sessions.</td>
</tr>
<tr>
<td><code>.withSearchableHistory(label)</code></td>
<td>Add a cross-session searchable history block. The model can search past conversations from any session.</td>
</tr>
</tbody>
</table>
<h3 id="session-lifecycle">Session lifecycle</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2384.md")
</div>
<h3 id="accessing-sessions">Accessing sessions</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2385.md")
</div>
<h3 id="message-convenience-methods">Message convenience methods</h3>
<p>These delegate to the underlying Session and update the session's <code>updated_at</code> timestamp:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2386.md")
</div>
<h3 id="forking">Forking</h3>
<p>Fork a session at a specific message — copies history up to that point into a new session:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2387.md")
</div>
<h3 id="compaction-helpers">Compaction helpers</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2388.md")
</div>
<p><code>compactAndSplit()</code> creates a new session with a summary message instead of an in-place overlay. The original session is marked with <code>end_reason: &quot;compaction&quot;</code>.</p>
<h3 id="usage-tracking">Usage tracking</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2389.md")
</div>
<h3 id="cross-session-search">Cross-session search</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2390.md")
</div>
<h2 id="custom-providers">Custom providers</h2>
<p>Implement any of the four provider interfaces to plug in your own storage:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2391.md")
</div>
<p>You can also implement <code>SessionProvider</code> to replace the SQLite storage entirely:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2392.md")
</div>
<h2 id="postgres-providers">Postgres providers</h2>
<p>By default, Session storage uses Durable Object SQLite and creates tables lazily. If you need session data in an external Postgres database for cross-agent queries, analytics, or shared storage, use <code>PostgresSessionProvider</code>, <code>PostgresContextProvider</code>, and <code>PostgresSearchProvider</code>.</p>
<p>These providers work with Postgres-compatible databases through <a href="/hyperdrive/">Hyperdrive</a> for connection pooling.</p>
<h3 id="1-create-a-hyperdrive-config"><ol>
<li>Create a Hyperdrive config</li>
</ol></h3>
<p>Create a Hyperdrive config for your Postgres database:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive create my-session-db \&#10;	&#45;-connection-string=&quot;postgresql://user:password@host:port/dbname&quot;&#10;</code></pre>
<p>Then add the Hyperdrive binding to <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2393.md")
</div>
<p>If you know your database region, configure placement close to the database to reduce query latency.</p>
<h3 id="2-create-the-tables"><ol start="2">
<li>Create the tables</li>
</ol></h3>
<p>The Postgres user may not have permission to create tables at runtime. Run the schema once in your database console:</p>
<pre tabindex="0"><code class="language-sql">CREATE TABLE IF NOT EXISTS assistant_messages (&#10;	id TEXT NOT NULL,&#10;	session_id TEXT NOT NULL DEFAULT &#x27;&#x27;,&#10;	parent_id TEXT,&#10;	role TEXT NOT NULL,&#10;	content TEXT NOT NULL,&#10;	text_content TEXT NOT NULL DEFAULT &#x27;&#x27;,&#10;	created_at TIMESTAMPTZ DEFAULT NOW(),&#10;	content_tsv TSVECTOR GENERATED ALWAYS AS (to_tsvector(&#x27;english&#x27;, text_content)) STORED,&#10;	PRIMARY KEY (session_id, id)&#10;);&#10;&#10;CREATE INDEX IF NOT EXISTS idx_assistant_msg_parent&#10;	ON assistant_messages (parent_id);&#10;CREATE INDEX IF NOT EXISTS idx_assistant_msg_session&#10;	ON assistant_messages (session_id);&#10;CREATE INDEX IF NOT EXISTS idx_assistant_msg_fts&#10;	ON assistant_messages USING GIN (content_tsv);&#10;&#10;CREATE TABLE IF NOT EXISTS assistant_compactions (&#10;	id TEXT PRIMARY KEY,&#10;	session_id TEXT NOT NULL DEFAULT &#x27;&#x27;,&#10;	summary TEXT NOT NULL,&#10;	from_message_id TEXT NOT NULL,&#10;	to_message_id TEXT NOT NULL,&#10;	created_at TIMESTAMPTZ DEFAULT NOW()&#10;);&#10;&#10;CREATE TABLE IF NOT EXISTS cf_agents_context_blocks (&#10;	label TEXT PRIMARY KEY,&#10;	content TEXT NOT NULL,&#10;	updated_at TIMESTAMPTZ DEFAULT NOW()&#10;);&#10;&#10;CREATE TABLE IF NOT EXISTS cf_agents_search_entries (&#10;	label TEXT NOT NULL,&#10;	key TEXT NOT NULL,&#10;	content TEXT NOT NULL,&#10;	content_tsv TSVECTOR GENERATED ALWAYS AS (to_tsvector(&#x27;english&#x27;, content)) STORED,&#10;	created_at TIMESTAMPTZ DEFAULT NOW(),&#10;	updated_at TIMESTAMPTZ DEFAULT NOW(),&#10;	PRIMARY KEY (label, key)&#10;);&#10;&#10;CREATE INDEX IF NOT EXISTS idx_search_entries_fts&#10;	ON cf_agents_search_entries USING GIN (content_tsv);&#10;</code></pre>
<h3 id="3-wire-it-up"><ol start="3">
<li>Wire it up</li>
</ol></h3>
<p>Install <code>pg</code>, then create a client from the Hyperdrive connection string and pass it to the Postgres providers:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2394.md")
</div>
<h3 id="behavior-differences">Behavior differences</h3>
<p>When <code>Session.create()</code> receives a <code>SessionProvider</code> instead of a SQLite-backed provider, it skips SQLite auto-wiring:</p>
<ul>
<li><strong>Context blocks need explicit providers.</strong> Each <code>withContext()</code> call that should persist data needs a <code>provider</code> option.</li>
<li><strong><code>withCachedPrompt()</code> needs an explicit provider.</strong> Pass a <code>PostgresContextProvider</code> to persist the frozen system prompt.</li>
<li><strong>Session methods are async.</strong> Use <code>await</code> for reads and writes so the same code works with local SQLite and external storage.</li>
<li><strong>Broadcaster support is skipped.</strong> WebSocket status broadcasts for Session events only work with SQLite-backed sessions.</li>
</ul>
<h3 id="system-prompt-lifecycle">System prompt lifecycle</h3>
<p><code>freezeSystemPrompt()</code> returns the cached prompt from storage. On first call, it loads context blocks from providers, renders the prompt, and persists it. Subsequent calls return the stored value without re-rendering.</p>
<p>Use <code>refreshSystemPrompt()</code> to force reload context blocks, re-render the prompt, and update the stored value.</p>
<h2 id="storage-tables">Storage tables</h2>
<p>By default, storage is in Durable Object SQLite and tables are created lazily on first use. Postgres-backed sessions use the external tables shown in the Postgres providers section.</p>
<table>
<thead>
<tr>
<th>Table</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>assistant_messages</code></td>
<td>Tree-structured messages with <code>id</code>, <code>session_id</code>, <code>parent_id</code>, <code>role</code>, <code>content</code> (JSON), <code>created_at</code></td>
</tr>
<tr>
<td><code>assistant_compactions</code></td>
<td>Compaction overlays with <code>summary</code>, <code>from_message_id</code>, <code>to_message_id</code></td>
</tr>
<tr>
<td><code>assistant_fts</code></td>
<td>FTS5 virtual table for message search (porter stemming, unicode tokenization)</td>
</tr>
<tr>
<td><code>assistant_sessions</code></td>
<td>Session registry (SessionManager only) with <code>name</code>, <code>parent_session_id</code>, <code>model</code>, <code>source</code>, token/cost counters</td>
</tr>
<tr>
<td><code>cf_agents_context_blocks</code></td>
<td>Persistent context block storage (<code>AgentContextProvider</code>)</td>
</tr>
<tr>
<td><code>cf_agents_search_entries</code> / <code>cf_agents_search_fts</code></td>
<td>Searchable context entries and FTS5 index (<code>AgentSearchProvider</code>)</td>
</tr>
</tbody>
</table>
<h2 id="acknowledgments">Acknowledgments</h2>
<ul>
<li>Session's tree-structured messages are inspired by <a href="https://pi.dev">Pi</a>.</li>
<li>Context blocks are inspired by <a href="https://www.letta.com/blog/memory-blocks">Letta AI memory blocks</a>.</li>
<li>Formatting of blocks is inspired by <a href="https://github.com/nousresearch/hermes-agent">Hermes Agent</a>.</li>
</ul>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/harnesses/think/">Think</a> — opinionated chat agent that uses Session for conversation storage via <code>configureSession()</code></li>
<li><a href="/agents/communication-channels/chat/chat-agents/">Chat agents</a> — <code>AIChatAgent</code> with its own message persistence layer</li>
<li><a href="/agents/runtime/lifecycle/state/">Store and sync state</a> — <code>setState()</code> for simpler key-value persistence</li>
</ul>
