---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/security-level/
  description: Set the Security Level threshold for challenging suspicious visitors.
  full_title: Security Level · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Security Level · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Set the Security Level threshold for challenging suspicious visitors."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/security-level/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/security-level/index.md"><meta property="og:title" content="Security Level · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set the Security Level threshold for challenging suspicious visitors."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/security-level/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/security-level/#page","headline":"Security Level \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Set the Security Level threshold for challenging suspicious visitors.","url":"https://developers.cloudflare.com/waf/tools/security-level/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/security-level/
  schema: 1
---
<p>In the old Cloudflare dashboard, security level has the value <em>Always protected</em> and you cannot change this setting. To turn <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> on or off, use the separate toggle.</p>
<p>In the new security dashboard, the Cloudflare API, and in Terraform, use security level to turn Under Attack mode on or off.</p>
<p>Cloudflare's <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> performs additional security checks to help mitigate layer 7 DDoS attacks. When you enable Under Attack mode, Cloudflare will present a Managed Challenge page.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15337.md")
</aside>
<h2 id="threat-score">Threat score</h2>
<p>Previously, a threat score represented a Cloudflare threat score from 0–100, where 0 indicates low risk. Now, the threat score is always <code>0</code> (zero).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommendation">Recommendation</h3>
@markup("md", "content/.markup/bodies/15336.md")
</aside>
