---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/ip-visibility/
  description: Reference information for IP visibility in Zero Trust analytics.
  full_title: IP visibility · Cloudflare One docs
  head_html: <title>IP visibility · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for IP visibility in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/ip-visibility/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/ip-visibility/index.md"><meta property="og:title" content="IP visibility · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for IP visibility in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/ip-visibility/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPv4,IPv6,Windows,Linux,MacOS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/ip-visibility/#page","headline":"IP visibility \u00b7 Cloudflare One docs","description":"Reference information for IP visibility in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/ip-visibility/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPv4","IPv6","Windows","Linux","MacOS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/ip-visibility/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4970.md")
</div></details>
<p>DEX's IP visibility gives administrators insight into three different IP types per device:</p>
<ol>
<li><strong>Device</strong>: The private IP address of an end-user device.</li>
<li><strong>ISP</strong>: The public IP that the ISP assigns when it routes the end-user device's traffic.</li>
<li><strong>Gateway</strong>: The router's private IP (the router the end device is connected to.)</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4969.md")
</aside>
<p>DEX's IP visibility supports both IPv6 and IPv4 addresses.</p>
<p>IP information helps IT administrators troubleshoot network issues and identify device locations. Common uses include:</p>
<ul>
<li>Identifying which access point or network segment a user is connected to</li>
<li>Verifying that network access control (NAC) policies are applied correctly</li>
<li>Diagnosing firewall restrictions on specific VLANs (virtual local area networks)</li>
<li>Troubleshooting Layer 2 (data link layer) and DHCP (Dynamic Host Configuration Protocol) issues</li>
<li>Indirectly determining user identity and device location</li>
</ul>
<h2 id="view-a-device-s-ip-information">View a device's IP information</h2>
<p>To view IP information for a user device:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select a device, then select <strong>View details</strong>.</li>
<li>Go to <strong>IP details</strong>.</li>
<li>Review the IP details for your selected device's most recent session.</li>
</ol>
<h2 id="view-a-device-s-ip-history">View a device's IP history</h2>
<p>DEX's IP visibility allows you to review an event log of a device's IP history for the last seven days. To view a device's IP history:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select a device &gt; <strong>View details</strong> &gt; go to <strong>IP details</strong>.</li>
<li>Select <strong>View all ISPs</strong>.</li>
</ol>
<h2 id="troubleshoot-with-ip-visibility">Troubleshoot with IP visibility</h2>
<p>While IP visibility allows you to inspect a device's IP information, use <a href="/cloudflare-one/insights/dex/monitoring/#available-metrics">DEX's live analytics</a> to review which Cloudflare data center the device is connected to. When traffic leaves a Cloudflare One Client-connected end-user device, it will hit a <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#identify-the-cloudflare-data-center-serving-your-request">Cloudflare data center</a>.</p>
<p>To find which Cloudflare data center a device is connected to:</p>
<ol>
<li>Follow the steps listed in <a href="#view-a-devices-ip-history">View IP information</a> to find a device's IP information.</li>
<li>On the device page, select <strong>Colocation &amp; client</strong> or find the <strong>Client</strong> table at the top of the page.</li>
<li>In the <strong>Client</strong> table, find <strong>Colocation</strong> to review which Cloudflare data center your selected device's outbound (egress) traffic is routed through.</li>
</ol>
