---
cp9:
  canonical: https://developers.cloudflare.com/cache/get-started/
  description: Set up and configure Cloudflare caching for your website.
  full_title: Get started with Cache · Cloudflare Cache (CDN) docs
  head_html: <title>Get started with Cache · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and configure Cloudflare caching for your website."><link rel="canonical" href="https://developers.cloudflare.com/cache/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/get-started/index.md"><meta property="og:title" content="Get started with Cache · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and configure Cloudflare caching for your website."><meta property="og:url" content="https://developers.cloudflare.com/cache/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="CORS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/get-started/#page","headline":"Get started with Cache \u00b7 Cloudflare Cache (CDN) docs","description":"Set up and configure Cloudflare caching for your website.","url":"https://developers.cloudflare.com/cache/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CORS"]}</script>
  markdown: true
  noindex: false
  route: /cache/get-started/
  schema: 1
---
<p>Cloudflare speeds up your website by caching content across globally distributed data centers.</p>
<p>Content can be static or dynamic. Static content — such as images, CSS, and JavaScript files — is <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">cacheable</a> by default. Dynamic content, such as HTML pages, is not cached by default, but you can use <a href="/cache/how-to/cache-rules/">Cache Rules</a> to cache it.</p>
<p>Cloudflare caches static content based on the following factors:</p>
<ul>
<li><a href="/cache/how-to/set-caching-levels/">Caching levels</a></li>
<li><a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">File extension</a></li>
<li>Presence of <a href="/cache/advanced-configuration/query-string-sort/">query strings</a></li>
<li><a href="/cache/concepts/cache-control/">Origin cache-control headers</a></li>
<li>Origin headers that indicate <span class="nb-glossary-tooltip" title="dynamic content">dynamic content</span></li>
<li>Cache rules that bypass cache on cookie</li>
</ul>
<p>Cloudflare only caches resources within the Cloudflare data center that serve the request. Cloudflare does not cache off-site or third-party resources, or content hosted on <a href="/dns/proxy-status/">DNS-only (unproxied)</a> DNS records.</p>
<h2 id="learn-the-basics">Learn the basics</h2>
<p>Discover the benefits of caching with Cloudflare's CDN and understand the default cache behavior.</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/cdn/what-is-a-cdn/">Understand what is a CDN</a></li>
<li><a href="/cache/concepts/default-cache-behavior/">Understand default cache behavior</a></li>
<li><a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">Understand the default file types Cloudflare caches</a></li>
</ul>
<h2 id="make-more-resources-cacheable">Make more resources cacheable</h2>
<p>Configure your settings to cache static HTML or cache anonymous page views of dynamic content.</p>
<ul>
<li><a href="/cache/how-to/cache-rules/">Customize Caching with Cache Rules</a></li>
<li><a href="/cache/concepts/customize-cache/">Specify which resources to cache</a></li>
<li><a href="/cache/concepts/cache-control/">Understand Origin Cache Control</a></li>
<li><a href="/cache/how-to/cache-rules/examples/cache-device-type/">Cache by device type (Enterprise only)</a></li>
</ul>
<h2 id="improve-cache-hit-rates">Improve cache HIT rates</h2>
<p>Include or exclude query strings, optimize cache keys, or enable <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> to improve HIT rates and reduce traffic to your origin.</p>
<ul>
<li><a href="/cache/how-to/set-caching-levels/">Choose a cache level</a></li>
<li><a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache with Argo</a></li>
<li><a href="/cache/how-to/cache-keys/">Configure custom cache keys (Enterprise only)</a></li>
<li><a href="/speed/optimization/content/prefetch-urls/">Enable Prefetch URLs (Enterprise only)</a></li>
</ul>
<h2 id="secure-your-cache-configuration">Secure your cache configuration</h2>
<p>Control resources a client is allowed to load and set access permissions to allow different origins to access your origin's resources. Protect your site from web cache deception attacks while still caching static assets.</p>
<ul>
<li><a href="/cache/cache-security/avoid-web-poisoning/">Avoid web cache poisoning attacks</a></li>
<li><a href="/cache/cache-security/cors/">Configure Cross-Origin Resource Sharing (CORS)</a></li>
<li><a href="/cache/cache-security/cache-deception-armor/#enable-cache-deception-armor">Enable Cache Deception Armor</a></li>
</ul>
<h2 id="features-that-alter-cached-content">Features that alter cached content</h2>
<p>Some Cloudflare features modify your HTML or cached objects at the edge to enable optimizations or security protections.
These alterations only affect cached copies at Cloudflare's edge and do not change your original source files. Cloudflare removes the changes when you disable the feature and purge the cache.
These alterations only affect cached copies at Cloudflare's edge and do not change your original source files. The changes are removed if the feature is disabled and the cache is purged.</p>
<ul>
<li><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a></li>
<li><a href="/images/polish/">Polish</a></li>
<li><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a></li>
<li><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email address obfuscation</a></li>
<li><a href="/bots/additional-configurations/javascript-detections/">Bot Management JavaScript Detections</a></li>
</ul>
<h2 id="troubleshoot">Troubleshoot</h2>
<p>Resolve common caching concerns.</p>
<ul>
<li><a href="/cache/concepts/cache-responses/">Learn about Cloudflare's cache response statuses</a></li>
<li><a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#troubleshoot-requests-with-curl">Investigate Cloudflare's cache response with cURL</a></li>
<li><a href="/cache/troubleshooting/always-online/">Diagnose Always Online issues</a></li>
</ul>
