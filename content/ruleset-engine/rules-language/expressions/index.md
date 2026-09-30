---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/
  description: Write expressions that match request characteristics for rule evaluation.
  full_title: Rule expressions · Cloudflare Ruleset Engine docs
  head_html: <title>Rule expressions · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Write expressions that match request characteristics for rule evaluation."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/index.md"><meta property="og:title" content="Rule expressions · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write expressions that match request characteristics for rule evaluation."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/#page","headline":"Rule expressions \u00b7 Cloudflare Ruleset Engine docs","description":"Write expressions that match request characteristics for rule evaluation.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rules-language/expressions/
  schema: 1
---
<p>The Rules language supports two kinds of expressions: simple and compound.</p>
<h2 id="simple-expressions">Simple expressions</h2>
<p><strong>Simple expressions</strong> compare a value from an HTTP request to a value defined in the expression. For example, this simple expression matches Microsoft Exchange Autodiscover requests:</p>
<pre tabindex="0"><code class="language-txt">http.request.uri.path matches &quot;/autodiscover\.(xml|src)$&quot;&#10;</code></pre>
<p>Simple expressions have the following syntax:</p>
<pre tabindex="0"><code class="language-txt">&lt;field&gt; &lt;comparison_operator&gt; &lt;value&gt;&#10;</code></pre>
<p>Where:</p>
<ul>
<li>
<p><a href="/ruleset-engine/rules-language/fields/">Fields</a> specify properties associated with an HTTP request.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/operators/#comparison-operators">Comparison operators</a> define how values must relate to actual request data for an expression to return <code>true</code>.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/values/">Values</a> represent the data associated with fields. When evaluating a rule, Cloudflare compares these values with the actual data obtained from the request.</p>
</li>
</ul>
<h2 id="compound-expressions">Compound expressions</h2>
<p><strong>Compound expressions</strong> use <a href="/ruleset-engine/rules-language/operators/#logical-operators">logical operators</a> such as <code>and</code> to combine two or more expressions into a single expression.</p>
<p>For example, this expression uses the <code>and</code> operator to target requests to <code>www.example.com</code> that are not on ports 80 or 443:</p>
<pre tabindex="0"><code class="language-txt">http.host eq &quot;www.example.com&quot; and not cf.edge.server_port in {80 443}&#10;</code></pre>
<p>Compound expressions have the following general syntax:</p>
<pre tabindex="0"><code class="language-txt">&lt;expression&gt; &lt;logical_operator&gt; &lt;expression&gt;&#10;</code></pre>
<p>Compound expressions allow you to generate sophisticated, highly targeted rules.</p>
<h2 id="maximum-rule-expression-length">Maximum rule expression length</h2>
<p>The maximum length of a rule expression is 4,096 characters.</p>
<p>This limit applies whether you use the visual <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a> to define your expression, or write the expression manually in the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a>.</p>
<h2 id="maximum-regular-expressions-per-rule">Maximum regular expressions per rule</h2>
<p>Each rule can contain a maximum of 64 regular expressions in its expression. This limit applies across all rule types that use the <a href="/ruleset-engine/rules-language/">Rules language</a>.</p>
<p>Rules that exceed this limit cannot be created or updated. Existing rules above this limit continue to work but cannot be modified until the expression is simplified.</p>
<h2 id="additional-features">Additional features</h2>
<p>You can also use the following Rules language features in your expressions:</p>
<ul>
<li>
<p><a href="/ruleset-engine/rules-language/operators/#grouping-symbols">Grouping symbols</a> allow you to explicitly group expressions that should be evaluated together.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/functions/">Functions</a> allow you to manipulate and validate values in expressions.</p>
</li>
</ul>
