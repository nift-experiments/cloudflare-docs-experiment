---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/
  description: Manage domain access with IP rules.
  full_title: Control domain access · Cloudflare Learning Paths
  head_html: <title>Control domain access · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Manage domain access with IP rules."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/index.md"><meta property="og:title" content="Control domain access · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage domain access with IP rules."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF,Cache / CDN,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/#page","headline":"Control domain access \u00b7 Cloudflare Learning Paths","description":"Manage domain access with IP rules.","url":"https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/surge-readiness/security/control-domain-access/
  schema: 1
---
<p><a href="/waf/tools/ip-access-rules/">IP Access Rules</a> specify an action based on the origin of your user across a single domain or all of the domains in your account.</p>
<p>IP Access Rules can be applied based on:</p>
<ul>
<li>IPv4 address or range: Specified in CIDR notation as <code>/16</code> or <code>/24</code></li>
<li>IPv6 address or range: Specified in CIDR notation as <code>/32</code>, <code>/48</code>, <code>/64</code></li>
<li>ASN</li>
<li>Country or the Tor network</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10275.md")
</aside>
<p>Actions:</p>
<ul>
<li>Block: Ensures that an IP address will never be allowed to access your site.</li>
<li>Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before allowed access.</li>
<li>Interactive Challenge: Visitors will be shown an interactive challenge before allowed access.</li>
<li>Allowlist: Ensures that an IP address will never be blocked from accessing your site. This supersedes any Cloudflare security profile.</li>
</ul>
