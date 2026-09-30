---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/
  description: Available actions for IP Access rules.
  full_title: IP Access rules actions · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>IP Access rules actions · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Available actions for IP Access rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/index.md"><meta property="og:title" content="IP Access rules actions · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available actions for IP Access rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/#page","headline":"IP Access rules actions \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Available actions for IP Access rules.","url":"https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/ip-access-rules/actions/
  schema: 1
---
<p>An IP Access rule can perform one of the following actions:</p>
<ul>
<li>
<p><strong>Block</strong>: Prevents a visitor from visiting your site.</p>
</li>
<li>
<p><strong>Allow</strong>: Excludes visitors from all security checks, including <a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a>, <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a>, and the WAF. Use this option when a trusted visitor is being blocked by Cloudflare's default security features. The <em>Allow</em> action takes precedence over the <em>Block</em> action.<br/>Allowing a given country code will not bypass WAF managed rules (previous and new versions). Refer to <a href="/waf/tools/ip-access-rules/#important-remarks-about-allowingblocking-by-country">Important remarks about allowing/blocking by country</a> for more information.</p>
</li>
<li>
<p><strong>Managed Challenge</strong>: Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge from a list of possible actions. For more information, refer to <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Interstitial Challenge Pages</a>.</p>
</li>
<li>
<p><strong>Non-Interactive Challenge</strong>: Presents a non-interactive challenge page to visitors. Prevents bots from accessing the site.</p>
</li>
<li>
<p><strong>Interactive Challenge</strong>: Requires the visitor to complete an interactive challenge before visiting your site. Prevents bots from accessing the site.</p>
</li>
</ul>
