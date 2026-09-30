<p>This guide shows you how to monitor filesystem changes in real-time using the Sandbox SDK's file watching API. File watching is useful for building development tools, automated workflows, and applications that react to file changes as they happen.</p>
<p>The <code>watch()</code> method returns an SSE (Server-Sent Events) stream that you consume with <code>parseSSEStream()</code>. Each event in the stream describes a filesystem change.</p>
<h2 id="basic-file-watching">Basic file watching</h2>
<p>Start by watching a directory for any changes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13427.md")
</div>
<p>The stream emits four lifecycle event types:</p>
<ul>
<li><strong><code>watching</code></strong> — Watch established, includes the <code>watchId</code></li>
<li><strong><code>event</code></strong> — A filesystem change occurred</li>
<li><strong><code>error</code></strong> — The watch encountered an error</li>
<li><strong><code>stopped</code></strong> — The watch was stopped</li>
</ul>
<p>Filesystem change events (<code>event.eventType</code>) include:</p>
<ul>
<li><strong><code>create</code></strong> — File or directory was created</li>
<li><strong><code>modify</code></strong> — File content changed</li>
<li><strong><code>delete</code></strong> — File or directory was removed</li>
<li><strong><code>move_from</code></strong> / <strong><code>move_to</code></strong> — File or directory was moved or renamed</li>
<li><strong><code>attrib</code></strong> — File attributes changed (permissions, timestamps)</li>
</ul>
<h2 id="filter-by-file-type">Filter by file type</h2>
<p>Use <code>include</code> patterns to watch only specific file types:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13428.md")
</div>
<p>Common include patterns:</p>
<ul>
<li><code>*.ts</code> — TypeScript files</li>
<li><code>*.js</code> — JavaScript files</li>
<li><code>*.json</code> — JSON configuration files</li>
<li><code>*.md</code> — Markdown documentation</li>
<li><code>package*.json</code> — Package files specifically</li>
</ul>
<h2 id="exclude-directories">Exclude directories</h2>
<p>Use <code>exclude</code> patterns to skip certain directories or files:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13429.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="default-exclusions">Default exclusions</h3>
@markup("md", "content/.markup/bodies/13426.md")
</aside>
<h2 id="build-responsive-development-tools">Build responsive development tools</h2>
<h3 id="auto-rebuild-on-changes">Auto-rebuild on changes</h3>
<p>Trigger builds automatically when source files are modified:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13430.md")
</div>
<h3 id="auto-run-tests-on-change">Auto-run tests on change</h3>
<p>Re-run tests when test files are modified:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13431.md")
</div>
<h3 id="incremental-indexing">Incremental indexing</h3>
<p>Re-index only changed files instead of rescanning an entire directory tree:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13432.md")
</div>
<h2 id="advanced-patterns">Advanced patterns</h2>
<h3 id="process-events-with-a-helper-function">Process events with a helper function</h3>
<p>Extract event processing into a reusable function that handles stream lifecycle:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13433.md")
</div>
<h3 id="debounced-file-operations">Debounced file operations</h3>
<p>Avoid excessive operations by collecting changes before processing:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13434.md")
</div>
<h3 id="watch-with-non-recursive-mode">Watch with non-recursive mode</h3>
<p>Watch only the top level of a directory, without descending into subdirectories:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13435.md")
</div>
<h2 id="stop-a-watch">Stop a watch</h2>
<p>The stream ends naturally when the container sleeps or shuts down. There are two ways to stop a watch early:</p>
<h3 id="use-an-abortcontroller">Use an AbortController</h3>
<p>Pass an <code>AbortSignal</code> to <code>parseSSEStream</code>. Aborting the signal cancels the stream reader, which propagates cleanup to the server. This is the recommended approach when you need to cancel the watch from outside the consuming loop:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13436.md")
</div>
<h3 id="break-out-of-the-loop">Break out of the loop</h3>
<p>Breaking out of the <code>for await</code> loop also cancels the stream:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13437.md")
</div>
<h2 id="best-practices">Best practices</h2>
<h3 id="use-server-side-filtering">Use server-side filtering</h3>
<p>Filter with <code>include</code> or <code>exclude</code> patterns rather than filtering events in JavaScript. Server-side filtering happens at the inotify level, which reduces the number of events sent over the network.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13425.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13438.md")
</div>
<h3 id="handle-errors-in-event-processing">Handle errors in event processing</h3>
<p>Errors in your event handler do not stop the watch stream. Wrap handler logic in <code>try...catch</code> to prevent unhandled exceptions:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13439.md")
</div>
<h3 id="ensure-directories-exist-before-watching">Ensure directories exist before watching</h3>
<p>Watching a non-existent path returns an error. Verify the path exists before starting a watch:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13440.md")
</div>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="high-cpu-usage">High CPU usage</h3>
<p>If watching large directories causes performance issues:</p>
<ol>
<li>Use specific <code>include</code> patterns instead of watching everything</li>
<li>Exclude large directories like <code>node_modules</code> and <code>dist</code></li>
<li>Watch specific subdirectories instead of the entire project</li>
<li>Use <code>recursive: false</code> for shallow monitoring</li>
</ol>
<h3 id="path-not-found-errors">Path not found errors</h3>
<p>All paths must exist and resolve to within <code>/workspace</code>. Relative paths are resolved from <code>/workspace</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="container-lifecycle">Container lifecycle</h3>
@markup("md", "content/.markup/bodies/13424.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/file-watching/">File Watching API reference</a> — Complete API documentation and types</li>
<li><a href="/sandbox/guides/manage-files/">Manage files guide</a> — File operations</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> — Long-running processes</li>
<li><a href="/sandbox/guides/streaming-output/">Stream output guide</a> — Real-time output handling</li>
</ul>
