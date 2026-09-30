---
cp9:
  canonical: https://developers.cloudflare.com/waf/account/managed-rulesets/
  description: Deploy and manage WAF managed rulesets at the account level.
  full_title: Managed rulesets · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Managed rulesets · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy and manage WAF managed rulesets at the account level."><link rel="canonical" href="https://developers.cloudflare.com/waf/account/managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/account/managed-rulesets/index.md"><meta property="og:title" content="Managed rulesets · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy and manage WAF managed rulesets at the account level."><meta property="og:url" content="https://developers.cloudflare.com/waf/account/managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/account/managed-rulesets/#page","headline":"Managed rulesets \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Deploy and manage WAF managed rulesets at the account level.","url":"https://developers.cloudflare.com/waf/account/managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/account/managed-rulesets/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15426.md")
</aside>
<p>Cloudflare provides pre-configured managed rulesets that protect against web application exploits such as the following:</p>
<ul>
<li>Zero-day vulnerabilities</li>
<li>Top-10 attack techniques</li>
<li>Use of stolen/leaked credentials</li>
<li>Extraction of sensitive data</li>
</ul>
<p>Managed rulesets are <a href="/waf/change-log/">regularly updated</a>. Each rule has a default action that varies according to the severity of the rule. You can adjust the behavior of specific rules, choosing from several possible actions.</p>
<p>Rules of managed rulesets have associated tags (such as <code>wordpress</code>) that allow you to search for a specific group of rules and configure them in bulk.</p>
<h2 id="account-level-deployment">Account-level deployment</h2>
<p>At the zone level, each <a href="/waf/managed-rules/#available-managed-rulesets">WAF managed ruleset</a> can only be deployed once. At the account level, you can deploy each managed ruleset more than once. This allows you to apply the same ruleset with different configurations to different subsets of incoming traffic across the Enterprise zones in your account.</p>
<p>For example, you could deploy the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a> multiple times with different <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#paranoia-level">paranoia levels</a> and a different action (<em>Managed Challenge</em> action for PL3 and <em>Log</em> action for PL4). Higher paranoia levels enable additional rules that are more likely to produce false positives.</p>
<details class="nb-details"><summary>Example: Deploy OWASP with two different configurations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15430.md")
</div></details>
<h2 id="customize-the-behavior-of-managed-rulesets">Customize the behavior of managed rulesets</h2>
<p>To customize the behavior of managed rulesets, do one of the following:</p>
<ul>
<li><a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a> to skip the execution of managed rulesets or some of their rules under certain conditions.</li>
<li><a href="/waf/account/managed-rulesets/deploy-dashboard/#configure-a-managed-ruleset">Configure overrides</a> to change the rule action
or disable one or more rules of managed rulesets. Overrides can affect an
entire managed ruleset, specific tags, or specific rules in the managed
ruleset.</li>
</ul>
<p>Exceptions have priority over overrides.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15425.md")
</aside>
