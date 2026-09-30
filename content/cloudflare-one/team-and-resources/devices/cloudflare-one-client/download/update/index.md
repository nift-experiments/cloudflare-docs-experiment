---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/
  description: How Update the Cloudflare One Client works in Zero Trust.
  full_title: Update the Cloudflare One Client · Cloudflare One docs
  head_html: <title>Update the Cloudflare One Client · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Update the Cloudflare One Client works in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/index.md"><meta property="og:title" content="Update the Cloudflare One Client · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Update the Cloudflare One Client works in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/#page","headline":"Update the Cloudflare One Client \u00b7 Cloudflare One docs","description":"How Update the Cloudflare One Client works in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/
  schema: 1
---
<p>This guide covers best practices for updating the Cloudflare One Client (formerly WARP).</p>
<h2 id="when-to-update-the-cloudflare-one-client">When to update the Cloudflare One Client</h2>
<p>There are two update strategies:</p>
<ul>
<li><strong>Always deploy the latest stable release</strong> (recommended) — You get the newest bug fixes, performance improvements, and features.</li>
<li><strong>Deploy only LTS releases</strong> — If your organization has limited update cycles due to change management, QA testing, or other constraints, you can skip intermediate stable releases and deploy only the latest <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/">LTS (Long-Term Support) release</a>. This strategy reduces deployment churn while still addressing security bug fixes in a timely manner.</li>
</ul>
<p>If you run into issues that require troubleshooting or support tickets, one of the first requested actions by our support team will be to update your clients to the latest version.</p>
<p>For more details on Cloudflare One Client support timelines and end-of-life (EOL) policies, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/">Support lifecycle</a> page.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/6105.md")
</aside>
<h2 id="how-to-update-the-cloudflare-one-client">How to update the Cloudflare One Client</h2>
<h3 id="windows-macos-and-linux">Windows, macOS, and Linux</h3>
<h4 id="managed-devices">Managed devices</h4>
<p>JAMF, Intune, and other MDM tools perform software updates by installing a new binary file. If you deployed the Cloudflare One Client using a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">device management tool</a>, the update procedure will look exactly the same as your initial installation. To update the Cloudflare One Client, push the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">latest binary file</a> with the same deployment parameters. End users will not be signed out of their client, and they will not have to manually engage with the update.</p>
<h4 id="devices-managed-from-the-cloudflare-dashboard">Devices managed from the Cloudflare dashboard</h4>
<p>On Windows and macOS devices running Cloudflare One Client version <code>2026.6.0</code> or later, you can assign a target client version to groups of devices directly from the Zero Trust dashboard. Matching devices silently install the target version on their next registration refresh, without requiring an MDM push or end-user action. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a>.</p>
<h4 id="unmanaged-devices">Unmanaged devices</h4>
<p>If your users have local administration rights on their device, you can allow them to update the Cloudflare One Client on their own via the client GUI. <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-updates"><strong>Allow updates</strong></a> is usually disabled on managed devices, as it can introduce version consistency control issues if client versions are centrally managed by IT.</p>
<h3 id="ios-android-and-chromeos">iOS, Android, and ChromeOS</h3>
<p>The iOS App Store and Google Play store can automatically push automatic updates to devices which have auto update enabled. We recommend using this method to keep the Cloudflare One Agent up-to-date on your mobile devices (managed or unmanaged).</p>
<h2 id="test-before-updates">Test before updates</h2>
<p>Most issues that occur after an update are due to compatibility issues between the Cloudflare One Client and third party security software. Before rolling out an update to your organization, be sure to test the new Cloudflare One Client release alongside your other software.</p>
<p>To deploy an update incrementally:</p>
<ol>
<li>Install the latest version of the Cloudflare One Client on a single device.</li>
<li>Verify connectivity in your Gateway logs, and verify that your third party software still works as expected.</li>
<li>Deploy the update to a few more devices that represent a broad set of configurations within your organization. For example, you could include devices from a variety of departments such as Engineering, Human Resources, and IT.</li>
<li>Verify connectivity for these devices.</li>
<li>Once everything is working, deploy the update to the rest of your organization.</li>
</ol>
