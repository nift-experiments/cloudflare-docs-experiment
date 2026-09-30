<p>Though Cloudflare Workers behave similarly to <a href="https://www.cloudflare.com/learning/serverless/serverless-javascript/">JavaScript</a> in the browser or in Node.js, there are a few differences in how you have to think about your code. Under the hood, the Workers runtime uses the <a href="https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/">V8 engine</a> — the same engine used by Chromium and Node.js. The Workers runtime also implements many of the standard <a href="/workers/runtime-apis/">APIs</a> available in most modern browsers.</p>
<p>The differences between JavaScript written for the browser or Node.js happen at runtime. Rather than running on an individual's machine (for example, <a href="https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/">a browser application or on a centralized server</a>), Workers functions run on <a href="https://www.cloudflare.com/network">Cloudflare's global network</a> - a growing global network of thousands of machines distributed across hundreds of locations.</p>
<p>Each of these machines hosts an instance of the Workers runtime, and each of those runtimes is capable of running thousands of user-defined applications. This guide will review some of those differences.</p>
<p>For more information, refer to the <a href="https://blog.cloudflare.com/cloud-computing-without-containers">Cloud Computing without Containers blog post</a>.</p>
<p>The three largest differences are: Isolates, Compute per Request, and Distributed Execution.</p>
<h2 id="isolates">Isolates</h2>
<p><a href="https://v8.dev">V8</a> orchestrates isolates: lightweight contexts that provide your code with variables it can access and a safe environment to be executed within. You could even consider an isolate a sandbox for your function to run in.</p>
<p>A single instance of the runtime can run hundreds or thousands of isolates, seamlessly switching between them. Each isolate's memory is completely isolated, so each piece of code is protected from other untrusted or user-written code on the runtime. Isolates are also designed to start very quickly. Instead of creating a virtual machine for each function, an isolate is created within an existing environment. This model eliminates the cold starts of the virtual machine model.</p>
<p>Unlike other serverless providers which use <a href="https://www.cloudflare.com/learning/serverless/serverless-vs-containers/">containerized processes</a> each running an instance of a language runtime, Workers pays the overhead of a JavaScript runtime once on the start of a container. Workers processes are able to run essentially limitless scripts with almost no individual overhead. Any given isolate can start around a hundred times faster than a Node process on a container or virtual machine. Notably, on startup isolates consume an order of magnitude less memory.</p>
<div class="nb-interactive-component" data-cf-component="WorkersIsolateDiagram"></div>
<p>A given isolate has its own scope, but isolates are not necessarily long-lived. An isolate may be spun down and evicted for a number of reasons:</p>
<ul>
<li>Resource limitations on the machine.</li>
<li>A suspicious script - anything seen as trying to break out of the isolate sandbox.</li>
<li>Individual <a href="/workers/platform/limits/">resource limits</a>.</li>
</ul>
<p>Because of this, it is generally advised that you not store mutable state in your global scope unless you have accounted for this contingency.</p>
<p>If you are interested in how Cloudflare handles security with the Workers runtime, you can <a href="/workers/reference/security-model/">read more about how Isolates relate to Security and Spectre Threat Mitigation</a>.</p>
<h2 id="compute-per-request">Compute per request</h2>
<p>Most Workers are a variation on the default Workers flow:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16180.md")
</div></div>
<p>For Workers written in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a>, when a request to your <code>*.workers.dev</code> subdomain or to your Cloudflare-managed domain is received by any of Cloudflare's data centers, the request invokes the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a> defined in your Worker code with the given request. You can respond to the request by returning a <a href="/workers/runtime-apis/response/"><code>Response</code></a> object.</p>
<h2 id="distributed-execution">Distributed execution</h2>
<p>Isolates are resilient and continuously available for the duration of a request, but in rare instances isolates may be evicted. When a Worker hits official <a href="/workers/platform/limits/">limits</a> or when resources are exceptionally tight on the machine the request is running on, the runtime will selectively evict isolates after their events are properly resolved.</p>
<p>Like all other JavaScript platforms, a single Workers instance may handle multiple requests including concurrent requests in a single-threaded event loop. That means that other requests may (or may not) be processed during awaiting any <code>async</code> tasks (such as <code>fetch</code>) if other requests come in while processing a request.
Because there is no guarantee that any two user requests will be routed to the same or a different instance of your Worker, Cloudflare recommends you do not use or mutate global state.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a> - Review how incoming HTTP requests to a Worker are passed to the <code>fetch()</code> handler.</li>
<li><a href="/workers/runtime-apis/request/">Request</a> - Learn how incoming HTTP requests are passed to the <code>fetch()</code> handler.</li>
<li><a href="/workers/platform/limits/">Workers limits</a> - Learn about Workers limits including Worker size, startup time, and more.</li>
</ul>
