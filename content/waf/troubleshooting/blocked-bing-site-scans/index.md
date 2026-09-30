---
cp9:
  canonical: https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/
  description: A WAF managed rule may block site scans performed by Bing Webmaster Tools.
  full_title: Bing's Site Scan blocked by a managed rule · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Bing&#x27;s Site Scan blocked by a managed rule · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="A WAF managed rule may block site scans performed by Bing Webmaster Tools."><link rel="canonical" href="https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/index.md"><meta property="og:title" content="Bing&#x27;s Site Scan blocked by a managed rule · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A WAF managed rule may block site scans performed by Bing Webmaster Tools."><meta property="og:url" content="https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Microsoft,Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/#page","headline":"Bing's Site Scan blocked by a managed rule \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"A WAF managed rule may block site scans performed by Bing Webmaster Tools.","url":"https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft","Debugging"]}</script>
  markdown: true
  noindex: false
  route: /waf/troubleshooting/blocked-bing-site-scans/
  schema: 1
---
<p>Microsoft <a href="https://www.bing.com/webmaster/tools">Bing Webmaster Tools</a> provides a Site Scan feature that crawls your website searching for possible SEO improvements.</p>
<p>Site Scan does not use the same IP address range as Bingbot (Bing's website crawler). Additionally, the <a href="https://www.bing.com/toolbox/verify-bingbot">Verify Bingbot</a> tool does not recognize Site Scan's IP addresses as Bingbot. Due to this reason, the WAF managed rule that blocks fake Bingbot requests may trigger for Site Scan requests. This is a known issue of Bing Webmaster Tools.</p>
<p>To allow Site Scan to run on your website, Cloudflare recommends that you temporarily skip the triggered WAF managed rule by creating an <a href="/waf/managed-rules/waf-exceptions/">exception</a>. After the scan finishes successfully, delete the exception to start blocking fake Bingbot requests again.</p>
<p>The rule you should temporarily skip is the following:</p>
<table>
<thead>
<tr>
<th></th>
<th>Name</th>
<th>ID</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Managed Ruleset</strong></td>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code></td>
</tr>
<tr>
<td><strong>Rule</strong></td>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td><code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code></td>
</tr>
</tbody>
</table>
<p>The exception, shown as a rule with a <strong>Skip</strong> action, must appear in the rules list before the rule executing the Cloudflare Managed Ruleset, or else nothing will be skipped.</p>
<p>To check the rule order, use one of the following methods:</p>
<ul>
<li>When using the old Cloudflare dashboard, the rules listed in <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> run in order.</li>
<li>When using the new security dashboard, the rules listed in <strong>Security</strong> &gt; <strong>Security rules</strong> run in order.</li>
<li>When using the Cloudflare API, the rules in the <code>rules</code> object obtained using the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation (for your zone and for the <code>http_request_firewall_managed</code> phase) run in order.</li>
</ul>
<p>For more information on creating exceptions, refer to <a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a>.</p>
