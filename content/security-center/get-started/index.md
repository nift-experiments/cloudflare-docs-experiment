---
cp9:
  canonical: https://developers.cloudflare.com/security-center/get-started/
  description: Use Security Insights to scan your account for misconfigurations and vulnerabilities.
  full_title: Get started · Cloudflare Security Center docs
  head_html: <title>Get started · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Security Insights to scan your account for misconfigurations and vulnerabilities."><link rel="canonical" href="https://developers.cloudflare.com/security-center/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Security Insights to scan your account for misconfigurations and vulnerabilities."><meta property="og:url" content="https://developers.cloudflare.com/security-center/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security-center/get-started/#page","headline":"Get started \u00b7 Cloudflare Security Center docs","description":"Use Security Insights to scan your account for misconfigurations and vulnerabilities.","url":"https://developers.cloudflare.com/security-center/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security-center/get-started/
  schema: 1
---
<p>Security Center scans your Cloudflare account configuration and identifies potential security risks, misconfigurations, and vulnerabilities across your domains. This guide covers the initial setup.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account.</li>
<li>At least one <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> (domain or subdomain) added to your Cloudflare account.</li>
</ul>
<h2 id="turn-security-insights-on-or-off">Turn Security Insights on or off</h2>
<p>Security Insights scans are enabled by default. Security Insights will scan your Cloudflare environment and provide you with a list of detected <a href="/security/security-insights/">insights</a>. Refer to <a href="/security/security-insights/how-it-works/">How it works</a> to learn more about how Security Insights perform a scan.</p>
<p>The initial scan time depends on the number of IT assets in all the domains of your Cloudflare account. When the scan is complete, the status of the page will change from <strong>Scan in Progress</strong> to <strong>Last scan performed on: <code>&lt;DATE_TIME&gt;</code></strong>.</p>
<p>You can decide to stop a scan, and restart a scan later.</p>
<p>To disable scans:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Disable Security Center scans</strong>, select <strong>Disable scans</strong>.</li>
</ol>
<p>To restart a scan:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Scan now</strong>.</li>
</ol>
<h3 id="start-a-new-scan">Start a new scan</h3>
<p>To manually start a scan:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Scan now</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/373.md")
</aside>
<h3 id="scan-frequency">Scan frequency</h3>
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
<p>For more details, refer to <a href="/security/security-insights/how-it-works/#scan-frequency">How it works</a>.</p>
