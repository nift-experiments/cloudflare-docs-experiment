<p>This guide covers how to deploy the Cloudflare One Client (formerly WARP) using Jamf.</p>
<h2 id="macos">macOS</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>A <a href="https://www.jamf.com/products/jamf-pro/">Jamf Pro account</a></li>
<li>A Cloudflare account that has a <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a></li>
<li>macOS devices enrolled in Jamf</li>
</ul>
<h3 id="1-upload-the-cloudflare-one-client-package"><ol>
<li>Upload the Cloudflare One Client package</li>
</ol></h3>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos">Download</a> the <code>Cloudflare_WARP.pkg</code> file.</li>
<li>Log in to your <a href="https://www.jamf.com/">Jamf</a> account.</li>
<li>Go to <strong>*Settings</strong> (gear icon).</li>
<li>Select <strong>Computer Management</strong> &gt; <strong>Packages</strong> &gt; <strong>New</strong>.</li>
<li>Upload the <code>Cloudflare_WARP_&lt;VERSION&gt;.pkg</code> file.</li>
<li>For <strong>Display Name</strong>, we recommend entering the version number of the package being uploaded.</li>
<li>Select <strong>Save</strong> to complete the upload.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="repeat-this-step-to-update-the-cloudflare-one-client-when-a-new-release-is-available">Repeat this step to update the Cloudflare One Client when a new release is available</h3>
@markup("md", "content/.markup/bodies/6387.md")
</aside>
<h3 id="2-create-a-jamf-policy"><ol start="2">
<li>Create a Jamf policy</li>
</ol></h3>
<ol>
<li>Go to <strong>Computers</strong> &gt; <strong>Policies</strong> &gt; <strong>+ New</strong>.</li>
<li>Enter a <strong>Display Name</strong> such as <code>Cloudflare One Client</code>.</li>
<li>For <strong>Triggers</strong>, choose the events that will trigger a Cloudflare One Client deployment. We recommend selecting <strong>Startup</strong>, <strong>Login</strong>, <strong>Enrollment Complete</strong>, and <strong>Recurring Check-in</strong>.</li>
<li>Select <strong>Packages</strong> &gt; <strong>Configure</strong>.</li>
<li>Select <strong>Add</strong> next to the <code>Cloudflare_WARP_&lt;VERSION&gt;.pkg</code> file you previously uploaded.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="3-add-a-configuration-profile"><ol start="3">
<li>Add a Configuration Profile</li>
</ol></h3>
<ol>
<li>Go to <strong>Computers</strong> &gt; <strong>Configuration Profiles</strong> &gt; <strong>New</strong>.</li>
<li>Enter a name for your new profile, such as <code>Cloudflare Zero Trust</code>.</li>
<li>Scroll through the <strong>Options</strong> list and select <strong>Application &amp; Custom Settings</strong> &gt; <strong>Upload</strong>.</li>
<li>In <strong>Preference Domain</strong>, enter <code>com.cloudflare.warp</code>.</li>
<li>To configure the <strong>Property List</strong>:
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#plist-file">Create a <code>plist</code> file</a> with your desired deployment parameters.</li>
<li>Upload your <code>plist</code> file to Jamf and select <strong>Save</strong>.</li>
</ol>
</li>
<li>(Recommended) Advanced security features require deploying a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">user-side certificate</a> so that devices can establish trust with Cloudflare when their traffic is inspected. To deploy a user-side certificate using Jamf:
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">generate and activate</a> a Cloudflare root certificate.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#download-a-cloudflare-root-certificate">Download the Cloudflare root certificate</a> in <code>.pem</code> format.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#convert-the-certificate">Convert</a> the certificate to <code>.cer</code> format.</li>
<li>In your Jamf configuration profile, scroll down the <strong>Options</strong> list and select <strong>Certificate</strong> &gt; <strong>Configure</strong>.</li>
<li>Enter a <strong>Display name</strong> for the certificate such as <code>Cloudflare root certificate</code>.</li>
<li>In the <strong>Select Certificate Option</strong> dropdown, select <em>Upload</em>.</li>
<li>Upload your <code>.cer</code> file and select <strong>Save</strong>.</li>
</ol>
</li>
<li>Go to <strong>Scope</strong> to configure which devices in your organization will receive this profile.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Jamf will now deploy the Cloudflare One Client to targeted macOS devices.
After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h2 id="ios">iOS</h2>
<p>The Cloudflare One Agent allows for an automated install via Jamf.</p>
<h3 id="prerequisites-1">Prerequisites</h3>
<p>Create an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#ios">XML file</a> with your custom deployment preferences.</p>
<h3 id="configure-jamf-for-ios">Configure Jamf for iOS</h3>
<ol>
<li>Log in to your <a href="https://www.jamf.com/">Jamf</a> account.</li>
<li>Go to <strong>Devices</strong> &gt; <strong>Mobile Device Apps</strong> &gt; <strong>+ New</strong>.</li>
<li>Select <em>App store app or apps purchased in volume</em> and select <strong>Next</strong>.</li>
<li>In the search box, enter <code>Cloudflare One Agent</code>. Select <strong>Next</strong>.</li>
<li>In the row for <em>Cloudflare One Agent by Cloudflare Inc.</em>, select <strong>Add</strong>. To verify that it is the correct application, view it in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">App Store</a>.</li>
<li>Go to <strong>Scope</strong> and specify the devices in your organization that will receive the application.</li>
<li>Go to <strong>App Configuration</strong> and copy/paste your XML file.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Jamf is now configured to deploy the Cloudflare One Agent.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h3 id="per-app-vpn">Per-app VPN</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6386.md")
</aside>
<p>Before proceeding with per-app VPN configuration, you must make sure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">Auto connect</a> is disabled in Zero Trust. To disable Auto connect:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Select your device profile and select <strong>Edit</strong>.</li>
<li>Turn off <strong>Auto Connect</strong>.</li>
</ol>
<p>To configure per-app VPN:</p>
<ol>
<li>Log in to the Jamf dashboard for your organization.</li>
<li>Go to <strong>Devices</strong> &gt; <strong>Configuration Policies</strong> &gt; select <strong>+ New</strong>.</li>
<li>Under <strong>Options</strong>, select <strong>VPN</strong>. Then:
<ul>
<li>Give the VPN a <strong>Connection Name</strong>.</li>
<li>Select <em>Per-App VPN</em> from the <strong>VPN Type</strong> dropdown menu.</li>
<li>Check the box for <strong>Automatically start Per-App VPN connection</strong>.</li>
</ul>
</li>
<li>Under Per-App VPN Connection Type, set the <strong>Connection Type</strong> to <em>Custom SSL</em> via the dropdown menu. Then, enter <code>com.cloudflare.cloudflareoneagent</code> as the <strong>Identifier</strong>, <code>1.1.1.1</code> as the <strong>Server</strong>, and <code>com.cloudflare.cloudflareoneagent.worker</code> as the <strong>Provider Bundle Identifier</strong>.</li>
<li>Set the <strong>Provider Type</strong> to <em>Packet-Tunnel</em> and select the checkboxes for <strong>Include All Networks</strong> and <strong>Enable VPN on Demand</strong>.</li>
<li>Go to the <strong>Scope</strong> tab and add the devices that will use the Per-App VPN.</li>
<li>Save the Configuration Profile.</li>
<li>Go to <strong>Devices</strong> &gt; <strong>Mobile Device Apps</strong> &gt; select <strong>+ New</strong>.</li>
<li>As the <strong>App Type</strong>, select <strong>App Store app or apps purchased in volume</strong> and select <strong>Next</strong>.</li>
<li>In the search bar, enter the name of the app that you want to use the VPN for and select <strong>Next</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6385.md")
</aside>
<ol start="11">
<li>Find the app you are looking for in the search results and select <strong>Add</strong>.</li>
<li>Select your preferred <strong>Distribution Method</strong> and under <strong>Per-App Networking</strong>, select the VPN connection you just configured.</li>
<li>Repeat steps 8-12 for each app you want to use the VPN.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6384.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6383.md")
</aside>
