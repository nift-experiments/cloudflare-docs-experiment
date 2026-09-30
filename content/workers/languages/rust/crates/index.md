<h2 id="background">Background</h2>
<p>Learn about popular Rust crates which have been confirmed to work on Workers when using <a href="https://github.com/cloudflare/workers-rs"><code>workers-rs</code></a> (or in some cases just <code>wasm-bindgen</code>), to write Workers in WebAssembly.
Each Rust crate example includes any custom configuration that is required.</p>
<p>This is not an exhaustive list, many Rust crates can be compiled to the <a href="https://doc.rust-lang.org/rustc/platform-support/wasm64-unknown-unknown.html"><code>wasm32-unknown-unknown</code></a> target that is supported by Workers.
In some cases, this may require disabling default features or enabling a Wasm-specific feature. It is important to consider the addition of new dependencies, as this can significantly increase the <a href="/workers/platform/limits/#worker-size">size</a> of your Worker.</p>
<h2 id="time"><code>time</code></h2>
<p>Many crates which have been made Wasm-friendly, will use the <code>time</code> crate instead of <code>std::time</code>. For the <code>time</code> crate to work in Wasm, the <code>wasm-bindgen</code> feature must be enabled to obtain timing information from JavaScript.</p>
<h2 id="tracing"><code>tracing</code></h2>
<p>Tracing can be enabled by using the <code>tracing-web</code> crate and the <code>time</code> feature for <code>tracing-subscriber</code>.
Due to <a href="/workers/reference/security-model/#step-1-disallow-timers-and-multi-threading">timing limitations</a> on Workers, spans will have identical start and end times unless they encompass I/O.</p>
<p><a href="https://github.com/cloudflare/workers-rs/tree/main/examples/tracing">Refer to the <code>tracing</code> example</a> for more information.</p>
<h2 id="reqwest"><code>reqwest</code></h2>
<p>The <a href="https://docs.rs/reqwest/latest/reqwest/"><code>reqwest</code> library</a> can be compiled to Wasm, and hooks into the JavaScript <code>fetch</code> API automatically using <code>wasm-bindgen</code>.</p>
<h2 id="tokio-postgres"><code>tokio-postgres</code></h2>
<p><code>tokio-postgres</code> can be compiled to Wasm. It must be configured to use a <code>Socket</code> from <code>workers-rs</code>:</p>
<p><a href="https://github.com/cloudflare/workers-rs/tree/main/examples/tokio-postgres">Refer to the <code>tokio-postgres</code> example</a> for more information.</p>
<h2 id="hyper"><code>hyper</code></h2>
<p>The <code>hyper</code> crate contains two HTTP clients, the lower-level <code>conn</code> module and the higher-level <code>Client</code>.
The <code>conn</code> module can be used with Workers <code>Socket</code>, however <code>Client</code> requires timing dependencies which are
not yet Wasm friendly.</p>
<p><a href="https://github.com/cloudflare/workers-rs/tree/main/examples/hyper">Refer to the <code>hyper</code> example</a> for more information.</p>
