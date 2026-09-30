<p><a href="https://webassembly.org/">WebAssembly</a> (abbreviated Wasm) allows you to compile languages like <a href="/workers/languages/rust/">Rust</a>, Go, or C to a binary format that can run in a wide variety of environments, including <a href="https://developer.mozilla.org/en-US/docs/WebAssembly#browser_compatibility">web browsers</a>, Cloudflare Workers, and other WebAssembly runtimes.</p>
<p>You can use WebAssembly to:</p>
<ul>
<li>Execute code written in a language other than JavaScript, via <code>WebAssembly.instantiate()</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17063.md")
</aside>
<ul>
<li>Write an entire Cloudflare Worker in Rust, using bindings that make Workers' JavaScript APIs available directly from your Rust code.</li>
</ul>
<p>Most programming languages can be compiled to Wasm, although support varies across languages and compilers. Guides are available for the following languages:</p>
<ul class="directory-listing"><li><a href="/workers/runtime-apis/webassembly/javascript/">Wasm in JavaScript</a></li></ul>
<h2 id="supported-proposals">Supported proposals</h2>
<p>WebAssembly is a rapidly evolving set of standards, with <a href="https://webassembly.org/roadmap/">many proposed APIs</a> which are in various stages of development. In general, Workers supports the same set of features that are available in Google Chrome.</p>
<h3 id="simd">SIMD</h3>
<p>SIMD is supported on Workers. For more information on using SIMD in WebAssembly, refer to <a href="https://v8.dev/features/simd">Fast, parallel applications with WebAssembly SIMD</a>.</p>
<h3 id="threading">Threading</h3>
<p>Threading is not possible in Workers. Each Worker runs in a single thread, and the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API">Web Worker</a> API is not supported.</p>
<h2 id="binary-size">Binary size</h2>
<p>Compiling to WebAssembly often requires including additional runtime dependencies. As a result, Workers that use WebAssembly are typically larger than an equivalent Worker written in JavaScript. The larger your Worker is, the longer it may take your Worker to start. Refer to <a href="https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time">Worker startup time</a> for more information. We recommend using tools like <a href="https://github.com/brson/wasm-opt-rs"><code>wasm-opt</code></a> to optimize the size of your Wasm binary.</p>
<h2 id="webassembly-system-interface-wasi">WebAssembly System Interface (WASI)</h2>
<p>The <a href="https://wasi.dev/">WebAssembly System Interface</a> (abbreviated WASI) is a modular system interface for WebAssembly that standardizes a set of underlying system calls for networking, file system access, and more. Applications can depend on the WebAssembly System Interface to behave identically across host environments and operating systems.</p>
<p>WASI is an earlier and more rapidly evolving set of standards than Wasm. WASI support is experimental on Cloudflare Workers, with only some syscalls implemented. Refer to our <a href="https://github.com/cloudflare/workers-wasi">open source implementation of WASI</a>, and <a href="https://blog.cloudflare.com/announcing-wasi-on-workers/">blog post about WASI on Workers</a> demonstrating its use.</p>
<h3 id="resources-on-webassembly">Resources on WebAssembly</h3>
<ul>
<li><a href="https://blog.cloudflare.com/cloudflare-workers-as-a-serverless-rust-platform/">Serverless Rust with Cloudflare Workers</a></li>
<li><a href="https://blog.cloudflare.com/webassembly-on-cloudflare-workers/">WebAssembly on Cloudflare Workers</a></li>
</ul>
