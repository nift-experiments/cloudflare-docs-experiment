---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/added-detections/
  description: Manage Email security detection settings for domain age, encrypted attachments, anti-spam, and more.
  full_title: Added Detections · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Added Detections · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage Email security detection settings for domain age, encrypted attachments, anti-spam, and more."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/added-detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/added-detections/index.md"><meta property="og:title" content="Added Detections · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage Email security detection settings for domain age, encrypted attachments, anti-spam, and more."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/added-detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/enhanced-detections/added-detections/
  schema: 1
---
<p>With <strong>Added Detections</strong>, you can manage various configurations applied at the time of analyzing email traffic.</p>
<p>These settings apply particularly to trusted business partners that your organization may do business with (vendors, external providers, and more).</p>
<h2 id="available-configurations">Available configurations</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Malicious Domain Age</td>
<td>Controls the threshold for a <strong>Malicious</strong> <span class="nb-glossary-tooltip" title="disposition">disposition</span> based on domain age. Maximum of 120 days.</td>
</tr>
<tr>
<td>Suspicious Domain Age</td>
<td>Controls the threshold for a <strong>Suspicious</strong> <a href="/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a> based on domain age. Maximum of 120 days.</td>
</tr>
<tr>
<td>Encrypted Attachment Scanning</td>
<td>Auto-scans encrypted attachments to detect sophisticated malware campaigns.</td>
</tr>
<tr>
<td>Anti-Spam Engine</td>
<td>Detects bulk emails or unsolicited commercial emails and marks them with a <strong>Bulk</strong> <a href="/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a>.</td>
</tr>
<tr>
<td>Active Fraud Prevention</td>
<td>Inspects and assesses new domain traffic that could be launched from third-party partners or similar organizations.</td>
</tr>
<tr>
<td>Blank Email Detection</td>
<td>Detects emails with blank bodies and assigns a default disposition. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as <a href="/email-security/reference/dispositions-and-attributes/#dispositions">dispositions</a>.</td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Automated_clearing_house">ACH</a> change from free email detection</td>
<td>Detects payroll inquiries or change requests from free email domains. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as <a href="/email-security/reference/dispositions-and-attributes/#dispositions">dispositions</a>.</td>
</tr>
<tr>
<td>HTML attachment email detection</td>
<td>Detects HTM and HTML attachments in emails. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as <a href="/email-security/reference/dispositions-and-attributes/#dispositions">dispositions</a>.</td>
</tr>
</tbody>
</table>
<h2 id="access-added-detections">Access Added Detections</h2>
<p>To access <strong>Added Detections</strong> and potentially adjust your settings:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Enhanced Detections</strong> &gt; <strong>Added Detections</strong>.</li>
</ol>
<p>From this view, you can adjust <a href="#available-configurations">various configurations</a>.</p>
