<p>This tutorial explains how to analyze <a href="https://www.cloudflare.com/products/cloudflare-logs/">Cloudflare Logs</a> using the <a href="https://splunkbase.splunk.com/app/4501/">Cloudflare App for Splunk</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before sending your Cloudflare log data to Splunk, ensure that you:</p>
<ul>
<li>Have an existing Splunk Enterprise or Cloud account</li>
<li>Have a Cloudflare Enterprise account</li>
<li>Consult the <a href="https://splunkbase.splunk.com/app/4501/">Splunk documentation</a> for the Cloudflare App</li>
</ul>
<h2 id="task-1-install-and-configure-the-cloudflare-app-for-splunk">Task 1 - Install and Configure the Cloudflare App for Splunk</h2>
<p>To install the <a href="https://splunkbase.splunk.com/app/4501/">Cloudflare App for Splunk</a>:</p>
<ol>
<li>Log in to your Splunk instance.</li>
<li>Under <strong>Apps</strong> &gt; <strong>Find More Apps</strong>, search for <em>Cloudflare App for Splunk.</em></li>
<li>Click <strong>Install</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/splunk/screenshots/splunk-cloudflare-app-for-splunk.png" alt="Splunk website with Apps menu expanded and Search &amp; Reporting menu item along with Cloudflare App for Splunk" /></p>
<ol start="4">
<li>
<p>Restart and reopen your Splunk instance.</p>
</li>
<li>
<p>Edit the <code>cloudflare:json</code> source type in the Cloudflare App for Splunk. To edit the source type:</p>
<ol>
<li>Click the <strong>Settings</strong> dropdown and select <strong>Source types</strong>.</li>
<li>Uncheck <strong>Show only popular</strong> and search for <em>cloudflare</em>.</li>
<li>Click <strong>Edit</strong> and change the Regex expression to <code>([\r\n]+)</code>.</li>
<li>Save your edits.</li>
</ol>
</li>
<li>
<p>Create an index on Splunk to store the HTTP Event logs. To create an index:</p>
<ol>
<li>Open the setup screen by clicking the <strong>Settings</strong> dropdown, then click <strong>Indexes</strong>.</li>
<li>Select <strong>New Index</strong>. Note that the <strong>Indexes</strong> page also gives you the status of all your existing indexes so that you can see whether you're about to use up your licensed amount of space.</li>
<li>Name the index <strong>cloudflare</strong>, which is the default index that the Cloudflare App will use.</li>
<li>Set <strong>Index Data Type</strong> to <strong>Events</strong>, then select <strong>Save</strong>.</li>
</ol>
</li>
<li>
<p>Set up the HTTP Event Collector (HEC) on Splunk. To create an HEC:</p>
<ol>
<li>Click the <strong>Settings</strong> dropdown and select <strong>Data inputs</strong>.</li>
<li>Select <strong>+Add new</strong> next to <strong>HTTP Event Collector</strong> and follow the wizard. When prompted, submit the following responses:
<ul>
<li>Name: Cloudflare</li>
<li>Source Type: Select &gt; <code>cloudflare:json</code></li>
<li>App Context: Cloudflare App for Splunk (cloudflare)</li>
<li>Index: cloudflare</li>
</ul>
</li>
<li>At the end of the wizard you will see a <strong>Token Value</strong>. This token authorizes the Cloudflare Logpush job to send data to your Splunk instance. If you forget to copy it now, Splunk allows you to get the value at any time.</li>
</ol>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enable-hec-and-ssl">Enable HEC and SSL</h3>
@markup("md", "content/.markup/bodies/3151.md")
</aside>
<ol start="8">
<li>
<p>Verify whether Splunk is using a self-signed certificate. You'll need this information when creating the Logpush job.</p>
</li>
<li>
<p>Determine the endpoint to use to send the data to. The endpoint should be:</p>
</li>
</ol>
<pre><code class="language-sql">&quot;&lt;protocol&gt;://input-&lt;host&gt;:&lt;port&gt;/&lt;endpoint&gt;&quot; or &quot;&lt;protocol&gt;://http-inputs-&lt;host&gt;:&lt;port&gt;/&lt;endpoint&gt;&quot;&#10;</code></pre>
<p>Where:</p>
<ul>
<li><code>protocol</code>: HTTP or HTTPS</li>
<li><code>input</code>: <code>input</code> or <code>http-inputs</code> based on whether you have a self-service or managed cloud plan</li>
<li><code>host</code>: The hostname of your Splunk instance. The easiest way to determine the hostname is to look at the URL you went to when you logged in to Splunk.</li>
<li><code>port</code>: 443 or 8088</li>
<li><code>endpoint</code>: services/collector/raw</li>
</ul>
<p>For example: <code>https://prd-p-0qk3h.splunkcloud.com:8088/services/collector/raw</code>. Refer to the <a href="https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/UsetheHTTPEventCollector">Splunk Documentation</a> for more details and examples.</p>
<p><strong>Post Installation Notes</strong></p>
<p>You can change the <strong>Index Name</strong> after the initial configuration by clicking on the <strong>Settings</strong> dropdown and navigating to <strong>Advanced search</strong>. There you can select <strong>Search macros</strong> and look for the Cloudflare App for Splunk.</p>
<p><img src="/assets/upstream/images/fundamentals/splunk/screenshots/splunk-settings-advanced-search-search-macros.png" alt="Splunk interface highlighting Apps menu and Manage Apps option along with Enable Acceleration checkbox" /></p>
<p>The Cloudflare App for Splunk comes with a custom Cloudflare Data Model that has an acceleration time frame of 1 day but is not accelerated by default. If you enable <a href="https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/Acceleratedatamodels">Data Model acceleration</a>, we recommend that the Data Model is only accelerated for 1 or 7 days to ensure there are no adverse effects within your Splunk environment.</p>
<p>Enable or disable acceleration after the initial configuration by accessing the app Set up page by clicking the <strong>Apps</strong> dropdown, then <strong>Manage Apps</strong> &gt; <strong>Cloudflare Set Up</strong>.</p>
<p><img src="/assets/upstream/images/fundamentals/splunk/screenshots/splunk-apps-manage-apps-cloudflare-set-up-enable-data-model-acceleration.png" alt="Splunk Advanced Search page highlighted Search macros and Advanced search" /></p>
<p>You can also manually configure Data Models by going to <strong>Settings</strong> &gt; <strong>Data models</strong>. Learn more about data model acceleration in the <a href="https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/Acceleratedatamodels">Splunk documentation</a>.</p>
<h2 id="task-2-create-the-cloudflare-logpush-job-to-splunk">Task 2 - create the Cloudflare Logpush job to Splunk</h2>
<p>Create the Logpush job by following <a href="/logs/logpush/logpush-job/enable-destinations/splunk/">Enable Logpush to Splunk</a>. When you fill in the Splunk destination:</p>
<ul>
<li>Use the endpoint you configured in <a href="#task-1---install-and-configure-the-cloudflare-app-for-splunk">Task 1</a> for <strong>Splunk HEC URL</strong>, including the <code>/services/collector/raw</code> path.</li>
<li>Use the HEC token you created in <a href="#task-1---install-and-configure-the-cloudflare-app-for-splunk">Task 1</a> for <strong>Auth Token</strong>, prefixed with <code>Splunk</code> (for example, <code>Splunk 12345678-1234-1234-1234-1234567890ab</code>).</li>
<li>Set <strong>Source Type</strong> to the value that matches the dataset you want to push, so the Cloudflare App for Splunk parses events correctly:
<ul>
<li>HTTP requests, Firewall events, Spectrum events, and most zone-scoped datasets: <code>cloudflare:json</code></li>
<li>DNS logs, including Zero Trust Gateway DNS: <code>cloudflare:dns</code></li>
<li>Audit logs: <code>cloudflare:audit</code></li>
<li>Access requests: <code>cloudflare:access</code></li>
<li>CASB findings: <code>cloudflare:casb</code></li>
<li>Zero Trust Gateway HTTP: <code>cloudflare:http</code></li>
<li>Zero Trust Gateway Network: <code>cloudflare:network</code></li>
</ul>
</li>
<li>Only turn on <strong>Use insecure skip verify option</strong> if your Splunk instance uses a self-signed certificate, as noted in <a href="#task-1---install-and-configure-the-cloudflare-app-for-splunk">Task 1</a>.</li>
</ul>
<p>Under <strong>Send the following fields</strong>, keep the defaults or refer to the <a href="#task-3---view-the-dashboards">Dashboard section</a> to select the fields required to fully populate the Cloudflare App for Splunk dashboards.</p>
<p>After you create the job, enable it to start sending logs. To confirm end-to-end delivery, run the following search in Splunk:</p>
<pre><code class="language-txt">index=&quot;cloudflare&quot;&#10;</code></pre>
<p>Cloudflare sends two system confirmation events to verify connectivity and delivery setup as soon as you enable the job. Regular Cloudflare logs start streaming shortly afterward. Data can take a few minutes to appear.</p>
<h2 id="task-3-view-the-dashboards">Task 3 - View the Dashboards</h2>
<p>You can analyze Cloudflare logs with the thirteen (13) dashboards listed below.</p>
<p>You can use filters within these dashboards to help narrow the analysis by date and time, device type, country, user agent, client IP, hostname, and more to further help with debugging and tracing.</p>
<h3 id="about-the-dashboards">About the Dashboards</h3>
<p>The following dashboards outlined below are available as part of the Cloudflare App for Splunk.</p>
<h4 id="cloudflare-snapshot">Cloudflare - Snapshot</h4>
<p><em>Web Traffic Overview</em> and <em>Web Traffic Types</em>: Get an overview of the most important metrics from your websites and applications on the Cloudflare network.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-snapshot-dashboard.png" alt="Splunk dashboard with Web Traffic Overview metrics" /></p>
<h4 id="cloudflare-reliability">Cloudflare - Reliability</h4>
<p><em>Summary</em> and <em>Detailed</em>: Get insights on the availability of your websites and applications. Metrics include origin response error ratio, origin response status over time, percentage of 3xx/4xx/5xx errors over time, and more.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-reliability-summary-dashboard.png" alt="Splunk dashboard with a high level summary of Reliability metrics" /></p>
<p><img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-reliability-detailed-dashboard.png" alt="Splunk dashboard with a detailed summary of Reliability metrics" /></p>
<h4 id="cloudflare-security">Cloudflare - Security</h4>
<p><em>Overview</em>: Get insights on threats to your websites and applications, including number of threats stopped, threats over time, top threat countries, and more.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-security-overview.png" alt="Splunk dashboard with an overview of Security metrics" /></p>
<p><em>WAF</em>: Get insights on threat identification and mitigation by our Web Application Firewall, including events like SQL injections, XSS, and more. Use this data to fine tune the firewall to target obvious threats and prevent false positives.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-security-waf-dashboard.png" alt="Splunk dashboard with an overview of Security metrics for WAF" /></p>
<p><em>Rate Limiting</em>: Get insights on rate limiting protection against denial-of-service attacks, brute-force login attempts, and other types of abusive behavior targeted at your websites or applications.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-security-rate-limiting-dashboard.png" alt="Splunk dashboard with an overview of Security metrics for Rate Limiting" /></p>
<p><em>Bots Summary</em> and <em>Bots Detailed</em>: Investigate bot activity on your website to prevent content scraping, checkout fraud, spam registration and other malicious activities.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-security-bot-summary-dashboard.png" alt="Splunk dashboard with a high level summary of Security metrics for Bots" /></p>
<p><img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-security-bots-detailed-dashboard.png" alt="Splunk dashboard with a detailed summary of Security metrics for Bots" /></p>
<h4 id="cloudflare-performance">Cloudflare - Performance</h4>
<p><em>Requests and Cache</em> and <em>Bandwidth</em>: Identify and address performance issues and caching misconfigurations. Metrics include total vs. cached bandwidth, saved bandwidth, total requests, cache ratio, top uncached requests, and more.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-performance-requests-and-cache-dashboard.png" alt="Splunk dashboard with Performance metrics for Requests and Cache" /></p>
<p><img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-performance-bandwidth-dashboard.png" alt="Splunk dashboard with Performance metrics for Bandwidth" /></p>
<p><em>Hostname, Content Type, Request Methods, Connection Type</em>: Get insights into your most popular hostnames, most requested content types, breakdown of request methods, and connection type.</p>
<p><img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-performance-hostname-dashboard.png" alt="Splunk dashboard with Cloudflare Performance metrics including for Hostname, Content Type, Request Methods, Connection Type" /></p>
<p><em>Static vs. Dynamic Content</em>: Get insights into the performance of your static and dynamic content, including slowest URLs.
<img src="/assets/upstream/images/fundamentals/splunk/dashboards/splunk-cloudflare-performance-static-vs-dynamic-dashboard.png" alt="Splunk dashboard with Cloudflare Performance metrics for Static vs. Dynamic Content" /></p>
<h3 id="filters">Filters</h3>
<p>All dashboard have a set of filters that you can apply to the entire dashboard, as shown in the following example. Filters are applied across the entire dashboard.</p>
<p><img src="/assets/upstream/images/fundamentals/splunk/screenshots/splunk-filters.png" alt="Available dashboard filters from the Splunk dashboard" /></p>
<p>You can use filters to drill down and examine the data at a granular level. Filters include client country, client device type, client IP, client request host, client request URI, client request user agent, edge response status, origin IP, and origin response status.</p>
<p>The default time interval is set to 24 hours. Note that for correct calculations filter will need to exclude Worker subrequests (<strong>WorkerSubrequest</strong> = <em>false</em>) and purge requests (<strong>ClientRequestMethod</strong> is not <em>PURGE</em>).</p>
<p>Available Filters:</p>
<ul>
<li>
<p>Time Range (EdgeStartTimestamp)</p>
</li>
<li>
<p>Client Country</p>
</li>
<li>
<p>Client Device type</p>
</li>
<li>
<p>Client IP</p>
</li>
<li>
<p>Client Request Host</p>
</li>
<li>
<p>Client Request URI</p>
</li>
<li>
<p>Client Request User Agent</p>
</li>
<li>
<p>Edge response status</p>
</li>
<li>
<p>Origin IP</p>
</li>
<li>
<p>Origin Response Status</p>
</li>
<li>
<p>RayID</p>
</li>
<li>
<p>Worker Subrequest</p>
</li>
<li>
<p>Client Request Method</p>
</li>
</ul>
<h2 id="splunk-cim-field-mappings">Splunk CIM field mappings</h2>
<p>The Cloudflare App for Splunk maps Cloudflare log fields to <a href="https://docs.splunk.com/Documentation/CIM/latest/User/Overview">Splunk Common Information Model (CIM)</a> field names, so that you can search, correlate, and accelerate Cloudflare data alongside other CIM-compliant sources in your Splunk deployment. The following tables list the mappings the app applies per Cloudflare Logpush dataset.</p>
<h3 id="http-requests">HTTP requests</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ClientIP</code></td>
<td><code>src_ip</code></td>
</tr>
<tr>
<td><code>ClientRequestBytes</code></td>
<td><code>bytes_in</code></td>
</tr>
<tr>
<td><code>ClientRequestHost</code></td>
<td><code>dest_host</code></td>
</tr>
<tr>
<td><code>ClientRequestMethod</code></td>
<td><code>http_method</code></td>
</tr>
<tr>
<td><code>ClientRequestPath</code></td>
<td><code>uri_path</code></td>
</tr>
<tr>
<td><code>ClientRequestReferer</code></td>
<td><code>http_referrer</code></td>
</tr>
<tr>
<td><code>ClientRequestURI</code></td>
<td><code>uri</code></td>
</tr>
<tr>
<td><code>ClientRequestUserAgent</code></td>
<td><code>http_user_agent</code></td>
</tr>
<tr>
<td><code>ClientSrcPort</code></td>
<td><code>src_port</code></td>
</tr>
<tr>
<td><code>ClientSSLProtocol</code></td>
<td><code>ssl_protocol</code></td>
</tr>
<tr>
<td><code>EdgeRateLimitAction</code></td>
<td><code>action</code></td>
</tr>
<tr>
<td><code>EdgeResponseBytes</code></td>
<td><code>bytes_out</code></td>
</tr>
<tr>
<td><code>EdgeResponseContentType</code></td>
<td><code>http_content_type</code></td>
</tr>
<tr>
<td><code>EdgeResponseStatus</code></td>
<td><code>status</code></td>
</tr>
<tr>
<td><code>OriginIP</code></td>
<td><code>dest_ip</code></td>
</tr>
<tr>
<td><code>OriginResponseTime</code></td>
<td><code>response_time</code></td>
</tr>
</tbody>
</table>
<h3 id="casb-findings">CASB findings</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AssetDisplayName</code></td>
<td><code>dest</code></td>
</tr>
<tr>
<td><code>AssetLink</code></td>
<td><code>url</code></td>
</tr>
<tr>
<td><code>FindingTypeDisplayName</code></td>
<td><code>category</code></td>
</tr>
<tr>
<td><code>FindingTypeID</code></td>
<td><code>category_id</code></td>
</tr>
<tr>
<td><code>FindingTypeSeverity</code></td>
<td><code>severity</code></td>
</tr>
<tr>
<td><code>InstanceID</code></td>
<td><code>signature_id</code></td>
</tr>
</tbody>
</table>
<h3 id="zero-trust-gateway-dns">Zero Trust Gateway DNS</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DstIP</code></td>
<td><code>dest</code></td>
</tr>
<tr>
<td><code>DstPort</code></td>
<td><code>dest_port</code></td>
</tr>
<tr>
<td><code>Protocol</code></td>
<td><code>transport</code></td>
</tr>
<tr>
<td><code>QueryName</code></td>
<td><code>query</code></td>
</tr>
<tr>
<td><code>QueryTypeName</code></td>
<td><code>query_type</code></td>
</tr>
<tr>
<td><code>RCode</code></td>
<td><code>reply_code</code></td>
</tr>
<tr>
<td><code>SrcIP</code></td>
<td><code>src</code></td>
</tr>
<tr>
<td><code>SrcPort</code></td>
<td><code>src_port</code></td>
</tr>
</tbody>
</table>
<h3 id="audit-logs">Audit logs</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ActionResult</code></td>
<td><code>status</code></td>
</tr>
<tr>
<td><code>ActionType</code></td>
<td><code>action</code></td>
</tr>
<tr>
<td><code>ActorID</code></td>
<td><code>user</code></td>
</tr>
<tr>
<td><code>ActorIP</code></td>
<td><code>src</code></td>
</tr>
<tr>
<td><code>ActorType</code></td>
<td><code>user_category</code></td>
</tr>
<tr>
<td><code>OwnerID</code></td>
<td><code>src_user</code></td>
</tr>
</tbody>
</table>
<h3 id="access-requests">Access requests</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Action</code></td>
<td><code>action</code></td>
</tr>
<tr>
<td><code>AppDomain</code></td>
<td><code>app</code></td>
</tr>
<tr>
<td><code>Connection</code></td>
<td><code>authentication_service</code></td>
</tr>
<tr>
<td><code>IPAddress</code></td>
<td><code>src</code></td>
</tr>
<tr>
<td><code>PurposeJustificationResponse</code></td>
<td><code>reason</code></td>
</tr>
<tr>
<td><code>RayID</code></td>
<td><code>signature_id</code></td>
</tr>
<tr>
<td><code>UserUID</code></td>
<td><code>user_id</code></td>
</tr>
</tbody>
</table>
<h3 id="zero-trust-gateway-http">Zero Trust Gateway HTTP</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Action</code></td>
<td><code>action</code></td>
</tr>
<tr>
<td><code>DestinationIP</code></td>
<td><code>dest</code></td>
</tr>
<tr>
<td><code>DestinationPort</code></td>
<td><code>dest_port</code></td>
</tr>
<tr>
<td><code>HTTPMethod</code></td>
<td><code>http_method</code></td>
</tr>
<tr>
<td><code>Referer</code></td>
<td><code>http_referrer</code></td>
</tr>
<tr>
<td><code>SourceIP</code></td>
<td><code>src</code></td>
</tr>
<tr>
<td><code>URL</code></td>
<td><code>url</code></td>
</tr>
<tr>
<td><code>UserAgent</code></td>
<td><code>http_user_agent</code></td>
</tr>
<tr>
<td><code>UserID</code></td>
<td><code>user</code></td>
</tr>
</tbody>
</table>
<h3 id="zero-trust-gateway-network">Zero Trust Gateway Network</h3>
<p>The app applies the following mappings:</p>
<table>
<thead>
<tr>
<th>Cloudflare field</th>
<th>Splunk CIM field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Action</code></td>
<td><code>action</code></td>
</tr>
<tr>
<td><code>DestinationIP</code></td>
<td><code>dest_ip</code></td>
</tr>
<tr>
<td><code>DestinationPort</code></td>
<td><code>dest_port</code></td>
</tr>
<tr>
<td><code>DeviceName</code></td>
<td><code>dvc</code></td>
</tr>
<tr>
<td><code>OverrideIP</code></td>
<td><code>dest_translated_ip</code></td>
</tr>
<tr>
<td><code>OverridePort</code></td>
<td><code>dest_translated_port</code></td>
</tr>
<tr>
<td><code>PolicyID</code></td>
<td><code>rule</code></td>
</tr>
<tr>
<td><code>SessionID</code></td>
<td><code>session_id</code></td>
</tr>
<tr>
<td><code>SourceIP</code></td>
<td><code>src_ip</code></td>
</tr>
<tr>
<td><code>SourcePort</code></td>
<td><code>src_port</code></td>
</tr>
<tr>
<td><code>Transport</code></td>
<td><code>transport</code></td>
</tr>
<tr>
<td><code>UserID</code></td>
<td><code>user</code></td>
</tr>
</tbody>
</table>
<h2 id="debugging-tips">Debugging tips</h2>
<h3 id="incomplete-dashboards">Incomplete dashboards</h3>
<p>The Splunk Cloudflare App relies on data from the Cloudflare Enterprise Logs fields outlined below. Depending on which fields you have enabled, certain dashboards might not populate fully.</p>
<p>If that is the case, verify and test the Cloudflare App filters below each dashboard (these filters are the same across all dashboards). You can delete any filters that you do not need, even if such filters include data fields already contained in your logs.</p>
<p>Also, you could compare the list of fields you are getting in Cloudflare Logs with the fields listed in <strong>Splunk</strong> &gt; <strong>Settings</strong> &gt; <strong>Data Model</strong> &gt; <strong>Cloudflare</strong>.</p>
<p>The available fields are:</p>
<ul>
<li>
<p>CacheCacheStatus</p>
</li>
<li>
<p>CacheResponseBytes</p>
</li>
<li>
<p>CacheResponseStatus (deprecated)</p>
</li>
<li>
<p>ClientASN</p>
</li>
<li>
<p>ClientCountry</p>
</li>
<li>
<p>ClientDeviceType</p>
</li>
<li>
<p>ClientIP</p>
</li>
<li>
<p>ClientIPClass</p>
</li>
<li>
<p>ClientRequestBytes</p>
</li>
<li>
<p>ClientRequestHost</p>
</li>
<li>
<p>ClientRequestMethod</p>
</li>
<li>
<p>ClientRequestPath</p>
</li>
<li>
<p>ClientRequestProtocol</p>
</li>
<li>
<p>ClientRequestReferer</p>
</li>
<li>
<p>ClientRequestURI</p>
</li>
<li>
<p>ClientRequestUserAgent</p>
</li>
<li>
<p>ClientSSLCipher</p>
</li>
<li>
<p>ClientSSLProtocol</p>
</li>
<li>
<p>ClientSrcPort</p>
</li>
<li>
<p>EdgeColoCode</p>
</li>
<li>
<p>EdgeColoID</p>
</li>
<li>
<p>EdgeEndTimestamp</p>
</li>
<li>
<p>EdgePathingOp</p>
</li>
<li>
<p>EdgePathingSrc</p>
</li>
<li>
<p>EdgePathingStatus</p>
</li>
<li>
<p>EdgeRequestHost</p>
</li>
<li>
<p>EdgeResponseBytes</p>
</li>
<li>
<p>EdgeResponseContentType</p>
</li>
<li>
<p>EdgeResponseStatus</p>
</li>
<li>
<p>EdgeServerIP</p>
</li>
<li>
<p>EdgeStartTimestamp</p>
</li>
<li>
<p>OriginIP</p>
</li>
<li>
<p>OriginResponseStatus</p>
</li>
<li>
<p>OriginResponseTime</p>
</li>
<li>
<p>OriginSSLProtocol</p>
</li>
<li>
<p>RayID</p>
</li>
<li>
<p>SecurityAction</p>
</li>
<li>
<p>SecurityActions</p>
</li>
<li>
<p>SecurityRuleDescription</p>
</li>
<li>
<p>SecurityRuleID</p>
</li>
<li>
<p>SecurityRuleIDs</p>
</li>
<li>
<p>SecuritySources</p>
</li>
<li>
<p>WAFFlags</p>
</li>
<li>
<p>WAFMatchedVar</p>
</li>
<li>
<p>WorkerSubrequest</p>
</li>
<li>
<p>ZoneID</p>
</li>
</ul>
