---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/
  description: Deploy rulesets to a phase entry point using the API.
  full_title: Deploy rulesets · Cloudflare Ruleset Engine docs
  head_html: <title>Deploy rulesets · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy rulesets to a phase entry point using the API."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/index.md"><meta property="og:title" content="Deploy rulesets · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy rulesets to a phase entry point using the API."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/#page","headline":"Deploy rulesets \u00b7 Cloudflare Ruleset Engine docs","description":"Deploy rulesets to a phase entry point using the API.","url":"https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/basic-operations/deploy-rulesets/
  schema: 1
---
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to deploy a ruleset. To deploy a ruleset, add a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> to a <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">phase entry point ruleset</a>, specifying the ruleset ID to execute as an action parameter. Use a separate rule for each ruleset you want to deploy.</p>
<p>A rule that executes a ruleset consists of:</p>
<ul>
<li>The ID of the ruleset you want to execute, included in <code>action_parameters.id</code>.</li>
<li>An expression.</li>
<li>The <code>execute</code> action.</li>
</ul>
<p>The rules in the ruleset execute when a request satisfies the expression.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13286.md")
</aside>
<h2 id="example">Example</h2>
<p>The following example deploys the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> (with ID <code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code>) to the <code>http_request_firewall_managed</code> phase of a given zone (<code>$ZONE_ID</code>) by adding a rule that executes the managed ruleset.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Execute Cloudflare Managed Ruleset on my zone ruleset&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ZONE_PHASE_RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;latest&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;					&quot;version&quot;: &quot;3&quot;&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Execute Cloudflare Managed Ruleset on my zone ruleset&quot;,&#10;				&quot;last_updated&quot;: &quot;2021-03-18T18:08:14.003361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2021-03-18T18:08:14.003361Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13285.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<p>For more examples of deploying rulesets, refer to the following pages:</p>
<ul>
<li><a href="/ruleset-engine/managed-rulesets/deploy-managed-ruleset/">Deploy a managed ruleset</a></li>
<li><a href="/ruleset-engine/managed-rulesets/override-examples/">Managed ruleset override examples</a>.</li>
<li><a href="/ruleset-engine/custom-rulesets/deploy-custom-ruleset/">Deploy a custom ruleset</a></li>
</ul>
<p>Refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a> and <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> for more information.</p>
<p>For more information on the available API endpoints for editing and deploying rulesets, refer to <a href="/ruleset-engine/rulesets-api/update/">Update or deploy a ruleset</a>.</p>
