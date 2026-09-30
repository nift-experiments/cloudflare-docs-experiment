<h2 id="background">Background</h2>
<p><code>BYOB</code> is an abbreviation of bring your own buffer. A <code>ReadableStreamBYOBReader</code> allows reading into a developer-supplied buffer, thus minimizing copies.</p>
<p>An instance of <code>ReadableStreamBYOBReader</code> is functionally identical to <a href="/workers/runtime-apis/streams/readablestreamdefaultreader/"><code>ReadableStreamDefaultReader</code></a> with the exception of the <code>read</code> method.</p>
<p>A <code>ReadableStreamBYOBReader</code> is not instantiated via its constructor. Rather, it is retrieved from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>:</p>
<pre><code class="language-js">const { readable, writable } = new TransformStream();&#10;const reader = readable.getReader({ mode: &#x27;byob&#x27; });&#10;</code></pre>
<hr />
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>read(bufferArrayBufferView)</code> : Promise&lt;ReadableStreamBYOBReadResult&gt;</p>
<ul>
<li>Returns a promise with the next available chunk of data read into a passed-in buffer.</li>
</ul>
</li>
<li>
<p><code>readAtLeast(minElements, bufferArrayBufferView)</code> : Promise&lt;ReadableStreamBYOBReadResult&gt;</p>
<ul>
<li>
<p>Returns a promise with the next available chunk of data read into a passed-in buffer. The promise will not resolve until at least <code>minElements</code> elements have been read.  The element size is determined by <code>bufferArrayBufferView</code>, for example 4 bytes per element for a <code>Uint32Array</code>. However, fewer than <code>minElements</code> elements may be returned if the end of the stream is reached or the underlying stream is closed. Specifically:</p>
<ul>
<li>If <code>minElements</code> or more elements are available, the promise resolves with <code>{ value: &lt;buffer view sized to bytes read&gt;, done: false }</code>.</li>
<li>If the stream ends after some data has been read but fewer than <code>minElements</code> elements, the promise resolves with the partial data: <code>{ value: &lt;buffer view sized to bytes actually read&gt;, done: false }</code>. The next call to <code>read</code> or <code>readAtLeast</code> will then return <code>{ value: undefined, done: true }</code>.</li>
<li>If the stream ends with zero bytes available (that is, the stream is already at EOF), the promise resolves with <code>{ value: &lt;zero-length view&gt;, done: true }</code>.</li>
<li>If the stream errors, the promise rejects.</li>
<li><code>minElements</code> must be at least 1, and <code>minElements * elementSize</code> must not exceed the byte length of <code>bufferArrayBufferView</code>, or the promise rejects with a <code>TypeError</code>. For a <code>Uint8Array</code>, element size is 1, so <code>minElements</code> is effectively a byte count.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="common-issues">Common issues</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17067.md")
</aside>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#byob-readers">Background about BYOB readers in the Streams API WHATWG specification</a></li>
</ul>
