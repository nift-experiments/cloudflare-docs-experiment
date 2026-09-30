---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/
  description: Traffic detection signals including attack scores, bot scores, and leaked credentials.
  full_title: Traffic detections · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Traffic detections · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Traffic detection signals including attack scores, bot scores, and leaked credentials."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/index.md"><meta property="og:title" content="Traffic detections · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Traffic detection signals including attack scores, bot scores, and leaked credentials."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/#page","headline":"Traffic detections \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Traffic detection signals including attack scores, bot scores, and leaked credentials.","url":"https://developers.cloudflare.com/waf/detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/
  schema: 1
---
<p>Traffic detections check incoming requests for malicious, potentially malicious, or non-conforming activity. Each enabled detection scores or classifies requests by populating one or more fields. These fields appear as filters in the <a href="/waf/analytics/security-analytics/">Security Analytics</a> dashboard, and you can use them in rule expressions.</p>
<p>Detections are always on once enabled, even if you have not configured any security rules that use them. You can review detection results in <a href="/waf/analytics/security-analytics/">Security Analytics</a> to identify traffic patterns and spot potentially malicious traffic. For example, you can analyze traffic based on <a href="/waf/detections/attack-score/">attack score</a>, <a href="/bots/concepts/bot-score/">bot score</a>, <a href="/waf/detections/malicious-uploads/">content scan results</a>, or the <a href="/waf/detections/ai-security-for-apps/">presence of personally identifiable information (PII)</a> in large language model (LLM) prompts.</p>
<p><a href="/waf/detections/application-profiles/">Application Profiles</a> compare requests with application-specific expected structures. Profile detections do not mitigate traffic without a security rule.</p>
<p><a href="/waf/detections/attack-signature-detection/">Attack Signature Detection</a> evaluates requests against Cloudflare attack signatures. It exposes match metadata independently from mitigation.</p>
<p>Attack Signature Detection is available in Early Access. Contact your Cloudflare account team to request access.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="application-profiles-availability">Application Profiles availability</h3>
@markup("md", "content/.markup/bodies/15387.md")
</aside>
<p>Cloudflare provides the following detections:</p>
<ul class="directory-listing"><li><a href="/waf/detections/attack-score/">WAF attack score</a></li><li><a href="/waf/detections/attack-signature-detection/">Attack Signature Detection</a></li><li><a href="/waf/detections/application-profiles/">Application Profiles</a></li><li><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a></li><li><a href="/waf/detections/malicious-uploads/">Malicious uploads detection</a></li><li><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a></li><li><a href="/waf/detections/threat-intelligence/">Threat intelligence</a></li><li><a href="/bots/concepts/bot-score/">Bot score</a></li></ul>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Malicious uploads detection</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Paid add-on</td>
</tr>
<tr>
<td>Leaked credentials detection</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Leaked credentials fields</td>
<td>Password Leaked</td>
<td>Password Leaked, User and Password Leaked</td>
<td>Password Leaked, User and Password Leaked</td>
<td>All leaked credentials fields</td>
</tr>
<tr>
<td>Number of custom detection locations</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>10</td>
</tr>
<tr>
<td>Attack score</td>
<td>No</td>
<td>No</td>
<td>One field only</td>
<td>Yes</td>
</tr>
<tr>
<td>AI Security for Apps</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>For more information on bot score, refer to <a href="/bots/concepts/bot-score/">Bot scores</a>.</p>
<h2 id="turn-on-a-settings-managed-detection">Turn on a settings-managed detection</h2>
<p>For detections managed through Security settings:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15388.md")
</div>
<p>Detections enabled through Security settings run for all incoming traffic. Application Profiles instead evaluate requests after a learned or uploaded profile becomes available.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15386.md")
</aside>
<h2 id="more-resources">More resources</h2>
<p>For more information on detection versus mitigation, refer to <a href="/waf/concepts/#detection-versus-mitigation">Concepts</a>.</p>
