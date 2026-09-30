<p>After you <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">create a proxy endpoint</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#2-create-a-pac-file">create a PAC file</a>, configure your devices to use the PAC file URL. You can configure system-level proxy settings (which apply to most browsers) or configure individual browsers separately.</p>
<p>Chromium-based browsers (Google Chrome, Microsoft Edge, Brave) use the operating system proxy settings. Firefox uses its own proxy settings by default and must be configured separately. Safari and iOS/iPadOS do not support the HTTPS proxy type required by proxy endpoints.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you configure a PAC file on your device, make sure you have:</p>
<ul>
<li>A <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#1-create-a-proxy-endpoint">Cloudflare Gateway proxy endpoint</a></li>
<li>A PAC file URL (either <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">hosted by Cloudflare</a> or <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#self-hosting-pac-files">self-hosted</a>)</li>
<li>The <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Cloudflare certificate installed</a> on your device (required for HTTPS inspection)</li>
</ul>
<h2 id="configure-system-proxy-settings">Configure system proxy settings</h2>
<p>Configure your operating system to use the PAC file. This applies the proxy to all browsers that use system proxy settings (Chrome, Edge, Brave).</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5860.md")
</div></div>
<h2 id="configure-firefox-separately">Configure Firefox separately</h2>
<p>Firefox uses its own proxy settings and does not inherit the operating system proxy configuration by default. To configure Firefox to use your PAC file:</p>
<ol>
<li>In Firefox, go to <strong>Settings</strong> and scroll to <strong>Network Settings</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Select <strong>Automatic proxy configuration URL</strong>.</li>
<li>Enter your PAC file URL (for example, <code>https://pac.cloudflare-gateway.com/&lt;account-id&gt;/&lt;slug&gt;</code>).</li>
<li>Select <strong>OK</strong>.</li>
</ol>
<p>HTTP traffic from Firefox is now filtered by Gateway.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5846.md")
</aside>
<h2 id="deploy-pac-files-at-scale">Deploy PAC files at scale</h2>
<p>For enterprise environments, you can deploy PAC file configurations to managed devices using Group Policy, MDM, or browser management tools.</p>
<h3 id="windows-group-policy-gpo">Windows Group Policy (GPO)</h3>
<p>You can deploy the PAC file URL through Group Policy by configuring the Internet Settings preference:</p>
<ol>
<li>Open <strong>Group Policy Management</strong> and create or edit a Group Policy Object.</li>
<li>Go to <strong>User Configuration</strong> &gt; <strong>Preferences</strong> &gt; <strong>Windows Settings</strong> &gt; <strong>Registry</strong>.</li>
<li>Add a registry item with the following values:
<ul>
<li><strong>Hive</strong>: <code>HKEY_CURRENT_USER</code></li>
<li><strong>Key path</strong>: <code>Software\Microsoft\Windows\CurrentVersion\Internet Settings</code></li>
<li><strong>Value name</strong>: <code>AutoConfigURL</code></li>
<li><strong>Value type</strong>: <code>REG_SZ</code></li>
<li><strong>Value data</strong>: Your PAC file URL</li>
</ul>
</li>
</ol>
<h3 id="microsoft-intune">Microsoft Intune</h3>
<p>Use the Settings Catalog to deploy proxy auto-configuration:</p>
<ol>
<li>In the <a href="https://intune.microsoft.com/">Microsoft Intune admin center</a>, create a new <strong>Configuration profile</strong>.</li>
<li>Select <strong>Settings catalog</strong> as the profile type.</li>
<li>Search for <strong>Proxy</strong> and configure the auto-config URL setting for your target platform (Windows or macOS).</li>
<li>Assign the profile to your device groups.</li>
</ol>
<h3 id="apple-mdm-jamf-pro-jamf-school-other-mdm">Apple MDM (Jamf Pro, Jamf School, other MDM)</h3>
<p>Deploy a configuration profile with the proxy payload:</p>
<ol>
<li>Create a new configuration profile in your MDM solution.</li>
<li>Add a <strong>Global HTTP Proxy</strong> or <strong>Network</strong> payload.</li>
<li>Set the proxy type to <strong>Auto</strong> and enter your PAC file URL.</li>
</ol>
<p>For detailed payload settings, refer to the <a href="https://support.apple.com/guide/deployment/network-proxy-configuration-settings-depb27492e34/web">Network Proxy Configuration settings</a> in the Apple Platform Deployment guide.</p>
<h3 id="google-admin-console-chromeos">Google Admin console (ChromeOS)</h3>
<p>For managed ChromeOS devices and Chrome browsers:</p>
<ol>
<li>In the <a href="https://admin.google.com/">Google Admin console</a>, go to <strong>Devices</strong> &gt; <strong>Networks</strong>.</li>
<li>Select the organizational unit for your managed devices.</li>
<li>Add or edit a network configuration (Wi-Fi or Ethernet).</li>
<li>Under <strong>Proxy settings</strong>, select <strong>Automatic proxy configuration</strong>.</li>
<li>Enter your PAC file URL.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>For more information, refer to <a href="https://support.google.com/chrome/a/answer/2634553">Set up networks for managed devices</a>.</p>
<h3 id="chrome-browser-cloud-management">Chrome Browser Cloud Management</h3>
<p>To deploy proxy settings to managed Chrome browsers on any operating system:</p>
<ol>
<li>In the <a href="https://admin.google.com/">Google Admin console</a>, go to <strong>Devices</strong> &gt; <strong>Chrome</strong> &gt; <strong>Settings</strong>.</li>
<li>Select the organizational unit for your managed browsers.</li>
<li>Search for <strong>Proxy</strong> and configure the <strong>Proxy mode</strong> to <strong>Use a .pac proxy auto-config file</strong>.</li>
<li>Enter your PAC file URL.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="verify-your-configuration">Verify your configuration</h2>
<p>After you configure a PAC file on your device, verify that traffic routes through Gateway:</p>
<ol>
<li>Open a browser on the configured device.</li>
<li>Create an <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a> to block a test domain (for example, <code>example.com</code>).</li>
<li>Visit the blocked domain in your browser.</li>
<li>Verify that the Gateway block page appears.</li>
</ol>
<p>If the block page does not appear, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/#troubleshoot-configurations">PAC file troubleshooting section</a> for debugging steps.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-one/traffic-policies/http-policies/">Create HTTP policies</a> to filter proxy endpoint traffic.</li>
<li>Review <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/">PAC file best practices</a> for formatting, performance optimization, and bypass rules.</li>
<li>Use the <a href="/cloudflare-one/traffic-policies/http-policies/#proxy-endpoint">Proxy Endpoint selector</a> in HTTP and network policies to apply rules to proxy traffic.</li>
</ul>
