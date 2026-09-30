---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/application-security/
  description: Protect web applications and APIs with Cloudflare Application security (WAF), DDoS protection, bot security, API Shield, and client-side security.
  full_title: Application security · Use cases · Cloudflare use cases
  head_html: <title>Application security · Use cases · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Protect web applications and APIs with Cloudflare Application security (WAF), DDoS protection, bot security, API Shield, and client-side security."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/application-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/application-security/index.md"><meta property="og:title" content="Application security · Use cases · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect web applications and APIs with Cloudflare Application security (WAF), DDoS protection, bot security, API Shield, and client-side security."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/application-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Use cases,WAF,DDoS Protection,Bots,API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/use-cases/application-security/#page","headline":"Application security \u00b7 Use cases \u00b7 Cloudflare use cases","description":"Protect web applications and APIs with Cloudflare Application security (WAF), DDoS protection, bot security, API Shield, and client-side security.","url":"https://developers.cloudflare.com/use-cases/application-security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/application-security/
  schema: 1
---
<p>Protect your website or application from attacks, bots, and abuse. Cloudflare's application security (also known as Web Application Firewall or WAF) blocks SQL injection, XSS, and OWASP Top 10 vulnerabilities. DDoS Protection mitigates volumetric and application-layer attacks automatically. Bot Security uses machine learning to score every request. API Shield validates API traffic against your OpenAPI specification. Client-side security monitors third-party scripts for malicious behavior.</p>
<ul class="directory-listing"><li><a href="/use-cases/application-security/block-attacks/">Block application attacks</a></li><li><a href="/use-cases/application-security/ddos/">Mitigate DDoS attacks</a></li><li><a href="/use-cases/application-security/bots/">Stop malicious bots</a></li><li><a href="/use-cases/application-security/client-side/">Protect against client-side threats</a></li><li><a href="/use-cases/application-security/api-endpoints/">Secure API endpoints</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="web-application-security">Web application security</h3>
<p>Protect a website or web application from common attacks:</p>
<ul>
<li><strong>SSL/TLS</strong> encrypts all traffic between visitors and Cloudflare</li>
<li><strong>Security rules</strong> managed rulesets block SQL injection, XSS, and OWASP Top 10 vulnerabilities</li>
<li><strong>DDoS Protection</strong> mitigates volumetric and application-layer attacks automatically</li>
<li><strong>Bot Security</strong> scores every request and blocks automated threats</li>
</ul>
<h3 id="api-security">API security</h3>
<p>Secure Application Programming Interface (API) endpoints with schema enforcement and authentication:</p>
<ul>
<li><strong>API Shield</strong> validates requests against your OpenAPI specification</li>
<li><strong>Rate Limiting</strong> prevents abuse with per-endpoint request limits</li>
<li><strong>mTLS</strong> authenticates known clients with mutual TLS certificates</li>
</ul>
<h3 id="client-side-defense">Client-side defense</h3>
<p>Protect visitors from threats that execute in the browser:</p>
<ul>
<li><strong>Client-side security</strong> monitors third-party scripts loading on your pages</li>
<li><strong>Turnstile</strong> replaces CAPTCHAs on forms with a privacy-preserving challenge</li>
<li><strong>Content security rules</strong> block requests from known malicious sources</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a>. All solutions in this use case require your domain's DNS records to be proxied through Cloudflare so that traffic passes through Cloudflare's network before reaching your origin.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15243.md")
</div>
