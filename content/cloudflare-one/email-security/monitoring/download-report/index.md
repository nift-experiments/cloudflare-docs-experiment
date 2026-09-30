---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/
  description: Download a report in Email Security.
  full_title: Download a report · Cloudflare One docs
  head_html: <title>Download a report · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Download a report in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/index.md"><meta property="og:title" content="Download a report · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Download a report in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/#page","headline":"Download a report \u00b7 Cloudflare One docs","description":"Download a report in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/monitoring/download-report/
  schema: 1
---
<p>Email security allows you to download three types of reports:</p>
<ul>
<li>Disposition report</li>
<li>Retro scan report</li>
<li>Security report</li>
</ul>
<h2 id="download-a-disposition-report">Download a disposition report</h2>
<p>A disposition report shows you all the email messages based on the type of disposition you selected.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Select <strong>Monitoring</strong> &gt; <strong>Download report</strong>.</li>
<li>In <strong>Report type</strong>, select <strong>Email disposition report</strong>.</li>
<li>Under <strong>Email disposition report</strong>, select the <strong>Date Range</strong> (required), and the <strong>Disposition</strong>.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">Dispositions and attributes</a> to learn more.</p>
<h2 id="download-a-retro-scan-report">Download a retro scan report</h2>
<p>Retro scan scans the last 14 days of your emails, and gives you a report on bulk, spam, spoof, suspicious and malicious emails.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Select <strong>Monitoring</strong> &gt; <strong>Download report</strong>.</li>
<li>In <strong>Report type</strong>, select <strong>Retro Scan report</strong>.</li>
<li>Select <strong>View report</strong> to view a report of your last 14 days of emails.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/email-security/retro-scan/">Retro Scan</a> to learn more.</p>
<h2 id="download-a-security-report">Download a security report</h2>
<p>A security report provides an overview of your email traffic. The report can be generated on the last 30, 60, 90 days, or a timeframe of your choice.</p>
<p>The reports contains:</p>
<ul>
<li>An executive summary: A summary of the threats detected in your organization's email traffic in the last 30 days.</li>
<li>Threat detection: Review metrics regarding dispositions, policy detection, and impersonation attempts.</li>
<li>Submissions: Review the metrics of emails your security team or users have requested to reclassify.</li>
</ul>
<p>To download a security report:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Select <strong>Monitoring</strong> &gt; <strong>Download report</strong>.</li>
<li>In <strong>Report type</strong>, select <strong>Security report</strong> and the <strong>Date range</strong>.</li>
<li>Select <strong>Generate report</strong>.</li>
<li>Your security report is being generated. You will receive an email with the security report attached once it is ready.</li>
</ol>
