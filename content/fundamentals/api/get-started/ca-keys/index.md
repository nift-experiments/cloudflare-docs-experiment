---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/
  description: Retrieve or change your Cloudflare Origin CA key used to authenticate Origin CA certificate API requests.
  full_title: Get Origin CA keys · Cloudflare Fundamentals docs
  head_html: <title>Get Origin CA keys · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Retrieve or change your Cloudflare Origin CA key used to authenticate Origin CA certificate API requests."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/index.md"><meta property="og:title" content="Get Origin CA keys · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retrieve or change your Cloudflare Origin CA key used to authenticate Origin CA certificate API requests."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/#page","headline":"Get Origin CA keys \u00b7 Cloudflare Fundamentals docs","description":"Retrieve or change your Cloudflare Origin CA key used to authenticate Origin CA certificate API requests.","url":"https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/get-started/ca-keys/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecated">Deprecated</h3>
@markup("md", "content/.markup/bodies/9003.md")
</aside>
<p>Origin CA keys are often used as the value of header <code>X-AUTH-USER-SERVICE-KEY</code> when interacting with <a href="/ssl/origin-configuration/origin-ca/">Origin CA certificates</a> API. It is also used by <a href="/ssl/keyless-ssl/">Keyless SSL</a> key server.</p>
<p>The key value always starts with <code>v1.0-</code>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Changing the Origin CA key is not recorded by <a href="/fundamentals/account/account-security/review-audit-logs/">Audit Logs</a>.</li>
<li>Each time you view the Origin CA key, it will be presented as a different value. All these different values are <strong>simultaneously valid</strong> until you click the <code>Change</code> button, which immediately invalidates all previously generated values.</li>
<li>Origin CA keys have access to every account the user has access to.</li>
</ul>
<h2 id="view-change-your-origin-ca-keys">View/Change your Origin CA keys</h2>
<p>To retrieve your Origin CA keys:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>User Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>In the <strong>API Keys</strong> section, select <code>Origin CA Key</code>.</li>
</ol>
