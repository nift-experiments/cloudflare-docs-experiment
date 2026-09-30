---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/
  description: New updates and improvements at Cloudflare.
  full_title: Retry-After HTTP header for retryable 1xxx errors · Changelog
  head_html: <title>Retry-After HTTP header for retryable 1xxx errors · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Retry-After HTTP header for retryable 1xxx errors · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/#page","headline":"Retry-After HTTP header for retryable 1xxx errors \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 12, 2026</time><h2 id="post-title">Retry-After HTTP header for retryable 1xxx errors</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare-generated 1xxx error responses now include a standard <code>Retry-After</code> HTTP header when the error is retryable. Agents and HTTP clients can read the recommended wait time from response headers alone — no body parsing required.</p>
<h4 id="changes">Changes</h4>
<p>Seven retryable error codes now emit <code>Retry-After</code>:</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Retry-After (seconds)</th>
<th>Error name</th>
</tr>
</thead>
<tbody>
<tr>
<td>1004</td>
<td>120</td>
<td>DNS resolution error</td>
</tr>
<tr>
<td>1005</td>
<td>120</td>
<td>Banned zone</td>
</tr>
<tr>
<td>1015</td>
<td>30</td>
<td>Rate limited</td>
</tr>
<tr>
<td>1033</td>
<td>120</td>
<td>Argo Tunnel error</td>
</tr>
<tr>
<td>1038</td>
<td>60</td>
<td>HTTP headers limit exceeded</td>
</tr>
<tr>
<td>1200</td>
<td>60</td>
<td>Cache connection limit</td>
</tr>
<tr>
<td>1205</td>
<td>5</td>
<td>Too many redirects</td>
</tr>
</tbody>
</table>
<p>The header value matches the existing <code>retry_after</code> body field in JSON and Markdown responses.</p>
<p>If a WAF rate limiting rule has already set a dynamic <code>Retry-After</code> value on the response, that value takes precedence.</p>
<h4 id="availability">Availability</h4>
<p>Available for all zones on all plans.</p>
<h4 id="verify">Verify</h4>
<p>Check for the header on any retryable error:</p>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | grep -i retry-after&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9110#section-10.2.3">RFC 9110 section 10.2.3 - Retry-After</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>
</div></article></div>
