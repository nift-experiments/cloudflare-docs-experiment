---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/items/workers-binding/
  description: Upload, list, and manage documents in AI Search instances using the Items Workers binding.
  full_title: Workers binding · Cloudflare AI Search docs
  head_html: <title>Workers binding · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload, list, and manage documents in AI Search instances using the Items Workers binding."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/items/workers-binding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/items/workers-binding/index.md"><meta property="og:title" content="Workers binding · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload, list, and manage documents in AI Search instances using the Items Workers binding."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/items/workers-binding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/items/workers-binding/#page","headline":"Workers binding \u00b7 Cloudflare AI Search docs","description":"Upload, list, and manage documents in AI Search instances using the Items Workers binding.","url":"https://developers.cloudflare.com/ai-search/api/items/workers-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/items/workers-binding/
  schema: 1
---
<p><a href="/workers/">Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones. Use a <a href="/workers/runtime-apis/bindings/">Workers binding</a> to upload, list, and manage documents in your AI Search instances from a Cloudflare Worker. Access the Items API through the <code>items</code> property on an instance handle.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3070.md")
</aside>
<h2 id="configure-the-binding">Configure the binding</h2>
<p>To use AI Search with Workers, you must create an AI Search binding. You create bindings by updating your <a href="/workers/wrangler/configuration/">Wrangler configuration</a>. AI Search provides two types of bindings:</p>
<ul>
<li>Namespace binding: <code>ai_search_namespaces</code></li>
<li>Instance binding: <code>ai_search</code></li>
</ul>
<h3 id="namespace-binding">Namespace binding</h3>
<p>Access all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a>. You can get, create, list, and delete instances at runtime.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3071.md")
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>binding</code></td>
<td>string</td>
<td>Yes</td>
<td>The variable name available on <code>env</code>. For example, <code>&quot;AI_SEARCH&quot;</code> makes it accessible as <code>env.AI_SEARCH</code>.</td>
</tr>
<tr>
<td><code>namespace</code></td>
<td>string</td>
<td>Yes</td>
<td>The <a href="/ai-search/concepts/namespaces/">namespace</a> to bind to. A <code>default</code> namespace is created automatically for every account. If the namespace does not exist, Wrangler creates it on deploy.</td>
</tr>
<tr>
<td><code>remote</code></td>
<td>boolean</td>
<td>No</td>
<td>Set to <code>true</code> for local development with <code>wrangler dev</code>.</td>
</tr>
</tbody>
</table>
<h3 id="instance-binding">Instance binding</h3>
<p>Bind directly to a single instance in the <code>default</code> namespace. Use this when you know which instance you need at deploy time.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3072.md")
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>binding</code></td>
<td>string</td>
<td>Yes</td>
<td>The variable name available on <code>env</code>. For example, <code>&quot;MY_SEARCH&quot;</code> makes it accessible as <code>env.MY_SEARCH</code>.</td>
</tr>
<tr>
<td><code>instance_name</code></td>
<td>string</td>
<td>Yes</td>
<td>The name of the AI Search instance. Must exist in the default namespace at deploy time.</td>
</tr>
<tr>
<td><code>remote</code></td>
<td>boolean</td>
<td>No</td>
<td>Set to <code>true</code> for local development with <code>wrangler dev</code>.</td>
</tr>
</tbody>
</table>
<h2 id="methods">Methods</h2>
<p>The Items API methods are available on both the <code>ai_search_namespaces</code> and <code>ai_search</code> bindings. With the namespace binding, call methods on the handle returned by <code>get()</code>. With the instance binding, call methods directly on the binding (for example, <code>env.MY_SEARCH.items.upload()</code>).</p>
<p>The examples below use the namespace binding.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;</code></pre>
<h3 id="items-upload"><code>items.upload()</code></h3>
<p>Uploads a document for indexing. Returns immediately. The document is queued for processing.</p>
<pre tabindex="0"><code class="language-ts">// Upload from a string&#10;await instance.items.upload(&#10;	&quot;faq.md&quot;,&#10;	&quot;# FAQ\n\nQ: How do I reset my password?\nA: Go to Settings &gt; Security...&quot;,&#10;);&#10;&#10;// Upload from an ArrayBuffer&#10;const pdfResponse = await fetch(&quot;https://example.com/guide.pdf&quot;);&#10;const pdfBuffer = await pdfResponse.arrayBuffer();&#10;await instance.items.upload(&quot;guide.pdf&quot;, pdfBuffer);&#10;&#10;// Upload from a ReadableStream&#10;await instance.items.upload(&quot;doc.txt&quot;, request.body);&#10;</code></pre>
<h4 id="upload-with-metadata">Upload with metadata</h4>
<p>Attach <a href="/ai-search/configuration/indexing/metadata/">custom metadata</a> to a document for filtering in search queries. Custom metadata fields must be defined on the instance first using the <a href="/ai-search/api/instances/workers-binding/#update">update()</a> method or at creation time.</p>
<pre tabindex="0"><code class="language-ts">await instance.items.upload(&quot;guide.pdf&quot;, pdfBuffer, {&#10;	metadata: {&#10;		category: &quot;onboarding&quot;,&#10;		language: &quot;en&quot;,&#10;		version: &quot;2.0&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>string</td>
<td>Yes</td>
<td>The filename for the uploaded document. Used as the item key.</td>
</tr>
<tr>
<td><code>content</code></td>
<td>ReadableStream, ArrayBuffer, or string</td>
<td>Yes</td>
<td>The document content. Maximum file size is 4 MB. Pass a string for plain text or markdown, an <code>ArrayBuffer</code> for binary files, or a <code>ReadableStream</code> for streaming uploads.</td>
</tr>
<tr>
<td><code>options.metadata</code></td>
<td>Record&lt;string, string&gt;</td>
<td>No</td>
<td>Custom metadata key-value pairs to attach to the item. Use for filtering in search queries. Maximum 5 fields per instance.</td>
</tr>
</tbody>
</table>
<h4 id="response">Response</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>The unique item identifier.</td>
</tr>
<tr>
<td><code>key</code></td>
<td>string</td>
<td>The filename or key of the item.</td>
</tr>
</tbody>
</table>
<h3 id="items-uploadandpoll"><code>items.uploadAndPoll()</code></h3>
<p>Uploads a document and polls until processing completes or the timeout is reached. Use this when you need to search the document immediately after upload.</p>
<pre tabindex="0"><code class="language-ts">// Wait for a specific document to finish indexing before searching&#10;const item = await instance.items.uploadAndPoll(&#10;	&quot;handbook.txt&quot;,&#10;	handbookContent,&#10;);&#10;console.log(`handbook.txt status: ${item.status}`); // &quot;completed&quot;&#10;&#10;// Now search across all uploaded documents&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;password reset policy&quot; }],&#10;});&#10;</code></pre>
<h4 id="parameters-1">Parameters</h4>
<p>Same as <a href="#parameters"><code>items.upload()</code></a>, with additional polling options:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>options.pollIntervalMs</code></td>
<td>number</td>
<td>No</td>
<td>How often to check the item status, in milliseconds. Defaults to <code>1000</code>.</td>
</tr>
<tr>
<td><code>options.timeoutMs</code></td>
<td>number</td>
<td>No</td>
<td>Maximum time to wait for processing to complete, in milliseconds. Defaults to <code>30000</code>.</td>
</tr>
</tbody>
</table>
<h4 id="response-1">Response</h4>
<p>Returns the full item object after polling completes:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>The unique item identifier.</td>
</tr>
<tr>
<td><code>key</code></td>
<td>string</td>
<td>The filename or key of the item.</td>
</tr>
<tr>
<td><code>status</code></td>
<td>string</td>
<td>The processing status: <code>queued</code>, <code>running</code>, <code>completed</code>, <code>error</code>, <code>skipped</code>, <code>outdated</code>.</td>
</tr>
<tr>
<td><code>chunks_count</code></td>
<td>number</td>
<td>Number of chunks created from the document.</td>
</tr>
<tr>
<td><code>file_size</code></td>
<td>number</td>
<td>Size of the uploaded file in bytes.</td>
</tr>
<tr>
<td><code>metadata</code></td>
<td>object</td>
<td>Item metadata including <code>filename</code>, <code>folder</code>, and <code>timestamp</code>.</td>
</tr>
<tr>
<td><code>source_id</code></td>
<td>string</td>
<td>The source identifier (for example, <code>builtin</code> for uploaded files).</td>
</tr>
<tr>
<td><code>created_at</code></td>
<td>string</td>
<td>Timestamp of when the item was created.</td>
</tr>
<tr>
<td><code>last_seen_at</code></td>
<td>string</td>
<td>Timestamp of when the item was last seen during indexing.</td>
</tr>
</tbody>
</table>
<h3 id="items-list"><code>items.list()</code></h3>
<p>Returns a paginated list of items in the instance.</p>
<pre tabindex="0"><code class="language-ts">const { result, result_info } = await instance.items.list();&#10;&#10;for (const item of result) {&#10;	console.log(`${item.key} (${item.status})`);&#10;}&#10;// result_info.total_count contains the total number of items&#10;</code></pre>
<h4 id="parameters-2">Parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>page</code></td>
<td>number</td>
<td>No</td>
<td>The page number to return. Defaults to <code>1</code>.</td>
</tr>
<tr>
<td><code>per_page</code></td>
<td>number</td>
<td>No</td>
<td>The number of items per page. Defaults to <code>20</code>. Maximum <code>50</code>.</td>
</tr>
<tr>
<td><code>status</code></td>
<td>string</td>
<td>No</td>
<td>Filter by processing status: <code>queued</code>, <code>running</code>, <code>completed</code>, <code>error</code>, <code>skipped</code>, or <code>outdated</code>.</td>
</tr>
<tr>
<td><code>sort_by</code></td>
<td>string</td>
<td>No</td>
<td>Sort order for items: <code>status</code> (default) or <code>modified_at</code>.</td>
</tr>
<tr>
<td><code>search</code></td>
<td>string</td>
<td>No</td>
<td>Search items by text content.</td>
</tr>
<tr>
<td><code>source</code></td>
<td>string</td>
<td>No</td>
<td>Filter by source identifier (for example, <code>builtin</code> for uploaded files).</td>
</tr>
</tbody>
</table>
<h4 id="response-2">Response</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>result</code></td>
<td>array</td>
<td>Array of item objects.</td>
</tr>
<tr>
<td><code>result[].id</code></td>
<td>string</td>
<td>The unique item identifier.</td>
</tr>
<tr>
<td><code>result[].key</code></td>
<td>string</td>
<td>The filename or key of the item.</td>
</tr>
<tr>
<td><code>result[].status</code></td>
<td>string</td>
<td>The processing status: <code>queued</code>, <code>running</code>, <code>completed</code>, <code>error</code>, <code>skipped</code>, <code>outdated</code>.</td>
</tr>
<tr>
<td><code>result[].chunks_count</code></td>
<td>number</td>
<td>Number of chunks created from the document.</td>
</tr>
<tr>
<td><code>result[].file_size</code></td>
<td>number</td>
<td>Size of the uploaded file in bytes.</td>
</tr>
<tr>
<td><code>result[].metadata</code></td>
<td>object</td>
<td>Item metadata including <code>filename</code>, <code>folder</code>, and <code>timestamp</code>.</td>
</tr>
<tr>
<td><code>result[].source_id</code></td>
<td>string</td>
<td>The source identifier (for example, <code>builtin</code> for uploaded files).</td>
</tr>
<tr>
<td><code>result[].created_at</code></td>
<td>string</td>
<td>Timestamp of when the item was created.</td>
</tr>
<tr>
<td><code>result[].last_seen_at</code></td>
<td>string</td>
<td>Timestamp of when the item was last seen during indexing.</td>
</tr>
<tr>
<td><code>result_info</code></td>
<td>object</td>
<td>Pagination metadata.</td>
</tr>
<tr>
<td><code>result_info.count</code></td>
<td>number</td>
<td>Number of items in the current page.</td>
</tr>
<tr>
<td><code>result_info.total_count</code></td>
<td>number</td>
<td>Total number of items in the instance.</td>
</tr>
<tr>
<td><code>result_info.page</code></td>
<td>number</td>
<td>The current page number.</td>
</tr>
<tr>
<td><code>result_info.per_page</code></td>
<td>number</td>
<td>Items per page.</td>
</tr>
</tbody>
</table>
<h3 id="items-delete"><code>items.delete()</code></h3>
<p>Deletes an item and its indexed chunks.</p>
<pre tabindex="0"><code class="language-ts">await instance.items.delete(&quot;item-id-123&quot;);&#10;</code></pre>
<h4 id="parameters-3">Parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>itemId</code></td>
<td>string</td>
<td>Yes</td>
<td>The unique identifier of the item to delete.</td>
</tr>
</tbody>
</table>
<h4 id="response-3">Response</h4>
<p>Returns <code>void</code>. Throws an error if the item does not exist.</p>
<h3 id="items-get"><code>items.get()</code></h3>
<p>Returns a handle to a specific item for retrieving its status or downloading the original file.</p>
<h4 id="items-get-info"><code>items.get().info()</code></h4>
<p>Returns the status and metadata of a specific item.</p>
<pre tabindex="0"><code class="language-ts">const itemInfo = await instance.items.get(&quot;item-id-123&quot;).info();&#10;</code></pre>
<h5 id="parameters-4">Parameters</h5>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>itemId</code></td>
<td>string</td>
<td>Yes</td>
<td>The unique identifier of the item.</td>
</tr>
</tbody>
</table>
<h5 id="response-4">Response</h5>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>The unique item identifier.</td>
</tr>
<tr>
<td><code>key</code></td>
<td>string</td>
<td>The filename or key of the item.</td>
</tr>
<tr>
<td><code>status</code></td>
<td>string</td>
<td>The processing status: <code>queued</code>, <code>running</code>, <code>completed</code>, <code>error</code>, <code>skipped</code>, <code>outdated</code>.</td>
</tr>
<tr>
<td><code>chunks_count</code></td>
<td>number</td>
<td>Number of chunks created from the document.</td>
</tr>
<tr>
<td><code>file_size</code></td>
<td>number</td>
<td>Size of the uploaded file in bytes.</td>
</tr>
<tr>
<td><code>metadata</code></td>
<td>object</td>
<td>Item metadata including <code>filename</code>, <code>folder</code>, and <code>timestamp</code>.</td>
</tr>
<tr>
<td><code>source_id</code></td>
<td>string</td>
<td>The source identifier (for example, <code>builtin</code> for uploaded files).</td>
</tr>
<tr>
<td><code>created_at</code></td>
<td>string</td>
<td>Timestamp of when the item was created.</td>
</tr>
<tr>
<td><code>last_seen_at</code></td>
<td>string</td>
<td>Timestamp of when the item was last seen during indexing.</td>
</tr>
</tbody>
</table>
<h4 id="items-get-download"><code>items.get().download()</code></h4>
<p>Downloads the original source file for an item.</p>
<pre tabindex="0"><code class="language-ts">const file = await instance.items.get(&quot;item-id-123&quot;).download();&#10;// file.body is a ReadableStream&#10;</code></pre>
<h5 id="parameters-5">Parameters</h5>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>itemId</code></td>
<td>string</td>
<td>Yes</td>
<td>The unique identifier of the item.</td>
</tr>
</tbody>
</table>
<h5 id="response-5">Response</h5>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>filename</code></td>
<td>string</td>
<td>The original filename.</td>
</tr>
<tr>
<td><code>contentType</code></td>
<td>string</td>
<td>The MIME type of the file (for example, <code>application/pdf</code>).</td>
</tr>
<tr>
<td><code>size</code></td>
<td>number</td>
<td>The file size in bytes.</td>
</tr>
<tr>
<td><code>body</code></td>
<td>ReadableStream</td>
<td>A readable stream of the file contents.</td>
</tr>
</tbody>
</table>
