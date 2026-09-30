---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/changelog/historical-changelog/
  description: Review pre-2023 changes to Cloudflare Workers.
  full_title: Historical changelog · Cloudflare Workers docs
  head_html: <title>Historical changelog · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Review pre-2023 changes to Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/changelog/historical-changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/changelog/historical-changelog/index.md"><meta property="og:title" content="Historical changelog · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review pre-2023 changes to Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/changelog/historical-changelog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/platform/changelog/historical-changelog/#page","headline":"Historical changelog \u00b7 Cloudflare Workers docs","description":"Review pre-2023 changes to Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/platform/changelog/historical-changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/changelog/historical-changelog/
  schema: 1
---
<p>This page tracks changes made to Cloudflare Workers before 2023. For a view of more recent updates, refer to the <a href="/workers/platform/changelog/">current changelog</a>.</p>
<h2 id="2022-12-16">2022-12-16</h2>
<ul>
<li>Conditional <code>PUT</code> requests have been fixed in the R2 bindings API.</li>
</ul>
<h2 id="2022-12-02">2022-12-02</h2>
<ul>
<li>Queues no longer support calling <code>send()</code> with an undefined JavaScript value as the message.</li>
</ul>
<h2 id="2022-11-30">2022-11-30</h2>
<ul>
<li>The DOMException constructor has been updated to align better with the standard specification. Specifically, the message and name arguments can now be any JavaScript value that is coercible into a string (previously, passing non-string values would throw).</li>
<li>Extended the R2 binding API to include support for multipart uploads.</li>
</ul>
<h2 id="2022-11-17">2022-11-17</h2>
<ul>
<li>V8 update: 10.6 → 10.8</li>
</ul>
<h2 id="2022-11-02">2022-11-02</h2>
<ul>
<li>Implemented <code>toJSON()</code> for R2Checksums so that it is usable with <code>JSON.stringify()</code>.</li>
</ul>
<h2 id="2022-10-21">2022-10-21</h2>
<ul>
<li>The alarm retry limit will no longer apply to errors that are our fault.</li>
<li>Compatibility dates have been added for multiple flags including the new streams implementation.</li>
<li><code>DurableObjectStorage</code> has a new method <code>sync()</code> that provides a way for a Worker to wait for its writes (including those performed with <code>allowUnconfirmed</code>) to be synchronized with storage.</li>
</ul>
<h2 id="2022-10-10">2022-10-10</h2>
<ul>
<li>Fixed a bug where if an ES-modules-syntax script exported an array-typed value from the top-level module, the upload API would refuse it with a <a href="https://community.cloudflare.com/t/community-tip-fixing-error-500-internal-server-error/44453"><code>500</code> error</a>.</li>
<li><code>console.log</code> now prints more information about certain objects, for example Promises.</li>
<li>The Workers Runtime is now built from the Open Source code in: <a href="https://github.com/cloudflare/workerd">GitHub - cloudflare/workerd: The JavaScript / Wasm runtime that powers Cloudflare Workers</a>.</li>
</ul>
<h2 id="2022-09-16">2022-09-16</h2>
<ul>
<li>R2 <code>put</code> bindings options can now have an <code>onlyIf</code> field similar to <code>get</code> that does a conditional upload.</li>
<li>Allow deleting multiple keys at once in R2 bindings.</li>
<li>Added support for SHA-1, SHA-256, SHA-384, SHA-512 checksums in R2 <code>put</code> options.</li>
<li>User-specified object checksums will now be available in the R2 <code>get/head</code> bindings response. MD5 is included by default for non-multipart uploaded objects.</li>
<li>Updated V8 to 10.6.</li>
</ul>
<h2 id="2022-08-12">2022-08-12</h2>
<ul>
<li>A <code>Headers</code> object with the <code>range</code> header can now be used for range within <code>R2GetOptions</code> for the <code>get</code> R2 binding.</li>
<li>When headers are used for <code>onlyIf</code> within <code>R2GetOptions</code> for the <code>get</code> R2 binding, they now correctly compare against the second granularity. This allows correctly round-tripping to the browser and back. Additionally, <code>secondsGranularity</code> is now an option that can be passed into options constructed by hand to specify this when constructing outside Headers for the same effect.</li>
<li>Fixed the TypeScript type of <code>DurableObjectState.id</code> in <a href="https://github.com/cloudflare/workers-types">@cloudflare/workers-types</a> to always be a <code>DurableObjectId</code>.</li>
<li>Validation errors during Worker upload for module scripts now include correct line and column numbers.</li>
<li>Bugfix, Profiling tools and flame graphs via Chrome’s debug tools now properly report information.</li>
</ul>
<h2 id="2022-07-08">2022-07-08</h2>
<ul>
<li>Workers Usage Report and Workers Weekly Summary have been disabled due to scaling issues with the service.</li>
</ul>
<h2 id="2022-06-24">2022-06-24</h2>
<ul>
<li><code>wrangler dev</code> in global network preview mode now supports scheduling alarms.</li>
<li>R2 GET requests made with the <code>range</code> option now contain the returned range in the <code>GetObject</code>’s <code>range</code> parameter.</li>
<li>Some Web Cryptography API error messages include more information now.</li>
<li>Updated V8 from 10.2 to 10.3.</li>
</ul>
<h2 id="2022-06-18">2022-06-18</h2>
<ul>
<li>Cron trigger events on Worker scripts using the old <code>addEventListener</code> syntax are now treated as failing if there is no event listener registered for <code>scheduled</code> events.</li>
<li>The <code>durable_object_alarms</code> flag no longer needs to be explicitly provided to use DO alarms.</li>
</ul>
<h2 id="2022-06-09">2022-06-09</h2>
<ul>
<li>No externally-visible changes.</li>
</ul>
<h2 id="2022-06-03">2022-06-03</h2>
<ul>
<li>It is now possible to create standard <code>TransformStream</code> instances that can perform transformations on the data. Because this changes the behavior of the default <code>new TransformStream()</code> with no arguments, the <code>transformstream_enable_standard_constructor</code> compatibility flag is required to enable.</li>
<li>Preview in Quick Edit now correctly uses the correct R2 bindings.</li>
<li>Updated V8 from 10.1 to 10.2.</li>
</ul>
<h2 id="2022-05-26">2022-05-26</h2>
<ul>
<li>The static <code>Response.json()</code> method can be used to initialize a Response object with a JSON-serialized payload (refer to <a href="https://github.com/whatwg/fetch/pull/1392">whatwg/fetch #1392</a>).</li>
<li>R2 exceptions being thrown now have the <code>error</code> code appended in the message in parenthesis. This is a stop-gap until we are able to explicitly add the code property on the thrown <code>Error</code> object.</li>
</ul>
<h2 id="2022-05-19">2022-05-19</h2>
<ul>
<li>R2 bindings: <code>contentEncoding</code>, <code>contentLanguage</code>, and <code>cacheControl</code> are now correctly rendered.</li>
<li>ReadableStream <code>pipeTo</code> and <code>pipeThrough</code> now support cancellation using <code>AbortSignal</code>.</li>
<li>Calling <code>setAlarm()</code> in a DO with no <code>alarm()</code> handler implemented will now throw instead of failing silently. Calling <code>getAlarm()</code> when no <code>alarm()</code> handler is currently implemented will return null, even if an alarm was previously set on an old version of the DO class, as no execution will take place.</li>
<li>R2: Better runtime support for additional ranges.</li>
<li>R2 bindings now support ranges that have an <code>offset</code> and an optional <code>length</code>, a <code>length</code> and an optional <code>offset</code>, or a <code>suffix</code> (returns the last <code>N</code> bytes of a file).</li>
</ul>
<h2 id="2022-05-12">2022-05-12</h2>
<ul>
<li>Fix R2 bindings saving cache-control under content-language and rendering cache-control under content-language.</li>
<li>Fix R2 bindings list without options to use the default list limit instead of never returning any results.</li>
<li>Fix R2 bindings which did not correctly handle error messages from R2, resulting in <code>internal error</code> being thrown. Also fix behavior for get throwing an exception on a non-existent key instead of returning null. <code>R2Error</code> is removed for the time being and will be reinstated at some future time TBD.</li>
<li>R2 bindings: if the onlyIf condition results in a precondition failure or a not modified result, the object is returned without a body instead of returning null.</li>
<li>R2 bindings: sha1 is removed as an option because it was not actually hooked up to anything. TBD on additional checksum options beyond md5.</li>
<li>Added <code>startAfter</code> option to the <code>list()</code> method in the Durable Object storage API.</li>
</ul>
<h2 id="2022-05-05">2022-05-05</h2>
<ul>
<li><code>Response.redirect(url)</code> will no longer coalesce multiple consecutive slash characters appearing in the URL’s path.</li>
<li>Fix generated types for Date.</li>
<li>Fix R2 bindings list without options to use the default list limit instead of never returning any results.</li>
<li>Fix R2 bindings did not correctly handle error messages from R2, resulting in internal error being thrown. Also fix behavior for get throwing an exception on a non-existent key instead of returning null. <code>R2Error</code> is removed for the time being and will be reinstated at some future time TBD.</li>
</ul>
<h2 id="2022-04-29">2022-04-29</h2>
<ul>
<li>Minor V8 update: 10.0 → 10.1.</li>
<li>R2 public beta bindings are the default regardless of compat date or flags. Internal beta bindings customers should transition to public beta bindings as soon as possible. A back compatibility flag is available if this is not immediately possible. After some lag, new scripts carrying the <code>r2_public_beta_bindings</code> compatibility flag will stop accepting to be published until that flag is removed.</li>
</ul>
<h2 id="2022-04-22">2022-04-22</h2>
<ul>
<li>Major V8 update: 9.9 → 10.0.</li>
</ul>
<h2 id="2022-04-14">2022-04-14</h2>
<ul>
<li>Performance and stability improvements.</li>
</ul>
<h2 id="2022-04-08">2022-04-08</h2>
<ul>
<li>The AES-GCM implementation that is part of the Web Cryptography API now returns a friendlier error explaining that 0-length IVs are not allowed.</li>
<li>R2 error responses now include better details.</li>
</ul>
<h2 id="2022-03-24">2022-03-24</h2>
<ul>
<li>A new compatibility flag has been introduced, <code>minimal_subrequests</code> , which removes some features that were unintentionally being applied to same-zone <code>fetch()</code> calls. The flag will default to enabled on Tuesday, 2022-04-05, and is described in <a href="/workers/configuration/compatibility-flags/#minimal-subrequests">Workers <code>minimal_subrequests</code> compatibility flag</a>.</li>
<li>When creating a <code>Response</code> with JavaScript-backed ReadableStreams, the <code>Body</code> mixin functions (e.g. <code>await response.text()</code> ) are now implemented.</li>
<li>The <code>IdentityTransformStream</code> creates a byte-oriented <code>TransformStream</code> implementation that simply passes bytes through unmodified. The readable half of the <code>TransformStream</code> supports BYOB-reads. It is important to note that <code>IdentityTransformStream</code> is identical to the current non-spec compliant <code>TransformStream</code> implementation, which will be updated soon to conform to the WHATWG Stream Standard. All current uses of <code>new TransformStream()</code> should be replaced with <code>new IdentityTransformStream()</code> to avoid potentially breaking changes later.</li>
</ul>
<h2 id="2022-03-17">2022-03-17</h2>
<ul>
<li>The standard <a href="https://developer.mozilla.org/en-US/docs/Web/API/ByteLengthQueuingStrategy">ByteLengthQueuingStrategy</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/API/CountQueuingStrategy">CountQueuingStrategy</a> classes are now available.</li>
<li>When the <code>capture_async_api_throws</code> flag is set, built-in Cloudflare-specific and Web Platform Standard APIs that return Promises will no longer throw errors synchronously and will instead return rejected promises. Exception is given with fatal errors such as out of memory errors.</li>
<li>Fix R2 publish date rendering.</li>
<li>Fix R2 bucket binding .get populating contentRange with garbage. contentRange is now undefined as intended.</li>
<li>When using JavaScript-backed <code>ReadableStream</code>, it is now possible to use those streams with <code>new Response()</code>.</li>
</ul>
<h2 id="2022-03-11">2022-03-11</h2>
<ul>
<li>Fixed a bug where the key size was not counted when determining how many write units to charge for a Durable Object single-key <code>put()</code>. This may result in future writes costing one write unit more than past writes when the key is large enough to bump the total write size up above the next billing unit threshold of 4096 bytes. Multi-key <code>put()</code> operations have always properly counted the key size when determining billable write units.</li>
<li>Implementations of <code>CompressionStream</code> and <code>DecompressionStream</code> are now available.</li>
</ul>
<h2 id="2022-03-04">2022-03-04</h2>
<ul>
<li>Initial pipeTo/pipeThrough support on ReadableStreams constructed using the new <code>ReadableStream()</code> constructor is now available.</li>
<li>With the <code>global_navigator</code> compatibility flag set, the <code>navigator.userAgent</code> property can be used to detect when code is running within the Workers environment.</li>
<li>A bug in the new URL implementation was fixed when setting the value of a <code>URLSearchParam</code>.</li>
<li>The global <code>addEventListener</code> and dispatchEvent APIs are now available when using module syntax.</li>
<li>An implementation of <code>URLPattern</code> is now available.</li>
</ul>
<h2 id="2022-02-25">2022-02-25</h2>
<ul>
<li>The <code>TextDecoder</code> class now supports the full range of text encodings defined by the WHATWG Encoding Standard.</li>
<li>Both global <code>fetch()</code> and durable object <code>fetch()</code> now throw a TypeError when they receive a WebSocket in response to a request without the “Upgrade: websocket” header.</li>
<li>Durable Objects users may now store up to 50 GB of data across the objects in their account by default. As before, if you need more storage than that you can contact us for an increase.</li>
</ul>
<h2 id="2022-02-18">2022-02-18</h2>
<ul>
<li><code>TextDecoder</code> now supports Windows-1252 labels (aka ASCII): <a href="https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings">Encoding API Encodings - Web APIs | MDN</a>.</li>
</ul>
<h2 id="2022-02-11">2022-02-11</h2>
<ul>
<li>WebSocket message sends were erroneously not respecting Durable Object output gates as described in the <a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">I/O gate blog post</a>. That bug has now been fixed, meaning that WebSockets will now never send a message under the assumption that a storage write has succeeded unless that write actually has succeeded.</li>
</ul>
<h2 id="2022-02-05">2022-02-05</h2>
<ul>
<li>Fixed bug causing WebSockets to Durable Objects to occasionally hang when the script implementing both a Worker and a Durable Object is re-deployed with new code.</li>
<li><code>crypto.getRandomValues</code> now supports BigInt64Array and BigUint64Array.</li>
<li>A new implementation of the standard URL implementation is available. Use <code>url_standard</code> feature flag to enable the spec-compliant URL API implementation.</li>
</ul>
<h2 id="2022-01-28">2022-01-28</h2>
<ul>
<li>No user-visible changes.</li>
</ul>
<h2 id="2022-01-20">2022-01-20</h2>
<ul>
<li>Updated V8: 9.7 → 9.8.</li>
</ul>
<h2 id="2022-01-17">2022-01-17</h2>
<ul>
<li><code>HTMLRewriter</code> now supports inspecting and modifying end tags, not just start tags.</li>
<li>Fixed bug where Durable Objects experiencing a transient CPU overload condition would cause in-progress requests to be unable to return a response (appearing as an indefinite hang from the client side), even after the overload condition clears.</li>
</ul>
<h2 id="2022-01-07">2022-01-07</h2>
<ul>
<li>The <code>workers_api_getters_setters_on_prototype</code> configuration flag corrects the way Workers attaches property getters and setters to API objects so that they can be properly subclassed.</li>
</ul>
<h2 id="2021-12-22">2021-12-22</h2>
<ul>
<li>Async iteration (using <code>for</code> and <code>await</code>) on instances of <code>ReadableStream</code> is now available.</li>
</ul>
<h2 id="2021-12-10">2021-12-10</h2>
<ul>
<li>Raised the max value size in Durable Object storage from 32 KiB to 128 KiB.</li>
<li><code>AbortSignal.timeout(delay)</code> returns an <code>AbortSignal</code> that will be triggered after the given number of milliseconds.</li>
<li>Preview implementations of the new <code>ReadableStream</code> and new <code>WritableStream</code> constructors are available behind the <code>streams_enable_constructors</code> feature flag.</li>
<li><code>crypto.DigestStream</code> is a non-standard extension to the crypto API that supports generating a hash digest from streaming data. The <code>DigestStream</code> itself is a <code>WritableStream</code> that does not retain the data written into it; instead, it generates a digest hash automatically when the flow of data has ended. The same hash algorithms supported by <code>crypto.subtle.digest()</code> are supported by the <code>crypto.DigestStream</code>.</li>
<li>Added early support for the <code>scheduler.wait()</code> API, which is <a href="https://github.com/WICG/scheduling-apis">going through the WICG standardization process</a>, to provide an <code>await</code>-able alternative to <code>setTimeout()</code>.</li>
<li>Fixed bug in <code>deleteAll</code> in Durable Objects containing more than 10000 keys that could sometimes cause incomplete data deletion and/or hangs.</li>
</ul>
<h2 id="2021-12-02">2021-12-02</h2>
<ul>
<li>The Streams spec requires that methods returning promises must not throw synchronous errors. As part of the effort of making the Streams implementation more spec compliant, we are converting a number of sync throws to async rejections.</li>
<li>Major V8 update: 9.6 → 9.7. See <a href="https://v8.dev/blog/v8-release-97">V8 release v9.7 · V8</a> for more details.</li>
</ul>
<h2 id="2021-11-19">2021-11-19</h2>
<ul>
<li>Durable Object stubs that receive an overload exception will be permanently broken to match the behavior of other exception types.</li>
<li>Fixed issue where preview service claimed Let’s Encrypt certificates were expired.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/structuredClone"><code>structuredClone()</code></a> is now supported.</li>
</ul>
<h2 id="2021-11-12">2021-11-12</h2>
<ul>
<li>The <code>AbortSignal</code> object has a new <code>reason</code> property indicating the reason for the cancellation. The reason can be specified when the <code>AbortSignal</code> is triggered or created.</li>
<li>Unhandled rejection warnings will be printed to the inspector console.</li>
</ul>
<h2 id="2021-11-05">2021-11-05</h2>
<ul>
<li>Upgrade to V8 9.6. This adds support for WebAssembly reference types. Refer to the <a href="https://v8.dev/blog/v8-release-96">V8 release v9.6 · V8</a> for more details.</li>
<li>Streams: When using the BYOB reader, the <code>ArrayBuffer</code> of the provided TypedArray should be detached, per the Streams spec. Because Workers was not previously enforcing that rule, and changing to comply with the spec could breaking existing code, a new compatibility flag, <a href="https://github.com/cloudflare/cloudflare-docs/pull/2644">streams_byob_reader_detaches_buffer</a>, has been introduced that will be enabled by default on 2021-11-10. User code should never try to reuse an <code>ArrayBuffer</code> that has been passed in to a BYOB readers <code>read()</code> method. The more recently added extension method <code>readAtLeast()</code> will always detach the <code>ArrayBuffer</code> and is unaffected by the compatibility flag setting.</li>
</ul>
<h2 id="2021-10-21">2021-10-21</h2>
<ul>
<li>Added support for the <code>signal</code> option in <code>EventTarget.addEventListener()</code>, to remove an event listener in response to an <code>AbortSignal</code>.</li>
<li>The <code>unhandledrejection</code> and <code>rejectionhandled</code> events are now supported.</li>
<li>The <code>ReadableStreamDefaultReader</code> and <code>ReadableStreamBYOBReader</code> constructors are now supported.</li>
<li>Added non-standard <code>ReadableStreamBYOBReader</code> method <code>.readAtLeast(size, buffer)</code> that can be used to return a buffer with at least <code>size</code> bytes. The <code>buffer</code> parameter must be an <code>ArrayBufferView</code>. Behavior is identical to <code>.read()</code> except that at least <code>size</code> bytes are read, only returning fewer if EOF is encountered. One final call to <code>.readAtLeast()</code> is still needed to get back a <code>done = true</code> value.</li>
<li>The compatibility flags <code>formdata_parser_supports_files</code>, <code>fetch_refuses_unknown_protocols</code>, and <code>durable_object_fetch_requires_full_url</code> have been scheduled to be turned on by default as of 2021-11-03, 2021-11-10, and 2021-11-10, respectively. For more details, refer to <a href="/workers/configuration/compatibility-dates/">Compatibility Dates</a></li>
</ul>
<h2 id="2021-10-14">2021-10-14</h2>
<ul>
<li><code>request.signal</code> will always return an <code>AbortSignal</code>.</li>
<li>Cloudflare Workers’ integration with Chrome DevTools profiling now more accurately reports the line numbers and time elapsed. Previously, the line numbers were shown as one line later then the actual code, and the time shown would be proportional but much longer than the actual time used.</li>
<li>Upgrade to v8 9.5. Refer to <a href="https://v8.dev/blog/v8-release-95">V8 release v9.5 · V8</a> for more details.</li>
</ul>
<h2 id="2021-09-24">2021-09-24</h2>
<ul>
<li>The <code>AbortController</code> and <code>AbortSignal</code> objects are now available.</li>
<li>The Web Platform <code>queueMicrotask</code> API is now available.</li>
<li>It is now possible to use new <code>EventTarget()</code> and to create custom <code>EventTarget</code> subclasses.</li>
<li>The <code>once</code> option is now supported on <code>addEventTarget</code> to register event handlers that will be invoked only once.</li>
<li>Per the HTML specification, a listener passed in to the <code>addEventListener</code> function is allowed to either be a function or an object with a <code>handleEvent</code> member function. Previously, Workers only supported the function option, now it supports both.</li>
<li>The <code>Event</code> object now supports most standard methods and properties.</li>
<li>V8 updated from 9.3 to 9.4.</li>
</ul>
<h2 id="2021-09-03">2021-09-03</h2>
<ul>
<li>The <code>crypto.randomUUID()</code> method can be used to generate a new random version 4 UUID.</li>
<li>Durable Objects are now scheduled more evenly around a colocation (colo).</li>
</ul>
<h2 id="2021-08-05">2021-08-05</h2>
<ul>
<li>No user-facing changes. Just bug fixes &amp; internal maintenance.</li>
</ul>
<h2 id="2021-07-30">2021-07-30</h2>
<ul>
<li>Fixed a hang in Durable Objects when reading more than 16MB of data at once (for example, with a large <code>list()</code> operation).</li>
<li>Added a new compatibility flag <code>html_rewriter_treats_esi_include_as_void_tag</code> which causes <code>HTMLRewriter</code> to treat <code>&lt;esi:include&gt;</code> and <code>&lt;esi:comment&gt;</code> as void tags, such that they are considered to have neither an end tag nor nested content. To opt a worker into the new behavior, you must use Wrangler v1.19.0 or newer and specify the flag in <code>wrangler.toml</code>. Refer to the <a href="https://github.com/cloudflare/wrangler-legacy/pull/2009">Wrangler compatibility flag notes</a> for details.</li>
</ul>
<h2 id="2021-07-23">2021-07-23</h2>
<ul>
<li>Performance and stability improvements.</li>
</ul>
<h2 id="2021-07-16">2021-07-16</h2>
<ul>
<li>Workers can now make up to 1000 subrequests to Durable Objects from a within a single request invocation, up from the prior limit of 50.</li>
<li>Major changes to Durable Objects implementation, the details of which will be the subject of an upcoming blog post. In theory, the changes should not harm existing apps, except to make them faster. Let your account team know if you observe anything unusual or report your issue in the <a href="https://discord.cloudflare.com">Workers Discord</a>.</li>
<li>Durable Object constructors may now initiate I/O, such as <code>fetch()</code> calls.</li>
<li>Added Durable Objects <code>state.blockConcurrencyWhile()</code> API useful for delaying delivery of requests and other events while performing some critical state-affecting task. For example, this can be used to perform start-up initialization in an object’s constructor.</li>
<li>In Durable Objects, the callback passed to <code>storage.transaction()</code> can now return a value, which will be propagated as the return value of the <code>transaction()</code> call.</li>
</ul>
<h2 id="2021-07-13">2021-07-13</h2>
<ul>
<li>The preview service now prints a warning in the devtools console when a script uses <code>Response/Request.clone()</code> but does not read one of the cloned bodies. Such a situation forces the runtime to buffer the entire message body in memory, which reduces performance. <a href="https://cloudflareworkers.com/#823fbe463bfafd5a06bcfeabbdf5eeae:https://tutorial.cloudflareworkers.com">Find an example here</a>.</li>
</ul>
<h2 id="2021-07-01">2021-07-01</h2>
<ul>
<li>Fixed bug where registering the same exact event listener method twice on the same event type threw an internal error.</li>
<li>Add support for the <code>.forEach()</code> method for <code>Headers</code>, <code>URLSearchParameters</code>, and <code>FormData</code>.</li>
</ul>
<h2 id="2021-06-27">2021-06-27</h2>
<ul>
<li>WebCrypto: Implemented non-standard Ed25519 operation (algorithm NODE-ED25519, curve name NODE-ED25519). The Ed25519 implementation differs from NodeJS’s in that raw import/export of private keys is disallowed, per parity with ECDSA/ECDH.</li>
</ul>
<h2 id="2021-06-17">2021-06-17</h2>
<p>Changes this week:</p>
<ul>
<li>Updated V8 from 9.1 to 9.2.</li>
<li><code>wrangler tail</code> now works on Durable Objects. Note that logs from long-lived WebSockets will not be visible until the WebSocket is closed.</li>
</ul>
<h2 id="2021-06-11">2021-06-11</h2>
<p>Changes this week:</p>
<ul>
<li>Turn on V8 Sparkplug compiler.</li>
<li>Durable Objects that are finishing up existing requests after their code is updated will be disconnected from the persistent storage API, to maintain the invariant that only a single instance ever has access to persistent storage for a given Durable Object.</li>
</ul>
<h2 id="2021-06-04">2021-06-04</h2>
<p>Changes this week:</p>
<ul>
<li>WebCrypto: We now support the “raw” import/export format for ECDSA/ECDH public keys.</li>
<li><code>request.cf</code> is no longer missing when writing Workers using modules syntax.</li>
</ul>
<h2 id="2021-05-14">2021-05-14</h2>
<p>Changes this week:</p>
<ul>
<li>Improve error messages coming from the WebCrypto API.</li>
<li>Updated V8: 9.0 → 9.1</li>
</ul>
<p>Changes in an earlier release:</p>
<ul>
<li>WebCrypto: Implement JWK export for RSA, ECDSA, &amp; ECDH.</li>
<li>WebCrypto: Add support for RSA-OAEP</li>
<li>WebCrypto: HKDF implemented.</li>
<li>Fix recently-introduced backwards clock jumps in Durable Objects.</li>
<li><code>WebCrypto.generateKey()</code>, when asked to generate a key pair with algorithm RSA-PSS, would instead return a key pair using algorithm RSASSA-PKCS1-v1_5. Although the key structure is the same, the signature algorithms differ, and therefore, signatures generated using the key would not be accepted by a correct implementation of RSA-PSS, and vice versa. Since this would be a pretty obvious problem, but no one ever reported it to us, we guess that currently, no one is using this functionality on Workers.</li>
</ul>
<h2 id="2021-04-29">2021-04-29</h2>
<p>Changes this week:</p>
<ul>
<li>WebCrypto: Implemented <code>wrapKey()</code> / <code>unwrapKey()</code> for AES algorithms.</li>
<li>The arguments to <code>WebSocket.close()</code> are now optional, as the standard says they should be.</li>
</ul>
<h2 id="2021-04-23">2021-04-23</h2>
<p>Changes this week:</p>
<ul>
<li>In the WebCrypto API, encrypt and decrypt operations are now supported for the “AES-CTR” encryption algorithm.</li>
<li>For Durable Objects, CPU time limits are now enforced on the object level rather than the request level. Each time a new request arrives, the time limit is “topped up” to 500ms. After the (free) beta period ends and Durable Objects becomes generally available, we will increase this to 30 seconds.</li>
<li>When a Durable Object exceeds its CPU time limit, the entire object will be discarded and recreated. Previously, we allowed subrequest requests to continue using the same object, but this was dangerous because hitting the CPU time limit can leave the object in an inconsistent state.</li>
<li>Long running Durable Objects are given more subrequest quota as additional WebSocket messages are sent to them, to avoid the problem of a long-running Object being unable to make any more subrequests after it has been held open by a particular WebSocket for a while.</li>
<li>When a Durable Object’s code is updated, or when its isolate is reset due to exceeding the memory limit, all stubs pointing to the object will become invalidated and have to be recreated. This is consistent with what happens when the CPU time is exceeded, or when stubs become disconnected due to random network errors. This behavior is useful, as apps can now assume that two messages sent to the same stub will be delivered to exactly the same live instance (if they are delivered at all). Apps which do not care about this property should recreate their stubs for every request; there is no performance penalty from doing so.</li>
<li>When a Durable Object’s isolate exceeds its memory limit, an exception with an explanatory message will now be thrown to the caller, instead of “internal error”.</li>
<li>When a Durable Object exceeds its CPU time limit, an exception with an explanatory message will now be thrown to the caller, instead of “internal error”.</li>
<li><code>wrangler tail</code> now reports CPU-time-exceeded exceptions with an explanatory message instead of “internal error”.</li>
</ul>
<h2 id="2021-04-19">2021-04-19</h2>
<p>Changes since the last post on 3/26:</p>
<ul>
<li>Cron Triggers now have a 15 minute wall time limit, in addition to the existing CPU time limit. (Previously, there was no limit, so a cron trigger that spent all its time waiting for I/O could hang forever.)</li>
<li>Our WebCrypto implementation now supports importing and exporting HMAC and AES keys in JWK format.</li>
<li>Our WebCrypto implementation now supports AES key generation for CTR, CBC, and KW modes. AES-CTR encrypt/decrypt and AES-KW key wrapping/unwrapping support will land in a later release.</li>
<li>Fixed bug where <code>crypto.subtle.encrypt()</code> on zero-length inputs would sometimes throw an exception.</li>
<li>Errors on script upload will now be properly reported for module-based scripts, instead of appearing as a ReferenceError.</li>
<li>WebCrypto: Key derivation for ECDH.</li>
<li>WebCrypto: Support ECDH key generation &amp; import.</li>
<li>WebCrypto: Support ECDSA key generation.</li>
<li>Fixed bug where <code>crypto.subtle.encrypt()</code> on zero-length inputs would sometimes throw an exception.</li>
<li>Improved exception messages thrown by the WebCrypto API somewhat.</li>
<li><code>waitUntil</code> is now supported for module Workers. An additional argument called ‘ctx’ is passed after ‘env’, and <code>waitUntil</code> is a method on ‘ctx’.</li>
<li><code>passThroughOnException</code> is now available under the ctx argument to module handlers</li>
<li>Reliability improvements for Durable Objects</li>
<li>Reliability improvements for Durable Objects persistent storage API</li>
<li><code>ScheduledEvent.cron</code> is now set to the original cron string that the event was scheduled for.</li>
</ul>
<h2 id="2021-03-26">2021-03-26</h2>
<p>Changes this week:</p>
<ul>
<li>Existing WebSocket connections to Durable Objects will now be forcibly disconnected on code updates, in order to force clients to connect to the instance running the new code.</li>
</ul>
<h2 id="2021-03-11">2021-03-11</h2>
<p>New this week:</p>
<ul>
<li>When the Workers Runtime itself reloads due to us deploying a new version or config change, we now preload high-traffic Workers in the new instance of the runtime before traffic cuts over. This ensures that users do not observe cold starts for these Workers due to the upgrade, and also fixes a low rate of spurious 503 errors that we had previously been seeing due to overload during such reloads.</li>
</ul>
<p>(It looks like no release notes were posted the last few weeks, but there were no new user-visible changes to report.)</p>
<h2 id="2021-02-11">2021-02-11</h2>
<p>Changes this week:</p>
<ul>
<li>In the preview mode of the dashboard, a Worker that fails during startup will now return a 500 response, rather than getting the default passthrough behavior, which was making it harder to notice when a Worker was failing.</li>
<li>A Durable Object’s ID is now provided to it in its constructor. It can be accessed off of the <code>state</code> provided as the constructor’s first argument, as in <code>state.id</code>.</li>
</ul>
<h2 id="2021-02-05">2021-02-05</h2>
<p>New this week:</p>
<ul>
<li>V8 has been updated from 8.8 to 8.9.</li>
<li>During a <code>fetch()</code>, if the destination server commits certain HTTP protocol errors, such as returning invalid (unparsable) headers, we now throw an exception whose description explains the problem, rather than an “internal error”.</li>
</ul>
<p>New last week (forgot to post):</p>
<ul>
<li>Added support for <code>waitUntil()</code> in Durable Objects. It is a method on the state object passed to the Durable Object class’s constructor.</li>
</ul>
<h2 id="2021-01-22">2021-01-22</h2>
<p>New in the past week:</p>
<ul>
<li>Fixed a bug which caused scripts with WebAssembly modules to hang when using devtools in the preview service.</li>
</ul>
<h2 id="2021-01-14">2021-01-14</h2>
<p>Changes this week:</p>
<ul>
<li>Implemented File and Blob APIs, which can be used when constructing FormData in outgoing requests. Unfortunately, FormData from incoming requests at this time will still use strings even when file metadata was present, in order to avoid breaking existing deployed Workers. We will find a way to fix that in the future.</li>
</ul>
<h2 id="2021-01-07">2021-01-07</h2>
<p>Changes this week:</p>
<ul>
<li>No user-visible changes.</li>
</ul>
<p>Changes in the prior release:</p>
<ul>
<li>Fixed delivery of WebSocket “error” events.</li>
<li>Fixed a rare bug where a WritableStream could be garbage collected while it still had writes queued, causing those writes to be lost.</li>
</ul>
<h2 id="2020-12-10">2020-12-10</h2>
<p>Changes this week:</p>
<ul>
<li>Major V8 update: 8.7.220.29 -&gt; 8.8.278.8</li>
</ul>
<h2 id="2019-09-19">2019-09-19</h2>
<p>Changes this week:</p>
<ul>
<li>Unannounced new feature. (Stay tuned.)</li>
<li>Enforced new limit on concurrent subrequests (see below).</li>
<li>Stability improvements.</li>
</ul>
<p><strong>Concurrent Subrequest Limit</strong></p>
<p>As of this release, we impose a limit on the number of outgoing HTTP requests that a Worker can make simultaneously. <strong>For each incoming request</strong>, a Worker can make up to 6 concurrent outgoing <code>fetch()</code> requests.</p>
<p>If a Worker’s request handler attempts to call <code>fetch()</code> more than six times (on behalf of a single incoming request) without waiting for previous fetches to complete, then fetches after the sixth will be delayed until previous fetches have finished. A Worker is still allowed to make up to 50 total subrequests per incoming request, as before; the new limit is only on how many can execute simultaneously.</p>
<p><strong>Automatic deadlock avoidance</strong></p>
<p>Our implementation automatically detects if delaying a fetch would cause the Worker to deadlock, and prevents the deadlock by cancelling the least-recently-used request. For example, imagine a Worker that starts 10 requests and waits to receive all the responses without reading the response bodies. A fetch is not considered complete until the response body is fully-consumed (for example, by calling <code>response.text()</code> or <code>response.json()</code>, or by reading from <code>response.body</code>). Therefore, in this scenario, the first six requests will run and their response objects would be returned, but the remaining four requests would not start until the earlier responses are consumed. If the Worker fails to actually read the earlier response bodies and is still waiting for the last four requests, then the Workers Runtime will automatically cancel the first four requests so that the remaining ones can complete. If the Worker later goes back and tries to read the response bodies, exceptions will be thrown.</p>
<p><strong>Most Workers are Not Affected</strong></p>
<p>The vast majority of Workers make fewer than six outgoing requests per incoming request. Such Workers are totally unaffected by this change.</p>
<p>Of Workers that do make more than six outgoing requests concurrently for a single incoming request, the vast majority either read the response bodies immediately upon each response returning, or never read the response bodies at all. In either case, these Workers will still work as intended – although they may be a little slower due to outgoing requests after the sixth being delayed.</p>
<p>A very small number of deployed Workers (about 20 total) make more than 6 requests concurrently, wait for all responses to return, and then go back to read the response bodies later. For all known Workers that do this, we have temporarily grandfathered your zone into the old behavior, so that your Workers will continue to operate. However, we will be communicating with customers one-by-one to request that you update your code to proactively read request bodies, so that it works correctly under the new limit.</p>
<p><strong>Why did we do this?</strong></p>
<p>Cloudflare communicates with origin servers using HTTP/1.1, not HTTP/2. Under HTTP/1.1, each concurrent request requires a separate connection. So, Workers that make many requests concurrently could force the creation of an excessive number of connections to origin servers. In some cases, this caused resource exhaustion problems either at the origin server or within our own stack.</p>
<p>On investigating the use cases for such Workers, every case we looked at turned out to be a mistake or otherwise unnecessary. Often, developers were making requests and receiving responses, but they only cared about the response status and headers but not the body. So, they threw away the response objects without reading the body, essentially leaking connections. In some other cases, developers had simply accidentally written code that made excessive requests in a loop for no good reason at all. Both of these cases should now cause no problems under the new behavior.</p>
<p>We chose the limit of 6 concurrent connections based on the fact that Chrome enforces the same limit on web sites in the browser.</p>
<h2 id="2020-12-04">2020-12-04</h2>
<p>Changes this week:</p>
<ul>
<li>Durable Objects storage API now supports listing keys by prefix.</li>
<li>Improved error message when a single request performs more than 1000 KV operations to make clear that a per-request limit was reached, not a global rate limit.</li>
<li><code>wrangler dev</code> previews should now honor non-default resource limits, for example, longer CPU limits for those in the Workers Unbound beta.</li>
<li>Fixed off-by-one line numbers in Worker exceptions.</li>
<li>Exceptions thrown in a Durable Object’s <code>fetch()</code> method are now tunneled to its caller.</li>
<li>Fixed a bug where a large Durable Object response body could cause the Durable Object to become unresponsive.</li>
</ul>
<h2 id="2020-11-13">2020-11-13</h2>
<p>Changes over the past week:</p>
<ul>
<li><code>ReadableStream.cancel()</code> and <code>ReadableStream.getReader().cancel()</code> now take an optional, instead of a mandatory, argument, to conform with the Streams spec.</li>
<li>Fixed an error that occurred when a WASM module declared that it wanted to grow larger than 128MB. Instead, the actual memory usage of the module is monitored and an error is thrown if it exceeds 128MB used.</li>
</ul>
<h2 id="2020-11-05">2020-11-05</h2>
<p>Changes this week:</p>
<ul>
<li>Major V8 update: 8.6 -&gt; 8.7</li>
<li>Limit the maximum number of Durable Objects keys that can be changed in a single transaction to 128.</li>
</ul>
<h2 id="2020-10-05">2020-10-05</h2>
<p>We had our usual weekly release last week, but:</p>
<ul>
<li>No user-visible changes.</li>
</ul>
<h2 id="2020-09-24">2020-09-24</h2>
<p>Changes this week:</p>
<ul>
<li>Internal changes to support upcoming features.</li>
</ul>
<p>Also, a change from the 2020-09-08 release that it seems we forgot to post:</p>
<ul>
<li>V8 major update: 8.5 -&gt; 8.6</li>
</ul>
<h2 id="2020-08-03">2020-08-03</h2>
<p>Changes last week:</p>
<ul>
<li>Fixed a regression which could cause <code>HTMLRewriter.transform()</code> to throw spurious “The parser has stopped.” errors.</li>
<li>Upgraded V8 from 8.4 to 8.5.</li>
</ul>
<h2 id="2020-07-09">2020-07-09</h2>
<p>Changes this week:</p>
<ul>
<li>Fixed a regression in HTMLRewriter: <a href="https://github.com/cloudflare/lol-html/issues/50">https://github.com/cloudflare/lol-html/issues/50</a></li>
<li>Common HTTP method names passed to <code>fetch()</code> or <code>new Request()</code> are now case-insensitive as required by the Fetch API spec.</li>
</ul>
<p>Changes last week (… forgot to post):</p>
<ul>
<li><code>setTimeout</code>/<code>setInterval</code> can now take additional arguments which will be passed on to the callback, as required by the spec. (Few people use this feature today because it’s usually much easier to use lambda captures.)</li>
</ul>
<p>Changes the week before last (… also… forgot to post… we really need to code up a bot for this):</p>
<ul>
<li>The HTMLRewriter now supports the <code>:nth-child</code> , <code>:first-child</code> , <code>:nth-of-type</code> , and <code>:first-of-type</code> selectors.</li>
</ul>
<h2 id="2020-05-15">2020-05-15</h2>
<p>Changes this week:</p>
<ul>
<li>Implemented API for yet-to-be-announced new feature.</li>
</ul>
<h2 id="2020-04-20">2020-04-20</h2>
<p>Looks like we forgot to post release notes for a couple weeks. Releases still are happening weekly as always, but the “post to the community” step is insufficiently automated…
4/2 release:</p>
<ul>
<li>Fixed a source of long garbage collection paused in memory limit enforcement.</li>
</ul>
<p>4/9 release:</p>
<ul>
<li>No publicly-visible changes.</li>
</ul>
<p>4/16 release:</p>
<ul>
<li>In preview, we now log a warning when attempting to construct a <code>Request</code> or <code>Response</code> whose body is of type <code>FormData</code> but with the <code>Content-Type</code> header overridden. Such bodies would not be parseable by the receiver.</li>
</ul>
<h2 id="2020-03-26">2020-03-26</h2>
<p>New this week:</p>
<ul>
<li>Certain “internal errors” that could be thrown when using the Cache API are now reported with human-friendly error messages. For example, <code>caches.default.match(&quot;not a URL&quot;)</code> now throws a TypeError.</li>
</ul>
<h2 id="2020-02-28">2020-02-28</h2>
<p>New from the past two weeks:</p>
<ul>
<li>Fixed a bug in the preview service where the CPU time limiter was overly lenient for the first several requests handled by a newly-started worker. The same bug actually exists in production as well, but we are much more cautious about fixing it there, since doing so might break live sites. If you find your worker now exceeds CPU time limits in preview, then it is likely exceeding time limits in production as well, but only appearing to work because the limits are too lenient for the first few requests. Such Workers will eventually fail in production, too (and always have), so it is best to fix the problem in preview before deploying.</li>
<li>Major V8 update: 8.0 -&gt; 8.1</li>
<li>Minor bug fixes.</li>
</ul>
<h2 id="2020-02-13">2020-02-13</h2>
<p>Changes over the last couple weeks:</p>
<ul>
<li>Fixed a bug where if two differently-named scripts within the same account had identical content and were deployed to the same zone, they would be treated as the “same Worker”, meaning they would share the same isolate and global variables. This only applied between Workers on the same zone, so was not a security threat, but it caused confusion. Now, two differently-named Worker scripts will never be considered the same Worker even if they have identical content.</li>
<li>Performance and stability improvements.</li>
</ul>
<h2 id="2020-01-24">2020-01-24</h2>
<p>It has been a while since we posted release notes, partly due to the holidays. Here is what is new over the past month:</p>
<ul>
<li>Performance and stability improvements.</li>
<li>A rare source of <code>daemonDown</code> errors when processing bursty traffic over HTTP/2 has been eliminated.</li>
<li>Updated V8 7.9 -&gt; 8.0.</li>
</ul>
<h2 id="2019-12-12">2019-12-12</h2>
<p>New this week:</p>
<ul>
<li>We now pass correct line and column numbers more often when reporting exceptions to the V8 inspector. There remain some cases where the reported line and column numbers will be wrong.</li>
<li>Fixed a significant source of daemonDown (1105) errors.</li>
</ul>
<h2 id="2019-12-06">2019-12-06</h2>
<p>Runtime release notes covering the past few weeks:</p>
<ul>
<li>Increased total per-request <code>Cache.put()</code> limit to 5GiB.</li>
<li>Increased individual <code>Cache.put()</code> limits to the lesser of 5GiB or the zone’s normal <a href="/cache/concepts/default-cache-behavior/">cache limits</a>.</li>
<li>Added a helpful error message explaining AES decryption failures.</li>
<li>Some overload errors were erroneously being reported as daemonDown (1105) errors. They have been changed to exceededCpu (1102) errors, which better describes their cause.</li>
<li>More “internal errors” were converted to useful user-facing errors.</li>
<li>Stability improvements and bug fixes.</li>
</ul>
