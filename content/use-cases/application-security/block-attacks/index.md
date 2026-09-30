---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/application-security/block-attacks/
  description: Protect against SQL injection, XSS, and other OWASP Top 10 vulnerabilities.
  full_title: Block application attacks · Cloudflare use cases
  head_html: <title>Block application attacks · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Protect against SQL injection, XSS, and other OWASP Top 10 vulnerabilities."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/application-security/block-attacks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/application-security/block-attacks/index.md"><meta property="og:title" content="Block application attacks · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect against SQL injection, XSS, and other OWASP Top 10 vulnerabilities."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/application-security/block-attacks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,WAF,Rate limiting"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/application-security/block-attacks/#page","headline":"Block application attacks \u00b7 Cloudflare use cases","description":"Protect against SQL injection, XSS, and other OWASP Top 10 vulnerabilities.","url":"https://developers.cloudflare.com/use-cases/application-security/block-attacks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/application-security/block-attacks/
  schema: 1
---
<p>Web applications face constant threats from SQL injection, Cross-Site Scripting (XSS), and other Open Web Application Security Project (OWASP) Top 10 vulnerabilities. Cloudflare WAF managed rulesets block these attacks automatically, and rate limiting prevents brute force abuse.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="application-security-waf">Application security (WAF)</h3>
<p>Get automatic protection from vulnerabilities and create your own custom rules. <a href="/waf/">Learn more about WAF</a>.</p>
<ul>
<li><strong>Managed rulesets</strong> - Pre-configured rules covering OWASP Top 10 and emerging threats, updated by Cloudflare</li>
<li><strong>Zero-day protection</strong> - Rules are updated as new vulnerabilities are discovered, with no action required from you</li>
<li><strong>Custom rules</strong> - Block or challenge requests based on any request attribute including headers, cookies, and IP reputation</li>
</ul>
<h3 id="rate-limiting">Rate limiting</h3>
<p>Limit request rates based on flexible matching criteria. <a href="/waf/rate-limiting-rules/">Learn more about rate limiting</a>.</p>
<ul>
<li><strong>Rate limiting</strong> - Prevent brute force attacks and Application Programming Interface (API) abuse with flexible per-endpoint request limits</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/waf/managed-rules/deploy-zone-dashboard/">Deploy WAF managed rulesets</a></li>
<li><a href="/waf/custom-rules/create-dashboard/">Create custom rules</a></li>
<li><a href="/waf/rate-limiting-rules/create-zone-dashboard/">Configure rate limiting rules</a></li>
</ol>
<p>For custom rules and rate limiting patterns specific to bot traffic, refer to <a href="/use-cases/solutions/stop-malicious-bots/">Stop malicious bots while allowing legitimate traffic (Free, Pro, and Business)</a>.</p>
