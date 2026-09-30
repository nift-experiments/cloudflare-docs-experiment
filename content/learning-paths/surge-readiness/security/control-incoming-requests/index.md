---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/
  description: Filter incoming requests with WAF rules.
  full_title: Control incoming requests · Cloudflare Learning Paths
  head_html: <title>Control incoming requests · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Filter incoming requests with WAF rules."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/index.md"><meta property="og:title" content="Control incoming requests · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Filter incoming requests with WAF rules."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF,Cache / CDN,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/#page","headline":"Control incoming requests \u00b7 Cloudflare Learning Paths","description":"Filter incoming requests with WAF rules.","url":"https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/surge-readiness/security/control-incoming-requests/
  schema: 1
---
<p>Use <a href="/waf/custom-rules/">Custom rules</a> to allow you to control incoming traffic by filtering requests to a zone. They work as customized web application firewall (WAF) rules that you can use to perform actions like Block or Managed Challenge on incoming requests.</p>
<p>Use WAF <a href="/waf/managed-rules/">Managed Rules</a> to apply custom criteria for all incoming HTTP requests.</p>
<h2 id="understand-hosting-plan-limits">Understand hosting plan limits</h2>
<p>Cloudflare offsets most of the load to your website via caching and request filtering, but some traffic will still pass through to your origin. Knowing the limits of your hosting plan can help prevent a bottleneck from your host.</p>
<p>Once you are aware of your plan limits, you can use <a href="/waf/rate-limiting-rules/">Rate Limiting</a> to restrict how many times a requesting entity can make a request to your website.</p>
<p>To help you define the best rate limiting setting for your use case, refer to <a href="/waf/rate-limiting-rules/request-rate/">How Cloudflare determines the request rate</a>.</p>
<h2 id="security-models">Security models</h2>
<ul>
<li>Positive Security policy: Allow specific requests and deny everything else.</li>
<li>Negative Security policy: Block specific requests and allow everything else.</li>
</ul>
<h2 id="actions">Actions</h2>
<ul>
<li>Log: Test rule effectiveness before committing to a more severe action.</li>
<li>Allow: Allow matching requests to access the site.</li>
<li>Block: Block matching requests from accessing the site.</li>
<li>Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before proceeding.</li>
<li>Interactive Challenge: Visitors will be shown an interactive challenge before proceeding.</li>
</ul>
