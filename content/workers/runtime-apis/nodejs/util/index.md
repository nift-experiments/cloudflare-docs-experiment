<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17128.md")
</aside>
<h2 id="promisify-callbackify">promisify/callbackify</h2>
<p>The <code>promisify</code> and <code>callbackify</code> APIs in Node.js provide a means of bridging between a Promise-based programming model and a callback-based model.</p>
<p>The <code>promisify</code> method allows taking a Node.js-style callback function and converting it into a Promise-returning async function:</p>
<pre><code class="language-js">import { promisify } from &quot;node:util&quot;;&#10;&#10;function foo(args, callback) {&#10;	try {&#10;		callback(null, 1);&#10;	} catch (err) {&#10;		// Errors are emitted to the callback via the first argument.&#10;		callback(err);&#10;	}&#10;}&#10;&#10;const promisifiedFoo = promisify(foo);&#10;await promisifiedFoo(args);&#10;</code></pre>
<p>Similarly to <code>promisify</code>, <code>callbackify</code> converts a Promise-returning async function into a Node.js-style callback function:</p>
<pre><code class="language-js">import { callbackify } from &#x27;node:util&#x27;;&#10;&#10;async function foo(args) {&#10;  throw new Error(&#x27;boom&#x27;);&#10;}&#10;&#10;const callbackifiedFoo = callbackify(foo);&#10;&#10;callbackifiedFoo(args, (err, value) =&gt; {&#10;  if (err) throw err;&#10;});&#10;</code></pre>
<p><code>callbackify</code> and <code>promisify</code> make it easy to handle all of the challenges that come with bridging between callbacks and promises.</p>
<p>Refer to the <a href="https://nodejs.org/dist/latest-v19.x/docs/api/util.html#utilcallbackifyoriginal">Node.js documentation for <code>callbackify</code></a> and <a href="https://nodejs.org/dist/latest-v19.x/docs/api/util.html#utilpromisifyoriginal">Node.js documentation for <code>promisify</code></a> for more information.</p>
<h2 id="util-types">util.types</h2>
<p>The <code>util.types</code> API provides a reliable and efficient way of checking that values are instances of various built-in types.</p>
<pre><code class="language-js">import { types } from &quot;node:util&quot;;&#10;&#10;types.isAnyArrayBuffer(new ArrayBuffer()); // Returns true&#10;types.isAnyArrayBuffer(new SharedArrayBuffer()); // Returns true&#10;types.isArrayBufferView(new Int8Array()); // true&#10;types.isArrayBufferView(Buffer.from(&quot;hello world&quot;)); // true&#10;types.isArrayBufferView(new DataView(new ArrayBuffer(16))); // true&#10;types.isArrayBufferView(new ArrayBuffer()); // false&#10;function foo() {&#10;	types.isArgumentsObject(arguments); // Returns true&#10;}&#10;types.isAsyncFunction(function foo() {}); // Returns false&#10;types.isAsyncFunction(async function foo() {}); // Returns true&#10;// .. and so on&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17127.md")
</aside>
<p>For more about <code>util.types</code>, refer to the <a href="https://nodejs.org/dist/latest-v19.x/docs/api/util.html#utiltypes">Node.js documentation for <code>util.types</code></a>.</p>
<h2 id="util-mimetype">util.MIMEType</h2>
<p><code>util.MIMEType</code> provides convenience methods that allow you to more easily work with and manipulate <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types">MIME types</a>. For example:</p>
<pre><code class="language-js">import { MIMEType } from &quot;node:util&quot;;&#10;&#10;const myMIME = new MIMEType(&quot;text/javascript;key=value&quot;);&#10;&#10;console.log(myMIME.type);&#10;// Prints: text&#10;&#10;console.log(myMIME.essence);&#10;// Prints: text/javascript&#10;&#10;console.log(myMIME.subtype);&#10;// Prints: javascript&#10;&#10;console.log(String(myMIME));&#10;// Prints: application/javascript;key=value&#10;</code></pre>
<p>For more about <code>util.MIMEType</code>, refer to the <a href="https://nodejs.org/api/util.html#class-utilmimetype">Node.js documentation for <code>util.MIMEType</code></a>.</p>
