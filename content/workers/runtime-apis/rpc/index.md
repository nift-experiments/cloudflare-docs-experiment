<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17086.md")
</aside>
<p>Workers provide a built-in, JavaScript-native <a href="https://en.wikipedia.org/wiki/Remote_procedure_call">RPC (Remote Procedure Call)</a> system, allowing you to:</p>
<ul>
<li>Define public methods on your Worker that can be called by other Workers on the same Cloudflare account, via <a href="/workers/runtime-apis/bindings/service-bindings/rpc">Service Bindings</a></li>
<li>Define public methods on <a href="/durable-objects">Durable Objects</a> that can be called by other workers on the same Cloudflare account that declare a binding to it.</li>
</ul>
<p>The RPC system is designed to feel as similar as possible to calling a JavaScript function in the same Worker. In most cases, you should be able to write code in the same way you would if everything was in a single Worker.</p>
<h2 id="example">Example</h2>
<p>For example, if Worker B implements the public method <code>add(a, b)</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17087.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17090.md")
</div></div>
<p>Worker A can declare a <a href="/workers/runtime-apis/bindings">binding</a> to Worker B:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17091.md")
</div>
<p>Making it possible for Worker A to call the <code>add()</code> method from Worker B:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17094.md")
</div></div>
<p>The client, in this case Worker A, calls Worker B and tells it to execute a specific procedure using specific arguments that the client provides. This is accomplished with standard JavaScript classes.</p>
<h2 id="all-calls-are-asynchronous">All calls are asynchronous</h2>
<p>Whether or not the method you are calling was declared asynchronous on the server side, it will behave as such on the client side. You must <code>await</code> the result.</p>
<p>Note that RPC calls do not actually return <code>Promise</code>s, but they return a type that behaves like a <code>Promise</code>. The type is a &quot;custom thenable&quot;, in that it implements the method <code>then()</code>. JavaScript supports awaiting any &quot;thenable&quot; type, so, for the most part, you can treat the return value like a Promise.</p>
<p>(We'll see why the type is not actually a Promise a bit later.)</p>
<h2 id="structured-cloneable-types-and-more">Structured cloneable types, and more</h2>
<p>Nearly all types that are <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">Structured Cloneable</a> can be used as a parameter or return value of an RPC method. This includes, most basic &quot;value&quot; types in JavaScript, including objects, arrays, strings and numbers.</p>
<p>As an exception to Structured Clone, application-defined classes (or objects with custom prototypes) cannot be passed over RPC, except as described below.</p>
<p>The RPC system also supports a number of types that are not Structured Cloneable, including:</p>
<ul>
<li>Functions, which are replaced by stubs that call back to the sender.</li>
<li>Application-defined classes that extend <code>RpcTarget</code>, which are similarly replaced by stubs.</li>
<li><a href="/workers/runtime-apis/streams/readablestream/">ReadableStream</a> and <a href="/workers/runtime-apis/streams/writablestream/">WritableStream</a>, with automatic streaming flow control.</li>
<li><a href="/workers/runtime-apis/request/">Request</a> and <a href="/workers/runtime-apis/response/">Response</a>, for conveniently representing HTTP messages.</li>
<li>RPC stubs themselves, even if the stub was received from a third Worker.</li>
</ul>
<h2 id="functions">Functions</h2>
<p>You can send a function over RPC. When you do so, the function is replaced by a &quot;stub&quot;. The recipient can call the stub like a function, but doing so makes a new RPC back to the place where the function originated.</p>
<h3 id="return-functions-from-rpc-methods">Return functions from RPC methods</h3>
<p>Consider the following two Workers, connected via a <a href="/workers/runtime-apis/bindings/service-bindings/rpc">Service Binding</a>. The counter service provides the RPC method <code>newCounter()</code>, which returns a function:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17095.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17098.md")
</div></div>
<p>This function can then be called by the client Worker:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17099.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17102.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17085.md")
</aside>
<p>How is this possible? The system is not serializing the function itself. When the function returned by <code>CounterService</code> is called, it runs within <code>CounterService</code> — even if it is called by another Worker.</p>
<p>Under the hood, the caller is not really calling the function itself directly, but calling what is called a &quot;stub&quot;. A &quot;stub&quot; is a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy">Proxy</a> object that allows the client to call the remote service as if it were local, running in the same Worker. Behind the scenes, it calls back to the Worker that implements <code>CounterService</code> and asks it to execute the function closure that had been returned earlier.</p>
<h3 id="send-functions-as-parameters-of-rpc-methods">Send functions as parameters of RPC methods</h3>
<p>You can also send a function in the parameters of an RPC. This enables the &quot;server&quot; to call back to the &quot;client&quot;, reversing the direction of the relationship.</p>
<p>Because of this, the words &quot;client&quot; and &quot;server&quot; can be ambiguous when talking about RPC. The &quot;server&quot; is a Durable Object or WorkerEntrypoint, and the &quot;client&quot; is the Worker that invoked the server via a binding. But, RPCs can flow both ways between the two. When talking about an individual RPC, we recommend instead using the words &quot;caller&quot; and &quot;callee&quot;.</p>
<h2 id="class-instances">Class Instances</h2>
<p>To use an instance of a class that you define as a parameter or return value of an RPC method, you must extend the built-in <code>RpcTarget</code> class.</p>
<p>Consider the following example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17103.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17105.md")
</div></div>
<p>The method <code>increment</code> can be called directly by the client, as can the public property <code>value</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17106.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17109.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17084.md")
</aside>
<p>Classes that extend <code>RpcTarget</code> work a lot like functions: the object itself is not serialized, but is instead replaced by a stub. In this case, the stub itself is not callable, but its methods are. Calling any method on the stub actually makes an RPC back to the original object, where it was created.</p>
<p>As shown above, you can also access properties of classes. Properties behave like RPC methods that don't take any arguments — you await the property to asynchronously fetch its current value. Note that the act of awaiting the property (which, behind the scenes, calls <code>.then()</code> on it) is what causes the property to be fetched. If you do not use <code>await</code> when accessing the property, it will not be fetched.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17083.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17082.md")
</aside>
<h3 id="promise-pipelining">Promise pipelining</h3>
<p>When you call an RPC method and get back an object, it's common to immediately call a method on the object:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17112.md")
</div></div>
<p>But consider the case where the Worker service that you are calling may be far away across the network, as in the case of <a href="/workers/configuration/placement/">Smart Placement</a> or <a href="/durable-objects">Durable Objects</a>. The code above makes two round trips, once when calling <code>getCounter()</code>, and again when calling <code>.increment()</code>. We'd like to avoid this.</p>
<p>With most RPC systems, the only way to avoid the problem would be to combine the two calls into a single &quot;batch&quot; call, perhaps called <code>getCounterAndIncrement()</code>. However, this makes the interface worse. You wouldn't design a local interface this way.</p>
<p>Workers RPC allows a different approach: You can simply omit the first <code>await</code>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17115.md")
</div></div>
<p>In this code, <code>getCounter()</code> returns a promise for a counter. Normally, the only thing you would do with a promise is <code>await</code> it. However, Workers RPC promises are special: they also allow you to initiate speculative calls on the future result of the promise. These calls are sent to the server immediately, without waiting for the initial call to complete. Thus, multiple chained calls can be completed in a single round trip.</p>
<p>How does this work? The promise returned by an RPC is not a real JavaScript <code>Promise</code>. Instead, it is a custom <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables">&quot;Thenable&quot;</a>. It has a <code>.then()</code> method like <code>Promise</code>, which allows it to be used in all the places where you'd use a normal <code>Promise</code>. For instance, you can <code>await</code> it. But, in addition to that, an RPC promise also acts like a stub. Calling any method name on the promise forms a speculative call on the promise's eventual result. This is known as &quot;promise pipelining&quot;.</p>
<p>This works when calling properties of objects returned by RPC methods as well. For example:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17118.md")
</div></div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17121.md")
</div></div>
<p>If the initial RPC ends up throwing an exception, then any pipelined calls will also fail with the same exception</p>
<h2 id="readablestream-writablestream-request-and-response">ReadableStream, WritableStream, Request and Response</h2>
<p>You can send and receive <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>, <a href="/workers/runtime-apis/streams/writablestream/"><code>WritableStream</code></a>, <a href="/workers/runtime-apis/request/"><code>Request</code></a>, and <a href="/workers/runtime-apis/response/"><code>Response</code></a> using RPC methods. When doing so, bytes in the body are automatically streamed with appropriate flow control. This allows you to send messages over RPC which are larger than <a href="#limitations">the typical 32 MiB limit</a>.</p>
<p>Only <a href="https://developer.mozilla.org/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams">byte-oriented streams</a> (streams with an underlying byte source of <code>type: &quot;bytes&quot;</code>) are supported.</p>
<p>In all cases, ownership of the stream is transferred to the recipient. The sender can no longer read/write the stream after sending it. If the sender wishes to keep its own copy, it can use the <a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/tee"><code>tee()</code> method of <code>ReadableStream</code></a> or the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Response/clone"><code>clone()</code> method of <code>Request</code> or <code>Response</code></a>. Keep in mind that doing this may force the system to buffer bytes and lose the benefits of flow control.</p>
<h2 id="forwarding-rpc-stubs">Forwarding RPC stubs</h2>
<p>A stub received over RPC from one Worker can be forwarded over RPC to another Worker.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17124.md")
</div></div>
<p>Here, three different workers are involved:</p>
<ol>
<li>The calling Worker (we'll call this the &quot;introducer&quot;)</li>
<li><code>COUNTER_SERVICE</code></li>
<li><code>ANOTHER_SERVICE</code></li>
</ol>
<p>When <code>ANOTHER_SERVICE</code> calls a method on the <code>counter</code> that is passed to it, this call will automatically be proxied through the introducer and on to the <a href="/workers/runtime-apis/rpc/"><code>RpcTarget</code></a> class implemented by <code>COUNTER_SERVICE</code>.</p>
<p>In this way, the introducer Worker can connect two Workers that did not otherwise have any ability to form direct connections to each other.</p>
<p>Currently, this proxying only lasts until the end of the Workers' execution contexts. A proxy connection cannot be persisted for later use.</p>
<h2 id="video-tutorial">Video Tutorial</h2>
<p>In this video, we explore how Cloudflare Workers support Remote Procedure Calls (RPC) to simplify communication between Workers. Learn how to implement RPC in your JavaScript applications and build serverless solutions with ease. Whether you're managing microservices or optimizing web architecture, this tutorial will show you how to quickly set up and use Cloudflare Workers for RPC calls. By the end of this video, you'll understand how to call functions between Workers, pass functions as arguments, and implement user authentication with Cloudflare Workers.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/Ei8VRDNoD7I" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="more-details">More Details</h2>
<ul class="directory-listing"><li><a href="/workers/runtime-apis/rpc/lifecycle/">Lifecycle</a></li><li><a href="/workers/runtime-apis/rpc/reserved-methods/">Reserved Methods</a></li><li><a href="/workers/runtime-apis/rpc/visibility/">Visibility and Security Model</a></li><li><a href="/workers/runtime-apis/rpc/typescript/">TypeScript</a></li><li><a href="/workers/runtime-apis/rpc/error-handling/">Error handling</a></li></ul>
<h2 id="limitations">Limitations</h2>
<ul>
<li>
<p><a href="/workers/configuration/placement/">Smart Placement</a> is currently ignored when making RPC calls. If Smart Placement is enabled for Worker A, and Worker B declares a <a href="/workers/runtime-apis/bindings">Service Binding</a> to it, when Worker B calls Worker A via RPC, Worker A will run locally, on the same machine.</p>
</li>
<li>
<p>The maximum serialized RPC limit is 32 MiB. Consider using <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a> when returning more data.</p>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17125.md")
</div>
