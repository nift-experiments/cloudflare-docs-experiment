---
cp9:
  canonical: https://developers.cloudflare.com/cache/reference/etag-headers/
  description: How ETag headers work with Cloudflare caching.
  full_title: Using ETag Headers with Cloudflare · Cloudflare Cache (CDN) docs
  head_html: <title>Using ETag Headers with Cloudflare · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="How ETag headers work with Cloudflare caching."><link rel="canonical" href="https://developers.cloudflare.com/cache/reference/etag-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/reference/etag-headers/index.md"><meta property="og:title" content="Using ETag Headers with Cloudflare · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How ETag headers work with Cloudflare caching."><meta property="og:url" content="https://developers.cloudflare.com/cache/reference/etag-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/reference/etag-headers/#page","headline":"Using ETag Headers with Cloudflare \u00b7 Cloudflare Cache (CDN) docs","description":"How ETag headers work with Cloudflare caching.","url":"https://developers.cloudflare.com/cache/reference/etag-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/reference/etag-headers/
  schema: 1
---
<p>ETag headers identify whether the version of a resource cached in the browser is the same as the resource at the origin web server. A visitor's browser stores ETags. When a visitor revisits a site, the browser compares each ETag to the one it stored. Matching values cause a <code>304 Not-Modified HTTP</code> response that indicates the cached resource version is current. Cloudflare supports both strong and weak ETags configured at your origin web server.</p>
<h2 id="weak-etags">Weak ETags</h2>
<p>Weak ETag headers indicate a cached resource is semantically equivalent to the version on the web server but not necessarily byte-for-byte identical.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3798.md")
</aside>
<h2 id="strong-etags">Strong ETags</h2>
<p>Strong ETag headers ensure the resource in browser cache and on the web server are byte-for-byte identical. Use <a href="/cache/how-to/cache-rules/">Cache Rules</a> to enable strong ETag headers.</p>
<h3 id="behavior-with-respect-strong-etags-enabled">Behavior with Respect Strong ETags enabled</h3>
<p>When you enable <strong>Respect Strong ETags</strong> in a cache rule, Cloudflare will use strong ETag header validation to ensure that resources in the Cloudflare cache and on the origin server are byte-for-byte identical.</p>
<p>However, in some situations Cloudflare will convert strong ETags to weak ETags. For example, given the following conditions:</p>
<ul>
<li><strong>Respect Strong ETags</strong> is enabled</li>
<li><a href="/speed/optimization/content/compression/">Brotli compression</a> is enabled</li>
<li>The origin server's response includes an <code>etag: &quot;foobar&quot;</code> strong ETag header</li>
</ul>
<p>The Cloudflare network will take the following actions, depending on the visitor's <code>accept-encoding</code> header and the compression used in the origin server's response:</p>
<table-wrap>
<table>
<thead>
<tr>
<th><code>accept-encoding</code><br/>header from visitor</th>
<th>Compression used in origin server response</th>
<th>Cloudflare actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gzip, br</code></td>
<td>GZIP</td>
<td>Return GZIP-compressed response to visitor with strong ETag header: <code>etag: &quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip, br</code></td>
<td>Brotli</td>
<td>Return Brotli-compressed response to visitor with strong ETag header: <code>etag: &quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>br</code></td>
<td>GZIP</td>
<td>Decompress GZIP and return uncompressed response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip</code></td>
<td>Brotli</td>
<td>Decompress Brotli and return uncompressed response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip</code></td>
<td>(none)</td>
<td>Return uncompressed response to visitor with strong ETag header: <code>etag: &quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip, br, zstd</code></td>
<td>Zstandard</td>
<td>Return zstd-compressed response to visitor with strong ETag header: <code>etag: &quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip, br</code></td>
<td>Zstandard</td>
<td>Decompress zstd and return br response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>zstd</code></td>
<td>Brotli/GZIP</td>
<td>Decompress zstd and return zstd response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
</tbody>
</table>
</table-wrap>
<p>Enabling <strong>Respect Strong ETags</strong> in Cloudflare automatically disables Rocket Loader, Email Obfuscation, and Automatic HTTPS Rewrites.</p>
<h3 id="behavior-with-respect-strong-etags-disabled">Behavior with Respect Strong ETags disabled</h3>
<p>When <strong>Respect Strong ETags</strong> is disabled, Cloudflare will preserve strong ETag headers set by the origin web server if all the following conditions apply:</p>
<ul>
<li>The origin server sends a response compressed using GZIP or Brotli, or an uncompressed response.</li>
<li>If the origin server sends a compressed response, the visitor accepts the same compression (GZIP, Brotli), according to the <code>accept-encoding</code> header.</li>
<li><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a> and <a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Obfuscation</a> features are disabled.</li>
</ul>
<p>In all other situations, Cloudflare will either convert strong ETag headers to weak ETag headers or remove the strong ETag. For example, given the following conditions:</p>
<ul>
<li><strong>Respect Strong ETags</strong> is disabled</li>
<li><a href="/speed/optimization/content/compression/">Brotli compression</a> is enabled</li>
<li>The origin server's response includes an <code>etag: &quot;foobar&quot;</code> strong ETag header</li>
</ul>
<p>The Cloudflare network will take the following actions, depending on the visitor's <code>accept-encoding</code> header and the compression used in the origin server's response:</p>
<table-wrap>
<table>
<thead>
<tr>
<th><code>accept-encoding</code><br/>header from visitor</th>
<th>Compression used in origin server response</th>
<th>Cloudflare actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gzip, br</code></td>
<td>GZIP</td>
<td>Decompress GZIP and return Brotli-compressed response to visitor (since Brotli compression is enabled) with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip, br</code></td>
<td>Brotli</td>
<td>Return Brotli-compressed response to visitor with strong ETag header: <code>etag: &quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>br</code></td>
<td>GZIP</td>
<td>Decompress GZIP and return Brotli-compressed response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip</code></td>
<td>Brotli</td>
<td>Decompress Brotli and return GZIP-compressed response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip</code></td>
<td>(none)</td>
<td>Compress origin response using GZIP and return it to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip, br, zstd</code></td>
<td>Zstandard</td>
<td>Return zstd-compressed response to visitor with strong ETag header: <code>etag: &quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>gzip, br</code></td>
<td>Zstandard</td>
<td>Decompress zstd and return uncompressed response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
<tr>
<td><code>zstd</code></td>
<td>Brotli</td>
<td>Decompress zstd and return uncompressed response to visitor with weak ETag header: <code>etag: W/&quot;foobar&quot;</code>.</td>
</tr>
</tbody>
</table>
</table-wrap>
<p>Refer to <a href="/speed/optimization/content/compression/">Content compression</a> for more information.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>You must set the value in a strong ETag header using double quotes (for example, <code>etag: &quot;foobar&quot;</code>). If you use an incorrect format, Cloudflare will remove the ETag header instead of converting it to a weak ETag. </p>
</li>
<li>
<p>If a resource is cacheable and there is a cache miss, Cloudflare does not send ETag headers to the origin server. This is because Cloudflare requires the full response body to fill its cache.</p>
</li>
<li>
<p>If your origin (or R2) applies compression based on <code>accept-encoding</code>, the first compression type will be cached. Consider whether strong ETags fit your use case, or use cache key rules to handle different compression types.</p>
</li>
</ul>
