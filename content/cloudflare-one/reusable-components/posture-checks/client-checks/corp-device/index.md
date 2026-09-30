---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/
  description: Device serial numbers in Zero Trust.
  full_title: Device serial numbers · Cloudflare One docs
  head_html: <title>Device serial numbers · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Device serial numbers in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/index.md"><meta property="og:title" content="Device serial numbers · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Device serial numbers in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/#page","headline":"Device serial numbers \u00b7 Cloudflare One docs","description":"Device serial numbers in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/
  schema: 1
---
<p>Cloudflare One allows you to build Zero Trust rules based on device serial numbers. You can create these rules so that access to applications is granted only to users connecting from company devices.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="create-a-list-of-serial-numbers">Create a list of serial numbers</h2>
<p>To create rules based on device serial numbers, you first need to create a <a href="/cloudflare-one/reusable-components/lists/">Gateway List</a> of numbers.</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Lists</strong>.</p>
</li>
<li>
<p>Select <strong>Create manual list</strong> or <strong>Upload CSV</strong>. For larger teams, we recommend uploading a CSV or using Cloudflare's <a href="/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/list/">API endpoint</a>.</p>
</li>
<li>
<p>Give your list a descriptive name, as this name will appear when configuring your policies.</p>
</li>
<li>
<p>Set <strong>List Type</strong> to <em>Serial numbers</em>.</p>
</li>
<li>
<p>Enter the serial numbers of the devices your team manages, or upload your CSV file.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>You can now create an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> or a Gateway <a href="/cloudflare-one/traffic-policies/network-policies/common-policies/#enforce-device-posture">network policy</a> that checks if the device presents a serial number on your list. In Access, the serial number check will appear as a <em>Device Posture - Serial Number List</em> selector. In Gateway, your serial number list will appear in the <strong>Value</strong> dropdown when you choose the <a href="/cloudflare-one/traffic-policies/network-policies/#device-posture">Passed Device Posture Check</a> selector.</p>
<h2 id="validate-the-serial-number">Validate the serial number</h2>
<p>You can use the following commands to check the serial number of your device. The results can help you validate if the posture check is working as expected.</p>
<h3 id="macos">macOS</h3>
<ol>
<li>Open a terminal window.</li>
<li>Use the <code>system_profiler</code> command to check for the value of <code>SPHardwareDataType</code> and retrieve the serial number.</li>
</ol>
<pre tabindex="0"><code class="language-sh">system_profiler SPHardwareDataType | grep &#x27;Serial Number&#x27;&#10;</code></pre>
<h3 id="windows">Windows</h3>
<ol>
<li>Open a PowerShell window.</li>
<li>Use the <code>Get-CimInstance</code> command to get the SerialNumber property of the <code>Win32_BIOS</code> class.</li>
</ol>
<pre tabindex="0"><code class="language-powershell">Get-CimInstance Win32_BIOS&#10;</code></pre>
<h3 id="linux">Linux</h3>
<ol>
<li>Open a Terminal Window</li>
<li>Use the <code>dmidecode</code> command to get the version property <code>system-serial-number</code>.</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo dmidecode -s system-serial-number&#10;</code></pre>
<h3 id="ios-android-and-chromeos">iOS, Android and ChromeOS</h3>
<p>Serial number checks are not supported on mobile devices. You can identify mobile devices by a <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/device-uuid">unique client ID</a> instead of by serial number.</p>
