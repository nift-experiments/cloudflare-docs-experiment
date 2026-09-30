<p>You can scan HTTP traffic for sensitive data through <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a> policies. To enforce <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4906.md")
</div> policies, first configure a **DLP profile** that defines what sensitive data patterns to detect. Then build a **Gateway HTTP policy** that defines what action to take (allow, block, or log) when Gateway finds matching data.
<p>Before creating a policy, use <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection</a> to explore sensitive data in sampled Gateway traffic. Its findings can help you choose which data types and destinations your policy should cover.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4905.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Set up <a href="/cloudflare-one/traffic-policies/get-started/http/">Gateway HTTP filtering</a>. This routes your users' web traffic through Cloudflare Gateway so it can be inspected.
<ul>
<li>HTTP filtering requires turning on the <a href="/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy">Gateway proxy</a> for TCP traffic.</li>
</ul>
</li>
<li>Turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption">TLS decryption</a>. Because most web traffic is encrypted with HTTPS, Gateway must decrypt it before DLP can scan the request body for sensitive data.</li>
</ul>
<h2 id="1-configure-a-dlp-profile"><ol>
<li>Configure a DLP profile</li>
</ol></h2>
<p>A DLP profile defines the sensitive data patterns you want to detect — for example, social security number formats, credit card numbers, or custom patterns specific to your organization. Refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Configure a DLP profile</a>. We recommend getting started with a predefined profile.</p>
<h2 id="2-create-a-dlp-policy"><ol start="2">
<li>Create a DLP policy</li>
</ol></h2>
<p>DLP Profiles may be used alongside other Cloudflare One rules in a <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policy</a>. To start logging or blocking traffic, create a policy for DLP:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>. Select <strong>HTTP</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Build an <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a> using the <a href="/cloudflare-one/traffic-policies/http-policies/#dlp-profile">DLP Profile</a> selector. For example, the following policy blocks users from uploading sensitive data to any location other than an approved corporate application. It combines three conditions: the request content matches a DLP profile, the HTTP method is <code>POST</code>, and the destination is not an approved application:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Social Security, Insurance, Tax, and Identifier Numbers</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>HTTP Method</td>
<td>in</td>
<td><em>POST</em></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Application</td>
<td>not in</td>
<td><em>Workday</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>Gateway now applies the configured action when traffic matches the complete HTTP policy.</p>
<h2 id="3-test-dlp-policy"><ol start="3">
<li>Test DLP policy</li>
</ol></h2>
<p>You can test your DLP policy on any device connected to your <a href="/cloudflare-one/">Zero Trust organization</a>. To perform a basic test:</p>
<ol>
<li>Go to <a href="http://dlptest.com/http-post/">dlptest.com</a>.</li>
<li>Enter a text message or upload a file containing the sensitive data.</li>
<li>Select <strong>Submit</strong> to send the request.</li>
</ol>
<p>The request will be allowed or blocked according to your DLP policies. If the data matches a DLP policy, you will see the request in your <a href="#4-view-dlp-logs">DLP logs</a>.</p>
<p>Different sites will send requests in different ways. For example, some sites will split a file upload into multiple requests. Therefore, even if the policy works on <code>dlptest.com</code>, it is not guaranteed to work the same way on another site or application.</p>
<p>If the request is not blocked as expected, use <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan</a> to confirm that the profile detects your sample content on its own. A profile that matches in a test scan but not in traffic points to the policy, the traffic path, or TLS decryption.</p>
<h2 id="4-view-dlp-logs"><ol start="4">
<li>View DLP logs</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>HTTP request logs</strong>.</li>
<li>Select <strong>Filter</strong>.</li>
<li>Choose an item under one of the following filters:
<ul>
<li><strong>DLP Profiles</strong> shows the requests which matched a specific DLP profile.</li>
<li><strong>Policy</strong> shows the requests which matched a specific DLP policy.</li>
</ul>
</li>
</ol>
<p>You can expand an individual row to view details about the request. By default, logs show that a match occurred but do not include the actual matched content. To see the data that triggered the DLP policy, <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/">configure logging options</a>.</p>
<h3 id="report-false-positives">Report false positives</h3>
<p>If DLP flags a request that does not actually contain sensitive data (a false positive), you can report it to Cloudflare:</p>
<ol>
<li>Select the log you want to report.</li>
<li>Select <strong>Report DLP false positive</strong> under <strong>DLP details</strong>.</li>
<li>The information to be sent to Cloudflare will appear. To confirm your report, select <strong>Send report</strong>.</li>
</ol>
<p>Cloudflare will not respond directly to your report, but reporting false positives helps us improve our products. If you require technical assistance, reach out to <a href="https://dash.cloudflare.com/?to=/:account/support">support</a>.</p>
