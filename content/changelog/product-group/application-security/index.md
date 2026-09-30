<h1 id="changelog">Changelog</h1>

<h2 id="waf-release-2026-09-15"><a href="/changelog/post/2026-09-15-waf-release/">WAF Release - 2026-09-15</a></h2>
<p><em>2026-09-15</em></p>
<p>This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b2170b7b1a2c4b8eba0b498eca453d31">ca453d31</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 3</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="02c818297e6d42aaa55e67f5e540f17f">e540f17f</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID:{" "}<code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="93793848937f4f988f1dfdabba458b4b">ba458b4b</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 10</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>


<h2 id="waf-release-scheduled-changes-for-2026-09-22"><a href="/changelog/post/scheduled-waf-release/">WAF Release - Scheduled changes for 2026-09-22</a></h2>
<p><em>2026-09-15</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Announcement Date</th>
<th>Release Date</th>
<th>Release Behavior</th>
<th>Legacy Rule ID</th>
<th>Rule ID</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="40b93de7a8f848709c4ec3e60f0313d6">0f0313d6</code>
</td>
<td>SSRF - Block jar HTTP loopback payload</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="ca05d6c847834f75a317c33b5f21b651">5f21b651</code>
</td>
<td>SSRF - Cloud,Link-Local non-standard IP notation</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="48dfa3e5bef84063914edfe175cd912a">75cd912a</code>
</td>
<td>SSRF - Local non-standard IP notation</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="cd1de1fd21c443508f9073f2a1ba83f6">a1ba83f6</code>
</td>
<td>SSTI - Jinja Dangerous Globals Chain</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-09-10-emergency"><a href="/changelog/post/2026-09-10-emergency-waf-release/">WAF Release - 2026-09-10 - Emergency</a></h2>
<p><em>2026-09-10</em></p>
<p>This update provides immediate defense against a high-severity, actively exploited zero-day vulnerability targeting Adobe Commerce and Magento Open Source storefronts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Adobe Commerce and Magento RCE (CVE-2026-75650 / &quot;StyleSmuggler&quot;): Unauthenticated Remote Code Execution (RCE) vulnerability caused by improper neutralization of special elements in the platform's template engine. Unauthenticated attackers can inject arbitrary PHP payloads through style properties to execute system commands and deploy persistent malware.</li>
</ul>
<p><strong>Impact</strong></p>
<p>This emergency rule provides immediate edge-level mitigation and virtual patching, origin applications must be urgently updated. We strongly recommend to apply the hotfix outlined in Adobe Security Bulletin <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146">APSB26-146</a> and immediately rotate all potentially exposed encryption keys, integration tokens, and system credentials, as patching alone does not remediate an existing compromise.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f9a3026b0fdc4d63b7338346440f5c55">440f5c55</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2026-75650</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-09-08"><a href="/changelog/post/2026-09-08-waf-release/">WAF Release - 2026-09-08</a></h2>
<p><em>2026-09-08</em></p>
<p>This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d5d9f863e50b416faf43934dc76ba662">c76ba662</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID:{" "}<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="771ac3761dcd485cb0e91ea0208457cf">208457cf</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID:{" "}<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>).</td>
</tr>
</tbody>
</table>


<h2 id="create-multiple-cloudflare-tunnel-and-cloudflare-mesh-routes-at-once"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>


