<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack">Stack traces</a> help with debugging your code when your application encounters an unhandled exception. Stack traces show you the specific functions that were called, in what order, from which line and file, and with what arguments.</p>
<p>Most JavaScript code is first bundled, often transpiled, and then minified before being deployed to production. This process creates smaller bundles to optimize performance and converts code from TypeScript to Javascript if needed.</p>
<p>Source maps translate compiled and minified code back to the original code that you wrote. Source maps are combined with the stack trace returned by the JavaScript runtime to present you with a stack trace.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10939.md")
</aside>
<h2 id="source-maps">Source Maps</h2>
<p>To enable source maps, provide the <code>--upload-source-maps</code> flag to <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a> or add the following to your Pages application's <a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a> if you are using the Pages build environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10940.md")
</div>
<p>When uploading source maps is enabled, Wrangler will automatically generate and upload source map files when you run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a>.</p>
<h2 id="stack-traces">Stack traces</h2>
<p>​​
When your application throws an uncaught exception, we fetch the source map and use it to map the stack trace of the exception back to lines of your application’s original source code.</p>
<p>You can then view the stack trace when streaming <a href="/pages/functions/debugging-and-logging/">real-time logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10938.md")
</aside>
<h2 id="limits">Limits</h2>
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
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/functions/debugging-and-logging/">Real-time logs</a> - Learn how to capture Pages logs in real-time.</li>
</ul>
