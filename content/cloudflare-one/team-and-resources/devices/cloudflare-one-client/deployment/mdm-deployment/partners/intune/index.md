---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/
  description: Intune in Zero Trust.
  full_title: Intune · Cloudflare One docs
  head_html: <title>Intune · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Intune in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/index.md"><meta property="og:title" content="Intune · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Intune in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft,XML,PowerShell"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/#page","headline":"Intune \u00b7 Cloudflare One docs","description":"Intune in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft","XML","PowerShell"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/intune/
  schema: 1
---
<p>This guide covers how to deploy the Cloudflare One Client (formerly WARP) using Microsoft Intune.</p>
<h2 id="windows">Windows</h2>
<h3 id="deploy-the-cloudflare-one-client">Deploy the Cloudflare One Client</h3>
<p>To deploy the Cloudflare One Client on Windows using Intune:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#windows">Download the <code>Cloudflare_WARP_&lt;VERSION&gt;.msi</code> installer</a>.</li>
<li>Log in to your Microsoft Intune account.</li>
<li>Go to <strong>Apps</strong> &gt; <strong>All Apps</strong> &gt; <strong>Add</strong>.</li>
<li>In <strong>App type</strong>, select <em>Line-of-business app</em> from the drop-down menu. Select <strong>Select</strong>.</li>
<li>Select <strong>Select app package file</strong> and upload the <code>Cloudflare_WARP_&lt;VERSION&gt;.msi</code> installer you downloaded previously.</li>
<li>Select <strong>OK</strong>.</li>
<li>For <strong>Run this script using the logged on credentials</strong>, choose <em>No</em>.</li>
<li>For <strong>Enforce script signature check</strong>, choose <em>No</em>.</li>
<li>In the <strong>Name</strong> field, we recommend entering the version number of the package being uploaded.</li>
<li>In the <strong>Publisher</strong> field, we recommend entering <code>Cloudflare, Inc</code>.</li>
<li>In the <strong>Command-line arguments</strong> field, enter a valid installation command. For example:</li>
</ol>
<pre tabindex="0"><code class="language-txt">/qn ORGANIZATION=&quot;your-team-name&quot; SUPPORT_URL=&quot;http://support.example.com&quot;&#10;</code></pre>
<pre tabindex="0"><code>Refer to [deployment parameters](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/) for a description of each argument. You can change these parameters at any time by pushing a new [MDM file](#update-mdm-parameters).&#10;</code></pre>
<ol start="12">
<li>Select <strong>Next</strong>.</li>
<li>Add the users or groups who require the Cloudflare One Client and select <strong>Next</strong>.</li>
<li>Review your configuration and select <strong>Create</strong>.</li>
</ol>
<p>Intune is now configured to deploy the Cloudflare One Client.</p>
<h3 id="update-mdm-parameters">Update MDM parameters</h3>
<p>You can use Intune to update <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">MDM parameters</a> for the Cloudflare One Client. On Windows, these parameters are stored on the local device in <code>C:\ProgramData\Cloudflare\mdm.xml</code>.</p>
<p>To push a new <code>mdm.xml</code> file using Intune:</p>
<ol>
<li>Log in to your Microsoft Intune account.</li>
<li>Go to <strong>Devices</strong> &gt; <strong>Scripts and remediations</strong>.</li>
<li>Select the <strong>Platform scripts</strong> tab and select <strong>Add</strong>.</li>
<li>Select <strong>Windows 10 and later</strong>.</li>
<li>Enter a name for the script (for example, <code>Deploy Cloudflare mdm.xml</code>).</li>
<li>In <strong>PowerShell script</strong>, upload the following <code>.ps1</code> file. Be sure to modify the XML content with your desired <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">parameters</a>.</li>
</ol>
<pre tabindex="0"><code class="language-powershell">&#35; Define the path to the file&#10;$filePath = &quot;C:\ProgramData\Cloudflare\mdm.xml&quot;&#10;&#10;&#35; Create the XML content as a string&#10;$xmlContent = @&quot;&#10;&lt;dict&gt;&#10;	&lt;key&gt;multi_user&lt;/key&gt;&#10;	&lt;true/&gt;&#10;	&lt;key&gt;pre_login&lt;/key&gt;&#10;	&lt;dict&gt;&#10;		&lt;key&gt;organization&lt;/key&gt;&#10;		&lt;string&gt;mycompany&lt;/string&gt;&#10;		&lt;key&gt;auth_client_id&lt;/key&gt;&#10;		&lt;string&gt;88bf3b6d86161464f6509f7219099e57.access&lt;/string&gt;&#10;		&lt;key&gt;auth_client_secret&lt;/key&gt;&#10;		&lt;string&gt;bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5&lt;/string&gt;&#10;	&lt;/dict&gt;&#10;	&lt;key&gt;configs&lt;/key&gt;&#10;	&lt;array&gt;&#10;		&lt;dict&gt;&#10;			&lt;key&gt;organization&lt;/key&gt;&#10;			&lt;string&gt;mycompany&lt;/string&gt;&#10;			&lt;key&gt;display_name&lt;/key&gt;&#10;			&lt;string&gt;Production environment&lt;/string&gt;&#10;		&lt;/dict&gt;&#10;		&lt;dict&gt;&#10;			&lt;key&gt;organization&lt;/key&gt;&#10;			&lt;string&gt;test-org&lt;/string&gt;&#10;			&lt;key&gt;display_name&lt;/key&gt;&#10;			&lt;string&gt;Test environment&lt;/string&gt;&#10;		&lt;/dict&gt;&#10;	&lt;/array&gt;&#10;&lt;/dict&gt;&#10;&quot;@&#10;&#10;&#35; Ensure the directory exists&#10;$directory = Split-Path $filePath -parent&#10;if (-not (Test-Path $directory)) {&#10;	New-Item -ItemType Directory -Path $directory | Out-Null&#10;}&#10;&#10;&#35; Write the XML content to the file&#10;try {&#10;	$xmlContent | Out-File -Encoding UTF8 -FilePath $filePath&#10;	Write-Host &quot;mdm.xml file created successfully at: $filePath&quot;&#10;}&#10;catch {&#10;	Write-Error &quot;Failed to create mdm.xml file: $_&quot;&#10;}&#10;</code></pre>
<ol start="7">
<li>In <strong>Assignments</strong>, select the Windows devices that should receive the new <code>mdm.xml</code> file.</li>
<li>To deploy the script, select <strong>Add</strong>.</li>
</ol>
<p>Intune will now execute the Powershell script on the target devices and overwrite the previous <code>mdm.xml</code> file. Once the new <code>mdm.xml</code> file is created, the Cloudflare One Client will immediately start using the new configuration.
After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<p>If you prefer to use Intune's Win32 App tool to run the Powershell script, refer to the <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-win32-app-management">Intune documentation</a>.</p>
<h2 id="macos">macOS</h2>
<p>The following steps outline deploying the Cloudflare One Client on macOS using Intune.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6400.md")
</aside>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>A <a href="https://login.microsoftonline.com/">Microsoft Intune account</a>.</li>
<li>A Cloudflare account that has a <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a>.</li>
<li>macOS devices enrolled in Intune.</li>
</ul>
<h3 id="deployment-order">Deployment order</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/6399.md")
</aside>
<ul>
<li>Upload user-side certificate.</li>
<li>Allow system extensions (bundle ID and team identifier policy).</li>
<li>Upload MobileConfig (custom configuration policy).</li>
<li>Upload and assign the Cloudflare One Client <code>.pkg</code> (application policy).</li>
</ul>
<h3 id="1-upload-user-side-certificate"><ol>
<li>Upload user-side certificate</li>
</ol></h3>
<h4 id="1-1-download-user-side-certificate">1.1 Download user-side certificate</h4>
<p>You must deploy a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">user-side certificate</a> so that macOS devices managed by Intune can establish trust with Cloudflare when their traffic is inspected.</p>
<ol>
<li>
<p>(Optional) Generate a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">Cloudflare root certificate</a>.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#download-a-cloudflare-root-certificate">Download a root certificate</a> in <code>.crt</code> format.</p>
</li>
</ol>
<h4 id="1-2-upload-user-side-certificate-to-intune">1.2 Upload user-side certificate to Intune</h4>
<ol>
<li>In the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, go to <strong>Devices</strong> &gt; select <strong>macOS</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/intune/devices-macos.png" alt="Intune admin console where you select macOS before creating a policy" /></p>
<ol start="2">
<li>Under <strong>Manage devices</strong>, select <strong>Configuration</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/intune/manage-devices-configuration.png" alt="Intune admin console where you will create a new policy" /></p>
<ol start="3">
<li>
<p>Select <strong>Create</strong> &gt; <strong>New Policy</strong>.</p>
</li>
<li>
<p>For <strong>Profile Type</strong>, select <em>Templates</em> &gt; select <strong>Trusted certificate</strong> as the Template name &gt; select <strong>Create</strong>.</p>
</li>
<li>
<p>In <strong>Basics</strong>, input the necessary field(s) and give your policy a name like <code>Cloudflare certificate</code> &gt; select <strong>Next</strong>.</p>
</li>
<li>
<p>For <strong>Deployment Channel</strong>, select <strong>Device Channel</strong>.</p>
</li>
<li>
<p>Upload your file (Intune may request <code>.cer</code> format, though <code>.crt</code> files are also accepted) &gt; select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Assignments</strong>, select an option (for example, <strong>Add all devices</strong> or <strong>Add all users</strong>) that is valid for your scope. This will be the same scope for all steps. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your configuration in <strong>Review + create</strong> and select <strong>Create</strong>.</p>
</li>
</ol>
<p>Sharing this certificate with Intune automates the installation of this certificate on your user devices, creating trust between browsers on a user's device and Cloudflare.</p>
<h3 id="2-upload-mobileconfig-configuration"><ol start="2">
<li>Upload <code>MobileConfig</code> configuration</li>
</ol></h3>
<ol>
<li>Open a text editor and paste in the following <code>.mobileconfig</code> template:</li>
</ol>
<pre tabindex="0"><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;!DOCTYPE plist PUBLIC &quot;-//Apple//DTD PLIST 1.0//EN&quot; &quot;http://www.apple.com/DTDs/PropertyList-1.0.dtd&quot;&gt;&#10;&lt;plist version=&quot;1.0&quot;&gt;&#10;		&lt;dict&gt;&#10;				&lt;key&gt;PayloadDisplayName&lt;/key&gt;&#10;				&lt;string&gt;Cloudflare WARP&lt;/string&gt;&#10;				&lt;key&gt;PayloadIdentifier&lt;/key&gt;&#10;				&lt;string&gt;cloudflare_warp&lt;/string&gt;&#10;				&lt;key&gt;PayloadOrganization&lt;/key&gt;&#10;				&lt;string&gt;Cloudflare, Ltd.&lt;/string&gt;&#10;				&lt;key&gt;PayloadRemovalDisallowed&lt;/key&gt;&#10;				&lt;false/&gt;&#10;				&lt;key&gt;PayloadType&lt;/key&gt;&#10;				&lt;string&gt;Configuration&lt;/string&gt;&#10;				&lt;key&gt;PayloadScope&lt;/key&gt;&#10;				&lt;string&gt;System&lt;/string&gt;&#10;				&lt;key&gt;PayloadUUID&lt;/key&gt;&#10;				&lt;string&gt;YOUR_PAYLOAD_UUID_HERE&lt;/string&gt;&#10;				&lt;key&gt;PayloadVersion&lt;/key&gt;&#10;				&lt;integer&gt;1&lt;/integer&gt;&#10;				&lt;key&gt;PayloadContent&lt;/key&gt;&#10;				&lt;array&gt;&#10;						&lt;dict&gt;&#10;								&lt;key&gt;organization&lt;/key&gt;&#10;								&lt;string&gt;YOUR_TEAM_NAME_HERE&lt;/string&gt;&#10;								&lt;key&gt;auto_connect&lt;/key&gt;&#10;								&lt;integer&gt;120&lt;/integer&gt;&#10;								&lt;key&gt;onboarding&lt;/key&gt;&#10;								&lt;false/&gt;&#10;								&lt;key&gt;PayloadDisplayName&lt;/key&gt;&#10;								&lt;string&gt;Warp Configuration&lt;/string&gt;&#10;								&lt;key&gt;PayloadIdentifier&lt;/key&gt;&#10;								&lt;string&gt;com.cloudflare.warp.YOUR_PAYLOAD_UUID_HERE&lt;/string&gt;&#10;								&lt;key&gt;PayloadOrganization&lt;/key&gt;&#10;								&lt;string&gt;Cloudflare Ltd.&lt;/string&gt;&#10;								&lt;key&gt;PayloadType&lt;/key&gt;&#10;								&lt;string&gt;com.cloudflare.warp&lt;/string&gt;&#10;								&lt;key&gt;PayloadUUID&lt;/key&gt;&#10;								&lt;string&gt;YOUR_PAYLOAD_UUID_HERE&lt;/string&gt;&#10;								&lt;key&gt;PayloadVersion&lt;/key&gt;&#10;								&lt;integer&gt;1&lt;/integer&gt;&#10;						&lt;/dict&gt;&#10;				&lt;/array&gt;&#10;		&lt;/dict&gt;&#10;&lt;/plist&gt;&#10;</code></pre>
<ol start="2">
<li>
<p>Open your macOS Terminal and run <code>uuidgen</code>. This will generate a value for <code>PayloadUUID</code>. Use this value to replace the default value (<code>YOUR_PAYLOAD_UUID_HERE</code>) used in the template (three locations total).</p>
</li>
<li>
<p>Update your organization's string (<code>YOUR_TEAM_NAME_HERE</code>) with your <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team name</a>.</p>
</li>
<li>
<p>Modify the file with your desired <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a>.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-xml">&lt;array&gt;&#10;	&lt;dict&gt;&#10;			&lt;key&gt;organization&lt;/key&gt;&#10;			&lt;string&gt;YOUR_TEAM_NAME_HERE&lt;/string&gt;&#10;			// add desired deployment parameters here&#10;</code></pre>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice-1">Best practice</h3>
@markup("md", "content/.markup/bodies/6398.md")
</aside>
<ol start="5">
<li>
<p>In the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, go to <strong>Devices</strong> &gt; <strong>macOS</strong>.</p>
</li>
<li>
<p>Under <strong>Manage devices</strong>, select <strong>Configuration</strong>.</p>
</li>
<li>
<p>Select <strong>Create</strong> &gt; <strong>New Policy</strong>.</p>
</li>
<li>
<p>For <strong>Profile Type</strong>, select <em>Templates</em> &gt; select <strong>Custom</strong> as the <strong>Template name</strong> &gt; select <strong>Create</strong>.</p>
</li>
<li>
<p>In <strong>Basics</strong>, input the necessary field(s) &gt; select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Custom configuration profile name</strong>, input a name.</p>
</li>
<li>
<p>For <strong>Deployment Channel</strong>, select <strong>Device Channel</strong>.</p>
</li>
<li>
<p>Under <strong>Configuration profile file</strong>, upload the <code>.mobileconfig</code> file that you created in your text editor in step 1 &gt; select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Assignments</strong>, select an option (for example, <strong>Add all devices</strong> or <strong>Add all users</strong>) that is valid for your scope. This will be the same scope for all steps.</p>
</li>
<li>
<p>Review your configuration and create your policy.</p>
</li>
</ol>
<p>By completing this step, you preconfigure the Cloudflare One Client with your team settings so it connects automatically upon installation.</p>
<h3 id="3-upload-cloudflare-one-client-pkg"><ol start="3">
<li>Upload Cloudflare One Client <code>.pkg</code></li>
</ol></h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice-2">Best practice</h3>
@markup("md", "content/.markup/bodies/6397.md")
</aside>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos">Download the Cloudflare One Client</a> in <code>.pkg</code> format.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="repeat-this-step-to-update-the-cloudflare-one-client-when-a-new-release-is-available">Repeat this step to update the Cloudflare One Client when a new release is available</h3>
@markup("md", "content/.markup/bodies/6396.md")
</aside>
<ol start="2">
<li>Log in to the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, and go to <strong>Apps</strong> &gt; <strong>macOS</strong>.</li>
<li>Select <strong>Create</strong>.</li>
<li>For <strong>App type</strong>, select <em>macOS app (PKG)</em>.</li>
<li>In <strong>App information</strong>, select the <code>.pkg</code> file you downloaded and input required details. Enter <code>Cloudflare</code> as the Publisher.</li>
<li>In <strong>Requirements</strong>, refer to the OS versions listed in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos">stable releases for macOS</a> and find what matches for you.</li>
<li>In <strong>Detection rules</strong>, note that the Cloudflare One Client package will have filled in the App bundle ID and App version.</li>
<li>In <strong>Assignments</strong>, select an option (for example, <strong>Add all devices</strong> or <strong>Add all users</strong>) that is valid for your scope. Select <strong>Next</strong>.</li>
<li>Review your configuration in <strong>Review + create</strong> and select <strong>Create</strong>.</li>
</ol>
<p>By completing this step, you deliver the Cloudflare One Client to targeted macOS devices, either automatically (assignment scope set as <strong>Required</strong>) or on-demand (assignment scope as <strong>Available</strong>) through your company portal.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6395.md")
</aside>
<h2 id="ios">iOS</h2>
<p>The following steps outline how to deploy the Cloudflare One Agent (Cloudflare One Client) on iOS using Microsoft Intune and preconfigure it with MDM parameters.</p>
<h3 id="prerequisites-1">Prerequisites</h3>
<ul>
<li>A <a href="https://intune.microsoft.com">Microsoft Intune account</a></li>
<li>A Cloudflare account that has a <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">Zero Trust organization</a></li>
<li>iOS/iPadOS devices enrolled in Intune</li>
<li><a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> enabled in Cloudflare Gateway (if you plan to inspect HTTPS traffic)</li>
</ul>
<h3 id="1-upload-user-side-certificate-1"><ol>
<li>Upload user-side certificate</li>
</ol></h3>
<h4 id="1-1-download-user-side-certificate-1">1.1 Download user-side certificate</h4>
<p>You must deploy a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">user-side certificate</a> so that iOS devices managed by Intune can establish trust with Cloudflare when their traffic is inspected.</p>
<ol>
<li>
<p>(Optional) Generate a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">Cloudflare root certificate</a>.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#download-a-cloudflare-root-certificate">Download a root certificate</a> in <code>.crt</code> format.</p>
</li>
</ol>
<h4 id="1-2-upload-user-side-certificate-to-intune-1">1.2 Upload user-side certificate to Intune</h4>
<ol>
<li>In the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, go to <strong>Devices</strong> &gt; select <strong>iOS/iPadOS</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/intune/devices-iOS.png" alt="Intune admin console where you select iOS/iPadOS before creating a policy" /></p>
<ol start="2">
<li>Under <strong>Manage devices</strong>, select <strong>Configuration</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/intune/manage-devices-configuration-iOS.png" alt="Intune admin console where you will create a new policy" /></p>
<ol start="3">
<li>
<p>Select <strong>Create</strong> &gt; <strong>New Policy</strong>.</p>
</li>
<li>
<p>For <strong>Profile Type</strong>, select <em>Templates</em> &gt; select <strong>Trusted certificate</strong> as the Template name &gt; select <strong>Create</strong>.</p>
</li>
<li>
<p>In <strong>Basics</strong>, input the necessary field(s) and give your policy a name like <code>Cloudflare certificate</code> &gt; select <strong>Next</strong>.</p>
</li>
<li>
<p>For <strong>Deployment Channel</strong>, select <strong>Device Channel</strong>.</p>
</li>
<li>
<p>Upload your file (Intune may request <code>.cer</code> format, though <code>.crt</code> files are also accepted) &gt; select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Assignments</strong>, select an option (for example, <strong>Add all devices</strong> or <strong>Add all users</strong>) that is valid for your scope. This will be the same scope for all steps. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your configuration in <strong>Review + create</strong> and select <strong>Create</strong>.</p>
</li>
</ol>
<p>Sharing this certificate with Intune automates the installation of this certificate on your user devices, creating trust between browsers on a user's device and Cloudflare.</p>
<h3 id="2-add-cloudflare-one-agent-app-to-intune-configuration"><ol start="2">
<li>Add Cloudflare One Agent app to Intune configuration</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, select <strong>Apps</strong> &gt; <strong>iOS/iPadOS</strong>.</p>
</li>
<li>
<p>Select <strong>Create</strong>.</p>
</li>
<li>
<p>For App type, select <em>iOS store app</em> &gt; select <strong>Select</strong> to continue.</p>
</li>
<li>
<p>Select <strong>Search the App Store</strong> and search for the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#ios">Cloudflare One Agent</a>. After you have found the Cloudflare One Agent, select it and select <strong>Select</strong> to continue.</p>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="add-the-right-app">Add the right app</h3>
@markup("md", "content/.markup/bodies/6394.md")
</aside>
<ol start="5">
<li>
<p>The fields in <strong>App information</strong> will be filled in automatically. Select <strong>Next</strong> to continue.</p>
</li>
<li>
<p>In <strong>Assignments</strong>, select an option (for example, <strong>Add all devices</strong> or <strong>Add all users</strong>) that is valid for your scope. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your configuration in <strong>Review + create</strong> and select <strong>Create</strong>.</p>
</li>
</ol>
<p>By completing this step, you deliver the Cloudflare One Client to targeted iOS devices, either automatically (assignment scope set as <strong>Required</strong>) or on-demand (assignment scope as <strong>Available</strong>) through your company portal.</p>
<h3 id="3-configure-cloudflare-one-agent-app"><ol start="3">
<li>Configure Cloudflare One Agent app</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, select <strong>Apps</strong> &gt; <strong>Manage apps</strong> &gt; <strong>Configuration</strong>.</p>
</li>
<li>
<p>Select <strong>Create</strong> &gt; <em>Managed devices</em>.</p>
</li>
<li>
<p>In <strong>Basics</strong>, input the necessary field(s) and give your policy an easily identifiable name like <code>Cloudflare One Agent</code>. Select <em>iOS/iPadOS</em> for Platform and target the Cloudflare One Agent app. Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Settings</strong>, select <em>Enter XML data</em> and copy and paste the following:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;	&lt;key&gt;organization&lt;/key&gt;&#10;	&lt;string&gt;YOUR_TEAM_NAME_HERE&lt;/string&gt;&#10;	&lt;key&gt;auto_connect&lt;/key&gt;&#10;	&lt;integer&gt;1&lt;/integer&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>Replace <code>YOUR_TEAM_NAME_HERE</code> with your <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team name</a>. Review the definitions of the above parameters in the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">Parameters documentation</a>.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="successfully-complete-your-registration">Successfully complete your registration</h3>
@markup("md", "content/.markup/bodies/6393.md")
</aside>
<ol start="5">
<li>
<p>In <strong>Assignments</strong>, select an option (for example, <strong>Add all devices</strong> or <strong>Add all users</strong>) that is valid for your scope. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your configuration in <strong>Review + create</strong> and select <strong>Create</strong>.</p>
</li>
</ol>
<p>By completing this step, you preconfigure the Cloudflare One Agent with your <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a> and connection settings so that enrolled iOS devices automatically apply a consistent Cloudflare One Client configuration when the app installs.</p>
<h3 id="intune-configuration">Intune configuration</h3>
<p>Intune allows you to insert <a href="https://learn.microsoft.com/en-us/mem/intune/apps/app-configuration-policies-use-ios#tokens-used-in-the-property-list">predefined variables</a> into the XML configuration file. For example, you can set the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#unique_client_id"><code>unique_client_id</code></a> key to <code>{{deviceid}}</code> for a <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/device-uuid/">device UUID posture check</a> deployment.</p>
<h3 id="per-app-vpn-for-ios">Per-app VPN for iOS</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6392.md")
</aside>
<p>Before proceeding with per-app VPN configuration, you must make sure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">Auto connect</a> is disabled in Zero Trust. To disable Auto connect:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Select your device profile and select <strong>Edit</strong>.</li>
<li>Turn off <strong>Auto Connect</strong>.</li>
</ol>
<p>To configure per-app VPN:</p>
<ol>
<li>Log in to Microsoft Intune admin center for your organization.</li>
<li>Go to <strong>Devices</strong> &gt; <strong>iOS/iPadOS Devices</strong> &gt; <strong>Manage Devices</strong> &gt; <strong>Configuration</strong> &gt; select <strong>+ Create</strong> &gt; <strong>New Policy.</strong></li>
<li>Select <em>Templates</em> in the <strong>Profile Type</strong> dropdown menu, then select <strong>VPN</strong> as the <strong>Template Name</strong> and select <strong>Create</strong>.</li>
<li>Give the configuration a name, and an optional description, if you desire, then select <strong>Next</strong>.</li>
<li>Select <em>Custom VPN</em> from the <strong>Connection Type</strong> dropdown menu.</li>
<li>Expand the <strong>Base VPN</strong> section.
<ul>
<li>Give the VPN connection a name.</li>
<li>Enter &quot;1.1.1.1&quot; as the VPN server address (this value is not actually used.)</li>
<li>Set <em>Username and password</em> as the <strong>Authentication method</strong>.</li>
<li>Enter &quot;com.cloudflare.cloudflareoneagent&quot; as the VPN identifier.</li>
<li>Enter any Key and Value into the custom VPN attributes (Cloudflare One does not use these but Intunes requires at least one entry.)</li>
</ul>
</li>
<li>Expand the <strong>Automatic VPN</strong> section.
<ul>
<li>Select <em>Per-app VPN</em> as the <strong>Type of automatic VPN</strong>.</li>
<li>Select <em>packet-tunnel</em> as the <strong>Provider Type</strong>. Select <strong>Next</strong>.</li>
</ul>
</li>
<li>Add any Groups, Users, or Devices to which you want to distribute this configuration and select <strong>Next</strong>.</li>
<li>Review the settings and select <strong>Create</strong>.</li>
<li>Go to <strong>Apps</strong> &gt; <strong>iOS/iPadOS Apps</strong> and select <strong>+ Add</strong>.</li>
<li>Select <em>iOS store app</em> from the <strong>App Type</strong> dropdown &gt; <strong>Select</strong>.</li>
<li>Select <strong>Search the App Store</strong>, then search for the app whose traffic you want to go through the VPN &gt; select the desired app &gt; <strong>Select</strong>.</li>
<li>Review the selected app settings and select <strong>Next</strong>.</li>
<li>Select <strong>+ Add Group</strong> to add the group of users to which to distribute this app. Then select <strong>None</strong> underneath VPN.</li>
<li>Select the configuration you just created from the VPN dropdown menu and select <strong>OK</strong>.</li>
<li>Select <strong>Next</strong>, review the settings, then select <strong>Create</strong>.</li>
<li>Repeat steps 10-16 for each app you want to use the VPN with.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6391.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6390.md")
</aside>
<h2 id="android">Android</h2>
<p>To deploy the Cloudflare One Client on Android devices:</p>
<ol>
<li>Log in to your Microsoft Intune account.</li>
<li>Go to <strong>Apps</strong> &gt; <strong>Android</strong> &gt;<strong>Add</strong>.</li>
<li>In <strong>App type</strong>, select <em>Managed Google Play app</em>.</li>
<li>Add the <strong>Cloudflare One Agent</strong> app from the Google Play store. Its application ID is <code>com.cloudflare.cloudflareoneagent</code>.</li>
<li>Go to <strong>Apps</strong> &gt; <strong>App Configuration policies</strong> &gt; <strong>Add</strong>.</li>
<li>Select <em>Managed devices</em>.</li>
<li>In <strong>Name</strong>, enter <code>Cloudflare One Agent</code>.</li>
<li>For <strong>Platform</strong>, select <em>Android Enterprise</em>.</li>
<li>Choose your desired <strong>Profile Type</strong>.</li>
<li>For <strong>Targeted app</strong>, select <strong>Cloudflare One Agent</strong>. Select <strong>Next</strong>.</li>
<li>For <strong>Configuration settings format</strong>, select <em>Enter JSON data</em>. Enter your desired <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a> in the <code>managedProperty</code> field. For example:</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;kind&quot;: &quot;androidenterprise#managedConfiguration&quot;,&#10;	&quot;productId&quot;: &quot;app:com.cloudflare.cloudflareoneagent&quot;,&#10;	&quot;managedProperty&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;app_config_bundle_list&quot;,&#10;			&quot;valueBundleArray&quot;: [&#10;				{&#10;					&quot;managedProperty&quot;: [&#10;						{&#10;							&quot;key&quot;: &quot;organization&quot;,&#10;							&quot;valueString&quot;: &quot;your-team-name&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;display_name&quot;,&#10;							&quot;valueString&quot;: &quot;Production environment&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;service_mode&quot;,&#10;							&quot;valueString&quot;: &quot;warp&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;onboarding&quot;,&#10;							&quot;valueBool&quot;: false&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;support_url&quot;,&#10;							&quot;valueString&quot;: &quot;https://support.example.com/&quot;&#10;						}&#10;					]&#10;				},&#10;				{&#10;					&quot;managedProperty&quot;: [&#10;						{&#10;							&quot;key&quot;: &quot;organization&quot;,&#10;							&quot;valueString&quot;: &quot;test-org&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;display_name&quot;,&#10;							&quot;valueString&quot;: &quot;Test environment&quot;&#10;						}&#10;					]&#10;				}&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<pre tabindex="0"><code>Alternatively, if you do not want to copy and paste the JSON data, you can change **Configuration settings format** to _Use configuration designer_ and manually configure each deployment parameter.&#10;&#10;Once you have configured the deployment parameters, select **Next**.&#10;</code></pre>
<ol start="12">
<li>Assign users or groups to this policy and select <strong>Next</strong>.</li>
<li>Save the app configuration policy.</li>
<li>Assign users or groups to the application:
<ol>
<li>Go to <strong>Apps</strong> &gt; <strong>Android</strong> &gt; <strong>Cloudflare One Agent</strong> &gt; <strong>Manage Properties</strong>.</li>
<li>Select <strong>Edit</strong> and add users or groups.</li>
<li>Select <strong>Review + save</strong> &gt; <strong>Save</strong>.</li>
</ol>
</li>
</ol>
<p>Intune will now deploy the Cloudflare One Agent to user devices.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6389.md")
</aside>
<h3 id="per-app-vpn-for-android">Per-app VPN for Android</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6388.md")
</aside>
<p>Review the following steps to approve and deploy the Cloudflare One Agent application in Microsoft Intune and use a configuration policy to set up the per-app VPN. To use the per-app VPN, the admin must have linked the Microsoft Intune account with the Google-managed Play account. For more information, refer to <a href="https://learn.microsoft.com/en-us/mem/intune/enrollment/connect-intune-android-enterprise">Connect your Intune account to your managed Google Play account in the Microsoft documentation</a>.</p>
<h4 id="approve-the-cloudflare-one-agent-app-within-microsoft-intune">Approve the Cloudflare One Agent app within Microsoft Intune</h4>
<ol>
<li>Log into the Microsoft Intune admin center.</li>
<li>Go to <strong>Apps</strong> &gt; <strong>All apps</strong> &gt; select <strong>Add</strong>.</li>
<li>In App type, select <em>Managed Google Play</em>.</li>
<li>Search for <em>Cloudflare One Agent</em> &gt; select the app &gt; select <strong>Sync</strong>.</li>
<li>Once the sync is successful, admin will see the Cloudflare One Agent app within the <strong>All apps</strong> view in the Microsoft Intune admin center.</li>
</ol>
<h4 id="configure-your-cloudflare-one-agent-app-policy">Configure your Cloudflare One Agent app policy</h4>
<p>To configure your Cloudflare One Agent app policy:</p>
<ol>
<li>
<p>In the Microsoft Intune admin center, go to <strong>Apps</strong> &gt; <strong>App configuration policies</strong> &gt; select <strong>Add</strong> &gt; <strong>Managed Devices</strong>.</p>
</li>
<li>
<p>Fill out the basic details of your configuration policy:</p>
<ol>
<li>Enter the <strong>Name</strong> of the profile. (For example: Cloudflare One Agent - configuration policy)</li>
<li>Select the Platform as <strong>Android Enterprise</strong>.</li>
<li>Select the desired <strong>Profile Type</strong>. (For example: Personally-Owned Work Profile Only)</li>
<li>Select <strong>Cloudflare One Agent</strong> as the <strong>Targeted app</strong>.</li>
<li>Select <strong>Next</strong>.</li>
</ol>
</li>
<li>
<p>Fill out the settings for the configuration policy.</p>
<ol>
<li>Select <strong>Configuration setting format</strong> as <strong>Enter JSON data</strong>.</li>
<li>Enter your desired deployment parameters in the <code>managedProperty</code> field. For example:</li>
</ol>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">	{&#10;	&quot;kind&quot;: &quot;androidenterprise#managedConfiguration&quot;,&#10;	&quot;productId&quot;: &quot;app:com.cloudflare.cloudflareoneagent&quot;,&#10;	&quot;managedProperty&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;app_config_bundle_list&quot;,&#10;			&quot;valueBundleArray&quot;: [&#10;				{&#10;					&quot;managedProperty&quot;: [&#10;						{&#10;							&quot;key&quot;: &quot;organization&quot;,&#10;							&quot;valueString&quot;: &quot;${ORGANIZATION_NAME-1}&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;service_mode&quot;,&#10;							&quot;valueString&quot;: &quot;warp&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;onboarding&quot;,&#10;							&quot;valueBool&quot;: true&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;display_name&quot;,&#10;							&quot;valueString&quot;: &quot;${UNIQUE_DISPLAY_NAME-1}&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;warp_tunnel_protocol&quot;,&#10;							&quot;valueString&quot;: &quot;MASQUE&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;tunneled_apps&quot;,&#10;							&quot;valueBundleArray&quot; :[&#10;								{&#10;									&quot;managedProperty&quot;: [&#10;										{&#10;											&quot;key&quot;: &quot;app_identifier&quot;,&#10;											&quot;valueString&quot;: &quot;com.android.chrome&quot; # Application package name/unique bundle identifier for the Chrome app browser&#10;										},&#10;										{&#10;											&quot;key&quot;: &quot;is_browser&quot;,&#10;											&quot;valueBool&quot;: true&#10;										}&#10;									]&#10;								},&#10;								{&#10;									&quot;managedProperty&quot;: [&#10;										{&#10;											&quot;key&quot;: &quot;app_identifier&quot;,&#10;											&quot;valueString&quot;: &quot;com.google.android.gm&quot; # Application package name/unique bundle identifier for the Gmail app&#10;										},&#10;										{&#10;											&quot;key&quot;: &quot;is_browser&quot;,&#10;											&quot;valueBool&quot;: false # Default value is false, if a user does not define `is_browser` property our app would not treat `app_identifier` package name as a browser.&#10;										}&#10;									]&#10;								}&#10;							]&#10;						}&#10;					]&#10;				},&#10;				{&#10;					&quot;managedProperty&quot;: [&#10;						{&#10;							&quot;key&quot;: &quot;organization&quot;,&#10;							&quot;valueString&quot;: &quot;${ORGANIZATION_NAME-1}&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;service_mode&quot;,&#10;							&quot;valueString&quot;: &quot;warp&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;display_name&quot;,&#10;							&quot;valueString&quot;: &quot;${UNIQUE_DISPLAY_NAME-2}&quot;&#10;						},&#10;						{&#10;							&quot;key&quot;: &quot;warp_tunnel_protocol&quot;,&#10;							&quot;valueString&quot;: &quot;wireguard&quot;&#10;						}&#10;					]&#10;				}&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<pre tabindex="0"><code>  Refer to [Per-app VPN parameters](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#per-app-vpn-parameters-android) to learn more about the MDM parameters introduced to support the per-app VPN for Android devices.&#10;</code></pre>
<ol start="3">
<li>
<p>After you have configured the deployment parameters, click <strong>Next</strong>.</p>
</li>
<li>
<p>Fill out the assignments for the configuration policy. The admin can <code>Include</code> or <code>Exclude</code> specific groups of users to this policy. After you finish, select <strong>Next</strong>.</p>
</li>
<li>
<p>Review the policy and select <strong>Create</strong>.</p>
</li>
</ol>
<h4 id="assign-users-to-the-cloudflare-one-agent-application">Assign users to the Cloudflare One Agent application</h4>
<ol>
<li>Go to <strong>Apps</strong> &gt; <strong>All Apps</strong> &gt; select <strong>Cloudflare One Agent</strong>.</li>
<li>Under <strong>Manage</strong>, select <strong>Properties</strong> and near <strong>Assignments</strong>, select <strong>Edit</strong>.</li>
<li>Add the groups of users in the assignments &gt; select <strong>Review + Save</strong> &gt; select <strong>Save</strong>.</li>
</ol>
<p>Intune will now deploy the Cloudflare One Agent application on a user's device with the managed parameters.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
