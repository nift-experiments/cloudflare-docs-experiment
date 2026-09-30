---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/
  description: Use the Node.js timers API in Cloudflare Workers to schedule functions with setTimeout, setInterval, and setImmediate.
  full_title: timers · Cloudflare Workers docs
  head_html: <title>timers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js timers API in Cloudflare Workers to schedule functions with setTimeout, setInterval, and setImmediate."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/index.md"><meta property="og:title" content="timers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js timers API in Cloudflare Workers to schedule functions with setTimeout, setInterval, and setImmediate."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/#page","headline":"timers \u00b7 Cloudflare Workers docs","description":"Use the Node.js timers API in Cloudflare Workers to schedule functions with setTimeout, setInterval, and setImmediate.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/timers/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17133.md")
</aside>
<p>Use <a href="https://nodejs.org/api/timers.html"><code>node:timers</code></a> APIs to schedule functions to be executed later.</p>
<p>This includes <a href="https://nodejs.org/api/timers.html#settimeoutcallback-delay-args"><code>setTimeout</code></a> for calling a function after a delay,
<a href="https://nodejs.org/api/timers.html#clearintervaltimeout"><code>setInterval</code></a> for calling a function repeatedly,
and <a href="https://nodejs.org/api/timers.html#setimmediatecallback-args"><code>setImmediate</code></a> for calling a function in the next iteration of the event loop.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17134.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17132.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17131.md")
</aside>
<p>The full <code>node:timers</code> API is documented in the <a href="https://nodejs.org/api/timers.html">Node.js documentation for <code>node:timers</code></a>.</p>
