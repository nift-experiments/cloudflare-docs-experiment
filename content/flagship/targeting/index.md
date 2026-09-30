---
cp9:
  canonical: https://developers.cloudflare.com/flagship/targeting/
  description: Serve different Flagship flag values to different users based on attributes, conditions, and logical grouping.
  full_title: Targeting rules · Cloudflare Flagship docs
  head_html: <title>Targeting rules · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve different Flagship flag values to different users based on attributes, conditions, and logical grouping."><link rel="canonical" href="https://developers.cloudflare.com/flagship/targeting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/targeting/index.md"><meta property="og:title" content="Targeting rules · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve different Flagship flag values to different users based on attributes, conditions, and logical grouping."><meta property="og:url" content="https://developers.cloudflare.com/flagship/targeting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/flagship/targeting/#page","headline":"Targeting rules \u00b7 Cloudflare Flagship docs","description":"Serve different Flagship flag values to different users based on attributes, conditions, and logical grouping.","url":"https://developers.cloudflare.com/flagship/targeting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/targeting/
  schema: 1
---
<p>Targeting rules let you serve different flag values to different users based on their attributes. Each flag can have zero or more rules.</p>
<p>Rules are evaluated in sequential order, from top to bottom. The first rule whose conditions match is used, and its configured variant is returned. If no rule matches, Flagship returns the flag's default variant.</p>
<p>When a flag is disabled, the default variant is always returned regardless of rules.</p>
<p>Place more specific rules before broader rules. A broad catch-all rule can prevent later rules from running.</p>
<h2 id="how-rules-work">How rules work</h2>
<p>A rule consists of:</p>
<ul>
<li><strong>Conditions</strong> — One or more attribute comparisons that must be satisfied. For example, <code>country equals &quot;US&quot;</code> or <code>plan in [&quot;enterprise&quot;, &quot;business&quot;]</code>.</li>
<li><strong>Serve variant</strong> — The variant to return when the rule matches.</li>
<li><strong>Rollout</strong> (optional) — A percentage-based gradual release. Only the specified percentage of matching users receive the rule's variant. The rest continue to the next rule.</li>
</ul>
<h2 id="condition-structure">Condition structure</h2>
<p>Each condition compares an attribute from the evaluation context against a value using an operator:</p>
<ul>
<li><strong>Attribute</strong> — The context key to evaluate (for example, <code>userId</code>, <code>country</code>, <code>plan</code>).</li>
<li><strong>Operator</strong> — The comparison to perform. Flagship supports <a href="/flagship/targeting/operators/">11 operators</a>.</li>
<li><strong>Value</strong> — The value to compare against. Can be a string, number, or array depending on the operator.</li>
</ul>
<p>If the evaluation context does not include the attribute referenced by a condition, that condition does not match.</p>
<h2 id="logical-grouping">Logical grouping</h2>
<p>Conditions within a rule can be grouped with <code>AND</code>/<code>OR</code> operators and nested up to five levels deep.</p>
<p>For example, to target enterprise users in the US or Canada:</p>
<ul>
<li><code>AND</code>:
<ul>
<li><code>plan equals &quot;enterprise&quot;</code></li>
<li><code>OR</code>:
<ul>
<li><code>country equals &quot;US&quot;</code></li>
<li><code>country equals &quot;CA&quot;</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Use the smallest set of context attributes necessary to express the rule. This keeps rule behavior easier to reason about and avoids sending unnecessary user data in evaluation context.</p>
<h2 id="learn-more">Learn more</h2>
<ul class="directory-listing"><li><a href="/flagship/targeting/operators/">Operators</a></li><li><a href="/flagship/targeting/percentage-rollouts/">Percentage rollouts</a></li></ul>
