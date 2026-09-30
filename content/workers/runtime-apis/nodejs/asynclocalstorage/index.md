<h2 id="background">Background</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17159.md")
</aside>
<p>Cloudflare Workers provides an implementation of a subset of the Node.js <a href="https://nodejs.org/dist/latest-v18.x/docs/api/async_context.html#class-asynclocalstorage"><code>AsyncLocalStorage</code></a> API for creating in-memory stores that remain coherent through asynchronous operations.</p>
<h2 id="constructor">Constructor</h2>
<pre><code class="language-js">import { AsyncLocalStorage } from &quot;node:async_hooks&quot;;&#10;&#10;const asyncLocalStorage = new AsyncLocalStorage();&#10;</code></pre>
<ul>
<li><code>new AsyncLocalStorage()</code> : AsyncLocalStorage
<ul>
<li>Returns a new <code>AsyncLocalStorage</code> instance.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>getStore()</code> : any</p>
<ul>
<li>Returns the current store. If called outside of an asynchronous context initialized by calling <code>asyncLocalStorage.run()</code>, it returns <code>undefined</code>.</li>
</ul>
</li>
<li>
<p><code>run(storeany, callbackfunction, ...argsarguments)</code> : any</p>
<ul>
<li>Runs a function synchronously within a context and returns its return value. The store is not accessible outside of the callback function. The store is accessible to any asynchronous operations created within the callback. The optional <code>args</code> are passed to the callback function. If the callback function throws an error, the error is thrown by <code>run()</code> also.</li>
</ul>
</li>
<li>
<p><code>exit(callbackfunction, ...argsarguments)</code> : any</p>
<ul>
<li>Runs a function synchronously outside of a context and returns its return value. This method is equivalent to calling <code>run()</code> with the <code>store</code> value set to <code>undefined</code>.</li>
</ul>
</li>
</ul>
<h2 id="static-methods">Static Methods</h2>
<ul>
<li>
<p><code>AsyncLocalStorage.bind(fn)</code> : function</p>
<ul>
<li>Captures the asynchronous context that is current when <code>bind()</code> is called and returns a function that enters that context before calling the passed in function.</li>
</ul>
</li>
<li>
<p><code>AsyncLocalStorage.snapshot()</code> : function</p>
<ul>
<li>Captures the asynchronous context that is current when <code>snapshot()</code> is called and returns a function that enters that context before calling a given function.</li>
</ul>
</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="fetch-listener">Fetch Listener</h3>
<pre><code class="language-js">import { AsyncLocalStorage } from &#x27;node:async_hooks&#x27;;&#10;&#10;const asyncLocalStorage = new AsyncLocalStorage();&#10;let idSeq = 0;&#10;&#10;export default {&#10;  async fetch(req) {&#10;    return asyncLocalStorage.run(idSeq++, () =&gt; {&#10;      // Simulate some async activity...&#10;      await scheduler.wait(1000);&#10;      return new Response(asyncLocalStorage.getStore());&#10;    });&#10;  }&#10;};&#10;</code></pre>
<h3 id="multiple-stores">Multiple stores</h3>
<p>The API supports multiple <code>AsyncLocalStorage</code> instances to be used concurrently.</p>
<pre><code class="language-js">import { AsyncLocalStorage } from &#x27;node:async_hooks&#x27;;&#10;&#10;const als1 = new AsyncLocalStorage();&#10;const als2 = new AsyncLocalStorage();&#10;&#10;export default {&#10;  async fetch(req) {&#10;    return als1.run(123, () =&gt; {&#10;      return als2.run(321, () =&gt; {&#10;        // Simulate some async activity...&#10;        await scheduler.wait(1000);&#10;        return new Response(`${als1.getStore()}-${als2.getStore()}`);&#10;      });&#10;    });&#10;  }&#10;};&#10;</code></pre>
<h3 id="unhandled-rejections">Unhandled Rejections</h3>
<p>When a <code>Promise</code> rejects and the rejection is unhandled, the async context propagates to the <code>'unhandledrejection'</code> event handler:</p>
<pre><code class="language-js">import { AsyncLocalStorage } from &quot;node:async_hooks&quot;;&#10;&#10;const asyncLocalStorage = new AsyncLocalStorage();&#10;let idSeq = 0;&#10;&#10;addEventListener(&quot;unhandledrejection&quot;, (event) =&gt; {&#10;	console.log(asyncLocalStorage.getStore(), &quot;unhandled rejection!&quot;);&#10;});&#10;&#10;export default {&#10;	async fetch(req) {&#10;		return asyncLocalStorage.run(idSeq++, () =&gt; {&#10;			// Cause an unhandled rejection!&#10;			throw new Error(&quot;boom&quot;);&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h3 id="asynclocalstorage-bind-and-asynclocalstorage-snapshot"><code>AsyncLocalStorage.bind()</code> and <code>AsyncLocalStorage.snapshot()</code></h3>
<pre><code class="language-js">import { AsyncLocalStorage } from &quot;node:async_hooks&quot;;&#10;&#10;const als = new AsyncLocalStorage();&#10;&#10;function foo() {&#10;	console.log(als.getStore());&#10;}&#10;function bar() {&#10;	console.log(als.getStore());&#10;}&#10;&#10;const oneFoo = als.run(123, () =&gt; AsyncLocalStorage.bind(foo));&#10;oneFoo(); // prints 123&#10;&#10;const snapshot = als.run(&quot;abc&quot;, () =&gt; AsyncLocalStorage.snapshot());&#10;snapshot(foo); // prints &#x27;abc&#x27;&#10;snapshot(bar); // prints &#x27;abc&#x27;&#10;</code></pre>
<pre><code class="language-js">import { AsyncLocalStorage } from &quot;node:async_hooks&quot;;&#10;&#10;const als = new AsyncLocalStorage();&#10;&#10;class MyResource {&#10;	&#35;runInAsyncScope = AsyncLocalStorage.snapshot();&#10;&#10;	doSomething() {&#10;		this.#runInAsyncScope(() =&gt; {&#10;			return als.getStore();&#10;		});&#10;	}&#10;}&#10;&#10;const myResource = als.run(123, () =&gt; new MyResource());&#10;console.log(myResource.doSomething()); // prints 123&#10;</code></pre>
<h2 id="asyncresource"><code>AsyncResource</code></h2>
<p>The <a href="https://nodejs.org/dist/latest-v18.x/docs/api/async_context.html#class-asyncresource"><code>AsyncResource</code></a> class is a component of Node.js' async context tracking API that allows users to create their own async contexts. Objects that extend from <code>AsyncResource</code> are capable of propagating the async context in much the same way as promises.</p>
<p>Note that <code>AsyncLocalStorage.snapshot()</code> and <code>AsyncLocalStorage.bind()</code> provide a better approach. <code>AsyncResource</code> is provided solely for backwards compatibility with Node.js.</p>
<h3 id="constructor-1">Constructor</h3>
<pre><code class="language-js">import { AsyncResource, AsyncLocalStorage } from &quot;node:async_hooks&quot;;&#10;&#10;const als = new AsyncLocalStorage();&#10;&#10;class MyResource extends AsyncResource {&#10;	constructor() {&#10;		// The type string is required by Node.js but unused in Workers.&#10;		super(&quot;MyResource&quot;);&#10;	}&#10;&#10;	doSomething() {&#10;		this.runInAsyncScope(() =&gt; {&#10;			return als.getStore();&#10;		});&#10;	}&#10;}&#10;&#10;const myResource = als.run(123, () =&gt; new MyResource());&#10;console.log(myResource.doSomething()); // prints 123&#10;</code></pre>
<ul>
<li>
<p><code>new AsyncResource(typestring, optionsAsyncResourceOptions)</code> :
AsyncResource</p>
<ul>
<li>Returns a new <code>AsyncResource</code>. Importantly, while the constructor arguments are required in Node.js' implementation of <code>AsyncResource</code>, they are not used in Workers.</li>
</ul>
</li>
<li>
<p><code>AsyncResource.bind(fnfunction, typestring, thisArgany)</code></p>
<ul>
<li>Binds the given function to the current async context.</li>
</ul>
</li>
</ul>
<h3 id="methods-1">Methods</h3>
<ul>
<li>
<p><code>asyncResource.bind(fnfunction, thisArgany)</code></p>
<ul>
<li>Binds the given function to the async context associated with this <code>AsyncResource</code>.</li>
</ul>
</li>
<li>
<p><code>asyncResource.runInAsyncScope(fnfunction, thisArgany, ...argsarguments)</code></p>
<ul>
<li>Call the provided function with the given arguments in the async context associated with this <code>AsyncResource</code>.</li>
</ul>
</li>
</ul>
<h2 id="caveats">Caveats</h2>
<ul>
<li>
<p>The <code>AsyncLocalStorage</code> implementation provided by Workers intentionally omits support for the <a href="https://nodejs.org/dist/latest-v18.x/docs/api/async_context.html#asynclocalstorageenterwithstore"><code>asyncLocalStorage.enterWith()</code></a> and <a href="https://nodejs.org/dist/latest-v18.x/docs/api/async_context.html#asynclocalstoragedisable"><code>asyncLocalStorage.disable()</code></a> methods.</p>
</li>
<li>
<p>Workers does not implement the full <a href="https://nodejs.org/dist/latest-v18.x/docs/api/async_hooks.html"><code>async_hooks</code></a> API upon which Node.js' implementation of <code>AsyncLocalStorage</code> is built.</p>
</li>
<li>
<p>Workers does not implement the ability to create an <code>AsyncResource</code> with an explicitly identified trigger context as allowed by Node.js. This means that a new <code>AsyncResource</code> will always be bound to the async context in which it was created.</p>
</li>
<li>
<p>Thenables (non-Promise objects that expose a <code>then()</code> method) are not fully supported when using <code>AsyncLocalStorage</code>. When working with thenables, instead use <a href="https://nodejs.org/api/async_context.html#static-method-asynclocalstoragesnapshot"><code>AsyncLocalStorage.snapshot()</code></a> to capture a snapshot of the current context.</p>
</li>
</ul>
