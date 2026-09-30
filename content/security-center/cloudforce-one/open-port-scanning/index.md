<p>Open Port Scanning allows <a href="/magic-transit/">Magic Transit</a> and <a href="/byoip/">Bring your Own IPs</a> users to efficiently monitor IP ranges for security vulnerabilities. This API enables users to scan their designated IP ranges, detect any open ports, and receive daily notifications regarding newly opened ports.</p>
<p>You can access this feature via the <a href="/api/resources/cloudforce_one/subresources/scans/subresources/config/">API</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Cloudforce One Administrator, Administrator and Super Administrator roles.</li>
<li>Account token: <strong>Custom API Token</strong> &gt;  <strong>Cloudforce One:Edit</strong>.</li>
</ul>
<p>To create a custom API token:</p>
<ol>
<li>From the <a href="https://dash.cloudflare.com/profile/api-tokens/">Cloudflare dashboard</a>, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong> for user tokens. Go to <strong>Create Custom Token</strong> &gt; <strong>Get started</strong>.</li>
<li>Enter a <strong>Token name</strong>, for example, <code>Open Port Scanning</code>.</li>
<li>In <strong>Permissions</strong>:
<ul>
<li>Choose <strong>Account</strong>.</li>
<li>Select <strong>Cloudforce One</strong> as the account.</li>
<li>Choose <strong>Edit</strong> access.</li>
</ul>
</li>
<li>In Client IP Address Filtering:
<ul>
<li>In <strong>Operator</strong>, select <code>is in</code>.</li>
<li>In <strong>Value</strong>, enter a valid IP address.</li>
</ul>
</li>
<li>Select <strong>Continue to summary</strong>.</li>
<li>Review the token, then select <strong>Create Token</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13824.md")
</aside>
<h2 id="configure-open-port-scanning">Configure Open Port Scanning</h2>
<p>To configure Open Port Scanning, follow these steps:</p>
<ol>
<li><strong>Create a new scan config</strong>:
<ul>
<li><strong>IPs</strong>: Enter the IP ranges you wish to monitor. Ensure that the ranges are correctly formatted to avoid scanning errors. The API will validate if the IPs requested are onboarded to Cloudflare and associated to the account belonging to the API token used.</li>
<li><strong>Frequency</strong>: Enter the scan frequency in days.</li>
<li><strong>Ports</strong>: Select the ports to scan. Choose among:
<ul>
<li>All</li>
<li>Default (refer to <a href="/security-center/cloudforce-one/open-port-scanning/#default-ports">Default ports</a> for a comprehensive list)</li>
<li>List of specific ports</li>
</ul>
</li>
</ul>
</li>
<li><strong>Scan IPs</strong>: Initiate the scanning process. The system will analyze the specified IP ranges to identify any open ports.</li>
<li><strong>Generate list of open ports</strong>: Once the scan is complete, the API will generate a list of detected open ports for review and action.</li>
<li><strong>Select open ports to list</strong>: Choose which open ports you would like to be notified about. You can exclude  any ports that do not require immediate attention.</li>
<li><strong>View differences from previous scan</strong>: The API will highlight any changes in open ports since the last scan, allowing you to quickly assess new vulnerabilities.</li>
<li><strong>Stop scanning</strong>: If necessary, you can stop  the scanning process at any time.</li>
<li><strong>Set up alerts</strong>: Configure alerts for specific ports of interest. You will be notified immediately via email or webhook if any of these designated ports become newly open.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="beta-feature-notice">Beta feature notice</h3>
@markup("md", "content/.markup/bodies/13823.md")
</aside>
<h2 id="default-ports">Default ports</h2>
<details class="nb-details"><summary>List of default ports</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13825.md")
</div></details>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<ol>
<li>
<p>What IPs will the scan come from?</p>
<ul>
<li><code>2a09:bac0:1008:5000:1000:0000:0000:0050/104.30.128.13</code></li>
<li><code>2a09:bac0:1008:5000:1000:0000:0000:0048/104.30.129.33</code></li>
<li><code>2001:19f0:1000:2941:5400:4ff:fe70:2a7a/140.82.60.241</code></li>
</ul>
</li>
<li>
<p>Can the Port Scanner bypass other security rules configured?</p>
<ul>
<li>The Cloudforce One team asks customers to ensure they allow the IPs for the scanner to run correctly.</li>
</ul>
</li>
<li>
<p>How long do scans take?</p>
<ul>
<li>Depending on the number of IP addresses and number of ports scanned, scans can take between a few minutes and up to 10 hours.</li>
</ul>
</li>
<li>
<p>Can I stop automatic scanning?</p>
<ul>
<li>Yes, you can decide at any point to stop scan and restart scans when it is convenient for you.</li>
</ul>
</li>
<li>
<p>What are the limitations for the scans?</p>
<ul>
<li>Scans are limited to ranges of up to 5,000 IPs.</li>
<li>The API scans both IPv4 and IPv6 IP addresses.</li>
</ul>
</li>
</ol>
