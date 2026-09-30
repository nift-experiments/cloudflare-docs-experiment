---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/threat-intelligence/
  description: Match incoming requests against Cloudforce One threat intelligence in WAF rules.
  full_title: Threat intelligence · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Threat intelligence · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Match incoming requests against Cloudforce One threat intelligence in WAF rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/index.md"><meta property="og:title" content="Threat intelligence · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Match incoming requests against Cloudforce One threat intelligence in WAF rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/threat-intelligence/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Threat Intelligence"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/threat-intelligence/#page","headline":"Threat intelligence \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Match incoming requests against Cloudforce One threat intelligence in WAF rules.","url":"https://developers.cloudflare.com/waf/detections/threat-intelligence/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Threat Intelligence"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/threat-intelligence/
  schema: 1
---
<p>The threat intelligence detection matches incoming requests against indicators in the <a href="/security-center/cloudforce-one/">Cloudforce One</a> threat intelligence database. The detection matches on client IP address. If the IP was involved in threat activity in the past seven days, Cloudflare populates <a href="/waf/detections/threat-intelligence/fields/">threat intelligence fields</a> you can use in WAF rule expressions.</p>
<p>You can use these fields in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to match on:</p>
<ul>
<li>Known threat actor names (<code>cf.intel.ip.attacker_names</code>)</li>
<li>Industries the IP address has targeted (<code>cf.intel.ip.target_industries</code>)</li>
<li>Source and target countries of threat activity (<code>cf.intel.ip.attacker_countries</code>, <code>cf.intel.ip.target_countries</code>)</li>
<li>The dataset that flagged the IP address (<code>cf.intel.ip.datasets</code> — values: <code>ddos</code>, <code>waf</code>)</li>
</ul>
<p>You can review matches in <a href="/waf/analytics/security-analytics/">Security Analytics</a> to see which threat actors and campaigns are reaching your application.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15480.md")
</aside>
<h2 id="data-freshness">Data freshness</h2>
<p>The threat intelligence database reflects a rolling seven-day window:</p>
<ul>
<li>An IP address flagged earlier in the window still matches, even if the threat is no longer active.</li>
<li>An IP address ages out seven days after the last observed activity. Rules that matched it stop matching with no notification.</li>
</ul>
<h2 id="availability">Availability</h2>
<p>Requires an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. Contact your account team for access.</p>
<p>The WAF must be enabled on your zone before threat intelligence fields can be used in rule expressions.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/waf/detections/threat-intelligence/fields/">Threat intelligence fields</a> — Available fields and matching behavior.</li>
<li><a href="/waf/detections/threat-intelligence/get-started/">Get started</a> — Create your first threat intelligence rule.</li>
<li><a href="/security-center/cloudforce-one/">Threat Events</a> — Investigate threats in the Cloudforce One dashboard.</li>
</ul>
