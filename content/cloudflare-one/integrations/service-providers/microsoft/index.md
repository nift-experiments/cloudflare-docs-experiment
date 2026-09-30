---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/
  description: Microsoft Endpoint Manager in Zero Trust integrations.
  full_title: Microsoft Endpoint Manager · Cloudflare One docs
  head_html: <title>Microsoft Endpoint Manager · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Microsoft Endpoint Manager in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/index.md"><meta property="og:title" content="Microsoft Endpoint Manager · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Microsoft Endpoint Manager in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/#page","headline":"Microsoft Endpoint Manager \u00b7 Cloudflare One docs","description":"Microsoft Endpoint Manager in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/service-providers/microsoft/
  schema: 1
---
<p>Cloudflare One can integrate with Microsoft to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Microsoft. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Device posture with Microsoft Endpoint Manager requires:</p>
<ul>
<li>An Intune license</li>
<li>Microsoft Endpoint Manager is managing the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5024.md")
</aside>
<h2 id="1-obtain-microsoft-graph-settings"><ol>
<li>Obtain Microsoft Graph settings</li>
</ol></h2>
<p>The following values are required:</p>
<ul>
<li>Client secret</li>
<li>Application (client) ID</li>
<li>Direct (tenant) ID</li>
</ul>
<p>To retrieve those values:</p>
<ol>
<li>Log in to your Microsoft Dashboard.</li>
<li>Go to <strong>App Registrations</strong> and select <strong>New Registrations</strong>.</li>
<li>Copy the <code>Application (client) ID</code> value to a safe place. This will be your Client ID.</li>
<li>Copy the <code>Directory (tenant) ID</code> value to a safe place. This will be your Customer ID.</li>
<li>Go to <strong>Certificates &amp; Secrets</strong> and select <strong>New client secret</strong>.</li>
<li>Fill in a description and how long the secret should be valid.</li>
<li>After completing the form, immediately copy the resulting secret. This will be your Client Secret.</li>
<li>Go to <strong>API Permissions</strong> and select <strong>Add permission</strong>.</li>
<li>Select <strong>Microsoft Graph</strong>.</li>
<li>Select <strong>Application permissions</strong>.</li>
<li>Add <code>DeviceManagementManagedDevices.Read.All</code>.</li>
<li>If the permission status shows <strong>Not granted</strong>, select <strong>Grant admin consent</strong>.</li>
</ol>
<h2 id="2-add-intune-as-a-service-provider"><ol start="2">
<li>Add Intune as a service provider</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Microsoft Endpoint Manager</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>Enter the <strong>Client ID</strong>, <strong>Client secret</strong> and <strong>Customer ID</strong> as you noted down above.</p>
</li>
<li>
<p>Select a <strong>Polling frequency</strong> for how often Cloudflare One should query Microsoft Graph API for information.</p>
</li>
<li>
<p>Select <strong>Test and save</strong>.</p>
</li>
</ol>
<h2 id="3-configure-the-posture-check"><ol start="3">
<li>Configure the posture check</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong> &gt; <strong>Service provider checks</strong>.</li>
<li>Select <strong>Add a check</strong>.</li>
<li>Select the Microsoft Endpoint Manager provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<p>The Microsoft Endpoint Manager device posture check relies on information from the Microsoft Graph API. Refer to Microsoft's <a href="https://docs.microsoft.com/en-us/graph/api/resources/intune-devices-compliancestate?view=graph-rest-1.0">ComplianceState</a> and <a href="https://docs.microsoft.com/en-us/graph/api/intune-devices-manageddevice-list?view=graph-rest-1.0">List managedDevices</a> documentation for a list of properties returned by the API.</p>
<p>To learn more about how to control ComplianceState, refer to Microsoft's <a href="https://docs.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started">compliance policies guide</a>.</p>
