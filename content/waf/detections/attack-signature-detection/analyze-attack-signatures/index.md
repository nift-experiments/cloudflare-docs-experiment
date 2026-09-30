---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/
  description: Investigate attack signature matches, affected applications, request outcomes, and possible false positives in Security Analytics.
  full_title: Analyze attack signatures · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Analyze attack signatures · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Investigate attack signature matches, affected applications, request outcomes, and possible false positives in Security Analytics."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/index.md"><meta property="og:title" content="Analyze attack signatures · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Investigate attack signature matches, affected applications, request outcomes, and possible false positives in Security Analytics."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/#page","headline":"Analyze attack signatures \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Investigate attack signature matches, affected applications, request outcomes, and possible false positives in Security Analytics.","url":"https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/attack-signature-detection/analyze-attack-signatures/
  schema: 1
---
<p>Use <strong>Security Analytics</strong> &gt; <strong>Attack Analysis</strong> to investigate attack signature matches before applying mitigation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15542.md")
</aside>
<h2 id="review-signature-matches">Review signature matches</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15543.md")
</div>
<p>Use this analysis to identify common signatures and attack categories. You can also investigate a specific Common Vulnerabilities and Exposures (CVE) identifier or attack technique. Correlate the matches with <a href="/waf/detections/attack-score/">WAF Attack Score</a> to add another signal.</p>
<p>The request outcome shows whether existing protections mitigated matching traffic. It also helps identify requests served by Cloudflare or your origin. A detection does not apply an action by itself.</p>
<h2 id="interpret-confidence">Interpret confidence</h2>
<p>Confidence describes the expected false-positive characteristics of a signature. It does not prove that a request is malicious.</p>
<table>
<thead>
<tr>
<th>Confidence</th>
<th>Meaning</th>
<th>Comparison with Managed Rules</th>
<th>Recommended analysis</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>high</code></td>
<td>The signature targets a high true-positive and low false-positive rate.</td>
<td>Includes the same signatures that the default Managed Rules deployment enables.</td>
<td>Confirm affected traffic and current mitigation before applying a broad action.</td>
</tr>
<tr>
<td><code>low</code></td>
<td>The signature has a greater risk of matching legitimate application traffic.</td>
<td>Includes the Managed Rules signatures that are disabled by default.</td>
<td>Review requests and scope mitigation to the affected application surface.</td>
</tr>
</tbody>
</table>
<h2 id="investigate-possible-false-positives">Investigate possible false positives</h2>
<p>Legitimate rich-text input can match a generic cross-site scripting signature. For example, a content management or support application may accept HTML.</p>
<p>Filter the analysis to that hostname, path, and method. Review representative requests to distinguish expected content from attacks. Then create a scoped rule or exception instead of changing protection for the entire application.</p>
<h2 id="compare-results-with-managed-rules">Compare results with Managed Rules</h2>
<p>Each signature Ref matches the corresponding Managed Rule public Rule ID. Use this identifier to find the Managed Rule and compare the detection with your deployment.</p>
<p>Check the request outcome and <a href="/waf/analytics/security-events/">Security Events</a> before assuming Managed Rules blocked a match. Managed Rules actions and overrides determine their behavior.</p>
<h2 id="sampling">Sampling</h2>
<p>Attack Analysis uses <a href="/waf/analytics/security-analytics/#sampling">Security Analytics adaptive sampling</a>. Use <a href="/log-explorer/">Log Explorer</a> when you need 100% retention rather than sampled data.</p>
<p>After reviewing historical traffic, refer to <a href="/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/">Use attack signatures in Security Rules</a>.</p>
