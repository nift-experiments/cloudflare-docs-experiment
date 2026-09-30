<p>Read, write, and manage files in the sandbox filesystem. All paths are absolute (e.g., <code>/workspace/app.js</code>).</p>
<h2 id="methods">Methods</h2>
<h3 id="writefile"><code>writeFile()</code></h3>
<p>Write content to a file.</p>
<pre><code class="language-ts">await sandbox.writeFile(path: string, content: string, options?: WriteFileOptions): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>path</code> - Absolute path to the file</li>
<li><code>content</code> - Content to write</li>
<li><code>options</code> (optional):
<ul>
<li><code>encoding</code> - File encoding (<code>&quot;utf-8&quot;</code> or <code>&quot;base64&quot;</code>, default: <code>&quot;utf-8&quot;</code>)</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13663.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="base64-validation">Base64 validation</h3>
@markup("md", "content/.markup/bodies/13662.md")
</aside>
<h4 id="large-files-and-binary-data">Large files and binary data</h4>
<p>When using the <a href="/sandbox/configuration/transport/"><code>rpc</code> transport</a> the <code>writeFile()</code> method supports passing a <code>ReadableStream</code> as the <code>content</code> parameter. This allows binary data and files greater than <a href="/workers/runtime-apis/rpc/#limitations">32 MiB</a> to be written to the sandbox. It replaces the <code>&quot;base64&quot;</code> encoding option.</p>
<pre><code class="language-js">// Requires SANDBOX_TRANSPORT to be &quot;rpc&quot; in wrangler.jsonc&#10;const req = await fetch(&quot;https://example.com/archive.tar.gz&quot;);&#10;await sandbox.writeFile(&#x27;/workspace/archive.tar.gz&#x27;, req.body);&#10;</code></pre>
<h3 id="readfile"><code>readFile()</code></h3>
<p>Read a file from the sandbox. By default returns the content as a string. This is useful for small text files. For larger files and binary data use <code>encoding: &quot;none&quot;</code> to get back a <code>ReadableStream</code> with the file data.</p>
<pre><code class="language-ts">const file = await sandbox.readFile(path: string, options?: ReadFileOptions): Promise&lt;ReadFileResult | ReadFileStreamResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>path</code> - Absolute path to the file</li>
<li><code>options</code> (optional):
<ul>
<li><code>encoding</code> - File encoding (<code>&quot;utf-8&quot;</code>, <code>&quot;base64&quot;</code> or <code>&quot;none&quot;</code>, default: auto-detected from MIME type)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ReadFileResult | ReadFileStreamResult&gt;</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="encoding">Encoding</h3>
@markup("md", "content/.markup/bodies/13661.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13664.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="encoding-behavior">Encoding behavior</h3>
@markup("md", "content/.markup/bodies/13660.md")
</aside>
<h3 id="exists"><code>exists()</code></h3>
<p>Check if a file or directory exists.</p>
<pre><code class="language-ts">const result = await sandbox.exists(path: string): Promise&lt;FileExistsResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>path</code> - Absolute path to check</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;FileExistsResult&gt;</code> with <code>exists</code> boolean</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13665.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="available-on-sessions">Available on sessions</h3>
@markup("md", "content/.markup/bodies/13659.md")
</aside>
<h3 id="mkdir"><code>mkdir()</code></h3>
<p>Create a directory.</p>
<pre><code class="language-ts">await sandbox.mkdir(path: string, options?: MkdirOptions): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>path</code> - Absolute path to the directory</li>
<li><code>options</code> (optional):
<ul>
<li><code>recursive</code> - Create parent directories if needed (default: <code>false</code>)</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13666.md")
</div>
<h3 id="deletefile"><code>deleteFile()</code></h3>
<p>Delete a file.</p>
<pre><code class="language-ts">await sandbox.deleteFile(path: string): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>path</code> - Absolute path to the file</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13667.md")
</div>
<h3 id="renamefile"><code>renameFile()</code></h3>
<p>Rename a file.</p>
<pre><code class="language-ts">await sandbox.renameFile(oldPath: string, newPath: string): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>oldPath</code> - Current file path</li>
<li><code>newPath</code> - New file path</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13668.md")
</div>
<h3 id="movefile"><code>moveFile()</code></h3>
<p>Move a file to a different directory.</p>
<pre><code class="language-ts">await sandbox.moveFile(sourcePath: string, destinationPath: string): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>sourcePath</code> - Current file path</li>
<li><code>destinationPath</code> - Destination path</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13669.md")
</div>
<h3 id="gitcheckout"><code>gitCheckout()</code></h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13658.md")
</aside>
<p>Clone a git repository.</p>
<pre><code class="language-ts">await sandbox.gitCheckout(repoUrl: string, options?: GitCheckoutOptions): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>repoUrl</code> - Git repository URL</li>
<li><code>options</code> (optional):
<ul>
<li><code>branch</code> - Branch to checkout (default: repository default branch)</li>
<li><code>targetDir</code> - Directory to clone into (default: <code>/workspace/{repoName}</code>)</li>
<li><code>depth</code> - Clone depth for shallow clones (e.g., <code>1</code> for latest commit only)</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13670.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/manage-files/">Manage files guide</a> - Detailed guide with best practices</li>
<li><a href="/sandbox/api/commands/">Commands API</a> - Execute commands</li>
</ul>
