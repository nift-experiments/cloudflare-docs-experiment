---
cp9:
  canonical: https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/
  description: Upgrade deprecated Firewall Rules to WAF custom rules.
  full_title: Firewall rules upgrade · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Firewall rules upgrade · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Upgrade deprecated Firewall Rules to WAF custom rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/index.md"><meta property="og:title" content="Firewall rules upgrade · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upgrade deprecated Firewall Rules to WAF custom rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/#page","headline":"Firewall rules upgrade \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Upgrade deprecated Firewall Rules to WAF custom rules.","url":"https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/reference/legacy/firewall-rules-upgrade/
  schema: 1
---
<p>Cloudflare upgraded existing <a href="/firewall/">firewall rules</a> into <a href="/waf/custom-rules/">custom rules</a>. With custom rules, you get the same level of protection and a few additional features. Custom rules are available in the Cloudflare dashboard in the following location:</p>
<ul>
<li>Old dashboard: <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Custom rules</strong>.</li>
<li>New security dashboard: <strong>Security</strong> &gt; <strong>Security rules</strong>.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15677.md")
</aside>
<h2 id="main-differences">Main differences</h2>
<p>The main differences between firewall rules and WAF custom rules are the following:</p>
<ul>
<li><a href="#improved-response-for-block-action">Improved response for Block action</a></li>
<li><a href="#different-error-page-for-blocked-requests">Different error page for blocked requests</a></li>
<li><a href="#new-skip-action-replacing-both-allow-and-bypass-actions">New Skip action replacing both Allow and Bypass actions</a></li>
<li><a href="#custom-rules-are-evaluated-in-order">Custom rules are evaluated in order</a></li>
<li><a href="#logs-and-events">Logs and events</a></li>
<li><a href="#new-api-and-terraform-resources">New API and Terraform resources</a></li>
</ul>
<h3 id="improved-response-for-block-action">Improved response for Block action</h3>
<p>In WAF custom rules you can <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">customize the response of the <em>Block</em> action</a>.</p>
<p>The default block response is a Cloudflare standard HTML page. If you need to send a custom response for <em>Block</em> actions, configure the custom rule to return a fixed response with a custom response code (403, by default) and a custom body (HTML, JSON, XML, or plain text).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15676.md")
</aside>
<h3 id="different-error-page-for-blocked-requests">Different error page for blocked requests</h3>
<p>Requests blocked by a firewall rule with a <em>Block</em> action would get a Cloudflare <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/">1020 error code</a> response. Cloudflare users could customize this error page for a zone in <strong>Error Pages</strong> &gt; <strong>1000 class errors</strong>.</p>
<p>Requests blocked by a WAF custom rule will get a different response: the WAF block response. To customize the default block response, you can either:</p>
<ul>
<li>Define a custom WAF block response for your entire zone in <a href="https://dash.cloudflare.com/?to=/:account/:zone/error-pages"><strong>Error Pages</strong></a> &gt; <strong>WAF block</strong>. This error page will always have an HTML content type.</li>
<li><a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">Define a custom response</a> for requests blocked by a specific WAF custom rule. This custom response supports other content types besides HTML.</li>
</ul>
<p>If you have customized your 1XXX error page in Error Pages for requests blocked by firewall rules, you will need to create a new response page for blocked requests using one of the above methods.</p>
<p>For more information on Error Pages, refer to <a href="/rules/custom-errors/">Custom Errors</a>.</p>
<h3 id="new-skip-action-replacing-both-allow-and-bypass-actions">New Skip action replacing both Allow and Bypass actions</h3>
<p>Firewall Rules supported the <em>Allow</em> and <em>Bypass</em> actions, often used together. These actions were commonly used for handling known legitimate requests — for example, requests coming from trusted IP addresses.</p>
<p>When a request triggered <em>Allow</em>, all remaining firewall rules were not evaluated, effectively allowing the request to continue to the next security product. The <em>Bypass</em> action was designed to specify which security products (such as WAF managed rules, rate limiting rules, and User Agent Blocking) should not run on the request triggering the action.</p>
<p>With Firewall Rules, if you wanted to stop running all security products for a given request, you would create two rules:</p>
<ul>
<li>One rule with <em>Bypass</em> action (selecting all security products).</li>
<li>One rule with <em>Allow</em> action (to stop executing other firewall rules).</li>
</ul>
<p>The requirement of having two rules to address this common scenario no longer applies to WAF custom rules. You should now <a href="/waf/custom-rules/skip/">use the <em>Skip</em> action</a>, which combines the <em>Allow</em> and <em>Bypass</em> actions. The <em>Skip</em> action fully replaces the <em>Allow</em> and <em>Bypass</em> actions, which are not supported in WAF custom rules.</p>
<p>With the <em>Skip</em> action you can do the following:</p>
<ul>
<li>Stop running all the remaining custom rules (equivalent to the <em>Allow</em> action)</li>
<li>Avoid running other security products (equivalent to the <em>Bypass</em> action)</li>
<li>A combination of the above.</li>
</ul>
<p>You can also select whether you want to log events matching the custom rule with the <em>Skip</em> action or not. This is especially useful when creating a positive security model to avoid logging large amounts of legitimate traffic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15675.md")
</aside>
<h3 id="custom-rules-are-evaluated-in-order">Custom rules are evaluated in order</h3>
<p>Firewall rules actions had a specific <a href="/firewall/cf-firewall-rules/actions/">order of precedence</a> when using <a href="/firewall/cf-firewall-rules/order-priority/#managing-rule-evaluation-by-priority-order">priority ordering</a>. In contrast, custom rules actions do not have such an order. Custom rules are always evaluated in order, and some actions like <em>Block</em> will stop the evaluation of other rules.</p>
<p>For example, if you were using priority ordering and had the following firewall rules with the same priority both matching an incoming request:</p>
<ul>
<li>Firewall rule #1 — Priority: 2 / Action: <em>Block</em></li>
<li>Firewall rule #2 — Priority: 2 / Action: <em>Allow</em></li>
</ul>
<p>The request would be allowed, since the <em>Allow</em> action in Firewall Rules would have precedence over the <em>Block</em> action.</p>
<p>In contrast, if you create two custom rules where both rules match an incoming request:</p>
<ul>
<li>Custom rule #1 — Action: <em>Block</em></li>
<li>Custom rule #2 — Action: <em>Skip</em> (configured to skip all remaining custom rules)</li>
</ul>
<p>The request would be blocked, since custom rules are evaluated in order and the <em>Block</em> action will stop the evaluation of other rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15674.md")
</aside>
<h3 id="logs-and-events">Logs and events</h3>
<p>Events logged by custom rules are shown in <a href="/waf/analytics/security-events/">Security Events</a> with <code>Custom Rules</code> as their source.</p>
<p>You may still find events generated by Firewall Rules in the Security Events page when you select a time frame including the days when the transition to custom rules occurred. Similarly, you may still find events with both <em>Skip</em> and <em>Allow</em> actions in the same view during the transition period.</p>
<h3 id="new-api-and-terraform-resources">New API and Terraform resources</h3>
<p>The preferred API for managing WAF custom rules is the <a href="/waf/custom-rules/create-api/">Rulesets API</a>. The Rulesets API is used on all recent Cloudflare security products to provide a uniform user experience when interacting with our API. For more information on migrating to the Rulesets API, refer to <a href="#relevant-changes-for-api-users">Relevant changes for API users</a>.</p>
<p>The Firewall Rules API and Filters API are no longer supported since 2025-06-15. There is now a single list of rules for both firewall rules and WAF custom rules, and this list contains WAF custom rules. Thanks to an internal conversion process, the Firewall Rules API and Filters API return firewall rules/filters converted from these WAF custom rules until the APIs sunset date.</p>
<p>If you are using Terraform, you must update your configuration to use <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> resources with the <code>http_request_firewall_custom</code> phase to manage custom rules. For more information on updating your Terraform configuration, refer to <a href="#relevant-changes-for-terraform-users">Relevant changes for Terraform users</a>.</p>
<h2 id="relevant-changes-for-dashboard-users">Relevant changes for dashboard users</h2>
<p><strong>The Firewall Rules tab in the Cloudflare dashboard is now deprecated</strong>. Firewall rules are displayed as <a href="/waf/custom-rules/">custom rules</a> in the Cloudflare dashboard.</p>
<p>For users that have access to both products, the <strong>Firewall rules</strong> tab is only available in the old dashboard in <strong>Security</strong> &gt; <strong>WAF</strong>.</p>
<h2 id="relevant-changes-for-api-users">Relevant changes for API users</h2>
<p><strong>The <a href="/firewall/api/cf-firewall-rules/">Firewall Rules API</a> and the associated <a href="/firewall/api/cf-filters/">Cloudflare Filters API</a> are now deprecated.</strong> These APIs are no longer supported since 2025-06-15. You must manually update any automation based on the Firewall Rules API or Cloudflare Filters API to the <a href="/waf/custom-rules/create-api/">Rulesets API</a> to prevent any issues. Rule IDs are different between firewall rules and custom rules, which may affect automated processes dealing with specific rule IDs.</p>
<p>Before the APIs sunset date, Cloudflare will internally convert your <a href="/firewall/api/cf-firewall-rules/">Firewall Rules API</a> and <a href="/firewall/api/cf-filters/">Filters API</a> calls into the corresponding <a href="/waf/custom-rules/create-api/">Rulesets API</a> calls. The converted API calls between the Firewall Rules API/Filters API and the Rulesets API appear in audit logs as generated by Cloudflare and not by the actual user making the requests. There will be a single list of rules for both firewall rules and WAF custom rules.</p>
<p>Some new features of WAF custom rules, like custom responses for blocked requests and the <em>Skip</em> action, are not supported in the Firewall Rules API. To take advantage of these features, Cloudflare recommends that you use the custom rules page in the Cloudflare dashboard or the Rulesets API.</p>
<p>Refer to the WAF documentation for <a href="/waf/custom-rules/create-api/">examples of managing WAF custom rules using the Rulesets API</a>.</p>
<h2 id="relevant-changes-for-terraform-users">Relevant changes for Terraform users</h2>
<p><strong>The following Terraform resources from the Cloudflare provider are now deprecated:</strong></p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/firewall_rule"><code>cloudflare_firewall_rule</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/filter"><code>cloudflare_filter</code></a></li>
</ul>
<p>These resources are no longer supported since 2025-06-15. If you are using these resources to manage your Firewall Rules configuration, you must manually update any Terraform configuration to <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> resources to prevent any issues.</p>
<p>There will be a single list of rules for both firewall rules and WAF custom rules.</p>
<p>Some new features of WAF custom rules are not supported in the deprecated Terraform resources. To take advantage of these features, Cloudflare recommends that you use the <code>cloudflare_ruleset</code> resource.</p>
<p>Refer to the documentation about Terraform for <a href="/terraform/additional-configurations/waf-custom-rules/">examples of configuring WAF custom rules using Terraform</a>.</p>
<h3 id="replace-your-configuration-using-cf-terraforming">Replace your configuration using <code>cf-terraforming</code></h3>
<p>You can use the <a href="https://github.com/cloudflare/cf-terraforming"><code>cf-terraforming</code></a> tool to generate the Terraform configuration for your current WAF custom rules (converted by Cloudflare from your firewall rules). Then, import the new resources to Terraform state.</p>
<p>The recommended steps for replacing your firewall rules (and filters) configuration in Terraform with a new ruleset configuration are the following.</p>
<ol>
<li>Run the following command to generate all ruleset configurations for a zone:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cf-terraforming generate --zone &lt;ZONE_ID&gt; --resource-type &quot;cloudflare_ruleset&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">resource &quot;cloudflare_ruleset&quot; &quot;terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31&quot; {&#10;  kind    = &quot;zone&quot;&#10;  name    = &quot;default&quot;&#10;  phase   = &quot;http_request_firewall_custom&quot;&#10;  zone_id = &quot;&lt;ZONE_ID&gt;&quot;&#10;  rules {&#10;    [...]&#10;  }&#10;  [...]&#10;}&#10;[...]&#10;</code></pre>
<ol start="2">
<li>
<p>The previous command may return additional ruleset configurations for other Cloudflare products also based on the <a href="/ruleset-engine/">Ruleset Engine</a>. Since you are migrating firewall rules to custom rules, keep only the Terraform resource for the <code>http_request_firewall_custom</code> phase and save it to a <code>.tf</code> configuration file. You will need the full resource name in the next step.</p>
</li>
<li>
<p>Import the <code>cloudflare_ruleset</code> resource you previously identified into Terraform state using the <code>terraform import</code> command. For example:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform import cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31 zone/&lt;ZONE_ID&gt;/3c0b456bc2aa443089c5f40f45f51b31&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Importing from ID &quot;zone/&lt;ZONE_ID&gt;/3c0b456bc2aa443089c5f40f45f51b31&quot;...&#10;cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Import prepared!&#10;  Prepared cloudflare_ruleset for import&#10;cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;&#10;Import successful!&#10;&#10;The resources that were imported are shown above. These resources are now in&#10;your Terraform state and will henceforth be managed by Terraform.&#10;</code></pre>
<ol start="4">
<li>Run <code>terraform plan</code> to validate that Terraform now checks the state of the new <code>cloudflare_ruleset</code> resource, in addition to other existing resources already managed by Terraform. For example:</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform plan&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">&#10;cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;[...]&#10;cloudflare_filter.my_filter: Refreshing state... [id=14a2524fd75c419f8d273116815b6349]&#10;cloudflare_firewall_rule.my_firewall_rule: Refreshing state... [id=0580eb5d92e344ddb2374979f74c3ddf]&#10;[...]&#10;</code></pre>
<ol start="5">
<li>Remove any state related to firewall rules and filters from your Terraform state:</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15673.md")
</aside>
   1. Run the following command to find all resources related to firewall rules and filters:
