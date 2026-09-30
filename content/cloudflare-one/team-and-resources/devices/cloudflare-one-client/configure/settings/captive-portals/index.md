<p>Captive portals are used by public Wi-Fi networks (such as airports, coffee shops, and hotels) to make a user agree to their Terms of Service or provide payment before allowing access to the Internet. When a user connects to the Wi-Fi, the captive portal blocks all HTTPS traffic until the user completes a captive portal login flow in their browser. This prevents the Cloudflare One Client (formerly WARP) from connecting to Cloudflare. At the same time, the Cloudflare One Client creates <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic">firewall rules</a> on the device to send all traffic to Cloudflare. The user is therefore unable to access the captive portal login screen unless they temporarily disconnect the Cloudflare One Client.</p>
<h2 id="allow-users-to-connect-to-captive-portals">Allow users to connect to captive portals</h2>
<p>To allow users to connect through a captive portal, administrators can configure the following device client settings:</p>
<h3 id="no-user-interaction-required">No user interaction required</h3>
<ul>
<li>Enable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#captive-portal-detection">Captive portal detection</a>. This allows the Cloudflare One Client to temporarily disconnect when it detects a captive portal on the network. For more details, refer to <a href="#how-captive-portal-detection-works">how captive portal detection works</a> and its <a href="#limitations">limitations</a>.</li>
<li>Set <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">Device tunnel protocol</a> to <strong>MASQUE</strong>. When using MASQUE, client traffic will look like standard HTTPS traffic and is therefore less likely to be blocked by captive portals.</li>
</ul>
<h3 id="user-interaction-required">User interaction required</h3>
<ul>
<li>Enable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch">Lock device client switch</a> and enable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes">Allow admin override codes</a>. Users can contact the IT administrator for a one-time code that allows them to manually disconnect the Cloudflare One Client and connect to a portal.</li>
<li>For employees who travel, disable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch">Lock device client switch</a> and set an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">Auto connect</a> duration. This allows the user to manually disconnect the Cloudflare One Client without contacting IT.</li>
</ul>
<h2 id="how-captive-portal-detection-works">How captive portal detection works</h2>
<p>If the Cloudflare One Client cannot establish a connection to Cloudflare, it will:</p>
<ol>
<li>
<p>Start the captive portal timer.</p>
</li>
<li>
<p>Send a series of requests to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#captive-portal">Cloudflare captive portal URLs</a> and other OS and browser-specific captive portal URLs. These requests are sent outside of the WARP tunnel.</p>
</li>
<li>
<p>If a request is intercepted, the Cloudflare One Client assumes the network is behind a captive portal and fully opens the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic">system firewall</a>. While the firewall is open, all device traffic will bypass the Cloudflare One Client.</p>
</li>
<li>
<p>Re-enable the firewall after the user successfully connects to the portal or after the timeout period expires.</p>
</li>
</ol>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Due to <a href="#how-captive-portal-detection-works">how captive portal detection works</a>, it may be possible for an employee to spoof a captive portal in order to disconnect the Cloudflare One Client.</li>
<li>Some captive portals, particularly those on airlines, may be slow to respond and exceed the captive portal detection timeout. Users will likely see a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#cf_captive_portal_timed_out">CF_CAPTIVE_PORTAL_TIMED_OUT</a> error when they try to connect. For context on the steps leading up to these errors, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a>.</li>
<li>The Cloudflare One Client may not be able to detect multi-stage captive portals, which redirect the user to different networks during the login process. Users will need to manually disconnect the Cloudflare One Client to get through the captive portal.</li>
<li>Some public Wi-Fi networks are incompatible with running the Cloudflare One Client:
<ul>
<li>Captive portals that intercept all DNS traffic will block the Cloudflare One Client's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#overview">DoH connection</a>. Users will likely see a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#cf_no_network">CF_NO_NETWORK</a> error after they login to the captive portal.</li>
<li>Captive portals that only allow HTTPS traffic will block the Cloudflare One Client's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#overview">Wireguard UDP connection</a>. Users will likely see a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#cf_happy_eyeballs_mitm_failure">CF_HAPPY_EYEBALLS_MITM_FAILURE</a> error after they login to the captive portal.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="check-system-notifications">Check system notifications</h3>
@markup("md", "content/.markup/bodies/6271.md")
</aside>
<h2 id="get-captive-portal-logs">Get captive portal logs <span class="nb-badge">Beta</span></h2>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6272.md")
</div></details>
<p>Captive portal logs are used by Cloudflare Support to troubleshoot Cloudflare One Client captive portal issues. When an end user reports an issue with a captive portal, the IT administrator can ask the user to collect captive portal logs on their device. The administrator can then attach the logs to a Cloudflare Support ticket.</p>
<p>To get captive portal logs:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6275.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="macos-limitation">macOS limitation</h3>
@markup("md", "content/.markup/bodies/6270.md")
</aside>
<p>Once the diagnostic finishes running, the Cloudflare One Client will place a <code>warp-captive-portal-diag-&lt;date&gt;-&lt;time&gt;.zip</code> file on the user's desktop. The end user can now share this file with their IT administrator.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> - Learn about the status messages displayed by the Cloudflare One Client during its connection process, and understand each stage as the client establishes a secure tunnel to Cloudflare.</li>
</ul>
