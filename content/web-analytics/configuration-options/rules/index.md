---
cp9:
  canonical: https://developers.cloudflare.com/web-analytics/configuration-options/rules/
  description: Create rules to include or exclude traffic from Web Analytics.
  full_title: Rules · Cloudflare Web Analytics docs
  head_html: <title>Rules · Cloudflare Web Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Create rules to include or exclude traffic from Web Analytics."><link rel="canonical" href="https://developers.cloudflare.com/web-analytics/configuration-options/rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web-analytics/configuration-options/rules/index.md"><meta property="og:title" content="Rules · Cloudflare Web Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create rules to include or exclude traffic from Web Analytics."><meta property="og:url" content="https://developers.cloudflare.com/web-analytics/configuration-options/rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Web Analytics"><meta name="algolia_product_filter" content="Cloudflare Web Analytics"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Web Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web-analytics/configuration-options/rules/#page","headline":"Rules \u00b7 Cloudflare Web Analytics docs","description":"Create rules to include or exclude traffic from Web Analytics.","url":"https://developers.cloudflare.com/web-analytics/configuration-options/rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web-analytics/configuration-options/rules/
  schema: 1
---
<p>Use <strong>Rules</strong> to configure whether to track Web Analytics for specific websites or paths. By default, Web Analytics automatically creates a single rule for the zone that injects the JavaScript (JS) snippet for all pages.</p>
<p>Rules are only available for sites proxied through Cloudflare. For more information, refer to <a href="/web-analytics/limits/">Limits</a>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the site you want to configure and select <strong>Manage site</strong>.</li>
<li>Select <strong>Advanced options</strong> &gt; <strong>Add rule</strong>.</li>
<li>Select the <strong>Action</strong> and fill in the hostname and path(s) you want to add a rule for.</li>
<li>If you want to add additional rules, select <strong>Add rule</strong>. Otherwise select <strong>Update</strong> to save the rule.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/15779.md")
</aside>
