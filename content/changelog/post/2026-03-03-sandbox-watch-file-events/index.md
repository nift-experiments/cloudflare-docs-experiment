<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 3, 2026</time><h2 id="post-title">Real-time file watching in Sandboxes</h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> now support real-time filesystem watching via <code>sandbox.watch()</code>. The method returns a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events">Server-Sent Events</a> stream backed by native inotify, so your Worker receives <code>create</code>, <code>modify</code>, <code>delete</code>, and <code>move</code> events as they happen inside the container.</p>
<h4 id="sandbox-watch-path-options"><code>sandbox.watch(path, options)</code></h4>
<p>Pass a directory path and optional filters. The returned stream is a standard <code>ReadableStream</code> you can proxy directly to a browser client or consume server-side.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17650.md")</div>
<h4 id="server-side-consumption-with-parsessestream">Server-side consumption with <code>parseSSEStream</code></h4>
<p>Use <code>parseSSEStream</code> to iterate over events inside a Worker without forwarding them to a client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17651.md")</div>
<p>Each event includes a <code>type</code> field (<code>create</code>, <code>modify</code>, <code>delete</code>, or <code>move</code>) and the affected <code>path</code>. Move events also include a <code>from</code> field with the original path.</p>
<h4 id="options">Options</h4>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>recursive</code></td>
<td><code>boolean</code></td>
<td>Watch subdirectories. Defaults to <code>false</code>.</td>
</tr>
<tr>
<td><code>include</code></td>
<td><code>string[]</code></td>
<td>Glob patterns to filter events. Omit to receive all events.</td>
</tr>
</tbody>
</table>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
<p>For full API details, refer to the <a href="/sandbox/api/file-watching/">Sandbox file watching reference</a>.</p>
</div></article></div>
