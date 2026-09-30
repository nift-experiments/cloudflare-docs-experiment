<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17161.md")
</aside>
<p>The <a href="https://nodejs.org/docs/latest/api/assert.html"><code>node:assert</code></a> module in Node.js provides a number of useful assertions that are useful when building tests.</p>
<pre><code class="language-js">import { strictEqual, deepStrictEqual, ok, doesNotReject } from &quot;node:assert&quot;;&#10;&#10;strictEqual(1, 1); // ok!&#10;strictEqual(1, &quot;1&quot;); // fails! throws AssertionError&#10;&#10;deepStrictEqual({ a: { b: 1 } }, { a: { b: 1 } }); // ok!&#10;deepStrictEqual({ a: { b: 1 } }, { a: { b: 2 } }); // fails! throws AssertionError&#10;&#10;ok(true); // ok!&#10;ok(false); // fails! throws AssertionError&#10;&#10;await doesNotReject(async () =&gt; {}); // ok!&#10;await doesNotReject(async () =&gt; {&#10;	throw new Error(&quot;boom&quot;);&#10;}); // fails! throws AssertionError&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17160.md")
</aside>
<p>Refer to the <a href="https://nodejs.org/dist/latest-v19.x/docs/api/assert.html">Node.js documentation for <code>assert</code></a> for more information.</p>
