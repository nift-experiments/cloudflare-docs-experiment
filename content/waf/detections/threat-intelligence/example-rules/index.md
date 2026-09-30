---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/
  description: Mitigate high-risk traffic using threat intelligence fields in WAF rules.
  full_title: Example rules using threat intelligence · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Example rules using threat intelligence · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Mitigate high-risk traffic using threat intelligence fields in WAF rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/index.md"><meta property="og:title" content="Example rules using threat intelligence · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Mitigate high-risk traffic using threat intelligence fields in WAF rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Threat Intelligence"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/#page","headline":"Example rules using threat intelligence \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Mitigate high-risk traffic using threat intelligence fields in WAF rules.","url":"https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Threat Intelligence"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/threat-intelligence/example-rules/
  schema: 1
---
<p><a href="/waf/custom-rules/">Custom rule</a> and <a href="/waf/rate-limiting-rules/">rate limiting rule</a> examples using <a href="/waf/detections/threat-intelligence/fields/">threat intelligence fields</a>. All fields are arrays — use <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> with <code>[*]</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15488.md")
</aside>
<h2 id="log-matches-before-blocking">Log matches before blocking</h2>
<p>Deploy with <em>Log</em> (Enterprise plans) to review matches before enforcing:</p>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.attacker_names[*] != &quot;&quot;)</code></li>
<li><strong>Action:</strong> <em>Log</em></li>
</ul>
<p>Review matches in <a href="/waf/analytics/security-events/">Security Events</a>, then change the action to <em>Block</em> or <em>Managed Challenge</em>.</p>
<h2 id="block-ddos-participants-targeting-your-region">Block DDoS participants targeting your region</h2>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="challenge-a-threat-actor-targeting-the-finance-sector">Challenge a threat actor targeting the finance sector</h2>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.target_industries[*] == &quot;Banking &amp; Financial Services&quot;) and any(cf.intel.ip.attacker_names[*] == &quot;BLACKBASTA&quot;)</code></li>
<li><strong>Action:</strong> <em>Managed Challenge</em></li>
</ul>
<h2 id="filter-by-attacker-country">Filter by attacker country</h2>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.attacker_countries[*] == &quot;CN&quot;)</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="combine-with-attack-score">Combine with attack score</h2>
<p>Block requests flagged by the WAF threat intelligence dataset that also have a low <a href="/waf/detections/attack-score/">attack score</a>:</p>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.datasets[*] == &quot;waf&quot;) and cf.waf.score lt 20</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="rate-limit-threat-actors-on-api-paths">Rate limit threat actors on API paths</h2>
<p><a href="/waf/rate-limiting-rules/">Rate limiting rule</a> applying a stricter rate to flagged IPs on your API:</p>
<ul>
<li><strong>Expression:</strong><br/>
<code>any(cf.intel.ip.datasets[*] == &quot;ddos&quot;) and starts_with(http.request.uri.path, &quot;/api/&quot;)</code></li>
<li><strong>Action:</strong> <em>Block</em> when the rate is exceeded.</li>
</ul>
