---
cp9:
  canonical: https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/
  description: Create and configure Cloudflare rate limiting rules at the zone or account level using Terraform.
  full_title: Rate limiting rules configuration using Terraform · Cloudflare Terraform docs
  head_html: <title>Rate limiting rules configuration using Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and configure Cloudflare rate limiting rules at the zone or account level using Terraform."><link rel="canonical" href="https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/index.md"><meta property="og:title" content="Rate limiting rules configuration using Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and configure Cloudflare rate limiting rules at the zone or account level using Terraform."><meta property="og:url" content="https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/#page","headline":"Rate limiting rules configuration using Terraform \u00b7 Cloudflare Terraform docs","description":"Create and configure Cloudflare rate limiting rules at the zone or account level using Terraform.","url":"https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/additional-configurations/rate-limiting-rules/
  schema: 1
---
<p>This page provides examples of creating <a href="/waf/rate-limiting-rules/">rate limiting rules</a> in a zone or account using Terraform.</p>
<p>If you are using the Cloudflare API, refer to the following resources:</p>
<ul>
<li><a href="/waf/rate-limiting-rules/create-api/">Create a rate limiting rule via API</a></li>
<li><a href="/waf/account/rate-limiting-rulesets/create-api/">Create a rate limiting ruleset via API</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14829.md")
</aside>
<h2 id="before-you-start">Before you start</h2>
<h3 id="obtain-the-necessary-account-or-zone-ids">Obtain the necessary account or zone IDs</h3>
<p>The Terraform configurations provided in this page need the zone ID (or account ID) of the zone/account where you will deploy rulesets.</p>
<ul>
<li>To retrieve the list of accounts you have access to, including their IDs, use the <a href="/api/resources/accounts/methods/list/">List accounts</a> operation.</li>
<li>To retrieve the list of zones you have access to, including their IDs, use the <a href="/api/resources/zones/methods/list/">List zones</a> operation.</li>
</ul>
<h3 id="import-or-delete-existing-rulesets">Import or delete existing rulesets</h3>
<p>Terraform assumes that it has complete control over account and zone rulesets. If you already have rulesets configured in your account or zone, do one of the following:</p>
<ul>
<li><a href="/terraform/advanced-topics/import-cloudflare-resources/">Import existing rulesets to Terraform</a> using the <code>cf-terraforming</code> tool. Recent versions of the tool can generate resource definitions for existing rulesets and import their configuration to Terraform state.</li>
<li>Start from scratch by <a href="/ruleset-engine/rulesets-api/delete/#delete-ruleset">deleting existing rulesets</a> (account and zone rulesets with <code>&quot;kind&quot;: &quot;root&quot;</code> and <code>&quot;kind&quot;: &quot;zone&quot;</code>, respectively) and then defining your rulesets configuration in Terraform.</li>
</ul>
<hr />
<h2 id="create-a-rate-limiting-rule-at-the-zone-level">Create a rate limiting rule at the zone level</h2>
<p>This example creates a rate limiting rule in zone with ID <code>&lt;ZONE_ID&gt;</code> blocking traffic that exceeds the configured rate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14833.md")
</div></div>
<br />
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="use-a-single-ruleset-resource-per-phase">Use a single ruleset resource per phase</h3>
@markup("md", "content/.markup/bodies/14828.md")
</aside>
<h2 id="create-a-rate-limiting-rule-at-the-account-level">Create a rate limiting rule at the account level</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/14827.md")
</aside>
<p>This example defines a <a href="/ruleset-engine/custom-rulesets/">custom ruleset</a> with a single rate limiting rule in account with ID <code>&lt;ACCOUNT_ID&gt;</code> that blocks traffic for the <code>/api/</code> path exceeding the configured rate. The second <code>cloudflare_ruleset</code> resource defines an <code>execute</code> rule that deploys the custom ruleset for traffic addressed at <code>example.com</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14837.md")
</div></div>
<br />
<h2 id="create-an-advanced-rate-limiting-rule">Create an advanced rate limiting rule</h2>
<p>This example creates a rate limiting rule in zone with ID <code>&lt;ZONE_ID&gt;</code> with:</p>
<ul>
<li>A custom counting expression that includes a response field (<code>http.response.code</code>).</li>
<li>A custom JSON response for rate limited requests.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14841.md")
</div></div>
<br />
