<p>Review common troubleshooting scenarios for Digital Experience Monitoring (DEX).</p>
<h2 id="data-visibility">Data visibility</h2>
<h3 id="no-data-displayed-for-certain-users">No data displayed for certain users</h3>
If you do not see DEX data for specific users in your organization, verify the following:
<ul>
<li><strong>Client version</strong>: Ensure the users are running a version of the Cloudflare One Client that supports DEX.</li>
<li><strong>DEX enabled</strong>: Confirm that DEX is enabled for the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> assigned to those users.</li>
<li><strong>Traffic routing</strong>: DEX requires that traffic to Cloudflare's orchestration API is not blocked by local firewalls or SSL-inspecting proxies.</li>
</ul>
<h3 id="fleet-status-not-updating">Fleet status not updating</h3>
The Fleet status dashboard can take several minutes to reflect changes in device connectivity. If a device remains in an incorrect state, try disconnecting and reconnecting the Cloudflare One Client to force a status update.
<h2 id="remote-captures">Remote captures</h2>
<h3 id="remote-capture-fails-to-start">Remote capture fails to start</h3>
Remote captures require the Cloudflare One Client to be connected and able to communicate with the Cloudflare control plane. If a capture fails to start:
<ul>
<li>Verify the device status in the Zero Trust dashboard.</li>
<li>Ensure the device has sufficient disk space to store the capture files before upload.</li>
<li>Check for any local firewall rules that might be blocking the capture command.</li>
</ul>
<hr />
<h2 id="how-to-contact-support">How to contact Support</h2>
<p>If you cannot resolve the issue, <a href="/support/contacting-cloudflare-support/">open a support case</a>. Please provide a <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/">remote capture</a> from the Zero Trust dashboard for the affected device.</p>
