<h2 id="background">Background</h2>
<p>A <code>WritableStream</code> is the <code>writable</code> property of a <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a>. On the Workers platform, <code>WritableStream</code> cannot be directly created using the <code>WritableStream</code> constructor.</p>
<p>A typical way to write to a <code>WritableStream</code> is to pipe a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a> to it.</p>
<pre><code class="language-js">readableStream&#10;  .pipeTo(writableStream)&#10;  .then(() =&gt; console.log(&#x27;All data successfully written!&#x27;))&#10;  .catch(e =&gt; console.error(&#x27;Something went wrong!&#x27;, e));&#10;</code></pre>
<p>To write to a <code>WritableStream</code> directly, you must use its writer.</p>
<pre><code class="language-js">const writer = writableStream.getWriter();&#10;writer.write(data);&#10;</code></pre>
<p>Refer to the <a href="/workers/runtime-apis/streams/writablestreamdefaultwriter/">WritableStreamDefaultWriter</a> documentation for further detail.</p>
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>locked</code> boolean</p>
<ul>
<li>A Boolean value to indicate if the writable stream is locked to a writer.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>abort(reasonstringoptional)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Aborts the stream. This method returns a promise that fulfills with a response <code>undefined</code>. <code>reason</code> is an optional human-readable string indicating the reason for cancellation. <code>reason</code> will be passed to the underlying sink’s abort algorithm. If this writable stream is one side of a <a href="/workers/runtime-apis/streams/transformstream/">TransformStream</a>, then its abort algorithm causes the transform’s readable side to become errored with <code>reason</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17065.md")
</aside>
<ul>
<li>
<p><code>getWriter()</code> : WritableStreamDefaultWriter</p>
<ul>
<li>Gets an instance of <code>WritableStreamDefaultWriter</code> and locks the <code>WritableStream</code> to that writer instance.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#ws-model">Writable streams in the WHATWG Streams API specification</a></li>
</ul>
