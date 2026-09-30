---
cp9:
  canonical: https://developers.cloudflare.com/security/security-insights/how-it-works/
  description: How Security Insights scans your account and produces security findings.
  full_title: How it works · Security dashboard docs
  head_html: <title>How it works · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="How Security Insights scans your account and produces security findings."><link rel="canonical" href="https://developers.cloudflare.com/security/security-insights/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/security-insights/how-it-works/index.md"><meta property="og:title" content="How it works · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Security Insights scans your account and produces security findings."><meta property="og:url" content="https://developers.cloudflare.com/security/security-insights/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/security-insights/how-it-works/#page","headline":"How it works \u00b7 Security dashboard docs","description":"How Security Insights scans your account and produces security findings.","url":"https://developers.cloudflare.com/security/security-insights/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/security-insights/how-it-works/
  schema: 1
---
<p>Cloudflare runs regular security scans on your account. These scans check your Cloudflare account settings, DNS record configurations, and product configurations — such as SSL/TLS, WAF, and Access — across all domains in your account.</p>
<p>Each scan compares your current configuration against a set of ideal product configurations that indicate a strong security posture. When your configuration does not match an ideal configuration for one or more checks, the scan produces a <strong>Security Insight</strong> — a finding that represents a potential risk.</p>
<p>The <a href="/security/security-insights/">list of insights</a> may include potential security threats, vulnerabilities, compliance risks, insecure configurations, or any other identified risks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13847.md")
</aside>
<h2 id="scan-properties">Scan properties</h2>
<p>Each insight has the following properties:</p>
<ul>
<li><strong>Severity</strong>: The security risk of the insight. The severity values are: <em>Low</em>, <em>Moderate</em>, and <em>Critical</em>. The higher the severity level, the higher the risk of threat to your environment.</li>
<li><strong>Insight</strong>: The insight description detailing the current configuration that is causing the risk or vulnerability.</li>
<li><strong>Risk</strong>: A description of the risk associated with not addressing the issue.</li>
<li><strong>Type</strong>: The insight category.</li>
</ul>
<p>For a full list of insight types and their descriptions, refer to <a href="/security/security-insights/">Security Insights</a>.</p>
<h2 id="scan-frequency">Scan frequency</h2>
<p>Cloudflare performs scans automatically for all accounts and zones by default. On-demand scans are available on all plans:</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Scan Frequency</th>
<th>On-Demand</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free</td>
<td>Every 7 days</td>
<td>Yes</td>
</tr>
<tr>
<td>Pro and Business</td>
<td>Every 3 days</td>
<td>Yes</td>
</tr>
<tr>
<td>Enterprise</td>
<td>Daily</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13846.md")
</aside>
<p>All accounts can also manually start a scan from the <strong>Security Insights</strong> page in the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
