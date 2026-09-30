---
cp9:
  canonical: https://developers.cloudflare.com/rules/compression-rules/create-api/
  description: Create compression rules using the Rulesets API.
  full_title: Create a compression rule via API · Cloudflare Rules docs
  head_html: <title>Create a compression rule via API · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create compression rules using the Rulesets API."><link rel="canonical" href="https://developers.cloudflare.com/rules/compression-rules/create-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/compression-rules/create-api/index.md"><meta property="og:title" content="Create a compression rule via API · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create compression rules using the Rulesets API."><meta property="og:url" content="https://developers.cloudflare.com/rules/compression-rules/create-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/compression-rules/create-api/#page","headline":"Create a compression rule via API \u00b7 Cloudflare Rules docs","description":"Create compression rules using the Rulesets API.","url":"https://developers.cloudflare.com/rules/compression-rules/create-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/compression-rules/create-api/
  schema: 1
---
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a compression rule via API.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a compression rule via API, make sure you:</p>
<ul>
<li>Set the rule action to <code>compress_response</code>.</li>
<li>Define the parameters in the <code>action_parameters</code> field according to the <a href="/rules/compression-rules/settings/#api-configuration-settings">settings</a> you wish to override for matching requests.</li>
<li>Deploy the rule to the <code>http_response_compression</code> phase at the zone level.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<p>Follow this workflow to create a compression rule for a given zone via API:</p>
<ol>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> operation to check if there is already a ruleset for the <code>http_response_compression</code> phase at the zone level.</p>
</li>
<li>
<p>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:</p>
<ul>
<li><strong>kind</strong>: <code>zone</code></li>
<li><strong>phase</strong>: <code>http_response_compression</code></li>
</ul>
</li>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add a compression rule to the list of ruleset rules. Alternatively, include the rule in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</p>
</li>
</ol>
<h2 id="examples">Examples</h2>
<p>For example API requests, refer to the <a href="/rules/compression-rules/examples/">Examples gallery</a>.</p>
