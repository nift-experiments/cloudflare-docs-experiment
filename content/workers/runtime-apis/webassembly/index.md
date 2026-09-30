---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/webassembly/
  description: Execute code written in a language other than JavaScript or write an entire Cloudflare Worker in Rust.
  full_title: WebAssembly (Wasm) · Cloudflare Workers docs
  head_html: <title>WebAssembly (Wasm) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Execute code written in a language other than JavaScript or write an entire Cloudflare Worker in Rust."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/webassembly/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/webassembly/index.md"><meta property="og:title" content="WebAssembly (Wasm) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Execute code written in a language other than JavaScript or write an entire Cloudflare Worker in Rust."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/webassembly/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/webassembly/#page","headline":"WebAssembly (Wasm) \u00b7 Cloudflare Workers docs","description":"Execute code written in a language other than JavaScript or write an entire Cloudflare Worker in Rust.","url":"https://developers.cloudflare.com/workers/runtime-apis/webassembly/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/webassembly/
  schema: 1
---
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
