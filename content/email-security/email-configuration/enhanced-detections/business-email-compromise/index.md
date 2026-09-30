---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/
  description: Protect against executive impersonation attacks with Email security BEC detection and directory integration.
  full_title: Business email compromise (BEC) · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Business email compromise (BEC) · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Protect against executive impersonation attacks with Email security BEC detection and directory integration."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/index.md"><meta property="og:title" content="Business email compromise (BEC) · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect against executive impersonation attacks with Email security BEC detection and directory integration."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/enhanced-detections/business-email-compromise/
  schema: 1
---
<p>Attackers often try to impersonate executives within an organization when sending malicious emails (with requests about banking information, trade secrets, etc.).</p>
<p>The <strong>Business email compromise (BEC)</strong> feature protects against these attacks by adding <a href="/email-security/reference/dispositions-and-attributes/#attributes">an attribute</a> to any spoofed email messages matching these sensitive email addresses. Information about key users you enter in the dashboard is used by Email security to run enhanced scan techniques and find these spoofed emails.</p>
<h2 id="setup">Setup</h2>
<p>You have several options for adding email addresses to BEC protection.</p>
<h3 id="using-the-dashboard">Using the dashboard</h3>
<p>Using the dashboard, you can add email addresses individually or upload a CSV file:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Enhanced Detections</strong>.</li>
<li>Select <strong>New Display Name</strong>.</li>
<li>Enter an email address manually or upload a CSV file.</li>
</ol>
<h4 id="csv-uploads">CSV uploads</h4>
<p>You can also upload a CSV file of multiple email addresses. The CSV file must be smaller than 150 KB, start with a header row of all required values, and contain no additional fields.</p>
<p>An example file would look like this:</p>
<pre tabindex="0"><code class="language-txt">Display_Name, Email&#10;Star Phish, star@nophish.com&#10;Phish Ee, phishee@nophish.com&#10;</code></pre>
<h3 id="integrating-a-directory">Integrating a directory</h3>
<p>If you want your BEC contacts automatically synced, Email security also supports directory integration for Microsoft and Gmail. Refer to <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/o365-directory-guide/">Office 365 directory guide</a> and <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/gworkspaces-directory-guide/">Google Workspaces directory integration</a> for more information.</p>
<h3 id="review-threats">Review threats</h3>
<p>Email security's dashboard has at-a-glance insights regarding BEC attacks, such as top email addresses targeted. Refer to <a href="/email-security/reporting/statistics-overview/">Statistics overview</a> and <a href="/email-security/reporting/types-malicious-detections/">Types of malicious detections</a> for more information.</p>
