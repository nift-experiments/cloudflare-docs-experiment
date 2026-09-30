---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/
  description: Email security logs in Zero Trust analytics.
  full_title: Email security logs · Cloudflare One docs
  head_html: <title>Email security logs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Email security logs in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/index.md"><meta property="og:title" content="Email security logs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Email security logs in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#page","headline":"Email security logs \u00b7 Cloudflare One docs","description":"Email security logs in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/logpush/email-security-logs/
  schema: 1
---
<p>Email security allows you to configure Logpush to export two types of log data: detection logs (records of threats identified in email traffic) and user action logs (records of administrative actions taken via the API or the dashboard). Each log type requires separate configuration.</p>
<h2 id="enable-detection-logs">Enable detection logs</h2>
<p>Detection logs record each threat identified by Email security, including metadata such as the message sender, recipient, and detection verdict.</p>
<p>To enable detection logs, refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a>. When configuring the Logpush job, select <strong>Email security alerts</strong> as the dataset.</p>
<h2 id="enable-user-action-logs">Enable user action logs</h2>
<p>User action logs record all administrative actions taken via the <a href="/api/resources/email_security/">API</a> or the dashboard.</p>
<p>Before you can enable user action logs for Email security, you must have a Logpush job configured for your storage destination. Refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a> to enable logs on destinations such as Cloudflare R2, HTTP, Amazon S3, and more.</p>
<p>Once you have configured your destination, you can set up user action logs:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your storage destination.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Under <strong>Configure logpush job</strong>:</li>
</ol>
<ul>
<li><strong>Job name</strong>: Enter the job name, if it is not already prepopulated.</li>
<li><strong>If logs match</strong> &gt; Select <strong>Filtered logs</strong> to capture only Email security events:
<ul>
<li><strong>Field</strong>: Choose <code>ResourceType</code> (the type of resource that was changed).</li>
<li><strong>Operator</strong>: Choose <code>starts with</code>.</li>
<li><strong>Value</strong>: Enter <code>email_security</code>.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>Select <strong>Submit</strong>.</li>
</ol>
<p>You can now view logs via the Cloudflare dashboard.</p>
