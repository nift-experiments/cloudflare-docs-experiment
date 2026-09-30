<p>Client version assignments let you target a specific Cloudflare One Client (formerly WARP) version at a group of devices from the Cloudflare dashboard, without touching your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6377.md")
</div> or asking users to update the client themselves.
<p>Once an assignment is in place, matching devices silently upgrade or downgrade to the target version. End users see an <strong>Update in progress</strong> banner in the client GUI while the install runs. The client returns to normal operation once the update completes.</p>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6378.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6376.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>A <strong>deployment group</strong> links one or more target client versions to one or more policy IDs from your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>. Each entry in the group specifies a <code>target_environment</code> (<code>windows</code> or <code>macos</code>) and the <code>version</code> to deploy on that platform. A single deployment group can target both platforms at once.</p>
<p>When you save a deployment group, the Cloudflare API pushes the assignment to every device whose device profile policy ID is in the group. Each device then:</p>
<ol>
<li>Compares its running version against the assigned version on its next registration refresh.</li>
<li>If the versions differ, downloads the target installer and verifies its cryptographic signature.</li>
<li>Runs the installer silently and resumes normal operation once the new version is in place.</li>
</ol>
<p>The client coordinates the install through a separate persistent OS service that ships alongside the existing service in client version <code>2026.6.0</code> and later. If any step fails — download, signature verification, or install — the device stays on its previous version and remains functional.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6375.md")
</aside>
<h2 id="set-up-a-deployment-group">Set up a deployment group</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6382.md")
</div></div>
<h2 id="when-a-device-evaluates-an-assignment">When a device evaluates an assignment</h2>
<p>After you create, update, or delete a deployment group, the API notifies affected devices of the change. Delivery can take up to 15 minutes. Once a device receives the notification, it evaluates the assignment shortly after and installs the target version if it differs from the running version.</p>
<p>Devices also re-evaluate the most recent assignment they have received in these additional situations:</p>
<ul>
<li><strong>When the client service starts or restarts.</strong></li>
<li><strong>When the device wakes from sleep.</strong></li>
</ul>
<h2 id="verify-a-device-received-the-assignment">Verify a device received the assignment</h2>
<p>To confirm a device has received its assigned version, open a terminal on the device and run:</p>
<pre><code class="language-sh">warp-cli settings&#10;</code></pre>
<p>The output includes the resolved target version under <code>version_config</code>. If the device is not yet running that version, the next evaluation triggers an install.</p>
<h2 id="override-an-assignment-with-mdm">Override an assignment with MDM</h2>
<p>You can suppress client version assignments on individual devices by setting <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#allow_managed_deployments"><code>allow_managed_deployments</code></a> to <code>false</code> in your MDM file. When this parameter is <code>false</code>, the device ignores any assignment from the dashboard and stays on its current version. Use this for devices that must be pinned through MDM rather than the dashboard.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Devices must be running client version <code>2026.6.0</code> or later to apply an assignment. Older versions ignore the assignment entirely.</li>
<li>Once an install has started on a device, it cannot be cancelled. Changing the target version while a device is still downloading the previous target cancels the download cleanly.</li>
<li>Each device profile policy ID can belong to only one deployment group at a time.</li>
</ul>
<h2 id="antivirus-and-endpoint-security-configuration">Antivirus and endpoint security configuration</h2>
<p>Starting in version <code>2026.6.0</code>, the client install adds a second persistent OS service that handles updates triggered by client version assignments. If your endpoint protection or antivirus tools maintain process or service allowlists, add the following alongside your existing entries for the Cloudflare One Client:</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Service identifier</th>
<th>Process name</th>
</tr>
</thead>
<tbody>
<tr>
<td>macOS</td>
<td><code>com.cloudflare.warp.updater</code></td>
<td><code>warp-updater</code></td>
</tr>
<tr>
<td>Windows</td>
<td><code>CloudflareWARPUpdater</code></td>
<td><code>warp-updater-armed.exe</code></td>
</tr>
</tbody>
</table>
<h2 id="troubleshoot-a-failed-update">Troubleshoot a failed update</h2>
<p>If a device does not receive its assigned version, collect diagnostic logs using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/"><code>warp-diag</code></a>. The diagnostic archive includes an <code>updater/</code> directory with per-attempt installer logs and a human-readable update history summary that you can share with Cloudflare Support.</p>
