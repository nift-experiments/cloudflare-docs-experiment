---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/
  description: Retro Scan in Email Security.
  full_title: Retro Scan · Cloudflare One docs
  head_html: <title>Retro Scan · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Retro Scan in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/index.md"><meta property="og:title" content="Retro Scan · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retro Scan in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/#page","headline":"Retro Scan \u00b7 Cloudflare One docs","description":"Retro Scan in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/retro-scan/
  schema: 1
---
<p>Use Retro Scan to check whether your current email security provider has missed any threats. Cloudflare scans up to 14 days of emails in your Microsoft 365 mailbox and generates a report of malicious messages. Once the scan is complete, you will receive an email notification with a link to the report.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4502.md")
</aside>
<p>To start a free scan:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong> &gt; <strong>Overview</strong>.</li>
<li>Select <strong>Start a free scan</strong> &gt; <strong>Generate report</strong>.</li>
<li>Enable your <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">Microsoft integration</a>. Once you have enabled your Microsoft integration, you will be redirected to a page where you will add your domains and specify your current email security system.</li>
<li>Generate Retro Scan report:
<ul>
<li><strong>Connect domains</strong>: Select at least one domain from your integration, then select <strong>Continue</strong>.</li>
<li><strong>Select current solution</strong>: Select the email security tool you are currently using, then select <strong>Continue</strong>.</li>
<li><strong>Review details</strong>: Confirm the domain and current solution you selected, then select <strong>Continue</strong>. You will receive an email notification once the report is ready.</li>
</ul>
</li>
<li>When you receive the notification email, select the link to view the full report.</li>
<li>On the Cloudflare dashboard, select <strong>View report</strong>.</li>
</ol>
<p>The dashboard will display <strong>Overview</strong> and <strong>Details</strong> pages.</p>
<h3 id="overview">Overview</h3>
<p>The <strong>Overview</strong> page shows a summary of the scan results across your selected domains, including:</p>
<ul>
<li><a href="/cloudflare-one/email-security/monitoring/#disposition-evaluation">Disposition evaluation</a>, the verdict assigned to each scanned message (for example: malicious, suspicious, or spam)</li>
<li>Malicious threat types</li>
<li>Malicious targets, the top recipients targeted by malicious messages</li>
<li>Malicious threat origins</li>
</ul>
<h3 id="details">Details</h3>
<p>The <strong>Details</strong> page lists up to 1,000 emails that were assigned a disposition during the scan. Select any email to review <a href="/cloudflare-one/email-security/investigation/search-email/#details">details</a> about the message.</p>
