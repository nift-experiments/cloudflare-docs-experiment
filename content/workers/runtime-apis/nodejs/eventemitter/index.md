<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17162.md")
</aside>
<p>An <a href="https://nodejs.org/docs/latest/api/events.html#class-eventemitter"><code>EventEmitter</code></a>
is an object that emits named events that cause listeners to be called.</p>
<pre><code class="language-js">import { EventEmitter } from &quot;node:events&quot;;&#10;&#10;const emitter = new EventEmitter();&#10;emitter.on(&quot;hello&quot;, (...args) =&gt; {&#10;	console.log(...args); // 1 2 3&#10;});&#10;&#10;emitter.emit(&quot;hello&quot;, 1, 2, 3);&#10;</code></pre>
<p>The implementation in the Workers runtime supports the entire Node.js <code>EventEmitter</code> API. This includes the <a href="https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises"><code>captureRejections</code></a>
option that allows improved handling of async functions as event handlers:</p>
<pre><code class="language-js">const emitter = new EventEmitter({ captureRejections: true });&#10;emitter.on(&quot;hello&quot;, async (...args) =&gt; {&#10;	throw new Error(&quot;boom&quot;);&#10;});&#10;emitter.on(&quot;error&quot;, (err) =&gt; {&#10;	// the async promise rejection is emitted here!&#10;});&#10;</code></pre>
<p>Like Node.js, when an <code>'error'</code> event is emitted on an <code>EventEmitter</code> and there
is no listener for it, the error will be immediately thrown. However, in Node.js
it is possible to add a handler on the <code>process</code> object for the
<code>'uncaughtException'</code> event to catch globally uncaught exceptions. The
<code>'uncaughtException'</code> event, however, is currently not implemented in the
Workers runtime. It is strongly recommended to always add an <code>'error'</code> listener
to any <code>EventEmitter</code> instance.</p>
<p>Refer to the <a href="https://nodejs.org/api/events.html#class-eventemitter">Node.js documentation for <code>EventEmitter</code></a> for more information.</p>
