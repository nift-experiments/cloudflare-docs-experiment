---
cp9:
  canonical: https://developers.cloudflare.com/network-interconnect/operational-guidance/
  description: Validate CNI failover and troubleshoot connectivity issues.
  full_title: Operational guidance · Cloudflare Network Interconnect docs
  head_html: <title>Operational guidance · Cloudflare Network Interconnect docs</title><meta name="generator" content="Nift"><meta name="description" content="Validate CNI failover and troubleshoot connectivity issues."><link rel="canonical" href="https://developers.cloudflare.com/network-interconnect/operational-guidance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-interconnect/operational-guidance/index.md"><meta property="og:title" content="Operational guidance · Cloudflare Network Interconnect docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Validate CNI failover and troubleshoot connectivity issues."><meta property="og:url" content="https://developers.cloudflare.com/network-interconnect/operational-guidance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Interconnect"><meta name="algolia_product_filter" content="Network Interconnect"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network Interconnect"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-interconnect/operational-guidance/#page","headline":"Operational guidance \u00b7 Cloudflare Network Interconnect docs","description":"Validate CNI failover and troubleshoot connectivity issues.","url":"https://developers.cloudflare.com/network-interconnect/operational-guidance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-interconnect/operational-guidance/
  schema: 1
---
<p>For maintenance expectations and notifications, refer to <a href="/network-interconnect/maintenance/">Maintenance</a>.</p>
<h2 id="customer-responsibility">Customer responsibility</h2>
<p>Your CNI deployment must tolerate an unplanned outage on any single circuit at any time. This means:</p>
<ul>
<li>Traffic failover between redundant circuits must be automatic.</li>
<li>If your operations require manual intervention to reroute traffic during maintenance, your configuration needs review.</li>
<li>Contact your account team to validate your failover design.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When facing connectivity problems, your first action should be to check for broader service disruptions. Visit <a href="https://www.cloudflarestatus.com/">Cloudflare Status</a> to see if any scheduled maintenance or active incidents are impacting services. This helps determine if the issue originates outside your network. Refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>
<p>If no system-wide problems are reported, gather the following information before submitting a support case. Providing comprehensive details facilitates a faster resolution:</p>
<ul>
<li><strong>Timeline</strong>: When the issue began and ended (if applicable), including the timezone.</li>
<li><strong>Identification</strong>: The CNI IP address or point-to-point prefix for the impacted CNI. If your CNI is part of a Magic setup, please also provide the name of the Magic Transit/WAN interconnect as listed in your dashboard.</li>
<li><strong>Physical Layer</strong>: Light levels of the CNI link (if applicable).</li>
<li><strong>Service Impact</strong>: Confirmation whether Magic Transit / WAN traffic was affected.</li>
<li><strong>Problem Description</strong>: A clear summary of the issue (for example, CNI down, Border Gateway Protocol (BGP) session down, prefixes withdrawn).</li>
</ul>