<h2 id="waf-release-2026-09-01"><a href="/changelog/post/2026-09-01-waf-release/">WAF Release - 2026-09-01</a></h2>
<p><em>2026-09-01</em></p>
<p>This release introduces a new threat detection to enhance protection against SQL injection (SQLi) attempts exploiting complex query syntax.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>SQLi Protection: Improved coverage for SQL injection patterns involving WHERE comparisons combined with WITH clauses.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d2d75b2f0614405f9fab0354bcfa0966">bcfa0966</code>
</td>
<td>N/A</td>
<td>SQLi - WHERE Comparison With WITH Clause</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-08-26-emergency"><a href="/changelog/post/2026-08-26-emergency-waf-release/">WAF Release - 2026-08-26 - Emergency</a></h2>
<p><em>2026-08-26</em></p>
<p>This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution.</p>
</li>
<li>
<p>GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Next.js recommends updating to version 16.3.3 or 15.5.24 to address these vulnerabilities.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="symmetric-key-support-for-jwt-validation"><a href="/changelog/post/2026-08-25-symmetric-jwt-validation/">Symmetric key support for JWT validation</a></h2>
<p><em>2026-08-25</em></p>
<p>API Shield <a href="/api-shield/security/jwt-validation/">JSON Web Token validation</a> now supports symmetric keys that use the <code>HS256</code>, <code>HS384</code>, and <code>HS512</code> algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.</p>
<p>Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.</p>
<p>Refer to <a href="/api-shield/security/jwt-validation/api/#credentials">Configure JWT validation via the API</a> for supported key formats and credential requirements.</p>


