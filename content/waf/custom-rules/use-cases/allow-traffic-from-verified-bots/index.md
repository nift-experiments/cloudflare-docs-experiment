---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/
  description: Allow traffic from search engine and verified bots.
  full_title: Allow traffic from search engine bots and other verified bots · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Allow traffic from search engine bots and other verified bots · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Allow traffic from search engine and verified bots."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/index.md"><meta property="og:title" content="Allow traffic from search engine bots and other verified bots · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Allow traffic from search engine and verified bots."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/#page","headline":"Allow traffic from search engine bots and other verified bots \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Allow traffic from search engine and verified bots.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/allow-traffic-from-verified-bots/
  schema: 1
---
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> challenges requests from a list of countries, but allows traffic from search engine bots — such as Googlebot and Bingbot — and from other <a href="/bots/concepts/bot/verified-bots/">verified bots</a>.</p>
<p>The rule expression uses the <a href="/ruleset-engine/rules-language/fields/reference/cf.client.bot/"><code>cf.client.bot</code></a> field to determine if the request originated from a known good bot or crawler.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Country</td>
<td>is in</td>
<td><code>Mexico</code>, <code>United States</code></td>
<td>And</td>
</tr>
<tr>
<td>Known Bots</td>
<td>equals</td>
<td><code>false</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.country in {&quot;US&quot; &quot;MX&quot;} and not cf.client.bot)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Managed Challenge</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/challenge-bad-bots/">Use case: Challenge bad bots</a></li>
<li><a href="/bots/">Cloudflare bot solutions</a></li>
<li><a href="/waf/troubleshooting/blocked-bing-site-scans/">Troubleshooting: Bing's Site Scan blocked by a WAF managed rule</a></li>
<li><a href="https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/">Learning Center: What is a web crawler?</a></li>
</ul>
