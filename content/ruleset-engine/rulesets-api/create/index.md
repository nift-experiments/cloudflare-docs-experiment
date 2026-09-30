---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rulesets-api/create/
  description: Create a new ruleset using the Rulesets API.
  full_title: Create a ruleset · Cloudflare Ruleset Engine docs
  head_html: <title>Create a ruleset · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a new ruleset using the Rulesets API."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/create/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/create/index.md"><meta property="og:title" content="Create a ruleset · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a new ruleset using the Rulesets API."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rulesets-api/create/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/create/#page","headline":"Create a ruleset \u00b7 Cloudflare Ruleset Engine docs","description":"Create a new ruleset using the Rulesets API.","url":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/create/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rulesets-api/create/
  schema: 1
---
<p>Creates a ruleset of a given kind in the specified phase. Allows you to create phase entry point rulesets.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/methods/create/">Create an account ruleset</a><br/>
<code>POST /accounts/{account_id}/rulesets</code></li>
<li><a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a><br/>
<code>POST /zones/{zone_id}/rulesets</code></li>
</ul>
<h2 id="parameters">Parameters</h2>
<p>A <code>POST</code> request to create a ruleset supports the following parameters in the request body:</p>
<ul>
<li><code>name</code> <span class="nb-type">String</span>
<ul>
<li>A human-readable name for the ruleset.</li>
<li>The name is immutable. You cannot change it over the lifetime of the ruleset.</li>
</ul>
</li>
<li><code>description</code> <span class="nb-type">String</span> <span class="nb-metainfo">Optional</span>
<ul>
<li>Optional description for the ruleset.</li>
<li>You can change the description over the lifetime of the ruleset.</li>
</ul>
</li>
<li><code>kind</code> <span class="nb-type">String</span>
<ul>
<li>The kind of ruleset the JSON object represents.</li>
<li>Allowed values:
<ul>
<li><code>custom</code>: Creates a custom ruleset</li>
<li><code>root</code>: Creates a phase <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> at the account level</li>
<li><code>zone</code>: Creates a phase entry point ruleset at the zone level</li>
</ul>
</li>
</ul>
</li>
<li><code>phase</code> <span class="nb-type">String</span>
<ul>
<li>The name of the <a href="/ruleset-engine/about/phases/">phase</a> where the ruleset will be created.</li>
<li>Check the <a href="/ruleset-engine/reference/phases-list/">phases list</a> or the specific Cloudflare product documentation for more information on the phases where you can create rulesets for that product.</li>
</ul>
</li>
<li><code>rules</code> <span class="nb-type">Array&lt;Rule&gt;</span> <span class="nb-metainfo">Optional</span>
<ul>
<li>A list of <a href="/ruleset-engine/rulesets-api/json-object/#rule-object-structure-and-properties">rules</a> to include in the ruleset.</li>
</ul>
</li>
</ul>
<p>For additional details on these parameters, refer to <a href="/ruleset-engine/rulesets-api/json-object/">JSON objects</a>.</p>
<h2 id="example-create-a-custom-ruleset">Example - Create a custom ruleset</h2>
<p>The following <code>POST</code> request creates a custom ruleset in the <code>http_request_firewall_custom</code> phase at the account level containing a single rule.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Example custom ruleset&quot;,&#10;  &quot;kind&quot;: &quot;custom&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;log&quot;,&#10;      &quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot;&quot;&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Example custom ruleset&quot;,&#10;		&quot;description&quot;: &quot;Example ruleset description&quot;,&#10;		&quot;kind&quot;: &quot;custom&quot;,&#10;		&quot;version&quot;: &quot;1&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;log&quot;,&#10;				&quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot;&quot;,&#10;				&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="example-create-a-zone-level-phase-entry-point-ruleset">Example - Create a zone-level phase entry point ruleset</h2>
<p>The following <code>POST</code> request creates a zone-level phase entry point ruleset at the <code>http_request_firewall_managed</code> phase with a single rule that executes a managed ruleset.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13245.md")
</aside>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;description&quot;: &quot;This ruleset executes a managed ruleset.&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;      }&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;This ruleset executes a managed ruleset.&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;1&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;				},&#10;				&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="example-create-an-account-level-phase-entry-point-ruleset">Example - Create an account-level phase entry point ruleset</h2>
<p>The following <code>POST</code> request creates an account-level phase entry point ruleset for the <code>http_ratelimit</code> phase with a single rule that executes a rate limiting ruleset for all Enterprise zones in the account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13244.md")
</aside>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Account-level phase entry point&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;description&quot;: &quot;This ruleset executes a rate limiting ruleset.&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;(cf.zone.plan eq \&quot;ENT\&quot;)&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;RATE_LIMITING_RULESET_ID&gt;&quot;&#10;      }&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_ratelimit&quot;&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Account-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;This ruleset executes a rate limiting ruleset.&quot;,&#10;		&quot;kind&quot;: &quot;root&quot;,&#10;		&quot;version&quot;: &quot;1&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;(cf.zone.plan eq \&quot;ENT\&quot;)&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;&lt;RATE_LIMITING_RULESET_ID&gt;&quot;&#10;				},&#10;				&quot;last_updated&quot;: &quot;2024-09-17T15:42:37.917815Z&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2024-09-17T15:42:37.917815Z&quot;,&#10;		&quot;phase&quot;: &quot;http_ratelimit&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13243.md")
</aside>