<pre tabindex="0"><code class="language-sh">terraform state list | grep -E &#x27;^cloudflare_(filter|firewall_rule)\.&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">cloudflare_filter.my_filter&#10;cloudflare_firewall_rule.my_firewall_rule&#10;</code></pre>
<ol start="2">
<li>Run the <code>terraform state rm ...</code> command in dry-run mode to understand the impact of removing those resources without performing any changes:</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform state rm -dry-run cloudflare_filter.my_filter cloudflare_firewall_rule.my_firewall_rule&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Would remove cloudflare_filter.my_filter&#10;Would remove cloudflare_firewall_rule.my_firewall_rule&#10;</code></pre>
<ol start="3">
<li>If the impact looks correct, run the same command without the <code>-dry-run</code> parameter to actually remove the resources from Terraform state:</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform state rm cloudflare_filter.my_filter cloudflare_firewall_rule.my_firewall_rule&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Removed cloudflare_filter.my_filter&#10;Removed cloudflare_firewall_rule.my_firewall_rule&#10;Successfully removed 2 resource instance(s).&#10;</code></pre>
<ol start="6">
<li>
<p>After removing firewall rules and filters resources from Terraform state, delete <code>cloudflare_filter</code> and <code>cloudflare_firewall_rule</code> resources from <code>.tf</code> configuration files.</p>
</li>
<li>
<p>Run <code>terraform plan</code> to verify that the resources you deleted from configuration files no longer appear. You should not have any pending changes.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform plan&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;[...]&#10;&#10;No changes. Your infrastructure matches the configuration.&#10;&#10;Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.&#10;</code></pre>
<p>For details on importing Cloudflare resources to Terraform and using the <code>cf-terraforming</code> tool, refer to the following resources:</p>
<ul>
<li><a href="/terraform/advanced-topics/import-cloudflare-resources/">Import Cloudflare resources</a></li>
<li><a href="https://github.com/cloudflare/cf-terraforming"><code>cf-terraforming</code> GitHub repository</a></li>
</ul>
<h2 id="final-remarks">Final remarks</h2>
<p>Any unpaused firewall rules with paused <a href="/firewall/api/cf-filters/what-is-a-filter/">filters</a> will become enabled when converted to custom rules.</p>
