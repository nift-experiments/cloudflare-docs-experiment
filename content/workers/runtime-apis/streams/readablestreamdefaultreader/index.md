<h2 id="background">Background</h2>
<p>A reader is used when you want to read from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>, rather than piping its output to a <a href="/workers/runtime-apis/streams/writablestream/"><code>WritableStream</code></a>.</p>
<p>A <code>ReadableStreamDefaultReader</code> is not instantiated via its constructor. Rather, it is retrieved from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>:</p>
<pre><code class="language-js">const { readable, writable } = new TransformStream();&#10;const reader = readable.getReader();&#10;</code></pre>
<hr />
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>reader.closed</code> : Promise</p>
<ul>
<li>A promise indicating if the reader is closed. The promise is fulfilled when the reader stream closes and is rejected if there is an error in the stream.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>read()</code> : Promise</p>
<ul>
<li>A promise that returns the next available chunk of data being passed through the reader queue.</li>
</ul>
</li>
<li>
<p><code>cancel(reasonstringoptional)</code> : void</p>
<ul>
<li>Cancels the stream. <code>reason</code> is an optional human-readable string indicating the reason for cancellation. <code>reason</code> will be passed to the underlying source’s cancel algorithm -- if this readable stream is one side of a <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a>, then its cancel algorithm causes the transform’s writable side to become errored with <code>reason</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17066.md")
</aside>
<ul>
<li>
<p><code>releaseLock()</code> : void</p>
<ul>
<li>Releases the lock on the readable stream. A lock cannot be released if the reader has pending read operations. A <code>TypeError</code> is thrown and the reader remains locked.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#rs-model">Readable streams in the WHATWG Streams API specification</a></li>
</ul>
