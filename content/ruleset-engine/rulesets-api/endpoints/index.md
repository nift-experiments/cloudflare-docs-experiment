---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/
  description: Available Rulesets API endpoints for zones and accounts.
  full_title: Endpoints · Cloudflare Ruleset Engine docs
  head_html: <title>Endpoints · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Available Rulesets API endpoints for zones and accounts."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/index.md"><meta property="og:title" content="Endpoints · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available Rulesets API endpoints for zones and accounts."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/#page","headline":"Endpoints \u00b7 Cloudflare Ruleset Engine docs","description":"Available Rulesets API endpoints for zones and accounts.","url":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rulesets-api/endpoints/
  schema: 1
---
<p>For some operations, you can use specific endpoints provided by the Rulesets API for managing phase entry point rulesets. These endpoints include the phase name in the endpoint instead of the ruleset ID.</p>
<p>For example, instead of using the following endpoint:</p>
<pre tabindex="0"><code class="language-txt">PUT /zones/{zone_id}/rulesets/{ruleset_id}&#10;</code></pre>
<p>You can use the following endpoint:</p>
<pre tabindex="0"><code class="language-txt">PUT /zones/{zone_id}/rulesets/phases/{phase_name}/entrypoint&#10;</code></pre>
<p>To invoke a Rulesets API operation, append the endpoint to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>For authentication instructions, refer to <a href="/fundamentals/api/">Getting Started: Requests</a> in the Cloudflare API documentation.</p>
<p>For help with endpoints and pagination, refer to <a href="/fundamentals/api/">Getting Started: Endpoints</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13240.md")
</aside>
<p>The Cloudflare Rulesets API supports the operations outlined below. Visit the associated links for API endpoints and examples.</p>
<h2 id="list-and-view-rulesets">List and view rulesets</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method</th>
<th>Notes</th>
</tr>
</thead>
<tbody style="vertical-align:top">
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/view/#list-existing-rulesets">List existing rulesets</a>
</td>
<td>
        <code>GET</code>
</td>
<td>
        <p>Returns the list of existing rulesets at the account level or at the zone level.</p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/view/#view-a-specific-ruleset">View a specific ruleset</a>
</td>
<td>
        <code>GET</code>
</td>
<td>
        <p>Returns the properties of the most recent version of a specific ruleset.</p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/view/#list-all-versions-of-a-ruleset">
          List all versions of a ruleset
        </a>
</td>
<td>
        <code>GET</code>
</td>
<td>
        <p>Returns a list of all the versions of a ruleset.</p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/view/#view-a-specific-version-of-a-ruleset">
          View a specific version of a ruleset
        </a>
</td>
<td>
        <code>GET</code>
</td>
<td>
        <p>Returns the configuration of a specific version of a ruleset, including its rules.</p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/view/#list-rules-in-a-managed-ruleset-with-a-specific-tag">
          List rules in a managed ruleset with a specific tag
        </a>
</td>
<td>
        <code>GET</code>
</td>
<td>
        <p>Returns a list of all the rules in a managed ruleset with a specific tag.</p>
</td>
</tr>
</tbody>
</table>
<h2 id="create-rulesets">Create rulesets</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb</th>
<th>Notes</th>
</tr>
</thead>
<tbody style="vertical-align:top">
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/create/">Create a ruleset</a>
</td>
<td>
        <code>POST</code>
</td>
<td>
        <p>Creates a new ruleset or a new phase entry point.</p>
</td>
</tr>
</tbody>
</table>
<h2 id="update-and-deploy-rulesets">Update and deploy rulesets</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb</th>
<th>Notes</th>
</tr>
</thead>
<tbody style="vertical-align:top">
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/update/">Update or deploy a ruleset</a>
</td>
<td>
        <code>PUT</code>
</td>
<td>
        <p>
          Updates the basic properties of a ruleset and the list of rules in the ruleset.
<br />
          Allows you to configure the execution of managed rulesets.
        </p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/add-rule/">Add a rule to a ruleset</a>
</td>
<td>
        <code>POST</code>
</td>
<td>
        <p>
          Adds a single rule to an existing ruleset.
<br />
          Allows you to add a single rule without having to include all the existing ruleset rules
          in the request.
        </p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/update-rule/">Update a rule in a ruleset</a>
</td>
<td>
        <code>PATCH</code>
</td>
<td>
        <p>
          Updates the definition of a single rule within a ruleset.
<br />
          Allows you to change the order of a rule in a ruleset.
        </p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/delete-rule/">Delete a rule in a ruleset</a>
</td>
<td>
        <code>DELETE</code>
</td>
<td>
        <p>Deletes a single rule in a ruleset.</p>
</td>
</tr>
</tbody>
</table>
<h2 id="delete-rulesets">Delete rulesets</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb</th>
<th>Notes</th>
</tr>
</thead>
<tbody style="vertical-align:top">
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/delete/#delete-ruleset">Delete a ruleset</a>
</td>
<td>
        <code>DELETE</code>
</td>
<td>
        <p>Deletes all the versions of a ruleset.</p>
</td>
</tr>
<tr>
<td>
        <a href="/ruleset-engine/rulesets-api/delete/#delete-ruleset-version">Delete a ruleset version</a>
</td>
<td>
        <code>DELETE</code>
</td>
<td>
        <p>Deletes a specific version of a ruleset.</p>
</td>
</tr>
</tbody>
</table>
