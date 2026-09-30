---
cp9:
  canonical: https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/
  description: Guide on upgrading rate limiting rules from the previous version to the new version.
  full_title: Rate limiting (previous version) upgrade · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Rate limiting (previous version) upgrade · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Guide on upgrading rate limiting rules from the previous version to the new version."><link rel="canonical" href="https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/index.md"><meta property="og:title" content="Rate limiting (previous version) upgrade · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Guide on upgrading rate limiting rules from the previous version to the new version."><meta property="og:url" content="https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/#page","headline":"Rate limiting (previous version) upgrade \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Guide on upgrading rate limiting rules from the previous version to the new version.","url":"https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/reference/legacy/old-rate-limiting/upgrade/
  schema: 1
---
<p>Cloudflare has upgraded all rate limiting rules created in the <a href="/waf/reference/legacy/old-rate-limiting/">previous version</a> to the <a href="/waf/rate-limiting-rules/">new version of rate limiting rules</a>.</p>
<p>The Cloudflare dashboard now shows all your rate limiting rules in a single list.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="sunset-notice">Sunset notice</h3>
@markup("md", "content/.markup/bodies/15690.md")
</aside>
<h2 id="main-differences">Main differences</h2>
<ul>
<li>
<p><strong>Billing model:</strong> The previous version of Rate Limiting was billed based on usage and it was available as an add-on on all plans, while the new version is included in Cloudflare plans. For Enterprise plans, Rate Limiting is priced based on total contracted HTTP traffic. The new rate limiting rules offer all the capabilities available on the previous version of rate limiting along with several additional features.</p>
</li>
<li>
<p><strong>Advanced scope expressions:</strong> The previous version of Rate Limiting allowed you to scope the rules based on a single path and method of the request. In the new version, you can write rules similar to <a href="/waf/custom-rules/">WAF custom rules</a>, combining multiple parameters of the HTTP request.</p>
</li>
<li>
<p><strong>Counter scope:</strong> The new version of rate limiting uses counters scoped per data center, with <code>cf.colo.id</code> always included as a characteristic. This means thresholds can behave differently for traffic distributed across multiple Cloudflare locations. Data centers in the same geographic location share counters. For more information, refer to <a href="/waf/rate-limiting-rules/request-rate/">How Cloudflare determines the request rate</a>.</p>
</li>
<li>
<p><strong>Separate counting and mitigation expressions:</strong> In the new version of Rate Limiting, counting and mitigation expressions are separate (for Business and Enterprise customers). The counting expression defines which requests are used to compute the rate. The mitigation expression defines which requests are mitigated once the threshold has been reached. Using these separate expressions, you can track the rate of requests on a specific path such as <code>/login</code> and, when an IP exceeds the threshold, block every request from the same IP addressed at your domain.</p>
</li>
<li>
<p><strong>Additional counting dimensions (Advanced Rate Limiting only):</strong> Like in the previous version of Rate Limiting, customers with the new Rate Limiting get IP-based rate limiting, where Cloudflare counts requests based on the source IP address of incoming requests. In addition to IP-based rate limiting, customers with the new Rate Limiting who subscribe to Advanced Rate Limiting can group requests based on other characteristics, such as the value of API keys, cookies, session headers, ASN, query parameters, or a specific JSON body field. Refer to <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> for examples.</p>
</li>
<li>
<p><strong>Number of rules per plan</strong>: Besides the exact features per Cloudflare plan, the number of rules per plan is different in the new version of Rate Limiting (for information on the new version limits, refer to <a href="/waf/rate-limiting-rules/#availability">Rate limiting rules</a>):</p>
</li>
</ul>
<table>
<thead>
<tr>
<th>Product</th>
<th align="center">Free</th>
<th align="center">Pro</th>
<th align="center">Business</th>
<th align="center">Enterprise with RL add-on,<br/> or equivalent plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rate Limiting (previous version)</td>
<td align="center">1</td>
<td align="center">10</td>
<td align="center">15</td>
<td align="center">100</td>
</tr>
<tr>
<td>Rate Limiting (new version)</td>
<td align="center">1</td>
<td align="center">2</td>
<td align="center">5</td>
<td align="center">100</td>
</tr>
</tbody>
</table>
<p>Enterprise customers must have application security on their contract to get access to rate limiting rules.</p>
<p>Refer to <a href="#important-remarks-about-the-upgrade">Important remarks about the upgrade</a> for details on how Cloudflare will adjust your rules quota, if needed, after the upgrade.</p>
<p>For more details on the differences between old and new rate limiting rules, refer to <a href="https://blog.cloudflare.com/unmetered-ratelimiting/">our blog post</a>.</p>
<h2 id="important-remarks-about-the-upgrade">Important remarks about the upgrade</h2>
<ul>
<li>
<p><strong>After the upgrade, you will not be able to create or edit rate limiting rules while you are above the new rules quota for your Cloudflare plan.</strong> The number of rate limiting rules included in your Cloudflare plan can be lower than before. If you are over the new limit, you will need to either upgrade to a plan that gives you more rules, or delete existing rules until the number of rules is less or equal to the new maximum number of rules for your plan.</p>
</li>
<li>
<p><strong>Custom timeouts will be rounded to the nearest supported timeout.</strong> Both custom counting periods and custom mitigation timeouts will be rounded up or down to the nearest counting period and mitigation timeout supported in the new version (refer to <a href="/waf/rate-limiting-rules/#availability">Availability</a> for details on the available values per plan).<br/>
For example, if you had a rate limiting rule with a mitigation timeout of 55 seconds, this timeout will be rounded up to one minute (nearest value).<br/>
Enterprise customers will be able to set a custom mitigation timeout for a rule after the upgrade, but this configuration is only available via API.</p>
</li>
<li>
<p><strong>Customers on a Business plan (or higher) will have access to the <a href="/waf/rate-limiting-rules/parameters/#use-cases-of-ip-with-nat-support">IP with NAT support</a> characteristic.</strong> This characteristic is used to handle situations such as requests under NAT sharing the same IP address.</p>
</li>
<li>
<p><strong>Existing custom rules skipping old Rate Limiting will not be updated to skip the new version instead.</strong> Cloudflare will not update existing custom rules that skip the previous version of Rate Limiting (skip rules with the option <strong>More components to skip</strong> &gt; <strong>Rate limiting rules (Previous version)</strong>) to skip the new version.<br/>
For existing skip rules (custom rules with a <em>Skip</em> action), you will have to manually update them, if required, to skip the new version of rate limiting rules (<strong>WAF components to skip</strong> &gt; <strong>All rate limiting rules</strong> option) instead of the old implementation.</p>
</li>
</ul>
<hr />
<h3 id="relevant-changes-in-the-dashboard">Relevant changes in the dashboard</h3>
<p>If you had access to the previous version of Cloudflare Rate Limiting, you will now find all rate limiting rules in the same list in <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Rate limiting rules</strong>.
Rate limiting rules created in the previous version are tagged with <code>Previous version</code> in the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/waf/reference/rate-limiting-rules-upgrade-ui.png" alt="Rate limiting rules user interface showing two rules created in the previous version." /></p>
<p>If you are using the new <a href="/security/">application security dashboard</a>, only the rate limiting rules that have been upgraded to the new version will be shown at <strong>Security</strong> &gt; <strong>Security rules</strong>.</p>
<p>If you edit a rule with this tag in the dashboard, you will no longer be able to edit the rule using the API and Terraform resource for the previous version of rate limiting rules. In this case, you will need to start using the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> or the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> Terraform resource for this purpose. Refer to <a href="#relevant-changes-for-api-users">Relevant changes for API users</a> and <a href="#relevant-changes-for-terraform-users">Relevant changes for Terraform users</a> for more information.</p>
<h3 id="relevant-changes-for-api-users">Relevant changes for API users</h3>
<p><strong>The previous Rate Limiting API is deprecated.</strong> The API is no longer supported since 2025-06-15. You must update any automation based on the <a href="/api/resources/rate_limits/">previous Rate Limiting API</a> to the <a href="/waf/rate-limiting-rules/create-api/">Rulesets API</a> to prevent any issues.</p>
<p>The new rate limiting rules are based on the <a href="/ruleset-engine/">Ruleset Engine</a>. To configure these rate limiting rules via the API you must use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. Since rate limiting rules created in the previous version were upgraded to the new version, this API will also return these rules created in the new version.</p>
<p>The <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> is the only API that allows you to create, edit, and delete any rate limiting rule, regardless of the implementation version where you created the rule. The <a href="/api/resources/rate_limits/">previous Rate Limiting API</a> will only work with rate limiting rules created in the previous version that you have not edited in the dashboard or modified through the new API/Terraform resource since they were upgraded to the new version.</p>
<p>Until the API sunset date, you can use the <a href="/api/resources/rate_limits/">previous Rate Limiting API</a> to create, edit, and delete rate limiting rules created in the previous version (which Cloudflare upgraded to the new version). However, if you use the Rulesets API to edit a rule created in the previous version, or if you change such a rule in the Cloudflare dashboard – including changing the rule order – you will no longer be able to manage this rule (upgraded from the previous version and then updated using the Rulesets API) using the old API operations. In this case, you will need to completely switch to the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> for managing this specific rule.</p>
<h3 id="relevant-changes-for-terraform-users">Relevant changes for Terraform users</h3>
<p><strong>The <code>cloudflare_rate_limit</code> Terraform resource is deprecated.</strong> The resource is no longer supported since 2025-06-15. You must manually update your rate limiting configuration in Terraform from <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/rate_limit"><code>cloudflare_rate_limit</code></a> resources to <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> resources to prevent any issues.</p>
<p>The new rate limiting rules are based on the <a href="/ruleset-engine/">Ruleset Engine</a>. To configure these rate limiting rules with Terraform you must use the <code>cloudflare_ruleset</code> Terraform resource.</p>
<p>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> Terraform resource is the only resource that allows you to create, edit, and delete any rate limiting rule, regardless of the implementation version where you created the rule. The <code>cloudflare_rate_limit</code> Terraform resource will only work with rate limiting rules created in the previous version that you have not edited in the dashboard or modified through the new API/Terraform resource since they were upgraded to the new version.</p>
<p>Until the sunset date for the <code>cloudflare_rate_limit</code> Terraform resource, you can use this resource to create, edit, and delete rate limiting rules created in the previous version (which Cloudflare upgraded to the new version). However, if you start using the <code>cloudflare_ruleset</code> Terraform resource to manage a rule created in the previous version, or if you edit such a rule in the Cloudflare dashboard – including changing the rule order – you will no longer be able to manage this rule (upgraded from the previous version and then updated using the new resource) using the old Terraform resource. In this case, you will need to completely switch to the <code>cloudflare_ruleset</code> Terraform resource for managing this specific rule.</p>
<p>Refer to the Terraform documentation for <a href="/terraform/additional-configurations/rate-limiting-rules/">examples of configuring the new rate limiting rules using Terraform</a>.</p>
<h3 id="replace-your-configuration-with-cf-terraforming">Replace your configuration with cf-terraforming</h3>
<p>You can use the <a href="https://github.com/cloudflare/cf-terraforming"><code>cf-terraforming</code></a> tool to generate your new Terraform configuration for rate limiting rules created in the previous version. Then, you can import the new resources to Terraform state.</p>
<p>The recommended steps for replacing your old rate limiting configuration in Terraform with a new ruleset configuration are the following.</p>
<ol>
<li>Run the following command to generate all ruleset configurations for a zone:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cf-terraforming generate --zone &lt;ZONE_ID&gt; --resource-type &quot;cloudflare_ruleset&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_ruleset&quot; &quot;terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31&quot; {&#10;  kind    = &quot;zone&quot;&#10;  name    = &quot;default&quot;&#10;  phase   = &quot;http_ratelimit&quot;&#10;  zone_id = &quot;&lt;ZONE_ID&gt;&quot;&#10;  rules {&#10;    &#35; (...)&#10;  }&#10;  &#35; (...)&#10;}&#10;&#35; (...)&#10;</code></pre>
<ol start="2">
<li>
<p>The previous command may return additional ruleset configurations for other Cloudflare products also based on the <a href="/ruleset-engine/">Ruleset Engine</a>. Since you are updating your rate limiting rules configuration, keep only the Terraform resource for the <code>http_ratelimit</code> phase and save it to a <code>.tf</code> configuration file. You will need the full resource name in the next step.</p>
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
<pre tabindex="0"><code class="language-txt">cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;[...]&#10;cloudflare_rate_limit.my_rate_limiting_rules: Refreshing state... [id=0580eb5d92e344ddb2374979f74c3ddf]&#10;[...]&#10;</code></pre>
<ol start="5">
<li>Remove any state related to rate limiting rules configured through the old <code>cloudflare_rate_limit</code> resource from your Terraform state:</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15689.md")
</aside>
    1. Run the following command to find all resources related to rate limiting rules (previous version):
<pre tabindex="0"><code class="language-sh">terraform state list | grep -E &#x27;^cloudflare_rate_limit\.&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">cloudflare_rate_limit.my_rate_limiting_rules&#10;</code></pre>
<pre tabindex="0"><code>2. Run the `terraform state rm ...` command in dry-run mode to understand the impact of removing those resources without performing any changes:&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">terraform state rm -dry-run cloudflare_rate_limit.my_rate_limiting_rules&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Would remove cloudflare_rate_limit.my_rate_limiting_rules&#10;</code></pre>
<pre tabindex="0"><code>3. If the impact looks correct, run the same command without the `-dry-run` parameter to actually remove the resources from Terraform state:&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">terraform state rm cloudflare_rate_limit.my_rate_limiting_rules&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Removed cloudflare_rate_limit.my_rate_limiting_rules&#10;Successfully removed 1 resource instance(s).&#10;</code></pre>
<ol start="6">
<li>
<p>After removing <code>cloudflare_rate_limit</code> resources from Terraform state, delete all these resources from <code>.tf</code> configuration files.</p>
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
<h2 id="more-resources">More resources</h2>
<p>For more information on the new rate limiting implementation, including the available features in each Cloudflare plan, refer to <a href="/waf/rate-limiting-rules/">Rate limiting rules</a>.</p>
<p>Cloudflare also offers an Advanced version of Rate Limiting, which is available to Enterprise customers. For more information, refer to the <a href="https://blog.cloudflare.com/advanced-rate-limiting/">Introducing Advanced Rate Limiting</a> blog post.</p>
<p>To learn more about what you can do with the new rate limiting, refer to <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a>.</p>
