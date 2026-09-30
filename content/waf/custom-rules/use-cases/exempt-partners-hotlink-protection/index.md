---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/
  description: Exempt partners from Hotlink Protection using custom rules.
  full_title: Exempt partners from Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Exempt partners from Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Exempt partners from Hotlink Protection using custom rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/index.md"><meta property="og:title" content="Exempt partners from Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Exempt partners from Hotlink Protection using custom rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/#page","headline":"Exempt partners from Hotlink Protection \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Exempt partners from Hotlink Protection using custom rules.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/exempt-partners-hotlink-protection/
  schema: 1
---
<p>When enabled, <a href="/waf/tools/scrape-shield/hotlink-protection/">Cloudflare Hotlink Protection</a> blocks all HTTP referrers that are not part of your domain or zone. That presents a problem if you allow partners to use inline links to your assets.</p>
<h2 id="allow-requests-from-partners-using-custom-rules">Allow requests from partners using custom rules</h2>
<p>You can use custom rules to protect against hotlinking while allowing inline links from your partners. In this case, you will need to disable <a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a> so that partner referrals are not blocked by that feature.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> uses the <a href="/ruleset-engine/rules-language/fields/reference/http.referer/"><code>http.referer</code></a> field to target HTTP referrals from partner sites.</p>
<p>The <code>not</code> operator matches HTTP referrals that are not from partner sites, and the action blocks them:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>not (http.referer contains &quot;example.com&quot; or http.referer eq &quot;www.example.net&quot; or http.referer eq &quot;www.cloudflare.com&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<h2 id="allow-requests-from-partners-using-configuration-rules">Allow requests from partners using Configuration Rules</h2>
<p>Alternatively, you can <a href="/rules/configuration-rules/create-dashboard/">create a configuration rule</a> to exclude HTTP referrals from partner sites from Hotlink Protection. In this case, you would keep the Hotlink Protection feature enabled.</p>
