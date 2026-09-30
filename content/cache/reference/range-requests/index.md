---
cp9:
  canonical: https://developers.cloudflare.com/cache/reference/range-requests/
  description: Learn how Cloudflare processes HTTP range requests and what origin responses must include.
  full_title: Range request behavior · Cloudflare Cache (CDN) docs
  head_html: <title>Range request behavior · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Cloudflare processes HTTP range requests and what origin responses must include."><link rel="canonical" href="https://developers.cloudflare.com/cache/reference/range-requests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/reference/range-requests/index.md"><meta property="og:title" content="Range request behavior · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Cloudflare processes HTTP range requests and what origin responses must include."><meta property="og:url" content="https://developers.cloudflare.com/cache/reference/range-requests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/reference/range-requests/#page","headline":"Range request behavior \u00b7 Cloudflare Cache (CDN) docs","description":"Learn how Cloudflare processes HTTP range requests and what origin responses must include.","url":"https://developers.cloudflare.com/cache/reference/range-requests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/reference/range-requests/
  schema: 1
---
<p>Cloudflare can serve HTTP range requests from complete or partial cached files. <a href="/cache/how-to/cache-rules/settings/#origin-range-requests">Origin Range Requests</a> let Cloudflare fetch eligible files from your origin in cache-aligned byte ranges.</p>
<h2 id="request-eligibility">Request eligibility</h2>
<p>Cloudflare uses the partial-file path only for a <code>GET</code> request that is eligible for caching when the request arrives. The origin response may later prove uncacheable. In that case, Cloudflare can still use origin range fetching, but does not store the response bytes.</p>
<p><code>HEAD</code> requests and other methods do not use this path.</p>
<h3 id="head-requests">HEAD requests</h3>
<p>A <code>HEAD</code> request containing <code>Range</code> can return <code>200 OK</code>, <code>206 Partial Content</code>, <code>304 Not Modified</code>, or <code>416 Range Not Satisfiable</code>. A <code>HEAD</code> response never has a body. A <code>206 Partial Content</code> response includes <code>Content-Range</code>. When Cloudflare serves a complete cached file without Origin Range Requests, a matching <code>If-Range</code> validator can preserve a <code>206 Partial Content</code> response, while a mismatch returns <code>200 OK</code>. Cloudflare ignores <code>If-Range</code> for other <code>HEAD</code> request paths.</p>
<h2 id="client-response-behavior">Client response behavior</h2>
<h3 id="requests-without-range">Requests without Range</h3>
<p>A successful, unconditional <code>GET</code> without <code>Range</code> returns the complete file as <code>200 OK</code>. On a cold cache miss, the first origin request also omits <code>Range</code>.</p>
<p>If only part of the file is cached, Cloudflare may request the missing bytes from the origin. The client still receives one complete <code>200 OK</code> response.</p>
<h3 id="one-valid-range">One valid range</h3>
<p>The following requests return <code>206 Partial Content</code> when successful:</p>
<ul>
<li><code>Range: bytes=100-199</code></li>
<li><code>Range: bytes=100-</code></li>
<li><code>Range: bytes=-100</code></li>
</ul>
<p>Cloudflare shortens an end position that exceeds the file size. A suffix range larger than the file returns the complete file as <code>206 Partial Content</code>.</p>
<h3 id="unsatisfiable-ranges">Unsatisfiable ranges</h3>
<p>Cloudflare returns <code>416 Range Not Satisfiable</code> for:</p>
<ul>
<li>An empty range, such as <code>bytes=</code></li>
<li>A zero-length suffix, such as <code>bytes=-0</code></li>
<li>Inverted range bounds</li>
<li>A range starting at or beyond the end of the file</li>
<li>A range against an empty, uncompressed file</li>
<li>Overlapping or out-of-order ranges when Origin Range Requests applies</li>
</ul>
<p>A Cloudflare-generated <code>416 Range Not Satisfiable</code> response has an empty body. It includes <code>Content-Range: bytes */&lt;FILE_SIZE&gt;</code>.</p>
<p>When Cloudflare serves a complete cached file without Origin Range Requests, it ignores overlapping or out-of-order ranges and normally returns the complete file as <code>200 OK</code>.</p>
<h3 id="ignored-range-headers">Ignored Range headers</h3>
<p>Cloudflare processes the request as a non-range request when:</p>
<ul>
<li>The range syntax cannot be parsed</li>
<li>The range unit is not <code>bytes</code></li>
<li>A number is too large to parse</li>
<li>The header contains more than 300 ranges, or exactly 300 ranges when Cloudflare serves a complete cached file without Origin Range Requests</li>
</ul>
<p>This normally returns the complete file as <code>200 OK</code>. Conditional requests can return <code>304 Not Modified</code>, and origin errors still apply.</p>
<h3 id="multiple-ranges">Multiple ranges</h3>
<p>When Origin Range Requests applies, between two and 300 valid, ascending, non-overlapping ranges return a multipart <code>206 Partial Content</code> response. Cloudflare omits individual ranges that cannot be satisfied. The response remains multipart if only one range remains. If no ranges remain, Cloudflare returns <code>416 Range Not Satisfiable</code>.</p>
<p>When Cloudflare serves a complete cached file without Origin Range Requests, one remaining satisfiable range produces a single-range <code>206 Partial Content</code> response.</p>
<h3 id="conditional-requests">Conditional requests</h3>
<p><code>If-None-Match</code> and <code>If-Modified-Since</code> take precedence over <code>Range</code>. They can produce a <code>304 Not Modified</code> response.</p>
<p>Otherwise, an <code>If-Range</code> value that exactly matches the cached <code>ETag</code> or <code>Last-Modified</code> value preserves range behavior. A mismatch causes Cloudflare to ignore <code>Range</code> and use the complete-response path.</p>
<h3 id="decompression">Decompression</h3>
<p>If Cloudflare must decompress a complete encoded response, it ignores <code>Range</code>. Cloudflare sends the complete, uncompressed body as <code>200 OK</code>. This applies to cached responses and responses received from the origin.</p>
<p>A range request for an empty, encoded response returns an empty <code>200 OK</code>, not <code>416 Range Not Satisfiable</code>.</p>
<h2 id="origin-request-behavior">Origin request behavior</h2>
<p>Cloudflare aligns origin range requests to 1 MiB cache boundaries. For example, if a client requests a 1 KiB range, Cloudflare may fetch a 1 MiB range from your origin and return only the requested 1 KiB to the client. Cloudflare may also split one client request into several single-range origin requests. The <code>Range</code> values seen by your origin can differ from the client's header. Consider this behavior when configuring origin logs, request limits, rate limits, or request signing.</p>
<p>Cloudflare adds <code>Accept-Encoding: identity</code> to every origin request generated by Origin Range Requests. This includes a complete-file <code>GET</code> handled by the feature. It does not disable normal compression between Cloudflare and the client.</p>
<h3 id="partial-response-requirements">Partial response requirements</h3>
<p>For Cloudflare to cache an origin <code>206 Partial Content</code> response, the response must meet these requirements:</p>
<table>
<thead>
<tr>
<th>Response field</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Content-Encoding</code></td>
<td>The response must be unencoded.</td>
</tr>
<tr>
<td><code>Content-Range</code></td>
<td>Include a concrete range. Its start must match Cloudflare's request. Its end must match the requested end or the end of the file, whichever comes first. Include the complete file size.</td>
</tr>
<tr>
<td><code>Content-Length</code></td>
<td>Include a numeric value equal to the returned interval length.</td>
</tr>
<tr>
<td><code>Transfer-Encoding</code></td>
<td>Omit this header.</td>
</tr>
<tr>
<td><code>ETag</code></td>
<td>Optional. If present, its presence and exact value must remain consistent across responses for the same cached representation.</td>
</tr>
</tbody>
</table>
<p>The complete file size must also remain consistent across responses. Violations can prevent caching or end responses served to the client early.</p>
<h3 id="origin-responses-that-do-not-honor-range">Origin responses that do not honor Range</h3>
<p>If the origin ignores a Cloudflare-generated <code>Range</code> header and returns a complete <code>200 OK</code>, Cloudflare can use the response. Cloudflare must download the complete file and may then return the requested range to the client.</p>
<p>If the origin returns an encoded <code>206 Partial Content</code> response, Cloudflare does not cache it. Before the client response starts, Cloudflare may send that single response without caching. After the response starts, Cloudflare ends it early, and the client receives fewer bytes than promised.</p>
<p>Other incompatible origin responses during a response assembled from several requests can also end the client response early.</p>
<h2 id="caching-limitations">Caching limitations</h2>
<p>Origin Range Requests do not make an otherwise ineligible request or response cacheable. Cloudflare checks the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">maximum cacheable file size</a> against the complete size from <code>Content-Range</code>. Requesting a small range does not bypass this limit.</p>
<p>Origin Range Requests are not supported with <a href="/cache/advanced-configuration/cache-reserve/#limits">Cache Reserve</a>.</p>
