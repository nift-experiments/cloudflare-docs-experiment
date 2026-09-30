---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/
  description: Learn how to deploy the Cloudflare One Client using JumpCloud.
  full_title: JumpCloud · Cloudflare One docs
  head_html: <title>JumpCloud · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to deploy the Cloudflare One Client using JumpCloud."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/index.md"><meta property="og:title" content="JumpCloud · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to deploy the Cloudflare One Client using JumpCloud."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/#page","headline":"JumpCloud \u00b7 Cloudflare One docs","description":"Learn how to deploy the Cloudflare One Client using JumpCloud.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/
  schema: 1
---
<h2 id="windows">Windows</h2>
<ol>
<li>
<p>Log in to the <a href="https://console.jumpcloud.com">JumpCloud Admin Portal</a>.</p>
</li>
<li>
<p>Go to <strong>Device Management</strong> &gt; <strong>Software Management</strong>.</p>
</li>
<li>
<p>Select the <strong>Windows</strong> tab, then select <strong>(+)</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/jumpcloud.png" alt="Configuring the Cloudflare One Client in the JumpCloud Windows tab" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol start="4">
<li>
<p>In the <strong>Software Name</strong> field, enter a unique display name.</p>
</li>
<li>
<p>In the <strong>Package ID</strong> field, enter <code>warp</code>.</p>
</li>
<li>
<p>Select <strong>Install this software</strong>.</p>
</li>
<li>
<p>(Optional) Select <strong>Keep software package up to date</strong> to automatically update this app as updates become available.</p>
</li>
<li>
<p>(Optional) Select <strong>Allow end users to delay updates for up to one week</strong> to avoid updates during a busy time.</p>
</li>
<li>
<p>Select <strong>save</strong>.</p>
</li>
<li>
<p>Select the device(s) you want to deploy the app to:</p>
<ul>
<li><strong>Single device</strong>: Go to the <strong>Devices</strong> tab and select the target device.</li>
<li><strong>Device group</strong>: Go to the <strong>Device Groups</strong> tab and select the target device group.</li>
</ul>
</li>
<li>
<p>Select <strong>save</strong>.</p>
</li>
<li>
<p>Select <strong>save</strong> again.</p>
</li>
</ol>
<p>Verify that the Cloudflare One Client was installed by selecting the app and viewing the <strong>Status</strong> tab.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h2 id="macos">macOS</h2>
<ol>
<li>
<p>Log in to the <a href="https://console.jumpcloud.com">JumpCloud Admin Portal</a>.</p>
</li>
<li>
<p>Go to <strong>Device Management</strong> &gt; <strong>Software Management</strong>.</p>
</li>
<li>
<p>Select the <strong>Apple</strong> tab, then select <strong>(+)</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/jumpcloud-mac.png" alt="Configuring the Cloudflare One Client in the JumpCloud Apple tab" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol start="4">
<li>
<p>In the <strong>Software Description</strong> field, enter a unique display name.</p>
</li>
<li>
<p>In the <strong>Software Package URL</strong>, enter the URL location of the <code>Cloudflare_WARP_&lt;VERSION&gt;.pkg</code> file. If you do not already have the installer package, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos">download it here</a>.</p>
</li>
<li>
<p>Select the device(s) you want to deploy the app to:</p>
<ul>
<li><strong>Single device</strong>: Go to the <strong>Devices</strong> tab and select the target device. To select all devices, select the checkbox next to <strong>Type</strong>.</li>
<li><strong>Device group</strong>: Go to the <strong>Device Groups</strong> tab and select the target device group. To select all device groups, select the checkbox next to <strong>Type</strong>.</li>
</ul>
</li>
<li>
<p>Select <strong>save</strong> to install the client.</p>
</li>
</ol>
<p>Verify that the Cloudflare One Client was installed by selecting the app and viewing the <strong>Status</strong> tab.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
