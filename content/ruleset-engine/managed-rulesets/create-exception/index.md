---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/
  description: Create an exception to skip specific rules or rulesets.
  full_title: Create an exception · Cloudflare Ruleset Engine docs
  head_html: <title>Create an exception · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Create an exception to skip specific rules or rulesets."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/index.md"><meta property="og:title" content="Create an exception · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create an exception to skip specific rules or rulesets."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/#page","headline":"Create an exception \u00b7 Cloudflare Ruleset Engine docs","description":"Create an exception to skip specific rules or rulesets.","url":"https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/managed-rulesets/create-exception/
  schema: 1
---
<p>Use <a href="/waf/managed-rules/waf-exceptions/">exceptions</a> to skip the execution of a managed ruleset of some of its rules.</p>
<p>The exception configuration includes an <a href="/ruleset-engine/rules-language/expressions/">expression</a> that defines the skip conditions, and the rules or managed rulesets to skip under those conditions.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/waf-managed-rulesets/#configure-exceptions">Configure exceptions</a> in the Terraform documentation.</p>
<p>If you are using the Cloudflare dashboard, refer to <a href="/waf/managed-rules/waf-exceptions/define-dashboard/">Add an exception in the dashboard</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13276.md")
</aside>
<h2 id="types-of-exceptions">Types of exceptions</h2>
<p>An exception can have one of the following behaviors (from highest to lowest priority):</p>
<ul>
<li><a href="#skip-all-remaining-rules">Skip all remaining rules in the entry point ruleset</a></li>
<li><a href="#skip-one-or-more-managed-rulesets">Skip one or more managed rulesets</a></li>
<li><a href="#skip-one-or-more-rules-of-managed-rulesets">Skip one or more rules of managed rulesets</a></li>
</ul>
<p>You define exceptions in a given context — zone level or account level — and they apply only to that context. For example, if you define an exception that skips all remaining rules at the account level, the rules defined in the entry point ruleset at the zone level will still be evaluated.</p>
<p>If there is a match for the expressions of several exceptions, Cloudflare will consider the exception with the highest priority.</p>
<p>Exceptions only apply to rules executing a managed ruleset listed after them. If you add an exception at the end of the list of rules of an entry point ruleset, nothing will be skipped.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="additional-requirement-for-account-level-exceptions">Additional requirement for account-level exceptions</h3>
@markup("md", "content/.markup/bodies/13275.md")
</aside>
<h3 id="skip-all-remaining-rules">Skip all remaining rules</h3>
<p>To skip all the remaining rules in the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a>, create a rule with <code>skip</code> action and include <code>&quot;ruleset&quot;: &quot;current&quot;</code> in the <code>action_parameters</code> object.</p>
<p>Example of rule definition:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;expression&quot;: &quot;&lt;RULE_EXPRESSION&gt;&quot;,&#10;	&quot;action&quot;: &quot;skip&quot;,&#10;	&quot;action_parameters&quot;: {&#10;		&quot;ruleset&quot;: &quot;current&quot;&#10;	}&#10;}&#10;</code></pre>
<p>Skipping all remaining rules only affects the rules in the current context (account or zone). For example, adding a rule with <code>skip</code> action to the account-level phase entry point ruleset has no impact on the rules defined in the zone-level phase entry point ruleset — these zone-level rules will still be evaluated.</p>
<p>For a full example, refer to the <a href="/waf/managed-rules/waf-exceptions/define-api/#skip-all-remaining-rules">WAF documentation</a>.</p>
<h3 id="skip-one-or-more-managed-rulesets">Skip one or more managed rulesets</h3>
<p>To skip one or more managed rulesets, create a rule with <code>skip</code> action containing a <code>rulesets</code> field in the <code>action_parameters</code> object. The <code>rulesets</code> field must contain a list of managed ruleset IDs you want to skip.</p>
<p>Example of rule definition:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;expression&quot;: &quot;&lt;RULE_EXPRESSION&gt;&quot;,&#10;	&quot;action&quot;: &quot;skip&quot;,&#10;	&quot;action_parameters&quot;: {&#10;		&quot;rulesets&quot;: [&quot;&lt;MANAGED_RULESET_1_ID&gt;&quot;, &quot;&lt;MANAGED_RULESET_2_ID&gt;&quot;]&#10;	}&#10;}&#10;</code></pre>
<p>For a full example, refer to the <a href="/waf/managed-rules/waf-exceptions/define-api/#skip-the-cloudflare-managed-ruleset">WAF documentation</a>.</p>
<h3 id="skip-one-or-more-rules-of-managed-rulesets">Skip one or more rules of managed rulesets</h3>
<p>To skip one or more rules of managed rulesets, create a rule with <code>skip</code> action containing a <code>rules</code> object in the <code>action_parameters</code> object. The <code>rules</code> object must contain one or more managed ruleset IDs as keys, and a list of rules to skip in those managed rulesets as the value of each key.</p>
<p>Example of a rule definition that skips rules <code>A</code> and <code>B</code> of managed ruleset <code>1</code>, and rule <code>X</code> of managed ruleset <code>2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;expression&quot;: &quot;&lt;RULE_EXPRESSION&gt;&quot;,&#10;	&quot;action&quot;: &quot;skip&quot;,&#10;	&quot;action_parameters&quot;: {&#10;		&quot;rules&quot;: {&#10;			&quot;&lt;MANAGED_RULESET_1_ID&gt;&quot;: [&quot;&lt;RULE_A_ID&gt;&quot;, &quot;&lt;RULE_B_ID&gt;&quot;],&#10;			&quot;&lt;MANAGED_RULESET_2_ID&gt;&quot;: [&quot;&lt;RULE_X_ID&gt;&quot;]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The rules in the <code>rules</code> object must belong to the specified managed rulesets, otherwise you will get an error.</p>
<p>For a full example, refer to the <a href="/waf/managed-rules/waf-exceptions/define-api/#skip-one-or-more-rules-of-waf-managed-rulesets">WAF documentation</a>.</p>
<hr />
<h2 id="additional-notes">Additional notes</h2>
<ul>
<li>Exceptions have priority over <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a>.</li>
<li>If you define an exception that skips all remaining rules, the expressions of those rules are not evaluated.</li>
<li>If you define an exception that skips a rule of a managed ruleset, the expression of the rule that executes the managed ruleset is evaluated and the managed ruleset rules are executed except for that specific rule, which is bypassed.</li>
</ul>
