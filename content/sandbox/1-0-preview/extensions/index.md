<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13748.md")
</aside>
<p>Extensions add optional capabilities to your <code>Sandbox</code> subclass as nested namespaces (for example <code>sandbox.interpreter.*</code>). They are not free-floating globals on every app.</p>
<h2 id="attach-pattern">Attach pattern</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13749.md")
</div>
<p>Export that class from your Worker. Call extension methods through the nested property from application code.</p>
<h2 id="first-party-extensions">First-party extensions</h2>
<p>The following first-party extensions are available on the preview package:</p>
<table>
<thead>
<tr>
<th>Extension</th>
<th>Package</th>
<th>Docs</th>
</tr>
</thead>
<tbody>
<tr>
<td>Code interpreter</td>
<td><code>@cloudflare/sandbox/interpreter</code></td>
<td><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>, <a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a></td>
</tr>
<tr>
<td>OpenCode</td>
<td><code>@cloudflare/sandbox/opencode</code></td>
<td>Confirm exports in your installed <code>@next</code> version (for example <code>withOpenCode</code> and client/proxy helpers).</td>
</tr>
</tbody>
</table>
<p>For the interpreter, attach once, then use the same method names as the stable package (<code>createCodeContext</code>, <code>runCode</code>, and related calls) on <code>sandbox.interpreter</code>. Python needs the <strong><code>-python</code></strong> image variant. For the full how-to, refer to <a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>.</p>
<h2 id="custom-extensions">Custom extensions</h2>
<p>Application-defined extensions are experimental. Helpers exist under <code>@cloudflare/sandbox/extensions</code>, but preview documentation does not yet cover authoring or publishing a custom extension. Prefer the first-party extensions in the table, or keep any custom code inside your application until a supported authoring guide ships.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a></li>
<li><a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
