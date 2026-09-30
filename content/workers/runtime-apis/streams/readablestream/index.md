<h2 id="background">Background</h2>
<p>A <code>ReadableStream</code> is returned by the <code>readable</code> property inside <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a>.</p>
<h2 id="properties">Properties</h2>
<ul>
<li><code>locked</code> boolean
<ul>
<li>A Boolean value that indicates if the readable stream is locked to a reader.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>pipeTo(destinationWritableStream, optionsPipeToOptions)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Pipes the readable stream to a given writable stream <code>destination</code> and returns a promise that is fulfilled when the <code>write</code> operation succeeds or rejects it if the operation fails.</li>
</ul>
</li>
<li>
<p><code>pipeThrough(transformStream, optionsPipeToOptions)</code> : ReadableStream</p>
<ul>
<li>Pipes the readable stream to the writable side of a given <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a> and returns the transform's readable side, so that calls can be chained. <code>options</code> accepts the same values as <code>pipeTo()</code>.</li>
</ul>
</li>
<li>
<p><code>getReader(optionsObject)</code> : ReadableStreamDefaultReader</p>
<ul>
<li>Gets an instance of <code>ReadableStreamDefaultReader</code> and locks the <code>ReadableStream</code> to that reader instance. This method accepts an object argument indicating options. The only supported option is <code>mode</code>, which can be set to <code>byob</code> to create a <a href="/workers/runtime-apis/streams/readablestreambyobreader/"><code>ReadableStreamBYOBReader</code></a>, as shown here:</li>
</ul>
</li>
</ul>
<pre><code class="language-js">let reader = readable.getReader({ mode: &#x27;byob&#x27; });&#10;</code></pre>
<ul>
<li>
<p><code>cancel(reasonstringoptional)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Cancels the stream. <code>reason</code> is an optional human-readable string indicating the reason for cancellation. <code>reason</code> will be passed to the underlying source’s cancel algorithm. Any data not yet read is lost.</li>
</ul>
</li>
<li>
<p><code>tee()</code> : [ReadableStream, ReadableStream]</p>
<ul>
<li>Locks the stream and returns an array of two new <code>ReadableStream</code> instances, each of which reads the same data as the original stream. Backpressure to the underlying source follows the branch with the most unread data, which avoids unbounded buffering when one branch reads more slowly than the other, as long as the underlying source responds to backpressure. Refer to <a href="https://github.com/cloudflare/workerd/blob/main/src/workerd/api/streams/README.md#tee-behavior">workerd's streams documentation</a> for implementation details.</li>
</ul>
</li>
<li>
<p><code>values(optionsObject)</code> : AsyncIterableIterator</p>
<ul>
<li>Returns an async iterator that reads and consumes the chunks of the stream. This method accepts an object argument indicating options. The only supported option is <code>preventCancel</code>, which, when <code>true</code>, prevents the stream from being canceled when the iterator exits early (for example, from a <code>break</code> statement). A <code>ReadableStream</code> is also async iterable directly:</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17068.md")
</div>
<h3 id="pipetooptions"><code>PipeToOptions</code></h3>
<ul>
<li>
<p><code>preventClose</code> bool</p>
<ul>
<li>When <code>true</code>, closure of the source <code>ReadableStream</code> will not cause the destination <code>WritableStream</code> to be closed.</li>
</ul>
</li>
<li>
<p><code>preventAbort</code> bool</p>
<ul>
<li>When <code>true</code>, errors in the source <code>ReadableStream</code> will no longer abort the destination <code>WritableStream</code>. <code>pipeTo</code> will return a rejected promise with the error from the source or any error that occurred while aborting the destination.</li>
</ul>
</li>
</ul>
<h2 id="static-methods">Static methods</h2>
<ul>
<li>
<p><code>ReadableStream.from(asyncIterable)</code> : ReadableStream</p>
<ul>
<li>Creates a new <code>ReadableStream</code> whose chunks are the values yielded by <code>asyncIterable</code>, which may be any iterable or async iterable, including an async generator.</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17069.md")
</div>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#rs-model">Readable streams in the WHATWG Streams API specification</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream">MDN’s <code>ReadableStream</code> documentation</a></li>
</ul>
