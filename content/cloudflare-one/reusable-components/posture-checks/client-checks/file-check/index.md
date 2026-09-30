<p>The File Check device posture attribute checks for the presence of a file on a device. You can create multiple file checks for each operating system you need to run it on, or if you need to check for multiple files.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="configure-a-file-check">Configure a file check</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>File Check</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ol>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select your operating system.</li>
<li><strong>File Path</strong>: Enter a file path (for example, <code>c:\my folder\myfile.exe</code>).</li>
</ol>
</li>
</ol>
<details class="nb-details" open><summary>Environment variables</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5918.md")
</div></details>
<ol start="4">
<li>
<p><strong>Signing certificate thumbprint (recommended)</strong>: Enter the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/#determine-the-signing-thumbprint">thumbprint</a> of the publishing certificate used to sign the file. Adding this information will enable the check to ensure that the file was signed by the expected software developer.</p>
</li>
<li>
<p><strong>SHA-256 (optional)</strong>: Enter the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/#determine-the-sha-256-value">SHA-256 value</a> of the file. This is used to ensure the integrity of the file on the device.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the file check is returning the expected results.</p>
