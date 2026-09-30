---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/
  description: New updates and improvements at Cloudflare.
  full_title: New functions for array and map operations · Changelog
  head_html: <title>New functions for array and map operations · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New functions for array and map operations · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/#page","headline":"New functions for array and map operations \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-20-array-map-functions/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">New functions for array and map operations</h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><h4 id="new-functions-for-array-and-map-operations">New functions for array and map operations</h4>
<p>Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.</p>
<hr />
<h4 id="new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>split(source, delimiter)</code></td>
<td>Splits a string into an array of strings using the specified delimiter.</td>
</tr>
<tr>
<td><code>join(array, delimiter)</code></td>
<td>Joins an array of strings into a single string using the specified delimiter.</td>
</tr>
<tr>
<td><code>has_key(map, key)</code></td>
<td>Returns <code>true</code> if the specified key exists in the map.</td>
</tr>
<tr>
<td><code>has_value(map, value)</code></td>
<td>Returns <code>true</code> if the specified value exists in the map.</td>
</tr>
</tbody>
</table>
<hr />
<h4 id="example-use-cases">Example use cases</h4>
<p><strong>Check if a country code exists in a header list:</strong></p>
<pre tabindex="0"><code class="language-txt">has_value(split(http.response.headers[&quot;x-allow-country&quot;][0], &quot;,&quot;), ip.src.country)&#10;</code></pre>
<p><strong>Check if a specific header key exists:</strong></p>
<pre tabindex="0"><code class="language-txt">has_key(http.request.headers, &quot;x-custom-header&quot;)&#10;</code></pre>
<p><strong>Join array values for logging or comparison:</strong></p>
<pre tabindex="0"><code class="language-txt">join(http.request.headers.names, &quot;, &quot;)&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>
</div></article></div>