<h2 id="waf-release-2026-08-25"><a href="/changelog/post/2026-08-25-waf-release/">WAF Release - 2026-08-25</a></h2>
<p><em>2026-08-25</em></p>
<p>This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Four new detections move from Log to Block: HTTP/2 Request Smuggling - Request Body Anomaly and XSS - JavaScript Event Handler Coercion across Headers, Body, and URI.</p>
</li>
<li>
<p>The XSS, HTML Injection - Script Tag - Beta rule is merged into the original rule.</p>
</li>
<li>
<p>A Generic Rules - Remote Code Execution detection is added in Block mode.</p>
</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a80f214f0947435dabb2ba2d1489d892">1489d892</code>
</td>
<td>N/A</td>
<td>HTTP/2 Request Smuggling - Request Body Anomaly</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58a184412d2b4113bca6379b20646260">20646260</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e79cb939d6aa41db984e6db3d706d517">d706d517</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - Body</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7e3249c7a5d8469697478746660886c8">660886c8</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d34bc5db8cbc4e18a44ed115c293b926">c293b926</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Script Tag - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "XSS, HTML Injection - Script Tag" (ID:{" "}<code class="nb-rule-id" title="9c8dda9708cc4452ac76e7be7b58420b">7b58420b</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Remote Code Execution</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="leaked-credentials-detection-now-scans-authorization-headers"><a href="/changelog/post/2026-08-20-leaked-credentials-authorization-header/">Leaked credentials detection now scans Authorization headers</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> now scans the <code>Authorization</code> request header for Basic Authentication credentials. Previously, the detection only inspected request bodies, query strings, and headers for well-known web applications or custom detection locations, which meant credentials sent through HTTP Basic Authentication were not covered by default.</p>
<p>This new default scan location decodes the <code>Authorization: Basic &lt;credentials&gt;</code> header and compares the extracted username and password against Cloudflare's database of leaked credentials, the same way as other default scan locations. Matches populate the existing <a href="/waf/detections/leaked-credentials/#leaked-credentials-fields">leaked credentials fields</a>, such as <code>cf.waf.credential_check.password_leaked</code>, and trigger the <a href="/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header"><code>Exposed-Credential-Check</code> managed transform header</a> if configured, so you can reuse existing <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> without changes.</p>
<p>This change was applied automatically for zones with leaked credentials detection enabled. No configuration changes are required.</p>
<p>For more information, refer to <a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a>.</p>


<h2 id="configure-origin-application-settings-for-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/">Configure origin application settings for Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-18</em></p>
<p>You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a <a href="/tunnel/">Cloudflare Tunnel</a>. These settings control how <code>cloudflared</code> connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-origin-settings-dashboard.gif" alt="Configure origin application settings in the Cloudflare dashboard" /></p>
<p>When editing a published application, expand <strong>Additional application settings</strong> to configure parameters organized into three categories:</p>
<ul>
<li><strong>HTTP</strong> — Set a custom HTTP Host header or disable chunked encoding.</li>
<li><strong>TLS</strong> — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.</li>
<li><strong>Connection</strong> — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For the full list of origin parameters, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>


<h2 id="waf-release-2026-08-17"><a href="/changelog/post/2026-08-17-waf-release/">WAF Release - 2026-08-17</a></h2>
<p><em>2026-08-17</em></p>
<p>This release updates WordPress remote code execution rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify CVE-2026-65640.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-65640: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.</li>
</ul>
<p><strong>Impact</strong></p>
<p>The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-65640</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-65640</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="oracle-cloud-infrastructure-object-storage-support-in-cloud-connector"><a href="/changelog/post/2026-08-13-oci-object-storage-cloud-connector/">Oracle Cloud Infrastructure Object Storage support in Cloud Connector</a></h2>
<p><em>2026-08-13</em></p>
<p>Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.</p>
<p>OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional <code>oraclecloud.com</code> and dedicated <code>customer-oci.com</code> path-style endpoints.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-08-13-oci-object-storage-cloud-connector-public-buckets-only">Public buckets only</h4>
@markup("md", "content/.markup/bodies/17751.md")</aside>
<h4 id="2026-08-13-oci-object-storage-cloud-connector-api-example">API example</h4>
<p>Set <code>provider</code> to <code>oci_storage</code> and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:</p>
<pre><code class="language-json">{&#10;	&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/assets/*\&quot;&quot;,&#10;	&quot;provider&quot;: &quot;oci_storage&quot;,&#10;	&quot;description&quot;: &quot;Route assets to OCI Object Storage&quot;,&#10;	&quot;enabled&quot;: true,&#10;	&quot;parameters&quot;: {&#10;		&quot;host&quot;: &quot;&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For endpoint formats and bucket requirements, refer to <a href="/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage">Supported cloud providers in Cloud Connector</a>.</p>


<h2 id="certificate-transparency-monitoring-is-now-generally-available"><a href="/changelog/post/2026-08-13-ct-monitoring-ga/">Certificate Transparency Monitoring is now Generally Available</a></h2>
<p><em>2026-08-13</em></p>
<p>Certificate Transparency Monitoring is now <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">generally available</a> across all Cloudflare plans.</p>
<p>Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.</p>
<p>Learn more in the <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">launch blog post</a> or the <a href="/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">CT Monitoring docs</a>.</p>


<h2 id="hostname-routing-is-now-generally-available-with-a-new-public-ip-range-for-initial-resolved-ips"><a href="/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/">Hostname routing is now generally available, with a new public IP range for initial resolved IPs</a></h2>
<p><em>2026-08-11</em></p>
<p><a href="https://blog.cloudflare.com/tunnel-hostname-routing/">Hostname routing</a> is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong>: route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> (for example, <code>wiki.internal.local</code>) to a private application behind your tunnel, or a <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> (for example, <code>bank.example.com</code>) to egress through a specific tunnel and anchor traffic to a dedicated exit node.</li>
<li><strong>Cloudflare Mesh</strong>: attract a <a href="/mesh/features/routes/#hostname-routes">private or public hostname's traffic</a> to a Mesh node.</li>
</ul>
<p>Alongside GA, the default IPv4 range used for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/17760.md")</div> (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p><strong>Why this is changing:</strong> Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restrictions block background requests to CGNAT addresses (<code>100.64.0.0/10</code>), which included the previous initial resolved IP default (<code>100.80.0.0/16</code>). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.</p>
<p><strong>What is affected:</strong> Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public</a> hostname routing for Cloudflare Tunnel</li>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a> for Cloudflare Mesh</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> on non-HTTPS ports</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> (Domain, Host, Application, and Content Categories)</li>
</ul>
<p>You can check your account's current range, or configure a custom range, at any time from <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>, or using the <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip">Initial Resolved IP Subnet API</a>.</p>
<div class="nb-dash-button"></div>
<p>For full instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>. The IPv6 range (<code>2606:4700:0cf1:4000::/64</code>) is unchanged and is not affected by this restriction.</p>
<p>The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details.</p>
<p>If you were relying on a Chrome Enterprise policy workaround (such as <code>LocalNetworkAccessRestrictionsTemporaryOptOut</code>) while your account was still on the legacy CGNAT-based range, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</a> for next steps.</p>


<h2 id="waf-release-2026-08-11"><a href="/changelog/post/2026-08-11-waf-release/">WAF Release - 2026-08-11</a></h2>
<p><em>2026-08-11</em></p>
<p>This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>A new detection provides protection against vBulletin CVE-2026-61511.</li>
<li>Two existing detections have been improved to strengthen coverage.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1b0775f0f092483387cfb23f94f3006b">94f3006b</code>
</td>
<td>N/A</td>
<td>vBulletin - Remote Code Execution - CVE:CVE-2026-61511</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="784d3824b6cf419db6af0b64098b749e">098b749e</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID: <code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a561c9138b46470ca6db96edd56225d8">d56225d8</code>
</td>
<td>N/A</td>
<td>vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: <code class="nb-rule-id" title="5137834eb8634842852273a08fe9f1c7">8fe9f1c7</code>)</td>
</tr>
</tbody>
</table>


<h2 id="stream-live-logs-from-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/">Stream live logs from Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-10</em></p>
<p>Real-time Tunnel log streaming is now available in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-live-logs-core-dashboard.gif" alt="Stream live logs from a tunnel in the Cloudflare dashboard" /></p>
<p>In the tunnel detail view, a new <strong>Live logs</strong> tab lets you:</p>
<ul>
<li><strong>Stream logs from single or multiple connectors</strong> — In <a href="/tunnel/configuration/#replicas-and-high-availability">highly available</a> deployments with multiple <code>cloudflared</code> replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.</li>
<li><strong>Filter by log level, event type, and HTTP method</strong> — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or <code>cloudflared</code> internal), at any log level.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/tunnel/observability/#remote-log-streaming">Tunnel observability</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a>.</p>


