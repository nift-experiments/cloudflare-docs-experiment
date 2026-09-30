---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/
  description: Query tagged resources using the tag filtering syntax.
  full_title: Filter resources by tag · Cloudflare Resource Tagging docs
  head_html: <title>Filter resources by tag · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="Query tagged resources using the tag filtering syntax."><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/index.md"><meta property="og:title" content="Filter resources by tag · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query tagged resources using the tag filtering syntax."><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/#page","headline":"Filter resources by tag \u00b7 Cloudflare Resource Tagging docs","description":"Query tagged resources using the tag filtering syntax.","url":"https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/how-to/filter-resources/
  schema: 1
---
<p>The <code>GET /accounts/{account_id}/tags/resources</code> endpoint supports tag filtering via the <code>tag</code> query parameter. Multiple <code>tag</code> parameters combine with AND logic. For the full endpoint specification, refer to the <a href="https://developers.cloudflare.com/api/resources/tags/">Resource Tagging API reference</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12769.md")
</aside>
<h2 id="filter-types">Filter types</h2>
<h3 id="key-only-filter">Key-only filter</h3>
<p>Match resources that have a specific tag key, regardless of value.</p>
<pre tabindex="0"><code class="language-bash">&#35; All resources with an &quot;environment&quot; tag (any value)&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h3 id="key-value-filter">Key-value filter</h3>
<p>Match resources where a tag key has a specific value.</p>
<pre tabindex="0"><code class="language-bash">&#35; All resources with environment=production&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h3 id="multiple-values-or">Multiple values (OR)</h3>
<p>Match resources where a tag key has any of the specified values. Separate values with commas.</p>
<pre tabindex="0"><code class="language-bash">&#35; environment=production OR environment=staging&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production,staging&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Maximum of 10 OR values per filter (error code <code>1013</code> if exceeded).</p>
<h3 id="negate-key">Negate key</h3>
<p>Match resources that do <strong>not</strong> have a specific tag key.</p>
<pre tabindex="0"><code class="language-bash">&#35; All resources without an &quot;archived&quot; tag&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=!archived&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h3 id="negate-key-value">Negate key-value</h3>
<p>Match resources where a tag key does <strong>not</strong> have a specific value.</p>
<pre tabindex="0"><code class="language-bash">&#35; All resources where region is NOT us-west-1&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=region!=us-west-1&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h2 id="combining-filters">Combining filters</h2>
<p>Multiple <code>tag</code> parameters combine with AND logic. All conditions must match.</p>
<pre tabindex="0"><code class="language-bash">&#35; Production resources in US regions, excluding archived&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production&amp;tag=region=us-west-1,us-east-1&amp;tag=!archived&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Maximum of 20 tag filters per query (error code <code>1010</code> if exceeded).</p>
<h2 id="discover-available-tags">Discover available tags</h2>
<h3 id="list-all-tag-keys">List all tag keys</h3>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/keys&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h3 id="list-values-for-a-key">List values for a key</h3>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/values/environment&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Optionally filter by resource type:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/values/environment?type=worker&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h2 id="pagination">Pagination</h2>
<p>All list endpoints use cursor-based pagination with a fixed page size of 100 results.</p>
<p>When the response includes a non-null <code>result_info.cursor</code>, pass it as a query parameter to get the next page:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production&amp;cursor=$CURSOR&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>When <code>cursor</code> is <code>null</code>, you have reached the last page. Pagination works seamlessly with tag filters.</p>
