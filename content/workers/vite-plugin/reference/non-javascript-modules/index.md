<p>In addition to TypeScript and JavaScript, the following module types are automatically configured to be importable in your Worker code.</p>
<table>
<thead>
<tr>
<th>Module extension</th>
<th>Imported type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.txt</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.html</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.sql</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.bin</code></td>
<td><code>ArrayBuffer</code></td>
</tr>
<tr>
<td><code>.wasm</code>, <code>.wasm?module</code></td>
<td><code>WebAssembly.Module</code></td>
</tr>
</tbody>
</table>
<p>For example, with the following import, <code>text</code> will be a string containing the contents of <code>example.txt</code>:</p>
<pre><code class="language-js">import text from &quot;./example.txt&quot;;&#10;</code></pre>
<p>This is also the basis for importing Wasm, as in the following example:</p>
<pre><code class="language-ts">import wasm from &quot;./example.wasm&quot;;&#10;&#10;// Instantiate Wasm modules in the module scope&#10;const instance = await WebAssembly.instantiate(wasm);&#10;&#10;export default {&#10;	fetch() {&#10;		const result = instance.exports.exported_func();&#10;&#10;		return new Response(result);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17390.md")
</aside>
