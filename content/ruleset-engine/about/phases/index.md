---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/about/phases/
  description: How phases organize rule execution in the Ruleset Engine request lifecycle.
  full_title: Phases · Cloudflare Ruleset Engine docs
  head_html: <title>Phases · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="How phases organize rule execution in the Ruleset Engine request lifecycle."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/about/phases/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/about/phases/index.md"><meta property="og:title" content="Phases · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How phases organize rule execution in the Ruleset Engine request lifecycle."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/about/phases/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/about/phases/#page","headline":"Phases \u00b7 Cloudflare Ruleset Engine docs","description":"How phases organize rule execution in the Ruleset Engine request lifecycle.","url":"https://developers.cloudflare.com/ruleset-engine/about/phases/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/about/phases/
  schema: 1
---
<p>A phase defines a stage in the life of a request where you can execute <a href="/ruleset-engine/about/rulesets/">rulesets</a>. Phases are defined by Cloudflare and cannot be modified.</p>
<p>Phases exist at two levels:</p>
<ul>
<li>At the <a href="/fundamentals/concepts/accounts-and-zones/#accounts">account</a> level</li>
<li>At the <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> level</li>
</ul>
<p>For the same phase, rules defined at the account level are evaluated before the rules defined at the zone level.</p>
<p>Each phase has at most one <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> at the account and zone level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13292.md")
</aside>
<p>The following diagram outlines the request handling process where requests go through the available phases:</p>
<p><img src="/assets/upstream/images/ruleset-engine/rulesets-phases.png" alt="Diagram showing the request handling process. The user request goes through several request phases until it eventually reaches the origin server (the request can also be blocked). The origin returns a response, which goes through several response phases until it reaches the user." /></p>
<p>Cloudflare products are specific to one or more phases, and they add support for different features. Check the documentation for each Cloudflare product for details on the applicable phases.</p>
<p>Refer to <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for a list of phases and their corresponding Cloudflare products.</p>
