---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/
  description: Rules in the Cloudflare Exposed Credentials Check managed ruleset.
  full_title: Cloudflare Exposed Credentials Check Managed Ruleset · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Cloudflare Exposed Credentials Check Managed Ruleset · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Rules in the Cloudflare Exposed Credentials Check managed ruleset."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/index.md"><meta property="og:title" content="Cloudflare Exposed Credentials Check Managed Ruleset · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Rules in the Cloudflare Exposed Credentials Check managed ruleset."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/#page","headline":"Cloudflare Exposed Credentials Check Managed Ruleset \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Rules in the Cloudflare Exposed Credentials Check managed ruleset.","url":"https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication"]}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/reference/exposed-credentials-check/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15611.md")
</aside>
<p>The Cloudflare Exposed Credentials Check Managed Ruleset is a set of pre-configured rules for well-known CMS applications that perform a lookup against a public database of stolen credentials.</p>
<p>The managed ruleset includes rules for the following CMS applications:</p>
<ul>
<li>WordPress</li>
<li>Joomla</li>
<li>Drupal</li>
<li>Ghost</li>
<li>Plone</li>
<li>Magento</li>
</ul>
<p>Additionally, this managed ruleset also includes generic rules for other common patterns:</p>
<ul>
<li>Check forms submitted using a <code>POST</code> request containing <code>username</code> and <code>password</code> arguments</li>
<li>Check credentials sent as JSON with <code>email</code> and <code>password</code> keys</li>
<li>Check credentials sent as JSON with <code>username</code> and <code>password</code> keys</li>
</ul>
<p>The default action for the rules in managed ruleset is <em>Exposed-Credential-Check Header</em> (named <code>rewrite</code> in the API and in <a href="/waf/analytics/security-events/#sampled-logs">Security Events</a>).</p>
<p>The managed ruleset also contains a rule that blocks HTTP requests already containing the <code>Exposed-Credential-Check</code> HTTP header used by the <em>Exposed-Credential-Check Header</em> action. These requests could be used to trick the origin into believing that a request contained (or did not contain) exposed credentials.</p>
<p>For more information on exposed credential checks, refer to <a href="/waf/managed-rules/check-for-exposed-credentials/">Check for exposed credentials</a>.</p>
<h2 id="configure-in-the-dashboard">Configure in the dashboard</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15610.md")
</aside>
<p>You can configure the following settings of the Cloudflare Exposed Credentials Check Managed Ruleset in the dashboard:</p>
<ul>
<li><strong>Set the action to perform.</strong> When you define an action for the ruleset, you override the default action defined for each rule. The available actions are: <em>Block</em>, <em>Log</em>, <em>Non-Interactive Challenge</em>, <em>Managed Challenge</em>, and <em>Interactive Challenge</em>. To remove the action override, set the ruleset action to <em>Default</em>.</li>
<li><strong>Override the action performed by individual rules.</strong> The available actions are: <em>Exposed-Credential-Check Header</em>, <em>Block</em>, <em>Log</em>, <em>Non-Interactive Challenge</em>, <em>Managed Challenge</em>, and <em>Interactive Challenge</em>. For more information, refer to <a href="/waf/managed-rules/check-for-exposed-credentials/#available-actions">Available actions</a>.</li>
<li><strong>Disable specific rules.</strong></li>
<li><strong>Customize the filter expression.</strong> With a custom expression, the Cloudflare Exposed Credentials Check Managed Ruleset applies only to a subset of the incoming requests.</li>
<li><strong>Configure <a href="/waf/managed-rules/payload-logging/configure/">payload logging</a></strong>.</li>
</ul>
<p>For details on configuring a managed ruleset in the dashboard, refer to <a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">Configure a managed ruleset</a>.</p>
<h2 id="configure-via-api">Configure via API</h2>
<p>To enable the Cloudflare Exposed Credentials Check Managed Ruleset for a given zone via API, create a rule with <code>execute</code> action in the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> for the <code>http_request_firewall_managed</code> phase.</p>
<h3 id="example">Example</h3>
<p>This example deploys the Cloudflare Exposed Credentials Check Managed Ruleset to the <code>http_request_firewall_managed</code> phase of a given zone (<code>$ZONE_ID</code>) by creating a rule that executes the managed ruleset. The rules in the managed ruleset are executed for all incoming requests.</p>
<ol>
<li></li>
</ol>
<p>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation to obtain the definition of the entry point ruleset for the <code>http_request_firewall_managed</code> phase. You will need the <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a> for this task.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;description&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;id&quot;: &quot;&lt;ENTRY_POINT_RULESET_ID&gt;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;last_updated&quot;: &quot;2024-03-16T15:40:08.202335Z&quot;,&#10;		&quot;name&quot;: &quot;zone&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;,&#10;		&quot;rules&quot;: [&#10;			// ...&#10;		],&#10;		&quot;source&quot;: &quot;firewall_managed&quot;,&#10;		&quot;version&quot;: &quot;10&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li></li>
</ol>
<p>If the entry point ruleset already exists (that is, if you received a <code>200 OK</code> status code and the ruleset definition), take note of the ruleset ID in the response. Then, invoke the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add an <code>execute</code> rule to the existing ruleset deploying the <p>Cloudflare Exposed Credentials Check Managed Ruleset (with ID �CODE17�)</p>
. By default, the rule will be added at the end of the list of rules already in the ruleset.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;c2e184081120413c86c3ab7e14069605&quot;&#10;  },&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;description&quot;: &quot;Execute the Cloudflare Exposed Credentials Check Managed Ruleset&quot;&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ENTRY_POINT_RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;11&quot;,&#10;		&quot;rules&quot;: [&#10;			// ... any existing rules&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;c2e184081120413c86c3ab7e14069605&quot;,&#10;					&quot;version&quot;: &quot;latest&quot;&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Execute the Cloudflare Exposed Credentials Check Managed Ruleset&quot;,&#10;				&quot;last_updated&quot;: &quot;2024-03-18T18:08:14.003361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2024-03-18T18:08:14.003361Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="3">
<li></li>
</ol>
<p>If the entry point ruleset does not exist (that is, if you received a <code>404 Not Found</code> status code in step 1), create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. Include a single rule in the <code>rules</code> array that executes the <p>Cloudflare Exposed Credentials Check Managed Ruleset (with ID �CODE20�)</p>
for <p>all incoming requests in the zone</p>
.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;My ruleset&quot;,&#10;  &quot;description&quot;: &quot;Entry point ruleset for WAF managed rulesets&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;phase&quot;: &quot;http_request_firewall_managed&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;c2e184081120413c86c3ab7e14069605&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Execute the Cloudflare Exposed Credentials Check Managed Ruleset&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h3 id="next-steps">Next steps</h3>
<p>To configure the Exposed Credentials Check Managed Ruleset via API, create <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> using the Rulesets API. You can perform the following configurations:</p>
<ul>
<pre tabindex="0"><code>&lt;li&gt;&#10;	Specify the action to perform for all the rules in the ruleset by creating&#10;	a ruleset override.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Disable or customize the action of individual rules by creating rule&#10;	overrides.&#10;&lt;/li&gt;&#10;</code></pre>
</ul>
<p>For examples of creating overrides using the API, refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="checking-for-exposed-credentials-in-custom-rules">Checking for exposed credentials in custom rules</h3>
@markup("md", "content/.markup/bodies/15609.md")
</aside>
<h3 id="more-resources">More resources</h3>
<p>For more information on working with managed rulesets via API, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a> in the Ruleset Engine documentation.</p>
