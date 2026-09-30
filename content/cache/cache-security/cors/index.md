---
cp9:
  canonical: https://developers.cloudflare.com/cache/cache-security/cors/
  description: How Cloudflare handles CORS headers and cross-origin resource caching.
  full_title: Cross-Origin Resource Sharing (CORS) · Cloudflare Cache (CDN) docs
  head_html: <title>Cross-Origin Resource Sharing (CORS) · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="How Cloudflare handles CORS headers and cross-origin resource caching."><link rel="canonical" href="https://developers.cloudflare.com/cache/cache-security/cors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/cache-security/cors/index.md"><meta property="og:title" content="Cross-Origin Resource Sharing (CORS) · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Cloudflare handles CORS headers and cross-origin resource caching."><meta property="og:url" content="https://developers.cloudflare.com/cache/cache-security/cors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="CORS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/cache-security/cors/#page","headline":"Cross-Origin Resource Sharing (CORS) \u00b7 Cloudflare Cache (CDN) docs","description":"How Cloudflare handles CORS headers and cross-origin resource caching.","url":"https://developers.cloudflare.com/cache/cache-security/cors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CORS"]}</script>
  markdown: true
  noindex: false
  route: /cache/cache-security/cors/
  schema: 1
---
<p>A cross-origin request occurs when a webpage on one origin (for example, <code>a.example.com</code>) requests a resource from a different origin (for example, <code>b.secondexample.com</code>). Cross-Origin Resource Sharing (CORS) is a mechanism that uses HTTP headers to let the server at <code>b.secondexample.com</code> indicate whether <code>a.example.com</code> is allowed to access its resources. Browsers enforce these headers and block access to responses that are not permitted.</p>
<p>Cloudflare supports CORS by:</p>
<ul>
<li>Identifying cached assets based on the <code>Host</code> Header, <code>Origin</code> Header, URL path, and query. This allows different resources to use the same <code>Host</code> header but different <code>Origin</code> headers.</li>
<li>Passing <code>Access-Control-Allow-Origin</code> headers from the origin server to the browser.</li>
</ul>
<p>The <code>Access-Control-Allow-Origin</code> header lets a server specify rules for sharing its resources with external origins. A server may respond with different <code>Access-Control-Allow-Origin</code> values depending on the <code>Origin</code> header in the request. These headers are often present on <a href="/cache/concepts/default-cache-behavior/">cacheable content</a>.</p>
<h2 id="add-or-change-cors-headers-at-the-origin-server">Add or change CORS headers at the origin server</h2>
<p>If you add or change CORS configuration at your origin web server, purging the Cloudflare cache by URL does not update the CORS headers. Force Cloudflare to retrieve the new CORS headers via one of the following options:</p>
<ul>
<li>Change the filename or URL to bypass cache to instruct Cloudflare to retrieve the latest CORS headers.</li>
<li>Use the <a href="/api/resources/cache/methods/purge/#purge-cached-content-by-url">single-file purge API</a> to specify the appropriate CORS headers along with the purge request.</li>
<li>Update the resource’s last-modified time at your origin web server. Then, complete a <a href="/cache/how-to/purge-cache/purge-everything/">full purge</a> to retrieve the latest version of your assets including updated CORS headers.</li>
</ul>
<h2 id="add-or-change-cors-headers-on-cloudflare">Add or change CORS headers on Cloudflare</h2>
<p>You can use one of following methods to set CORS headers using Cloudflare products:</p>
<ul>
<li>Use a <a href="/workers/">Worker</a>: Refer to <a href="/workers/examples/cors-header-proxy/">CORS header proxy</a> for an example.</li>
<li>Configure a <a href="/rules/snippets/">Snippet</a>: Refer to <a href="/rules/snippets/examples/define-cors-headers/">Define CORS headers</a> for an example.</li>
<li>Use <a href="/rules/transform/">Transform Rules</a>: Refer to <a href="/rules/transform/examples/add-cors-header/">Add a wildcard CORS response header</a> for an example.</li>
</ul>
