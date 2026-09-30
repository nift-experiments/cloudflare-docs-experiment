<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13726.md")
</aside>
<p>On <code>@next</code>, the code interpreter is an opt-in extension, not methods on bare <code>Sandbox</code>. Method names match the stable interpreter. You attach once, then call <code>sandbox.interpreter.*</code>. <code>runCode</code> returns plain serializable data across the Worker and Durable Object boundary.</p>
<p>Signatures and types: <a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a>.</p>
<h2 id="attach">Attach</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13727.md")
</div>
<p>Export that class from your Worker. The sidecar provisions on first use.</p>
<h2 id="image">Image</h2>
<table>
<thead>
<tr>
<th>Language</th>
<th>Image</th>
</tr>
</thead>
<tbody>
<tr>
<td>JavaScript / TypeScript</td>
<td>Default sandbox image (or any variant with a JS runtime)</td>
</tr>
<tr>
<td>Python</td>
<td><strong><code>-python</code></strong> image variant</td>
</tr>
</tbody>
</table>
<p>Use the same preview Worker package and container image line. Refer to <a href="/sandbox/configuration/dockerfile/">Dockerfile</a>.</p>
<h2 id="run-code">Run code</h2>
<p>A <strong>context</strong> keeps variables and imports until you delete it or the container is replaced.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13728.md")
</div>
<p>If you omit <code>context</code>, <code>runCode</code> uses a default context for the language (default language: <code>python</code>). Languages: <code>python</code>, <code>javascript</code>, <code>typescript</code>.</p>
<p>For result fields, streaming (<code>runCodeStream</code>), and list/delete context methods, refer to the <a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a>.</p>
<p>Contexts exist only in the <strong>current container</strong>. After stop or replace, create new ones. Refer to <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a></li>
<li><a href="/sandbox/1-0-preview/extensions/">Extensions</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li>Stable guide: <a href="/sandbox/guides/code-execution/">Use code interpreter</a></li>
</ul>
