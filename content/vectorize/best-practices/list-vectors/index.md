---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/best-practices/list-vectors/
  description: Enumerate vector identifiers in a Vectorize index using paginated list operations.
  full_title: List vectors · Cloudflare Vectorize docs
  head_html: <title>List vectors · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Enumerate vector identifiers in a Vectorize index using paginated list operations."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/best-practices/list-vectors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/best-practices/list-vectors/index.md"><meta property="og:title" content="List vectors · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enumerate vector identifiers in a Vectorize index using paginated list operations."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/best-practices/list-vectors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/best-practices/list-vectors/#page","headline":"List vectors \u00b7 Cloudflare Vectorize docs","description":"Enumerate vector identifiers in a Vectorize index using paginated list operations.","url":"https://developers.cloudflare.com/vectorize/best-practices/list-vectors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/best-practices/list-vectors/
  schema: 1
---
<p>The list-vectors operation allows you to enumerate all vector identifiers in a Vectorize index using paginated requests. This guide covers best practices for efficiently using this operation.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="python-sdk-availability">Python SDK availability</h3>
@markup("md", "content/.markup/bodies/15280.md")
</aside>
<h2 id="when-to-use-list-vectors">When to use list-vectors</h2>
<p>Use list-vectors for:</p>
<ul>
<li><strong>Bulk operations</strong>: To process all vectors in an index</li>
<li><strong>Auditing</strong>: To verify the contents of your index or generate reports</li>
<li><strong>Data migration</strong>: To move vectors between indexes or systems</li>
<li><strong>Cleanup operations</strong>: To identify and remove outdated vectors</li>
</ul>
<h2 id="pagination-behavior">Pagination behavior</h2>
<p>The list-vectors operation uses cursor-based pagination with important consistency guarantees:</p>
<h3 id="snapshot-consistency">Snapshot consistency</h3>
<p>Vector identifiers returned belong to the index snapshot captured at the time of the first list-vectors request. This ensures consistent pagination even when the index is being modified during iteration:</p>
<ul>
<li><strong>New vectors</strong>: Vectors inserted after the initial request will not appear in subsequent paginated results</li>
<li><strong>Deleted vectors</strong>: Vectors deleted after the initial request will continue to appear in the remaining responses until pagination is complete</li>
</ul>
<h3 id="starting-a-new-iteration">Starting a new iteration</h3>
<p>To see recently added or removed vectors, you must start a new list-vectors request sequence (without a cursor). This captures a fresh snapshot of the index.</p>
<h3 id="response-structure">Response structure</h3>
<p>Each response includes:</p>
<ul>
<li><code>count</code>: Number of vectors returned in this response</li>
<li><code>totalCount</code>: Total number of vectors in the index</li>
<li><code>isTruncated</code>: Whether there are more vectors available</li>
<li><code>nextCursor</code>: Cursor for the next page (null if no more results)</li>
<li><code>cursorExpirationTimestamp</code>: Timestamp of when the cursor expires</li>
<li><code>vectors</code>: Array of vector identifiers</li>
</ul>
<h3 id="cursor-expiration">Cursor expiration</h3>
<p>Cursors have an expiration timestamp. If a cursor expires, you'll need to start a new list-vectors request sequence to continue pagination.</p>
<h2 id="performance-considerations">Performance considerations</h2>
<p>Take care to have sufficient gap between consecutive requests to avoid hitting rate-limits.</p>
<h2 id="example-workflow">Example workflow</h2>
<p>Here's a typical pattern for processing all vectors in an index:</p>
<pre tabindex="0"><code class="language-sh">&#35; Start iteration&#10;wrangler vectorize list-vectors my-index --count=1000&#10;&#10;&#35; Continue with cursor from response&#10;wrangler vectorize list-vectors my-index --count=1000 --cursor=&quot;&lt;cursor-from-response&gt;&quot;&#10;&#10;&#35; Repeat until no more results&#10;</code></pre>
