---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/
  description: JSON object structure for rulesets and rules in API requests.
  full_title: JSON objects · Cloudflare Ruleset Engine docs
  head_html: <title>JSON objects · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="JSON object structure for rulesets and rules in API requests."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/index.md"><meta property="og:title" content="JSON objects · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="JSON object structure for rulesets and rules in API requests."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Ruleset Engine"><meta name="pcx_tags" content="JSON"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/#page","headline":"JSON objects \u00b7 Cloudflare Ruleset Engine docs","description":"JSON object structure for rulesets and rules in API requests.","url":"https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON"]}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rulesets-api/json-object/
  schema: 1
---
<p>This page describes the JSON objects used in API requests creating or updating rulesets and their rules via Rulesets API, as well as the objects returned by the API.</p>
<h2 id="ruleset-object">Ruleset object</h2>
<p>A fully populated ruleset object has the following JSON structure.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;6a359df138c442b385d20140d4d96919&quot;,&#10;	&quot;name&quot;: &quot;Example Ruleset&quot;,&#10;	&quot;description&quot;: &quot;Description of Example Ruleset&quot;,&#10;	&quot;kind&quot;: &quot;custom&quot;,&#10;	&quot;version&quot;: &quot;2&quot;,&#10;	&quot;phase&quot;: &quot;http_request_firewall_custom&quot;,&#10;	&quot;rules&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;fdb0dd271f3f40b19679cc5d91396024&quot;,&#10;			&quot;version&quot;: &quot;2&quot;,&#10;			&quot;action&quot;: &quot;block&quot;,&#10;			&quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot; &quot;,&#10;			&quot;last_updated&quot;: &quot;2022-07-20T10:44:29.124515Z&quot;&#10;		}&#10;	],&#10;	&quot;last_updated&quot;: &quot;2022-07-20T10:44:29.124515Z&quot;&#10;}&#10;</code></pre>
<p>For details on the properties of rules items in the <code>rules</code> array, refer to the <a href="#rule-object-structure-and-properties">Rule object structure and properties</a> section.</p>
<h3 id="properties">Properties</h3>
<p>The ruleset object has the following properties:</p>
<ul>
<li>
<p><code>id</code> <span class="nb-type">String</span></p>
<ul>
<li>A 32-character UUIDv4 string that represents the unique Cloudflare-generated identifier for a given version of a ruleset.</li>
<li>Unique, read-only.</li>
</ul>
</li>
<li>
<p><code>name</code> <span class="nb-type">String</span></p>
<ul>
<li>A human-readable name for the ruleset.</li>
<li>The name is immutable. You cannot change the name over the lifetime of the ruleset.</li>
</ul>
</li>
<li>
<p><code>description</code> <span class="nb-type">String</span></p>
<ul>
<li>Optional description for the ruleset.</li>
<li>You can change the description over the lifetime of the ruleset.</li>
</ul>
</li>
<li>
<p><code>kind</code> <span class="nb-type">String</span></p>
<ul>
<li>The kind of ruleset the JSON object represents.</li>
<li>One of <code>root</code>, <code>zone</code>, <code>managed</code>, <code>custom</code>.</li>
<li><code>kind</code> is immutable.</li>
</ul>
</li>
<li>
<p><code>version</code> <span class="nb-type">Integer</span></p>
<ul>
<li>The version of the ruleset.</li>
<li>Read-only value starting at <code>1</code> and incremented by <code>1</code> each time the ruleset is modified.</li>
</ul>
</li>
<li>
<p><code>rules</code> <span class="nb-type">Array&lt;Rule&gt;</span></p>
<ul>
<li>A list of rules to include in the ruleset. Refer to <a href="#rule-object-structure-and-properties">Rule object structure and properties</a> for details.</li>
</ul>
</li>
<li>
<p><code>last_updated</code> <span class="nb-type">Timestamp</span></p>
<ul>
<li>The time (UTC) when the ruleset was last updated in ISO 8601 format: <code>YYYY-MM-DDThh:mm:ss.TZD</code>.</li>
<li>Read-only.</li>
</ul>
</li>
</ul>
<h2 id="rule-object-structure-and-properties">Rule object structure and properties</h2>
<p>A fully populated rule JSON object has the following structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;fdb0dd271f3f40b19679cc5d91396024&quot;,&#10;	&quot;version&quot;: &quot;2&quot;,&#10;	&quot;ref&quot;: &quot;&lt;REF&gt;&quot;,&#10;	&quot;description&quot;: &quot;&lt;DESCRIPTION&gt;&quot;,&#10;	&quot;action&quot;: &quot;block&quot;,&#10;	&quot;action_parameters&quot;: [&#10;		// action parameters vary according to the action&#10;	],&#10;	&quot;categories&quot;: [&quot;&lt;CATEGORY_1&gt;&quot;, &quot;&lt;CATEGORY_2&gt;&quot;],&#10;	&quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot;&quot;,&#10;	&quot;last_updated&quot;: &quot;2025-07-20T10:44:29.124515Z&quot;,&#10;	&quot;enabled&quot;: true&#10;}&#10;</code></pre>
<p>The JSON object properties for a rule are defined as follows:</p>
<ul>
<li>
<p><code>id</code> <span class="nb-type">String</span></p>
<ul>
<li>A 32-character UUIDv4 string that represents the unique Cloudflare-generated identifier for a given version of a rule.</li>
<li>Unique, read-only.</li>
</ul>
</li>
<li>
<p><code>version</code> <span class="nb-type">Integer</span></p>
<ul>
<li>The version of the rule.</li>
<li>Read-only value starting at <code>1</code> and incremented by <code>1</code> each time the rule is modified.</li>
<li>Changing the order of a rule in a ruleset does not change its version.</li>
</ul>
</li>
<li>
<p><code>ref</code> <span class="nb-type">String</span></p>
<ul>
<li>A user-defined external identifier that must be unique for each rule in a ruleset.</li>
<li>Use this field in your Terraform configuration to prevent Terraform from recreating the rule on changes. Refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">How to keep the same rule ID between modifications</a> for more information.</li>
</ul>
</li>
<li>
<p><code>description</code> <span class="nb-type">String</span></p>
<ul>
<li>A descriptive name of the rule.</li>
</ul>
</li>
<li>
<p><code>action</code> <span class="nb-type">String</span></p>
<ul>
<li>Defines what happens when there is a match for the rule expression.</li>
<li>The available <a href="/ruleset-engine/rules-language/actions/">actions</a> depend on the <a href="/ruleset-engine/about/phases/">phase</a> where the rule's ruleset is executed.</li>
</ul>
</li>
<li>
<p><code>action_parameters</code> <span class="nb-type">Object</span></p>
<ul>
<li>One or more parameters configuring the rule action.</li>
<li>The exact properties vary according to the action. Refer to each Cloudflare product's API instructions for more information.</li>
</ul>
</li>
<li>
<p><code>categories</code> <span class="nb-type">Array&lt;String&gt;</span></p>
<ul>
<li>Tags associated with the current rule. You can define overrides that affect rules with a given tag.</li>
<li>Read-only. Only available in <a href="/waf/managed-rules/">WAF Managed Rules</a> and <a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a>.</li>
</ul>
</li>
<li>
<p><code>expression</code> <span class="nb-type">String</span></p>
<ul>
<li>Criteria defining when there is a match for the current rule.</li>
<li>The fields and functions you can use in a rule expression depend on the phase where the rule's ruleset is executed.</li>
</ul>
</li>
<li>
<p><code>last_updated</code> <span class="nb-type">Timestamp</span></p>
<ul>
<li>The time (UTC) when the rule was last updated in ISO 8601 format: <code>YYYY-MM-DDThh:mm:ss.TZD</code>.</li>
<li>Read-only.</li>
</ul>
</li>
<li>
<p><code>enabled</code> <span class="nb-type">Boolean</span></p>
<ul>
<li>When set to <code>true</code>, the current rule is enabled.</li>
</ul>
</li>
</ul>
