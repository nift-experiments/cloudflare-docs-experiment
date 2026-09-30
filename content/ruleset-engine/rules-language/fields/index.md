---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/
  description: Fields available for use in Ruleset Engine rule expressions.
  full_title: Fields reference · Cloudflare Ruleset Engine docs
  head_html: <title>Fields reference · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Fields available for use in Ruleset Engine rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/index.md"><meta property="og:title" content="Fields reference · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fields available for use in Ruleset Engine rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/#page","headline":"Fields reference \u00b7 Cloudflare Ruleset Engine docs","description":"Fields available for use in Ruleset Engine rule expressions.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rules-language/fields/
  schema: 1
---
<p>The Cloudflare Rules language supports different types of fields such as:</p>
<ul>
<li>Request fields that represent the basic properties of incoming requests, including specific fields for accessing request headers, URI components, and the request body.</li>
<li>Dynamic fields that represent computed or derived values, typically related to threat intelligence about an HTTP request.</li>
<li>Response fields that represent the basic properties of the received response.</li>
<li>Raw fields that preserve the original request values for later evaluations.</li>
</ul>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> for the list of available fields.</p>
<h2 id="differences-from-wireshark-display-fields">Differences from Wireshark display fields</h2>
<p>Most fields supported by the Cloudflare Rules language use the same naming conventions as <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">Wireshark display fields</a>. However, there are some subtle differences between Cloudflare and Wireshark:</p>
<ul>
<li>
<p>Wireshark supports <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR (Classless Inter-Domain Routing) notation</a> for expressing IP address ranges in equality comparisons (<code>ip.src == 1.2.3.0/24</code>, for example). Cloudflare does not.</p>
<p>To evaluate a range of addresses using CIDR notation, use the <a href="/ruleset-engine/rules-language/operators/#comparison-operators"><code>in</code></a> comparison operator as in this example: <code>ip.src in {1.2.3.0/24 4.5.6.0/24}</code>.</p>
</li>
<li>
<p>In Wireshark, <code>ssl</code> is a protocol field containing hundreds of other fields of various types that are available for comparison in multiple ways. However, in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/ssl/"><code>ssl</code></a> is a single Boolean field that indicates whether the connection from the client to Cloudflare is encrypted.</p>
</li>
<li>
<p>The Cloudflare Rules language does not support the <code>slice</code> operator.</p>
</li>
</ul>
