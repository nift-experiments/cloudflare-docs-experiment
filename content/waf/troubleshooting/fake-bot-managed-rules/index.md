---
cp9:
  canonical: https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/
  description: WAF managed rules that detect fake bots may block legitimate services that share infrastructure with known bots.
  full_title: Fake bot detection blocking legitimate requests · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Fake bot detection blocking legitimate requests · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="WAF managed rules that detect fake bots may block legitimate services that share infrastructure with known bots."><link rel="canonical" href="https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/index.md"><meta property="og:title" content="Fake bot detection blocking legitimate requests · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="WAF managed rules that detect fake bots may block legitimate services that share infrastructure with known bots."><meta property="og:url" content="https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/#page","headline":"Fake bot detection blocking legitimate requests \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"WAF managed rules that detect fake bots may block legitimate services that share infrastructure with known bots.","url":"https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /waf/troubleshooting/fake-bot-managed-rules/
  schema: 1
---
<p>The Cloudflare Managed Ruleset includes rules that detect requests impersonating well-known bots such as Googlebot and Bingbot. These rules compare the request's <code>User-Agent</code> header against known bot patterns and then verify the source using methods like reverse DNS lookup or IP validation. If the <code>User-Agent</code> matches a known bot but the source cannot be verified, the rule flags the request as a fake bot.</p>
<h2 id="fake-bot-rules">Fake bot rules</h2>
<p>The following table lists the fake bot detection rules in the Cloudflare Managed Ruleset:</p>
<table>
<thead>
<tr>
<th>Rule name</th>
<th>Rule ID</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anomaly:Header:User-Agent - Fake Google Bot</td>
<td><code class="nb-rule-id" title="ce11be543594412bb4bb92516aa0bef8">6aa0bef8</code></td>
</tr>
<tr>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td><code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code></td>
</tr>
</tbody>
</table>
<h2 id="common-false-positive-scenarios">Common false positive scenarios</h2>
<p>Fake bot rules may trigger false positives for legitimate services that share infrastructure or user agent patterns with known bots but use different IP ranges. Common examples include:</p>
<ul>
<li><strong>Google Cloud services</strong>: Services such as Google Cloud Workflows or Cloud Functions may send requests with a Google-related <code>User-Agent</code> header from IP addresses outside the standard Googlebot range. These requests fail the IP verification check and are flagged as fake Google bots.</li>
<li><strong>Bing Webmaster Tools Site Scan</strong>: Site Scan does not use the same IP range as Bingbot, causing the fake Bing bot rule to trigger. For specific guidance on this scenario, refer to <a href="/waf/troubleshooting/blocked-bing-site-scans/">Bing's Site Scan blocked by a managed rule</a>.</li>
<li><strong>Monitoring and testing tools</strong>: Third-party uptime monitors or automated testing tools that set a bot-like <code>User-Agent</code> header may also be flagged.</li>
</ul>
<h2 id="resolution">Resolution</h2>
<p>If a fake bot rule is blocking legitimate traffic, create an <a href="/waf/managed-rules/waf-exceptions/">exception</a> to skip the specific managed rule for the affected requests.</p>
<p>When defining the exception expression, use request properties that identify the legitimate traffic without broadly disabling the rule. For example:</p>
<ul>
<li>Filter by source IP address or IP range if the service uses a known set of addresses.</li>
<li>Filter by a specific URI path if the service only accesses certain endpoints.</li>
<li>Filter by ASN if the service originates from a specific network.</li>
</ul>
<p>The exception must appear in the rules list before the rule that executes the Cloudflare Managed Ruleset, or it will have no effect.</p>
<p>For instructions on creating exceptions, refer to <a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a>.</p>
