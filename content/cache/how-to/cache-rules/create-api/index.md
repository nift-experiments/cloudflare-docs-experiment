---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/
  description: Create cache rules using the Rulesets API.
  full_title: Create a cache rule via API · Cloudflare Cache (CDN) docs
  head_html: <title>Create a cache rule via API · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create cache rules using the Rulesets API."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/index.md"><meta property="og:title" content="Create a cache rule via API · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create cache rules using the Rulesets API."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/#page","headline":"Create a cache rule via API \u00b7 Cloudflare Cache (CDN) docs","description":"Create cache rules using the Rulesets API.","url":"https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-rules/create-api/
  schema: 1
---
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a cache rule via API. To configure Cloudflare’s API refer to the <a href="/fundamentals/api/get-started/">API documentation</a>.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a cache rule via API, make sure you:</p>
<ul>
<li>Set the rule action to <code>set_cache_settings</code>.</li>
<li>Define the parameters in the <code>action_parameters</code> field according to the <a href="/cache/how-to/cache-rules/settings/">settings</a> you wish to override for matching requests.</li>
<li>Deploy the rule to the <code>http_request_cache_settings</code> phase entry point ruleset.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<ol>
<li>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> method to obtain the list of rules already present in the <code>http_request_cache_settings</code> phase entry point ruleset.</li>
<li>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:
<ul>
<li>kind: <code>zone</code></li>
<li>phase: <code>http_request_cache_settings</code></li>
</ul>
</li>
<li>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add a cache rule to the list of ruleset rules. Alternatively, include the rule in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</li>
<li>(Optional) To update an existing cache rule, use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset rule</a> operation. For an example, refer to the section below.</li>
</ol>
<h2 id="example-requests">Example requests</h2>
<p>These examples are setting all the Cache Rules of a zone to a single rule, since using these examples directly will cause any existing rules to be deleted.</p>
<details class="nb-details"><summary>Example: Cache everything for example.com</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3909.md")
</div></details>
<details class="nb-details"><summary>Example: Extend read timeout for Android clients</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3910.md")
</div></details>
<details class="nb-details"><summary>Example: Disable Cache Reserve for frequently updated assets</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3911.md")
</div></details>
<details class="nb-details"><summary>Example: Turn on Origin Range Requests for large media files</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3912.md")
</div></details>
<details class="nb-details" id="example-turn-off-default-origin-range-requests"><summary>Example: Turn off default Origin Range Requests</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3913.md")
</div></details>
<details class="nb-details"><summary>Example: Turn off default cache TTLs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3914.md")
</div></details>
<details class="nb-details"><summary>Example: Cache expected Vary responses</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3915.md")
</div></details>
<details class="nb-details"><summary>Example: Update the position of an existing rule</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3916.md")
</div></details>
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>The API token used in API requests to manage Cache Rules must have the following permissions:</p>
<ul>
<li><em>Zone</em> &gt; <em>Cache Rules</em> &gt; <em>Edit</em></li>
<li><em>Account Rulesets</em> &gt; <em>Edit</em></li>
<li><em>Account Filter Lists</em> &gt; <em>Edit</em></li>
</ul>
