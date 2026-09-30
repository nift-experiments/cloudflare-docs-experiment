---
cp9:
  canonical: https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/
  description: Protect your site from web cache poisoning attacks.
  full_title: Avoid Web Cache Poisoning · Cloudflare Cache (CDN) docs
  head_html: <title>Avoid Web Cache Poisoning · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Protect your site from web cache poisoning attacks."><link rel="canonical" href="https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/index.md"><meta property="og:title" content="Avoid Web Cache Poisoning · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect your site from web cache poisoning attacks."><meta property="og:url" content="https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="Security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/#page","headline":"Avoid Web Cache Poisoning \u00b7 Cloudflare Cache (CDN) docs","description":"Protect your site from web cache poisoning attacks.","url":"https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Security"]}</script>
  markdown: true
  noindex: false
  route: /cache/cache-security/avoid-web-poisoning/
  schema: 1
---
<p>A cache poisoning attack uses an HTTP request to trick an origin web server into responding with a harmful resource that has the same cache key as a clean request. As a result, the poisoned resource gets cached and served to other users.</p>
<p>A Content Delivery Network (CDN) like Cloudflare relies on cache keys to compare new requests against cached resources. The CDN then determines whether the resource should be served from the cache or requested directly from the origin web server.</p>
<h2 id="learn-about-cache-poisoning">Learn about Cache Poisoning</h2>
<p>To deepen your understanding of the risks and vulnerabilities associated with cache poisoning, consult the following resources:</p>
<ul>
<li><a href="https://portswigger.net/blog/practical-web-cache-poisoning">Practical Web Cache Poisoning</a></li>
<li><a href="https://blog.cloudflare.com/cache-poisoning-protection/">How Cloudflare protects customers from cache poisoning</a></li>
</ul>
<h2 id="only-cache-files-that-are-truly-static">Only cache files that are truly static</h2>
<p>Review the caching configuration for your origin web server and ensure you are caching files that are static and do not depend on user input in any way. To learn more about Cloudflare caching, review:</p>
<ul>
<li><a href="/cache/concepts/default-cache-behavior/">Which file extensions does Cloudflare cache for static content?</a></li>
<li><a href="/cache/how-to/cache-rules/">How Do I Tell Cloudflare What to Cache?</a></li>
</ul>
<h2 id="do-not-trust-data-in-http-headers">Do not trust data in HTTP headers</h2>
<p>Attackers can exploit HTTP headers to inject malicious content into cached responses. For example, if your application reflects an untrusted header value in the response body, an attacker could use this to perform cross-site scripting (XSS) through the cache. To reduce this risk:</p>
<ul>
<li>Do not rely on values in HTTP headers if they are not part of your <a href="/cache/how-to/cache-keys/">cache key</a>.</li>
<li>Do not include untrusted header values in your response body.</li>
</ul>
<h2 id="do-not-trust-get-request-bodies">Do not trust GET request bodies</h2>
<p>Cloudflare caches contents of GET request bodies, but they are not included in the cache key. GET request bodies should be considered untrusted and should not modify the contents of a response. If a GET body can change the contents of a response, consider bypassing cache or using a POST request.</p>
<h2 id="monitor-web-security-advisories">Monitor web security advisories</h2>
<p>To keep informed about Internet security threats, Cloudflare recommends that you monitor web security advisories on a regular basis. Some of the more popular advisories include:</p>
<ul>
<li><a href="https://www.drupal.org/security">Drupal Security Advisories</a></li>
<li><a href="https://symfony.com/blog/category/security-advisories">Symfony Security Advisories</a></li>
<li><a href="https://getlaminas.org/security/advisories">Laminas Security Advisories</a></li>
</ul>
