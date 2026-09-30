---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/
  description: Filter AI Search results by metadata attributes at query time.
  full_title: Filtering · Cloudflare AI Search docs
  head_html: <title>Filtering · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Filter AI Search results by metadata attributes at query time."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/index.md"><meta property="og:title" content="Filtering · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Filter AI Search results by metadata attributes at query time."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/#page","headline":"Filtering \u00b7 Cloudflare AI Search docs","description":"Filter AI Search results by metadata attributes at query time.","url":"https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/retrieval/filtering/
  schema: 1
---
<p>Metadata filtering narrows down search results based on metadata, so only relevant content is retrieved. The filter is applied before retrieval, so you only query the documents that matter.</p>
<p>Filtering uses the metadata attributes extracted during indexing. To define custom attributes or use the built-in metadata attributes, refer to <a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a>.</p>
<p>AI Search can store string values longer than the filterable prefix. Filters only match the first 64 UTF-8 bytes of each indexed string. Vectorize can store string arrays, but does not currently index or filter them.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3077.md")
</aside>
<p>Here is an example of metadata filtering using the <a href="/ai-search/api/search/workers-binding/">Workers binding</a>:</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			filters: {&#10;				folder: &quot;docs/getting-started/&quot;,&#10;				timestamp: { $gte: 1735689600 },&#10;			},&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h2 id="filter-syntax">Filter syntax</h2>
<p>Filters are JSON objects where keys are metadata attribute names and values specify the filter condition.</p>
<h3 id="supported-operators">Supported operators</h3>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>$eq</code></td>
<td>Equals</td>
</tr>
<tr>
<td><code>$ne</code></td>
<td>Not equals</td>
</tr>
<tr>
<td><code>$in</code></td>
<td>Matches a stored scalar against any candidate scalar value</td>
</tr>
<tr>
<td><code>$nin</code></td>
<td>Excludes a stored scalar matching any candidate scalar value</td>
</tr>
<tr>
<td><code>$lt</code></td>
<td>Less than</td>
</tr>
<tr>
<td><code>$lte</code></td>
<td>Less than or equal to</td>
</tr>
<tr>
<td><code>$gt</code></td>
<td>Greater than</td>
</tr>
<tr>
<td><code>$gte</code></td>
<td>Greater than or equal to</td>
</tr>
</tbody>
</table>
<h3 id="implicit-eq">Implicit <code>$eq</code></h3>
<p>When you provide a direct value without an operator, it is treated as an equality check:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: { &quot;folder&quot;: &quot;docs/getting-started/&quot; }&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>This is equivalent to:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: { &quot;folder&quot;: { &quot;$eq&quot;: &quot;docs/getting-started/&quot; } }&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="range-queries">Range queries</h3>
<p>Combine upper and lower bound operators to filter by ranges:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: { &quot;timestamp&quot;: { &quot;$gte&quot;: 1735689600, &quot;$lt&quot;: 1735900000 } }&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="multiple-conditions-implicit-and">Multiple conditions (implicit AND)</h3>
<p>When you specify multiple keys, all conditions must match:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: {&#10;				&quot;folder&quot;: &quot;docs/getting-started/&quot;,&#10;				&quot;timestamp&quot;: { &quot;$gte&quot;: 1735689600 }&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="in-operator"><code>$in</code> operator</h3>
<p>Match a stored scalar field against any value in the candidate array. <code>$in</code> does not search inside stored arrays:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: { &quot;folder&quot;: { &quot;$in&quot;: [&quot;docs/guides/&quot;, &quot;docs/tutorials/&quot;] } }&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="starts-with-filter-for-folders">&quot;Starts with&quot; filter for folders</h2>
<p>Use range queries to filter for all files within a folder and its subfolders.</p>
<p>For example, consider this file structure:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/3078.md")&#10;&#10;&#10;</pre>
<p>Using <code>{ &quot;folder&quot;: &quot;docs/&quot; }</code> only matches files directly in that folder (like <code>guide.pdf</code>), not files in subfolders.</p>
<p>To match all files starting with <code>docs/</code>, use a range query:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: { &quot;folder&quot;: { &quot;$gte&quot;: &quot;docs/&quot;, &quot;$lt&quot;: &quot;docs0&quot; } }&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>This works because:</p>
<ul>
<li><code>$gte</code> includes all paths starting with <code>docs/</code></li>
<li><code>$lt</code> with <code>docs0</code> excludes paths that do not start with <code>docs/</code> (since <code>0</code> comes after <code>/</code> in ASCII)</li>
</ul>
