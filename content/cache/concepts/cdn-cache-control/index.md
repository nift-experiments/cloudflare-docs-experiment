---
cp9:
  canonical: https://developers.cloudflare.com/cache/concepts/cdn-cache-control/
  description: Use CDN-Cache-Control headers to control Cloudflare cache independently.
  full_title: CDN-Cache-Control · Cloudflare Cache (CDN) docs
  head_html: <title>CDN-Cache-Control · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Use CDN-Cache-Control headers to control Cloudflare cache independently."><link rel="canonical" href="https://developers.cloudflare.com/cache/concepts/cdn-cache-control/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/concepts/cdn-cache-control/index.md"><meta property="og:title" content="CDN-Cache-Control · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use CDN-Cache-Control headers to control Cloudflare cache independently."><meta property="og:url" content="https://developers.cloudflare.com/cache/concepts/cdn-cache-control/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/concepts/cdn-cache-control/#page","headline":"CDN-Cache-Control \u00b7 Cloudflare Cache (CDN) docs","description":"Use CDN-Cache-Control headers to control Cloudflare cache independently.","url":"https://developers.cloudflare.com/cache/concepts/cdn-cache-control/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers"]}</script>
  markdown: true
  noindex: false
  route: /cache/concepts/cdn-cache-control/
  schema: 1
---
<p><code>CDN-Cache-Control</code> is a response header field set on the origin to separately control the behavior of CDN caches from other intermediaries that might handle a response. You can set the <code>CDN-Cache-Control</code> or <code>Cloudflare-CDN-Cache-Control</code> response header using the same directives used with the <a href="/cache/concepts/cache-control/">Cache-Control</a>.</p>
<h2 id="header-precedence">Header precedence</h2>
<p>You have several options available to determine how <code>CDN-Cache-Control</code> directives interact with <code>Cache-Control</code> directives.</p>
<p>If a <a href="/cache/how-to/cache-response-rules/">Cache Response Rule</a> sets <code>Cache-Control</code> directives using the <code>set_cache_control</code> action, those directives take precedence over any origin-set <code>Cloudflare-CDN-Cache-Control</code> and <code>CDN-Cache-Control</code> headers.</p>
<p>When no Cache Response Rule applies, an origin can:</p>
<ul>
<li>
<p>Return the <code>CDN-Cache-Control</code> response header which Cloudflare evaluates to make caching decisions. <code>Cache-Control</code>, if also returned by the origin, is proxied as is and does not affect caching decisions made by Cloudflare. Additionally, <code>CDN-Cache-Control</code> is proxied downstream in case there are other CDNs between Cloudflare and the browser.</p>
</li>
<li>
<p>Return the <code>Cloudflare-CDN-Cache-Control</code> response header. This results in the same behavior as the origin returning <code>CDN-Cache-Control</code> except Cloudflare does not proxy <code>Cloudflare-CDN-Cache-Control</code> downstream because it’s a header only used to control Cloudflare. This option is beneficial if you want only Cloudflare to have a different caching behavior while all other downstream servers rely on <code>Cache-Control</code> or if you do not want Cloudflare to proxy the <code>CDN-Cache-Control</code> header downstream.</p>
</li>
<li>
<p>Return both <code>Cloudflare-CDN-Cache-Control</code> and <code>CDN-Cache-Control</code> response headers. In this case, Cloudflare only looks at <code>Cloudflare-CDN-Cache-Control</code> when making caching decisions because it is the most specific version of <code>CDN-Cache-Control</code> and proxies <code>CDN-Cache-Control</code> downstream. Only forwarding <code>CDN-Cache-Control</code> in this situation is beneficial if you want Cloudflare to have a different caching behavior than other CDNs downstream.</p>
</li>
</ul>
<p>Additionally, surrogates will not honor <code>Cache-Control</code> headers in the response from an origin. For example, if the <code>Surrogate-Control</code> header is present within the response, Cloudflare ignores any <code>Cache-Control</code> directives, even if the <code>Surrogate-Control</code> header does not contain directives.</p>
<h2 id="interaction-with-other-cloudflare-features">Interaction with other Cloudflare features</h2>
<h3 id="edge-cache-ttl-cache-rule">Edge Cache TTL cache rule</h3>
<p>The <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL cache rule</a> overrides the amount of time an asset is cached on the edge (Cloudflare data centers). This cache rule overrides directives in <code>Cloudflare-CDN-Cache-Control/CDN-Cache-Control</code> which manage how long an asset is cached on the edge. You can create this rule in the dashboard in <strong>Caching</strong> &gt; <strong>Cache Rules</strong>.</p>
<h3 id="browser-cache-ttl-cache-rule">Browser Cache TTL cache rule</h3>
<p>The <a href="/cache/how-to/cache-rules/settings/#browser-ttl">Browser Cache TTL cache rule</a> overrides the amount of time an asset is cached by browsers/servers downstream of Cloudflare. Browser Cache TTL only modifies the <code>Cache-Control</code> response header. This cache rule does not modify <code>Cloudflare-CDN-Cache-Control/CDN-Cache-Control</code> response headers.</p>
<h3 id="other-origin-response-headers">Other Origin Response Headers</h3>
<p>The origin returns the <code>Expires</code> response header which specifies the amount of time before an object is considered stale to the browser. This response header does not affect the caching decision at Cloudflare when <code>Cloudflare-CDN-Cache-Control/CDN-Cache-Control</code> is in use.</p>
<h3 id="cloudflare-default-cache-values">Cloudflare Default cache values</h3>
<p>In situations where Cloudflare does not receive <code>Cloudflare-CDN-Cache-Control</code>, <code>CDN-Cache-Control</code>, or <code>Cache-Control</code> values, cacheable assets use the general <a href="/cache/concepts/default-cache-behavior/">default values</a>.</p>
<h2 id="when-to-use-cdn-cache-control">When to use CDN-Cache-Control</h2>
<h3 id="manage-cached-assets-ttls">Manage cached assets TTLs</h3>
<p>Use <code>CDN-Cache-Control</code> when you want to manage cached asset’s TTLs separately for origin caches, CDN caches, and browser caches. The example below shows how you can manage your cached asset’s TTLs using origin-set response headers.</p>
<p>Headers:</p>
<ul>
<li><code>Cache-Control: max-age=14400, s-maxage=84000</code></li>
<li><code>Cloudflare-CDN-Cache-Control: max-age=24400</code></li>
<li><code>CDN-Cache-Control: max-age=18000</code></li>
</ul>
<p>Cache behavior:</p>
<table>
<tbody>
<th colspan="5" rowspan="1">
      Caches
