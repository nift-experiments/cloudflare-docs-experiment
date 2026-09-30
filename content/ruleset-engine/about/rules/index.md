---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/about/rules/
  description: Structure and properties of rules in the Ruleset Engine.
  full_title: Rules · Cloudflare Ruleset Engine docs
  head_html: <title>Rules · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Structure and properties of rules in the Ruleset Engine."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/about/rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/about/rules/index.md"><meta property="og:title" content="Rules · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Structure and properties of rules in the Ruleset Engine."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/about/rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/about/rules/#page","headline":"Rules \u00b7 Cloudflare Ruleset Engine docs","description":"Structure and properties of rules in the Ruleset Engine.","url":"https://developers.cloudflare.com/ruleset-engine/about/rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/about/rules/
  schema: 1
---
<p>A rule defines a filter and an action to perform on the incoming requests that match the filter.</p>
<ul>
<li>The rule <a href="/ruleset-engine/rules-language/expressions/">expression</a>, also called filter expression, defines the scope of the rule.</li>
<li>The rule <a href="/ruleset-engine/rules-language/actions/">action</a> defines what happens when there is a match for the expression.</li>
</ul>
<p>Rule expressions are defined using the <a href="/ruleset-engine/rules-language/">Rules language</a>.</p>
<p>For example, consider the following ruleset with four rules (R1, R2, R3, and R4). For a given incoming request, the expression of the first two rules matches the request properties. Therefore, the action for these rules runs (<em>Execute</em> and <em>Log</em>, respectively). The action of the first rule executes a managed ruleset, which means that every rule in the managed ruleset is evaluated. The action of the second rule logs an event associated with the current phase. There is no match for the expressions of rules 3 and 4, so their actions do not run. Since no rule blocks the request, it proceeds to the next phase.</p>
<p><img src="/assets/upstream/images/ruleset-engine/rulesets-rules-example.png" alt="Example of a rule execution scenario. Defines a ruleset with four rules, where the first rule executes a managed ruleset." /></p>
<p>Rules can have additional features through specific Cloudflare products. You may have more fields available for rule expressions, perform different actions, or configure additional behavior in a given phase.</p>
<h2 id="rule-evaluation">Rule evaluation</h2>
<p>When evaluating a rule, Cloudflare compares the values of request/response properties or derived values (obtained through <a href="/ruleset-engine/rules-language/fields/">fields</a>) to those defined in the rule's filter expression.</p>
<p>If the entire expression evaluates to <code>true</code>, there is a rule match and Cloudflare triggers the <a href="/ruleset-engine/rules-language/actions/">action</a> configured in the rule. If the expression evaluates to <code>false</code>, the rule does not match and its configured action is not applied.</p>
<p>Generally speaking, for <a href="/ruleset-engine/rules-language/actions/">non-terminating actions</a> the last change made by rules in the same <a href="/ruleset-engine/about/phases/">phase</a> will win (later rules can overwrite changes done by previous rules). However, for terminating actions (<em>Block</em>, <em>Redirect</em>, or one of the challenge actions), rule evaluation will stop and the action will be executed immediately.</p>
<p>For example, if multiple rules with the <em>Redirect</em> action match, Cloudflare will always use the URL redirect of the first rule that matches. Also, if you configure URL redirects using different Cloudflare products (Single Redirects and Bulk Redirects), the product executed first will apply, if there is a rule match (in this case, Single Redirects).</p>
<p>Refer to the <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for the product execution order.</p>
<p>When you use <code>true</code> as the rule filter expression, this means &quot;apply the rule to every incoming request&quot; at the current <a href="/ruleset-engine/about/phases/">phase</a> level, which can be zone or account.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/13291.md")
</aside>
<h3 id="field-values-during-rule-evaluation">Field values during rule evaluation</h3>
<p>While evaluating rules for a given request/response, the values of all request and response <a href="/ruleset-engine/rules-language/fields/">fields</a> are immutable within each phase. However, field values may change between phases.</p>
<p>For example:</p>
<ul>
<li>If a <a href="/rules/transform/url-rewrite/">URL rewrite rule</a> #1 updates the URI path or the query string of a request, URL rewrite rule #2 will not take these earlier changes into consideration.</li>
<li>If a <a href="/rules/transform/request-header-modification/">request header transform rule</a> #1 sets the value of an HTTP request header, request header transform rule #2 will not be able to read or evaluate this new value.</li>
<li>If a URL rewrite rule updates the URI path or query string of a request, the <code>http.request.uri</code>, <code>http.request.uri.*</code>, and <code>http.request.full_uri</code> fields will have a different value in phases after the <code>http_request_transform</code> phase (where URL Rewrite Rules are executed).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13290.md")
</aside>
