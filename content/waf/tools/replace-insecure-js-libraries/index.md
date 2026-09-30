---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/
  description: Detect and notify about insecure JavaScript libraries on your site.
  full_title: Replace insecure JavaScript libraries · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Replace insecure JavaScript libraries · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Detect and notify about insecure JavaScript libraries on your site."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/index.md"><meta property="og:title" content="Replace insecure JavaScript libraries · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect and notify about insecure JavaScript libraries on your site."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="JavaScript,CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/#page","headline":"Replace insecure JavaScript libraries \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Detect and notify about insecure JavaScript libraries on your site.","url":"https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","CSP"]}</script>
  markdown: true
  noindex: false
  route: /waf/tools/replace-insecure-js-libraries/
  schema: 1
---
<p>This feature, when turned on, automatically rewrites URLs to external JavaScript libraries to point to Cloudflare-hosted libraries instead. This change improves security and performance, and reduces the risk of malicious code being injected.</p>
<p>This rewrite operation currently supports the <code>polyfill</code> JavaScript library hosted in <code>polyfill.io</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15339.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>When turned on, Cloudflare will check HTTP(S) proxied traffic for <code>script</code> tags with an <code>src</code> attribute pointing to a potentially insecure service and replace the <code>src</code> value with the equivalent link hosted under <a href="https://cdnjs.cloudflare.com/">cdnjs</a>.</p>
<p>The rewritten URL will keep the original URL scheme (<code>http://</code> or <code>https://</code>).</p>
<p>For <code>polyfill.io</code> URL rewrites, all <code>3.*</code> versions of the <code>polyfill</code> library are supported under the <code>/v3</code> path. Additionally, the <code>/v2</code> path is also supported. If an unknown version is requested under the <code>/v3</code> path, Cloudflare will rewrite the URL to use the latest <code>3.*</code> version of the library (currently <code>3.111.0</code>).</p>
<h2 id="availability">Availability</h2>
<p>The feature is available in all Cloudflare plans, and is turned on by default on Free plans.</p>
<hr />
<h2 id="configure">Configure</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15343.md")
</div></div>
<hr />
<h2 id="final-remarks">Final remarks</h2>
<p>Since <a href="/pages/configuration/preview-deployments/"><code>pages.dev</code> zones</a> are on a Free plan, the <strong>Replace insecure JavaScript libraries</strong> feature is turned on by default on these zones and it is not possible to turn it off.</p>
