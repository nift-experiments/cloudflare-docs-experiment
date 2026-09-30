---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/
  description: Customize Network-layer DDoS Attack Protection rule actions and sensitivity levels.
  full_title: Network DDoS Attack Protection override rules · Cloudflare DDoS Protection docs
  head_html: <title>Network DDoS Attack Protection override rules · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize Network-layer DDoS Attack Protection rule actions and sensitivity levels."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/index.md"><meta property="og:title" content="Network DDoS Attack Protection override rules · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize Network-layer DDoS Attack Protection rule actions and sensitivity levels."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/#page","headline":"Network DDoS Attack Protection override rules \u00b7 Cloudflare DDoS Protection docs","description":"Customize Network-layer DDoS Attack Protection rule actions and sensitivity levels.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/network/network-overrides/
  schema: 1
---
<p>When Cloudflare's DDoS Protection systems detect an attack, an ephemeral mitigation rule is created and installed in-line to mitigate the attack. A mitigation rule is generated based on the logic of the DDoS Protection managed ruleset. Each mitigation rule is generated from a single managed rule.</p>
<p>All mitigations and its associated managed rules are evaluated in order by the DDoS systems one by one. Cloudflare will go through all of the rule overrides defined in the ruleset overrides until one matches the managed rule, and apply the action and stop at that point. Otherwise, the evaluation will continue in order until a rule matches.</p>
<p>You can create only one ruleset override that can contain one or multiple rule overrides.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7543.md")
</aside>
<p>A rule override instructs the DDoS system on the action it should take against the attack according to its matching managed rule.</p>
<p>However, within a rule override, specificity matters and the DDoS system will choose the more specific configuration. A rule override takes precedence over the ruleset override.</p>
<h2 id="example">Example</h2>
<p>A DDoS managed ruleset contains the following managed rules:</p>
<ul>
<li><strong>Managed rule 1</strong></li>
<li><strong>Managed rule 2</strong></li>
<li><strong>Managed rule 3</strong></li>
</ul>
<p>The following ruleset overrides have been configured:</p>
<ul>
<li><strong>Ruleset override A</strong>
<ul>
<li><strong>Managed rule 1</strong> is set to <code>block</code></li>
</ul>
</li>
<li><strong>Ruleset override B</strong>
<ul>
<li>The action of the entire ruleset (or <em>all managed rules</em>) is set to <code>Managed Challenge</code></li>
<li><strong>Managed rule 1</strong> is set to <code>log</code></li>
<li><strong>Managed rule 2</strong> is set to <code>log</code></li>
</ul>
</li>
<li><strong>Ruleset override C</strong>
<ul>
<li><strong>Managed rule 3</strong> is set to <code>log</code></li>
</ul>
</li>
</ul>
<h3 id="use-case">Use case</h3>
<p>A DDoS attack was detected on <strong>managed rules 1</strong>, <strong>2</strong>, and <strong>3</strong>, and has generated a mitigation rule.</p>
<ul>
<li>
<p>Since <strong>managed rule 1</strong> matches <strong>ruleset override A</strong>, Cloudflare will <code>block</code> the attacks and not proceed with the rest of the rules.</p>
</li>
<li>
<p><strong>Managed rule 2</strong> does not match <strong>ruleset override A</strong>, so Cloudflare proceeds to <strong>ruleset override B</strong>. <br /> <strong>Ruleset override B</strong> matches both all managed rules and <strong>managed rule 2</strong>, but specificity takes precedence. It does not <code>challenge</code> and instead proceeds with <code>log</code> since it matches the most specific managed rule.</p>
</li>
<li>
<p><strong>Managed rule 3</strong> does not match <strong>ruleset override A</strong>, so Cloudflare proceeds to <strong>rule override B</strong>. Since <strong>ruleset override B</strong> sets <em>all managed rules</em> to <code>challenge</code>, then Cloudflare does not proceed to <strong>ruleset override C</strong>.</p>
</li>
</ul>
<p>An additional dimension to take into account is Cloudflare’s DDoS systems will apply a given rule override only if its conditions are met — which includes the Sensitivity level. So, while it needs to match and modify the correct managed rule (or everything in the case of all managed rules above), it also has to meet the specified Sensitivity level of the rule.</p>
<ul>
<li>
<p><strong>Rule override A</strong></p>
<ul>
<li><em>All managed rules</em> are set to <code>challenge</code> at low sensitivity</li>
</ul>
</li>
<li>
<p><strong>Rule override B</strong></p>
<ul>
<li><strong>Managed rule 1</strong> is set to <code>log</code> at default sensitivity</li>
</ul>
</li>
</ul>
<p>You receive a small attack below the threshold for low sensitivity, but above the threshold for high sensitivity on <strong>managed rule 1</strong>.</p>
<ul>
<li><strong>Rule override A</strong> does not meet the low sensitivity threshold. Therefore, we do not match the override and do not mitigate the attack, but proceed to evaluate the next managed rule in case the rule override instructs DoS to mitigate.</li>
<li><strong>Rule override B</strong> sets <code>log</code> at default visibility, which matches the condition. So, the defined action is applied and attack traffic is logged.</li>
</ul>