<h2 id="turnstile-spin-is-now-generally-available"><a href="/changelog/post/2026-08-10-turnstile-spin-ga/">Turnstile Spin is now generally available</a></h2>
<p><em>2026-08-10</em></p>
<p><a href="/turnstile/spin/">Turnstile Spin</a> is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.</p>
<h4 id="2026-08-10-turnstile-spin-ga-server-side-verification">Server-side verification</h4>
<p>Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.</p>
<ul>
<li>The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.</li>
<li>The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select <strong>Fix with Spin</strong> to copy a prompt that guides your agent through wiring siteverify into your backend.</li>
<li>Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.</li>
</ul>
<h4 id="2026-08-10-turnstile-spin-ga-run-spin">Run Spin</h4>
<p>You can run Spin three ways:</p>
<ul>
<li>In the <strong>Turnstile dashboard</strong>, select <strong>Set up with Spin</strong>, enter your domains, then select <strong>Set up</strong>. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.</li>
<li>From the <code>Wrangler CLI</code>, run <a href="/turnstile/spin/#set-up-from-the-wrangler-cli"><code>wrangler turnstile widget create</code></a>. Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.</li>
<li>From your <strong>AI coding agent</strong>, paste the <a href="/turnstile/spin/#set-up-from-an-ai-coding-agent">Spin prompt</a> into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.</li>
</ul>
<p>To get started, refer to the <a href="/turnstile/spin/">Turnstile Spin documentation</a>.</p>


