---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/
  description: Create cache response rules using the Rulesets API.
  full_title: Create a Cache Response Rule via API · Cloudflare Cache (CDN) docs
  head_html: <title>Create a Cache Response Rule via API · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create cache response rules using the Rulesets API."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/index.md"><meta property="og:title" content="Create a Cache Response Rule via API · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create cache response rules using the Rulesets API."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/#page","headline":"Create a Cache Response Rule via API \u00b7 Cloudflare Cache (CDN) docs","description":"Create cache response rules using the Rulesets API.","url":"https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-response-rules/create-api/
  schema: 1
---
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a Cache Response Rule via API. To configure the Cloudflare API, refer to the <a href="/fundamentals/api/get-started/">API documentation</a>.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a Cache Response Rule via API, make sure you:</p>
<ul>
<li>Set the rule action to one of the <a href="/cache/how-to/cache-response-rules/settings/#available-actions">available actions</a>.</li>
<li>Define the parameters in the <code>action_parameters</code> field according to the <a href="/cache/how-to/cache-response-rules/settings/">settings</a> you wish to configure for matching responses.</li>
<li>Deploy the rule to the <code>http_response_cache_settings</code> phase entry point ruleset.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<ol>
<li>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> method to check if a ruleset already exists for the <code>http_response_cache_settings</code> phase.</li>
<li>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:
<ul>
<li>kind: <code>zone</code></li>
<li>phase: <code>http_response_cache_settings</code></li>
</ul>
</li>
<li>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add rules to the ruleset. Alternatively, include the rules in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</li>
</ol>
<h2 id="example-requests">Example requests</h2>
<p>These examples demonstrate all the available actions in Cache Response Rules using request and response matching criteria. Using these examples directly will cause any existing rules in the phase to be replaced.</p>
<details class="nb-details"><summary>Example: Strip response headers from JS files before caching</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3924.md")
</div></details>
<details class="nb-details"><summary>Example: Set static cache tags on API responses</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3925.md")
</div></details>
<details class="nb-details"><summary>Example: Add cache tags from a response header using an expression</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3926.md")
</div></details>
<details class="nb-details"><summary>Example: Override cache-control with max-age</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3927.md")
</div></details>
<details class="nb-details"><summary>Example: Set private directive with qualifiers</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3928.md")
</div></details>
<details class="nb-details"><summary>Example: Set immutable for static font assets</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3929.md")
</div></details>
<details class="nb-details"><summary>Example: Multiple rules with strip headers, tag responses, and set cache control</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3930.md")
</div></details>
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>The API token used in API requests to manage Cache Response Rules must have the following permissions:</p>
<ul>
<li><em>Zone</em> &gt; <em>Cache Rules</em> &gt; <em>Edit</em></li>
<li><em>Account Rulesets</em> &gt; <em>Edit</em></li>
<li><em>Account Filter Lists</em> &gt; <em>Edit</em></li>
</ul>
