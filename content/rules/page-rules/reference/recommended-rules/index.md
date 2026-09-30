---
cp9:
  canonical: https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/
  description: Recommended Page Rules configurations for common use cases.
  full_title: Recommended page rules · Cloudflare Rules docs
  head_html: <title>Recommended page rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Recommended Page Rules configurations for common use cases."><link rel="canonical" href="https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/index.md"><meta property="og:title" content="Recommended page rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Recommended Page Rules configurations for common use cases."><meta property="og:url" content="https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Caching,Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/#page","headline":"Recommended page rules \u00b7 Cloudflare Rules docs","description":"Recommended Page Rules configurations for common use cases.","url":"https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Caching","Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/page-rules/reference/recommended-rules/
  schema: 1
---
<p>Use Cloudflare Page Rules to improve the user experience of your domain with hardened security and enhanced site performance, while increasing reliability and minimizing bandwidth usage for your origin server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13110.md")
</aside>
<p>Keep in mind that not all rules will be right for everyone, but these are some of the most popular.</p>
<ul>
<li>301/302 Forwarding URL</li>
<li>Cache Level in specific paths</li>
<li>Edge Cache TTL, Always Online, and Browser Cache TTL</li>
</ul>
<h3 id="301-302-forwarding-url">301/302 Forwarding URL</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13109.md")
</aside>
<p>Two common examples for using forwarding URLs are:</p>
<ul>
<li>Defining the root as the canonical version of your domain.</li>
<li>Directing visitors to a specific page with an easy to remember URL.</li>
</ul>
<p>This example page rule configuration defines the root as the canonical version of your domain:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13111.md")
</div>
<p>This example redirects visitors to a specific page with an easy to remember URL:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/13112.md")
</div>
<h3 id="cache-level-in-specific-paths">Cache Level in specific paths</h3>
<p>Certain sections of a website, like the login or admin section, have different security and performance requirements than your general public-facing pages.</p>
<p>The following example page rule configuration bypasses cache for requests targeting a specific path:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/13113.md")
</div>
<h3 id="edge-cache-ttl-and-browser-cache-ttl">Edge Cache TTL and Browser Cache TTL</h3>
<p>Certain resources on your domain will likely not change often. For these resources, taking advantage of aggressive caching options can significantly reduce the load on your server and bandwidth utilization.</p>
<h4 id="examples">Examples</h4>
<p>In the following example page rule configuration, the target is a folder that holds the majority of the image assets as well as some other types of multimedia.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/13114.md")
</div>
<p>The following example page rule configuration applies unique rules for critical pages that do not change very often.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@markup("md", "content/.markup/bodies/13115.md")
</div>
