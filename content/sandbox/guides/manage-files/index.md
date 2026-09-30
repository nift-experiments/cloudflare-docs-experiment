<p>This guide shows you how to read, write, organize, and synchronize files in the sandbox filesystem.</p>
<h2 id="path-conventions">Path conventions</h2>
<p>File operations support both absolute and relative paths:</p>
<ul>
<li><code>/workspace</code> - Default working directory for application files</li>
<li><code>/tmp</code> - Temporary files (may be cleared)</li>
<li><code>/home</code> - User home directory</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13405.md")
</div>
<h2 id="write-files">Write files</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13406.md")
</div>
<h2 id="read-files">Read files</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13407.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13404.md")
</aside>
<h2 id="organize-files">Organize files</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13408.md")
</div>
<h2 id="batch-operations">Batch operations</h2>
<p>Write multiple files in parallel:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13409.md")
</div>
<h2 id="check-if-file-exists">Check if file exists</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13410.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Use <code>/workspace</code></strong> - Default working directory for app files</li>
<li><strong>Use absolute paths</strong> - Always use full paths like <code>/workspace/file.txt</code></li>
<li><strong>Batch operations</strong> - Use <code>Promise.all()</code> for multiple independent file writes</li>
<li><strong>Create parent directories</strong> - Use <code>recursive: true</code> when creating nested paths</li>
<li><strong>Handle errors</strong> - Check for <code>FILE_NOT_FOUND</code> errors gracefully</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="directory-doesn-t-exist">Directory doesn't exist</h3>
<p>Create parent directories first:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13411.md")
</div>
<h3 id="binary-file-encoding">Binary file encoding</h3>
<p>Use <code>encoding: &quot;none&quot;</code> (with <code>rpc</code> transport) for binary files:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13412.md")
</div>
<p>For older SDK versions or <code>http</code> transport:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13413.md")
</div>
<h3 id="base64-validation-errors">Base64 validation errors</h3>
<p>When writing with <code>encoding: 'base64'</code>, content must contain only valid base64 characters:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13414.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/files/">Files API reference</a> - Complete method documentation</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands guide</a> - Run file operations with commands</li>
<li><a href="/sandbox/guides/git-workflows/">Git workflows guide</a> - Clone and manage repositories</li>
<li><a href="/sandbox/guides/code-execution/">Code Interpreter guide</a> - Generate and execute code files</li>
</ul>
