<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17158.md")
</aside>
<p>The <a href="https://nodejs.org/docs/latest/api/buffer.html"><code>Buffer</code></a> API in Node.js is one of the most commonly used Node.js APIs for manipulating binary data. Every <code>Buffer</code> instance extends from the standard <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array"><code>Uint8Array</code></a> class, but adds a range of unique capabilities such as built-in base64 and hex encoding/decoding, byte-order manipulation, and encoding-aware substring searching.</p>
<pre><code class="language-js">import { Buffer } from &quot;node:buffer&quot;;&#10;&#10;const buf = Buffer.from(&quot;hello world&quot;, &quot;utf8&quot;);&#10;&#10;console.log(buf.toString(&quot;hex&quot;));&#10;// Prints: 68656c6c6f20776f726c64&#10;console.log(buf.toString(&quot;base64&quot;));&#10;// Prints: aGVsbG8gd29ybGQ=&#10;</code></pre>
<p>A Buffer extends from <code>Uint8Array</code>. Therefore, it can be used in any Workers API that currently accepts <code>Uint8Array</code>, such as creating a new Response:</p>
<pre><code class="language-js">const response = new Response(Buffer.from(&quot;hello world&quot;));&#10;</code></pre>
<p>You can also use the <code>Buffer</code> API when interacting with streams:</p>
<pre><code class="language-js">const writable = getWritableStreamSomehow();&#10;const writer = writable.getWriter();&#10;writer.write(Buffer.from(&quot;hello world&quot;));&#10;</code></pre>
<p>One key difference between the Workers implementation of <code>Buffer</code> and the Node.js
implementation is that some methods of creating a <code>Buffer</code> in Node.js will allocate
those from a global memory pool as a performance optimization. The Workers implementation
does not use a memory pool and all <code>Buffer</code> instances are allocated independently.</p>
<p>Further, in Node.js it is possible to allocate a <code>Buffer</code> with uninitialized memory
using the <code>Buffer.allocUnsafe()</code> method. This is not supported in Workers and <code>Buffer</code>
instances are always initialized so that the <code>Buffer</code> is always filled
with null bytes (<code>0x00</code>) when allocated.</p>
<p>Refer to the <a href="https://nodejs.org/dist/latest-v19.x/docs/api/buffer.html">Node.js documentation for <code>Buffer</code></a> for more information.</p>
