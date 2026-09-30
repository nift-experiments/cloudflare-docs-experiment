---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/
  description: No encryption is used for traffic between visitors and Cloudflare or between Cloudflare and origins. Everything is cleartext HTTP.
  full_title: Off - SSL/TLS encryption modes · Cloudflare SSL/TLS docs
  head_html: <title>Off - SSL/TLS encryption modes · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="No encryption is used for traffic between visitors and Cloudflare or between Cloudflare and origins. Everything is cleartext HTTP."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/index.md"><meta property="og:title" content="Off - SSL/TLS encryption modes · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="No encryption is used for traffic between visitors and Cloudflare or between Cloudflare and origins. Everything is cleartext HTTP."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/#page","headline":"Off - SSL/TLS encryption modes \u00b7 Cloudflare SSL/TLS docs","description":"No encryption is used for traffic between visitors and Cloudflare or between Cloudflare and origins. Everything is cleartext HTTP.","url":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/ssl-modes/off/
  schema: 1
---
<p>Setting your encryption mode to <strong>Off (not recommended)</strong> redirects any HTTPS request to plaintext HTTP.</p>
<pre tabindex="0"><code class="language-mermaid">    flowchart LR&#10;        accTitle: No SSL/TLS Encryption&#10;        accDescr: With an encryption mode of Off, your application does not encrypt traffic between the visitor and Cloudflare or between Cloudflare and your server.&#10;        A[Visitor] &lt;--Unencrypted--&gt; B((Cloudflare))&lt;--Unencrypted--&gt; C[(Origin server)]&#10;</code></pre>
<h2 id="use-when">Use when</h2>
<p>Cloudflare does not recommend setting your encryption mode to <strong>Off</strong>.</p>
<h2 id="required-setup">Required setup</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14252.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>When you set your encryption mode to <strong>Off</strong>, your application:</p>
<ul>
<li>Leaves your visitors and your application <a href="https://www.cloudflare.com/learning/ssl/why-use-https/">vulnerable to attacks</a>.</li>
<li>Will be marked as &quot;not secure&quot; by Chrome and other browsers, reducing visitor trust.</li>
<li>Will be penalized in <a href="https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html">SEO rankings</a>.</li>
</ul>
<h3 id="incompatible-settings">Incompatible settings</h3>
<p>When you set your SSL/TLS encryption mode to <strong>Off</strong>, you will not see the options for <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a> or <a href="/network/onion-routing/"><strong>Onion Routing</strong></a>.</p>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pull</a> does not work when your <a href="/ssl/origin-configuration/ssl-modes/"><strong>SSL/TLS encryption mode</strong></a> is set to <strong>Off</strong> or <strong>Flexible</strong>.
<br /></p>
