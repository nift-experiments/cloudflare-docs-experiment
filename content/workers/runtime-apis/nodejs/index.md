---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/
  description: Node.js APIs available in Cloudflare Workers
  full_title: Node.js compatibility · Cloudflare Workers docs
  head_html: <title>Node.js compatibility · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Node.js APIs available in Cloudflare Workers"><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/index.md"><meta property="og:title" content="Node.js compatibility · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Node.js APIs available in Cloudflare Workers"><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/#page","headline":"Node.js compatibility \u00b7 Cloudflare Workers docs","description":"Node.js APIs available in Cloudflare Workers","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/
  schema: 1
---
<p>When you write a Worker, you may need to import packages from <a href="https://www.npmjs.com/">npm</a>. Many npm packages rely on APIs from the <a href="https://nodejs.org/en/about">Node.js runtime</a>, and will not work unless these Node.js APIs are available.</p>
<p>Cloudflare Workers provides a subset of Node.js APIs in two forms:</p>
<ol>
<li>As built-in APIs provided by the Workers Runtime. Most of these APIs are
full implementations of the corresponding Node.js APIs, while a few are
partially supported.</li>
<li>As polyfill shim implementations that <a href="/workers/wrangler/">Wrangler</a> adds to your Worker's code, allowing it to import the module, but calling API methods will throw errors.</li>
</ol>
<h2 id="get-started">Get Started</h2>
<p>For compatibility dates of <code>2026-08-04</code> or later, Workers enables both <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> by default. Built-in Node.js APIs and polyfills are available without additional configuration.</p>
<p>For these compatibility dates, <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> are not used because the compatibility date enables the same behavior. Existing projects do not need to remove these flags when updating their compatibility date. Omit them from new configurations.</p>
<p>For compatibility dates from <code>2024-09-23</code> through <code>2026-08-03</code>, add the <code>nodejs_compat</code> compatibility flag to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to opt in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17143.md")
</div>
<p>To turn off Node.js compatibility completely with a compatibility date of <code>2026-08-04</code> or later, remove the positive flags if present. Then add both <code>no_nodejs_compat</code> and <code>no_nodejs_compat_v2</code>. For configuration examples, refer to the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>.</p>
<h2 id="supported-node-js-apis">Supported Node.js APIs</h2>
<p>The runtime APIs from Node.js listed in this section with the status &quot;🟢 supported&quot; are currently natively supported in the Workers Runtime. Items listed as &quot;🟡 partially supported&quot; include usable APIs, but do not implement the complete Node.js API surface.</p>
<p><a href="https://nodejs.org/docs/latest/api/documentation.html#stability-index">Deprecated or experimental APIs from Node.js</a>, and APIs that do not fit in a serverless context, are not included in the supported API list in this section. Some import-only stubs for these APIs are listed separately in <a href="#non-functional-stub-modules">Non-functional stub modules</a>.</p>
<table>
<thead>
<tr>
<th>API Name</th>
<th>Natively supported by the Workers Runtime</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/runtime-apis/nodejs/assert/">Assertion testing</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/asynclocalstorage/">Asynchronous context tracking</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/buffer/">Buffer</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/console.html">Console</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/crypto/">Crypto</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/observability/dev-tools/">Debugger</a></td>
<td>🟢 supported via <a href="/workers/observability/dev-tools/">Chrome DevTools integration</a></td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/diagnostics-channel/">Diagnostics Channel</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/dns/">DNS</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td>Errors</td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/eventemitter/">Events</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/fs/">File system</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td>Globals</td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/http/">HTTP</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/https/">HTTPS</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/module.html">Module</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/net/">Net</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/os.html">OS</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/path/">Path</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/perf_hooks.html">Performance hooks</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/process/">Process</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/punycode.html">Punycode</a> (deprecated)</td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/querystring.html">Query strings</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/streams/">Stream</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/string-decoder/">String decoder</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/test/">Test runner</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/timers/">Timers</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/tls/">TLS/SSL</a></td>
<td>🟡 partially supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/url/">URL</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/util/">Utilities</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/web-crypto/">Web Crypto API</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/streams/">Web Streams API</a></td>
<td>🟢 supported</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/zlib/">Zlib</a></td>
<td>🟢 supported</td>
</tr>
</tbody>
</table>
<p>Unless otherwise specified, native implementations of Node.js APIs in Workers are intended to match the implementation in the <a href="https://github.com/nodejs/release#release-schedule">Current release of Node.js</a>.</p>
<p>If an API you wish to use is missing and you want to suggest that Workers support it, please add a post or comment in the
<a href="https://github.com/cloudflare/workerd/discussions/categories/node-js-apis">Node.js APIs discussions category</a> on GitHub.</p>
<h3 id="non-functional-stub-modules">Non-functional stub modules</h3>
<p>Some Node.js modules are available as non-functional stubs. A stub can be imported or required, but does not provide a working implementation of the underlying Node.js API. These stubs exist so packages that check for the presence of a module can load in Workers, but they are not suitable for direct use in application code.</p>
<p>The following stubs are enabled automatically only when the <code>nodejs_compat</code> compatibility flag is enabled and your Worker's compatibility date is on or after the date shown. To enable one earlier, add the corresponding enable flag. To keep one unavailable after that date, add the corresponding disable flag.</p>
<table>
<thead>
<tr>
<th>Stub module</th>
<th>Enabled with <code>nodejs_compat</code> on or after</th>
<th>Enable flag</th>
<th>Disable flag</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/http2.html"><code>node:http2</code></a></td>
<td><code>2025-09-01</code></td>
<td><code>enable_nodejs_http2_module</code></td>
<td><code>disable_nodejs_http2_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/vm.html"><code>node:vm</code></a></td>
<td><code>2025-10-01</code></td>
<td><code>enable_nodejs_vm_module</code></td>
<td><code>disable_nodejs_vm_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/cluster.html"><code>node:cluster</code></a></td>
<td><code>2025-12-04</code></td>
<td><code>enable_nodejs_cluster_module</code></td>
<td><code>disable_nodejs_cluster_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/domain.html"><code>node:domain</code></a></td>
<td><code>2025-12-04</code></td>
<td><code>enable_nodejs_domain_module</code></td>
<td><code>disable_nodejs_domain_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/tracing.html"><code>node:trace_events</code></a></td>
<td><code>2025-12-04</code></td>
<td><code>enable_nodejs_trace_events_module</code></td>
<td><code>disable_nodejs_trace_events_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/wasi.html"><code>node:wasi</code></a></td>
<td><code>2025-12-04</code></td>
<td><code>enable_nodejs_wasi_module</code></td>
<td><code>disable_nodejs_wasi_module</code></td>
</tr>
<tr>
<td><code>node:_stream_wrap</code></td>
<td><code>2026-01-29</code></td>
<td><code>enable_nodejs_stream_wrap_module</code></td>
<td><code>disable_nodejs_stream_wrap_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/dgram.html"><code>node:dgram</code></a></td>
<td><code>2026-01-29</code></td>
<td><code>enable_nodejs_dgram_module</code></td>
<td><code>disable_nodejs_dgram_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/inspector.html"><code>node:inspector</code></a></td>
<td><code>2026-01-29</code></td>
<td><code>enable_nodejs_inspector_module</code></td>
<td><code>disable_nodejs_inspector_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/sqlite.html"><code>node:sqlite</code></a></td>
<td><code>2026-01-29</code></td>
<td><code>enable_nodejs_sqlite_module</code></td>
<td><code>disable_nodejs_sqlite_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/child_process.html"><code>node:child_process</code></a></td>
<td><code>2026-03-17</code></td>
<td><code>enable_nodejs_child_process_module</code></td>
<td><code>disable_nodejs_child_process_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/readline.html"><code>node:readline</code></a></td>
<td><code>2026-03-17</code></td>
<td><code>enable_nodejs_readline_module</code></td>
<td><code>disable_nodejs_readline_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/repl.html"><code>node:repl</code></a></td>
<td><code>2026-03-17</code></td>
<td><code>enable_nodejs_repl_module</code></td>
<td><code>disable_nodejs_repl_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/tty.html"><code>node:tty</code></a></td>
<td><code>2026-03-17</code></td>
<td><code>enable_nodejs_tty_module</code></td>
<td><code>disable_nodejs_tty_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/v8.html"><code>node:v8</code></a></td>
<td><code>2026-03-17</code></td>
<td><code>enable_nodejs_v8_module</code></td>
<td><code>disable_nodejs_v8_module</code></td>
</tr>
<tr>
<td><a href="https://nodejs.org/docs/latest/api/worker_threads.html"><code>node:worker_threads</code></a></td>
<td><code>2026-03-17</code></td>
<td><code>enable_nodejs_worker_threads_module</code></td>
<td><code>disable_nodejs_worker_threads_module</code></td>
</tr>
</tbody>
</table>
<h3 id="node-js-api-polyfills">Node.js API Polyfills</h3>
<p>Node.js APIs that are not yet supported in the Workers runtime are polyfilled via <a href="/workers/wrangler/">Wrangler</a>, which uses <a href="https://github.com/unjs/unenv">unenv</a>. If the <code>nodejs_compat</code> <a href="/workers/configuration/compatibility-flags/">compatibility flag</a> is enabled, and your Worker's <a href="/workers/configuration/compatibility-dates/">compatibility date</a> is 2024-09-23 or later, Wrangler will automatically inject polyfills into your Worker's code.</p>
<p>Adding polyfills maximizes compatibility with existing npm packages by providing modules with mocked methods. Calling these mocked methods will either noop or will throw an error with a message like:</p>
<pre tabindex="0"><code>[unenv] &lt;method name&gt; is not implemented yet!&#10;</code></pre>
<p>This allows you to import packages that use these Node.js modules, even if certain methods are not supported.</p>
<h2 id="enable-only-asynclocalstorage">Enable only AsyncLocalStorage</h2>
<p>If you need to enable only the Node.js <code>AsyncLocalStorage</code> API, you can enable the <code>nodejs_als</code> compatibility flag:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17144.md")
</div>
