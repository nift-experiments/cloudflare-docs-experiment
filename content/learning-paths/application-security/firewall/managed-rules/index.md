---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/
  description: Deploy WAF managed rulesets for threat protection.
  full_title: Managed Rules · Cloudflare Learning Paths
  head_html: <title>Managed Rules · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Deploy WAF managed rulesets for threat protection."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/index.md"><meta property="og:title" content="Managed Rules · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy WAF managed rulesets for threat protection."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF,DDoS Protection,SSL/TLS,DNS,Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/#page","headline":"Managed Rules \u00b7 Cloudflare Learning Paths","description":"Deploy WAF managed rulesets for threat protection.","url":"https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/application-security/firewall/managed-rules/
  schema: 1
---
<p>Cloudflare provides pre-configured managed rulesets that protect against web application exploits such as the following:</p>
<ul>
<li>Zero-day vulnerabilities</li>
<li>Top-10 attack techniques</li>
<li>Use of stolen/leaked credentials</li>
<li>Extraction of sensitive data</li>
</ul>
<p>Managed rulesets are <a href="/waf/change-log/">regularly updated</a>. Each rule has a default action that varies according to the severity of the rule. You can adjust the behavior of specific rules, choosing from several possible actions.</p>
<p>Rules of managed rulesets have associated tags (such as <code>wordpress</code>) that allow you to search for a specific group of rules and configure them in bulk.</p>
<h2 id="rulesets">Rulesets</h2>
<p>By default, Cloudflare offers the following rulesets:</p>
<ul>
<li><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a></li>
<li><a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a></li>
<li><a href="/waf/managed-rules/reference/exposed-credentials-check/">Cloudflare Exposed Credentials Check Managed Ruleset</a></li>
</ul>
