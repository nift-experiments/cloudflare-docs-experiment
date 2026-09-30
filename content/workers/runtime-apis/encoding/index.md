<h2 id="textencoder">TextEncoder</h2>
<h3 id="background">Background</h3>
<p>The <code>TextEncoder</code> takes a stream of code points as input and emits a stream of bytes. Encoding types passed to the constructor are ignored and a UTF-8 <code>TextEncoder</code> is created.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/TextEncoder"><code>TextEncoder()</code></a> returns a newly constructed <code>TextEncoder</code> that generates a byte stream with UTF-8 encoding. <code>TextEncoder</code> takes no parameters and throws no exceptions.</p>
<h3 id="constructor">Constructor</h3>
<pre><code class="language-js">let encoder = new TextEncoder();&#10;</code></pre>
<h3 id="properties">Properties</h3>
<ul>
<li><code>encoder.encoding</code> DOMString read-only
<ul>
<li>The name of the encoder as a string describing the method the <code>TextEncoder</code> uses (always <code>utf-8</code>).</li>
</ul>
</li>
</ul>
<h3 id="methods">Methods</h3>
<ul>
<li>
<p><code>encode(inputUSVString)</code> : Uint8Array</p>
<ul>
<li>Encodes a string input.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="textdecoder">TextDecoder</h2>
<h3 id="background-1">Background</h3>
<p>The <code>TextDecoder</code> interface represents a UTF-8 decoder. Decoders take a stream of bytes as input and emit a stream of code points.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/TextDecoder"><code>TextDecoder()</code></a> returns a newly constructed <code>TextDecoder</code> that generates a code-point stream.</p>
<h3 id="constructor-1">Constructor</h3>
<pre><code class="language-js">let decoder = new TextDecoder();&#10;</code></pre>
<h3 id="properties-1">Properties</h3>
<ul>
<li>
<p><code>decoder.encoding</code> DOMString read-only</p>
<ul>
<li>The name of the decoder that describes the method the <code>TextDecoder</code> uses.</li>
</ul>
</li>
<li>
<p><code>decoder.fatal</code> boolean read-only</p>
<ul>
<li>Indicates if the error mode is fatal.</li>
</ul>
</li>
<li>
<p><code>decoder.ignoreBOM</code> boolean read-only</p>
<ul>
<li>Indicates if the byte-order marker is ignored.</li>
</ul>
</li>
</ul>
<h3 id="methods-1">Methods</h3>
<ul>
<li><code>decode()</code> : DOMString
<ul>
<li>Decodes using the method specified in the <code>TextDecoder</code> object. Learn more at <a href="https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/decode">MDN’s <code>TextDecoder</code> documentation</a>.</li>
</ul>
</li>
</ul>
