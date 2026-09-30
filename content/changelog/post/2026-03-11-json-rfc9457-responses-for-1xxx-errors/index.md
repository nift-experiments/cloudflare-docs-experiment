---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/
  description: New updates and improvements at Cloudflare.
  full_title: JSON responses and RFC 9457 support for Cloudflare 1xxx errors · Changelog
  head_html: <title>JSON responses and RFC 9457 support for Cloudflare 1xxx errors · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="JSON responses and RFC 9457 support for Cloudflare 1xxx errors · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/#page","headline":"JSON responses and RFC 9457 support for Cloudflare 1xxx errors \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2026</time><h2 id="post-title">JSON responses and RFC 9457 support for Cloudflare 1xxx errors</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare-generated 1xxx errors now return structured JSON when clients send <code>Accept: application/json</code> or <code>Accept: application/problem+json</code>. JSON responses follow <a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 (Problem Details for HTTP APIs)</a>, so any HTTP client that understands Problem Details can parse the base members without Cloudflare-specific code.</p>
<h4 id="breaking-change">Breaking change</h4>
<p>The Markdown frontmatter field <code>http_status</code> has been renamed to <code>status</code>. Agents consuming Markdown frontmatter should update parsers accordingly.</p>
<h4 id="changes">Changes</h4>
<p><strong>JSON format.</strong> Clients sending <code>Accept: application/json</code> or <code>Accept: application/problem+json</code> now receive a structured JSON object with the same operational fields as Markdown frontmatter, plus RFC 9457 standard members.</p>
<p><strong>RFC 9457 standard members (JSON only):</strong></p>
<ul>
<li><code>type</code> — URI pointing to Cloudflare documentation for the specific error code</li>
<li><code>status</code> — HTTP status code (matching the response status)</li>
<li><code>title</code> — short, human-readable summary</li>
<li><code>detail</code> — human-readable explanation specific to this occurrence</li>
<li><code>instance</code> — Ray ID identifying this specific error occurrence</li>
</ul>
<p><strong>Field renames:</strong></p>
<ul>
<li><code>http_status</code> -&gt; <code>status</code> (JSON and Markdown)</li>
<li><code>what_happened</code> -&gt; <code>detail</code> (JSON only — Markdown prose sections are unchanged)</li>
</ul>
<p><strong>Content-Type mirroring.</strong> Clients sending <code>Accept: application/problem+json</code> receive <code>Content-Type: application/problem+json; charset=utf-8</code> back; <code>Accept: application/json</code> receives <code>application/json; charset=utf-8</code>. Same body in both cases.</p>
<h4 id="negotiation-behavior">Negotiation behavior</h4>
<table>
<thead>
<tr>
<th>Request header sent</th>
<th>Response format</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Accept: application/json</code></td>
<td>JSON (<code>application/json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/problem+json</code></td>
<td>JSON (<code>application/problem+json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/json, text/markdown;q=0.9</code></td>
<td>JSON</td>
</tr>
<tr>
<td><code>Accept: text/markdown</code></td>
<td>Markdown</td>
</tr>
<tr>
<td><code>Accept: text/markdown, application/json</code></td>
<td>Markdown (equal <code>q</code>, first-listed wins)</td>
</tr>
<tr>
<td><code>Accept: */*</code></td>
<td>HTML (default)</td>
</tr>
</tbody>
</table>
<h4 id="availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="get-started">Get started</h4>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -H &quot;Accept: application/problem+json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>
</div></article></div>
