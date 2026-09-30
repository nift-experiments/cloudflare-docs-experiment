<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 19, 2025</time><h2 id="post-title">Panic Recovery for Rust Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>In <a href="https://github.com/cloudflare/workers-rs">workers-rs</a>, Rust panics were previously non-recoverable. A panic would put the Worker into an invalid state, and further function calls could result in memory overflows or exceptions.</p>
<p>Now, when a panic occurs, in-flight requests will throw 500 errors, but the Worker will automatically and instantly recover for future requests.</p>
<p>This ensures more reliable deployments. Automatic panic recovery is enabled for all new workers-rs deployments as of version 0.6.5, with no configuration required.</p>
<h4 id="fixing-rust-panics-with-wasm-bindgen">Fixing Rust Panics with Wasm Bindgen</h4>
<p>Rust Workers are built with Wasm Bindgen, which treats panics as non-recoverable. After a panic, the entire Wasm application is considered to be in an invalid state.</p>
<p>We now attach a default panic handler in Rust:</p>
<pre><code class="language-rust">std::panic::set_hook(Box::new(move |panic_info| {&#10;  hook_impl(panic_info);&#10;}));&#10;</code></pre>
<p>Which is registered by default in the JS initialization:</p>
<pre><code class="language-js">import { setPanicHook } from &quot;./index.js&quot;;&#10;setPanicHook(function (err) {&#10;	console.error(&quot;Panic handler!&quot;, err);&#10;});&#10;</code></pre>
<p>When a panic occurs, we reset the Wasm state to revert the Wasm application to how it was when the application started.</p>
<h4 id="resetting-vm-state-in-wasm-bindgen">Resetting VM State in Wasm Bindgen</h4>
<p>We worked upstream on the Wasm Bindgen project to implement a new <a href="https://github.com/wasm-bindgen/wasm-bindgen/pull/4644"><code>--experimental-reset-state-function</code> compilation option</a> which outputs a new <code>__wbg_reset_state</code> function.</p>
<p>This function clears all internal state related to the Wasm VM, and updates all function bindings in place to reference the new WebAssembly instance.</p>
<p>One other necessary change here was associating Wasm-created JS objects with an instance identity. If a JS object created by an earlier instance is then passed into a new instance later on, a new &quot;stale object&quot; error is specially thrown when using this feature.</p>
<h4 id="layered-solution">Layered Solution</h4>
<p>Building on this new Wasm Bindgen feature, layered with our new default panic handler, we also added a proxy wrapper to ensure all top-level exported class instantiations (such as for Rust Durable Objects) are tracked and fully reinitialized when resetting the Wasm instance. This was necessary because
the workerd runtime will instantiate exported classes, which would then be associated with the Wasm instance.</p>
<p>This approach now provides full panic recovery for Rust Workers on subsequent requests.</p>
<p>Of course, we never want panics, but when they do happen they are isolated and can be investigated further from the error logs - avoiding broader service disruption.</p>
<h4 id="webassembly-exception-handling">WebAssembly Exception Handling</h4>
<p>In the future, full support for recoverable panics could be implemented without needing reinitialization at all, utilizing the <a href="https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md">WebAssembly Exception Handling</a>
proposal, part of the newly announced <a href="https://webassembly.org/news/2025-09-17-wasm-3.0/">WebAssembly 3.0</a> specification. This would allow unwinding panics as normal JS errors, and concurrent requests would no longer fail.</p>
<p><strong>We're making significant improvements to the reliability of <a href="https://github.com/cloudflare/workers-rs">Rust Workers</a>. Join us in <code>#rust-on-workers</code> on the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a> to stay updated.</strong></p>
</div></article></div>
