---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/create-api/
  description: Create WAF custom rules using the Rulesets API.
  full_title: Create a custom rule via API for a zone · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Create a custom rule via API for a zone · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create WAF custom rules using the Rulesets API."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/create-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/create-api/index.md"><meta property="og:title" content="Create a custom rule via API for a zone · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create WAF custom rules using the Rulesets API."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/create-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/create-api/#page","headline":"Create a custom rule via API for a zone \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create WAF custom rules using the Rulesets API.","url":"https://developers.cloudflare.com/waf/custom-rules/create-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/create-api/
  schema: 1
---
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a custom rule via API at the zone level.</p>
<p>You must deploy custom rules to the <code>http_request_firewall_custom</code> <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">phase entry point ruleset</a>.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/waf-custom-rules/">WAF custom rules configuration using Terraform</a>.</p>
<h2 id="create-a-custom-rule">Create a custom rule</h2>
<p>To create a custom rule for a zone, add a rule  to the <code>http_request_firewall_custom</code> phase entry point ruleset.</p>
<ol>
<li>
<p>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation to obtain the definition of the entry point ruleset for the <code>http_request_firewall_custom</code> phase. You will need the <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a> for this task.</p>
</li>
<li>
<p>If the entry point ruleset already exists (that is, if you received a <code>200 OK</code> status code and the ruleset definition), take note of the ruleset ID in the response. Then, invoke the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add a custom rule to the existing ruleset. Refer to the examples below for details.</p>
</li>
<li>
<p>If the entry point ruleset does not exist (that is, if you received a <code>404 Not Found</code> status code in step 1), create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. Include your custom rule in the <code>rules</code> array. Refer to <a href="/ruleset-engine/rulesets-api/create/#example---create-a-zone-level-phase-entry-point-ruleset">Create ruleset</a> for an example.</p>
</li>
</ol>
<h3 id="example-a">Example A</h3>
<p>This example request adds a rule to the <code>http_request_firewall_custom</code> phase entry point ruleset for the zone with ID <code>$ZONE_ID</code>. The entry point ruleset already exists, with ID <code>$RULESET_ID</code>.</p>
<p>The new rule, which will be the last rule in the ruleset, will challenge requests from the United Kingdom or France with an <span class="nb-glossary-tooltip" title="attack score">attack score</span> lower than <code>20</code>.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;My custom rule&quot;,&#10;  &quot;expression&quot;: &quot;(ip.src.country eq \&quot;GB\&quot; or ip.src.country eq \&quot;FR\&quot;) and cf.waf.score lt 20&quot;,&#10;  &quot;action&quot;: &quot;challenge&quot;&#10;}&#x27;</code></pre>
<p>To define a specific position for the new rule, include a <code>position</code> object in the request body according to the guidelines in <a href="/ruleset-engine/rulesets-api/update-rule/#change-the-order-of-a-rule-in-a-ruleset">Change the order of a rule in a ruleset</a>.</p>
<p>For instructions on creating an entry point ruleset and defining its rules using a single API call, refer to <a href="/ruleset-engine/basic-operations/add-rule-phase-rulesets/">Add rules to phase entry point rulesets</a>.</p>
<h3 id="example-b">Example B</h3>
<p>This example request adds a rule to the <code>http_request_firewall_custom</code> phase entry point ruleset for the zone with ID <code>$ZONE_ID</code>. The entry point ruleset already exists, with ID <code>$RULESET_ID</code>.</p>
<p>The new rule, which will be the last rule in the ruleset, includes the definition of a <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">custom response</a> for blocked requests.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;My custom rule with plain text response&quot;,&#10;  &quot;expression&quot;: &quot;(ip.src.country eq \&quot;GB\&quot; or ip.src.country eq \&quot;FR\&quot;) and cf.waf.score lt 20&quot;,&#10;  &quot;action&quot;: &quot;block&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;response&quot;: {&#10;      &quot;status_code&quot;: 403,&#10;      &quot;content&quot;: &quot;Your request was blocked.&quot;,&#10;      &quot;content_type&quot;: &quot;text/plain&quot;&#10;    }&#10;  }&#10;}&#x27;</code></pre>
<p>To define a specific position for the new rule, include a <code>position</code> object in the request body according to the guidelines in <a href="/ruleset-engine/rulesets-api/update-rule/#change-the-order-of-a-rule-in-a-ruleset">Change the order of a rule in a ruleset</a>.</p>
<p>For instructions on creating an entry point ruleset and defining its rules using a single API call, refer to <a href="/ruleset-engine/basic-operations/add-rule-phase-rulesets/">Add rules to phase entry point rulesets</a>.</p>
<hr />
<h2 id="next-steps">Next steps</h2>
<p>Use the different operations in the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to work with the rule you just created. The following table has a list of common tasks:</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>Procedure</th>
</tr>
</thead>
<tbody>
<tr>
<td>List all rules in ruleset</td>
<td><p>Use the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation with the <code>http_request_firewall_custom</code> phase name to obtain the list of configured custom rules and their IDs.</p><p>For more information, refer to <a href="/ruleset-engine/rulesets-api/view/#view-a-specific-ruleset">View a specific ruleset</a>.</p></td>
</tr>
<tr>
<td>Update a rule</td>
<td><p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset rule</a> operation.</p><p>You will need to provide the ruleset ID and the rule ID. To obtain these IDs, you can use the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation with the <code>http_request_firewall_custom</code> phase name.</p><p>For more information, refer to <a href="/ruleset-engine/rulesets-api/update-rule/">Update a rule in a ruleset</a>.</p></td>
</tr>
<tr>
<td>Delete a rule</td>
<td><p>Use the <a href="/api/resources/rulesets/methods/delete/">Delete a zone ruleset rule</a> operation.</p><p>You will need to provide the ruleset ID and the rule ID. To obtain these IDs, you can use the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation with the <code>http_request_firewall_custom</code> phase name.</p><p>For more information, refer to <a href="/ruleset-engine/rulesets-api/delete-rule/">Delete a rule in a ruleset</a>.</p></td>
</tr>
</tbody>
</table>
<p>These operations are covered in the Ruleset Engine documentation. The Ruleset Engine powers different Cloudflare products, including custom rules.</p>
<h2 id="more-resources">More resources</h2>
<p>For instructions on deploying custom rules at the account level via API, refer to <a href="/waf/account/custom-rulesets/create-api/">Create a custom ruleset using the API</a>.</p>
