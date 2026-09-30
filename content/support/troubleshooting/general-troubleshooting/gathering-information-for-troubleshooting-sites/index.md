<h2 id="about-this-guide">About this guide</h2>
<p>It is important to capture as much information as possible to diagnose an issue and to <a href="/support/contacting-cloudflare-support/">provide adequate details to Cloudflare support</a>. This article explains how to gather troubleshooting information commonly requested by Cloudflare Support.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14721.md")
</aside>
<hr />
<h2 id="quick-reference-choose-the-right-tool">Quick reference: Choose the right tool</h2>
<p>Use this table to quickly identify which troubleshooting method to use based on your issue:</p>
<table>
<thead>
<tr>
<th>Issue Type</th>
<th>Recommended Tool</th>
<th>When to Use</th>
</tr>
</thead>
<tbody>
<tr>
<td>Page not loading correctly</td>
<td><a href="#generate-a-har-file">HAR file</a></td>
<td>Visual issues, broken elements, slow page loads</td>
</tr>
<tr>
<td>JavaScript errors</td>
<td><a href="#export-console-log">Console log</a></td>
<td>CORS errors, scripts failing, browser-side errors</td>
</tr>
<tr>
<td>Protocol errors (QUIC/HTTP2)</td>
<td><a href="#capture-a-netlog-dump">NetLog dump</a></td>
<td><code>ERR_QUIC_PROTOCOL_ERROR</code>, <code>ERR_HTTP2_PROTOCOL_ERROR</code></td>
</tr>
<tr>
<td>Slow response times</td>
<td><a href="#performance">curl (performance)</a></td>
<td>Measuring latency, TLS handshake times</td>
</tr>
<tr>
<td>HTTP errors (5xx, 4xx)</td>
<td><a href="#http-errors">curl (HTTP errors)</a></td>
<td>Determining if errors originate from Cloudflare or origin</td>
</tr>
<tr>
<td>Caching issues</td>
<td><a href="#caching">curl (caching)</a></td>
<td>Cache misses, stale content, cache headers</td>
</tr>
<tr>
<td>SSL/TLS certificate issues</td>
<td><a href="#ssltls-certificates">curl (SSL/TLS)</a></td>
<td>Certificate errors, TLS version issues</td>
</tr>
<tr>
<td>Connection timeouts/drops</td>
<td><a href="#perform-a-traceroute">Traceroute</a> / <a href="#perform-a-mtr">MTR</a></td>
<td>Network path issues, latency between hops</td>
</tr>
<tr>
<td>Packet loss, connection resets</td>
<td><a href="#run-packet-captures">Packet capture</a></td>
<td>Layer 3/4 issues, SSL handshake failures</td>
</tr>
<tr>
<td>Identifying serving location</td>
<td><a href="#identify-the-cloudflare-data-center-serving-your-request">Cloudflare data center</a></td>
<td>Determine which Cloudflare PoP is serving requests</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="browser-based-troubleshooting">Browser-based troubleshooting</h2>
<p>These tools capture information directly from your web browser and are useful for diagnosing issues with how pages load and render.</p>
<h3 id="generate-a-har-file">Generate a HAR file</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use">When to use</h3>
@markup("md", "content/.markup/bodies/14720.md")
</aside>
<p>A HTTP Archive (HAR) records all web browser requests including the request and response headers, the body content, and the page load time. Be sure to use Incognito Mode or a Private Browsing window.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14719.md")
</aside>
<p>Some browsers either require a browser extension or cannot generate a HAR. When installing a browser extension, follow the instructions from the extension provider.</p>
<h4 id="in-chrome">In Chrome</h4>
<ol>
<li>
<p>In a browser page viewed in Incognito Mode, right-click anywhere and select <strong>Inspect Element</strong>.</p>
</li>
<li>
<p>The Chrome DevTools appear either at the bottom, or left side of the browser. Click the <strong>Network</strong> tab.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/support/gathering_har_file_network.png" alt="HAR network tab screenshot from Chrome developer tools" /></p>
<ol start="3">
<li>
<p>Check <strong>Preserve log</strong>. Please also check <strong>Disable cache</strong> if you are reporting a Cloudflare Cache issue.</p>
</li>
<li>
<p>Click record.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/support/gathering_har_file_record.png" alt="HAR record button in chrome dev tools." /></p>
<ol start="5">
<li>Browse to the URL that causes issues. Once the issue is experienced, click the &quot;Export HAR&quot; option at the top of DevTools.</li>
</ol>
<p><img src="/assets/upstream/images/support/export_har_chrome.png" alt="export HAR option in Chrome DevTools" />.</p>
<ol start="6">
<li>Attach the HAR file to your support ticket.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14718.md")
</aside>
<h4 id="in-firefox">In Firefox</h4>
<ol>
<li>
<p>While using a Private Window, use the application menu and select <strong>Tools</strong> &gt; <strong>Web Developer</strong> &gt; <strong>Network</strong> or press <em>Ctrl+Shift+I</em> (Windows/Linux) or <em>Cmd+Option+I</em> (OS X).</p>
</li>
<li>
<p>Browse to the URL that causes issues.</p>
</li>
<li>
<p>After duplicating the issue, right-click and choose <strong>Save All As HAR</strong>.</p>
</li>
</ol>
<h4 id="in-microsoft-edge">In Microsoft Edge</h4>
<ol>
<li>
<p>In a Private window, navigate to <strong>Developer tools</strong> (use <code>F12</code> as a shortcut) and select the <strong>Network</strong> tab.</p>
</li>
<li>
<p>Browse to the URL that causes issues.</p>
</li>
<li>
<p>After duplicating the issue, click on <strong>Export as HAR</strong> followed by <strong>Save As...</strong>.</p>
</li>
</ol>
<h4 id="in-safari">In Safari</h4>
<ol>
<li>
<p>In Safari, ensure a <strong>Develop</strong> menu appears at the top of a Private Window in the browser window. Otherwise, go to <strong>Safari</strong> &gt; <strong>Preferences</strong> &gt; <strong>Advanced</strong> and select <strong>Show Develop Menu in menu bar</strong></p>
</li>
<li>
<p>Navigate to <strong>Develop</strong> &gt; <strong>Show Web Inspector</strong>.</p>
</li>
<li>
<p>Browse to the URL that causes issues.</p>
</li>
<li>
<p>Ctrl + click on a resource within Web Inspector and click <strong>Export HAR</strong>.</p>
</li>
</ol>
<h4 id="in-mobile">In Mobile</h4>
<p><strong>For Android:</strong></p>
<ol>
<li>
<p>Enable USB Debugging mode on your mobile device.</p>
</li>
<li>
<p>Go to <code>chrome://inspect/#devices</code>.</p>
</li>
<li>
<p>If debugging mode is enabled, you will see your device listed below “Remote Target” like the example below:</p>
</li>
</ol>
<p><img src="/assets/upstream/images/support/step_1.jpg" alt="Where to find the Inspect Devices when in Debug Mode for Android." /></p>
<ol start="4">
<li>
<p>Type in the URL, select <strong>Open</strong> and <strong>inspect</strong> to open Chrome’s DevTools.</p>
</li>
<li>
<p>Select the <strong>Network</strong> tab in the DevTools window.</p>
</li>
<li>
<p>Check <strong>Preserve log</strong>. Please also check <strong><em>Disable cache</em></strong> if you are reporting a Cloudflare Cache issue.</p>
</li>
<li>
<p>Click <strong>record</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/support/step_2_-_better.jpg" alt="Where to find the record button in Chrome's dev tools." /></p>
<ol start="8">
<li>Browse to the URL that causes issues. Once the issue is experienced, right-click on any of the items within the <strong>Network</strong> tab and select <strong>Save all as HAR with Content</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/support/step_3.png" alt="How to save HAR content. " /></p>
<ol start="9">
<li>Attach the HAR file to your support ticket alongside a screen recording from the affected Samsung device. Instructions on how to do this from Samsung devices can be found in <a href="https://www.samsung.com/au/support/mobile-devices/screen-recorder/">Samsung's documentation here</a>.</li>
</ol>
<hr />
<p><strong>For iPhone:</strong></p>
<p>Refer to <a href="https://support.okta.com/help/s/article/How-to-generate-a-HAR-capture-on-an-iOS-device?language=en_US">Okta</a> or <a href="https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/GettingStarted/GettingStarted.html#//apple_ref/doc/uid/TP40007874-CH2-SW1">Apple's</a> support article on how to generate a HAR file from an iOS device. Attach the HAR file to your support ticket alongside a screen recording from the affected iOS device. Apple devices now have <a href="https://support.apple.com/en-us/HT207935">built-in screen recording functionality</a>.</p>
<h3 id="export-console-log">Export Console Log</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-1">When to use</h3>
@markup("md", "content/.markup/bodies/14717.md")
</aside>
<p>In certain situations when request is not issued or cancelled by the browser (for example, due to <a href="https://developer.mozilla.org/en-US/docs/Glossary/CORS">CORS</a>), we need to get JS console log output, in addition to the HAR file, to identify the root cause.</p>
<h4 id="in-chrome-1">In Chrome</h4>
<ol>
<li>Go to the <strong>Console</strong> tab from the DevTools bar.</li>
<li>Go to the Console Settings and select <strong>Preserve Log</strong>.</li>
<li>Leave the console open and perform the steps that reproduce the issue.</li>
<li>Right-click on any of the items within the <strong>Console</strong> tab and select <strong>Save as</strong> log file.</li>
<li>Attach the log file to your support ticket.</li>
</ol>
<p><img src="/assets/upstream/images/support/console_snapshot.png" alt="How to find the console tab in Chrome's developer tools." /></p>
<h4 id="in-firefox-1">In Firefox</h4>
<ol>
<li>Go to the <strong>Console</strong> tab from the Web Developer Tools bar.</li>
<li>Go to the Console Settings and select <strong>Persist Log</strong> and <strong>Show Timestamps</strong>.</li>
<li>Leave the console open and perform the steps that reproduce the issue.</li>
<li>Right click, <strong>Select All</strong> messages and <strong>Export Visible Messages to File</strong>.</li>
<li>Attach the log file to your support ticket.</li>
</ol>
<h4 id="in-microsoft-edge-1">In Microsoft Edge</h4>
<ol>
<li>Go to the <strong>Console</strong> tab from the Developer Tools bar.</li>
<li>Go to the Console Settings and select <strong>Preserve Log</strong>.</li>
<li>Leave the console open and perform the steps that reproduce the issue.</li>
<li>Right click on any of the items within the <strong>Console</strong> tab and select <strong>Save as</strong> log file.</li>
<li>Attach the log file to your support ticket.</li>
</ol>
<h4 id="in-safari-1">In Safari</h4>
<ol>
<li>Go to the <strong>Console</strong> tab from the Web Inspector bar.</li>
<li>Tick the box <strong>Preserve Log</strong>.</li>
<li>Leave the console open and perform the steps that reproduce the issue.</li>
<li>Select all the messages, right click and <strong>Save Selected</strong> to a log file.</li>
<li>Attach the log file to your support ticket.</li>
</ol>
<h3 id="capture-a-netlog-dump">Capture a NetLog dump</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-2">When to use</h3>
@markup("md", "content/.markup/bodies/14716.md")
</aside>
<p>In some cases, in order to further troubleshoot issues related to protocols (errors such as <code>ERR_QUIC_PROTOCOL_ERROR</code>, <code>ERR_HTTP2_PROTOCOL_ERROR</code>, etc..) our Support team may ask you to provide a <a href="https://www.chromium.org/for-testers/providing-network-details/">NetLog dump</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14715.md")
</aside>
<ol>
<li>Open a new tab and enter the following depending on the browser you're using:</li>
</ol>
<ul>
<li><code>chrome://net-export</code></li>
<li><code>edge://net-export</code></li>
<li><code>opera://net-export</code></li>
</ul>
<ol start="2">
<li>Click the <strong>Start Logging To Disk</strong> button.</li>
<li>Reproduce the network problem in a different tab.
(the <code>chrome://net-export/</code>, <code>edge://net-export/</code> or <code>opera://net-export</code> tab needs to stay open otherwise logging will automatically stop)</li>
<li>Click <strong>Stop Logging</strong> button.</li>
<li>Attach the log file to your support ticket.</li>
</ol>
<hr />
<h2 id="command-line-troubleshooting">Command-line troubleshooting</h2>
<p>These tools are run from your terminal or command prompt and are useful for testing connectivity, performance, and server responses without browser overhead.</p>
<h3 id="identify-the-cloudflare-data-center-serving-your-request">Identify the Cloudflare data center serving your request</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-3">When to use</h3>
@markup("md", "content/.markup/bodies/14714.md")
</aside>
<p><a href="https://www.cloudflare.com/network-map">A map of our data centers</a> is listed on the <a href="https://www.cloudflarestatus.com/locations">status page locations view</a>, sorted by continent.
The three-letter code in the data center name is the <a href="http://en.wikipedia.org/wiki/IATA_airport_code">IATA code</a> of the nearest major international airport.
Determine the Cloudflare data center serving requests for your browser by visiting:
<code>http://``_www.example.com_``/cdn-cgi/trace.</code></p>
<p>Replace <code>www.example.com</code> with your domain and hostname. Note the <code>colo</code> field from the output.</p>
<h3 id="troubleshoot-requests-with-curl">Troubleshoot requests with curl</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-4">When to use</h3>
@markup("md", "content/.markup/bodies/14713.md")
</aside>
<p><a href="https://curl.se/">curl</a> is a command line tool for sending HTTP/HTTPS requests and is useful for troubleshooting:</p>
<ul>
<li>HTTP/HTTPS Performance</li>
<li>HTTP Error Responses</li>
<li>HTTP Headers</li>
<li>APIs</li>
<li>Comparing Server/Proxy Responses</li>
<li>SSL Certificates</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14712.md")
</aside>
<p>Run the following command to send a standard HTTP GET request to your website (replace <code>www.example.com</code> with your hostname):</p>
<pre><code class="language-bash">curl -svo /dev/null http://www.example.com/&#10;</code></pre>
<p>This example curl command returns output detailing the HTTP response and request headers but discards the page body output. curl output confirms the HTTP response and whether Cloudflare is currently proxying traffic for the site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14711.md")
</aside>
<p>View the sections below for tips on troubleshooting HTTP errors, performance, caching, and SSL/TLS certificates:</p>
<h4 id="http-errors">HTTP errors</h4>
<p>When troubleshooting HTTP errors in responses from Cloudflare, test whether your origin caused the errors by sending requests directly to your origin web server. To troubleshoot HTTP errors, run a curl directly to your origin web server IP address (bypassing Cloudflare’s proxy):</p>
<pre><code class="language-bash">curl -svo /dev/null http://example.com --connect-to ::203.0.113.34&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14710.md")
</aside>
<h4 id="performance">Performance</h4>
<p>curl measures latency or performance degradation for HTTP/HTTPS requests via the <a href="https://curl.haxx.se/docs/manpage.html#-w"><code>-w</code> or <code>--write-out</code> curl option</a>. The example curl below measures several performance vectors in the request transaction such as duration of the TLS handshake, DNS lookup, redirects, transfers, etc:</p>
<pre><code class="language-bash">curl -svo /dev/null https://example.com/ -w &quot;\nContent Type: %{content_type} \&#10;\nHTTP Code: %{http_code} \&#10;\nHTTP Connect:%{http_connect} \&#10;\nNumber Connects: %{num_connects} \&#10;\nNumber Redirects: %{num_redirects} \&#10;\nRedirect URL: %{redirect_url} \&#10;\nSize Download: %{size_download} \&#10;\nSize Upload: %{size_upload} \&#10;\nSSL Verify: %{ssl_verify_result} \&#10;\nTime Handshake: %{time_appconnect} \&#10;\nTime Connect: %{time_connect} \&#10;\nName Lookup Time: %{time_namelookup} \&#10;\nTime Pretransfer: %{time_pretransfer} \&#10;\nTime Redirect: %{time_redirect} \&#10;\nTime Start Transfer: %{time_starttransfer} \&#10;\nTime Total: %{time_total} \&#10;\nEffective URL: %{url_effective}\n&quot; 2&gt;&amp;1&#10;</code></pre>
<p><a href="https://blog.cloudflare.com/a-question-of-timing/">Explanation of this timing output</a> is found on the Cloudflare blog.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14709.md")
</aside>
<h4 id="caching">Caching</h4>
<p>curl helps review the HTTP response headers that influence caching. In particular, review several HTTP headers when troubleshooting Cloudflare caching:</p>
<ul>
<li>CF-Cache-Status</li>
<li>Cache-Control/Pragma</li>
<li>Expires</li>
<li>Last-Modified</li>
<li>s-maxage</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14708.md")
</aside>
<h4 id="ssl-tls-certificates">SSL/TLS certificates</h4>
<h4 id="reviewing-certificates-with-curl">Reviewing Certificates with curl</h4>
<p>The following curl command shows the SSL certificate served by Cloudflare during an HTTPS request (replace <code>www.example.com</code> with your hostname):</p>
<pre><code class="language-sh">curl -svo /dev/null https://www.example.com/ 2&gt;&amp;1 | egrep -v &quot;^{.*$|^}.*$|^* http.*$&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14707.md")
</aside>
<p>To display the origin certificate (assuming one is installed), replace <code>203.0.113.34</code> below with the actual IP address of your origin web server and replace <code>www.example.com</code> with your domain and hostname:</p>
<pre><code class="language-sh">curl -svo /dev/null https://www.example.com --connect-to ::203.0.113.34 2&gt;&amp;1 | egrep -v &quot;^{.*$|^}.*$|^* http.*$&quot;&#10;</code></pre>
<h4 id="testing-tls-versions">Testing TLS Versions</h4>
<p>If troubleshooting browser support or confirming what TLS versions are supported, curl allows you to test a specific TLS version by adding the <a href="https://curl.se/docs/manpage.html#--tlsv10">--tlsv1.X</a> and <a href="https://curl.se/docs/manpage.html#--tls-max">--tls-max</a> options to your curl:</p>
<ul>
<li><code>--tlsv1.0 --tls-max 1.0</code></li>
<li><code>--tlsv1.1 --tls-max 1.1</code></li>
<li><code>--tlsv1.2 --tls-max 1.2</code></li>
<li><code>--tlsv1.3 --tls-max 1.3</code></li>
</ul>
<h3 id="temporarily-pause-cloudflare">Temporarily pause Cloudflare</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-5">When to use</h3>
@markup("md", "content/.markup/bodies/14706.md")
</aside>
<p>For more details, refer to <a href="/fundamentals/manage-domains/pause-cloudflare/">Pause Cloudflare</a>.</p>
<hr />
<h2 id="network-troubleshooting">Network troubleshooting</h2>
<p>These tools help diagnose network-level issues such as routing problems, packet loss, and connection failures between your location and Cloudflare or your origin server.</p>
<h3 id="perform-a-traceroute">Perform a traceroute</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-6">When to use</h3>
@markup("md", "content/.markup/bodies/14705.md")
</aside>
<p>Traceroute is a network diagnostic tool that measures the route latency of packets across a network. Most operating systems support the <code>traceroute</code> command. If you experience connectivity issues with your Cloudflare-proxied website and <a href="/support/contacting-cloudflare-support/">ask Cloudflare Support for assistance</a>, ensure to provide output from a traceroute.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14704.md")
</aside>
<p>Review the instructions below for running traceroute on different operating systems. Replace <code>www.example.com</code> with your domain and hostname in the examples below:</p>
<h4 id="run-traceroute-on-windows">Run traceroute on Windows</h4>
<ol>
<li>
<p>Open the <strong>Start</strong> menu.</p>
</li>
<li>
<p>Click <strong>Run</strong>.</p>
</li>
<li>
<p>To open the command line interface, type <strong>cmd</strong> and then click <strong>OK</strong>.</p>
</li>
<li>
<p>At the command line prompt, type:</p>
</li>
</ol>
<p>For IPv4 -</p>
<pre><code class="language-sh">tracert www.example.com&#10;</code></pre>
<p>For IPv6 -</p>
<pre><code class="language-sh">tracert -6 www.example.com&#10;</code></pre>
<ol start="5">
<li>
<p>Press <strong>Enter</strong>.</p>
</li>
<li>
<p>You can copy the results to save in a file or paste in another program.</p>
</li>
</ol>
<h4 id="run-traceroute-on-linux">Run traceroute on Linux</h4>
<ol>
<li>
<p>Open a terminal window.</p>
</li>
<li>
<p>At the command line prompt, type:</p>
</li>
</ol>
<p>For IPv4 -</p>
<pre><code class="language-sh">traceroute www.example.com&#10;</code></pre>
<p>For IPv6 -</p>
<pre><code class="language-sh">traceroute -6 www.example.com&#10;</code></pre>
<ol start="3">
<li>You can copy the results to save in a file or paste in another program.</li>
</ol>
<h4 id="run-traceroute-on-mac-os">Run traceroute on Mac OS</h4>
<ol>
<li>Open the <strong>Network Utility</strong> application.</li>
<li>Click the <strong>Traceroute</strong> tab.</li>
<li>Type the <em>domain</em> or <em>IP address</em> in the appropriate input field and press <strong>Trace</strong>.</li>
<li>You can copy the results to save in a file or paste in another program.</li>
</ol>
<p>Alternatively, follow the same Linux traceroute instructions above when using the Mac OS terminal program.</p>
<h3 id="add-the-cf-ray-header-to-your-logs">Add the CF-RAY header to your logs</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-7">When to use</h3>
@markup("md", "content/.markup/bodies/14703.md")
</aside>
<p>The <strong>CF-RAY</strong> header traces a website request through Cloudflare's network. Provide the <strong>CF-RAY</strong> of a web request to Cloudflare support when troubleshooting an issue. You can also add <strong>CF-RAY</strong> to your logs by editing your origin web server configuration with the snippet below that corresponds to your brand of web server:</p>
<h4 id="for-apache-web-servers-add-cf-ray-i-to-logformat">For Apache web servers, add <code>%{CF-Ray}i</code> to LogFormat</h4>
<pre><code>LogFormat &quot;%h %l %u %t \&quot;%r\&quot; %&gt;s %b \&quot;%{Referer}i\&quot; \&quot;%{User-agent}i\&quot; %{CF-Ray}i&quot; cf_custom&#10;</code></pre>
<h4 id="for-nginx-web-servers-add-http-cf-ray-to-log-format">For Nginx web servers, add '$http_cf_ray' to log_format</h4>
<pre><code>log_format cf_custom &#x27;$remote_addr - $remote_user [$time_local] &#x27;&#10;&#x27;&quot;$request&quot; $status $body_bytes_sent &#x27;&#10;&#x27;&quot;$http_referer&quot; &quot;$http_user_agent&quot; &#x27;&#10;&#x27;$http_cf_ray&#x27;;&#10;</code></pre>
<h3 id="perform-a-mtr">Perform a MTR</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-8">When to use</h3>
@markup("md", "content/.markup/bodies/14702.md")
</aside>
<p>My Traceroute (MTR) is a <a href="https://www.cloudflare.com/learning/network-layer/what-is-mtr/">tool</a> that combines traceroute and ping to measure a network path's health, which is another common method for testing network connectivity and speed. In addition to the hops along the network path, MTR shows constantly updating information about the latency and packet loss along the route to the destination. This helps in troubleshooting network issues by allowing you to see what's happening along the path in real-time.</p>
<p>MTR works by discovering the network path in a similar manner to traceroute, and then regularly sending packets to continue collecting information to provide an updated view into the network’s health and speed.</p>
<p>Like traceroute, MTR can use ICMP or UDP for outgoing packets but relies on ICMP for return (Type 11: Time Exceeded) packets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14701.md")
</aside>
<h4 id="how-do-i-use-mtr-to-generate-network-path-report">How do I use MTR to generate network path report?</h4>
<p><strong>Using MTR on NIX based machines</strong></p>
<p>Generally, we'd use MTR as the following:</p>
<pre><code class="language-sh">mtr -rw &lt;dest_hostname&gt; e.g.: mtr -rw one.one.one.one&#10;</code></pre>
<p>or with destination IP:</p>
<pre><code class="language-sh">mtr -rw &lt;dest_IP&gt; e.g.: mtr -rw 1.1.1.1&#10;</code></pre>
<p>with TCP port</p>
<pre><code class="language-sh">mtr -P &lt;tcp port&gt; -T &lt;destination ip&gt;&#10;</code></pre>
<p>Please refer to this documentation, which explains more about analysing MTR: <a href="https://www.cloudflare.com/en-gb/learning/network-layer/what-is-mtr/">How to read MTR</a>.</p>
<h3 id="run-packet-captures">Run Packet Captures</h3>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="when-to-use-9">When to use</h3>
@markup("md", "content/.markup/bodies/14700.md")
</aside>
<p>Issues that happen at the layers 3/4 occur before requests reaching Cloudflare's logging system, so they do not show up in the HTTP logs. Therefore, troubleshooting issues related to connection resets, packet loss or SSL handshake failures can be tricky without a deep investigation at the packet level.</p>
<p>Some HTTP errors generated by Cloudflare, such as <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520s</a>, <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524s</a> and <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/">525s</a>, show underlying issues at layers 3/4, and might require a packet capture for further investigation.</p>
<p><strong>How to Run a Packet Capture</strong></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14699.md")
</aside>
<p>Cloudflare suggests <a href="https://www.wireshark.org/download.html">Wireshark</a> for running packet captures. For instructions on how to use the <em>tcpdump</em> command line, refer to <a href="https://www.wireshark.org/docs/wsug_html_chunked/AppToolstcpdump.html">this</a> article.</p>
<ol>
<li>Close all programs/browser tabs that could be sending data in the background to avoid having to use a lot of display filters later.</li>
<li>Create your Wireshark capture filter (refer to <a href="https://wiki.wireshark.org/CaptureFilters">this</a> article for more information).</li>
<li>Select the appropriate interface (e.g. Wi-Fi: en0). If you're not sure which interface to use, Wireshark provides an I/O graph of each interface to give you a hint.</li>
<li>Click the blue shark fin icon in the top left-hand corner to start your packet capture.</li>
<li>Reproduce the issue while running capture.</li>
<li>Click the red square icon in the top left-hand corner to stop your packet capture.</li>
<li>Save as a <code>.pcap</code> file and attach it to your support ticket.</li>
</ol>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/support/contacting-cloudflare-support/">Contacting Cloudflare Support</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare HTTP 5XX errors</a></li>
<li><a href="https://www.cloudflare.com/en-gb/learning/network-layer/what-is-mtr/">Diagnosing network issues with MTR and traceroute</a></li>
<li><a href="https://curl.haxx.se/">cURL command line tool</a></li>
</ul>
