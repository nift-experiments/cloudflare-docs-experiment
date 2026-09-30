<p>The Firewall device posture attribute ensures that a firewall is running on a device.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-firewall-check">Enable the firewall check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>Firewall</strong>.</li>
<li>Enter a descriptive name for the check.</li>
<li>Select your operating system.</li>
<li>Configure <strong>Enable firewall check</strong> based on your desired security policy:
<ul>
<li><strong>Enabled</strong>: (Recommended) The posture check passes only if the firewall is running.</li>
<li><strong>Disabled</strong>: The posture check passes only if the firewall is turned off.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5917.md")
</aside>
7. Select **Save**.
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the firewall check is returning the expected results.</p>
<h2 id="validate-firewall-status">Validate firewall status</h2>
<p>Operating systems determine firewall configuration in various ways. Follow the steps below to understand how the Cloudflare One Client determines if the firewall is enabled.</p>
<h3 id="on-macos">On macOS</h3>
<p>macOS has two firewalls: an application-based firewall and a port-based firewall. The Cloudflare One Client will report a firewall is enabled if either firewall is running.</p>
<h4 id="application-based-firewall">Application-based firewall</h4>
<ol>
<li>Open <strong>System Settings</strong> and go to <strong>Network</strong>.</li>
<li>Verify that <strong>Firewall</strong> is <code>Active</code>.</li>
</ol>
<h4 id="port-based-firewall">Port-based firewall</h4>
<ol>
<li>Open Terminal and run:</li>
</ol>
<pre><code class="language-sh">sudo /sbin/pfctl -s info&#10;</code></pre>
<ol start="2">
<li>Verify that <strong>Status</strong> is <code>Enabled</code>.</li>
</ol>
<h3 id="on-windows">On Windows</h3>
<ol>
<li>Open PowerShell and run:</li>
</ol>
<pre><code class="language-powershell">Get-NetFirewallProfile -PolicyStore ActiveStore -Name Public&#10;</code></pre>
<ol start="2">
<li>Verify that <strong>Enabled</strong> is <code>True</code>.</li>
</ol>
