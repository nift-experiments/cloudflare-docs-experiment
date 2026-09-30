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
