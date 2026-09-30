<p>Use the results of a Digital Experience Monitoring (DEX) test to monitor availability and performance for a specific application. DEX stores test results for 7 days on all plans, according to the <a href="/cloudflare-one/insights/logs/#log-retention">log retention policy</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>At least one <a href="/cloudflare-one/insights/dex/tests/">test</a> has been created under <strong>DEX</strong> &gt; <strong>Tests</strong>.</li>
<li>Admins must have at least the <a href="/cloudflare-one/roles-permissions/#zero-trust-roles">Cloudflare Zero Trust Reporting role</a>.</li>
</ul>
<h2 id="view-results-for-all-devices">View results for all devices</h2>
<p>To view an overview of test results for all devices:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select a test to view detailed results.</li>
</ol>
<h2 id="view-results-for-an-individual-device">View results for an individual device</h2>
<p>To view analytics on a per-device level:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select the device you want to view, and then select <strong>View details</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select a test to view detailed results.</li>
</ol>
<h2 id="export-dex-application-test-logs">Export DEX application test logs</h2>
<p>You can use <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> to export <a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX application test</a> data to <a href="/r2/">R2</a> (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the <a href="/cloudflare-one/insights/logs/#log-retention">7-day log retention period</a> or correlate DEX data with other log sources.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/insights/dex/tests/http/">DEX HTTP test</a> - Send a <code>GET</code> request from enrolled devices to a web application and measure response times.</li>
<li><a href="/cloudflare-one/insights/dex/tests/traceroute/">DEX Traceroute test</a> - Map the network route between a device and a server, showing each hop along the path.</li>
<li><a href="/cloudflare-one/insights/dex/rules/">DEX rules</a> - Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.</li>
</ul>
