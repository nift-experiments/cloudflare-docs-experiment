---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/best-practices/create-indexes/
  description: Learn how to create Vectorize indexes, configure dimensions, and choose distance metrics.
  full_title: Create indexes · Cloudflare Vectorize docs
  head_html: <title>Create indexes · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to create Vectorize indexes, configure dimensions, and choose distance metrics."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/best-practices/create-indexes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/best-practices/create-indexes/index.md"><meta property="og:title" content="Create indexes · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to create Vectorize indexes, configure dimensions, and choose distance metrics."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/best-practices/create-indexes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/best-practices/create-indexes/#page","headline":"Create indexes \u00b7 Cloudflare Vectorize docs","description":"Learn how to create Vectorize indexes, configure dimensions, and choose distance metrics.","url":"https://developers.cloudflare.com/vectorize/best-practices/create-indexes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/best-practices/create-indexes/
  schema: 1
---
<p>Indexes are the &quot;atom&quot; of Vectorize. Vectors are inserted into an index and enable you to query the index for similar vectors for a given input vector.</p>
<p>Creating an index requires three inputs:</p>
<ul>
<li>A kebab-cased name, such as <code>prod-search-index</code> or <code>recommendations-idx-dev</code>.</li>
<li>The (fixed) <a href="#dimensions">dimension size</a> of each vector, for example 384 or 1536.</li>
<li>The (fixed) <a href="#distance-metrics">distance metric</a> to use for calculating vector similarity.</li>
</ul>
<p>An index cannot be created using the same name as an index that is currently active on your account. However, an index can be created with a name that belonged to an index that has been deleted.</p>
<p>The configuration of an index cannot be changed after creation.</p>
<h2 id="create-an-index">Create an index</h2>
<h3 id="wrangler-cli">wrangler CLI</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15286.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="using-legacy-vectorize-v1-indexes">Using legacy Vectorize (V1) indexes?</h3>
@markup("md", "content/.markup/bodies/15285.md")
</aside>
<p>To create an index with <code>wrangler</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler vectorize create your-index-name --dimensions=NUM_DIMENSIONS --metric=SELECTED_METRIC&#10;</code></pre>
<p>To create an index that can accept vector embeddings from Worker's AI's <a href="/workers-ai/models/?tasks=Text+Embeddings"><code>@cf/baai/bge-base-en-v1.5</code></a> embedding model, which outputs vectors with 768 dimensions, use the following command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler vectorize create your-index-name --dimensions=768 --metric=cosine&#10;</code></pre>
<h3 id="http-api">HTTP API</h3>
<p>Vectorize also supports creating indexes via <a href="/api/resources/vectorize/subresources/indexes/methods/create/">REST API</a>.</p>
<p>For example, to create an index directly from a Python script:</p>
<pre tabindex="0"><code class="language-py">import requests&#10;&#10;url = &quot;https://api.cloudflare.com/client/v4/accounts/{}/vectorize/v2/indexes&quot;.format(&quot;your-account-id&quot;)&#10;&#10;headers = {&#10;    &quot;Authorization&quot;: &quot;Bearer &lt;your-api-token&gt;&quot;&#10;}&#10;&#10;body = {&#10;	&quot;name&quot;: &quot;demo-index&quot;,&#10;	&quot;description&quot;: &quot;some index description&quot;,&#10;  &quot;config&quot;: {&#10;    &quot;dimensions&quot;: 1024,&#10;    &quot;metric&quot;: &quot;euclidean&quot;&#10;  },&#10;}&#10;&#10;resp = requests.post(url, headers=headers, json=body)&#10;&#10;print(&#x27;Status Code:&#x27;, resp.status_code)&#10;print(&#x27;Response JSON:&#x27;, resp.json())&#10;</code></pre>
<p>This script should print the response with a status code <code>201</code>, along with a JSON response body indicating the creation of an index with the provided configuration.</p>
<h2 id="dimensions">Dimensions</h2>
<p>Dimensions are determined from the output size of the machine learning (ML) model used to generate them, and are a function of how the model encodes and describes features into a vector embedding.</p>
<p>The number of output dimensions can determine vector search accuracy, search performance (latency), and the overall size of the index. Smaller output dimensions can be faster to search across, which can be useful for user-facing applications. Larger output dimensions can provide more accurate search, especially over larger datasets and/or datasets with substantially similar inputs.</p>
<p>The number of dimensions an index is created for cannot change. Indexes expect to receive dense vectors with the same number of dimensions.</p>
<p>The following table highlights some example embeddings models and their output dimensions:</p>
<table>
<thead>
<tr>
<th>Model / Embeddings API</th>
<th>Output dimensions</th>
<th>Use-case</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers AI - <code>@cf/baai/bge-base-en-v1.5</code></td>
<td>768</td>
<td>Text</td>
</tr>
<tr>
<td>OpenAI - <code>ada-002</code></td>
<td>1536</td>
<td>Text</td>
</tr>
<tr>
<td>Cohere - <code>embed-multilingual-v2.0</code></td>
<td>768</td>
<td>Text</td>
</tr>
<tr>
<td>Google Cloud - <code>multimodalembedding</code></td>
<td>1408</td>
<td>Multi-modal (text, images)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="learn-more-about-workers-ai">Learn more about Workers AI</h3>
@markup("md", "content/.markup/bodies/15284.md")
</aside>
<h2 id="distance-metrics">Distance metrics</h2>
<p>Distance metrics are functions that determine how close vectors are from each other. Vectorize indexes support the following distance metrics:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cosine</code></td>
<td>Distance is measured between <code>-1</code> (most dissimilar) to <code>1</code> (identical). <code>0</code> denotes an orthogonal vector.</td>
</tr>
<tr>
<td><code>euclidean</code></td>
<td>Euclidean (L2) distance. <code>0</code> denotes identical vectors. The larger the positive number, the further the vectors are apart.</td>
</tr>
<tr>
<td><code>dot-product</code></td>
<td>Negative dot product. Larger negative values <em>or</em> smaller positive values denote more similar vectors. A score of <code>-1000</code> is more similar than <code>-500</code>, and a score of <code>15</code> more similar than <code>50</code>.</td>
</tr>
</tbody>
</table>
<p>Determining the similarity between vectors can be subjective based on how the machine-learning model that represents features in the resulting vector embeddings. For example, a score of <code>0.8511</code> when using a <code>cosine</code> metric means that two vectors are close in distance, but whether data they represent is <em>similar</em> is a function of how well the model is able to represent the original content.</p>
<p>When querying vectors, you can specify Vectorize to use either:</p>
<ul>
<li>High-precision scoring, which increases the precision of the query matches scores as well as the accuracy of the query results.</li>
<li>Approximate scoring for faster response times. Using approximate scoring, returned scores will be an approximation of the real distance/similarity between your query and the returned vectors. Refer to <a href="/vectorize/best-practices/query-vectors/#control-over-scoring-precision-and-query-accuracy">Control over scoring precision and query accuracy</a>.</li>
</ul>
<p>Distance metrics cannot be changed after index creation, and that each metric has a different scoring function.</p>
