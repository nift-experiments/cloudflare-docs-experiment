---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/
  description: Purge a single cached file by URL.
  full_title: Purge by single-file · Cloudflare Cache (CDN) docs
  head_html: <title>Purge by single-file · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Purge a single cached file by URL."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/index.md"><meta property="og:title" content="Purge by single-file · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Purge a single cached file by URL."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/#page","headline":"Purge by single-file \u00b7 Cloudflare Cache (CDN) docs","description":"Purge a single cached file by URL.","url":"https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/purge-cache/purge-by-single-file/
  schema: 1
---
<p>With purge by single-file, cached resources are instantly removed from the stored assets in your Content Delivery Network (CDN) across all data centers. New requests for the purged asset receive the latest version from your origin web server and add it back to your CDN cache within the specific Cloudflare data center that served the request.</p>
<p>For information on single-file purge rate limits, refer to the <a href="/cache/how-to/purge-cache/#single-file-purge-limits">limits</a> section.</p>
<h2 id="how-to-purge-a-single-file">How to purge a single file</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Custom Purge</strong>. The <strong>Custom Purge</strong> window appears.</li>
<li>Under <strong>Purge by</strong>, select <strong>URL</strong>.</li>
<li>Enter the appropriate value(s) in the text field using the format shown in the example. Be aware that the host part of the URL is not case-sensitive, meaning it will always be converted to lowercase according to RFC standards. However, the path portion is case-sensitive. For example, <code>https://EXAMPLE.com/helloHI</code> would be treated as <code>https://example.com/helloHI</code>.</li>
<li>Perform any additional instructions to complete the form.</li>
<li>Review your entries.</li>
<li>Select <strong>Purge</strong>.</li>
</ol>
<h2 id="limitations-and-alternatives">Limitations and alternatives</h2>
<p>Single-file purge works for most resources, but there are situations where it cannot clear cached content. This section explains when single-file purge does not work and what to use instead.</p>
<h3 id="custom-cache-keys">Custom cache keys</h3>
<p>If you use <a href="/cache/how-to/cache-rules/">Cache Rules</a> to set a <a href="/cache/how-to/cache-keys/">custom cache key</a> that includes headers, cookies, or other request properties, single-file purge via the dashboard will not invalidate the cached resource. This is because the dashboard cannot send those values in a purge request. Custom cache keys that only change how the query string is handled (for example, ignoring the query string) generally work with dashboard single-file purge.</p>
<p><strong>What to do instead:</strong></p>
<ul>
<li><strong>Use the API</strong> to <a href="/api/resources/cache/methods/purge/#purge-cached-content-by-url">purge files by URL</a>, including all headers and cookies that are part of your custom cache key. If any header or cookie is missing from the purge request, Cloudflare treats it as an empty value in the cache key.</li>
<li><strong>Use purge by prefix</strong> (<a href="/cache/how-to/purge-cache/purge_by_prefix/">purge by prefix</a>) to clear all resources under a URL path.</li>
<li><strong>Use purge by tag</strong> (<a href="/cache/how-to/purge-cache/purge-by-tags/">purge by tag</a>) if your resources are tagged.</li>
<li><strong>Use purge everything</strong> (<a href="/cache/how-to/purge-cache/purge-everything/">purge everything</a>) to clear all cached resources for the zone.</li>
</ul>
<h3 id="cache-rules-that-match-on-request-properties">Cache Rules that match on request properties</h3>
<p>Single-file purge may also not work as expected if your Cache Rules match only on <code>GET</code> requests, or match on properties that are not present during a purge. For example, a Cache Rule with the expression <code>(http.host eq &quot;example.com&quot; and http.request.method eq &quot;GET&quot;)</code> will not match during a single-file purge.</p>
<p><strong>What to do instead:</strong></p>
<p>Update your Cache Rule expression to also match on the <code>PURGE</code> method, for example <code>(http.host eq &quot;example.com&quot; and (http.request.method eq &quot;GET&quot; or http.request.method eq &quot;PURGE&quot;))</code>. This allows the rule to apply to both client requests and purge requests.</p>
<p>For rules that match on fields which cannot be evaluated during purge (such as <code>cf.bot_management.score</code>), use <a href="/cache/how-to/purge-cache/purge_by_prefix/">purge by prefix</a>, <a href="/cache/how-to/purge-cache/purge-by-tags/">purge by tag</a>, or <a href="/cache/how-to/purge-cache/purge-everything/">purge everything</a>.</p>
<h3 id="redirect-responses">Redirect responses</h3>
<p>If the URL you want to purge returns a redirect (<code>301</code> or <code>302</code>), single-file purge removes the cached redirect response — not the content at the redirect destination. The resource at the destination URL remains cached.</p>
<p>To clear the destination content, purge the final destination URL directly. You can find it by following the redirect chain to its end:</p>
<pre tabindex="0"><code class="language-bash">curl -Ls -o /dev/null -w &quot;%{url_effective}&#10;&quot; https://example.com/redirecting-path&#10;</code></pre>
<p>This outputs the final URL after following all redirects. Use that URL for your purge request.</p>
<h3 id="resources-with-special-headers">Resources with special headers</h3>
<p>A single-file purge performed through your Cloudflare dashboard does not clear objects that contain any of the following:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin">Origin header</a></li>
<li>Any of these request headers:
<ul>
<li><code>X-Forwarded-Host</code></li>
<li><code>X-Host</code></li>
<li><code>X-Forwarded-Scheme</code></li>
<li><code>X-Original-URL</code></li>
<li><code>X-Rewrite-URL</code></li>
<li><code>Forwarded</code></li>
</ul>
</li>
</ul>
<p>You can purge objects with these characteristics using an API call to <a href="/api/resources/cache/methods/purge/">purge files by URL</a>. In the <code>headers</code> object of the request body, include the header values that match those used in the cached resource's cache key.</p>
<h2 id="additional-notes">Additional notes</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3871.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3870.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3869.md")
</aside>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purging by single-file deletes the resource, resulting in the <code>CF-Cache-Status</code> header being set to <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> for subsequent requests.</p>
