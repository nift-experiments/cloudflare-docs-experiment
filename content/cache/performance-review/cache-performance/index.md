---
cp9:
  canonical: https://developers.cloudflare.com/cache/performance-review/cache-performance/
  description: Measure and improve cache performance for your site.
  full_title: Cache performance · Cloudflare Cache (CDN) docs
  head_html: <title>Cache performance · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Measure and improve cache performance for your site."><link rel="canonical" href="https://developers.cloudflare.com/cache/performance-review/cache-performance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/performance-review/cache-performance/index.md"><meta property="og:title" content="Cache performance · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Measure and improve cache performance for your site."><meta property="og:url" content="https://developers.cloudflare.com/cache/performance-review/cache-performance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/performance-review/cache-performance/#page","headline":"Cache performance \u00b7 Cloudflare Cache (CDN) docs","description":"Measure and improve cache performance for your site.","url":"https://developers.cloudflare.com/cache/performance-review/cache-performance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/performance-review/cache-performance/
  schema: 1
---
<h2 id="optimize-cache-ratios">Optimize cache ratios</h2>
<p>Your cache ratio measures how often Cloudflare serves content from cache instead of contacting your origin server. A higher ratio means faster responses for visitors and less traffic to your origin.</p>
<p>Depending on the <a href="/cache/concepts/cache-responses/">cache status</a> you receive, you can make modifications to improve your cache ratio.</p>
<ul>
<li><strong>Dynamic</strong>: The resource was not eligible for caching. This is the default response for many file types including HTML. To cache additional content, refer to <a href="/cache/how-to/cache-rules/">Cache Rules</a>.</li>
<li><strong>Revalidated</strong>: The resource was in cache but Cloudflare confirmed with your origin that it was still current before serving it. To address an atypical quantity of revalidated content, consider <a href="/cache/how-to/cache-rules/settings/#edge-ttl">increasing your Edge Cache TTLs</a> (how long Cloudflare considers cached content fresh before checking your origin).</li>
<li><strong>Expired</strong>: The cached resource's TTL elapsed before it was requested again. Consider <a href="/cache/how-to/cache-rules/settings/#edge-ttl">extending Edge Cache TTLs</a> for these resources via a Cache Rule, or configure your origin to return <a href="/cache/concepts/cache-control/">revalidation headers</a> (<code>Last-Modified</code> or <code>ETag</code>) so Cloudflare can confirm content is still current without downloading it again.</li>
<li><strong>Miss</strong>: The resource was not found in cache and was served from your origin. Although tricky to optimize, there are a few potential remedies:
<ul>
<li><a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache</a> to check an upper-tier Cloudflare data center before contacting your origin server.</li>
<li><a href="/cache/how-to/cache-rules/examples/custom-cache-key/">Create a custom cache key</a> so that multiple URLs match the same cached resource, for example by ignoring the query string.</li>
</ul>
</li>
</ul>
<h2 id="troubleshoot-cache-performance-with-example-reports">Troubleshoot cache performance with example reports</h2>
<p>Use <a href="/cache/performance-review/cache-analytics/">Cache Analytics</a> to identify cache performance issues. The following examples show how to filter for common problems and resolve them.</p>
<ul>
<li>
<p>Not caching HTML.</p>
<ul>
<li>Identify the issue: Select <strong>Add filter</strong> and select <strong>Cache status equals Dynamic</strong>.</li>
<li>Resolution: Set a Cloudflare Cache Rule to <a href="/cache/how-to/cache-rules/examples/cache-everything/">cache dynamic content</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3800.md")
</aside>
<ul>
<li>
<p>Short cache expiration TTL.</p>
<ul>
<li>Identify the issue: Select <strong>Add filter</strong> and select <strong>Cache status equals Revalidated</strong>.</li>
<li>Resolution: <a href="/cache/how-to/cache-rules/examples/edge-ttl/">Increase Cloudflare's Edge Cache TTL via a Cache Rule</a>.</li>
</ul>
</li>
<li>
<p>Need to enable Tiered Cache or custom cache key.</p>
<ul>
<li>Identify the issue: Select <strong>Add filter</strong> and select <strong>Cache status equals Miss</strong>.</li>
<li>Resolution: <a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache</a> or <a href="/cache/how-to/cache-rules/examples/custom-cache-key/">create a custom cache key</a>.</li>
</ul>
</li>
</ul>
