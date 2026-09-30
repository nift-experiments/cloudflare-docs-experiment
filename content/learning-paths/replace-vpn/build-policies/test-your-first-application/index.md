<p>You have now set up your <a href="/learning-paths/replace-vpn/get-started/">Zero Trust organization</a>, <a href="/learning-paths/replace-vpn/configure-device-agent/">configured the Cloudflare One Client</a>, <a href="/learning-paths/replace-vpn/connect-devices/">installed it on devices</a>, and created your <a href="/learning-paths/replace-vpn/build-policies/">Access and Gateway policies</a>. The next step is to test those policies.</p>
<h2 id="1-manually-test-your-policies"><ol>
<li>Manually test your policies</li>
</ol></h2>
<p>Test if the Access or Gateway policy that you configured is working by using a device with the Cloudflare One Client installed to reach an internal application or external website.</p>
<p>If you cannot reach an application protected by Access or an external application through Gateway as expected, Cloudflare recommends starting with reviewing your Cloudflare One Client configuration.</p>
<h3 id="1-1-troubleshoot-the-cloudflare-one-client">1.1. Troubleshoot the Cloudflare One Client</h3>
<p>If your manual test fails, troubleshoot the Cloudflare One Client. Cloudflare recommends starting with reviewing your Cloudflare One Client configuration because misconfiguration is the most common cause of connectivity issues.</p>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/">WARP troubleshooting guide</a>: Step-by-step instructions to debug Cloudflare One Client issues.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/">Cloudflare One Client errors</a>: If you are receiving an error, review the associated solutions.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Cloudflare One Client connectivity status</a>: Review the connectivity stage of the WARP daemon as it establishes a connection from the device to Cloudflare.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">WARP with Firewall</a>: Ensure you have exempted the correct IP addresses and domains to allow the Cloudflare One Client to connect.</li>
</ul>
<h3 id="1-2-review-analytics">1.2. Review analytics</h3>
<p>Analytics provide visualizations of <a href="/learning-paths/replace-vpn/build-policies/test-your-first-application/#review-logs">log data</a>. To review Access or Gateway analytics:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Analytics</strong> &gt; <strong>Dashboards</strong>.</li>
<li>Select <strong><a href="/cloudflare-one/insights/analytics/access/">Access event analytics</a></strong> for a summary of login events or <strong><a href="/cloudflare-one/insights/analytics/application-access/">Application Access Report</a></strong> for a summary of overall Access Activity.</li>
<li>Select the <strong>HTTP request analytics</strong>, <strong>DNS query analytics</strong> or <strong>Network session analytics</strong> depending on <a href="/cloudflare-one/insights/analytics/gateway/">your Gateway investigation scope</a>.</li>
</ol>
<h3 id="1-3-review-logs">1.3. Review logs</h3>
<p><a href="/cloudflare-one/insights/logs/">Logs</a> provide event-level (such as an authentication attempt or a DNS query) visibility into your Cloudflare One environment.</p>
<p>To review traffic activity for applications protected by Access:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong>.</li>
<li>Select <strong>Access authentication logs</strong>.</li>
<li>Review the <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#per-request-logs">per-request logs</a> for your application.</li>
</ol>
<p>To review traffic activity in the <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway logs</a>:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong>.</li>
<li>Select <strong>HTTP request logs</strong>, <strong>Network logs</strong>, or <strong>DNS query logs</strong> depending on your investigation scope.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/traffic-policies/troubleshoot-gateway/">Troubleshoot Gateway</a> to troubleshoot common issues with Gateway egress policies.</p>
<h2 id="2-monitor-your-policies-and-device-connectivity"><ol start="2">
<li>Monitor your policies and device connectivity</li>
</ol></h2>
<p>After you confirm your policies work by testing manually, use DEX to monitor connectivity and performance over time.</p>
<p>Digital Experience Monitoring (DEX) provides visibility into device, network, and application performance across your Zero Trust organization.</p>
<p>With DEX, you can monitor the state of your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> deployment and resolve issues impacting end-user productivity. DEX is designed for IT and security teams who need to proactively monitor and troubleshoot device and network health across distributed environments. DEX is available on all Cloudflare Zero Trust and SASE plans.</p>
<p>Refer to <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for more information.</p>
<h3 id="example-use-case">Example use case</h3>
<ul>
<li>Imagine that you have three devices, with the Cloudflare One Client installed, set up in your testing environment.</li>
<li>You have set up a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> for your internal wiki that is available at <code>wiki.acme.org</code>.</li>
<li>You <a href="/learning-paths/replace-vpn/build-policies/test-your-first-application/#manually-test-your-policies">manually tested</a> the three Cloudflare One Client devices, and you confirmed they can all reach <code>wiki.acme.org</code>.</li>
<li>You want to set up automated connectivity and performance testing to <code>wiki.acme.org</code> for each of these Cloudflare One Client devices so you can monitor them over time.</li>
<li>You set up a DEX test, and it sends an HTTP GET request to <code>wiki.acme.org</code> from all three devices on a five minute interval.</li>
<li>If device connectivity drops, or if there are performance problems, you can see the DEX test results to troubleshoot the problem.</li>
</ul>
<h3 id="2-1-create-a-dex-test">2.1. Create a DEX test</h3>
<p>With Digital Experience Monitoring (DEX), you can test if your devices can connect to a private or public endpoint through the Cloudflare One Client. Tests allow you to monitor availability for a given application and investigate performance issues reported by your end users.</p>
<p>Refer to <a href="/cloudflare-one/insights/dex/tests/">DEX tests</a> for more information.</p>
<p>An HTTP test sends a <code>GET</code> request from an end-user device to a specific web application. You can use the response metrics to troubleshoot connectivity issues. For example, you can check whether the application is inaccessible for all users in your organization, or only certain ones.</p>
<p>To set up an HTTP test for an application:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select <strong>Add a Test</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Name</strong>: Enter any name for the test.</li>
<li><strong>Target</strong>: Enter the URL of the website or application that you want to test (for example, <code>https://jira.site.com</code>). Both public and private hostnames are supported. If testing a private hostname, ensure that the domain is on your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> list.</li>
<li><strong>Source device profiles</strong>: (Optional) Select the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a> that you want to run the test on. If no profiles are selected, the test will run on all supported devices connected to your Zero Trust organization.</li>
<li><strong>Test type</strong>: Select <em>HTTP Get</em>.</li>
<li><strong>Test frequency</strong>: Specify how often the test will run. Input a minute value between 5 and 60.</li>
</ul>
</li>
<li>Select <strong>Add test</strong>.</li>
<li>After the test is created and running, you can <a href="/cloudflare-one/insights/dex/tests/view-results/">view the results</a> of your test.</li>
</ol>
<h4 id="http-test-results">HTTP test results</h4>
<p>An HTTP test measures the following data:</p>
<table>
<thead>
<tr>
<th>Data</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Resource fetch time</td>
<td>Total time of all steps of the request, measured from <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Resource_timing"><code>startTime</code> to <code>responseEnd</code></a>.</td>
</tr>
<tr>
<td>Server response time</td>
<td>Round-trip time for the device to receive a response from the target.</td>
</tr>
<tr>
<td>DNS response time</td>
<td>Round-trip time for the DNS query to resolve.</td>
</tr>
<tr>
<td>HTTP status codes</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status">Status code</a> returned by the target.</td>
</tr>
</tbody>
</table>
<h3 id="2-2-set-up-notifications">2.2. Set up notifications</h3>
<p>Administrators can receive alerts when Cloudflare detects connectivity issues with the Cloudflare One Client or degraded application performance. Notifications can be delivered via email, webhook, and third-party services.</p>
<p>Refer to <a href="/cloudflare-one/insights/dex/notifications/">DEX Notifications</a> for more information on DEX-specific notifications.</p>
<h4 id="device-anomaly-notification-setup">Device anomaly notification setup</h4>
<p>Customers who want to be notified when Cloudflare detects a spike or drop in the number of devices connected to the Cloudflare One Client can create a <a href="/cloudflare-one/insights/dex/notifications/#available-notifications">Device connectivity anomaly</a> notification.</p>
<p>To create a device connectivity anomaly notification:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Add**.
3. Find **Product** DEX and **Alert type** Device connectivity anomaly, and choose **Select**.
4. Name the notification.
5. Enter an email address to receive the notifications or set up a [webhook](/notifications/get-started/configure-webhooks/).
6. (Optional) Specify any additional options for the notification, if required. For example, some notifications require that you select one or more domains or services.
7. Select **Create**.
<p>Refer to <a href="/notifications/get-started/">Notifications</a> for more information on editing, testing, and disabling notifications.</p>
<h2 id="conclusion">Conclusion</h2>
<p>Once your policies are live, you can use <a href="/learning-paths/replace-vpn/build-policies/test-your-first-application/#create-a-dex-test">DEX tests</a> and <a href="/learning-paths/replace-vpn/build-policies/test-your-first-application/#notifications">notifications</a> to ensure your team has secure, reliable access to internal and external resources.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="how-it-all-works-together">How it all works together</h3>
@markup("md", "content/.markup/bodies/9962.md")
</aside>
