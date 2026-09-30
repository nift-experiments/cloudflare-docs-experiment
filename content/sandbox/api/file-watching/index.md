---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/api/file-watching/
  description: Monitor sandbox filesystem changes in real-time using the Sandbox SDK watch API.
  full_title: File watching · Cloudflare Sandbox SDK docs
  head_html: <title>File watching · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor sandbox filesystem changes in real-time using the Sandbox SDK watch API."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/api/file-watching/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/api/file-watching/index.md"><meta property="og:title" content="File watching · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor sandbox filesystem changes in real-time using the Sandbox SDK watch API."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/api/file-watching/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/api/file-watching/#page","headline":"File watching \u00b7 Cloudflare Sandbox SDK docs","description":"Monitor sandbox filesystem changes in real-time using the Sandbox SDK watch API.","url":"https://developers.cloudflare.com/sandbox/api/file-watching/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/api/file-watching/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13676.md")
</aside>
<p>Monitor filesystem changes in real-time using Linux's native inotify system. The <code>watch()</code> method returns a Server-Sent Events (SSE) stream of file change events that you consume with <code>parseSSEStream()</code>.</p>
<h2 id="methods">Methods</h2>
<h3 id="watch"><code>watch()</code></h3>
<p>Watch a directory for filesystem changes. Returns an SSE stream of events.</p>
<pre tabindex="0"><code class="language-ts">const stream = await sandbox.watch(path: string, options?: WatchOptions): Promise&lt;ReadableStream&lt;Uint8Array&gt;&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>path</code> - Absolute path or relative to <code>/workspace</code> (for example, <code>/app/src</code> or <code>src</code>)</li>
<li><code>options</code> (optional):
<ul>
<li><code>recursive</code> - Watch subdirectories recursively (default: <code>true</code>)</li>
<li><code>include</code> - Glob patterns to include (for example, <code>['*.ts', '*.js']</code>). Cannot be used together with <code>exclude</code>.</li>
<li><code>exclude</code> - Glob patterns to exclude (default: <code>['.git', 'node_modules', '.DS_Store']</code>). Cannot be used together with <code>include</code>.</li>
<li><code>sessionId</code> - Session to run the watch in (if omittied, will use the default session unless <code>enableDefaultSession</code> is set to false)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ReadableStream&lt;Uint8Array&gt;&gt;</code> — an SSE stream of <code>FileWatchSSEEvent</code> objects</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13677.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13675.md")
</aside>
<h2 id="types">Types</h2>
<h3 id="filewatchsseevent"><code>FileWatchSSEEvent</code></h3>
<p>Union type of all SSE events emitted by the watch stream.</p>
<pre tabindex="0"><code class="language-ts">type FileWatchSSEEvent =&#10;	| { type: &quot;watching&quot;; path: string; watchId: string }&#10;	| {&#10;			type: &quot;event&quot;;&#10;			eventType: FileWatchEventType;&#10;			path: string;&#10;			isDirectory: boolean;&#10;			timestamp: string;&#10;	  }&#10;	| { type: &quot;error&quot;; error: string }&#10;	| { type: &quot;stopped&quot;; reason: string };&#10;</code></pre>
<ul>
<li><strong><code>watching</code></strong> — Emitted once when the watch is established. Contains the <code>watchId</code> and the <code>path</code> being watched.</li>
<li><strong><code>event</code></strong> — Emitted for each filesystem change. Contains the <code>eventType</code>, the <code>path</code> that changed, and whether it <code>isDirectory</code>.</li>
<li><strong><code>error</code></strong> — Emitted when the watch encounters an error.</li>
<li><strong><code>stopped</code></strong> — Emitted when the watch is stopped, with a <code>reason</code>.</li>
</ul>
<h3 id="filewatcheventtype"><code>FileWatchEventType</code></h3>
<p>Types of filesystem changes that can be detected.</p>
<pre tabindex="0"><code class="language-ts">type FileWatchEventType =&#10;	| &quot;create&quot;&#10;	| &quot;modify&quot;&#10;	| &quot;delete&quot;&#10;	| &quot;move_from&quot;&#10;	| &quot;move_to&quot;&#10;	| &quot;attrib&quot;;&#10;</code></pre>
<ul>
<li><strong><code>create</code></strong> — File or directory was created</li>
<li><strong><code>modify</code></strong> — File content changed</li>
<li><strong><code>delete</code></strong> — File or directory was deleted</li>
<li><strong><code>move_from</code></strong> — File or directory was moved away (source of a rename/move)</li>
<li><strong><code>move_to</code></strong> — File or directory was moved here (destination of a rename/move)</li>
<li><strong><code>attrib</code></strong> — File or directory attributes changed (permissions, timestamps)</li>
</ul>
<h3 id="watchoptions"><code>WatchOptions</code></h3>
<p>Configuration options for watching directories.</p>
<pre tabindex="0"><code class="language-ts">interface WatchOptions {&#10;	/** Watch subdirectories recursively (default: true) */&#10;	recursive?: boolean;&#10;	/** Glob patterns to include. Cannot be used together with `exclude`. */&#10;	include?: string[];&#10;	/** Glob patterns to exclude. Cannot be used together with `include`. Default: [&#x27;.git&#x27;, &#x27;node_modules&#x27;, &#x27;.DS_Store&#x27;] */&#10;	exclude?: string[];&#10;	/** Session to run the watch in. If omitted, the sandbox&#x27;s implicit execution mode is used. */&#10;	sessionId?: string;&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="mutual-exclusivity">Mutual exclusivity</h3>
@markup("md", "content/.markup/bodies/13674.md")
</aside>
<h3 id="parsessestream"><code>parseSSEStream()</code></h3>
<p>Converts a <code>ReadableStream&lt;Uint8Array&gt;</code> into a typed <code>AsyncGenerator</code> of events. Accepts an optional <code>AbortSignal</code> to cancel the stream.</p>
<pre tabindex="0"><code class="language-ts">function parseSSEStream&lt;T&gt;(&#10;	stream: ReadableStream&lt;Uint8Array&gt;,&#10;	signal?: AbortSignal,&#10;): AsyncGenerator&lt;T&gt;;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>stream</code> — The SSE stream returned by <code>watch()</code></li>
<li><code>signal</code> (optional) — An <code>AbortSignal</code> to cancel the stream. When aborted, the reader is cancelled which propagates cleanup to the server.</li>
</ul>
<p>Aborting the signal is the recommended way to stop a watch from outside the consuming loop:</p>
<pre tabindex="0"><code class="language-ts">const controller = new AbortController();&#10;&#10;// Cancel after 60 seconds&#10;setTimeout(() =&gt; controller.abort(), 60_000);&#10;&#10;for await (const event of parseSSEStream&lt;FileWatchSSEEvent&gt;(&#10;	stream,&#10;	controller.signal,&#10;)) {&#10;	// process events&#10;}&#10;</code></pre>
<h2 id="glob-pattern-support">Glob pattern support</h2>
<p>The <code>include</code> and <code>exclude</code> options accept a limited set of glob tokens for predictable matching:</p>
<table>
<thead>
<tr>
<th>Token</th>
<th>Meaning</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*</code></td>
<td>Match any characters within a path segment</td>
<td><code>*.ts</code> matches <code>index.ts</code></td>
</tr>
<tr>
<td><code>**</code></td>
<td>Match across directory boundaries</td>
<td><code>**/*.test.ts</code></td>
</tr>
<tr>
<td><code>?</code></td>
<td>Match a single character</td>
<td><code>?.js</code> matches <code>a.js</code></td>
</tr>
</tbody>
</table>
<p>Character classes (<code>[abc]</code>), brace expansion (<code>{a,b}</code>), and backslash escapes are not supported. Patterns containing these tokens are rejected with a validation error.</p>
<h2 id="notes">Notes</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="deterministic-readiness">Deterministic readiness</h3>
@markup("md", "content/.markup/bodies/13673.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="container-lifecycle">Container lifecycle</h3>
@markup("md", "content/.markup/bodies/13672.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="path-requirements">Path requirements</h3>
@markup("md", "content/.markup/bodies/13671.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/file-watching/">Watch filesystem changes guide</a> — Patterns, best practices, and real-world examples</li>
<li><a href="/sandbox/guides/manage-files/">Manage files guide</a> — File operations</li>
</ul>
