---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/
  description: Set how long browsers cache resources from your site.
  full_title: Set Browser Cache TTL · Cloudflare Cache (CDN) docs
  head_html: <title>Set Browser Cache TTL · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Set how long browsers cache resources from your site."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/index.md"><meta property="og:title" content="Set Browser Cache TTL · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set how long browsers cache resources from your site."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/#page","headline":"Set Browser Cache TTL \u00b7 Cloudflare Cache (CDN) docs","description":"Set how long browsers cache resources from your site.","url":"https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/edge-browser-cache-ttl/set-browser-ttl/
  schema: 1
---
<p>Specify a time for a visitor’s Browser Cache TTL to accelerate the page load for repeat visitors to your website. To configure cache duration within Cloudflare’s data centers, refer to <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL</a>.</p>
<p>By default, Cloudflare honors the cache expiration set in your <code>Expires</code> and <code>Cache-Control</code> headers. Cloudflare overrides any <code>Cache-Control</code> or <code>Expires</code> headers with values set via the <strong>Browser Cache TTL</strong> option under <strong>Caching</strong> on your dashboard if:</p>
<ul>
<li>The value of the <code>Cache-Control</code> header from the origin web server is less than the <strong>Browser Cache TTL</strong> setting. This means that <strong>Browser cache TTL</strong> value needs to be higher than origin <code>max-age</code>.</li>
<li>The origin web server does not send a <code>Cache-Control</code> or an <code>Expires</code> header.</li>
</ul>
<p>Unless specifically set in a <a href="/cache/how-to/cache-rules/">Cache Rule</a>, Cloudflare does not override or insert <code>Cache-Control</code> headers if you set <strong>Browser Cache TTL</strong> to <strong>Respect Existing Headers</strong>.</p>
<p>Nevertheless, the value you set via Cache Rule will be ignored if <code>Cache-Control: max-age</code> is higher. In other words, you can override to make browsers cache longer than Cloudflare's edge but not less.</p>
<h2 id="set-browser-cache-ttl">Set Browser Cache TTL</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3874.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Caching</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Browser Cache TTL</strong>, select the desired cache expiration time from the drop-down menu.</li>
</ol>
<p>The <strong>Respect Existing Headers</strong> option tells Cloudflare to honor the settings in the <code>Cache-Control</code> headers from your origin web server.</p>
