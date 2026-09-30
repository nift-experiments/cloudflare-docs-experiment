---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/
  description: Require a specific cookie value in incoming requests.
  full_title: Require a specific cookie · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Require a specific cookie · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Require a specific cookie value in incoming requests."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/index.md"><meta property="og:title" content="Require a specific cookie · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Require a specific cookie value in incoming requests."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/#page","headline":"Require a specific cookie \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Require a specific cookie value in incoming requests.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies"]}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/require-specific-cookie/
  schema: 1
---
<p>To secure a sensitive area such as a development area, you can share a cookie with trusted individuals and then filter requests so that only users with that cookie can access your site.</p>
<p>Use the <a href="/ruleset-engine/rules-language/fields/reference/http.cookie/"><code>http.cookie</code></a> field to target requests based on the presence of a specific cookie.</p>
<p>This example comprises two <a href="/waf/custom-rules/create-dashboard/">custom rules</a>:</p>
<ul>
<li>Rule #1 targets requests to <code>dev.www.example.com</code> that have a specific cookie key, <code>devaccess</code>. As long as the value of the cookie key contains one of three authorized users — <code>james</code>, <code>matt</code>, or <code>michael</code> — the expression matches and the request is allowed, skipping all other custom rules.</li>
<li>Rule #2 blocks all access to <code>dev.www.example.com</code>.</li>
</ul>
<p>Since custom rules are evaluated in order, Cloudflare grants access to requests that satisfy rule 1 and blocks all other requests to <code>dev.www.example.com</code>:</p>
<p><strong>Rule #1:</strong></p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(http.cookie contains &quot;devaccess=james&quot; or http.cookie contains &quot;devaccess=matt&quot; or http.cookie contains &quot;devaccess=michael&quot;) and http.host eq &quot;dev.www.example.com&quot;</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Skip:</em></p>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
</ul>
<p><strong>Rule #2:</strong></p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td><code>equals</code></td>
<td><code>dev.www.example.com</code></td>
</tr>
</tbody>
</table>
<p>If using the expression editor:<br/>
<code>(http.host eq &quot;dev.www.example.com&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
