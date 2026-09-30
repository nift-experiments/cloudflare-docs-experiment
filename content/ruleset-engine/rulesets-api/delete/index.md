---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/
  description: Delete a ruleset using the Rulesets API.
  full_title: Delete a ruleset · Cloudflare Ruleset Engine docs
  head_html: <title>Delete a ruleset · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Delete a ruleset using the Rulesets API."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/index.md"><meta property="og:title" content="Delete a ruleset · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Delete a ruleset using the Rulesets API."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/#page","headline":"Delete a ruleset \u00b7 Cloudflare Ruleset Engine docs","description":"Delete a ruleset using the Rulesets API.","url":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rulesets-api/delete/
  schema: 1
---
<p>You can use the API to delete all the versions of a ruleset or delete a specific version of a ruleset.</p>
<ul>
<li><a href="#delete-ruleset">Delete ruleset (all versions)</a></li>
<li><a href="#delete-ruleset-version">Delete ruleset version</a></li>
</ul>
<h2 id="delete-ruleset">Delete ruleset</h2>
<p>Deletes all the versions of an existing ruleset at the account or zone level.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/methods/delete/">Delete an account ruleset</a><br/>
<code>DELETE /accounts/{account_id}/rulesets/{ruleset_id}</code></li>
<li><a href="/api/resources/rulesets/methods/delete/">Delete a zone ruleset</a><br/>
<code>DELETE /zones/{zone_id}/rulesets/{ruleset_id}</code></li>
</ul>
<p>If the delete operation succeeds, the API method call returns a <code>204 No Content</code> HTTP status code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13242.md")
</aside>
<h3 id="example">Example</h3>
<p>The following example request deletes an existing ruleset with ID <code>$RULESET_ID</code>.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="delete-ruleset-version">Delete ruleset version</h2>
<p>Deletes a specific version of a ruleset.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/versions/methods/delete/">Delete an account ruleset version</a><br/>
<code>DELETE /accounts/{account_id}/rulesets/{ruleset_id}/versions/{version_number}</code></li>
<li><a href="/api/resources/rulesets/subresources/versions/methods/delete/">Delete a zone ruleset version</a><br/>
<code>DELETE /zones/{zone_id}/rulesets/{ruleset_id}/versions/{version_number}</code></li>
</ul>
<p>If the delete operation succeeds, the method call returns a <code>204 No Content</code> HTTP status code.</p>
<p>Later updates to the ruleset will not reuse the version number of a deleted ruleset version.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13241.md")
</aside>
<h3 id="example-1">Example</h3>
<p>The following example request deletes a version of an existing ruleset.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
