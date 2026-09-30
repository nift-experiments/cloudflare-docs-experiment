---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/create-rules/
  description: Create custom error rules in the dashboard or via the API.
  full_title: Create custom error rules · Cloudflare Rules docs
  head_html: <title>Create custom error rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom error rules in the dashboard or via the API."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/create-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/create-rules/index.md"><meta property="og:title" content="Create custom error rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom error rules in the dashboard or via the API."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/create-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/create-rules/#page","headline":"Create custom error rules \u00b7 Cloudflare Rules docs","description":"Create custom error rules in the dashboard or via the API.","url":"https://developers.cloudflare.com/rules/custom-errors/create-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/create-rules/
  schema: 1
---
<h2 id="in-the-dashboard">In the dashboard</h2>
<h3 id="create-a-custom-error-rule-create-a-custom-error-rule-dashboard">Create a custom error rule </h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12998.md")
</div>
<h3 id="create-a-custom-error-asset-create-a-custom-error-asset-dashboard">Create a custom error asset </h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12999.md")
</div>
<p>To review existing custom error assets, go to <strong>Rules</strong> &gt; <strong>Settings</strong> &gt; <strong>Custom Error Assets</strong> tab.</p>
<h2 id="via-api">Via API</h2>
<p>To configure a custom error rule via API:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13000.md")
</div>
<h3 id="create-a-custom-error-asset-create-a-custom-error-asset-api">Create a custom error asset </h3>
<p>The following <code>POST</code> request creates new a custom error asset in a zone based on the provided URL:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-json &#x27;{&#10;  &quot;name&quot;: &quot;500_error_template&quot;,&#10;  &quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/errors/500_template.html&quot;&#10;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;name&quot;: &quot;500_error_template&quot;,&#10;		&quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;		&quot;url&quot;: &quot;https://example.com/errors/500_template.html&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-02-10T11:36:07.810215Z&quot;,&#10;		&quot;size_bytes&quot;: 2048&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<h3 id="create-a-custom-error-rule-create-a-custom-error-rule-api">Create a custom error rule </h3>
<p>When creating a custom error rule via API, make sure you:</p>
<ul>
<li>Set the rule action to <code>serve_error</code>.</li>
<li>Define the <a href="/rules/custom-errors/reference/parameters/#custom-error-rules">rule parameters</a> in the <code>action_parameters</code> field according to response type.</li>
<li>Deploy the rule to the <code>http_custom_errors</code> phase.</li>
</ul>
<p>The first rule in the <code>http_custom_errors</code> phase ruleset that matches will be applied. No other rules in the ruleset will be matched or applied. Additionally, custom error rules defined at the zone level will have priority over rules defined at the account level.</p>
<h4 id="general-procedure">General procedure</h4>
<p>Follow this workflow to create a custom error rule for a given zone via API:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13001.md")
</div>
<p>To create a custom error rule at the account level, use the corresponding account-level API endpoints.</p>
<h4 id="example">Example</h4>
<p>This example configures a custom error rule returning a <a href="#create-a-custom-error-asset-api">previously created custom error asset</a> named <code>500_error_template</code> for responses with a <code>500</code> HTTP status code.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;ref&quot;: &quot;serve_500_template&quot;,&#10;      &quot;action&quot;: &quot;serve_error&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;asset_name&quot;: &quot;500_error_template&quot;,&#10;        &quot;content_type&quot;: &quot;text/html&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;http.response.code eq 500&quot;,&#10;      &quot;enabled&quot;: true&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a> in the Terraform documentation.</p>
<p>This <code>PUT</code> request, corresponding to the <a href="/api/resources/rulesets/subresources/phases/methods/update/">Update a zone entry point ruleset</a> operation, replaces any existing rules in the <code>http_custom_errors</code> phase entry point ruleset.</p>
<h3 id="required-api-token-permissions">Required API token permissions</h3>
<p>The API token used in API requests to manage Custom Error Rules and Custom Error Assets must have at least the following permission:</p>
<ul>
<li><em>Custom Error Rules</em> &gt; <em>Edit</em></li>
</ul>
