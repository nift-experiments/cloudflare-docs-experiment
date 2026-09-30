---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/
  description: Resolve common issues with Digital Experience Monitoring (DEX), including data visibility problems and remote capture failures.
  full_title: Troubleshoot Digital Experience Monitoring · Cloudflare One docs
  head_html: <title>Troubleshoot Digital Experience Monitoring · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common issues with Digital Experience Monitoring (DEX), including data visibility problems and remote capture failures."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/index.md"><meta property="og:title" content="Troubleshoot Digital Experience Monitoring · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common issues with Digital Experience Monitoring (DEX), including data visibility problems and remote capture failures."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/#page","headline":"Troubleshoot Digital Experience Monitoring \u00b7 Cloudflare One docs","description":"Resolve common issues with Digital Experience Monitoring (DEX), including data visibility problems and remote capture failures.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/troubleshooting/
  schema: 1
---
<p>Review common troubleshooting scenarios for Digital Experience Monitoring (DEX).</p>
<h2 id="data-visibility">Data visibility</h2>
<h3 id="no-data-displayed-for-certain-users">No data displayed for certain users</h3>
If you do not see DEX data for specific users in your organization, verify the following:
<ul>
<li><strong>Client version</strong>: Ensure the users are running a version of the Cloudflare One Client that supports DEX.</li>
<li><strong>DEX enabled</strong>: Confirm that DEX is enabled for the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> assigned to those users.</li>
<li><strong>Traffic routing</strong>: DEX requires that traffic to Cloudflare's orchestration API is not blocked by local firewalls or SSL-inspecting proxies.</li>
</ul>
<h3 id="fleet-status-not-updating">Fleet status not updating</h3>
The Fleet status dashboard can take several minutes to reflect changes in device connectivity. If a device remains in an incorrect state, try disconnecting and reconnecting the Cloudflare One Client to force a status update.
<h2 id="remote-captures">Remote captures</h2>
<h3 id="remote-capture-fails-to-start">Remote capture fails to start</h3>
Remote captures require the Cloudflare One Client to be connected and able to communicate with the Cloudflare control plane. If a capture fails to start:
<ul>
<li>Verify the device status in the Zero Trust dashboard.</li>
<li>Ensure the device has sufficient disk space to store the capture files before upload.</li>
<li>Check for any local firewall rules that might be blocking the capture command.</li>
</ul>
<hr />
<h2 id="how-to-contact-support">How to contact Support</h2>
<p>If you cannot resolve the issue, <a href="/support/contacting-cloudflare-support/">open a support case</a>. Please provide a <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/">remote capture</a> from the Zero Trust dashboard for the affected device.</p>
