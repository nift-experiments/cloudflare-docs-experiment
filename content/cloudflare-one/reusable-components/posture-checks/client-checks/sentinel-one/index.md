<p>Cloudflare One can check if <a href="https://www.sentinelone.com/">SentinelOne</a> is running on a device to determine if a request should be allowed to reach a protected resource.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>SentinelOne agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="configure-the-sentinelone-check">Configure the SentinelOne check</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>SentinelOne</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ol>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select your operating system. You will need to configure one posture check per operating system.</li>
<li><strong>Application Path</strong>: Enter the full path to the SentinelOne process to be checked (for example, <code>C:\Program Files\SentinelOne\Sentinel Agent 21.7.4.1043\SentinelAgent.exe</code>).</li>
</ol>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5909.md")
</aside>
<ol start="4">
<li><strong>Signing certificate thumbprint (recommended)</strong>: Enter the thumbprint of the publishing certificate used to sign the binary. This proves the binary came from SentinelOne and is the recommended way to validate the process.</li>
<li><strong>SHA-256 (optional)</strong>: Enter a SHA-256 value. This is used to validate the SHA256 signature of the binary and ensures the integrity of the binary file on the device. Note: do not fill out this field unless you strictly control updates to SentinelOne, as this will change between versions.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the SentinelOne check is returning the expected results.</p>
