<p>This section covers the most common issues you might encounter as you deploy the Cloudflare One Client (formerly WARP) in your organization, or turn on new features that interact with the client.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshoot-the-cloudflare-one-client">Troubleshoot the Cloudflare One Client</h3>
@markup("md", "content/.markup/bodies/6099.md")
</aside>
<h2 id="connectivity-and-registration">Connectivity and registration</h2>
<h3 id="stuck-on-disconnected-or-frequent-flapping">Stuck on &quot;Disconnected&quot; or frequent flapping</h3>
If the Cloudflare One Client is stuck in the `Disconnected` state or frequently changes between `Connected` and `Disconnected`, this indicates that the client cannot establish a connection to Cloudflare's global network.
<p>In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">client diagnostic logs</a>, <code>daemon.log</code> will typically show one or more of the following errors:</p>
<ul>
<li>Happy Eyeball checks failing: <code>All Happy Eyeballs checks failed</code>.</li>
<li>Connectivity checks timing out for <code>connectivity.cloudflareclient.com</code>.</li>
</ul>
<p><strong>Common causes</strong>:</p>
<ul>
<li><strong>Firewall blocks</strong>: A local or network firewall is blocking the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">required IP addresses</a>.</li>
<li><strong>VPN interference</strong>: A third-party VPN is fighting for control over the routing table or DNS. Refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/vpn/">VPN compatibility guide</a>.</li>
<li><strong>ISP blocks</strong>: Your country or ISP may be explicitly blocking client traffic.</li>
</ul>
<h3 id="registration-error-authentication-expired">Registration error (Authentication Expired)</h3>
When registering the client, you may see `Authentication Expired` or `Registration error. Please try again later`.
<p><strong>Common causes</strong>:</p>
<ul>
<li><strong>System clock out of sync</strong>: Your computer system clock must be properly synced via NTP. If your clock is off by more than 20 seconds, the authentication token (JWT) will be invalid.</li>
<li><strong>Prompt timeout</strong>: You must complete the registration in your browser and return to the client within one minute of the prompt.</li>
</ul>
<h3 id="linux-dns-connectivity-check-failed">(Linux) DNS connectivity check failed</h3>
This error often means that `systemd-resolved` is not allowing the client to resolve DNS requests. In `daemon.log`, you will see `DNS connectivity check failed to resolve host="warp-svc."`.
<p><strong>Solution</strong>:</p>
<ol>
<li>Add <code>ResolveUnicastSingleLabel=yes</code> to <code>/etc/systemd/resolved.conf</code>.</li>
<li>Ensure no other DNS servers are explicitly configured in that file.</li>
<li>Restart the service: <code>sudo systemctl restart systemd-resolved.service</code>.</li>
</ol>
<h3 id="mac-linux-invalid-character-in-resolv-conf">(Mac/Linux) Invalid character in resolv.conf</h3>
The client cannot parse `resolv.conf` files containing invalid characters like `!@#$%^&*()<>?` in `search` directives. Remove these characters to restore service.
<h2 id="browser-and-certificate-issues">Browser and certificate issues</h2>
<h3 id="your-connection-is-not-private-or-untrusted-warnings">&quot;Your connection is not private&quot; or untrusted warnings</h3>
Advanced security features require the [Cloudflare root certificate](/cloudflare-one/team-and-resources/devices/user-side-certificates/) to be trusted on the device.
<ul>
<li><strong>Chrome/Edge</strong>: These browsers cache certificates. If you installed the certificate while the browser was running, you must restart the browser.</li>
<li><strong>Root certificate expiry</strong>: The default Cloudflare root certificate expired on February 2, 2025. If you are seeing errors, <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">generate and activate a new certificate</a> in the dashboard.</li>
</ul>
<h3 id="2025-certificate-migration">2025 Certificate migration</h3>
Starting with version 2024.12.554.0, the client can automatically install new certificates as soon as they are **Available** in the dashboard. For older versions, certificates had to be marked **In-Use** first. Ensure **Install CA to system certificate store** is enabled in your [Device settings](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/).
<h2 id="windows-specific-issues">Windows-specific issues</h2>
<h3 id="windows-shows-no-internet-access">Windows shows &quot;No Internet access&quot;</h3>
This is often a cosmetic error with Windows Network Connectivity Status Indicator (NCSI). Apps like Outlook or JumpCloud may refuse to connect because of this status.
<p><strong>Solution</strong>:
Configure NCSI to detect the client's local DNS proxy and use active probing by setting these registry keys to <code>1</code>:</p>
<ul>
<li><code>HKEY_LOCAL_MACHINE\SOFTWARE\POLICIES\MICROSOFT\Windows\NetworkConnectivityStatusIndicator\UseGlobalDNS</code></li>
<li><code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet\EnableActiveProbing</code></li>
</ul>
<h3 id="setup-wizard-ends-prematurely">Setup Wizard ends prematurely</h3>
This usually indicates a missing dependency, such as .NET Framework `4.7.2` or later. Legacy systems (like Windows 10 Enterprise 1607) may require a manual update of the [.NET Framework Runtime](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net472).
<h2 id="other-environment-issues">Other environment issues</h2>
<h3 id="wsl2-connectivity">WSL2 connectivity</h3>
If WSL2 loses connectivity, check your [split tunnel configuration](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/). The IP range used by WSL to communicate with the host may be accidentally included in the tunnel. Exclude the WSL network range to restore connectivity.
<h3 id="smtp-port-25-blocked">SMTP port 25 blocked</h3>
The client blocks outgoing traffic on port `25` to prevent spam and reputational harm to IP addresses used by customers. Use port `587` or `465` for encrypted email.
<h3 id="admin-override-codes-expired">Admin override codes expired</h3>
[Admin override codes](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes) are time-sensitive and adhere to fixed-hour blocks. A code generated at 9:30 AM with a 1-hour timeout will expire at 10:00 AM because its validity is counted within the 9:00 AM-10:00 AM window.
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">Diagnostic logs</a> - Learn how to collect logs for support.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/">Known limitations</a> - Review unsupported features and environments.</li>
<li><a href="/cloudflare-one/troubleshooting/">Troubleshooting Cloudflare One</a> - View troubleshooting guides for other products.</li>
</ul>
