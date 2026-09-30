---
cp9:
  canonical: https://developers.cloudflare.com/cache/concepts/customize-cache/
  description: Methods for customizing cache behavior with rules, Workers, and headers.
  full_title: Customize cache · Cloudflare Cache (CDN) docs
  head_html: <title>Customize cache · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Methods for customizing cache behavior with rules, Workers, and headers."><link rel="canonical" href="https://developers.cloudflare.com/cache/concepts/customize-cache/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/concepts/customize-cache/index.md"><meta property="og:title" content="Customize cache · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Methods for customizing cache behavior with rules, Workers, and headers."><meta property="og:url" content="https://developers.cloudflare.com/cache/concepts/customize-cache/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/concepts/customize-cache/#page","headline":"Customize cache \u00b7 Cloudflare Cache (CDN) docs","description":"Methods for customizing cache behavior with rules, Workers, and headers.","url":"https://developers.cloudflare.com/cache/concepts/customize-cache/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/concepts/customize-cache/
  schema: 1
---
<p>Some possible combinations of origin web server settings and Cloudflare <a href="/cache/how-to/cache-rules/">Cache Rules</a> include:</p>
<h2 id="create-a-directory-for-static-content-at-your-origin-web-server">Create a directory for static content at your origin web server</h2>
<p>For example, create a <code>/static/</code> subdirectory at your origin web server and a Cache Everything Cache Rule matching the following expression:</p>
<ul>
<li>Using the Expression Builder: <code>Hostname contains &quot;example.com&quot; AND URI Path starts with &quot;/static&quot;</code></li>
<li>Using the Expression Editor: <code>(http.host contains &quot;example.com&quot; and starts_with(http.request.uri.path, &quot;/static&quot;))</code></li>
</ul>
<h2 id="append-a-unique-file-extension-to-static-pages">Append a unique file extension to static pages</h2>
<p>For example, create a <code>.shtml</code> file extension for resources at your origin web server and a Cache Everything Cache Rule matching the following expression:</p>
<ul>
<li>Using the Expression Builder: <code>Hostname contains &quot;example.com&quot; AND URI Path ends with &quot;.shtml&quot;</code></li>
<li>Using the Expression Editor: <code>(http.host contains &quot;example.com&quot; and ends_with(http.request.uri.path, &quot;.shtml&quot;))</code></li>
</ul>
<h2 id="add-a-query-string-to-a-resource-s-url-to-mark-the-content-as-static">Add a query string to a resource’s URL to mark the content as static</h2>
<p>For example, add a <code>static=true</code> query string for resources at your origin web server and a Cache Everything Cache Rule matching the following expression:</p>
<ul>
<li>Using the Expression Builder: <code>Hostname contains &quot;example.com&quot; AND URI Query String contains &quot;static=true&quot;</code></li>
<li>Using the Expression Editor: <code>(http.host contains &quot;example.com&quot; and http.request.uri.query contains &quot;static=true&quot;)</code></li>
</ul>
<p>Resources that match a Cache Everything Cache Rule are still not cached if the origin web server sends a Cache-Control header of <code>max-age=0</code>, <code>private</code>, <code>no-cache</code>, or an <code>Expires</code> header with an already expired date. Include the <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL</a> setting within the Cache Everything Cache Rule to additionally override the <code>Cache-Control</code> headers from the origin web server.</p>
