---
cp9:
  canonical: https://developers.cloudflare.com/security/security-insights/review-insights/
  description: Review, filter, and resolve security insights detected across your domains.
  full_title: Review Security Insights · Security dashboard docs
  head_html: <title>Review Security Insights · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Review, filter, and resolve security insights detected across your domains."><link rel="canonical" href="https://developers.cloudflare.com/security/security-insights/review-insights/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/security-insights/review-insights/index.md"><meta property="og:title" content="Review Security Insights · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review, filter, and resolve security insights detected across your domains."><meta property="og:url" content="https://developers.cloudflare.com/security/security-insights/review-insights/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/security-insights/review-insights/#page","headline":"Review Security Insights \u00b7 Security dashboard docs","description":"Review, filter, and resolve security insights detected across your domains.","url":"https://developers.cloudflare.com/security/security-insights/review-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/security-insights/review-insights/
  schema: 1
---
<p>Check the <strong>Security Insights</strong> tab for a list of detected insights that you should address.</p>
<p>For each detected insight, you can resolve it or archive it, after understanding its risks.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next to the insight you wish to address, select <strong>Details</strong> to review it.</li>
</ol>
<h2 id="resolve-an-insight">Resolve an insight</h2>
<aside class="nb-aside warning">
@markup("md", "content/.markup/bodies/13843.md")
</aside>
<p>In the Resolve insights page, if you choose to update a configuration based on the recommendation actions, follow the instructions on the insight details page.</p>
<p>The following insights follow a different yet straightforward workflow to be resolved:</p>
<ul>
<li><strong>Minimum Version of TLS 1.2 not enforced</strong>: To resolve this insight:
<ul>
<li>Go to <strong>SSL/TLS</strong> &gt; <strong>Edge Certificates</strong>.</li>
<li>Select <strong>TLS 1.2</strong>.</li>
</ul>
</li>
<li><strong>Domains without &quot;Always use HTTPS&quot;</strong>: To resolve this insight:
<ul>
<li>Go to <strong>SSL/TLS</strong> &gt; <strong>Edge Certificates</strong>.</li>
<li>Select <strong>Always Use HTTPS</strong>.</li>
</ul>
</li>
<li><strong>Turn on JavaScript Detections</strong>: To resolve this insight:
<ul>
<li>Go to <strong>Security</strong> &gt; <strong>Bots</strong> &gt; Select <strong>Configure Bot Management</strong>.</li>
<li>Select <strong>JavaScript Detections</strong>.</li>
</ul>
</li>
</ul>
<h2 id="export-insights">Export insights</h2>
<p>You can export security insights to a CSV format directly from the dashboard.</p>
<p>To export security insights:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Export insights</strong>.</li>
</ol>
<p>Exporting security insights allow you to perform a deeper analysis of your insights.</p>
<p>The exported CSV file includes information such as the severity of your data, insight type scan date, issue class and additional optional fields, such as insight details, risk assessment, detection method, and recommended actions.</p>
<h2 id="archive-insights">Archive insights</h2>
<p>You can archive one or more insights from the dashboard.</p>
<p>To archive insights:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the insight(s) you want to archive, then select <strong>Archive selected</strong>.</li>
</ol>
<p>Alternatively, to archive an insight:</p>
<ol>
<li>Select the insight you want to archive and select <strong>Details</strong>. The dashboard will open a page where you will be able to review <a href="/security/security-insights/how-it-works/#scan-properties">insight properties</a>.</li>
<li>Select <strong>Archive insight</strong>.</li>
</ol>
<h2 id="enable-alerts">Enable alerts</h2>
<p>You can enable alerts for critical insights.</p>
<p>To enable alerts:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the security insight(s) you want to create an alert for, then select <strong>Create alert for selected classes</strong>.</li>
<li>Enter the notification name, and choose one or more insights classes to filter a notification.</li>
<li>Select <strong>Add email recipient</strong> and enter an email address to receive the alert.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