<h2 id="waf-release-2026-08-07"><a href="/changelog/post/2026-08-07-waf-release/">WAF Release - 2026-08-07</a></h2>
<p><em>2026-08-07</em></p>
<p>This release updates WordPress XSS rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify XSS2Shell (CVE-2026-64638). It also disables the Command Injection - Obfuscation rule.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-64638: A pre-authentication reflected cross-site scripting vulnerability affecting the WordPress login screen. Exploitation requires social engineering and explicit interaction by the target user. Under additional conditions, it may be escalated to remote code execution.</li>
</ul>
<p><strong>Impact</strong></p>
<p>The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Wordpress - XSS - CVE:CVE-2026-64638</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Wordpress - XSS - CVE:CVE-2026-64638</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Block</td>
<td>Disabled</td>
<td>Detection logic has been deprecated</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-08-04"><a href="/changelog/post/2026-08-04-waf-release/">WAF Release - 2026-08-04</a></h2>
<p><em>2026-08-04</em></p>
<p>This release introduces new rules and updates Microsoft SharePoint RCE alongside enhanced SSRF cloud protection rule actions.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-50522: An insecure deserialization vulnerability in Microsoft SharePoint Server. This may allow an unauthenticated attacker to execute arbitrary code using crafted requests.</li>
<li>CVE-2026-66066: An improper input processing vulnerability in Ruby on Rails Active Storage image variant transformations. This may allow an unauthenticated attacker to perform arbitrary file reads and achieve Remote Code Execution (RCE) using maliciously crafted payload requests.</li>
<li>Generic Cloud Protections: Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="91aee93c31944828bf86f068052b07cf">052b07cf</code>
</td>
<td>N/A</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2026-50522</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>Rails - Arbitrary File Read & RCE - CVE:CVE-2026-66066</td>
<td>Block</td>
<td>Block</td>
<td>
				This was labeled as File Upload - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code>
</td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="281a1b7086b84db7a695220725ba9d7c">25ba9d7c</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud</td>
<td>Disabled</td>
<td>Block</td>
<td>
				We are changing the action for this rule from Disabled to BLOCK
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code>
</td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-07-29"><a href="/changelog/post/2026-07-29-waf-release/">WAF Release - 2026-07-29</a></h2>
<p><em>2026-07-29</em></p>
<p>This release introduces new rules and updates existing threat signatures to provide targeted protections for vulnerabilities in Nuxt Server Island components and Alibaba Fastjson deserialization routines, alongside enhanced protections for cloud metadata Server-Side Request Forgery (SSRF) and obfuscated command injection attempts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Nuxt Server Island - RCE(GHSA-9473-5f9j-94wq): An unauthenticated vulnerability in Nuxt Server Islands where remote attackers can supply arbitrary component names or props to endpoints. Manipulating these parameters allows unauthenticated component Remote Code Execution (RCE) on the server.</p>
</li>
<li>
<p>Alibaba Fastjson JSONType Remote Code Execution: A unauthenticated remote code execution vulnerability in Alibaba Fastjson (≤ 1.2.83) during JSON deserialization. Under default configurations, attackers can execute arbitrary system commands, bypassing traditional classpath and gadget-based defenses.</p>
</li>
<li>
<p>Generic Protections (SSRF &amp; Command Injection): Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications, alongside new rules targeting obfuscated command injection patterns across request parameters.</p>
</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is an improved detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Log</td>
<td>Block</td>            
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58df9693db4d454a8764fcda7347c892">7347c892</code>
</td>
<td>N/A</td>
<td>Alibaba Fastjson JSONType Remote Code Execution - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6159ead63d284147943dc5a18ec012ea">8ec012ea</code>
</td>
<td>N/A</td>
<td>Nuxt Server Island - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.This was labeled as Generic Rules - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ecac499d14a4750aa58c1e21b7f9c67">1b7f9c67</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="faster-and-more-secure-tls-handshakes-to-your-origins-automatically"><a href="/changelog/post/2026-07-21-automatic-origin-key-exchange/">Faster and more secure TLS handshakes to your origins, automatically</a></h2>
<p><em>2026-07-21</em></p>
<p>Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first <code>ClientHello</code>, helping avoid a <code>HelloRetryRequest</code> and one extra network round trip.</p>
<p>Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum <code>X25519MLKEM768</code> hybrid key agreement.</p>
<p>To change this behavior, go to <strong>SSL/TLS</strong> &gt; <strong>Overview</strong> &gt; <strong>Origin connection &amp; post-quantum encryption</strong>. Turn off <strong>Automatic key exchange</strong> to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.</p>
<p><strong>Compliance requirements</strong> apply only to TLS 1.3 connections. The <strong>Post-quantum hybrid</strong> option requires hybrid post-quantum key agreements support on your origin server. The <strong>Federal Information Processing Standards (FIPS)</strong> option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.</p>
<p>For requirements, configuration options, and rollout details, refer to <a href="/ssl/origin-configuration/automatic-key-exchange/">Automatic key exchange to origins</a>.</p>


