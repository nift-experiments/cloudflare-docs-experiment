---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/
  description: Create URL rewrite rules in the Cloudflare dashboard.
  full_title: Create a URL rewrite rule in the dashboard · Cloudflare Rules docs
  head_html: <title>Create a URL rewrite rule in the dashboard · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create URL rewrite rules in the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/index.md"><meta property="og:title" content="Create a URL rewrite rule in the dashboard · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create URL rewrite rules in the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="URL rewrite"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/#page","headline":"Create a URL rewrite rule in the dashboard \u00b7 Cloudflare Rules docs","description":"Create URL rewrite rules in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["URL rewrite"]}</script>
  markdown: true
  noindex: false
  route: /rules/transform/url-rewrite/create-dashboard/
  schema: 1
---
<p>Refer to the <a href="/rules/transform/examples/?operation=Rewrite+URL">Rules examples gallery</a> for examples of rule definitions.</p>
<p>To create a rule:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13129.md")
</div>
<h2 id="wildcard-pattern-parameters">Wildcard pattern parameters</h2>
<p>The Cloudflare dashboard offers a simplified user interface for creating URL rewrites based on wildcard matching and replacement. When you select <strong>Wildcard pattern</strong>, you will have the following parameters available:</p>
<ul>
<li>
<p><strong>Request URL</strong>: Enter the <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard pattern</a> using the asterisk (<code>*</code>) character to match multiple requests. For example, <code>http*://*.example.com/*</code>.</p>
</li>
<li>
<p><strong>Then rewrite the path and/or query</strong>: Define the <a href="/rules/transform/url-rewrite/reference/parameters/">URL rewrite settings</a> including:</p>
<ul>
<li><strong>Path</strong> &gt; <strong>Target path</strong>: Enter the URI path to match, which can include wildcards (for example, <code>/oldpath/*</code>).</li>
<li><strong>Path</strong> &gt; <strong>Rewrite to</strong>: Enter the new URI path. You can use <a href="/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard replacement</a> such as <code>${1}</code> and <code>${2}</code> to define a dynamic target path (for example, <code>/newpath/${1}</code>). Leave this field empty to remove the URI path.</li>
<li><strong>Query</strong> &gt; <strong>Target query</strong>: Enter the query string to match, which can include wildcards (for example, <code>?sort=*</code>).</li>
<li><strong>Query</strong> &gt; <strong>Rewrite to</strong>: Enter the new query string. You can use <a href="/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard replacement</a> such as <code>${1}</code> and <code>${2}</code> to define a dynamic query string (for example, <code>?order=${1}</code>). Leave this field empty to remove the query string.</li>
</ul>
</li>
</ul>
<p>Refer to <a href="/rules/transform/url-rewrite/reference/parameters/#wildcard-matching-and-replacement">URL rewrite parameters</a> for the equivalent rule configuration when using the API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/13127.md")
</aside>