</th>
<th colspan="5" rowspan="1">
      Cache TTL (seconds)
</th>
<tr>
<td colspan="5" rowspan="1">
        Origin Server Cache
</td>
<td colspan="5" rowspan="1">
        14400
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Network Shared Cache
</td>
<td colspan="5" rowspan="1">
        84000
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Cloudflare Edge
</td>
<td colspan="5" rowspan="1">
        24400
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Other CDNs
</td>
<td colspan="5" rowspan="1">
        18000
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Browser Cache
</td>
<td colspan="5" rowspan="1">
        14400
</td>
</tr>
</tbody>
</table>
<h3 id="specify-when-to-serve-stale-content">Specify when to serve stale content</h3>
<p>Use <code>CDN-Cache-Control</code> headers in conjunction with <code>Cache-Control</code> headers to specify when to serve stale content in the case of error or during revalidation. The example below shows how you might set your headers and directives to apply to CDNs when handling errors.</p>
<p>Headers:</p>
<ul>
<li><code>Cache-Control: stale-if-error=400</code></li>
<li><code>Cloudflare-CDN-Cache-Control: stale-if-error=60</code></li>
<li><code>CDN-Cache-Control: stale-if-error=200</code></li>
</ul>
<p>Behavior in response to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">5XX error</a>:</p>
<table>
<tbody>
<th colspan="5" rowspan="1">
      Caches
</th>
<th colspan="5" rowspan="1">
      Stale served (seconds) in response to error
</th>
<tr>
<td colspan="5" rowspan="1">
        Origin Cache Layer/Network Cache/Browser Cache
</td>
<td colspan="5" rowspan="1">
        400 (if it assumes the directive applies)
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Cloudflare Edge
</td>
<td colspan="5" rowspan="1">
        60
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Other CDN
</td>
<td colspan="5" rowspan="1">
        200
</td>
</tr>
</tbody>
</table>
