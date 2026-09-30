---
cp9:
  canonical: https://developers.cloudflare.com/dns/foundation-dns/setup/
  description: Set up advanced nameservers for your Foundation DNS zone.
  full_title: Set up advanced nameservers · Cloudflare DNS docs
  head_html: <title>Set up advanced nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up advanced nameservers for your Foundation DNS zone."><link rel="canonical" href="https://developers.cloudflare.com/dns/foundation-dns/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/foundation-dns/setup/index.md"><meta property="og:title" content="Set up advanced nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up advanced nameservers for your Foundation DNS zone."><meta property="og:url" content="https://developers.cloudflare.com/dns/foundation-dns/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/foundation-dns/setup/#page","headline":"Set up advanced nameservers \u00b7 Cloudflare DNS docs","description":"Set up advanced nameservers for your Foundation DNS zone.","url":"https://developers.cloudflare.com/dns/foundation-dns/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/foundation-dns/setup/
  schema: 1
---
<p>Advanced nameservers included with <a href="/dns/foundation-dns/">Foundation DNS</a> are an opt-in configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7662.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before opting in for advanced nameservers, consider the following:</p>
<ul>
<li></li>
</ul>
<p>The advantages that come with Foundation DNS <a href="/dns/foundation-dns/advanced-nameservers/">advanced nameservers</a> are currently not available for <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>. Make sure you only use one at a time.</p>
<h3 id="differences-from-standard-nameservers">Differences from standard nameservers</h3>
<p>Some behaviors are different from standard Cloudflare nameservers:</p>
<ul>
<li>Wildcard records are still supported but, with advanced nameservers, a wildcard record (<code>*.example.com</code>) will not apply to a subdomain that is an empty non-terminal. An empty non-terminal is a node in the DNS tree that has no records associated with it but has descendants that do, as exemplified below. This behavior is in compliance with <a href="https://www.rfc-editor.org/rfc/rfc4592.html">RFC 4592</a>, which defines the role of empty non-terminals in wildcard resolution.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7664.md")
</div></details>
<ul>
<li>Subdomain delegation: once a subdomain is delegated via NS records, Cloudflare will not serve any other records (such as A, TXT, or CNAME) on that subdomain from the parent zone, even if those records exist.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7666.md")
</div></details>
<h2 id="enable-on-a-zone">Enable on a zone</h2>
<p>To enable advanced nameservers on an existing zone:</p>
<ol>
<li>Opt for advanced nameservers on your zone:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7669.md")
</div></div>
<ol start="2">
<li>Update the authoritative nameservers at your registrar. This step depends on whether you are using <a href="/registrar/">Cloudflare Registrar</a>:
<ul>
<li>If you are using Cloudflare Registrar, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to have your nameservers updated.</li>
<li>If you are using a different registrar or if your zone is delegated, <a href="/dns/nameservers/update-nameservers/#specific-processes">manually update your nameservers</a>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7661.md")
</aside>
