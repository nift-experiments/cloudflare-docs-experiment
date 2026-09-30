---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/
  description: Configure edge and browser cache TTL for your resources.
  full_title: Edge and Browser Cache TTL · Cloudflare Cache (CDN) docs
  head_html: <title>Edge and Browser Cache TTL · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure edge and browser cache TTL for your resources."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/index.md"><meta property="og:title" content="Edge and Browser Cache TTL · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure edge and browser cache TTL for your resources."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/#page","headline":"Edge and Browser Cache TTL \u00b7 Cloudflare Cache (CDN) docs","description":"Configure edge and browser cache TTL for your resources.","url":"https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/edge-browser-cache-ttl/
  schema: 1
---
<h2 id="edge-cache-ttl">Edge Cache TTL</h2>
<p>Edge Cache TTL (Time to Live) specifies the maximum time to cache a resource in the Cloudflare global network. Edge Cache TTL is not visible in response headers and the minimum Edge Cache TTL depends on plan type.</p>
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
<td>Minimum Edge Cache TTL</td>
<td>2 hours</td>
<td>1 hour</td>
<td>1 second</td>
<td>1 second</td>
</tr>
</tbody>
</table>
<p>For more information on how to set up Edge Cache TTL, refer to <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Cache rules</a>.</p>
<h2 id="browser-cache-ttl">Browser Cache TTL</h2>
<p>The Browser Cache TTL sets the expiration for resources cached in a visitor’s browser. By default, Cloudflare honors the cache expiration set in your <code>Expires</code> and <code>Cache-Control</code> headers but overrides those headers if:</p>
<ul>
<li>The value of the <code>Expires</code> or <code>Cache-Control</code> header from the origin web server is less than the Browser Cache TTL Cloudflare setting.</li>
<li>The origin web server does not send a <code>Cache-Control</code> or an <code>Expires</code> header.</li>
</ul>
<p>Unless specifically set in a cache rule, Cloudflare does not override or insert <code>Cache-Control</code> headers if you set <strong>Browser Cache TTL</strong> to <strong>Respect Existing Headers</strong>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3875.md")
</aside>
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
<td>Minimum Browser Cache TTL (Page Rules)</td>
<td>2 minutes</td>
<td>2 minutes</td>
<td>2 minutes</td>
<td>30 seconds</td>
</tr>
<tr>
<td>Minimum Browser Cache TTL</td>
<td>1 second</td>
<td>1 second</td>
<td>1 second</td>
<td>1 second</td>
</tr>
<tr>
<td>Default Browser Cache TTL</td>
<td>4 hours</td>
<td>4 hours</td>
<td>4 hours</td>
<td>4 hours</td>
</tr>
</tbody>
</table>
<p>For more information on setting the Browser Cache TTL, refer to <a href="/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/">Set Browser Cache TTL</a>.</p>
