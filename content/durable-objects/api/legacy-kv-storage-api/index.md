---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/
  description: API reference for the legacy KV-backed Durable Objects storage methods, including get, put, delete, and list.
  full_title: KV-backed Durable Object Storage (Legacy) · Cloudflare Durable Objects docs
  head_html: <title>KV-backed Durable Object Storage (Legacy) · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for the legacy KV-backed Durable Objects storage methods, including get, put, delete, and list."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/index.md"><meta property="og:title" content="KV-backed Durable Object Storage (Legacy) · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for the legacy KV-backed Durable Objects storage methods, including get, put, delete, and list."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/#page","headline":"KV-backed Durable Object Storage (Legacy) \u00b7 Cloudflare Durable Objects docs","description":"API reference for the legacy KV-backed Durable Objects storage methods, including get, put, delete, and list.","url":"https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/api/legacy-kv-storage-api/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8378.md")
</aside>
<p>The Durable Object Storage API allows <span class="nb-glossary-tooltip" title="Durable Object">Durable Objects</span> to access transactional and strongly consistent storage. A Durable Object's attached storage is private to its unique instance and cannot be accessed by other objects.</p>
<p>The Durable Object Storage API comes with several methods, including SQL, point-in-time recovery (PITR), key-value (KV), and alarm APIs. Available API methods depend on the storage backend for a Durable Objects class, either <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite</a> or <a href="/durable-objects/reference/durable-object-class-migrations-legacy/#create-durable-object-class-with-key-value-storage">KV</a>.</p>
<table>
<thead>
<tr>
<th>Methods <sup>1</sup></th>
<th>SQLite-backed Durable Object class</th>
<th>KV-backed Durable Object class</th>
</tr>
</thead>
<tbody>
<tr>
<td>SQL API</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>PITR API</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Synchronous KV API</td>
<td>✅ <sup>2, 3</sup></td>
<td>❌</td>
</tr>
<tr>
<td>Asynchronous KV API</td>
<td>✅ <sup>3</sup></td>
<td>✅</td>
</tr>
<tr>
<td>Alarms API</td>
<td>✅</td>
<td>✅</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8380.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommended-sqlite-backed-durable-objects">Recommended SQLite-backed Durable Objects</h3>
@markup("md", "content/.markup/bodies/8377.md")
</aside>
<h2 id="access-storage">Access storage</h2>
<p>Durable Objects gain access to Storage API via the <code>DurableObjectStorage</code> interface and accessed by the <code>DurableObjectState::storage</code> property. This is frequently accessed via <code>this.ctx.storage</code> with the <code>ctx</code> parameter passed to the Durable Object constructor.</p>
<p>The following code snippet shows you how to store and retrieve data using the Durable Object Storage API.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8383.md")
</div></div>
<p>JavaScript is a single-threaded and event-driven programming language. This means that JavaScript runtimes, by default, allow requests to interleave with each other which can lead to concurrency bugs. The Durable Objects runtime uses a combination of <span class="nb-glossary-tooltip" title="input gate">input gates</span> and <span class="nb-glossary-tooltip" title="output gate">output gates</span> to avoid this type of concurrency bug when performing storage operations. Learn more in our <a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">blog post</a>.</p>
<h2 id="asynchronous-kv-api">Asynchronous KV API</h2>
<p>KV-backed Durable Objects provide KV API methods which are asynchronous.</p>
<h3 id="do-kv-async-get">get</h3>
<ul>
<li>
<p><code>ctx.storage.get(key <span class="nb-type">string</span>, options <span class="nb-type">Object</span>{&quot; &quot;}<span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise&lt;any&gt;</span></p>
<ul>
<li>Retrieves the value associated with the given key. The type of the returned value will be whatever was previously written for the key, or undefined if the key does not exist.</li>
</ul>
</li>
<li>
<p><code>ctx.storage.get(keys <span class="nb-type">Array&lt;string&gt;</span>, options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise&lt;Map&lt;string, any&gt;&gt;</span></p>
<ul>
<li>Retrieves the values associated with each of the provided keys. The type of each returned value in the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"><code>Map</code></a> will be whatever was previously written for the corresponding key. Results in the <code>Map</code> will be sorted in increasing order of their UTF-8 encodings, with any requested keys that do not exist being omitted. Supports up to 128 keys at a time.</li>
</ul>
</li>
</ul>
<h4 id="supported-options">Supported options</h4>
<ul>
<li>
<p><code>allowConcurrency</code>: <span class="nb-type">boolean</span></p>
<ul>
<li>By default, the system will pause delivery of I/O events to the Object while a storage operation is in progress, in order to avoid unexpected race conditions. Pass <code>allowConcurrency: true</code> to opt out of this behavior and allow concurrent events to be delivered.</li>
</ul>
</li>
<li>
<p><code>noCache</code>: <span class="nb-type">boolean</span></p>
<ul>
<li>If true, then the key/value will not be inserted into the in-memory cache. If the key is already in the cache, the cached value will be returned, but its last-used time will not be updated. Use this when you expect this key will not be used again in the near future. This flag is only a hint. This flag will never change the semantics of your code, but it may affect performance.</li>
</ul>
</li>
</ul>
<h3 id="do-kv-async-put">put</h3>
<ul>
<li>
<p><code>put(key <span class="nb-type">string</span>, value <span class="nb-type">any</span>, options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise</span></p>
<ul>
<li>
<p>Stores the value and associates it with the given key. The value can be any type supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm">structured clone algorithm</a>, which is true of most types.</p>
<p>The size of keys and values have different limits depending on the Durable Object storage backend you are using. Refer to either:</p>
<ul>
<li><a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">SQLite-backed Durable Object limits</a></li>
<li><a href="/durable-objects/platform/limits/#key-value-backed-durable-objects-general-limits">KV-backed Durable Object limits</a>.</li>
</ul>
<p>On a KV-backed Durable Object, if the serialized value exceeds the 128 KiB (131072 bytes) value-size limit, <code>put()</code> throws a <code>RangeError</code> (for example, <code>Values cannot be larger than 131072 bytes.</code>) before the write is applied.<br/><br/></p>
</li>
</ul>
</li>
<li>
<p><code>put(entries <span class="nb-type">Object</span>, options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise</span></p>
<ul>
<li>Takes an Object and stores each of its keys and values to storage.</li>
<li>Each value can be any type supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm">structured clone algorithm</a>, which is true of most types.</li>
<li>Supports up to 128 key-value pairs at a time. The size of keys and values have different limits depending on the flavor of Durable Object you are using. Refer to either:
<ul>
<li><a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">SQLite-backed Durable Object limits</a></li>
<li><a href="/durable-objects/platform/limits/#key-value-backed-durable-objects-general-limits">KV-backed Durable Object limits</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="do-kv-async-delete">delete</h3>
<ul>
<li>
<p><code>delete(key <span class="nb-type">string</span>, options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise&lt;boolean&gt;</span></p>
<ul>
<li>Deletes the key and associated value. Returns <code>true</code> if the key existed or <code>false</code> if it did not.</li>
</ul>
</li>
<li>
<p><code>delete(keys <span class="nb-type">Array&lt;string&gt;</span>, options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise&lt;number&gt;</span></p>
<ul>
<li>Deletes the provided keys and their associated values. Supports up to 128 keys at a time. Returns a count of the number of key-value pairs deleted.</li>
</ul>
</li>
</ul>
<h4 id="supported-options-1">Supported options</h4>
<ul>
<li>
<p><code>put()</code>, <code>delete()</code> and <code>deleteAll()</code> support the following options:</p>
</li>
<li>
<p><code>allowUnconfirmed</code> <span class="nb-type">boolean</span></p>
<ul>
<li>
<p>By default, the system will pause outgoing network messages from the Durable Object until all previous writes have been confirmed flushed to disk. If the write fails, the system will reset the Object, discard all outgoing messages, and respond to any clients with errors instead.</p>
</li>
<li>
<p>This way, Durable Objects can continue executing in parallel with a write operation, without having to worry about prematurely confirming writes, because it is impossible for any external party to observe the Object's actions unless the write actually succeeds.</p>
</li>
<li>
<p>After any write, subsequent network messages may be slightly delayed. Some applications may consider it acceptable to communicate on the basis of unconfirmed writes. Some programs may prefer to allow network traffic immediately. In this case, set <code>allowUnconfirmed</code> to <code>true</code> to opt out of the default behavior.</p>
</li>
<li>
<p>If you want to allow some outgoing network messages to proceed immediately but not others, you can use the allowUnconfirmed option to avoid blocking the messages that you want to proceed and then separately call the <a href="#sync"><code>sync()</code></a> method, which returns a promise that only resolves once all previous writes have successfully been persisted to disk.</p>
</li>
</ul>
</li>
<li>
<p><code>noCache</code> <span class="nb-type">boolean</span></p>
<ul>
<li>
<p>If true, then the key/value will be discarded from memory as soon as it has completed writing to disk.</p>
</li>
<li>
<p>Use <code>noCache</code> if the key will not be used again in the near future. <code>noCache</code> will never change the semantics of your code, but it may affect performance.</p>
</li>
<li>
<p>If you use <code>get()</code> to retrieve the key before the write has completed, the copy from the write buffer will be returned, thus ensuring consistency with the latest call to <code>put()</code>.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="automatic-write-coalescing">Automatic write coalescing</h3>
@markup("md", "content/.markup/bodies/8376.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="write-buffer-behavior">Write buffer behavior</h3>
@markup("md", "content/.markup/bodies/8375.md")
</aside>
<h3 id="do-kv-async-list">list</h3>
<ul>
<li><code>list(options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise&lt;Map&lt;string, any&gt;&gt;</span>
<ul>
<li>
<p>Returns all keys and values associated with the current Durable Object in ascending sorted order based on the keys' UTF-8 encodings.</p>
</li>
<li>
<p>The type of each returned value in the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"><code>Map</code></a> will be whatever was previously written for the corresponding key.</p>
</li>
<li>
<p>Be aware of how much data may be stored in your Durable Object before calling this version of <code>list</code> without options because all the data will be loaded into the Durable Object's memory, potentially hitting its <a href="/durable-objects/platform/limits/">limit</a>. If that is a concern, pass options to <code>list</code> as documented below.</p>
</li>
</ul>
</li>
</ul>
<h4 id="supported-options-2">Supported options</h4>
<ul>
<li>
<p><code>start</code> <span class="nb-type">string</span></p>
<ul>
<li>Key at which the list results should start, inclusive.</li>
</ul>
</li>
<li>
<p><code>startAfter</code> <span class="nb-type">string</span></p>
<ul>
<li>Key after which the list results should start, exclusive. Cannot be used simultaneously with <code>start</code>.</li>
</ul>
</li>
<li>
<p><code>end</code> <span class="nb-type">string</span></p>
<ul>
<li>Key at which the list results should end, exclusive.</li>
</ul>
</li>
<li>
<p><code>prefix</code> <span class="nb-type">string</span></p>
<ul>
<li>Restricts results to only include key-value pairs whose keys begin with the prefix.</li>
</ul>
</li>
<li>
<p><code>reverse</code> <span class="nb-type">boolean</span></p>
<ul>
<li>If true, return results in descending order instead of the default ascending order.</li>
<li>Enabling <code>reverse</code> does not change the meaning of <code>start</code>, <code>startKey</code>, or <code>endKey</code>. <code>start</code> still defines the smallest key in lexicographic order that can be returned (inclusive), effectively serving as the endpoint for a reverse-order list. <code>end</code> still defines the largest key in lexicographic order that the list should consider (exclusive), effectively serving as the starting point for a reverse-order list.</li>
</ul>
</li>
<li>
<p><code>limit</code> <span class="nb-type">number</span></p>
<ul>
<li>Maximum number of key-value pairs to return.</li>
</ul>
</li>
<li>
<p><code>allowConcurrency</code> <span class="nb-type">boolean</span></p>
<ul>
<li>Same as the option to <a href="#do-kv-async-get"><code>get()</code></a>, above.</li>
</ul>
</li>
<li>
<p><code>noCache</code> <span class="nb-type">boolean</span></p>
<ul>
<li>Same as the option to <a href="#do-kv-async-get"><code>get()</code></a>, above.</li>
</ul>
</li>
</ul>
<h2 id="alarms">Alarms</h2>
<h3 id="getalarm"><code>getAlarm</code></h3>
<ul>
<li><code>getAlarm(options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise&lt;Number | null&gt;</span>
<ul>
<li>Retrieves the current alarm time (if set) as integer milliseconds since epoch. The alarm is considered to be set if it has not started, or if it has failed and any retry has not begun. If no alarm is set, <code>getAlarm()</code> returns <code>null</code>.</li>
</ul>
</li>
</ul>
<h4 id="supported-options-3">Supported options</h4>
<ul>
<li>Same options as <a href="#do-kv-async-get"><code>get()</code></a>, but without <code>noCache</code>.</li>
</ul>
<h3 id="setalarm"><code>setAlarm</code></h3>
<ul>
<li>
<p><code>setAlarm(scheduledTime <span class="nb-type">Date | number</span>, options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise</span></p>
<ul>
<li>Sets the current alarm time, accepting either a JavaScript <code>Date</code>, or integer milliseconds since epoch.</li>
</ul>
<p>If <code>setAlarm()</code> is called with a time equal to or before <code>Date.now()</code>, the alarm will be scheduled for asynchronous execution in the immediate future. If the alarm handler is currently executing in this case, it will not be canceled. Alarms can be set to millisecond granularity and will usually execute within a few milliseconds after the set time, but can be delayed by up to a minute due to maintenance or failures while failover takes place.</p>
</li>
</ul>
<h3 id="deletealarm"><code>deleteAlarm</code></h3>
<ul>
<li><code>deleteAlarm(options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise</span>
<ul>
<li>Deletes the alarm if one exists. Does not cancel the alarm handler if it is currently executing.</li>
</ul>
</li>
</ul>
<h4 id="supported-options-4">Supported options</h4>
<ul>
<li><code>setAlarm()</code> and <code>deleteAlarm()</code> support the same options as <a href="#do-kv-async-put"><code>put()</code></a>, but without <code>noCache</code>.</li>
</ul>
<h2 id="other">Other</h2>
<h3 id="deleteall"><code>deleteAll</code></h3>
<ul>
<li><code>deleteAll(options <span class="nb-type">Object</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">Promise</span>
<ul>
<li>Deletes all stored data, effectively deallocating all storage used by the Durable Object. For Durable Objects with a key-value storage backend, <code>deleteAll()</code> removes all keys and associated values for an individual Durable Object. For Durable Objects with a <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a>, <code>deleteAll()</code> removes the entire contents of a Durable Object's private SQLite database, including both SQL data and key-value data.</li>
<li>For Durable Objects with a key-value storage backend, an in-progress <code>deleteAll()</code> operation can fail, which may leave a subset of data undeleted. Durable Objects with a SQLite storage backend do not have a partial <code>deleteAll()</code> issue because <code>deleteAll()</code> operations are atomic (all or nothing).</li>
<li>For Workers with a compatibility date of <code>2026-02-24</code> or later, <code>deleteAll()</code> also deletes any active <a href="/durable-objects/api/alarms/">alarm</a>. For earlier compatibility dates, <code>deleteAll()</code> does not delete alarms. Use <a href="/durable-objects/api/alarms/#deletealarm"><code>deleteAlarm()</code></a> separately, or enable the <code>delete_all_deletes_alarm</code> <a href="/workers/configuration/compatibility-flags/">compatibility flag</a>.</li>
</ul>
</li>
</ul>
<h3 id="transactionsync"><code>transactionSync</code></h3>
<ul>
<li><code>transactionSync(callback)</code>: <span class="nb-type">any</span>
<ul>
<li>
<p>Only available when using SQLite-backed Durable Objects.</p>
</li>
<li>
<p>Invokes <code>callback()</code> wrapped in a transaction, and returns its result.</p>
</li>
<li>
<p>If <code>callback()</code> throws an exception, the transaction will be rolled back.</p>
</li>
<li>
<p>The callback must complete synchronously, that is, it should not be declared <code>async</code> nor otherwise return a Promise. Only synchronous storage operations can be part of the transaction. This is intended for use with SQL queries using <a href="/durable-objects/api/sqlite-storage-api/#exec"><code>ctx.storage.sql.exec()</code></a>, which complete synchronously.</p>
</li>
</ul>
</li>
</ul>
<h3 id="transaction"><code>transaction</code></h3>
<ul>
<li>
<p><code>transaction(closureFunction(txn))</code>: <span class="nb-type">Promise</span></p>
<ul>
<li>
<p>Runs the sequence of storage operations called on <code>txn</code> in a single transaction that either commits successfully or aborts.</p>
</li>
<li>
<p>Explicit transactions are no longer necessary. Any series of write operations with no intervening <code>await</code> will automatically be submitted atomically, and the system will prevent concurrent events from executing while <code>await</code> a read operation (unless you use <code>allowConcurrency: true</code>). Therefore, a series of reads followed by a series of writes (with no other intervening I/O) are automatically atomic and behave like a transaction.</p>
</li>
</ul>
</li>
<li>
<p><code>txn</code></p>
<ul>
<li>
<p>Provides access to the <code>put()</code>, <code>get()</code>, <code>delete()</code>, and <code>list()</code> methods documented above to run in the current transaction context. In order to get transactional behavior within a transaction closure, you must call the methods on the <code>txn</code> Object instead of on the top-level <code>ctx.storage</code> Object.<br/><br/>Also supports a <code>rollback()</code> function that ensures any changes made during the transaction will be rolled back rather than committed. After <code>rollback()</code> is called, any subsequent operations on the <code>txn</code> Object will fail with an exception. <code>rollback()</code> takes no parameters and returns nothing to the caller.</p>
</li>
<li>
<p>When using <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">the SQLite-backed storage engine</a>, the <code>txn</code> object is obsolete. Any storage operations performed directly on the <code>ctx.storage</code> object, including SQL queries using <a href="/durable-objects/api/sqlite-storage-api/#exec"><code>ctx.storage.sql.exec()</code></a>, will be considered part of the transaction.</p>
</li>
</ul>
</li>
</ul>
<h3 id="sync"><code>sync</code></h3>
<ul>
<li><code>sync()</code>: <span class="nb-type">Promise</span>
<ul>
<li>
<p>Synchronizes any pending writes to disk.</p>
</li>
<li>
<p>This is similar to normal behavior from automatic write coalescing. If there are any pending writes in the write buffer (including those submitted with <a href="#supported-options-1">the <code>allowUnconfirmed</code> option</a>), the returned promise will resolve when they complete. If there are no pending writes, the returned promise will be already resolved.</p>
</li>
</ul>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct  Choose Three</a></li>
<li><a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a></li>
<li><a href="/durable-objects/best-practices/websockets/">WebSockets API</a></li>
</ul>
