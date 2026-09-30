---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/apis/protect-apis/
  description: Secure APIs against abuse and injection attacks with schema validation, rate limiting, mTLS, and WAF rules.
  full_title: Protect your APIs · Cloudflare use cases
  head_html: <title>Protect your APIs · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Secure APIs against abuse and injection attacks with schema validation, rate limiting, mTLS, and WAF rules."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/apis/protect-apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/apis/protect-apis/index.md"><meta property="og:title" content="Protect your APIs · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Secure APIs against abuse and injection attacks with schema validation, rate limiting, mTLS, and WAF rules."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/apis/protect-apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,API Shield,WAF,SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/apis/protect-apis/#page","headline":"Protect your APIs \u00b7 Cloudflare use cases","description":"Secure APIs against abuse and injection attacks with schema validation, rate limiting, mTLS, and WAF rules.","url":"https://developers.cloudflare.com/use-cases/apis/protect-apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/apis/protect-apis/
  schema: 1
---
<p>APIs are exposed to abuse, injection attacks, and unauthorized access. Cloudflare provides defense in depth with API Shield schema validation, per-endpoint rate limiting, mutual TLS (mTLS) client authentication, and security rules.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="api-shield">API Shield</h3>
<p>Discover, secure, and monitor your APIs. <a href="/api-shield/">Learn more about API Shield</a>.</p>
<ul>
<li><strong>Schema validation</strong> - Reject requests that do not conform to your OpenAPI specification before they reach your origin</li>
</ul>
<h3 id="rate-limiting">Rate Limiting</h3>
<p>Limit request rates based on flexible matching criteria. <a href="/waf/rate-limiting-rules/">Learn more about Rate Limiting</a>.</p>
<ul>
<li><strong>Rate limiting</strong> - Prevent abuse and volumetric attacks with per-IP or per-API-key request limits</li>
</ul>
<h3 id="mtls">mTLS</h3>
<p>Mutual TLS client certificate authentication. <a href="/ssl/client-certificates/">Learn more about mTLS</a>.</p>
<ul>
<li><strong>Client authentication</strong> - Require mutual TLS certificates for machine-to-machine communication</li>
</ul>
<h3 id="application-security">Application Security</h3>
<p>Get automatic protection from vulnerabilities and create your own custom rules. <a href="/waf/">Learn more about Application Security</a>.</p>
<ul>
<li><strong>Attack protection</strong> - Application security's managed rulesets block SQL injection, Cross-Site Scripting (XSS), and other injection attacks</li>
</ul>
<h3 id="access">Access</h3>
<p>Zero Trust access control for applications and infrastructure. <a href="/cloudflare-one/access-controls/policies/">Learn more about Access</a>.</p>
<ul>
<li><strong>Identity providers</strong> - Integrate with Okta, Azure AD, Google Workspace, and other identity providers (IdPs) to gate API access</li>
<li><strong>Service tokens</strong> - Issue long-lived credentials for machine-to-machine authentication between services</li>
</ul>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>JWT validation</strong> - Verify and decode JSON Web Tokens (JWTs) at the edge before requests reach your backend</li>
<li><strong>Custom auth logic</strong> - Build any authentication scheme — API keys, Hash-based Message Authentication Code (HMAC) signatures, custom headers — directly at the edge</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/api-shield/get-started/">API Shield get started</a></li>
<li><a href="/waf/rate-limiting-rules/">Configure rate limiting rules</a></li>
<li><a href="/ssl/client-certificates/">Set up mTLS authentication</a></li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/">Configure applications with Cloudflare Access</a></li>
<li><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a></li>
<li><a href="/workers/get-started/">Workers get started</a></li>
</ol>
