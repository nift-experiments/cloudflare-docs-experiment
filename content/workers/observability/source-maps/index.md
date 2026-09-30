<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack">Stack traces</a> help with debugging your code when your application encounters an unhandled exception. Stack traces show you the specific functions that were called, in what order, from which line and file, and with what arguments.</p>
<p>Most JavaScript code is first bundled, often transpiled, and then minified before being deployed to production. This process creates smaller bundles to optimize performance and converts code from TypeScript to Javascript if needed.</p>
<p>Source maps translate compiled and minified code back to the original code that you wrote. Source maps are combined with the stack trace returned by the JavaScript runtime to present you with a stack trace.</p>
<h2 id="source-maps">Source Maps</h2>
<p>To enable source maps, add the following to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16246.md")
</div>
<p>When <code>upload_source_maps</code> is set to <code>true</code>, Wrangler will automatically generate and upload source map files when you run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> or <a href="/workers/wrangler/commands/general/#versions-deploy"><code>wrangler versions deploy</code></a>.
​​</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16245.md")
</aside>
<h2 id="stack-traces">Stack traces</h2>
<p>​​
When your Worker throws an uncaught exception, we fetch the source map and use it to map the stack trace of the exception back to lines of your Worker’s original source code.</p>
<p>You can then view the stack trace when streaming <a href="/workers/observability/logs/real-time-logs/">real-time logs</a> or in <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16244.md")
</aside>
<p>When Cloudflare attempts to remap a stack trace to the Worker's source map, it does so line-by-line, remapping as much as possible. If a line of the stack trace cannot be remapped for any reason, Cloudflare will leave that line of the stack trace unchanged, and continue to the next line of the stack trace.</p>
<h2 id="limits">Limits</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version">Wrangler version</h3>
@markup("md", "content/.markup/bodies/16243.md")
</aside>
<table>
<thead>
<tr>
<th>Description</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum Source Map Size</td>
<td>15 MB gzipped</td>
</tr>
</tbody>
</table>
<h2 id="example">Example</h2>
<p>Consider a simple project. <code>src/index.ts</code> serves as the entrypoint of the application and <code>src/calculator.ts</code> defines a ComplexCalculator class that supports basic arithmetic.</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/16247.md")&#10;&#10;&#10;</pre>
<p>Let's see how source maps can simplify debugging an error in the ComplexCalculator class.</p>
<p><img src="/assets/upstream/images/workers-observability/without-source-map.png" alt="Stack Trace without Source Map remapping" /></p>
<p>With <strong>no source maps uploaded</strong>: notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references <code>js</code> instead of <code>ts</code>.</p>
<p><img src="/assets/upstream/images/workers-observability/with-source-map.png" alt="Stack Trace with Source Map remapping" /></p>
<p>With <strong>source maps uploaded</strong>: all methods reference the correct files and line numbers.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/observability/logs/tail-workers/">Tail Workers</a> - Learn how to attach Tail Workers to transform your logs and send them to HTTP endpoints.</li>
<li><a href="/workers/observability/logs/real-time-logs/">Real-time logs</a> - Learn how to capture Workers logs in real-time.</li>
<li><a href="/workers/runtime-apis/rpc/error-handling/">RPC error handling</a> - Learn how exceptions are handled over RPC (Remote Procedure Call).</li>
</ul>
