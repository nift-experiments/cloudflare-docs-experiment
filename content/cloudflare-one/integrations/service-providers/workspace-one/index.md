---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/
  description: Workspace ONE in Zero Trust integrations.
  full_title: Workspace ONE · Cloudflare One docs
  head_html: <title>Workspace ONE · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Workspace ONE in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/index.md"><meta property="og:title" content="Workspace ONE · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workspace ONE in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/#page","headline":"Workspace ONE \u00b7 Cloudflare One docs","description":"Workspace ONE in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/service-providers/workspace-one/
  schema: 1
---
<p>Cloudflare One can integrate with Workspace ONE to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Workspace ONE. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Workspace ONE agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<h2 id="1-obtain-workspace-one-settings"><ol>
<li>Obtain Workspace ONE Settings</li>
</ol></h2>
<p>The following Workspace ONE values are needed to set up the Workspace ONE posture check:</p>
<ul>
<li>ClientID</li>
<li>Client Secret</li>
<li>REST API URL</li>
<li>Region-Specific token URL</li>
</ul>
<p>To retrieve those values:</p>
<ol>
<li>Log in to your Workspace ONE dashboard.</li>
<li>Go to <strong>Groups &amp; Settings</strong> &gt; <strong>Configurations</strong>.</li>
<li>Enter <code>OAuth</code> in the search bar labeled <strong>Enter a name or category</strong>.</li>
<li>Select <strong>OAuth Client Management</strong> in the results. The OAuth Client Management screen displays.</li>
<li>Select <strong>Add</strong>.</li>
<li>Enter values for the <strong>Name</strong>, <strong>Description</strong>, <strong>Organization Group</strong>, and <strong>Role</strong>.</li>
<li>Ensure that the <strong>Status</strong> is <strong>Enabled</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Copy the <strong>Client ID</strong> and <strong>Client Secret</strong> to a safe place.</li>
<li>To obtain your REST API URL, gp tp <strong>Groups &amp; Settings</strong> &gt; <strong>All Settings</strong> &gt; <strong>System</strong> &gt; <strong>Advance</strong> &gt; <strong>Site URLs</strong> &gt; <strong>REST API URL</strong>.</li>
<li>Retrieve the Region-Specific Token URL from Workspace ONE and copy it to a safe place.</li>
</ol>
<h2 id="2-add-workspace-one-as-a-service-provider"><ol start="2">
<li>Add Workspace ONE as a service provider</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Workspace ONE</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>Enter the <strong>Client ID</strong> and <strong>Client secret</strong> you noted down above.</p>
</li>
<li>
<p>Select a <strong>Polling frequency</strong> for how often Cloudflare One should query Workspace ONE for information.</p>
</li>
<li>
<p>Enter the <strong>Region-specific token URL</strong> and <strong>REST API URL</strong> you noted down above.</p>
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
<li>Select the Workspace ONE provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<p>Workspace ONE posture checks work with the <a href="https://docs.vmware.com/en/VMware-Workspace-ONE-UEM/services/UEM_Managing_Devices/GUID-CompliancePolicies.html">Compliance flags</a> in Workspace ONE. All compliance tests must pass for the device to be considered compliant.</p>
