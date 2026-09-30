---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/
  description: Categories of rules in the HTTP DDoS Attack Protection managed ruleset.
  full_title: Rule categories — HTTP DDoS · Cloudflare DDoS Protection docs
  head_html: <title>Rule categories — HTTP DDoS · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Categories of rules in the HTTP DDoS Attack Protection managed ruleset."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/index.md"><meta property="og:title" content="Rule categories — HTTP DDoS · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Categories of rules in the HTTP DDoS Attack Protection managed ruleset."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/#page","headline":"Rule categories \u2014 HTTP DDoS \u00b7 Cloudflare DDoS Protection docs","description":"Categories of rules in the HTTP DDoS Attack Protection managed ruleset.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/http/rule-categories/
  schema: 1
---
<p>The main categories (or tags) of HTTP DDoS Attack Protection managed rules are the following:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>botnets</code></td>
<td>Rules for requests from known botnets, with very high accuracy and low risk of false positives. It is recommended that you keep these rules enabled.</td>
</tr>
<tr>
<td><code>unusual-requests</code></td>
<td>Rules for requests with suspicious characteristics that are not usually seen in legitimate traffic.</td>
</tr>
<tr>
<td><code>advanced</code></td>
<td>Rules related to features available to Advanced DDoS Protection customers, such as <a href="/ddos-protection/managed-rulesets/adaptive-protection/">Adaptive DDoS Protection</a>.</td>
</tr>
<tr>
<td><code>generic</code></td>
<td>Rules for detecting and mitigating floods of requests. These rules are useful for mitigating attacks that have no known signatures, but they may also trigger on unusually high volumes of legitimate traffic. To reduce the risk of false positives, their request per second (rps) activation threshold is higher. These rules either rate-limit or challenge traffic by default, but you can override them to block traffic if necessary.</td>
</tr>
<tr>
<td><code>read-only</code></td>
<td></td>
</tr>
</tbody>
</table>
Highly targeted rules for mitigating DDoS attacks with a high confidence rate. These rules are read-only — you cannot override their sensitivity level or action.
                                                                                                                                                                                                                                                                                                                                                     |
| `test`             | 
Rules used for testing the detection, mitigation, and alerting capabilities of Cloudflare's DDoS protection products.
                                                                                                                                                                                                                                                                                                                                                          |
