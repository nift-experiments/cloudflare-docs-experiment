<h2 id="javascript-standards">JavaScript standards</h2>
<p>The Cloudflare Workers runtime is <a href="/workers/reference/how-workers-works/">built on top of the V8 JavaScript and WebAssembly engine</a>. The Workers runtime is updated at least once a week, to at least the version of V8 that is currently used by Google Chrome's stable release. This means you can safely use the latest JavaScript features, with no need for transpilers.</p>
<p>All of the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference">standard built-in objects</a> supported by the current Google Chrome stable release are supported, with a few notable exceptions:</p>
<ul>
<li>For security reasons, the following are not allowed:
<ul>
<li><code>eval()</code></li>
<li><code>new Function</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/compile_static"><code>WebAssembly.compile</code></a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/compileStreaming_static"><code>WebAssembly.compileStreaming</code></a></li>
<li><code>WebAssembly.instantiate</code> with a <a href="https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/instantiate_static#primary_overload_%E2%80%94_taking_wasm_binary_code">buffer parameter</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/instantiateStreaming_static"><code>WebAssembly.instantiateStreaming</code></a></li>
</ul>
</li>
<li><code>Date.now()</code> returns the time of the last I/O; it does not advance during code execution.</li>
</ul>
<hr />
<h2 id="web-standards-and-global-apis">Web standards and global APIs</h2>
<p>The following methods are available per the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope">Worker Global Scope</a>:</p>
<h3 id="base64-utility-methods">Base64 utility methods</h3>
<ul>
<li>
<p>atob()</p>
<ul>
<li>Decodes a string of data which has been encoded using base-64 encoding.</li>
</ul>
</li>
<li>
<p>btoa()</p>
<ul>
<li>Creates a base-64 encoded ASCII string from a string of binary data.</li>
</ul>
</li>
</ul>
<h3 id="timers">Timers</h3>
<ul>
<li>
<p>setInterval()</p>
<ul>
<li>Schedules a function to execute every time a given number of milliseconds elapses.</li>
</ul>
</li>
<li>
<p>clearInterval()</p>
<ul>
<li>Cancels the repeated execution set using <a href="https://developer.mozilla.org/en-US/docs/Web/API/setInterval"><code>setInterval()</code></a>.</li>
</ul>
</li>
<li>
<p>setTimeout()</p>
<ul>
<li>Schedules a function to execute in a given amount of time.</li>
</ul>
</li>
<li>
<p>clearTimeout()</p>
<ul>
<li>Cancels the delayed execution set using <a href="https://developer.mozilla.org/en-US/docs/Web/API/setTimeout"><code>setTimeout()</code></a>.</li>
</ul>
</li>
<li>
<p><a href="/workers/runtime-apis/scheduler/"><code>scheduler.wait()</code></a></p>
<ul>
<li>Returns a Promise that resolves after a given number of milliseconds. An <code>await</code>-able alternative to <code>setTimeout()</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16123.md")
</aside>
<h3 id="performance-timeorigin-and-performance-now"><code>performance.timeOrigin</code> and <code>performance.now()</code></h3>
<ul>
<li>
<p>performance.timeOrigin</p>
<ul>
<li>Returns the high resolution time origin. Workers uses the UNIX epoch as the time origin, meaning that <code>performance.timeOrigin</code> will always return <code>0</code>.</li>
</ul>
</li>
<li>
<p>performance.now()</p>
<ul>
<li>Returns a <code>DOMHighResTimeStamp</code> representing the number of milliseconds elapsed since <code>performance.timeOrigin</code>. Note that Workers intentionally reduces the precision of <code>performance.now()</code> such that it returns the time of the last I/O and does not advance during code execution. Effectively, because of this, and because <code>performance.timeOrigin</code> is always, <code>0</code>, <code>performance.now()</code> will always equal <code>Date.now()</code>, yielding a consistent view of the passage of time within a Worker.</li>
</ul>
</li>
</ul>
<h3 id="eventtarget-and-event"><code>EventTarget</code> and <code>Event</code></h3>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/EventTarget"><code>EventTarget</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/API/Event"><code>Event</code></a> API allow objects to publish and subscribe to events.</p>
<h3 id="abortcontroller-and-abortsignal"><code>AbortController</code> and <code>AbortSignal</code></h3>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/AbortController"><code>AbortController</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal"><code>AbortSignal</code></a> APIs provide a common model for canceling asynchronous operations.</p>
<h3 id="fetch-global">Fetch global</h3>
<ul>
<li>fetch()
<ul>
<li>Starts the process of fetching a resource from the network. Refer to <a href="/workers/runtime-apis/fetch/">Fetch API</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16122.md")
</aside>
<hr />
<h2 id="encoding-api">Encoding API</h2>
<p>Both <code>TextEncoder</code> and <code>TextDecoder</code> support UTF-8 encoding/decoding.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API">Refer to the MDN documentation for more information</a>.</p>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/TextEncoderStream"><code>TextEncoderStream</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/API/TextDecoderStream"><code>TextDecoderStream</code></a> classes are also available.</p>
<hr />
<h2 id="url-api">URL API</h2>
<p>The URL API supports URLs conforming to HTTP and HTTPS schemes.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/URL">Refer to the MDN documentation for more information</a></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16121.md")
</aside>
<hr />
<h2 id="compression-streams">Compression Streams</h2>
<p>The <code>CompressionStream</code> and <code>DecompressionStream</code> classes support the deflate, deflate-raw and gzip compression methods.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/Compression_Streams_API">Refer to the MDN documentation for more information</a></p>
<hr />
<h2 id="urlpattern-api">URLPattern API</h2>
<p>The <code>URLPattern</code> API provides a mechanism for matching URLs based on a convenient pattern syntax.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/URLPattern">Refer to the MDN documentation for more information</a>.</p>
<hr />
<h2 id="intl"><code>Intl</code></h2>
<p>The <code>Intl</code> API allows you to format dates, times, numbers, and more to the format that is used by a provided locale (language and region).</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl">Refer to the MDN documentation for more information</a>.</p>
<hr />
<h2 id="navigator-useragent"><code>navigator.userAgent</code></h2>
<p>When the <a href="/workers/configuration/compatibility-flags/#global-navigator"><code>global_navigator</code></a> compatibility flag is set, the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent"><code>navigator.userAgent</code></a> property is available with the value <code>'Cloudflare-Workers'</code>. This can be used, for example, to reliably determine that code is running within the Workers environment.</p>
<h2 id="unhandled-promise-rejections">Unhandled promise rejections</h2>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event"><code>unhandledrejection</code></a> event is emitted by the global scope when a JavaScript promise is rejected without a rejection handler attached.</p>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/rejectionhandled_event"><code>rejectionhandled</code></a> event is emitted by the global scope when a JavaScript promise rejection is handled late (after a rejection handler is attached to the promise after an <code>unhandledrejection</code> event has already been emitted).</p>
<pre><code class="language-js">addEventListener(&quot;unhandledrejection&quot;, (event) =&gt; {&#10;	console.log(event.promise); // The promise that was rejected.&#10;	console.log(event.reason); // The value or Error with which the promise was rejected.&#10;});&#10;&#10;addEventListener(&quot;rejectionhandled&quot;, (event) =&gt; {&#10;	console.log(event.promise); // The promise that was rejected.&#10;	console.log(event.reason); // The value or Error with which the promise was rejected.&#10;});&#10;</code></pre>
<hr />
<h2 id="navigator-sendbeacon-url-data"><code>navigator.sendBeacon(url[, data])</code></h2>
<p>When the <a href="/workers/configuration/compatibility-flags/#global-navigator"><code>global_navigator</code></a> compatibility flag is set, the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon"><code>navigator.sendBeacon(...)</code></a> API is available to send an HTTP <code>POST</code> request containing a small amount of data to a web server. This API is intended as a means of transmitting analytics or diagnostics information asynchronously on a best-effort basis.</p>
<p>For example, you can replace:</p>
<pre><code class="language-js">const promise = fetch(&quot;https://example.com&quot;, {&#10;	method: &quot;POST&quot;,&#10;	body: &quot;hello world&quot;,&#10;});&#10;ctx.waitUntil(promise);&#10;</code></pre>
<p>with <code>navigator.sendBeacon(...)</code>:</p>
<pre><code class="language-js">navigator.sendBeacon(&quot;https://example.com&quot;, &quot;hello world&quot;);&#10;</code></pre>
<h2 id="the-web-file-system-access-api">The Web File System Access API</h2>
<p>When the <code>enable_web_file_system</code> compatibility flag is set, Workers supports the <a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API">Web File System Access API</a>, which allows you to read and write files and directories to a virtual file system within the Worker environment. This API provides access to the same in-memory virtual file system as the <a href="/workers/runtime-apis/nodejs/fs/"><code>node:fs</code> module</a> but does not require Node.js compatibility to be enabled.</p>
<pre><code class="language-js">const root = await navigator.storage.getDirectory();&#10;&#10;export default {&#10;	async fetch(request) {&#10;		const fileHandle = await root.getFileHandle(&quot;hello.txt&quot;, { create: true });&#10;		const writable = await fileHandle.createWritable();&#10;		await writable.write(&quot;Hello, world!&quot;);&#10;		await writable.close();&#10;&#10;		const file = await fileHandle.getFile();&#10;		const contents = await file.text();&#10;&#10;		return new Response(contents, { status: 200 });&#10;	},&#10;};&#10;</code></pre>
<p>Please refer to the <a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API">MDN documentation</a> for more information on using this API, and to the <a href="/workers/runtime-apis/nodejs/fs/"><code>node:fs</code> documentation</a> for details on the virtual file system structure and limitations.</p>
