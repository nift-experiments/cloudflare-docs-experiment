<p>This page lists the error codes that can appear in the Cloudflare One Client (formerly WARP) GUI. If you do not see your error below, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/">common issues</a> or <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshoot-the-cloudflare-one-client">Troubleshoot the Cloudflare One Client</h3>
@markup("md", "content/.markup/bodies/6100.md")
</aside>
<div class="medium-img">
<p><img src="/assets/upstream/images/cloudflare-one/connections/warp-gui-error.png" alt="Example of error message in Cloudflare One Client GUI" /></p>
</div>
<h2 id="cf-captive-portal-timed-out">CF_CAPTIVE_PORTAL_TIMED_OUT</h2>
<h3 id="symptoms">Symptoms</h3>
<ul>
<li>Unable to login to a captive portal network</li>
<li>No Internet connectivity</li>
</ul>
<h3 id="cause">Cause</h3>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#captive-portal-detection">Captive portal detection</a> is turned on and one of the following issues occurred:</p>
<ul>
<li>The user did not complete the captive portal login process within the time limit set by the Cloudflare One Client.</li>
<li>The captive portal redirected the user to a flow that is not yet supported by the captive portal detection feature.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<ol>
<li>Increase the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#captive-portal-detection">captive portal timeout</a> to allow users more time to login.</li>
<li>If this does not resolve the issue, allow users to manually <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch">disconnect</a>. We recommend setting an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">auto connect</a> value so that the client turns itself back on after a few minutes.</li>
</ol>
<h2 id="cf-connectivity-failure-unknown">CF_CONNECTIVITY_FAILURE_UNKNOWN</h2>
<h3 id="symptoms-1">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>No Internet connectivity</li>
<li>User may be behind a captive portal</li>
</ul>
<h3 id="cause-1">Cause</h3>
<p>The initial <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#connectivity-checks">connectivity check</a> failed for an unknown reason. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#unable-to-connect-warp">Unable to connect the Cloudflare One Client</a> for the most common reasons why this error occurs.</p>
<h3 id="resolution-1">Resolution</h3>
<ol>
<li>Retrieve <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">client diagnostic logs</a> for the device.</li>
<li>Follow the troubleshooting steps in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#unable-to-connect-warp">Unable to connect the Cloudflare One Client</a>.</li>
</ol>
<h2 id="cf-dns-lookup-failure">CF_DNS_LOOKUP_FAILURE</h2>
<h3 id="symptoms-2">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>Unable to browse the Internet</li>
<li><code>nslookup</code> and <code>dig</code> commands fail on the device</li>
</ul>
<h3 id="cause-2">Cause</h3>
<p>The Cloudflare One Client was unable to resolve hostnames via its <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">local DNS proxy</a>.</p>
<h3 id="resolution-2">Resolution</h3>
<ol>
<li>Verify that the network the user is on has DNS connectivity.</li>
<li>Verify that DNS resolution works when the Cloudflare One Client is disabled.</li>
<li>Ensure that no third-party tools are interfering with the Cloudflare One Client for control of DNS.</li>
<li>Ensure that no third-party tools are <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#a-third-party-security-product-is-interfering-with-gateway">performing TLS decryption</a> on traffic to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">WARP IP addresses</a>.</li>
</ol>
<h2 id="cf-dns-proxy-failure">CF_DNS_PROXY_FAILURE</h2>
<h3 id="symptoms-3">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client in a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">mode that enables DNS filtering</a>.</li>
</ul>
<h3 id="cause-3">Cause</h3>
<p>A third-party process (usually a third-party DNS software) is bound to port <code>53</code>, which is used by the Cloudflare One Client's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">local DNS proxy</a> to perform DNS resolution. The name of third-party process will appear in the GUI error message.</p>
<p>On macOS, you may see <code>mDNSResponder</code> instead of the specific application name -- <code>mDNSResponder</code> is a macOS system process that handles DNS requests on behalf of other processes. There is no known way to determine which process caused <code>mDNSResponder</code> to bind to port <code>53</code>, but the most common culprits are virtual machine software (for example, Docker and VMware Workstation) and the macOS Internet Sharing feature.</p>
<h3 id="resolution-3">Resolution</h3>
<ol>
<li>Remove or disable DNS interception in the third-party process.</li>
</ol>
<details class="nb-details"><summary>mDNSResponder</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6101.md")
</div></details>
<ol start="2">
<li>Alternatively, switch the Cloudflare One Client to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode">Traffic only mode</a> mode.</li>
</ol>
<h2 id="cf-failed-read-system-dns-config">CF_FAILED_READ_SYSTEM_DNS_CONFIG</h2>
<h3 id="symptoms-4">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>Unable to browse the Internet</li>
</ul>
<h3 id="cause-4">Cause</h3>
<p>The Cloudflare One Client could not read the system DNS configuration, most likely because it contains an invalid nameserver or search domain.</p>
<h3 id="resolution-4">Resolution</h3>
<p>On macOS and Linux, validate that <code>/etc/resolv.conf</code> is <a href="https://man7.org/linux/man-pages/man5/resolv.conf.5.html">formatted correctly</a> and check for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#maclinux-the-devices-etcresolvconf-file-has-an-invalid-character">invalid characters</a>.</p>
<p>On Windows, validate that the registry entry <code>HKLM\System\CurrentControlSet\Services\TCPIP\Parameters\SearchList</code> contains only valid search domains. Examples of invalid entries include IP addresses and domains that start with a period (such as <code>.local</code>).</p>
<h2 id="cf-failed-to-set-mtls">CF_FAILED_TO_SET_MTLS</h2>
<h3 id="symptoms-5">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
</ul>
<h3 id="cause-5">Cause</h3>
<p>The device failed to present a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-mtls-certificate">valid mTLS certificate</a> during device enrollment.</p>
<h3 id="resolution-5">Resolution</h3>
<ol>
<li>Ensure that there are no admin restrictions on certificate installation.</li>
<li>Re-install the client certificate on the device.</li>
</ol>
<h2 id="cf-happy-eyeballs-mitm-failure">CF_HAPPY_EYEBALLS_MITM_FAILURE</h2>
<h3 id="symptoms-6">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
</ul>
<h3 id="cause-6">Cause</h3>
<p>A router, firewall, antivirus software, or other third-party security product is blocking UDP on the WARP ports.</p>
<h3 id="resolution-6">Resolution</h3>
<ol>
<li>Configure the third-party security product to allow the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#warp-ingress-ip">WARP ingress IPs and ports</a>.</li>
<li>Ensure that your Internet router is working properly and try rebooting the router.</li>
<li>Check that the device is not revoked by going to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
</ol>
<h2 id="cf-host-unreachable-check">CF_HOST_UNREACHABLE_CHECK</h2>
<h3 id="symptoms-7">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>No Internet connectivity</li>
<li>User may be behind a captive portal</li>
</ul>
<h3 id="cause-7">Cause</h3>
<p>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#connectivity-checks">connectivity check</a> inside of the WARP tunnel has failed.</p>
<h3 id="resolution-7">Resolution</h3>
<ol>
<li>Check for the presence of third-party HTTP filtering software (AV, DLP, or firewall) that could be intercepting traffic to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall">WARP IPs</a>.</li>
<li>In the third-party software, bypass inspection for all IP traffic going through the Cloudflare One Client. To find out what traffic routes through the WARP tunnel, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a>.</li>
</ol>
<h2 id="cf-insufficient-disk">CF_INSUFFICIENT_DISK</h2>
<h3 id="symptoms-8">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>OS warns that the disk is full</li>
</ul>
<h3 id="cause-8">Cause</h3>
<p>The hard drive is full or has incorrect permissions for the Cloudflare One Client to write data.</p>
<h3 id="resolution-8">Resolution</h3>
<ol>
<li>Ensure that your device meets the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">HD space requirements</a> for the Cloudflare One Client.</li>
<li>Check for disk permissions that may prevent the Cloudflare One Client from using disk space.</li>
<li>Empty trash or remove large files.</li>
</ol>
<h2 id="cf-insufficient-file-descriptors">CF_INSUFFICIENT_FILE_DESCRIPTORS</h2>
<h3 id="symptoms-9">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>Unable to open files on the device</li>
</ul>
<h3 id="cause-9">Cause</h3>
<p>The device does not have sufficient file descriptors to create network sockets or open files.</p>
<h3 id="resolution-9">Resolution</h3>
<p>Increase the file descriptor limit in your system settings.</p>
<h2 id="cf-insufficient-memory">CF_INSUFFICIENT_MEMORY</h2>
<h3 id="symptoms-10">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>Device is very slow</li>
</ul>
<h3 id="cause-10">Cause</h3>
<p>The device does not have enough memory to run the Cloudflare One Client.</p>
<h3 id="resolution-10">Resolution</h3>
<ol>
<li>Ensure that your device meets the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">minimum memory requirements</a> for the Cloudflare One Client.</li>
<li>List all running processes to check memory usage.</li>
</ol>
<h2 id="cf-local-policy-file-failed-to-parse">CF_LOCAL_POLICY_FILE_FAILED_TO_PARSE</h2>
<h3 id="symptoms-11">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
</ul>
<h3 id="cause-11">Cause</h3>
<p>The Cloudflare One Client was deployed on the device using an invalid MDM configuration file.</p>
<h3 id="resolution-11">Resolution</h3>
<ol>
<li>Review the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">managed deployment guide</a> for your operating system.</li>
<li>Locate the MDM configuration file on your device.</li>
<li>Ensure that the file is formatted correctly and only contains <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">accepted arguments</a>.</li>
</ol>
<h2 id="cf-no-network">CF_NO_NETWORK</h2>
<h3 id="symptoms-12">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
<li>No Internet connectivity</li>
</ul>
<h3 id="cause-12">Cause</h3>
<p>The device is not connected to a Wi-Fi network or LAN that has connectivity to the Internet.</p>
<h3 id="resolution-12">Resolution</h3>
<ol>
<li>Launch the network settings panel on your device.</li>
<li>Ensure that you are connected to a valid network.</li>
<li>Check that your device is retrieving a valid IP address.</li>
<li>If this does not resolve the error, try rebooting your device or running your system's network diagnostics tool.</li>
</ol>
<h2 id="cf-registration-missing">CF_REGISTRATION_MISSING</h2>
<h3 id="symptoms-13">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
</ul>
<h3 id="cause-13">Cause</h3>
<p>The device is not authenticated to an <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">organization</a> because:</p>
<ul>
<li>The device was revoked in Zero Trust.</li>
<li>The registration was corrupted or deleted for an unknown reason.</li>
</ul>
<h3 id="resolution-13">Resolution</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6104.md")
</div></div>
<h3 id="cf-registration-missing-revoked">CF_REGISTRATION_MISSING (Revoked)</h3>
<h4 id="cause-14">Cause</h4>
<p>Your device was unenrolled from your company's <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">organization</a> by an administrator on your account.</p>
<h4 id="resolution-14">Resolution</h4>
<p>Contact your company or team administrator for assistance.</p>
<h2 id="cf-tls-interception-blocking-doh">CF_TLS_INTERCEPTION_BLOCKING_DOH</h2>
<h3 id="symptoms-14">Symptoms</h3>
<ul>
<li>DNS requests fail to resolve when the Cloudflare One Client is connected.</li>
</ul>
<h3 id="cause-15">Cause</h3>
<p>A third-party application or service is intercepting DNS over HTTPS traffic from the Cloudflare One Client.</p>
<h3 id="resolution-15">Resolution</h3>
<p>Configure the third-party application to exempt the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#doh-ip">WARP DoH IPs</a>.</p>
<h2 id="cf-tls-interception-check">CF_TLS_INTERCEPTION_CHECK</h2>
<h3 id="symptoms-15">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
</ul>
<h3 id="cause-16">Cause</h3>
<p>A third-party security product on the device or network is performing TLS decryption on HTTPS traffic. For more information, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#a-third-party-security-product-is-interfering-with-gateway">Troubleshooting guide</a>.</p>
<h3 id="resolution-16">Resolution</h3>
<p>In the third-party security product, disable HTTPS inspection and TLS decryption for the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">WARP IP addresses</a>.</p>
<h2 id="admin-directed-disconnect">Admin directed disconnect</h2>
<h3 id="symptoms-16">Symptoms</h3>
<ul>
<li>Unable to connect the Cloudflare One Client</li>
</ul>
<h3 id="cause-17">Cause</h3>
<p>The account administrator has disconnected the Cloudflare One Client for all devices registered to the account.</p>
<h3 id="resolution-17">Resolution</h3>
<p>The account administrator must turn off both of the following features: - <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-the-cloudflare-one-client-on-all-devices">Disconnect the Cloudflare One Client on all devices</a> - <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#manage-device-connection-using-an-external-signal">Manage device connection using an external signal</a></p>
