---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/about/rulesets/
  description: How rulesets group and organize rules in the Ruleset Engine.
  full_title: Rulesets · Cloudflare Ruleset Engine docs
  head_html: <title>Rulesets · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="How rulesets group and organize rules in the Ruleset Engine."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/about/rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/about/rulesets/index.md"><meta property="og:title" content="Rulesets · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How rulesets group and organize rules in the Ruleset Engine."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/about/rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/about/rulesets/#page","headline":"Rulesets \u00b7 Cloudflare Ruleset Engine docs","description":"How rulesets group and organize rules in the Ruleset Engine.","url":"https://developers.cloudflare.com/ruleset-engine/about/rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/about/rulesets/
  schema: 1
---
<p>A ruleset is an ordered set of <a href="/ruleset-engine/about/rules/">rules</a> that you can apply to traffic on the Cloudflare global network. Rulesets belong to a phase and can only execute in the same phase. To deploy a ruleset to a phase, add a rule that executes the ruleset to the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">phase entry point ruleset</a>.</p>
<p>Rulesets are versioned. Each ruleset modification creates a new version of the ruleset. You can have several versions of a ruleset in use at the same time. When you deploy a ruleset — that is, when you create a rule that executes the ruleset — the most recent version of the ruleset is selected by default.</p>
<p>There are several types of rulesets:</p>
<ul>
<li>Phases have their entry point rulesets.</li>
<li>Cloudflare provides managed rulesets you can deploy.</li>
<li>You can create and manage your own custom rulesets.</li>
</ul>
<p>Specific Cloudflare products may provide other types of rulesets.</p>
<h2 id="entry-point-ruleset">Entry point ruleset</h2>
<p>An entry point ruleset contains a list of ordered <a href="/ruleset-engine/about/rules/">rules</a> that run in a <a href="/ruleset-engine/about/phases/">phase</a> at the account or zone level. This ruleset is an entry point for all rules executed in a phase. Some of these rules may run other rulesets.</p>
<p>Each phase has at most one entry point ruleset at the account level and at the zone level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13289.md")
</aside>
<h2 id="managed-rulesets">Managed rulesets</h2>
<p>Managed rulesets are preconfigured rulesets provided by Cloudflare that you can deploy to a phase. Only Cloudflare can modify these rulesets.</p>
<p>The rules in a managed ruleset have a default action and status. However, you can define <strong>overrides</strong> that change these defaults.</p>
<p>There are several Cloudflare products that provide you with managed rulesets. Check each product’s documentation for details on the available managed rulesets.</p>
<p>For more information on deploying managed rulesets and defining overrides, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a>.</p>
<h2 id="custom-rulesets">Custom rulesets</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13288.md")
</aside>
<p>Use custom rulesets to define your own sets of rules. After creating a custom ruleset, deploy it to a phase by creating a rule that executes the ruleset.</p>
<p>For more information on creating and deploying custom rulesets, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a>.</p>
