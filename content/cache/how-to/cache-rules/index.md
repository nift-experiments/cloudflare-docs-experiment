---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-rules/
  description: Control what and how Cloudflare caches with Cache Rules.
  full_title: Cache Rules · Cloudflare Cache (CDN) docs
  head_html: <title>Cache Rules · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Control what and how Cloudflare caches with Cache Rules."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-rules/index.md"><meta property="og:title" content="Cache Rules · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control what and how Cloudflare caches with Cache Rules."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-rules/#page","headline":"Cache Rules \u00b7 Cloudflare Cache (CDN) docs","description":"Control what and how Cloudflare caches with Cache Rules.","url":"https://developers.cloudflare.com/cache/how-to/cache-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-rules/
  schema: 1
---
<p>Use Cache Rules to customize cache settings on Cloudflare. Cache Rules allows you to make adjustments to what is eligible to cache, how long it should be cached and where, as well as trigger specific interactions with Cloudflare's cache and other Rules products for matching requests.</p>
<p>Cache Rules can be created in the <a href="/cache/how-to/cache-rules/create-dashboard/">dashboard</a>, via <a href="/cache/how-to/cache-rules/create-api/">API</a> or <a href="/cache/how-to/cache-rules/terraform-example/">Terraform</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/3907.md")
</aside>
<h2 id="rules-templates">Rules templates</h2>
<p>Cloudflare provides you with rules templates for common use cases.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Templates</strong>, and then select one of the available templates.</li>
</ol>
<p>You can also refer to the <a href="/rules/examples/">Examples gallery</a> in the developer docs.</p>
<h2 id="availability">Availability</h2>
<p>The following table describes Cache Rules availability per plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>10</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
</tbody>
</table>
<h2 id="cache-rules-and-cache-keys">Cache Rules and cache keys</h2>
<p>When a Cache Rule sets a <a href="/cache/how-to/cache-keys/">custom cache key</a>, the resulting cache entry is indexed by that key rather than the request URL alone. Depending on what the custom cache key includes, this may affect <a href="/cache/how-to/purge-cache/purge-by-single-file/">single-file purge</a>:</p>
<ul>
<li><strong>Custom cache keys that only change how the query string is handled</strong> (for example, ignoring the query string) generally work with dashboard single-file purge.</li>
<li><strong>Custom cache keys that include headers, cookies, or other request properties</strong> will prevent dashboard single-file purge from working, because the dashboard cannot send those values in a purge request.</li>
<li><strong>Even without Cache Rules</strong>, Cloudflare's default cache key includes certain request headers. Dashboard single-file purge may not work for resources cached with those headers present.</li>
</ul>
<p>To purge resources that cannot be cleared via dashboard single-file purge, you have the following options:</p>
<ul>
<li>Use the API to <a href="/api/resources/cache/methods/purge/#purge-cached-content-by-url">purge by URL</a>, including all headers, cookies, and query strings that are part of your custom cache key. If any header or cookie is missing from the purge request, it is treated as an empty value in the cache key.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-hostname/">Purge by host</a>, which clears all resources for a hostname and is not affected by custom cache keys.</li>
<li><a href="/cache/how-to/purge-cache/purge_by_prefix/">Purge by prefix</a>, which purges all resources under a URL path and is not affected by custom cache keys.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-tags/">Purge by tag</a>, which is not affected by custom cache keys.</li>
<li><a href="/cache/how-to/purge-cache/purge-everything/">Purge everything</a>, which clears all cached resources for the zone.</li>
</ul>
<p>For more information, refer to <a href="/cache/how-to/cache-keys/">Cache keys</a> and <a href="/cache/how-to/purge-cache/purge-cache-key/">Purge cache key resources</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting Cache Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
