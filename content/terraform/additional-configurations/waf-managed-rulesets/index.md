---
cp9:
  canonical: https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/
  description: Deploy and configure Cloudflare WAF Managed Rules at the zone or account level using Terraform.
  full_title: WAF Managed Rules configuration using Terraform · Cloudflare Terraform docs
  head_html: <title>WAF Managed Rules configuration using Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy and configure Cloudflare WAF Managed Rules at the zone or account level using Terraform."><link rel="canonical" href="https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/index.md"><meta property="og:title" content="WAF Managed Rules configuration using Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy and configure Cloudflare WAF Managed Rules at the zone or account level using Terraform."><meta property="og:url" content="https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform,WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/#page","headline":"WAF Managed Rules configuration using Terraform \u00b7 Cloudflare Terraform docs","description":"Deploy and configure Cloudflare WAF Managed Rules at the zone or account level using Terraform.","url":"https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/additional-configurations/waf-managed-rulesets/
  schema: 1
---
<p>This page provides examples of deploying and configuring <a href="/waf/managed-rules/">WAF Managed Rules</a> in your zone or account using Terraform. It covers the following configurations:</p>
<ul>
<li><a href="#deploy-managed-rulesets-at-the-zone-level">Deploy managed rulesets at the zone level</a></li>
<li><a href="#deploy-managed-rulesets-at-the-account-level">Deploy managed rulesets at the account level</a></li>
<li><a href="#configure-exceptions">Configure exceptions</a></li>
<li><a href="#configure-payload-logging">Configure payload logging</a></li>
<li><a href="#configure-overrides">Configure overrides</a></li>
<li><a href="#configure-the-owasp-paranoia-level-score-threshold-and-action">Configure the OWASP paranoia level, score threshold, and action</a></li>
</ul>
<p>If you are using the Cloudflare API, refer to the following resources:</p>
<ul>
<li><a href="/waf/managed-rules/deploy-api/">Deploy a WAF managed ruleset via API</a></li>
<li><a href="/waf/account/managed-rulesets/deploy-api/">Deploy a WAF managed ruleset via API (account)</a></li>
</ul>
<p>For more information on deploying and configuring managed rulesets using the Rulesets API, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a> in the Ruleset Engine documentation.</p>
<h2 id="before-you-start">Before you start</h2>
<h3 id="obtain-the-necessary-account-zone-and-managed-ruleset-ids">Obtain the necessary account, zone, and managed ruleset IDs</h3>
<p>The Terraform configurations provided in this page need the zone ID (or account ID) of the zone/account where you will deploy the managed rulesets.</p>
<ul>
<li>To retrieve the list of accounts you have access to, including their IDs, use the <a href="/api/resources/accounts/methods/list/">List accounts</a> operation.</li>
<li>To retrieve the list of zones you have access to, including their IDs, use the <a href="/api/resources/zones/methods/list/">List zones</a> operation.</li>
</ul>
<p>The deployment of managed rulesets via Terraform requires that you use the ruleset IDs. To find the IDs of managed rulesets, use the <a href="/api/resources/rulesets/methods/list/">List account rulesets</a> operation. The response will include the description and IDs of existing managed rulesets.</p>
<p>The IDs of WAF managed rulesets are also available in the <a href="/waf/managed-rules/#available-managed-rulesets">WAF Managed Rules</a> page.</p>
<h3 id="import-or-delete-existing-rulesets">Import or delete existing rulesets</h3>
<p>Terraform assumes that it has complete control over account and zone rulesets. If you already have rulesets configured in your account or zone, do one of the following:</p>
<ul>
<li><a href="/terraform/advanced-topics/import-cloudflare-resources/">Import existing rulesets to Terraform</a> using the <code>cf-terraforming</code> tool. Recent versions of the tool can generate resource definitions for existing rulesets and import their configuration to Terraform state.</li>
<li>Start from scratch by <a href="/ruleset-engine/rulesets-api/delete/#delete-ruleset">deleting existing rulesets</a> (account and zone rulesets with <code>&quot;kind&quot;: &quot;root&quot;</code> and <code>&quot;kind&quot;: &quot;zone&quot;</code>, respectively) and then defining your rulesets configuration in Terraform.</li>
</ul>
<hr />
<h2 id="deploy-managed-rulesets-at-the-zone-level">Deploy managed rulesets at the zone level</h2>
<p>The following example deploys two managed rulesets to the zone with ID <code>&lt;ZONE_ID&gt;</code> using Terraform, using a <code>cloudflare_ruleset</code> resource with two rules that execute the managed rulesets.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14781.md")
</div></div>
<h2 id="deploy-managed-rulesets-at-the-account-level">Deploy managed rulesets at the account level</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/14777.md")
</aside>
<p>The following example deploys two managed rulesets to the account with ID <code>&lt;ACCOUNT_ID&gt;</code> using Terraform, using a <code>cloudflare_ruleset</code> resource with two rules that execute the managed rulesets for two hostnames belonging to Enterprise zones.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14785.md")
</div></div>
<h2 id="configure-exceptions">Configure exceptions</h2>
<p>The following example adds two <a href="/waf/managed-rules/waf-exceptions/">exceptions</a> for the Cloudflare Managed Ruleset:</p>
<ul>
<li>The first rule will skip the execution of the entire Cloudflare Managed Ruleset (with ID <code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code>) for specific URLs, according to the rule expression.</li>
<li>The second rule will skip the execution of two rules belonging to the Cloudflare Managed Ruleset for specific URLs, according to the rule expression.</li>
</ul>
<p>Add the two exceptions to the <code>cloudflare_ruleset</code> resource before the rule that deploys the Cloudflare Managed Ruleset:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14788.md")
</div></div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/14776.md")
</aside>
<h2 id="configure-overrides">Configure overrides</h2>
<p>The following example adds three <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> for the Cloudflare Managed Ruleset:</p>
<ul>
<li>A rule override for rule with ID <code>5de7edfa648c4d6891dc3e7f84534ffa</code> setting the action to <code>log</code>.</li>
<li>A rule override for rule with ID <code>75a0060762034a6cb663fd51a02344cb</code> disabling the rule.</li>
<li>A tag override for the <code>wordpress</code> tag, setting the action of all the rules with this tag to <code>js_challenge</code>.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-1">Important</h3>
@markup("md", "content/.markup/bodies/14775.md")
</aside>
<p>The following configuration includes the three overrides in the rule that executes the Cloudflare Managed Ruleset:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14791.md")
</div></div>
<h2 id="configure-payload-logging">Configure payload logging</h2>
<p>This example enables <a href="/waf/managed-rules/payload-logging/">payload logging</a> for matched rules of the Cloudflare Managed Ruleset, setting the public key used to encrypt the logged payload.</p>
<p>Building upon the rule that deploys the Cloudflare Managed Ruleset, the following rule configuration adds the <code>matched_data</code> object with the public key used to encrypt the payload:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14794.md")
</div></div>
<h2 id="configure-the-owasp-paranoia-level-score-threshold-and-action">Configure the OWASP paranoia level, score threshold, and action</h2>
<p>The OWASP managed ruleset supports the following configurations:</p>
<ul>
<li>
<p>Enable all the rules up to a specific paranoia level by creating tag overrides that disable all the rules associated with higher paranoia levels.</p>
</li>
<li>
<p>Set the action to perform when the calculated threat score is greater than the score threshold by creating a rule override for the last rule in the Cloudflare OWASP Core Ruleset (rule with ID <code class="nb-rule-id" title="6179ae15870a4bb7b2d480d4843b323c">843b323c</code>), and including the <code>action</code> property.</p>
</li>
<li>
<p>Set the score threshold by creating a rule override for the last rule in the Cloudflare OWASP Core Ruleset (rule with ID <code class="nb-rule-id" title="6179ae15870a4bb7b2d480d4843b323c">843b323c</code>), and including the <code>score_threshold</code> property.</p>
</li>
</ul>
<p>For more information on the available configuration values, refer to the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a> page in the WAF documentation.</p>
<p>The following example rule of a <code>cloudflare_ruleset</code> Terraform resource performs the following configuration:</p>
<ul>
<li>Deploys the OWASP managed ruleset.</li>
<li>Sets the OWASP paranoia level to <em>PL2</em>.</li>
<li>Sets the score threshold to <code>60</code> (<em>Low</em>).</li>
<li>Sets the ruleset action to <code>log</code>.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14797.md")
</div></div>
