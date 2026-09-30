---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/
  description: Connect to RDP in a browser in Zero Trust networking.
  full_title: Connect to RDP in a browser · Cloudflare One docs
  head_html: <title>Connect to RDP in a browser · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to RDP in a browser in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/index.md"><meta property="og:title" content="Connect to RDP in a browser · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to RDP in a browser in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="RDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#page","headline":"Connect to RDP in a browser \u00b7 Cloudflare One docs","description":"Connect to RDP in a browser in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["RDP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/
  schema: 1
---
<p>Users can connect to an RDP server without installing an RDP client or the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on their device. Browser-based RDP leverages <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>, which creates a secure, outbound-only connection from your RDP server to Cloudflare's global network. Setup involves running the <code>cloudflared</code> daemon on the RDP server (or any other host machine within the private network) and routing RDP traffic over a public hostname.</p>
<p>There are two ways for users to <a href="#4-connect-as-a-user">reach the RDP server in their browser</a>:</p>
<ul>
<li><strong>App Launcher (recommended)</strong>: Users can log in to the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">Access App Launcher</a> with their Cloudflare Access credentials and then initiate an RDP connection within the browser to their Windows machine. Users will authenticate to the Windows machine using their pre-configured Windows username and password. Cloudflare does not manage any credentials on the Windows server.</li>
<li><strong>Direct URL</strong>: A user may also navigate directly to the Windows server at <code>https://&lt;app-domain&gt;/rdp/&lt;vnet-id&gt;/&lt;target-ip&gt;/&lt;port&gt;</code>, where <code>vnet-id</code> is the <span class="nb-glossary-tooltip" title="Virtual network">virtual network</span> assigned to the Cloudflare Tunnel route. The authentication flow is the same as for the App Launcher; first users must log in to Cloudflare Access and then use their Windows credentials to authenticate to the Windows machine.</li>
</ul>
<p>Browser-based RDP can be used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/">the Cloudflare One Client</a> so that there are multiple ways to connect to the server. You can reuse the same Cloudflare Tunnel when configuring each connection method.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/fundamentals/manage-domains/add-site/">active domain on Cloudflare</a>.</li>
<li>The domain uses either a <a href="/dns/zone-setups/full-setup/">full setup</a> or a <a href="/dns/zone-setups/partial-setup/">partial (<code>CNAME</code>) setup</a>.</li>
<li>An RDP server running a supported <a href="#rdp-server-operating-systems">Windows operating system</a>.</li>
<li>The RDP server's <a href="#known-limitations">security layer</a> allows TLS (set to <strong>Negotiate</strong> or <strong>SSL</strong>, not the legacy <strong>RDP</strong> option).</li>
</ul>
<h2 id="1-connect-the-server-to-cloudflare"><ol>
<li>Connect the server to Cloudflare</li>
</ol></h2>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Create a new tunnel</a> or edit an existing <code>cloudflared</code> tunnel.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the IP or CIDR address of your server (typically a private IP, but public IPs are also allowed), and select <strong>Create route</strong>.</li>
</ol>
<h2 id="2-add-a-target"><ol start="2">
<li>Add a target</li>
</ol></h2>
<p>A target represents a single resource in your infrastructure (such as a server, Kubernetes cluster, database, or container) that users will connect to through Cloudflare.</p>
<p> Create a target for each Windows machine that requires RDP access.
To create a new target:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5516.md")
</div></div>
<p>Next, create an Access application to secure the target.</p>
<h2 id="3-create-a-dns-record"><ol start="3">
<li>Create a DNS record</li>
</ol></h2>
<p>To make your RDP targets (that is, your Windows machines) available through the browser, you will need a <a href="/dns/manage-dns-records/how-to/create-dns-records/">Cloudflare DNS record</a> for the domain and subdomain that users will connect to. This domain will be used to access any targets that are available to users through your Access application (see Step 4).</p>
<p>For example, if want users to connect to targets on <code>rdp.example.com</code>, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create a DNS record</a> for <code>rdp.example.com</code>. You can create either an <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record:</p>
<details class="nb-details"><summary>A record</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5517.md")
</div></details>
<details class="nb-details"><summary>AAAA record</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5518.md")
</div></details>
<details class="nb-details"><summary>CNAME record</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5519.md")
</div></details>
<p>The DNS record does not need to point to an active destination IP address or hostname; the DNS record just needs to be valid. Cloudflare's RDP proxy will handle the routing to the correct RDP target.</p>
<h2 id="4-create-an-access-application"><ol start="4">
<li>Create an Access application</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>Self-hosted and private</strong>.</p>
</li>
<li>
<p>Select <strong>Add public hostname</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5507.md")
</aside>
<ol start="5">
<li></li>
</ol>
<p>In the <strong>Domain</strong> dropdown, select the domain that will represent the application. Domains must belong to an active zone in your Cloudflare account. You can use <a href="/cloudflare-one/access-controls/policies/app-paths/">wildcards</a> to protect multiple parts of an application that share a root path.</p>
<pre tabindex="0"><code>	Alternatively, to use a [Cloudflare for SaaS custom hostname](/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/), select **Switch to custom input** and enter your custom hostname.&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5506.md")
</aside>
<ol start="6">
<li>
<p>Turn on <strong>Allow access through browser-based RDP, SSH, or VNC sessions</strong>, then select <em>RDP</em> from the dropdown menu.</p>
</li>
<li>
<p>In <strong>Target criteria</strong>, select the <a href="#2-add-a-target">target hostname(s)</a> that define your RDP servers. The application definition will apply to all targets that share the selected target hostname, including any targets added in the future.</p>
</li>
<li>
<p>In <strong>Port</strong>, enter the <a href="https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/change-listening-port">RDP listening port</a> of your server. It will likely be port <code>3389</code>.</p>
</li>
<li>
<p>(Optional) If you run RDP on more than one port, select <strong>Add new target criteria</strong> and reconfigure the same target hostname(s) with the different port number.</p>
</li>
<li></li>
</ol>
<p>Under <strong>Access policies</strong>, add an existing policy or <a href="/cloudflare-one/access-controls/policies/policy-management/">create a new policy</a> to control who can connect to your application. All Access applications are deny by default -- a user must match an Allow policy before they are granted access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5505.md")
</aside>
<ol start="11">
<li>
<p>(Optional) In your Access policy, configure <a href="#connection-settings">connection settings</a> to restrict clipboard and file transfer actions between the user's local machine and the browser-based RDP session.</p>
</li>
<li>
<p>Configure how users will authenticate:</p>
<ol>
<li>
Select the [identity providers](/cloudflare-one/integrations/identity-providers/) you want to enable for your application.
</li>
<li>
(Recommended) If you plan to only allow access via a single IdP, turn on **Apply instant authentication**. End users will not be shown the [Cloudflare Access login page](/cloudflare-one/reusable-components/custom-pages/access-login-page/). Instead, Cloudflare will redirect users directly to your SSO login event.
</li>
<li> <b>Authenticate with Cloudflare One Client</b> is not supported for browser-based RDP and should remain turned off. </li>
</ol>
</li>
<li></li>
</ol>
<p>In <strong>Session Duration</strong>, choose how often the user's <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> should expire.</p>
<p>Cloudflare checks every HTTP request to your application for a valid application token. If the user's application token (and global token) has expired, they will be prompted to reauthenticate with the IdP. For more information, refer to <a href="/cloudflare-one/access-controls/access-settings/session-management/">Session management</a>.</p>
<ol start="14">
<li>
<p>(Optional) Go to the <strong>Additional settings</strong> tab to customize the application experience:</p>
<ul>
<li><strong>App Launcher customization</strong>: The <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> allows users to view the Windows servers that they can access using browser-based RDP. Cloudflare recommends keeping <strong>Show application in App Launcher</strong> turned on. Without the App Launcher, users will need to know each target's direct URL.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5504.md")
</aside>
<pre tabindex="0"><code>- &#10;</code></pre>
<p><strong>Custom block pages</strong>: Choose what users will see when they are denied access to the application.</p>
<ul>
<li><strong>Cloudflare default</strong>: Reload the <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">login page</a> and display a block message below the Cloudflare Access logo. The default message is <code>That account does not have access</code>, or you can enter a custom message.</li>
<li><strong>Redirect URL</strong>: Redirect to the specified website.</li>
<li><strong>Custom page template</strong>: Display a <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/">custom block page</a> hosted in Cloudflare One.</li>
</ul>
<ul>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/"><strong>Cross-Origin Resource Sharing (CORS) settings</strong></a></li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#cookie-settings"><strong>Cookie settings</strong></a></li>
<li><strong>401 Response for Service Auth policies</strong>: Return a <code>401</code> response code when a user (or machine) makes a request to the application without the correct <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>.</li>
</ul>
<ol start="15">
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="5-recommended-modify-order-of-precedence-in-gateway"><ol start="5">
<li>(Recommended) Modify order of precedence in Gateway</li>
</ol></h2>
<p>By default, Cloudflare will evaluate Access application policies after evaluating all <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>. To evaluate Access applications before or after specific Gateway policies:</p>
<ol>
<li>
In the [Cloudflare dashboard](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall policies**. In **Network**, [create a Network policy](/cloudflare-one/traffic-policies/network-policies/) with the following configuration:
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access Infrastructure Target</td>
<td>is</td>
<td><em>Present</em></td>
<td>Allow</td>
</tr>
</tbody>
</table>
</li>
<li> Ensure that <strong>Enforce Cloudflare One Client session duration</strong> is turned off, otherwise users will be blocked from accessing RDP targets. </li>
<li>
	Update the policy's [order of
	precedence](/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence)
	using the dashboard or API.
