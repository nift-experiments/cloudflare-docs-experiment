<p>Cloudflare Workers provides support for Rust via the <a href="https://github.com/cloudflare/workers-rs"><code>workers-rs</code> crate</a>, which makes <a href="/workers/runtime-apis">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">bindings</a> to developer platform products, such as <a href="/kv/concepts/how-kv-works/">Workers KV</a>, <a href="/r2/">R2</a>, and <a href="/queues/">Queues</a>, available directly from your Rust code.</p>
<p>By following this guide, you will learn how to build a Worker entirely in the Rust programming language.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before starting this guide, make sure you have:</p>
<ul>
<li>A recent version of <a href="https://rustup.rs/"><code>Rust</code></a></li>
<li><a href="https://docs.npmjs.com/getting-started"><code>npm</code></a></li>
<li>The Rust <code>wasm32-unknown-unknown</code> toolchain:</li>
</ul>
<pre><code class="language-sh">rustup target add wasm32-unknown-unknown&#10;</code></pre>
<ul>
<li>And <code>cargo-generate</code> sub-command by running:</li>
</ul>
<pre><code class="language-sh">cargo install cargo-generate&#10;</code></pre>
<h2 id="1-create-a-new-project-with-wrangler"><ol>
<li>Create a new project with Wrangler</li>
</ol></h2>
<p>Open a terminal window, and run the following command to generate a Worker project template in Rust:</p>
<pre><code class="language-sh">cargo generate cloudflare/workers-rs&#10;</code></pre>
<p>Your project will be created in a new directory that you named, in which you will find the following files and folders:</p>
<ul>
<li><code>Cargo.toml</code> - The standard project configuration file for Rust's <a href="https://doc.rust-lang.org/cargo/"><code>Cargo</code></a> package manager. The template pre-populates some best-practice settings for building for Wasm on Workers.</li>
<li><code>wrangler.toml</code> - Wrangler configuration, pre-populated with a custom build command to invoke <code>worker-build</code> (Refer to <a href="/workers/languages/rust/#bundling-worker-build">Wrangler Bundling</a>).</li>
<li><code>src</code> - Rust source directory, pre-populated with Hello World Worker.</li>
</ul>
<h2 id="2-develop-locally"><ol start="2">
<li>Develop locally</li>
</ol></h2>
<p>After you have created your first Worker, run the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> command to start a local server for developing your Worker. This will allow you to test your Worker in development.</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>If you have not used Wrangler before, it will try to open your web browser to login with your Cloudflare account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17003.md")
</aside>
<p>Go to <a href="http://localhost:8787">http://localhost:8787</a> to review your Worker running. Any changes you make to your code will trigger a rebuild, and reloading the page will show you the up-to-date output of your Worker.</p>
<h2 id="3-write-your-worker-code"><ol start="3">
<li>Write your Worker code</li>
</ol></h2>
<p>With your new project generated, write your Worker code. Find the entrypoint to your Worker in <code>src/lib.rs</code>:</p>
<pre><code class="language-rust">use worker::*;&#10;&#10;&#35;[event(fetch)]&#10;async fn main(req: Request, env: Env, ctx: Context) -&gt; Result&lt;Response&gt; {&#10;    Response::ok(&quot;Hello, World!&quot;)&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17002.md")
</aside>
<h3 id="related-runtime-apis">Related runtime APIs</h3>
<p><code>workers-rs</code> provides a runtime API which closely matches Worker's JavaScript API, and enables integration with Worker's platform features. For detailed documentation of the API, refer to <a href="https://docs.rs/worker/latest/worker/"><code>docs.rs/worker</code></a>.</p>
<h4 id="event-macro"><code>event</code> macro</h4>
<p>This macro allows you to define entrypoints to your Worker. The <code>event</code> macro supports the following events:</p>
<ul>
<li><code>fetch</code> - Invoked by an incoming HTTP request.</li>
<li><code>scheduled</code> - Invoked by <a href="/workers/configuration/cron-triggers/"><code>Cron Triggers</code></a>.</li>
<li><code>queue</code> - Invoked by incoming message batches from <a href="/queues/">Queues</a> (Requires <code>queue</code> feature in <code>Cargo.toml</code>, refer to the <a href="https://github.com/cloudflare/workers-rs#queues"><code>workers-rs</code> GitHub repository and <code>queues</code> feature flag</a>).</li>
<li><code>start</code> - Invoked when the Worker is first launched (such as, to install panic hooks).</li>
</ul>
<h4 id="fetch-parameters"><code>fetch</code> parameters</h4>
<p>The <code>fetch</code> handler provides three arguments which match the JavaScript API:</p>
<ol>
<li><strong><a href="https://docs.rs/worker/latest/worker/struct.Request.html"><code>Request</code></a></strong></li>
</ol>
<p>An object representing the incoming request. This includes methods for accessing headers, method, path, Cloudflare properties, and body (with support for asynchronous streaming and JSON deserialization with <a href="https://serde.rs/">Serde</a>).</p>
<ol start="2">
<li><strong><a href="https://docs.rs/worker/latest/worker/struct.Env.html"><code>Env</code></a></strong></li>
</ol>
<p>Provides access to Worker <a href="/workers/runtime-apis/bindings/">bindings</a>.</p>
<ul>
<li><a href="https://docs.rs/worker/latest/worker/struct.Secret.html"><code>Secret</code></a> - Secret value configured in Cloudflare dashboard or using <code>wrangler secret put</code>.</li>
<li><a href="https://docs.rs/worker/latest/worker/type.Var.html"><code>Var</code></a> - Environment variable defined in <code>wrangler.toml</code>.</li>
<li><a href="https://docs.rs/worker/latest/worker/kv/struct.KvStore.html"><code>KvStore</code></a> - Workers <a href="/kv/api/">KV</a> namespace binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/durable/struct.ObjectNamespace.html"><code>ObjectNamespace</code></a> - <a href="/durable-objects/">Durable Object</a> binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.Fetcher.html"><code>Fetcher</code></a> - <a href="/workers/runtime-apis/bindings/service-bindings/">Service binding</a> to another Worker.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.Bucket.html"><code>Bucket</code></a> - <a href="/r2/">R2</a> Bucket binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/d1/struct.D1Database.html"><code>D1Database</code></a> - <a href="/d1/">D1</a> database binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.Queue.html"><code>Queue</code></a> - <a href="/queues/">Queues</a> producer binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.Ai.html"><code>Ai</code></a> - <a href="/workers-ai/">Workers AI</a> binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.Hyperdrive.html"><code>Hyperdrive</code></a> - <a href="/hyperdrive/">Hyperdrive</a> binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.AnalyticsEngineDataset.html"><code>AnalyticsEngineDataset</code></a> - <a href="/analytics/analytics-engine/">Analytics Engine</a> binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.DynamicDispatcher.html"><code>DynamicDispatcher</code></a> - <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic Dispatch</a> binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.SecretStore.html"><code>SecretStore</code></a> - <a href="/secrets-store/">Secrets Store</a> binding.</li>
<li><a href="https://docs.rs/worker/latest/worker/struct.RateLimiter.html"><code>RateLimiter</code></a> - <a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting</a> binding.</li>
</ul>
<ol start="3">
<li><strong><a href="https://docs.rs/worker/latest/worker/struct.Context.html"><code>Context</code></a></strong></li>
</ol>
<p>Provides access to <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> (deferred asynchronous tasks) and <a href="/workers/runtime-apis/context/#passthroughonexception"><code>passThroughOnException</code></a> (fail open) functionality.</p>
<h4 id="response-https-docs-rs-worker-latest-worker-struct-response-html"><a href="https://docs.rs/worker/latest/worker/struct.Response.html"><code>Response</code></a></h4>
<p>The <code>fetch</code> handler expects a <a href="https://docs.rs/worker/latest/worker/struct.Response.html"><code>Response</code></a> return type, which includes support for streaming responses to the client asynchronously. This is also the return type of any subrequests made from your Worker. There are methods for accessing status code and headers, as well as streaming the body asynchronously or deserializing from JSON using <a href="https://serde.rs/">Serde</a>.</p>
<h4 id="router"><code>Router</code></h4>
<p>Implements convenient <a href="https://docs.rs/worker/latest/worker/struct.Router.html">routing API</a> to serve multiple paths from one Worker. Refer to the <a href="https://github.com/cloudflare/workers-rs#or-use-the-router"><code>Router</code> example in the <code>worker-rs</code> GitHub repository</a>.</p>
<h2 id="4-deploy-your-worker-project"><ol start="4">
<li>Deploy your Worker project</li>
</ol></h2>
<p>With your project configured, you can now deploy your Worker, to a <code>*.workers.dev</code> subdomain, or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>, if you have one configured. If you have not configured any subdomain or domain, Wrangler will prompt you during the deployment process to set one up.</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Preview your Worker at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17001.md")
</aside>
<p>After completing these steps, you will have a basic Rust-based Worker deployed. From here, you can add create dependencies and write code in Rust to implement your Worker application. If you would like to know more about the inner workings of how Rust compiled to Wasm is supported by Workers, the next section outlines the libraries and tools involved.</p>
<h2 id="how-this-deployment-works">How this deployment works</h2>
<p>Wasm Workers are invoked from a JavaScript entrypoint script which is created automatically for you when using <code>workers-rs</code>.</p>
<h3 id="javascript-plumbing-wasm-bindgen">JavaScript Plumbing (<code>wasm-bindgen</code>)</h3>
<p>To access platform features such as bindings, Wasm Workers must be able to access methods from the JavaScript runtime API.</p>
<p>This interoperability is achieved using <a href="https://wasm-bindgen.github.io/wasm-bindgen/"><code>wasm-bindgen</code></a>, which provides the glue code needed to import runtime APIs to, and export event handlers from, the Wasm module. <code>wasm-bindgen</code> also provides <a href="https://docs.rs/js-sys/latest/js_sys/"><code>js-sys</code></a>, which implements types for interacting with JavaScript objects. In practice, this is an implementation detail, as <code>workers-rs</code>'s API handles conversion to and from JavaScript objects, and interaction with imported JavaScript runtime APIs for you.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17000.md")
</aside>
<h3 id="async-wasm-bindgen-futures">Async (<code>wasm-bindgen-futures</code>)</h3>
<p><a href="https://wasm-bindgen.github.io/wasm-bindgen/api/wasm_bindgen_futures/"><code>wasm-bindgen-futures</code></a> (part of the <code>wasm-bindgen</code> project) provides interoperability between Rust
Futures and JavaScript Promises. <code>workers-rs</code> invokes the entire event handler function using <code>spawn_local</code>, meaning that you can program using async Rust, which is turned
into a single JavaScript Promise and run on the JavaScript event loop. Calls to imported JavaScript runtime APIs are automatically converted to Rust Futures that can be invoked from async Rust functions.</p>
<h3 id="bundling-worker-build">Bundling (<code>worker-build</code>)</h3>
<p>To run the resulting Wasm binary on Workers, <code>workers-rs</code> includes a build tool called <a href="https://github.com/cloudflare/workers-rs/tree/main/worker-build"><code>worker-build</code></a> which:</p>
<ol>
<li>Creates a JavaScript entrypoint script that properly invokes the module using <code>wasm-bindgen</code>'s JavaScript API.</li>
<li>Invokes <code>web-pack</code> to minify and bundle the JavaScript code.</li>
<li>Outputs a directory structure that Wrangler can use to bundle and deploy the final Worker.</li>
</ol>
<p><code>worker-build</code> is invoked by default in the template project using a custom build command specified in the <code>wrangler.toml</code> file.</p>
<h3 id="binary-size-wasm-opt">Binary Size (<code>wasm-opt</code>)</h3>
<p>Unoptimized Rust Wasm binaries can be large and may exceed Worker bundle size limits or experience long startup times. The template project pre-configures several useful size optimizations in your <code>Cargo.toml</code> file:</p>
<pre><code class="language-toml">[profile.release]&#10;lto = true&#10;strip = true&#10;codegen-units = 1&#10;</code></pre>
<p>Finally, <code>worker-bundle</code> automatically invokes <a href="https://github.com/brson/wasm-opt-rs"><code>wasm-opt</code></a> to further optimize binary size before upload.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://rustwasm.github.io/docs/book/">Rust Wasm Book</a></li>
</ul>
