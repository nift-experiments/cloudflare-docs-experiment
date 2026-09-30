---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/
  description: Antivirus in Zero Trust.
  full_title: Antivirus · Cloudflare One docs
  head_html: <title>Antivirus · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Antivirus in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/index.md"><meta property="og:title" content="Antivirus · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Antivirus in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/#page","headline":"Antivirus \u00b7 Cloudflare One docs","description":"Antivirus in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/
  schema: 1
---
<p>The Antivirus device posture attribute checks if any antivirus software is installed and active on a device. The Cloudflare One Client queries the <a href="https://learn.microsoft.com/en-us/windows/win32/api/iwscapi/ne-iwscapi-wsc_security_product_state">Windows Security Center API</a> to determine the state of registered security products. For the posture check to pass, Windows Security Center must report that a security product is turned on and up to date.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-antivirus-check">Enable the antivirus check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>Antivirus</strong>.</li>
<li>Enter a descriptive name for the check.</li>
<li>Select your operating system.</li>
<li>(Optional) Set the maximum number of days allowed since the last antivirus signature update. If the device exceeds this limit (for example, you set 30 days but it has been 31 days since the last update), the device will fail the posture check.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the antivirus check is returning the expected results.</p>
<h2 id="validate-antivirus-status">Validate antivirus status</h2>
<p>You can use the following commands to validate if the posture check is working as expected.</p>
<h3 id="windows">Windows</h3>
<ol>
<li>Open a PowerShell window.</li>
<li>List all installed antivirus products registered with Windows Security Center:</li>
</ol>
<pre tabindex="0"><code class="language-powershell">Get-WmiObject -Namespace &quot;root\SecurityCenter2&quot; -ClassName &quot;AntiVirusProduct&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-powershell">&lt;redacted&gt;&#10;displayName              : Windows Defender&#10;instanceGuid             : {00000000-0000-0000-0000-000000000000}&#10;pathToSignedProductExe   : windowsdefender://&#10;pathToSignedReportingExe : %ProgramFiles%\Windows Defender\MsMpeng.exe&#10;productState             : 397568&#10;timestamp                : Fri, 09 Jan 2026 12:00:00 GMT&#10;PSComputerName           : ENDPOINT-01&#10;</code></pre>
<ol start="3">
<li>
<p>Microsoft does not support decoding the <code>productState</code> from the <code>SecurityCenter2</code> namespace. To verify that an antivirus product is active, open the <a href="https://support.microsoft.com/en-us/windows/stay-protected-with-the-windows-security-app-2ae0363d-0ada-c064-8b56-6a39afb6a963">Windows Security app</a>. The <strong>Virus &amp; threat protection</strong> panel should say <code>No action needed</code> with a green checkmark.</p>
<p>To determine which antivirus product is running, select <strong>Virus &amp; threat protection</strong> &gt; <strong>Manage providers</strong>. You will see the name of the antivirus product (for example, <code>Windows Defender Antivirus</code>) and its current state.</p>
</li>
<li>
<p>If you configured a maximum antivirus signature age in your posture check, compare the <code>timestamp</code> in the PowerShell output against the current system time. If the difference exceeds the configured number of days, the posture check will fail.</p>
</li>
</ol>
