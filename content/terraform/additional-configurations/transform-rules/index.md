---
cp9:
  canonical: https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/
  description: Create URL rewrites, request header, and response header Transform Rules using Terraform.
  full_title: Transform Rules configuration using Terraform · Cloudflare Terraform docs
  head_html: <title>Transform Rules configuration using Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Create URL rewrites, request header, and response header Transform Rules using Terraform."><link rel="canonical" href="https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/index.md"><meta property="og:title" content="Transform Rules configuration using Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create URL rewrites, request header, and response header Transform Rules using Terraform."><meta property="og:url" content="https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/#page","headline":"Transform Rules configuration using Terraform \u00b7 Cloudflare Terraform docs","description":"Create URL rewrites, request header, and response header Transform Rules using Terraform.","url":"https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/additional-configurations/transform-rules/
  schema: 1
---
<p>This page provides examples of creating <a href="/rules/transform/">Transform Rules</a> in a zone using Terraform. The examples cover the following scenarios:</p>
<ul>
<li><a href="#create-a-url-rewrite-rule">Create a URL rewrite rule</a></li>
<li><a href="#create-a-request-header-transform-rule">Create a request header transform rule</a></li>
<li><a href="#create-a-response-header-transform-rule">Create a response header transform rule</a></li>
<li><a href="#configure-managed-transforms">Configure Managed Transforms</a></li>
</ul>
<p>If you are using the Cloudflare API, refer to the following resources:</p>
<ul>
<li><a href="/rules/transform/url-rewrite/create-api/">Create a URL rewrite rule via API</a></li>
<li><a href="/rules/transform/request-header-modification/create-api/">Create a request header transform rule via API</a></li>
<li><a href="/rules/transform/response-header-modification/create-api/">Create a response header transform rule via API</a></li>
<li><a href="/rules/transform/managed-transforms/configure/">Configure Managed Transforms</a></li>
</ul>
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
<h2 id="create-a-url-rewrite-rule">Create a URL rewrite rule</h2>
<p>The following example creates a URL rewrite rule that rewrites requests for <code>example.com/old-folder</code> to <code>example.com/new-folder</code>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14814.md")
</div></div>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a>.</p>
<br />
<p>For more information on rewriting URLs, refer to <a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a>.</p>
<h2 id="create-a-request-header-transform-rule">Create a request header transform rule</h2>
<p>The following configuration example performs the following adjustments to HTTP request headers:</p>
<ul>
<li>Adds a <code>my-header-1</code> header to the request with a static value.</li>
<li>Adds a <code>my-header-2</code> header to the request with a dynamic value defined by an expression.</li>
<li>Deletes the <code>existing-header</code> header from the request, if it exists.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14818.md")
</div></div>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a>.</p>
<p>For more information on modifying request headers, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>.</p>
<h2 id="create-a-response-header-transform-rule">Create a response header transform rule</h2>
<p>The following configuration example performs the following adjustments to HTTP response headers:</p>
<ul>
<li>Adds a <code>my-header-1</code> header to the response with a static value.</li>
<li>Adds a <code>my-header-2</code> header to the response with a dynamic value defined by an expression.</li>
<li>Deletes the <code>existing-header</code> header from the response, if it exists.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14822.md")
</div></div>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a>.</p>
<p>For more information on modifying response headers, refer to <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a>.</p>
<h2 id="configure-managed-transforms">Configure Managed Transforms</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14826.md")
</div></div>
<p>Make sure you include the Managed Transforms you are updating in the correct object (<code>managed_request_headers</code> or <code>managed_response_headers</code>).</p>
<p>For more information on Managed Transforms, refer to <a href="/rules/transform/managed-transforms/">Managed Transforms</a>.</p>
