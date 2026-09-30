---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/reference/reports/
  description: View and share DDoS attack reports from the Cloudflare dashboard.
  full_title: DDoS reports · Cloudflare DDoS Protection docs
  head_html: <title>DDoS reports · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="View and share DDoS attack reports from the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/reference/reports/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/reference/reports/index.md"><meta property="og:title" content="DDoS reports · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View and share DDoS attack reports from the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/reference/reports/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/reference/reports/#page","headline":"DDoS reports \u00b7 Cloudflare DDoS Protection docs","description":"View and share DDoS attack reports from the Cloudflare dashboard.","url":"https://developers.cloudflare.com/ddos-protection/reference/reports/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/reference/reports/
  schema: 1
---
<p>To download an ad-hoc DDoS report, generate a PDF report file by selecting <strong>Print report</strong> in your <a href="/ddos-protection/reference/analytics/">analytics dashboard</a>.</p>
<p>WAF/CDN customers can download a monthly report in Account Home &gt; <strong>Security Center</strong>, by selecting <a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports</a> and downloading the desired monthly report.</p>
<p>Additionally, if you are a Magic Transit or Spectrum BYOIP customer, you will receive weekly DDoS reports by email with a snapshot of the DDoS attacks that Cloudflare detected and mitigated in the previous week.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/7454.md")
</aside>
<h2 id="weekly-ddos-reports">Weekly DDoS reports</h2>
<p>Cloudflare sends DDoS reports via email from <code>no-reply@notify.cloudflare.com</code> to users with the Super Administrator role on accounts with prefixes advertised by Cloudflare.</p>
<p>Reports contain the following information:</p>
<ul>
<li>Total number of DDoS attacks</li>
<li>Largest DDoS attack in packets per second (pps) and bits per second (bps)</li>
<li>Changes in DDoS attacks compared to the previous report</li>
<li>Top attack protocols</li>
<li>Top targeted IP addresses</li>
<li>Top targeted destination ports</li>
<li>Total potential downtime prevented (a sum of the duration of all attacks in that week)</li>
<li>Total bytes mitigated (a sum of all the mitigated attack traffic)</li>
</ul>
<p>Cloudflare issues DDoS reports via email each Tuesday. Reports summarize the attacks that occurred from Monday of the previous week to Sunday of the current week. For example, a report issued on 2020-11-10 (Tuesday) summarizes activity from 2020-11-02 (Monday) to 2020-11-08 (Sunday).</p>
<p>To receive real-time attack alerts, configure <a href="/ddos-protection/reference/alerts/">DDoS alerts</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/7453.md")
</aside>
<h3 id="example-report">Example report</h3>
<p>The following image shows an example DDoS report:</p>
<p><img src="/assets/upstream/images/ddos-protection/ddos-report-email.png" alt="Example email sent with a weekly DDoS report" /></p>
<p>When Cloudflare does not detect any L3/4 DDoS attacks in the prior week, Cloudflare sends a confirmation report:</p>
<p><img src="/assets/upstream/images/ddos-protection/ddos-report-no-attacks.png" alt="Example report email sent when Cloudflare does not detect any DDoS attack in the previous week" /></p>
<h3 id="manage-reporting-subscriptions">Manage reporting subscriptions</h3>
<p>Magic Transit and Spectrum BYOIP customers will receive the weekly DDoS report automatically.</p>
<p>To stop receiving DDoS reports, select the unsubscribe link at the bottom of the report email. To resubscribe after opting out, contact Cloudflare support.</p>
