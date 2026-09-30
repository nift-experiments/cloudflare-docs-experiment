<h2 id="background">Background</h2>
<p>A transform stream consists of a pair of streams: a writable stream, known as its writable side, and a readable stream, known as its readable side. Writes to the writable side result in new data being made available for reading from the readable side.</p>
<p>Workers currently only implements an identity transform stream, a type of transform stream which forwards all chunks written to its writable side to its readable side, without any changes.</p>
<hr />
<h2 id="constructor">Constructor</h2>
<pre><code class="language-js">let { readable, writable } = new TransformStream();&#10;</code></pre>
<ul>
<li>
<p><code>TransformStream()</code> TransformStream</p>
<ul>
<li>Returns a new identity transform stream.</li>
</ul>
</li>
</ul>
<h2 id="properties">Properties</h2>
<ul>
<li><code>readable</code> ReadableStream
<ul>
<li>An instance of a <code>ReadableStream</code>.</li>
</ul>
</li>
<li><code>writable</code> WritableStream
<ul>
<li>An instance of a <code>WritableStream</code>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="identitytransformstream"><code>IdentityTransformStream</code></h2>
<p>The current implementation of <code>TransformStream</code> in the Workers platform is not current compliant with the <a href="https://streams.spec.whatwg.org/#transform-stream">Streams Standard</a> and we will soon be making changes to the implementation to make it conform with the specification. In preparation for doing so, we have introduced the <code>IdentityTransformStream</code> class that implements behavior identical to the current <code>TransformStream</code> class. This type of stream forwards all chunks of byte data (in the form of <code>TypedArray</code>s) written to its writable side to its readable side, without any changes.</p>
<p>The <code>IdentityTransformStream</code> readable side supports <a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBReader">bring your own buffer (BYOB) reads</a>.</p>
<h3 id="constructor-1">Constructor</h3>
<pre><code class="language-js">let { readable, writable } = new IdentityTransformStream();&#10;</code></pre>
<ul>
<li>
<p><code>IdentityTransformStream()</code> IdentityTransformStream</p>
<ul>
<li>Returns a new identity transform stream.</li>
</ul>
</li>
</ul>
<h3 id="properties-1">Properties</h3>
<ul>
<li><code>readable</code> ReadableStream
<ul>
<li>An instance of a <code>ReadableStream</code>.</li>
</ul>
</li>
<li><code>writable</code> WritableStream
<ul>
<li>An instance of a <code>WritableStream</code>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="fixedlengthstream"><code>FixedLengthStream</code></h2>
<p>The <code>FixedLengthStream</code> is a specialization of <code>IdentityTransformStream</code> that limits the total number of bytes that the stream will passthrough. It is useful primarily because, when using <code>FixedLengthStream</code> to produce either a <code>Response</code> or <code>Request</code>, the fixed length of the stream will be used as the <code>Content-Length</code> header value as opposed to use chunked encoding when using any other type of stream. An error will occur if too many, or too few bytes are written through the stream.</p>
<h3 id="constructor-2">Constructor</h3>
<pre><code class="language-js">let { readable, writable } = new FixedLengthStream(1000);&#10;</code></pre>
<ul>
<li>
<p><code>FixedLengthStream(length)</code> FixedLengthStream</p>
<ul>
<li>Returns a new identity transform stream.</li>
<li><code>length</code> maybe a <code>number</code> or <code>bigint</code> with a maximum value of <code>2^53 - 1</code>.</li>
</ul>
</li>
</ul>
<h3 id="properties-2">Properties</h3>
<ul>
<li><code>readable</code> ReadableStream
<ul>
<li>An instance of a <code>ReadableStream</code>.</li>
</ul>
</li>
<li><code>writable</code> WritableStream
<ul>
<li>An instance of a <code>WritableStream</code>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#transform-stream">Transform Streams in the WHATWG Streams API specification</a></li>
</ul>
