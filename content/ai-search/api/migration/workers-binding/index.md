---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/migration/workers-binding/
  description: Upgrade from the legacy env.AI.autorag() binding to the new AI Search Workers bindings.
  full_title: Workers binding migration · Cloudflare AI Search docs
  head_html: <title>Workers binding migration · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Upgrade from the legacy env.AI.autorag() binding to the new AI Search Workers bindings."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/migration/workers-binding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/migration/workers-binding/index.md"><meta property="og:title" content="Workers binding migration · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upgrade from the legacy env.AI.autorag() binding to the new AI Search Workers bindings."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/migration/workers-binding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/migration/workers-binding/#page","headline":"Workers binding migration \u00b7 Cloudflare AI Search docs","description":"Upgrade from the legacy env.AI.autorag() binding to the new AI Search Workers bindings.","url":"https://developers.cloudflare.com/ai-search/api/migration/workers-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/migration/workers-binding/
  schema: 1
---
<p>The <a href="/ai-search/api/migration/workers-binding-legacy/"><code>env.AI.autorag()</code> binding</a> is the legacy API for AI Search. It will continue to work, but all new features and improvements are only available through the new AI Search bindings.</p>
<h2 id="what-changed">What changed</h2>
<p>Here is a summary of the key differences between the legacy and new bindings:</p>
<table>
<thead>
<tr>
<th></th>
<th>Legacy</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Wrangler config</strong></td>
<td><code>ai</code> binding</td>
<td><code>ai_search</code> or <code>ai_search_namespaces</code> binding</td>
</tr>
<tr>
<td><strong>Access pattern</strong></td>
<td><code>env.AI.autorag(&quot;name&quot;)</code></td>
<td><code>env.MY_INSTANCE</code> or <code>env.AI_SEARCH.get(&quot;name&quot;)</code></td>
</tr>
<tr>
<td><strong>Search format</strong></td>
<td><code>query</code> string</td>
<td><code>messages</code> array or <code>query</code> string</td>
</tr>
<tr>
<td><strong>Response format</strong></td>
<td><code>data</code> array</td>
<td><code>chunks</code> array</td>
</tr>
</tbody>
</table>
<h2 id="ai-search-bindings">AI Search bindings</h2>
<p>AI Search provides two new bindings:</p>
<p><strong>Instance binding (<code>ai_search</code>)</strong> binds directly to a single instance. This is the simplest migration path from <code>env.AI.autorag()</code>.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;MY_SEARCH&quot;,&#10;			&quot;instance_name&quot;: &quot;my-instance&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p><strong>Namespace binding (<code>ai_search_namespaces</code>)</strong> gives you access to all instances within a namespace. Use this if you need dynamic instance management, cross-instance search, or the Items API.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search_namespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;AI_SEARCH&quot;,&#10;			&quot;namespace&quot;: &quot;default&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>For more details on the difference, refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h2 id="requirements">Requirements</h2>
<p>The new bindings require the following minimum package versions for TypeScript types and local development support.</p>
<table>
<thead>
<tr>
<th>Package</th>
<th>Minimum version</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/workers-types</code></td>
<td><code>4.20260304.0</code></td>
</tr>
<tr>
<td><code>wrangler</code></td>
<td><code>4.68.1</code></td>
</tr>
</tbody>
</table>
<h2 id="step-1-update-wrangler-configuration">Step 1: Update Wrangler configuration</h2>
<p>Existing instances are in the default namespace. For a simple upgrade path, use the instance binding. For the namespace binding, refer to <a href="#ai-search-bindings">AI Search bindings</a>.</p>
<p><strong>Before:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3067.md")
</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3068.md")
</div>
<h2 id="step-2-update-the-type-definition">Step 2: Update the type definition</h2>
<p>Update the <code>Env</code> interface to use the new binding type.</p>
<p><strong>Before:</strong></p>
<pre tabindex="0"><code class="language-ts">export interface Env {&#10;	AI: Ai;&#10;}&#10;</code></pre>
<p><strong>After:</strong></p>
<pre tabindex="0"><code class="language-ts">export interface Env {&#10;	MY_INSTANCE: AiSearchInstance;&#10;}&#10;</code></pre>
<h2 id="step-3-update-search-calls">Step 3: Update search calls</h2>
<p>Replace <code>env.AI.autorag()</code> calls with the new binding.</p>
<p><strong>Before:</strong></p>
<pre tabindex="0"><code class="language-ts">const result = await env.AI.autorag(&quot;my-instance&quot;).search({&#10;	query: &quot;What is Cloudflare?&quot;,&#10;});&#10;</code></pre>
<p><strong>After:</strong></p>
<pre tabindex="0"><code class="language-ts">const result = await env.MY_INSTANCE.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;</code></pre>
<h2 id="step-4-update-response-handling">Step 4: Update response handling</h2>
<p>The response shape changed from a <code>data</code> array to a <code>chunks</code> array.</p>
<h3 id="field-mapping">Field mapping</h3>
<table>
<thead>
<tr>
<th>Old field</th>
<th>New field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>data[]</code></td>
<td><code>chunks[]</code></td>
</tr>
<tr>
<td><code>data[].file_id</code></td>
<td><code>chunks[].id</code></td>
</tr>
<tr>
<td><code>data[].filename</code></td>
<td><code>chunks[].item.key</code></td>
</tr>
<tr>
<td><code>data[].score</code></td>
<td><code>chunks[].score</code></td>
</tr>
<tr>
<td><code>data[].content[].text</code></td>
<td><code>chunks[].text</code></td>
</tr>
<tr>
<td><code>data[].attributes.modified_date</code></td>
<td><code>chunks[].item.timestamp</code></td>
</tr>
</tbody>
</table>
<h2 id="streaming-behavior-changes">Streaming behavior changes</h2>
<p>In the legacy binding, streaming with <code>env.AI.autorag().aiSearch({ stream: true })</code> only returned the streamed response without the retrieved chunks.</p>
<p>The new binding sends the retrieved chunks first as a <code>chunks</code> event, followed by the streamed response. This allows you to display source chunks immediately while streaming the generated response.</p>
<h2 id="filter-format-changes">Filter format changes</h2>
<p>The new binding uses Vectorize-style metadata filtering. Filters are now passed inside <code>ai_search_options.retrieval.filters</code>.</p>
<table>
<thead>
<tr>
<th>Old format</th>
<th>New format</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eq</code></td>
<td><code>$eq</code> (or implicit)</td>
</tr>
<tr>
<td><code>ne</code></td>
<td><code>$ne</code></td>
</tr>
<tr>
<td><code>gt</code></td>
<td><code>$gt</code></td>
</tr>
<tr>
<td><code>gte</code></td>
<td><code>$gte</code></td>
</tr>
<tr>
<td><code>lt</code></td>
<td><code>$lt</code></td>
</tr>
<tr>
<td><code>lte</code></td>
<td><code>$lte</code></td>
</tr>
<tr>
<td></td>
<td><code>$in</code> (new)</td>
</tr>
<tr>
<td></td>
<td><code>$nin</code> (new)</td>
</tr>
</tbody>
</table>
<h3 id="examples">Examples</h3>
<h4 id="simple-filter">Simple filter</h4>
<p>Filter by a single metadata field using implicit equality:</p>
<p><strong>Before:</strong></p>
<pre tabindex="0"><code class="language-ts">const result = await env.AI.autorag(&quot;my-instance&quot;).search({&#10;	query: &quot;What is Cloudflare?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;folder&quot;,&#10;		value: &quot;customer-a/&quot;,&#10;	},&#10;});&#10;</code></pre>
<p><strong>After:</strong></p>
<pre tabindex="0"><code class="language-ts">const result = await env.MY_INSTANCE.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			filters: { folder: &quot;customer-a/&quot; },&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h4 id="compound-filter-and">Compound filter (AND)</h4>
<p>Combine multiple conditions where all must match:</p>
<p><strong>Before:</strong></p>
<pre tabindex="0"><code class="language-ts">const result = await env.AI.autorag(&quot;my-instance&quot;).search({&#10;	query: &quot;What is Cloudflare?&quot;,&#10;	filters: {&#10;		type: &quot;and&quot;,&#10;		filters: [&#10;			{ type: &quot;eq&quot;, key: &quot;folder&quot;, value: &quot;customer-a/&quot; },&#10;			{ type: &quot;gte&quot;, key: &quot;timestamp&quot;, value: &quot;1735689600000&quot; },&#10;		],&#10;	},&#10;});&#10;</code></pre>
<p><strong>After:</strong></p>
<pre tabindex="0"><code class="language-ts">const result = await env.MY_INSTANCE.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			filters: {&#10;				folder: &quot;customer-a/&quot;,&#10;				timestamp: { $gte: 1735689600 },&#10;			},&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h2 id="backwards-compatibility">Backwards compatibility</h2>
<p>The <code>env.AI.autorag()</code> binding will continue to work indefinitely. You do not need to migrate immediately.</p>
<p>For the legacy API reference, refer to <a href="/ai-search/api/migration/workers-binding-legacy/">Workers binding (legacy)</a>.</p>
