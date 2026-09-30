---
cp9:
  canonical: https://developers.cloudflare.com/rules/trace-request/limitations/
  description: Known limitations when using the Trace feature.
  full_title: Cloudflare Trace limitations · Cloudflare Rules docs
  head_html: <title>Cloudflare Trace limitations · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Known limitations when using the Trace feature."><link rel="canonical" href="https://developers.cloudflare.com/rules/trace-request/limitations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/trace-request/limitations/index.md"><meta property="og:title" content="Cloudflare Trace limitations · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Known limitations when using the Trace feature."><meta property="og:url" content="https://developers.cloudflare.com/rules/trace-request/limitations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/trace-request/limitations/#page","headline":"Cloudflare Trace limitations \u00b7 Cloudflare Rules docs","description":"Known limitations when using the Trace feature.","url":"https://developers.cloudflare.com/rules/trace-request/limitations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/trace-request/limitations/
  schema: 1
---
<h2 id="automatic-rule-bypasses">Automatic rule bypasses</h2>
<p>Trace does not display rules that are automatically bypassed for operational reasons.</p>
<p>For example, when SSL/TLS certificates are in <code>pending_validation</code> status, security rules are automatically disabled for domain control validation (DCV) paths like <code>/.well-known/pki-validation/</code> and <code>/.well-known/acme-challenge/</code>. These bypasses will not appear in trace results.</p>
<p>For more information, refer to <a href="/waf/troubleshooting/faq/#why-are-some-rules-bypassed-when-i-did-not-create-an-exception">Why are some rules bypassed?</a> in the WAF documentation.</p>
<hr />
<h2 id="unsupported-features">Unsupported features</h2>
<p>Trace currently does not support:</p>
<ul>
<li>Hostnames using <a href="/data-localization/">Data Localization Suite</a></li>
<li><a href="/spectrum/">Spectrum</a> applications</li>
</ul>
<p>Additionally, the following products will not appear in trace results:</p>
<ul>
<li><a href="/firewall/">Firewall rules (deprecated)</a></li>
<li><a href="/load-balancing/">Load Balancing</a> and <a href="/load-balancing/additional-options/load-balancing-rules/">Load Balancer Custom Rules</a></li>
<li><a href="/waf/tools/ip-access-rules/">IP Access rules</a></li>
<li><a href="/waf/reference/legacy/old-rate-limiting/">Rate limiting rules (previous version)</a></li>
<li><a href="/waf/reference/legacy/old-waf-managed-rules/">WAF managed rules (previous version)</a></li>
<li><a href="/client-side-security/rules/">Content security rules</a></li>
</ul>
