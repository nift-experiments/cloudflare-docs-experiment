---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/
  description: Deploy the Cloudflare Managed Ruleset with only Joomla rules enabled.
  full_title: Use category overrides to enable Joomla rules · Cloudflare Ruleset Engine docs
  head_html: <title>Use category overrides to enable Joomla rules · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy the Cloudflare Managed Ruleset with only Joomla rules enabled."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/index.md"><meta property="og:title" content="Use category overrides to enable Joomla rules · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy the Cloudflare Managed Ruleset with only Joomla rules enabled."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/#page","headline":"Use category overrides to enable Joomla rules \u00b7 Cloudflare Ruleset Engine docs","description":"Deploy the Cloudflare Managed Ruleset with only Joomla rules enabled.","url":"https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/
  schema: 1
---
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to configure the execution of a managed ruleset and override its behavior. By default, enabled rules perform the actions defined by the managed ruleset issuer. This example uses overrides to ensure that only rules with a specific tag are enabled.</p>
<p>Follow the steps below to configure the execution of a managed ruleset with two overrides for enabling only the rules tagged with <code>joomla</code>.</p>
<ol>
<li><a href="/ruleset-engine/basic-operations/deploy-rulesets/">Add a rule</a> to a phase entry point ruleset that executes a managed ruleset.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a ruleset override</a> that disables all rules in the managed ruleset.</li>
<li>Configure a tag override that enables only the rules with a given tag.</li>
</ol>
<p>Tag overrides take precedence over ruleset overrides. Only the rules with the specified tag are enabled, and all other rules are disabled.</p>
<h2 id="example-1">Example 1</h2>
<p>This example deploys the Cloudflare Managed Ruleset to a phase with only Joomla rules enabled. The <code>name</code>, <code>kind</code>, and <code>phase</code> fields are omitted from the request because they are immutable.</p>
<details class="nb-details"><summary>Example: Enable only Joomla rules using category overrides at the zone level</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13296.md")
</div></details>
<details class="nb-details"><summary>Example: Enable only Joomla rules using category overrides at the account level</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13297.md")
</div></details>
<p>You can add more than one category override to a rule.</p>
<h2 id="example-2">Example 2</h2>
<p>This example adds two overrides to the rule that executes a managed ruleset (<code>&lt;MANAGED_RULESET_ID&gt;</code>) in the <code>http_request_firewall_managed</code> phase. Note that the <code>name</code>, <code>kind</code>, and <code>phase</code> fields are omitted from the request because they are immutable.</p>
<details class="nb-details"><summary>Example: Add more than one category override at the zone level</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13298.md")
</div></details>
<details class="nb-details"><summary>Example: Add more than one category override at the account level</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13299.md")
</div></details>
<p>The order of the overrides in the ruleset determines if rules in the deployed managed ruleset are enabled or disabled. Overrides placed later in the list take precedence over earlier overrides.</p>
<p>Consider four rules from the managed ruleset in the code above that have different combinations of <code>category</code> tags. The following table shows the status of the rules after the overrides.</p>
<table>
<thead>
<tr>
<th>Rule in managed ruleset</th>
<th>Tags</th>
<th>Rule status after overrides</th>
</tr>
</thead>
<tbody>
<tr>
<td>ManagedRule1</td>
<td><code>drupal</code>, <code>dos</code></td>
<td>Disabled</td>
</tr>
<tr>
<td>ManagedRule2</td>
<td><code>drupal</code>, <code>dos</code>, <code>joomla</code></td>
<td>Enabled</td>
</tr>
<tr>
<td>ManagedRule3</td>
<td><code>dos</code>, <code>joomla</code>, <code>wordpress</code></td>
<td>Disabled</td>
</tr>
<tr>
<td>ManagedRule4</td>
<td><code>drupal</code>, <code>wordpress</code></td>
<td>Disabled</td>
</tr>
<tr>
<td>ManagedRule5</td>
<td>(no tags)</td>
<td>Disabled</td>
</tr>
</tbody>
</table>
