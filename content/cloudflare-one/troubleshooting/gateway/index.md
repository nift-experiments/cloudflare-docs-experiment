<p>This guide helps you troubleshoot common issues with Cloudflare Gateway policies.</p>
<h2 id="blocked-websites-and-connectivity">Blocked websites and connectivity</h2>
<h3 id="a-website-is-blocked-incorrectly">A website is blocked incorrectly</h3>
If you believe a domain has been incorrectly blocked by Gateway's security categories or threat intelligence, you can use the [Cloudflare Radar categorization feedback form](https://radar.cloudflare.com/categorization-feedback/) to request a review.
<h3 id="error-526-invalid-ssl-certificate">Error 526: Invalid SSL certificate</h3>
Gateway presents a **526** error page when it cannot establish a secure connection to the origin. This typically occurs in two cases:
<ul>
<li><strong>Untrusted origin certificate</strong>: The certificate presented by the origin server is expired, revoked, or issued by an unknown authority.</li>
<li><strong>Insecure origin connection</strong>: The origin does not support modern cipher suites or redirects all HTTPS requests to HTTP.</li>
</ul>
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/">Error 526</a>.</p>
<h3 id="error-502-bad-gateway">Error 502: Bad Gateway</h3>
This issue can occur when communicating with an origin that partially supports HTTP/2. If the origin requests a downgrade to HTTP/1.1 (for example, via a `RST_STREAM` frame with `HTTP_1_1_REQUIRED`), Gateway will not automatically reissue the request over HTTP/1.1 and will instead return a `502 Bad Gateway`. To resolve this, disable HTTP/2 at the origin server.
<h3 id="untrusted-certificate-warnings">Untrusted certificate warnings</h3>
If users see certificate warnings for every page, ensure that the [Cloudflare root certificate](/cloudflare-one/team-and-resources/devices/user-side-certificates/) is installed and trusted on their devices. This is required for Gateway to inspect HTTPS traffic.
<h2 id="dashboard-and-analytics">Dashboard and analytics</h2>
<h3 id="gateway-analytics-not-displayed">Gateway analytics not displayed</h3>
If you do not see analytics on the Gateway Overview page:
<ul>
<li><strong>Verify DNS traffic</strong>: Ensure your devices are actually sending queries to Gateway. Check your <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a> and verify the source IPv4 address.</li>
<li><strong>Check other resolvers</strong>: Ensure that no other DNS resolvers are configured on the device, as they might be bypassing Gateway.</li>
<li><strong>Wait for processing</strong>: It can take up to 5 minutes for analytics to appear in the dashboard.</li>
</ul>
<h2 id="egress-policies">Egress policies</h2>
<p>Egress policies symptoms include traffic not using your dedicated egress IP, incorrect failover behavior, or high latency due to Gateway routing traffic through a distant data center.</p>
<h3 id="symptom-traffic-is-not-using-your-dedicated-egress-ip">Symptom: traffic is not using your dedicated egress IP</h3>
<p>Even with an active egress policy, you may find that traffic is egressing from a default Cloudflare IP address instead of your dedicated egress IP.</p>
<table>
<thead>
<tr>
<th>Common cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS resolution to an initial resolved IP</td>
<td>When an egress policy uses a <em>Domain</em> or <em>Host</em> selector, Gateway must first resolve that domain to an <a href="/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips">initial resolved IP</a>. If your account still uses a legacy range within CGNAT (carrier-grade NAT) address space, this IP may be treated as internal to Cloudflare's network and may not be subject to egress policies, which apply to traffic leaving the network. Change the selector in your egress policy from <em>Domain</em> or <em>Host</em> to <em>Destination IP</em> (using the public IP addresses of the service you are trying to reach), or <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">move your initial resolved IP range off CGNAT</a>.</td>
</tr>
<tr>
<td>Policy precedence</td>
<td>A different egress policy with a higher precedence (a lower number) is matching the traffic first. Remember that egress policies follow the same first-match-wins logic.</td>
</tr>
<tr>
<td>Split Tunnel configuration</td>
<td>The destination IP or domain is excluded from the WARP tunnel via your Split Tunnel configuration. Traffic that is excluded from the tunnel will not be subject to any Gateway policies, including egress.</td>
</tr>
<tr>
<td>No egress logs</td>
<td>Egress logging is available via Logpush with the Gateway Egress dataset. This is essential for troubleshooting. You can also use a third-party IP check service to verify the egress IP from a test device.</td>
</tr>
</tbody>
</table>
<h3 id="symptom-failover-is-not-working-or-is-using-the-wrong-ip">Symptom: failover is not working or is using the wrong IP</h3>
<p>Your primary dedicated egress IP becomes unavailable, but instead of using your configured secondary dedicated IP, traffic fails over to a default Cloudflare shared IP.</p>
<table>
<thead>
<tr>
<th>Common cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Routing or configuration issue on the Cloudflare side</td>
<td>Document the time of the incident and collect Request IDs from Gateway HTTP or DNS logs for affected users. Open a support ticket and provide this information. Temporarily, you can edit the egress policy to set your secondary IP as the primary to restore service.</td>
</tr>
</tbody>
</table>
<h3 id="symptom-users-are-egressing-from-a-geographically-distant-location">Symptom: users are egressing from a geographically distant location</h3>
<p>Gateway routes your users in one country (such as Australia) through a dedicated egress IP located in another region (such as Germany), causing high latency and breaking access to geo-restricted content.</p>
<table>
<thead>
<tr>
<th>Common cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single egress policy</td>
<td>You may have one broad egress policy that applies to all users regardless of their location. Create location-aware egress policies. Use the <em>User Location</em> selector in your policy to tie specific user locations to their nearest dedicated egress IP. For example, create one policy for when <em>User Location</em> is <code>United Kingdom</code>, egress via London IP; create a second policy for when <em>User Location</em> is <code>Australia</code>, egress via Sydney IP.</td>
</tr>
<tr>
<td>Incorrect geolocation data</td>
<td>The IP address of the user's ISP may not be correctly geolocated. Check the user's location as seen by Cloudflare in the Gateway logs. If it appears incorrect, you can report it to Cloudflare Support.</td>
</tr>
</tbody>
</table>
<h2 id="policy-precedence">Policy precedence</h2>
<p>A common point of confusion is how Gateway evaluates its different policy types and the rules within them.</p>
<h3 id="symptom-a-block-policy-is-overriding-a-more-specific-allow-or-do-not-scan-policy">Symptom: a Block policy is overriding a more specific Allow or Do Not Scan policy</h3>
<p>You have a high-precedence Allow or Do Not Scan policy for a specific application (such as Allow finance.example.com), but Gateway still block traffic with a low-precedence Block policy (such as Block All High-Risk Sites).</p>
<p>The most important concept is <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway policy precedence</a>, which Gateway enforces based on the policy's order number. A lower order number in the list means a higher precedence. Gateway stops processing further policies when it encounters the first rule that matches.</p>
<p>To resolve Gateway policy precedence issues:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Review the order of your DNS, Network, and HTTP policies.</li>
<li>Ensure that your most specific Allow, Do Not Scan, or Do Not Inspect policies have a lower order number than your general Block policies.</li>
<li>Drag and drop policies to reorder them as needed. An Allow policy for <code>teams.microsoft.com</code> should be placed before a general Block policy for all file sharing applications.</li>
</ol>
<h2 id="tls-decryption-breaks-applications">TLS decryption breaks applications</h2>
<p>Turning on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> is required for Gateway features such as Data Loss Prevention (DLP), Browser Isolation, and application-aware HTTP policies. However, it can cause issues with certain types of software.</p>
<h3 id="symptom-command-line-tools-cli-tools-or-native-applications-fail-with-certificate-errors">Symptom: command-line tools (CLI tools) or native applications fail with certificate errors</h3>
<p>If after turning on TLS decryption, command-line tools (such as <code>git</code>, <code>aws</code>, <code>kubectl</code>, and <code>terraform</code>) or desktop applications (such as ChatGPT or Docker) stop working, this may be due to certificate errors. Applications may return errors such as <code>SSL: CERTIFICATE_VERIFY_FAILED</code>, <code>self-signed certificate in certificate chain</code>, or similar TLS errors.</p>
<p>These applications do not use the operating system's trust store and therefore do not trust the Cloudflare root certificate that you installed. They often have their own certificate trust store or use certificate pinning, which expects the server's original certificate, not one re-signed by Cloudflare.</p>
<p>To resolve this issue:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4365.md")
</div></div>
<h3 id="symptom-the-custom-block-page-is-not-displayed">Symptom: the custom block page is not displayed</h3>
<p>When an HTTP policy blocks a user's request, their browser will return a generic error (<code>ERR_SSL_PROTOCOL_ERROR</code>) instead of your configured Gateway block page.</p>
<p>This happens because the browser does not trust the certificate presented by the block page, which is signed by the Cloudflare root certificate. This means the certificate is not installed or not trusted on the user's device.</p>
<p>To resolve this issue:</p>
<ol>
<li>Confirm that a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Cloudflare root certificate</a> is installed on the device.</li>
<li>Ensure the certificate is placed in the correct system-level trust store (such as, Keychain's System store on macOS, or Trusted Root Certification Authorities for the Local Computer on Windows).</li>
<li>If you are using an MDM, verify that your deployment script correctly installs and trusts the certificate.</li>
</ol>
<h2 id="private-dns-and-internal-resources-are-not-working">Private DNS and internal resources are not working</h2>
<p>You have configured Gateway to resolve internal hostnames, but users are unable to access them. For example, a user connected to the Cloudflare One Client tries to access an internal service like <code>jira.mycompany.local</code>, but the DNS query fails.</p>
<table>
<thead>
<tr>
<th>Common causes</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Missing or incorrect resolver policy</td>
<td>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>. Create a policy that matches your internal domain suffix and forwards queries to your internal DNS servers' IP addresses.</td>
</tr>
<tr>
<td>Split Tunnel excludes the private IP range</td>
<td>If your internal resources are in a private IP range (such as <code>10.0.0.0/8</code>), that range must be included in the tunnel. If it is in the Exclude list of your Split Tunnel configuration, the Cloudflare One Client will not proxy the traffic.</td>
</tr>
<tr>
<td>Local Domain Fallback misconfiguration</td>
<td>Use resolver policies for corporate DNS. Only use Local Domain Fallback for domains specific to a user's immediate physical network.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="more-gateway-resources">More Gateway resources</h2>
<p>For more information, refer to the full Gateway troubleshooting guide.</p>
<p><a class="nb-link-button" href="/cloudflare-one/traffic-policies/troubleshooting/">Full Gateway troubleshooting guide ❯</a></p>
