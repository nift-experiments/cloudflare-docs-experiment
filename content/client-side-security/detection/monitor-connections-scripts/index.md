---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/
  description: View and filter scripts, connections, and cookies detected on your domain.
  full_title: Monitor resources and cookies · Client-side security docs
  head_html: <title>Monitor resources and cookies · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="View and filter scripts, connections, and cookies detected on your domain."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/index.md"><meta property="og:title" content="Monitor resources and cookies · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View and filter scripts, connections, and cookies detected on your domain."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/#page","headline":"Monitor resources and cookies \u00b7 Client-side security docs","description":"View and filter scripts, connections, and cookies detected on your domain.","url":"https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/detection/monitor-connections-scripts/
  schema: 1
---
<p>Once you <a href="/client-side-security/get-started/">activate client-side security's resource monitoring</a>, the main client-side resources dashboard will show which resources (scripts and connections) are running on your domain, as well as the cookies recently detected in HTTP traffic.</p>
<p>If you notice unexpected scripts or connections on the dashboard, check them for signs of malicious activity. Customers with Client-Side Security Advanced will have their <a href="/client-side-security/how-it-works/malicious-script-detection/">connections and scripts classified as potentially malicious</a> based on threat feeds. You should also check for any new or unexpected cookies.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/4001.md")
</aside>
<h2 id="use-the-client-side-resources-dashboards">Use the client-side resources dashboards</h2>
<p>To review the resources detected by Cloudflare:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4002.md")
</div>
<h2 id="view-all-reported-scripts-or-connections">View all reported scripts or connections</h2>
<p>The All Reported Connections and All Reported Scripts dashboards show all the detected resources including infrequent or inactive ones, reported in the last 30 days. After 30 days without any report, Cloudflare will delete information about a previously reported resource, and it will no longer appear in any of the dashboards.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4000.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4003.md")
</div>
<p>You can filter the data in these dashboards using different criteria, and print a report with the displayed records.</p>
<h2 id="view-details">View details</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3999.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4006.md")
</div>
<h2 id="export-data">Export data</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3997.md")
</aside>
<p>Use this feature to extract data for review and annotation. The data in the exported file will honor any filters you configure in the dashboard.</p>
<p>To export script, connection, or cookie information in CSV format:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4007.md")
</div>
