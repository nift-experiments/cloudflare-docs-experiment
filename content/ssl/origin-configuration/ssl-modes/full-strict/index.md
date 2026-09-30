---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/
  description: Similar to Full Mode, but with added validation of the origin server’s certificate, which can be issued by a public CA like Let’s Encrypt or by Cloudflare Origin CA.
  full_title: Full (strict) - SSL/TLS encryption modes · Cloudflare SSL/TLS docs
  head_html: <title>Full (strict) - SSL/TLS encryption modes · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Similar to Full Mode, but with added validation of the origin server’s certificate, which can be issued by a public CA like Let’s Encrypt or by Cloudflare Origin CA."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/index.md"><meta property="og:title" content="Full (strict) - SSL/TLS encryption modes · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Similar to Full Mode, but with added validation of the origin server’s certificate, which can be issued by a public CA like Let’s Encrypt or by Cloudflare Origin CA."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/#page","headline":"Full (strict) - SSL/TLS encryption modes \u00b7 Cloudflare SSL/TLS docs","description":"Similar to Full Mode, but with added validation of the origin server\u2019s certificate, which can be issued by a public CA like Let\u2019s Encrypt or by Cloudflare Origin CA.","url":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/ssl-modes/full-strict/
  schema: 1
---
<p>When you set your encryption mode to <strong>Full (strict)</strong>, Cloudflare does everything in <a href="/ssl/origin-configuration/ssl-modes/full/">Full mode</a> but also enforces more stringent requirements for origin certificates.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Full - Strict SSL/TLS Encryption&#10;    accDescr: With an encryption mode of Full (strict), your application encrypts traffic going to and coming from Cloudflare.&#10;    A[Visitor] &lt;--Encrypted--&gt; B((Cloudflare))&lt;--Encrypted--&gt; C[(&quot;Origin server (verified) #9989;&quot;)]&#10;</code></pre>
<h2 id="use-when">Use when</h2>
<p>For the best security, choose <strong>Full (strict)</strong> mode whenever possible (unless you are an <a href="/ssl/origin-configuration/ssl-modes/ssl-only-origin-pull/">Enterprise customer</a>).</p>
<p>Your origin needs to be able to support an SSL certificate that is:</p>
<ul>
<li>Unexpired, meaning the certificate presents <code>notBeforeDate &lt; now() &lt; notAfterDate</code>.</li>
<li>Issued by a <a href="https://github.com/cloudflare/cfssl_trust">publicly trusted certificate authority</a> or <a href="/ssl/origin-configuration/origin-ca/">Cloudflare’s Origin CA</a>.</li>
<li>Contains a Common Name (CN) or Subject Alternative Name (SAN) that matches the requested or target hostname.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14263.md")
</aside>
<h2 id="required-setup">Required setup</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before enabling <strong>Full (strict)</strong> mode, make sure your origin:</p>
<ul>
<li>Allows HTTPS connections on port <code>443</code>.</li>
<li>Presents a certificate matching the requirements above.</li>
</ul>
<p>Otherwise, your visitors may experience a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/">526 error</a>.</p>
<h3 id="process">Process</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14266.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>Depending on your origin configuration, you may have to adjust settings to avoid <a href="/ssl/troubleshooting/mixed-content-errors/">Mixed Content errors</a> or <a href="/ssl/troubleshooting/too-many-redirects/">redirect loops</a>.</p>
