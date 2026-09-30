---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/
  description: Insert and upsert vectors into a Vectorize index, including supported formats and namespaces.
  full_title: Insert vectors · Cloudflare Vectorize docs
  head_html: <title>Insert vectors · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Insert and upsert vectors into a Vectorize index, including supported formats and namespaces."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/index.md"><meta property="og:title" content="Insert vectors · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Insert and upsert vectors into a Vectorize index, including supported formats and namespaces."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/#page","headline":"Insert vectors \u00b7 Cloudflare Vectorize docs","description":"Insert and upsert vectors into a Vectorize index, including supported formats and namespaces.","url":"https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/best-practices/insert-vectors/
  schema: 1
---
<p>Vectorize indexes allow you to insert vectors at any point: Vectorize will optimize the index behind the scenes to ensure that vector search remains efficient, even as new vectors are added or existing vectors updated.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="insert-vs-upsert">Insert vs Upsert</h3>
@markup("md", "content/.markup/bodies/15283.md")
</aside>
<h2 id="supported-vector-formats">Supported vector formats</h2>
<p>Vectorize supports the insert/upsert of vectors in three formats:</p>
<ul>
<li>An array of floating point numbers (converted into a JavaScript <code>number[]</code> array).</li>
<li>A <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a></li>
<li>A <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array">Float64Array</a></li>
</ul>
<p>In most cases, a <code>number[]</code> array is the easiest when dealing with other APIs, and is the return type of most machine-learning APIs.</p>
<p>Vectorize stores and restitutes vector dimensions as Float32; vector dimensions provided as Float64 will be converted to Float32 before being stored.</p>
<h2 id="metadata">Metadata</h2>
<p>Metadata is an optional set of key-value pairs that can be attached to a vector on insert or upsert, and allows you to embed or co-locate data about the vector itself.</p>
<p>Metadata keys cannot be empty, contain the dot character (<code>.</code>), contain the double-quote character (<code>&quot;</code>), or start with the dollar character (<code>$</code>).</p>
<p>Metadata can be used to:</p>
<ul>
<li>Include the object storage key, database UUID or other identifier to look up the content the vector embedding represents.</li>
<li>Store JSON data (up to the <a href="/vectorize/platform/limits/">metadata limits</a>), which can allow you to skip additional lookups for smaller content.</li>
<li>Keep track of dates, timestamps, or other metadata that describes when the vector embedding was generated or how it was generated.</li>
</ul>
<p>For example, a vector embedding representing an image could include the path to the <a href="/r2/">R2 object</a> it was generated from, the format, and a category lookup:</p>
<pre tabindex="0"><code class="language-ts">{ id: &#x27;1&#x27;, values: [32.4, 74.1, 3.2, ...], metadata: { path: &#x27;r2://bucket-name/path/to/image.png&#x27;, format: &#x27;png&#x27;, category: &#x27;profile_image&#x27; } }&#10;</code></pre>
<h3 id="performance-tips-when-filtering-by-metadata">Performance Tips When Filtering by Metadata</h3>
<p>When creating metadata indexes for a large Vectorize index, we encourage users to think ahead and plan how they will query for vectors with filters on this metadata.</p>
<p>Carefully consider the cardinality of metadata values in relation to your queries. Cardinality is the level of uniqueness of data values within a set. Low cardinality means there are only a few unique values: for instance, the number of planets in the Solar System; the number of countries in the world. High cardinality means there are many unique values: UUIv4 strings; timestamps with millisecond precision.</p>
<p>High cardinality is good for the selectiveness of the equal (<code>$eq</code>) filter. For example, if you want to find vectors associated with one user's id. But the filter is not going to help if all vectors have the same value. That's an example of extreme low cardinality.</p>
<p>High cardinality can also impact range queries, which searches across multiple unique metadata values. For example, an indexed metadata value using millisecond timestamps will see lower performance if the range spans long periods of time in which thousands of vectors with unique timestamps were written.</p>
<p>Behind the scenes, Vectorize uses a reverse index to map values to vector ids. If the number of unique values in a particular range is too high, then that requires reading large portions of the index (a full index scan in the worst case). This would lead to memory issues, so Vectorize will degrade performance and the accuracy of the query in order to finish the request.</p>
<p>One approach for high cardinality data is to somehow create buckets where more vectors get grouped to the same value. Continuing the millisecond timestamp example, let's imagine we typically filter with date ranges that have 5 minute increments of granularity. We could use a timestamp which is rounded down to the last 5 minute point. This &quot;windows&quot; our metadata values into 5 minute increments. And we can still store the original millisecond timestamp as a separate non-indexed field.</p>
<h2 id="namespaces">Namespaces</h2>
<p>Namespaces provide a way to segment the vectors within your index. For example, by customer, merchant or store ID.</p>
<p>To associate vectors with a namespace, you can optionally provide a <code>namespace: string</code> value when performing an insert or upsert operation. When querying, you can pass the namespace to search within as an optional parameter to your query.</p>
<p>A namespace can be up to 64 characters (bytes) in length and you can have up to 1,000 namespaces per index. Refer to the <a href="/vectorize/platform/limits/">Limits</a> documentation for more details.</p>
<p>When a namespace is specified in a query operation, only vectors within that namespace are used for the search. Namespace filtering is applied before vector search, increasing the precision of the matched results.</p>
<p>To insert vectors with a namespace:</p>
<pre tabindex="0"><code class="language-ts">// Mock vectors&#10;// Vectors from a machine-learning model are typically ~100 to 1536 dimensions&#10;// wide (or wider still).&#10;const sampleVectors: Array&lt;VectorizeVector&gt; = [&#10;	{&#10;		id: &quot;1&quot;,&#10;		values: [32.4, 74.1, 3.2, ...],&#10;		namespace: &quot;text&quot;,&#10;	},&#10;	{&#10;		id: &quot;2&quot;,&#10;		values: [15.1, 19.2, 15.8, ...],&#10;		namespace: &quot;images&quot;,&#10;	},&#10;	{&#10;		id: &quot;3&quot;,&#10;		values: [0.16, 1.2, 3.8, ...],&#10;		namespace: &quot;pdfs&quot;,&#10;	},&#10;];&#10;&#10;// Insert your vectors, returning a count of the vectors inserted and their vector IDs.&#10;let inserted = await env.TUTORIAL_INDEX.insert(sampleVectors);&#10;</code></pre>
<p>To query vectors within a namespace:</p>
<pre tabindex="0"><code class="language-ts">// Your queryVector will be searched against vectors within the namespace (only)&#10;let matches = await env.TUTORIAL_INDEX.query(queryVector, {&#10;	namespace: &quot;images&quot;,&#10;});&#10;</code></pre>
<h2 id="improve-write-throughput">Improve Write Throughput</h2>
<p>One way to reduce the time to make updates visible in queries is to batch more vectors into fewer requests. This is important for write-heavy workloads. To see how many vectors you can write in a single request, please refer to the <a href="/vectorize/platform/limits/">Limits</a> page.</p>
<p>Vectorize writes changes immediately to a write ahead log for durability. To make these writes visible for reads, an asynchronous job needs to read the current index files from R2, create an updated index, write the new index files back to R2, and commit the change. To keep the overhead of writes low and improve write throughput, Vectorize will combine multiple changes together into a single batch. It sets the maximum size of a batch to 200,000 total vectors or to 1,000 individual updates, whichever limit it hits first.</p>
<p>For example, let's say we have 250,000 vectors we would like to insert into our index. We decide to insert them one at a time, calling the insert API 250,000 times. Vectorize will only process 1000 vectors in each job, and will need to work through 250 total jobs. This could take at least an hour to do.</p>
<p>The better approach is to batch our updates. For example, we can split our 250,000 vectors into 100 files, where each file has 2,500 vectors. We would call the insert HTTP API 100 times. Vectorize would update the index in only 2 or 3 jobs. All 250,000 vectors will visible in queries within minutes.</p>
<h2 id="examples">Examples</h2>
<h3 id="workers-api">Workers API</h3>
<p>Use the <code>insert()</code> and <code>upsert()</code> methods available on an index from within a Cloudflare Worker to insert vectors into the current index.</p>
<pre tabindex="0"><code class="language-ts">// Mock vectors&#10;// Vectors from a machine-learning model are typically ~100 to 1536 dimensions&#10;// wide (or wider still).&#10;const sampleVectors: Array&lt;VectorizeVector&gt; = [&#10;	{&#10;		id: &quot;1&quot;,&#10;		values: [32.4, 74.1, 3.2, ...],&#10;		metadata: { url: &quot;/products/sku/13913913&quot; },&#10;	},&#10;	{&#10;		id: &quot;2&quot;,&#10;		values: [15.1, 19.2, 15.8, ...],&#10;		metadata: { url: &quot;/products/sku/10148191&quot; },&#10;	},&#10;	{&#10;		id: &quot;3&quot;,&#10;		values: [0.16, 1.2, 3.8, ...],&#10;		metadata: { url: &quot;/products/sku/97913813&quot; },&#10;	},&#10;];&#10;&#10;// Insert your vectors, returning a count of the vectors inserted and their vector IDs.&#10;let inserted = await env.TUTORIAL_INDEX.insert(sampleVectors);&#10;</code></pre>
<p>Refer to <a href="/vectorize/reference/client-api/">Vectorize API</a> for additional examples.</p>
<h3 id="wrangler-cli">wrangler CLI</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-api-rate-limit">Cloudflare API rate limit</h3>
@markup("md", "content/.markup/bodies/15282.md")
</aside>
<p>You can bulk upload vector embeddings directly:</p>
<ul>
<li>The file must be in newline-delimited JSON (NDJSON format): each complete vector must be newline separated, and not within an array or object.</li>
<li>Vectors must be complete and include a unique string <code>id</code> per vector.</li>
</ul>
<p>An example NDJSON formatted file:</p>
<pre tabindex="0"><code class="language-json">{ &quot;id&quot;: &quot;4444&quot;, &quot;values&quot;: [175.1, 167.1, 129.9], &quot;metadata&quot;: {&quot;url&quot;: &quot;/products/sku/918318313&quot;}}&#10;{ &quot;id&quot;: &quot;5555&quot;, &quot;values&quot;: [158.8, 116.7, 311.4], &quot;metadata&quot;: {&quot;url&quot;: &quot;/products/sku/183183183&quot;}}&#10;{ &quot;id&quot;: &quot;6666&quot;, &quot;values&quot;: [113.2, 67.5, 11.2], &quot;metadata&quot;: {&quot;url&quot;: &quot;/products/sku/717313811&quot;}}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15281.md")
</aside>
<pre tabindex="0"><code class="language-sh">wrangler vectorize insert &lt;your-index-name&gt; --file=embeddings.ndjson&#10;</code></pre>
<h3 id="http-api">HTTP API</h3>
<p>Vectorize also supports inserting vectors via the <a href="/api/resources/vectorize/subresources/indexes/methods/insert/">REST API</a>, which allows you to operate on a Vectorize index from existing machine-learning tooling and languages (including Python).</p>
<p>For example, to insert embeddings in <a href="#workers-api">NDJSON format</a> directly from a Python script:</p>
<pre tabindex="0"><code class="language-py">import requests&#10;&#10;url = &quot;https://api.cloudflare.com/client/v4/accounts/{}/vectorize/v2/indexes/{}/insert&quot;.format(&quot;your-account-id&quot;, &quot;index-name&quot;)&#10;&#10;headers = {&#10;    &quot;Authorization&quot;: &quot;Bearer &lt;your-api-token&gt;&quot;&#10;}&#10;&#10;with open(&#x27;embeddings.ndjson&#x27;, &#x27;rb&#x27;) as embeddings:&#10;    resp = requests.post(url, headers=headers, files=dict(vectors=embeddings))&#10;    print(resp)&#10;</code></pre>
<p>This code would insert the vectors defined in <code>embeddings.ndjson</code> into the provided index. Python libraries, including Pandas, also support the NDJSON format via the built-in <code>read_json</code> method:</p>
<pre tabindex="0"><code class="language-py">import pandas as pd&#10;data = pd.read_json(&#x27;embeddings.ndjson&#x27;, lines=True)&#10;</code></pre>
