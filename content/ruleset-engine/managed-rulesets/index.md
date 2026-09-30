---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/
  description: Deploy and customize managed rulesets provided by Cloudflare.
  full_title: Work with managed rulesets · Cloudflare Ruleset Engine docs
  head_html: <title>Work with managed rulesets · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy and customize managed rulesets provided by Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/index.md"><meta property="og:title" content="Work with managed rulesets · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy and customize managed rulesets provided by Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/ruleset-engine/managed-rulesets/#page","headline":"Work with managed rulesets \u00b7 Cloudflare Ruleset Engine docs","description":"Deploy and customize managed rulesets provided by Cloudflare.","url":"https://developers.cloudflare.com/ruleset-engine/managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/managed-rulesets/
  schema: 1
---
<p>Managed rulesets are preconfigured rulesets provided by Cloudflare that you can deploy. Only Cloudflare can modify these rulesets.</p>
<p>The rules in a managed ruleset have a default configuration. However, you can define <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> that change this default configuration.</p>
<p>Several Cloudflare products include managed rulesets:</p>
<ul>
<li><a href="/waf/managed-rules/">Web Application Firewall (WAF)</a></li>
<li><a href="/ddos-protection/managed-rulesets/">DDoS Protection</a></li>
<li><a href="/cloudflare-network-firewall/how-to/enable-managed-rulesets/">Cloudflare Network Firewall</a></li>
</ul>
<p>Check each product's documentation for details on the available managed rulesets.</p>
<h2 id="more-resources">More resources</h2>
<p>To view available managed rulesets, refer to <a href="/ruleset-engine/basic-operations/view-rulesets/">View rulesets</a>.</p>
<p>To deploy a managed ruleset to a phase, refer to <a href="/ruleset-engine/managed-rulesets/deploy-managed-ruleset/">Deploy a managed ruleset</a>.</p>
<p>To adjust the behavior of a managed ruleset, do one of the following:</p>
<ul>
<li>Customize the behavior of one or more rules by using <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a>.</li>
<li>Skip one or more managed rules by adding <a href="/ruleset-engine/managed-rulesets/create-exception/">exceptions</a>.</li>
</ul>
<p>Exceptions (only supported by the WAF) have priority over overrides.</p>
