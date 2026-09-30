---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/
  description: Deploy WAF managed rulesets per custom hostname using WAF for SaaS.
  full_title: Managed rulesets per custom hostname · Cloudflare for Platforms docs
  head_html: <title>Managed rulesets per custom hostname · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy WAF managed rulesets per custom hostname using WAF for SaaS."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/index.md"><meta property="og:title" content="Managed rulesets per custom hostname · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy WAF managed rulesets per custom hostname using WAF for SaaS."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/#page","headline":"Managed rulesets per custom hostname \u00b7 Cloudflare for Platforms docs","description":"Deploy WAF managed rulesets per custom hostname using WAF for SaaS.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/
  schema: 1
---
<p>If you are interested in <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">WAF for SaaS</a> but unsure of where to start, Cloudflare recommends using WAF Managed Rules. The Cloudflare security team creates and manages a variety of rules designed to detect common attack vectors and protect applications from vulnerabilities. These rules are offered in <a href="/waf/managed-rules/">managed rulesets</a>, like Cloudflare Managed and OWASP, which can be deployed with different settings and sensitivity levels.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<p>WAF for SaaS is available for customers on an Enterprise plan.</p>
<p>If you would like to deploy a managed ruleset at the account level, refer to the <a href="/waf/account/managed-rulesets/deploy-dashboard/">WAF documentation</a>.</p>
<p>Ensure you have reviewed <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Get Started with Cloudflare for SaaS</a> and familiarize yourself with <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">WAF for SaaS</a>.</p>
<p>Customers can automate the <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a> tagging by adding it to the custom hostnames at creation. For more information on tagging a custom hostname with custom metadata, refer to the <a href="/api/resources/custom_hostnames/methods/edit/">API documentation</a>.</p>
<hr />
<h2 id="1-choose-security-tagging-system"><ol>
<li>Choose security tagging system</li>
</ol></h2>
<ol>
<li>
<p>Outline <code>security_tag</code> buckets. These are fully customizable with no strict limit on quantity. For example, you can set <code>security_tag</code> to <code>low</code>,<code>medium</code>, and <code>high</code> as a default, with one tag per custom hostname.</p>
</li>
<li>
<p>If you have not already done so, <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/#1-associate-custom-metadata-to-a-custom-hostname">associate your custom metadata to custom hostnames</a> by including the <code>security_tag</code>in the custom metadata associated with the custom hostname. The JSON blob associated with the custom hostname is fully customizable.</p>
</li>
</ol>
<p>After the association is complete, the JSON blob is added to the defined custom hostname. This blob is then associated to every incoming request and exposed in the WAF through the <a href="/ruleset-engine/rules-language/fields/reference/cf.hostname.metadata/"><code>cf.hostname.metadata</code></a> field. In the rule, you can access <code>cf.hostname.metadata</code> and get the data you need from that blob.</p>
<hr />
<h2 id="2-deploy-rulesets"><ol start="2">
<li>Deploy rulesets</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4130.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>WAF</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Go to the <strong>Managed rulesets</strong> tab.</p>
</li>
<li>
<p>Select <strong>Deploy</strong> &gt; <strong>Deploy managed ruleset</strong>.</p>
</li>
<li>
<p>Next to <strong>Cloudflare Managed Ruleset</strong>, choose <strong>Select ruleset</strong>.</p>
</li>
<li>
<p>Give a name to the rule deploying the ruleset in <strong>Execution name</strong>.</p>
</li>
<li>
<p>Select <strong>Edit scope</strong> to execute the managed ruleset for a subset of incoming requests.</p>
</li>
<li>
<p>Select <strong>Custom filter expression</strong>.</p>
</li>
<li>
<p>Select <strong>Edit expression</strong> to switch to the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a>.</p>
</li>
<li>
<p>The basic expression should look like this, plus any logic you would like to add (like filtering by a specific custom hostname with <code>http.host eq &quot;&lt;HOSTNAME&gt;&quot;</code>):</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">(lookup_json_string(cf.hostname.metadata, &quot;security_tag&quot;) eq &quot;low&quot;) and (cf.zone.plan eq &quot;ENT&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4129.md")
</aside>
<ol start="10">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>(Optional) You can modify the ruleset configuration by changing, for example, what rules are enabled or what action should be the default.</p>
</li>
<li>
<p>Select <strong>Deploy</strong>.</p>
</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>While this guide uses the Cloudflare Managed Ruleset, you can also create a custom ruleset and deploy on your custom hostnames. To do this, go to the <strong>Custom rulesets</strong> tab and select <strong>Create ruleset</strong>. For examples of a low/medium/high ruleset, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">WAF for SaaS</a>.</p>
