---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/changelog/
  description: Review recent changes to Cloudflare Workers.
  full_title: Workers Changelog · Cloudflare Workers docs
  head_html: <title>Workers Changelog · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/workers/platform/changelog/index.xml"><meta property="og:title" content="Workers Changelog · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/workers/platform/changelog/#page","headline":"Workers Changelog \u00b7 Cloudflare Workers docs","description":"Review recent changes to Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/platform/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/changelog/
  schema: 1
---
<p>This changelog details meaningful changes made to Workers across the Cloudflare dashboard, Wrangler, the API, and the workerd runtime. These changes are not configurable.</p>
<p>This is <em>different</em> from <a href="/workers/configuration/compatibility-dates/">compatibility dates</a> and <a href="/workers/configuration/compatibility-flags/">compatibility flags</a>, which let you explicitly opt-in to or opt-out of specific changes to the Workers Runtime.</p>
<h2 id="2026-08-28">2026-08-28</h2><ul>
<li>Updated v8 to version 15.3.</li>
</ul><h2 id="2026-08-20">2026-08-20</h2><ul>
<li>Increased the Durable Object Dynamic Worker concurrency limit from 4 to 10.</li>
</ul><h2 id="2026-08-18">2026-08-18</h2><ul>
<li>Updated v8 to version 15.2.</li>
</ul><h2 id="2026-07-16">2026-07-16</h2><ul>
<li>Updated v8 to version 15.1.</li>
</ul><h2 id="2026-06-04">2026-06-04</h2><ul>
<li>Updated v8 to version 15.0.</li>
</ul><h2 id="2026-05-13">2026-05-13</h2><ul>
<li>Fixed a regression where passing an array for to/cc/bcc on the SendEmail builder produced &quot;Invalid email address&quot; errors.</li>
</ul><h2 id="2026-04-27">2026-04-27</h2><ul>
<li>Updated v8 to version 14.8.</li>
</ul><h2 id="2026-04-17">2026-04-17</h2><ul>
<li>Updated v8 to version 14.7.</li>
<li>Allow passing custom limits for dynamic workers.</li>
</ul><h2 id="2026-03-20">2026-03-20</h2><ul>
<li>Updated v8 to version 14.6.</li>
</ul><h2 id="2026-01-29">2026-01-29</h2><ul>
<li>Updated v8 to version 14.5.</li>
</ul><h2 id="2026-01-13">2026-01-13</h2><ul>
<li>Updated v8 to version 14.4.</li>
</ul><h2 id="2025-12-19">2025-12-19</h2><ul>
<li>Allow null name when creating dynamic workers.</li>
</ul><h2 id="2025-11-25">2025-11-25</h2><ul>
<li>Updated v8 to version 14.3.</li>
</ul><h2 id="2025-10-25">2025-10-25</h2><ul>
<li>The maximum WebSocket message size limit has been increased from 1 MiB to 32 MiB.</li>
</ul><h2 id="2025-10-22">2025-10-22</h2><ul>
<li>Warnings which were previously only visible via the devtools console in preview sessions are now also sent to the tail Worker, if one is attached.</li>
</ul><h2 id="2025-10-17">2025-10-17</h2><ul>
<li>Updated v8 to version 14.2.</li>
<li>Backported an optimization to <code>JSON.parse()</code>. More details are <a href="https://blog.cloudflare.com/unpacking-cloudflare-workers-cpu-performance-benchmarks/#json-parsing">available in this blog post</a> and <a href="https://chromium-review.googlesource.com/c/v8/v8/+/7027411">the upstream patch</a>.</li>
</ul><h2 id="2025-09-18">2025-09-18</h2><ul>
<li>Updated v8 to version 14.1.</li>
</ul><h2 id="2025-09-11">2025-09-11</h2><ul>
<li>The node:fs and Web File System APIs are now available within Workers.</li>
</ul><h2 id="2025-08-21">2025-08-21</h2><ul>
<li>Updated v8 to version 14.0.</li>
<li><code>Uint8Array</code> type in JavaScript now supports base64 and hex operations.</li>
</ul><h2 id="2025-08-14">2025-08-14</h2><ul>
<li>Enable V8 Sandbox for improved isolation and security.</li>
</ul><h2 id="2025-08-11">2025-08-11</h2><ul>
<li>The MessageChannel and MessagePort APIs are now available in Workers.</li>
</ul><h2 id="2025-06-27">2025-06-27</h2><ul>
<li>Updated v8 to version 13.9.</li>
</ul><h2 id="2025-06-23">2025-06-23</h2><ul>
<li>Enable FinalizationRegistry API. See <a href="https://blog.cloudflare.com/we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it/">We shipped FinalizationRegistry in Workers: why you should never use it</a> for details.</li>
</ul><h2 id="2025-06-04">2025-06-04</h2><ul>
<li>Updated v8 to version 13.8.</li>
</ul><h2 id="2025-05-27">2025-05-27</h2><ul>
<li>Historically, in some cases, the same instance of <code>ctx</code> would be passed to multiple invocations of the event handler. We now always pass a new object for each event. We made this change retroactive to all compatibility dates because we suspect it fixes security bugs in some workers and does not break any worker. However, the old behavior can be restored using the compat flag <code>nonclass_entrypoint_reuses_ctx_across_invocations</code>.</li>
</ul><h2 id="2025-05-22">2025-05-22</h2><ul>
<li>Enabled explicit resource context management and support for Float16Array</li>
</ul><h2 id="2025-05-20">2025-05-20</h2><ul>
<li>Updated v8 to version 13.7.</li>
</ul><h2 id="2025-04-16">2025-04-16</h2><ul>
<li>Updated v8 to version 13.6.</li>
</ul><h2 id="2025-04-14">2025-04-14</h2><ul>
<li>JSRPC message size limit has been increased to 32MiB.</li>
</ul><h2 id="2025-04-03">2025-04-03</h2><ul>
<li>Websocket client exceptions are now JS exceptions rather than internal errors.</li>
</ul><h2 id="2025-03-27">2025-03-27</h2><ul>
<li>Updated v8 to version 13.5.</li>
</ul><h2 id="2025-02-28">2025-02-28</h2><ul>
<li>Updated v8 to version 13.4.</li>
<li>When using <code>nodejs_compat</code>, the new <code>nodejs_compat_populate_process_env</code> compatibility flag will cause <code>process.env</code> to be automatically populated with text bindings configured for the worker.</li>
</ul><h2 id="2025-02-26">2025-02-26</h2><ul>
<li><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports building projects that use <strong>pnpm 10</strong> as the package manager. If your build previously failed due to this unsupported version, retry your build. No config changes needed.</li>
</ul><h2 id="2025-02-13">2025-02-13</h2><ul>
<li><a href="/workers/configuration/placement/">Smart Placement</a> no longer runs Workers in the same location as D1 databases they are bound to. The same <a href="/workers/configuration/placement/#understand-how-smart-placement-works">placement logic</a> now applies to all Workers that use Smart Placement, regardless of whether they use D1 bindings.</li>
</ul><h2 id="2025-02-11">2025-02-11</h2><ul>
<li>When Workers generate an &quot;internal error&quot; exception in response to certain failures, the exception message may provide a reference ID that customers can include in support communication for easier error identification.  For example, an exception with the new message might look like: <code>internal error; reference = 0123456789abcdefghijklmn</code>.</li>
</ul><h2 id="2025-01-31">2025-01-31</h2><ul>
<li>Updated v8 to version 13.3.</li>
</ul><h2 id="2025-01-15">2025-01-15</h2><ul>
<li>The runtime will no longer reuse isolates across worker versions even if the code happens to be identical. This &quot;optimization&quot; was deemed more confusing than it is worth.</li>
</ul><h2 id="2025-01-14">2025-01-14</h2><ul>
<li>Updated v8 to version 13.2.</li>
</ul><h2 id="2024-12-19">2024-12-19</h2><ul>
<li><strong>Cloudflare GitHub App Permissions Update</strong>
<ul>
<li>Cloudflare is requesting updated permissions for the <a href="https://github.com/apps/cloudflare-workers-and-pages">Cloudflare GitHub App</a> to enable features like automatically creating a repository on your GitHub account and deploying the new repository for you when getting started with a template. This feature is coming out soon to support a better onboarding experience.</li>
<li><strong>Requested permissions:</strong>
<ul>
<li><a href="https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-administration">Repository Administration</a> (read/write) to create repositories.</li>
<li><a href="https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-contents">Contents</a> (read/write) to push code to the created repositories.</li>
</ul>
</li>
<li><strong>Who is impacted:</strong>
<ul>
<li>Existing users will be prompted to update permissions when GitHub sends an email with subject &quot;[GitHub] Cloudflare Workers &amp; Pages is requesting updated permission&quot; on December 19th, 2024.</li>
<li>New users installing the app will see the updated permissions during the connecting repository process.</li>
</ul>
</li>
<li><strong>Action:</strong> Review and accept the permissions update to use upcoming features. <em>If you decline or take no action, you can continue connecting repositories and deploying changes via the Cloudflare GitHub App as you do today, but new features requiring these permissions will not be available.</em></li>
<li><strong>Questions?</strong> Visit <a href="https://discord.com/channels/595317990191398933/1313895851520688163">#github-permissions-update</a> in the Cloudflare Developers Discord.</li>
</ul>
</li>
</ul><h2 id="2024-11-18">2024-11-18</h2><ul>
<li>Updated v8 to version 13.1.</li>
</ul><h2 id="2024-11-12">2024-11-12</h2><ul>
<li>Fixes exception seen when trying to call deleteAll() during a SQLite-backed Durable Object's alarm handler.</li>
</ul><h2 id="2024-11-08">2024-11-08</h2><ul>
<li>Update SQLite to version 3.47.</li>
</ul><h2 id="2024-10-21">2024-10-21</h2><ul>
<li>Fixed encoding of WebSocket pong messages when talking to remote servers. Previously, when a Worker made a WebSocket connection to an external server, the server may have prematurely closed the WebSocket for failure to respond correctly to pings. Client-side connections were not affected.</li>
</ul><h2 id="2024-10-14">2024-10-14</h2><ul>
<li>Updated v8 to version 13.0.</li>
</ul><h2 id="2024-09-26">2024-09-26</h2><ul>
<li>You can now connect your GitHub or GitLab repository to an existing Worker to automatically build and deploy your changes when you make a git push with <a href="/workers/ci-cd/builds/">Workers Builds</a>.</li>
</ul><h2 id="2024-09-20">2024-09-20</h2><ul>
<li>Workers now support the [<code>handle_cross_request_promise_resolution</code>] compatibility flag which addresses certain edge cases around awaiting and resolving promises across multiple requests.</li>
</ul><h2 id="2024-09-19">2024-09-19</h2><ul>
<li>Revamped Workers and Pages UI settings to simplify the creation and management of project configurations. For bugs and general feedback, please submit this <a href="https://forms.gle/XXqhRGbZmuzninuN9">form</a>.</li>
</ul><h2 id="2024-09-16">2024-09-16</h2><ul>
<li>Updated v8 to version 12.9.</li>
</ul><h2 id="2024-08-19">2024-08-19</h2><ul>
<li>Workers now support the <a href="/workers/configuration/compatibility-flags/#allow-specifying-a-custom-port-when-making-a-subrequest-with-the-fetch-api"><code>allow_custom_ports</code> compatibility flag</a> which enables using the <code>fetch()</code> calls to custom ports.</li>
</ul><h2 id="2024-08-15">2024-08-15</h2><ul>
<li>Updated v8 to version 12.8.</li>
<li>You can now use <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try"><code>Promise.try()</code></a> in Cloudflare Workers. Refer to <a href="https://github.com/tc39/proposal-promise-try"><code>tc39/proposal-promise-try</code></a> for more context on this API that has recently been added to the JavaScript language.</li>
</ul><h2 id="2024-08-14">2024-08-14</h2><ul>
<li>When using the <code>nodejs_compat_v2</code> compatibility flag, the <code>setImmediate(fn)</code> API from Node.js is now available at the global scope.</li>
<li>The <code>internal_writable_stream_abort_clears_queue</code> compatibility flag will ensure that certain <code>WritableStream</code> <code>abort()</code> operations are handled immediately rather than lazily, ensuring that the stream is appropriately aborted when the consumer of the stream is no longer active.</li>
</ul><h2 id="2024-07-19">2024-07-19</h2><ul>
<li>Workers with the <a href="/workers/runtime-apis/bindings/mtls/">mTLS</a> binding now support <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual Deployments</a>.</li>
</ul><h2 id="2024-07-18">2024-07-18</h2><ul>
<li>Added a new <code>truncated</code> flag to <a href="/workers/observability/logs/tail-workers/">Tail Worker</a> events to indicate when the event buffer is full and events are being dropped.</li>
</ul><h2 id="2024-07-17">2024-07-17</h2><ul>
<li>Updated v8 to version 12.7.</li>
</ul><h2 id="2024-07-03">2024-07-03</h2><ul>
<li>The <a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a> implementation now includes the scrypt(...) and scryptSync(...) APIs.</li>
<li>Workers now support the standard <a href="/workers/runtime-apis/eventsource/">EventSource</a> API.</li>
<li>Fixed a bug where when writing to an HTTP Response body would sometimes hang when the client disconnected (and sometimes throw an exception). It will now always throw an exception.</li>
</ul><h2 id="2024-07-01">2024-07-01</h2><ul>
<li>When using <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual Deployments</a>, you can now use <a href="/workers/versions-and-deployments/version-overrides/">version overrides</a> to send a request to a specific version of your Worker.</li>
</ul><h2 id="2024-06-28">2024-06-28</h2><ul>
<li>Fixed a bug which caused <code>Date.now()</code> to return skewed results if called before the first I/O of the first request after a Worker first started up. The value returned would be offset backwards by the amount of CPU time spent starting the Worker (compiling and running global scope), making it seem like the first I/O (e.g. first fetch()) was slower than it really was. This skew had nothing to do with Spectre mitigations; it was simply a longstanding bug.</li>
</ul><h2 id="2024-06-24">2024-06-24</h2><ul>
<li><a href="/durable-objects/best-practices/error-handling">Exceptions</a> thrown from Durable Object internal operations and tunneled to the caller may now be populated with a <code>.retryable: true</code> property if the exception was likely due to a transient failure, or populated with an <code>.overloaded: true</code> property if the exception was due to <a href="/durable-objects/observability/troubleshooting/#durable-object-is-overloaded">overload</a>.</li>
</ul><h2 id="2024-06-20">2024-06-20</h2><ul>
<li>We now prompt for extra confirmation if attempting to rollback to a version of a Worker using the <a href="/api/resources/workers/subresources/scripts/subresources/deployments/methods/create/">Deployments API</a> where the value of a secret is different than the currently deployed version. A <code>?force=true</code> query parameter can be specified to proceed with the rollback.</li>
</ul><h2 id="2024-06-19">2024-06-19</h2><ul>
<li>When using <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code> compatibility flag</a>, the <code>buffer</code> module now has an implementation of <code>isAscii()</code> and <code>isUtf8()</code> methods.</li>
<li>Fixed a bug where exceptions propagated from <a href="/workers/runtime-apis/rpc">JS RPC</a> calls to Durable Objects would lack the <code>.remote</code> property that exceptions from <code>fetch()</code> calls to Durable Objects have.</li>
</ul><h2 id="2024-06-12">2024-06-12</h2><ul>
<li>Blob and Body objects now include a new <code>bytes()</code> method, reflecting <a href="https://w3c.github.io/FileAPI/#bytes-method-algo">recent</a> <a href="https://fetch.spec.whatwg.org/#dom-body-bytes">additions</a> to web standards.</li>
</ul><h2 id="2024-06-03">2024-06-03</h2><ul>
<li>Workers with <a href="/workers/configuration/placement/">Smart Placement</a> enabled now support <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual Deployments</a>.</li>
</ul><h2 id="2024-05-17">2024-05-17</h2><ul>
<li>Updated v8 to version 12.6.</li>
</ul><h2 id="2024-05-15">2024-05-15</h2><ul>
<li>The new <a href="/workers/configuration/compatibility-flags/#use-standard-url-parsing-in-fetch"><code>fetch_standard_url</code> compatibility flag</a> will become active by default on June 3rd, 2024 and ensures that URLs passed into the <code>fetch(...)</code> API, the <code>new Request(...)</code> constructor, and redirected requests will be parsed using the standard WHATWG URL parser.</li>
<li>DigestStream is now more efficient and exposes a new <code>bytesWritten</code> property that indicates that number of bytes written to the digest.</li>
</ul><h2 id="2024-05-13">2024-05-13</h2><ul>
<li>Updated v8 to version 12.5.</li>
<li>A bug in the fetch API implementation would cause the content type of a Blob to be incorrectly set. The fix is being released behind a new <a href="/workers/configuration/compatibility-flags/#properly-extract-blob-mime-type-from-content-type-headers"><code>blob_standard_mime_type</code> compatibility flag</a>.</li>
</ul><h2 id="2024-05-03">2024-05-03</h2><ul>
<li>Fixed RPC to/from Durable Objects not honoring the output gate.</li>
<li>The <code>internal_stream_byob_return_view</code> compatibility flag can be used to improve the standards compliance of the <code>ReadableStreamBYOBReader</code> implementation when working with BYOB streams provided by the runtime (like in <code>response.body</code> or <code>request.body</code>). The flag ensures that the final read result will always include a <code>value</code> field whose value is set to an empty <code>Uint8Array</code> whose underlying <code>ArrayBuffer</code> is the same memory allocation as the one passed in on the call to <code>read()</code>.</li>
<li>The Web platform standard <code>reportError(err)</code> global API is now available in workers. The reported error will first be emitted as an 'error' event on the global scope then reported in both the console output and tail worker exceptions by default.</li>
</ul><h2 id="2024-04-26">2024-04-26</h2><ul>
<li>Updated v8 to version 12.4.</li>
</ul><h2 id="2024-04-11">2024-04-11</h2><ul>
<li>Improve Streams API spec compliance by exposing <code>desiredSize</code> and other properties on stream class prototypes</li>
<li>The new <code>URL.parse(...)</code> method is implemented. This provides an alternative to the URL constructor that does not throw exceptions on invalid URLs.</li>
<li>R2 bindings objects now have a <code>storageClass</code> option. This can be set on object upload to specify the R2 storage class - Standard or Infrequent Access. The property is also returned with object metadata.</li>
</ul><h2 id="2024-04-05">2024-04-05</h2><ul>
<li>A new <a href="/workers/runtime-apis/rpc">JavaScript-native remote procedure call (RPC) API</a> is now available, allowing you to communicate more easily across Workers and between Workers and Durable Objects.</li>
</ul><h2 id="2024-04-04">2024-04-04</h2><ul>
<li>There is no longer an explicit limit on the total amount of data which may be uploaded with Cache API <a href="/workers/runtime-apis/cache/#put"><code>put()</code></a> per request. Other <a href="/workers/platform/limits/#cache-api-limits">Cache API Limits</a> continue to apply.</li>
<li>The Web standard <code>ReadableStream.from()</code> API is now implemented. The API enables creating a <code>ReadableStream</code> from a either a sync or async iterable.</li>
</ul><h2 id="2024-04-03">2024-04-03</h2><ul>
<li>When the <a href="/workers/configuration/compatibility-flags/#brotli-content-encoding-support"><code>brotli_content_encoding</code></a> compatibility flag is enabled, the Workers runtime now supports compressing and decompressing request bodies encoded using the <a href="https://developer.mozilla.org/en-US/docs/Glossary/Brotli_compression">Brotli</a> compression algorithm. Refer to <a href="/workers/runtime-apis/fetch/#how-the-accept-encoding-header-is-handled">this docs section</a> for more detail.</li>
</ul><h2 id="2024-04-02">2024-04-02</h2><ul>
<li>You can now <a href="/workers/languages/python">write Workers in Python</a></li>
</ul><h2 id="2024-04-01">2024-04-01</h2><ul>
<li>The new <a href="/workers/configuration/compatibility-flags/#handling-custom-thenables"><code>unwrap_custom_thenables</code> compatibility flag</a> enables workers to accept custom thenables in internal APIs that expect a promise (for instance, the <code>ctx.waitUntil(...)</code> method).</li>
<li>TransformStreams created with the TransformStream constructor now have a cancel algorithm that is called when the stream is canceled or aborted. This change is part of the implementation of the WHATWG Streams standard.</li>
<li>The <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code> compatibility flag</a> now includes an implementation of the <a href="https://nodejs.org/api/test.html#class-mocktracker"><code>MockTracker</code> API from <code>node:test</code></a>. This is not an implementation of the full <code>node:test</code> module, and mock timers are currently not included.</li>
<li>Exceptions reported to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> now include a &quot;stack&quot; property containing the exception's stack trace, if available.</li>
</ul><h2 id="2024-03-11">2024-03-11</h2><ul>
<li>Built-in APIs that return Promises will now produce stack traces when the Promise rejects. Previously, the rejection error lacked a stack trace.</li>
<li>A new compat flag <code>fetcher_no_get_put_delete</code> removes the <code>get()</code>, <code>put()</code>, and <code>delete()</code> methods on service bindings and Durable Object stubs. This will become the default as of compatibility date 2024-03-26. These methods were designed as simple convenience wrappers around <code>fetch()</code>, but were never documented.</li>
<li>Updated v8 to version 12.3.</li>
</ul><h2 id="2024-02-24">2024-02-24</h2><ul>
<li>v8 updated to version 12.2.</li>
<li>You can now use <a href="https://v8.dev/features/iterator-helpers">Iterator helpers</a> in Workers.</li>
<li>You can now use <a href="https://github.com/tc39/proposal-set-methods">new methods on <code>Set</code></a>, such as <code>Set.intersection</code> and <code>Set.union</code>, in Workers.</li>
</ul><h2 id="2024-02-23">2024-02-23</h2><ul>
<li>Sockets now support an <a href="/workers/runtime-apis/tcp-sockets/#socket"><code>opened</code></a> attribute.</li>
<li><a href="/durable-objects/api/alarms/#alarm">Durable Object alarm handlers</a> now impose a maximum wall time of 15 minutes.</li>
</ul><h2 id="2023-12-04">2023-12-04</h2><ul>
<li>The Web Platform standard <a href="/workers/runtime-apis/web-standards#navigatorsendbeaconurl-data"><code>navigator.sendBeacon(...)</code> API</a> is now provided by the Workers runtime.</li>
<li>V8 updated to 12.0.</li>
</ul><h2 id="2023-10-30">2023-10-30</h2><ul>
<li>A new usage model called <a href="/workers/platform/pricing/#workers">Workers Standard</a> is available for Workers and Pages Functions pricing. This is now the default usage model for accounts that are first upgraded to the Workers Paid plan. Read the <a href="https://blog.cloudflare.com/workers-pricing-scale-to-zero/">blog post</a> for more information.</li>
<li>The usage model set in a script's wrangler.toml will be ignored after an account has opted-in to <a href="/workers/platform/pricing/#workers">Workers Standard</a> pricing. It must be configured through the dashboard (Workers &amp; Pages &gt; Select your Worker &gt; Settings &gt; Usage Model).</li>
<li>Workers and Pages Functions on the Standard usage model can set custom <a href="/workers/wrangler/configuration/#limits">CPU limits</a> for their Workers</li>
</ul><h2 id="2023-10-20">2023-10-20</h2><ul>
<li>Added the <a href="/workers/configuration/compatibility-flags/#webcrypto-preserve-publicexponent-field"><code>crypto_preserve_public_exponent</code></a>
compatibility flag to correct a wrong type being used in the algorithm field of RSA keys in
the WebCrypto API.</li>
</ul><h2 id="2023-10-18">2023-10-18</h2><ul>
<li>The limit of 3 Cron Triggers per Worker has been removed. Account-level limits on the total number of
Cron Triggers across all Workers still apply.</li>
</ul><h2 id="2023-10-12">2023-10-12</h2><ul>
<li>A <a href="/workers/runtime-apis/tcp-sockets/">TCP Socket</a>'s WritableStream now ensures the connection has opened before resolving the promise returned by <code>close</code>.</li>
</ul><h2 id="2023-10-09">2023-10-09</h2><ul>
<li>The Web Platform standard <a href="https://dom.spec.whatwg.org/#interface-customevent"><code>CustomEvent</code> class</a> is now available in Workers.</li>
<li>Fixed a bug in the WebCrypto API where the <code>publicExponent</code> field of the algorithm of RSA keys would have the wrong type. Use the <a href="/workers/configuration/compatibility-flags/#webcrypto-preserve-publicexponent-field"><code>crypto_preserve_public_exponent</code> compatibility flag</a> to enable the new behavior.</li>
</ul><h2 id="2023-09-14">2023-09-14</h2><ul>
<li>An implementation of the <a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a>
API from Node.js is now available when the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code> compatibility flag</a>
is enabled.</li>
</ul><h2 id="2023-07-14">2023-07-14</h2><ul>
<li>An implementation of the <a href="https://nodejs.org/api/util.html#class-utilmimetype"><code>util.MIMEType</code></a>
API from Node.js is now available when the <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/"><code>nodejs_compat</code> compatibility flag</a>
is enabled.</li>
</ul><h2 id="2023-07-07">2023-07-07</h2><ul>
<li>An implementation of the <a href="/workers/runtime-apis/nodejs/process"><code>process.env</code></a> API from Node.js is now available when using the <code>nodejs_compat</code> compatibility flag.</li>
<li>An implementation of the <a href="/workers/runtime-apis/nodejs/diagnostics-channel"><code>diagnostics_channel</code></a> API from Node.js is now available when using the <code>nodejs_compat</code> compatibility flag.</li>
</ul><h2 id="2023-06-22">2023-06-22</h2><ul>
<li>Added the <a href="/workers/configuration/compatibility-flags/#strict-crypto-error-checking"><code>strict_crypto_checks</code></a> compatibility flag to enable additional <a href="/workers/runtime-apis/web-crypto/">Web Crypto API</a> error and security checking.</li>
<li>Fixes regression in the <a href="/workers/runtime-apis/tcp-sockets/">TCP Sockets API</a> where <code>connect(&quot;google.com:443&quot;)</code> would fail with a <code>TypeError</code>.</li>
</ul><h2 id="2023-06-19">2023-06-19</h2><ul>
<li>The <a href="/workers/runtime-apis/tcp-sockets/">TCP Sockets API</a> now reports clearer errors when a connection cannot be established.</li>
<li>Updated V8 to 11.5.</li>
</ul><h2 id="2023-06-09">2023-06-09</h2><ul>
<li><code>AbortSignal.any()</code> is now available.</li>
<li>Updated V8 to 11.4.</li>
<li>Following an update to the <a href="https://url.spec.whatwg.org/#interface-urlsearchparams">WHATWG URL spec</a>, the <code>delete()</code> and <code>has()</code> methods of the <code>URLSearchParams</code> class now accept an optional second argument to specify the search parameter’s value. This is potentially a breaking change, so it is gated behind the new <code>urlsearchparams_delete_has_value_arg</code> and <a href="/workers/configuration/compatibility-flags/#new-url-parser-implementation"><code>url_standard</code></a> compatibility flags.</li>
<li>Added the <a href="/workers/configuration/compatibility-flags/#strict-compression-error-checking"><code>strict_compression_checks</code></a> compatibility flag for additional <a href="/workers/runtime-apis/web-standards/#compression-streams"><code>DecompressionStream</code></a> error checking.</li>
</ul><h2 id="2023-05-26">2023-05-26</h2><ul>
<li>A new <a href="/durable-objects/best-practices/websockets/">Hibernatable WebSockets API</a>
(beta) has been added to <a href="/durable-objects/">Durable Objects</a>. The Hibernatable
WebSockets API allows a Durable Object that is not currently running an event
handler (for example, processing a WebSocket message or alarm) to be removed from
memory while keeping its WebSockets connected (“hibernation”). A Durable Object
that hibernates will not incur billable Duration (GB-sec) charges.</li>
</ul><h2 id="2023-05-16">2023-05-16</h2><ul>
<li>The <a href="/workers/runtime-apis/tcp-sockets/">new <code>connect()</code> method</a> allows you to connect to any TCP-speaking services directly from your Workers. To learn more about other protocols supported on the Workers platform, visit the <a href="/workers/reference/protocols/">new Protocols documentation</a>.</li>
<li>We have added new <a href="/workers/databases/native-integrations/">native database integrations</a> for popular serverless database providers, including Neon, PlanetScale, and Supabase. Native integrations automatically handle the process of creating a connection string and adding it as a Secret to your Worker.</li>
<li>You can now also connect directly to databases over TCP from a Worker, starting with <a href="/hyperdrive/examples/connect-to-postgres/">PostgreSQL</a>. Support for PostgreSQL is based on the popular <code>pg</code> driver, and allows you to connect to any PostgreSQL instance over TLS from a Worker directly.</li>
<li>The <a href="/r2/data-migration/">R2 Migrator</a> (Super Slurper), which automates the process of migrating from existing object storage providers to R2, is now Generally Available.</li>
</ul><h2 id="2023-05-15">2023-05-15</h2><ul>
<li><a href="/workers/ai/">Cursor</a>, an experimental AI assistant, trained to answer
questions about Cloudflare's Developer Platform, is now available to preview!
Cursor can answer questions about Workers and the Cloudflare Developer Platform,
and is itself built on Workers. You can read more about Cursor in the <a href="https://blog.cloudflare.com/introducing-cursor-the-ai-assistant-for-docs/">announcement
blog</a>.</li>
</ul><h2 id="2023-05-12">2023-05-12</h2><ul>
<li>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/now"><code>performance.now()</code></a>
and <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance/timeOrigin"><code>performance.timeOrigin</code></a>
APIs can now be used in Cloudflare Workers. Just like <code>Date.now()</code>, for <a href="/workers/reference/security-model/">security
reasons</a> time only advances after I/O.</li>
</ul><h2 id="2023-05-05">2023-05-05</h2><ul>
<li>The new <code>nodeJsCompatModule</code> type can be used with a Worker bundle to emulate a Node.js environment. Common Node.js globals such as <code>process</code> and <code>Buffer</code> will be present, and <code>require('...')</code> can be used to load Node.js built-ins without the <code>node:</code> specifier prefix.</li>
<li>Fixed an issue where websocket connections would be disconnected when updating workers. Now, only WebSockets connected to Durable Objects are disconnected by updates to that Durable Object’s code.</li>
</ul><h2 id="2023-04-28">2023-04-28</h2><ul>
<li>The Web Crypto API now supports curves Ed25519 and X25519 defined in the Secure Curves specification.</li>
<li>The global <code>connect</code> method has been moved to a <code>cloudflare:sockets</code> module.</li>
</ul><h2 id="2023-04-14">2023-04-14</h2><ul>
<li>No externally-visible changes this week.</li>
</ul><h2 id="2023-04-10">2023-04-10</h2><ul>
<li><code>URL.canParse(...)</code> is a new standard API for testing that an input string can be parsed successfully as a URL without the additional cost of creating and throwing an error.</li>
<li>The Workers-specific <code>IdentityTransformStream</code> and <code>FixedLengthStream</code> classes now support specifying a <code>highWaterMark</code> for the writable-side that is used for backpressure signaling using the standard <code>writer.desiredSize</code>/<code>writer.ready</code> mechanisms.</li>
</ul><h2 id="2023-03-24">2023-03-24</h2><ul>
<li>Fixed a bug in Wrangler tail and live logs on the dashboard that
prevented the Administrator Read-Only and Workers Tail Read roles from successfully
tailing Workers.</li>
</ul><h2 id="2023-03-09">2023-03-09</h2><ul>
<li>No externally-visible changes.</li>
</ul><h2 id="2023-03-06">2023-03-06</h2><ul>
<li><a href="/workers/observability/logs/logpush/#limits">Workers Logpush</a> now supports
300 characters per log line. This is an increase from the previous limit of 150
characters per line.</li>
</ul><h2 id="2023-02-06">2023-02-06</h2><ul>
<li>Fixed a bug where transferring large request bodies to a Durable Object was unexpectedly slow.</li>
<li>Previously, an error would be thrown when trying to access unimplemented standard <code>Request</code> and <code>Response</code> properties. Now those will be left as <code>undefined</code>.</li>
</ul><h2 id="2023-01-31">2023-01-31</h2><ul>
<li>The <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf</code></a> object now includes two additional properties, <code>tlsClientHelloLength</code> and <code>tlsClientRandom</code>.</li>
</ul><h2 id="2023-01-13">2023-01-13</h2><ul>
<li>Durable Objects can now use jurisdictions with <code>idFromName</code> via a new subnamespace API.</li>
<li>V8 updated to 10.9.</li>
</ul>