</li>
</ol>
<p> This Gateway policy will apply to all Access for Infrastructure targets, including RDP and SSH. </p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5503.md")
</aside>
<h2 id="6-connect-as-a-user"><ol start="6">
<li>Connect as a user</li>
</ol></h2>
<p>To connect to a Windows machine over RDP:</p>
<ol>
<li>Open a browser and go to your App Launcher URL:</li>
</ol>
<pre tabindex="0"><code class="language-text">https://&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<p>Replace <code>&lt;your-team-name&gt;</code> with your Zero Trust <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
<ol start="2">
<li>
<p>Follow the prompts to log in to your identity provider.</p>
<p>Once you have authenticated, the App Launcher will display tiles showing the applications that you are authorized to use. Windows servers (targets) available through browser-based RDP will also appear as tiles. If a target is reachable through multiple Access applications, the target will have a tile per Access application.</p>
</li>
<li>
<p>Select the target you want to connect to.</p>
<p>The App Launcher tile will launch a URL of the form <code>https://&lt;app-domain&gt;/rdp/&lt;vnet-id&gt;/&lt;target-ip&gt;/&lt;port&gt;</code>. You may also navigate directly to this URL.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="virtual-network-id">Virtual network ID</h3>
@markup("md", "content/.markup/bodies/5502.md")
</aside>
<ol start="4">
<li>Select the port that you want to connect to. The port selection screen only appears if the Access application allows RDP traffic on multiple ports (for example, port <code>3389</code> and port <code>65321</code>).</li>
<li>(Optional) In your browser settings, allow the Access application to access the clipboard. Clipboard access is subject to <a href="#configure-connection-settings">policy restrictions</a> configured by your administrator.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5501.md")
</aside>
<ol start="6">
<li>Enter your Windows username and password. For more information on how to format your username, refer to <a href="#user-identifier-formats">User identifier formats</a>.</li>
</ol>
<p>You now have access to the remote Windows desktop.</p>
<h2 id="connection-settings">Connection settings</h2>
<p>Connection settings restrict data transfer between the user's local machine and the browser-based RDP session. You can control text (copy and paste) and file transfers. Text controls manage clipboard content. File controls <span class="nb-badge">Beta</span> manage file uploads and downloads. These controls are configured per policy, so you can grant different permissions to different groups of users.</p>
<h3 id="default-behavior">Default behavior</h3>
<p>For new policies, both text controls and file controls are denied by default. You must explicitly allow each action. Existing applications retain full text clipboard access for backward compatibility. File controls are denied unless explicitly enabled.</p>
<h3 id="available-settings">Available settings</h3>
<p>Text controls and file controls use the same directional options:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Client to remote RDP session allowed</em></td>
<td>Users can transfer data from their local client into the browser-based RDP session.</td>
</tr>
<tr>
<td><em>Remote RDP session to client allowed</em></td>
<td>Users can transfer data from the browser-based RDP session to their local client.</td>
</tr>
<tr>
<td><em>Both directions allowed</em></td>
<td>Users can transfer data in both directions.</td>
</tr>
<tr>
<td><em>Disable copying/pasting</em></td>
<td>Users are not allowed to transfer data between the browser-based RDP session and their local client.</td>
</tr>
</tbody>
</table>
<p>For example, you can allow text copy and paste in both directions while restricting file transfers to uploads only.</p>
<p>When a user attempts a restricted clipboard action, the clipboard content is replaced with a message informing them that the action is not allowed. When file transfer is restricted, upload methods are disabled and download buttons do not appear in the control panel.</p>
<h3 id="configure-connection-settings">Configure connection settings</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5524.md")
</div></div>
<h3 id="transfer-files">Transfer files <span class="nb-badge">Beta</span></h3>
<p>To manage transfers, select the settings gear icon on the left side of the RDP session. You can drag this icon along the left edge to reposition it.</p>
<p>File transfer has the following limits:</p>
<ul>
<li><strong>Maximum file size:</strong> 2 GB per file (upload and download)</li>
<li><strong>Maximum files per upload:</strong> 1,000 files</li>
</ul>
<h4 id="upload-files-local-to-remote">Upload files (local to remote)</h4>
<p>To transfer files from your local machine to the remote Windows session, drag files onto the browser window or use the control panel. Drag and drop supports individual files and folders (including subfolders, up to 1,000 total entries). The control panel file picker selects individual files only. Files land on the active element of the remote desktop. For example, if you have a folder open in File Explorer, the file lands in that folder.</p>
<h4 id="download-files-remote-to-local">Download files (remote to local)</h4>
<p>To transfer files from the remote Windows session to your local machine:</p>
<ol>
<li>In the remote Windows session, copy the file you want to download. Right-click the file and select <strong>Copy</strong>, or select the file and press <strong>Ctrl+C</strong>.</li>
<li>The control panel icon does a small hop to indicate that a file is available. Open the control panel to view the file.</li>
<li>Select one of the following options:
<ul>
<li><strong>Download</strong>: Download the file to your local machine.</li>
<li><strong>Download zip</strong>: Download multiple files at once as a zipped folder to your local machine.</li>
<li><strong>Print</strong>: <a href="#print-pdfs">Print PDF files</a> to a local printer on your network.</li>
</ul>
</li>
</ol>
<h4 id="print-pdfs">Print PDFs</h4>
<p>You can print PDF files from the clipboard panel to a local printer. To print a single file, select the print icon next to the PDF. To print multiple files at once, copy the files together into the clipboard on the remote machine, then select <strong>Print all PDFs</strong> in the clipboard panel. The files are combined into a single PDF and sent to your browser as one print job.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5500.md")
</aside>
<h4 id="limitations">Limitations</h4>
<ul>
<li>Transfer history is discarded when the RDP session ends.</li>
<li>The remote Windows server must support file transfer via the RDP clipboard virtual channel. Windows Server 2012 and later support this by default.</li>
<li>If the remote server does not support file transfer, text clipboard continues to work normally.</li>
</ul>
<h2 id="compatibility">Compatibility</h2>
<h3 id="rdp-server-operating-systems">RDP server operating systems</h3>
<p>Browser-based RDP supports connecting to Windows machines that run the following operating systems:</p>
<ul>
<li>Windows 11 Pro</li>
<li>Windows 11 Enterprise</li>
<li>Windows 10 Pro</li>
<li>Windows 10 Enterprise</li>
<li>Windows Server 2025</li>
<li>Windows Server 2022</li>
<li>Windows Server 2019</li>
<li>Windows Server 2016</li>
</ul>
<h3 id="browsers">Browsers</h3>
<table>
<thead>
<tr>
<th>Browser</th>
<th>Compatibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Chrome</td>
<td>✅</td>
</tr>
<tr>
<td>Mozilla Firefox</td>
<td>✅</td>
</tr>
<tr>
<td>Safari</td>
<td>✅</td>
</tr>
<tr>
<td>Microsoft Edge (Chromium-based)</td>
<td>✅</td>
</tr>
<tr>
<td>Other Chromium-based browsers (Opera, Brave)</td>
<td>✅</td>
</tr>
<tr>
<td>Internet Explorer 11 and below</td>
<td>❌</td>
</tr>
</tbody>
</table>
<h3 id="powershell">Powershell</h3>
<p>Run Powershell 7 or higher to mitigate a prior Microsoft issue where keystrokes are not recorded.</p>
<h3 id="user-identifier-formats">User identifier formats</h3>
<p>Browser-based RDP supports connecting to Windows machines using the following login credentials:</p>
<h4 id="security-account-manager-sam">Security Account Manager (SAM)</h4>
<p>SAM-formatted user identifiers are supported with and without spaces.</p>
<p>Examples:</p>
<ul>
<li><code>DOMAIN\username</code></li>
<li><code>DOMAIN\username with spaces</code></li>
<li><code>.\username</code></li>
<li><code>.\username with spaces</code></li>
<li><code>username</code></li>
<li><code>username with spaces</code></li>
</ul>
<details class="nb-details" open><summary>Character limits</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5525.md")
</div></details>
<h4 id="user-principal-name-upn">User Principal Name (UPN)</h4>
<p>UPN-formatted user identifiers are supported with spaces, with and without quotes.</p>
<p>Examples:</p>
<ul>
<li><code>&quot;username with spaces&quot;@domain.org</code></li>
<li><code>username with spaces@domain.org</code></li>
<li><code>username@domain.org</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5499.md")
</aside>
<h4 id="microsoft-entra-id">Microsoft Entra ID</h4>
<p>User identifiers that are bound to Microsoft Entra ID domains must enter their username as <code>AzureAD\user@example.com</code> or <code>AzureAD\user</code>. The <code>AzureAD\</code> prefix is case-insensitive.
The login flow differs slightly when using an Microsoft Entra ID-bound username:</p>
<ol>
<li>Enter your username in one of the formats outlined above.</li>
<li>Once the username is entered, the password box will disappear and the RDP connection will initiate.</li>
<li>The RDP server will then prompt for the password before granting access to the RDP server.</li>
</ol>
<h3 id="cloudflare-products">Cloudflare products</h3>
<p>When using Access self-hosted applications, the majority of Cloudflare products will be compatible with your application.</p>
<p>However, the following products are not supported:</p>
<ul>
<li><a href="/automatic-platform-optimization">Automatic Platform Optimization</a></li>
<li><a href="/zaraz">Zaraz</a></li>
<li><a href="/google-tag-gateway">Google tag gateway for advertisers</a></li>
</ul>
<p>You can disable Zaraz for a specific application - instead of across your entire zone - using a <a href="/rules/configuration-rules/">Configuration Rule</a> scoped to the application domain.</p>
<p>Google tag gateway is configured at the zone level and cannot be scoped to specific hostnames. To use Access binding cookie on a hostname, disable Google tag gateway for the entire zone.</p>
<h2 id="known-limitations">Known limitations</h2>
<ul>
<li><strong>TLS certificate verification</strong>: Cloudflare uses TLS to connect to the RDP target but does not verify the origin TLS certificate.</li>
<li><strong>Device authentication identity</strong>: Since browser-based RDP traffic does not go through the Cloudflare One Client, users cannot use their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/#configure-warp-sessions-in-access">Cloudflare One Client session identity</a> to authenticate.</li>
<li><strong>Audio over RDP</strong>: Users cannot use their microphone and speaker to interact with the remote machine.</li>
<li><strong>Clipboard size limit</strong>: Data copied between the local machine and the browser-based RDP session may not exceed 500 KB.</li>
<li><strong>Clipboard data types</strong>: Text clipboard controls only support text data. Image clipboard transfers are not supported.</li>
<li><strong>File transfer availability</strong>: File transfer is in beta. Refer to <a href="#transfer-files">Transfer files</a> for supported functionality and limitations.</li>
<li><strong>Print to local printer</strong>: Local printing from a browser-based RDP session is only supported for PDF files through the <a href="#print-pdfs">file transfer control panel</a>.</li>
<li><strong>Network Level Authentication for Entra-joined accounts</strong>: Browser-based RDP does not support PKU2U authentication which is required for <a href="https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access#why-allow-connections-only-with-network-level-authentication">Network Level Authentication (NLA)</a> with Entra-joined accounts. Connecting to Entra-joined accounts requires disabling enforcement of NLA on the remote Windows machine. You can disable NLA from <strong>Settings</strong> &gt; <strong>System</strong> &gt; <strong>Remote Desktop</strong>, or use the Local Group Policy Editor to disable <strong>Require user authentication for remote connections by using Network Level Authentication</strong>. When disabling NLA, only turn off NLA itself — do not switch the security layer to the legacy <strong>RDP</strong> option, because browser-based RDP still requires TLS (refer to the <strong>RDP security layer must allow TLS</strong> limitation).</li>
<li><strong>RDP security layer must allow TLS</strong>: Browser-based RDP connects to the remote machine over TLS, so the machine's RDP security layer must be set to at least <strong>Negotiate</strong> (or <strong>SSL</strong>). If the server is set to use the legacy <strong>RDP</strong> security layer, connections will fail. You can configure this in the Local Group Policy Editor by setting <strong>Require use of specific security layer for remote (RDP) connections</strong> to <strong>Negotiate</strong> or <strong>SSL</strong>.</li>
<li><strong>Clipboard browser compatibility</strong>: Automatic clipboard sharing between the local and remote machine is only available in Chromium-based browsers by default (Google Chrome, Microsoft Edge, Opera, Brave). To enable this functionality in Firefox:
<ol>
<li>Type <code>about:config</code> into the browser address bar and press <strong>Enter</strong>.</li>
<li>Accept the warning prompt if displayed.</li>
<li>Search for <code>dom.events.testing.asyncClipboard</code> and set it to <code>true</code>.</li>
<li>Search for <code>dom.events.asyncClipboard.clipboardItem</code> and set it to <code>true</code>.</li>
<li>Search for <code>dom.events.asyncClipboard.readText</code> and set it to <code>true</code>.</li>
</ol>
</li>
</ul>
