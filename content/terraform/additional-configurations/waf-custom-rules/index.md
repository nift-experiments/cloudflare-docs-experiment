---
cp9:
  canonical: https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/
  description: Create and deploy Cloudflare WAF custom rules at the zone or account level using Terraform.
  full_title: WAF custom rules configuration using Terraform · Cloudflare Terraform docs
  head_html: <title>WAF custom rules configuration using Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and deploy Cloudflare WAF custom rules at the zone or account level using Terraform."><link rel="canonical" href="https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/index.md"><meta property="og:title" content="WAF custom rules configuration using Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and deploy Cloudflare WAF custom rules at the zone or account level using Terraform."><meta property="og:url" content="https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform,WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/#page","headline":"WAF custom rules configuration using Terraform \u00b7 Cloudflare Terraform docs","description":"Create and deploy Cloudflare WAF custom rules at the zone or account level using Terraform.","url":"https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/additional-configurations/waf-custom-rules/
  schema: 1
---
<p>This page provides examples of creating <a href="/waf/custom-rules/">WAF custom rules</a> in a zone or account using Terraform. The examples cover the following scenarios:</p>
<ul>
<li><a href="#add-a-custom-rule-to-a-zone">Add a custom rule to a zone</a></li>
<li><a href="#create-and-deploy-a-custom-ruleset">Create and deploy a custom ruleset</a></li>
</ul>
<p>The WAF documentation includes additional Terraform examples — refer to <a href="#more-resources">More resources</a>.</p>
<p>If you are using the Cloudflare API, refer to the following resources in the WAF documentation:</p>
<ul>
<li><a href="/waf/custom-rules/create-api/">Create a custom rule via API</a></li>
<li><a href="/waf/account/custom-rulesets/create-api/">Create a custom ruleset using the API</a></li>
</ul>
<p>For more information on deploying and configuring custom rulesets using the Rulesets API, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> in the Ruleset Engine documentation.</p>
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
<h2 id="add-a-custom-rule-to-a-zone">Add a custom rule to a zone</h2>
<p>The following example configures a custom rule in the zone entry point ruleset for the <code>http_request_firewall_custom</code> phase for zone with ID <code>&lt;ZONE_ID&gt;</code>. The rule will block all traffic on non-standard HTTP(S) ports:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14802.md")
</div></div>
<br />
<h2 id="create-and-deploy-a-custom-ruleset">Create and deploy a custom ruleset</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14798.md")
</aside>
<p>The following example creates a <a href="/ruleset-engine/custom-rulesets/">custom ruleset</a> in the account with ID <code>&lt;ACCOUNT_ID&gt;</code> containing a single custom rule. This custom ruleset is then deployed using a separate <code>cloudflare_ruleset</code> Terraform resource. If you do not deploy a custom ruleset, it will not execute.</p>
<p>The following configuration creates a custom ruleset with a single rule:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14806.md")
</div></div>
<br />
<p>The following configuration deploys the custom ruleset at the account level. It defines a dependency on the <code>account_firewall_custom_ruleset</code> resource and uses the ID of the created custom ruleset in <code>action_parameters</code>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14810.md")
</div></div>
<p>For more information on configuring and deploying custom rulesets, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> in the Ruleset Engine documentation.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/waf/detections/malicious-uploads/terraform-examples/#add-a-custom-rule-to-block-malicious-uploads">Malicious uploads detection: Add a custom rule to block malicious uploads</a></li>
<li><a href="/waf/detections/leaked-credentials/terraform-examples/#add-a-custom-rule-to-challenge-requests-with-leaked-credentials">Leaked credentials detection: Add a custom rule to challenge requests with leaked credentials</a></li>
</ul>