<h2 id="waf-release-2026-07-21"><a href="/changelog/post/2026-07-21-waf-release/">WAF Release - 2026-07-21</a></h2>
<p><em>2026-07-21</em></p>
<p>This release introduces new rules for vulnerabilities in Adobe ColdFusion, Next.js, WordPress alongside updates to existing rules thereby providing enhanced generic protections against Server-Side Request Forgery (SSRF), Local File Inclusion (LFI), and Cross-Site Scripting (XSS).</p>
<p><strong>WAF and framework adapter mitigations for Next.js vulnerabilities</strong></p>
<p>Multiple <a href="https://nextjs.org/blog/july-2026-security-release">security vulnerabilities</a> were disclosed and patched by the Next.js team through July 2026 security release. These include denial of service, middleware and proxy bypass, server-side request forgery, information disclosure, and cache poisoning across a range of severities.</p>
<p>Several of the disclosed vulnerabilities are not possible to block at WAF layer,we strongly recommend updating your application and its dependencies immediately. Patched versions are available through v16.2.11 (Active LTS) and v15.5.21 (Maintenance LTS) to address these issues.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Advisory</th>
<th>CVE</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF Coverage</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj">Denial of Service in App Router using Server Actions</a></td>
<td>CVE-2026-64641</td>
<td>High</td>
<td>
				Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage. The CPU usage blocks processing of further requests in the same process, leading to Denial of Service.
