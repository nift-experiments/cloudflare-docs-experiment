<h2 id="bindings">Bindings</h2>
<p>Variables and secrets are bound as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	bindings: {&#10;		KEY1: &quot;value1&quot;,&#10;		KEY2: &quot;value2&quot;,&#10;	},&#10;});&#10;</code></pre>
<h2 id="text-and-data-blobs">Text and Data Blobs</h2>
<p>Text and data blobs can be loaded from files. File contents will be read and
bound as <code>string</code>s and <code>ArrayBuffer</code>s respectively.</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	textBlobBindings: { TEXT: &quot;text.txt&quot; },&#10;	dataBlobBindings: { DATA: &quot;data.bin&quot; },&#10;});&#10;</code></pre>
<h2 id="globals">Globals</h2>
<p>Injecting arbitrary globals is not supported by <a href="https://github.com/cloudflare/workerd">workerd</a>. If you're using a service Worker, bindings will be injected as globals, but these must be JSON-serializable.</p>
