---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/
  description: Managed deployment in Zero Trust.
  full_title: Managed deployment · Cloudflare One docs
  head_html: <title>Managed deployment · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Managed deployment in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/index.md"><meta property="og:title" content="Managed deployment · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Managed deployment in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="XML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#page","headline":"Managed deployment \u00b7 Cloudflare One docs","description":"Managed deployment in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["XML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/
  schema: 1
---
<p>Organizations can deploy and manage the Cloudflare One Client (formerly WARP) across their fleet of devices in two complementary ways:</p>
<ul>
<li><strong>Through a mobility management solution (MDM)</strong> — Push the client installer and its deployment parameters using a tool such as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/">Intune, JAMF, Kandji, or JumpCloud</a>, or by executing an <code>.msi</code> file on desktop machines. This page covers the MDM-driven workflow.</li>
<li><strong>From the Cloudflare dashboard</strong> — Manage client versions for groups of devices directly from the Zero Trust dashboard, without relying on a third-party MDM solution. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a>.</li>
</ul>
<p>This page provides generic instructions for an automated deployment. If you want to deploy the Cloudflare One Client manually, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">instructions for manual deployment</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6371.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#windows">Download page</a> to review system requirements and download the installer for your operating system.</li>
<li></li>
</ul>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h2 id="windows">Windows</h2>
<p>The Cloudflare One Client for Windows allows for an automated install via tools like Intune, AD, or any script or management tool that can execute a <code>.msi</code> file.</p>
<h3 id="install-the-cloudflare-one-client">Install the Cloudflare One Client</h3>
<p>To install the Cloudflare One Client, run the following command:</p>
<pre tabindex="0"><code class="language-bash">msiexec /i &quot;Cloudflare_WARP_&lt;VERSION&gt;.msi&quot; /qn ORGANIZATION=&quot;your-team-name&quot; SUPPORT_URL=&quot;http://support.example.com&quot;&#10;</code></pre>
<h4 id="supported-properties">Supported properties</h4>
<p>The Cloudflare One Client MSI installer supports the following <a href="https://learn.microsoft.com/en-us/windows/win32/msi/public-properties">public properties</a>:</p>
<ul>
<li><code>ORGANIZATION</code></li>
<li><code>GATEWAY_UNIQUE_ID</code></li>
<li><code>AUTH_CLIENT_ID</code></li>
<li><code>AUTH_CLIENT_SECRET</code></li>
<li><code>ONBOARDING</code></li>
<li><code>OVERRIDE_API_ENDPOINT</code></li>
<li><code>OVERRIDE_DOH_ENDPOINT</code></li>
<li><code>OVERRIDE_WARP_ENDPOINT</code></li>
<li><code>SERVICE_MODE</code></li>
<li><code>SUPPORT_URL</code></li>
<li><code>SWITCH_LOCKED</code></li>
</ul>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a> for a description of each property.</p>
<h3 id="uninstall-the-cloudflare-one-client">Uninstall the Cloudflare One Client</h3>
<p>To uninstall the Cloudflare One Client:</p>
<ol>
<li>First, locate the <code>.msi</code> package with the following PowerShell command:</li>
</ol>
<pre tabindex="0"><code class="language-powershell">Get-WmiObject Win32_Product | Where-Object { $_.Name -match &quot;Cloudflare One Client&quot; } | Sort-Object -Property Name | Format-Table IdentifyingNumber, Name, LocalPackage -AutoSize&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">IdentifyingNumber                      Name                  LocalPackage&#10;&#45;----------------                      ----                  ------------&#10;{9949770E-B807-4610-9A96-8CD4997A736A} Cloudflare One Client C:\WINDOWS\Installer\cd8edd0.msi&#10;</code></pre>
<ol start="2">
<li>You can then use the LocalPackage output in the uninstall command. For example,</li>
</ol>
<pre tabindex="0"><code class="language-powershell">msiexec /x C:\WINDOWS\Installer\&lt;WARP_RELEASE&gt;.msi /quiet&#10;</code></pre>
<h3 id="update-mdm-parameters">Update MDM parameters</h3>
<p>The on-disk configuration of the Windows client can be changed at any time by modifying or replacing the contents of <code>C:\ProgramData\Cloudflare\mdm.xml</code>. The format of this file is as follows:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization&lt;/key&gt;&#10;  &lt;string&gt;your-team-name&lt;/string&gt;&#10;	&lt;key&gt;onboarding&lt;/key&gt;&#10;	&lt;false/&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>Changes to this file are processed immediately by the Cloudflare One Client.</p>
<h3 id="authenticate-in-embedded-browser">Authenticate in embedded browser</h3>
<p>By default the Cloudflare One Client will use the user's default browser to perform registration. You can override the default setting to instead authenticate users in an embedded browser. The embedded browser will work around any protocol handler issues that may prevent the default browser from launching.</p>
<p>To use an embedded browser:</p>
<ol>
<li>Download and install WebView2 by following the <a href="https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section">Microsoft instructions</a>.</li>
<li>Add a registry key with the following command:</li>
</ol>
<pre tabindex="0"><code class="language-txt">REG ADD HKLM\SOFTWARE\Cloudflare\CloudflareWARP /f /v UseWebView2 /t REG_SZ /d y&#10;</code></pre>
<p>The Cloudflare One Client will now launch WebView2 when the user is registering their device with Zero Trust.</p>
<h2 id="macos">macOS</h2>
<p>The Cloudflare One Client for macOS allows for an automated install via tools like Jamf, Intune, Kandji, or JumpCloud or any script or management tool that can place a <code>com.cloudflare.warp.plist</code> file in <code>/Library/Managed Preferences</code>. The plist can also be wrapped in a <code>.mobileconfig</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6370.md")
</aside>
<p>If you do not wish to use a management tool, you can manually place an <code>mdm.xml</code> file in <code>/Library/Application Support/Cloudflare</code>.</p>
<h3 id="prepare-file-for-mdm-deployment">Prepare file for MDM deployment</h3>
<h4 id="plist-file"><code>plist</code> file</h4>
<ol>
<li>
<p><a href="/cloudflare-one/static/mdm/com.cloudflare.warp.plist">Download</a> an example <code>com.cloudflare.warp.plist</code> file.</p>
</li>
<li>
<p>Replace <code>your-team-name</code> with your Cloudflare One <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
</li>
<li>
<p>Modify the file with your desired <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a>.</p>
</li>
</ol>
<h4 id="mobileconfig-file"><code>mobileconfig</code> file</h4>
<ol>
<li>
<p><a href="/cloudflare-one/static/mdm/CloudflareWARP.mobileconfig">Download</a> an example <code>.mobileconfig</code> file.</p>
</li>
<li>
<p>Replace <code>your-team-name</code> with your Cloudflare One <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
</li>
<li>
<p>Run <code>uuidgen</code> from your macOS Terminal. This will generate a value for <code>PayloadUUID</code>, which you can use to replace the default value used for <code>PayloadUUID</code>.</p>
</li>
<li>
<p>Modify the file with your desired <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a>.</p>
</li>
</ol>
<h3 id="place-an-unmanaged-mdm-xml-file">Place an unmanaged <code>mdm.xml</code> file</h3>
<p>You can configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">Cloudflare One Client deployment parameters</a> on macOS by manually placing an <code>mdm.xml</code> file in <code>/Library/Application Support/Cloudflare</code>. This deployment method is an alternative to pushing a <code>plist</code> or <code>mobileconfig</code> using an MDM tool.</p>
<p>The format of <code>/Library/Application Support/Cloudflare/mdm.xml</code> is as follows:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization&lt;/key&gt;&#10;  &lt;string&gt;your-team-name&lt;/string&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h2 id="linux">Linux</h2>
<p>The Cloudflare One Client for Linux allows for an automated install via the presence of an <code>mdm.xml</code> file in <code>/var/lib/cloudflare-warp</code>. The format of <code>/var/lib/cloudflare-warp/mdm.xml</code> is as follows:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization&lt;/key&gt;&#10;  &lt;string&gt;your-team-name&lt;/string&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a> for a list of accepted arguments.</p>
<p>To learn how to automate Cloudflare One Client deployment on headless servers, refer to our <a href="/cloudflare-one/tutorials/deploy-client-headless-linux/">tutorial</a>.</p>
<h2 id="ios">iOS</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="migrate-from-1-1-1-1">Migrate from 1.1.1.1</h3>
@markup("md", "content/.markup/bodies/6369.md")
</aside>
<p>The Cloudflare One Client for iOS, known in the App Store as <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">Cloudflare One Agent</a>, allows for an automated install via tools like Jamf, Intune, or SimpleMDM.</p>
<p>To proceed with the installation, here is an example of the XML code you will need:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;    &lt;key&gt;organization&lt;/key&gt;&#10;    &lt;string&gt;your-team-name&lt;/string&gt;&#10;    &lt;key&gt;auto_connect&lt;/key&gt;&#10;    &lt;integer&gt;1&lt;/integer&gt;&#10;    &lt;key&gt;switch_locked&lt;/key&gt;&#10;    &lt;false /&gt;&#10;    &lt;key&gt;service_mode&lt;/key&gt;&#10;    &lt;string&gt;warp&lt;/string&gt;&#10;    &lt;key&gt;support_url&lt;/key&gt;&#10;    &lt;string&gt;https://support.example.com&lt;/string&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a> for a description of each argument.</p>
<h2 id="android-chromeos">Android / ChromeOS</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="migrate-from-1-1-1-1-1">Migrate from 1.1.1.1</h3>
@markup("md", "content/.markup/bodies/6368.md")
</aside>
<p>The Cloudflare One Client for Android, known in the Google Play store as <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Cloudflare One Agent</a>, allows for an automated install via tools like Intune, Google Endpoint Manager, and others.</p>
<p>To proceed with the installation, here is an example of the XML code you will need:</p>
<pre tabindex="0"><code class="language-xml">&lt;key&gt;organization&lt;/key&gt;&#10;&lt;string&gt;your-team-name&lt;/string&gt;&#10;&lt;key&gt;switch_locked&lt;/key&gt;&#10;&lt;true /&gt;&#10;&lt;key&gt;auto_connect&lt;/key&gt;&#10;&lt;integer&gt;0&lt;/integer&gt;&#10;&lt;key&gt;gateway_unique_id&lt;/key&gt;&#10;&lt;string&gt;your_gateway_doh_subdomain&lt;/string&gt;&#10;&lt;key&gt;service_mode&lt;/key&gt;&#10;&lt;string&gt;warp&lt;/string&gt;&#10;&lt;key&gt;support_url&lt;/key&gt;&#10;&lt;string&gt;https://support.example.com&lt;/string&gt;&#10;</code></pre>
<p>If your MDM tool does not support XML, you may need to convert the XML to JSON. Here is an example below:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;organization&quot;: &quot;your-team-name&quot;,&#10;	&quot;gateway_unique_id&quot;: &quot;your_gateway_doh_subdomain&quot;,&#10;	&quot;onboarding&quot;: true,&#10;	&quot;switch_locked&quot;: true,&#10;	&quot;auto_connect&quot;: 0,&#10;	&quot;service_mode&quot;: &quot;warp&quot;,&#10;	&quot;support_url&quot;: &quot;https://support.example.com&quot;&#10;}&#10;</code></pre>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a> for a description of each value.</p>