</td>
<td>
				WAF rule Next.js - DoS - CVE-2026-64641 (<code class="nb-rule-id" title="b013b67c357547b4b866234390dcdb0a">90dcdb0a</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24">Middleware / Proxy bypass in App Router applications using Turbopack and single locale</a></td>
<td>CVE-2026-64642</td>
<td>High</td>
<td>
				Next.js applications using App Router built with Turbopack and a single entry in config.i18n.locales are vulnerable to a middleware/proxy bypass. Accordingly, any authentication or security checks that a middleware/proxy may perform are bypassed.
</td>
<td>
				This is a middleware bypass that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4">Server-Side Request Forgery in rewrites via attacker-controlled destination hostname</a></td>
<td>CVE-2026-64645</td>
<td>High</td>
<td>
				A rewrites() or redirects() rule that builds its external destination hostname from request-controlled input can be pointed at an arbitrary hostname, regardless of the rule's hostname suffix. For rewrites, this behavior enables Server-Side Request Forgery (SSRF); for redirects, Open Redirect can be achieved.
</td>
<td>
				Existing SSRF rules provide adequate coverage for this vulnerability, no tailored WAF rule was developed.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x">Server-Side Request Forgery in Server Actions on custom servers</a></td>
<td>CVE-2026-64649</td>
<td>High</td>
<td>
				When a Server Action forwards or redirects a request, an attacker can cause the server to send that outbound request to a malicious host (Server-Side Request Forgery). This requires the attacker’s request to control Host-associated headers.
</td>
<td>
				WAF rule Next.js - SSRF - CVE-2026-64649 (<code class="nb-rule-id" title="7fe6d6f3df774ae2a0011f20930091a3">930091a3</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch">Denial of Service in the Image Optimization API using SVGs</a></td>
<td>CVE-2026-64644</td>
<td>Medium</td>
<td>
				When self-hosting Next.js with the default image loader, the Image Optimization API can optimize remotely hosted images if configured (not enabled by default). If those images contain malicious content, the images can cause CPU exhaustion in the /_next/image endpoint.
</td>
<td>
				Malicious request is unfortunately indistinguishable from a legitimate image optimization request, so no WAF rule has been created to address this vulnerability.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3">Unbounded Server Action payload in Edge runtime</a></td>
<td>CVE-2026-64646</td>
<td>Medium</td>
<td>
				A crafted request can lead to memory consumption on Server Actions in the Edge runtime. Next.js applications which use App Router and have at least one Server Action are affected.
</td>
<td>
				Unfortunately there is no one size fits all rule that can be deployed through WAF in lieu of custom bodySizeLimit configurations, so no WAF rule has been created to address this vulnerability.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp">Unauthenticated disclosure of internal Server Function endpoints</a></td>
<td>CVE-2026-64643</td>
<td>Medium</td>
<td>
				In Next.js applications using App Router, Server Actions (use server) or use cache endpoint IDs can be globally disclosed. An attacker can use this for reconnaissance and as part of a broader attack chain.
</td>
<td>
				WAF rule Next.js - Information Disclosure - CVE-2026-64643 (<code class="nb-rule-id" title="6c4135d4d9d745e4866ad83672952826">72952826</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742">Cache confusion of response bodies for requests with bodies</a></td>
<td>CVE-2026-64648</td>
<td>Medium</td>
<td>
				A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies for fetch calls of the shape fetch(new Request(init), aDifferentInit)
</td>
<td>
				This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q">Cache confusion of response bodies for requests with bodies containing invalid UTF-8 byte sequences</a></td>
<td>CVE-2026-64647</td>
<td>Medium</td>
<td>
				A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies when receiving request bodies which contain invalid UTF-8 characters.
</td>
<td>
				This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
</tbody>
</table>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-48276: A path traversal vulnerability in Adobe ColdFusion file upload mechanisms allows unauthenticated attackers to write or upload files to arbitrary locations outside designated directories on the origin server.</p>
</li>
<li>
<p>CVE-2026-48282: A path traversal vulnerability in Adobe ColdFusion enables unauthenticated attackers to manipulate directory sequences and access restricted system files on the host filesystem.</p>
</li>
<li>
<p>CVE-2026-60137: An unauthenticated SQL injection vulnerability affecting WordPress. Threat actors exploit unsanitized input parameters to execute arbitrary SQL queries, leading to unauthorized database access, record manipulation, or data exfiltration.</p>
</li>
<li>
<p>CVE-2026-63030: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.</p>
</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7fbdc9407bdb4a4eae2b3d91215e7d31">215e7d31</code>
</td>
<td>N/A</td>
<td>SSRF - Restricted Protocol</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ca512d240d848d6a0c7ef42a935ee5d">a935ee5d</code>
</td>
<td>N/A</td>
<td>SSRF - Obfuscated Host</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3fb0870c38440d8a9a0eba81b0230ac">1b0230ac</code>
</td>
<td>N/A</td>
<td>LFI - Path Traversal</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="452a04be3f73458c863d8dae61349c8b">61349c8b</code>
</td>
<td>N/A</td>
<td>Adobe ColdFusion - File Upload Path Traversal - CVE:CVE-2026-48276</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a53a3fb491c64d74908081ee9cb61eac">9cb61eac</code>
</td>
<td>N/A</td>
<td>Adobe ColdFusion - Path Traversal - CVE:CVE-2026-48282</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d8b63828c2344d919b94d2594ac5e21f">4ac5e21f</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="264a83a764be428ca41d516ff31f5559">f31f5559</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4ba21a60837244029183b782987984fd">987984fd</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Wordpress - SQL Injection - CVE:CVE-2026-60137</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - SQLi.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-63030</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Unauthenticated RCE.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Wordpress - SQL Injection - CVE:CVE-2026-60137</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - SQLi.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-63030</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Unauthenticated RCE.
</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6c4135d4d9d745e4866ad83672952826">72952826</code>
</td>
<td>N/A</td>
<td>Next.js - Information Disclosure - CVE-2026-64643</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Information Disclosure.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7fe6d6f3df774ae2a0011f20930091a3">930091a3</code>
</td>
<td>N/A</td>
<td>Next.js - SSRF - CVE-2026-64649</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Auth Bypass - 2.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c4ca56c0a6a348299d5a93e663167195">63167195</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - Cache Components</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - RCE.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b013b67c357547b4b866234390dcdb0a">90dcdb0a</code>
</td>
<td>N/A</td>
<td>Next.js - DoS - CVE-2026-64641</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - DoS.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="aa21c9b8b97743bfb217748b2049a60c">2049a60c</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e7ee67e824844754b513cdf3836855a4">836855a4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5f2a6681a2b94442b23816286d060a0d">6d060a0d</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-07-17-emergency"><a href="/changelog/post/2026-07-17-emergency-waf-release/">WAF Release - 2026-07-17 - Emergency</a></h2>
<p><em>2026-07-17</em></p>
<p>This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.</p>
</li>
<li>
<p>Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.</p>
</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>


<h2 id="bot-management-fields-and-asn-support-in-cache-rules"><a href="/changelog/post/2026-07-16-cache-rules-bot-fields-asn/">Bot management fields and ASN support in Cache Rules</a></h2>
<p><em>2026-07-16</em></p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-bot-management-fields-and-asn-support-in-cache-rules">Bot management fields and ASN support in Cache Rules</h4>
<p>Cache Rules now supports bot management fields and the <code>ip.src.asnum</code> field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).</p>
<p>This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.</p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-new-fields">New fields</h4>
<p>The following fields are now available in Cache Rules expressions:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.bot_management.score</code></td>
<td>Number</td>
<td>Bot score from <code>1</code> to <code>99</code>, where a lower value indicates a higher likelihood that the request originates from a bot.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja3_hash</code></td>
<td>String</td>
<td>JA3 fingerprint of the request, which helps identify the client making the connection.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja4</code></td>
<td>String</td>
<td>JA4 fingerprint of the request, which provides a more detailed client identification than JA3.</td>
</tr>
<tr>
<td><code>cf.bot_management.verified_bot</code></td>
<td>Boolean</td>
<td>Whether the request originates from a verified bot, such as a search engine crawler.</td>
</tr>
<tr>
<td><code>cf.bot_management.static_resource</code></td>
<td>Boolean</td>
<td>Whether the request is for a static resource and therefore exempt from bot detection.</td>
</tr>
<tr>
<td><code>cf.bot_management.js_detection.passed</code></td>
<td>Boolean</td>
<td>Whether the browser passed JavaScript detection when the feature is enabled.</td>
</tr>
<tr>
<td><code>cf.bot_management.detection_ids</code></td>
<td>Array&lt;Number&gt;</td>
<td>List of IDs that correspond to Bot Management heuristic detections made on the request.</td>
</tr>
<tr>
<td><code>cf.bot_management.tags</code></td>
<td>Array&lt;String&gt;</td>
<td>List of tags associated with the bot traffic, such as <code>API</code>, <code>GOOGLE</code>, or <code>BING</code>. Match a tag with an expression such as <code>any(cf.bot_management.tags[*] eq &quot;API&quot;)</code>.</td>
</tr>
<tr>
<td><code>cf.bot_management.signed_agent</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known agent that identifies itself with Web Bot Auth.</td>
</tr>
<tr>
<td><code>cf.bot_management.corporate_proxy</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known corporate proxy.</td>
</tr>
<tr>
<td><code>ip.src.asnum</code></td>
<td>Number</td>
<td>The autonomous system number (ASN) of the incoming request's IP address.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17750.md")</aside>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-example">Example</h4>
<p>Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:</p>
<pre><code class="language-txt">(http.request.uri.path contains &quot;/api/&quot; and cf.bot_management.score lt 30)&#10;or&#10;(http.request.uri.path contains &quot;/api/&quot; and not ip.src.asnum in {12345 67890})&#10;</code></pre>
<p>To learn more, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a> and the <a href="/ruleset-engine/rules-language/fields/">Fields reference</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/2/">Next</a></nav>
