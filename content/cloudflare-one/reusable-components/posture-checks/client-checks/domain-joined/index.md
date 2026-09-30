<p>The Domain Joined device posture attribute ensures that a user is a member of a specific Windows Active Directory domain.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-domain-joined-check">Enable the Domain Joined check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>Domain Joined</strong>.</li>
<li>Enter a descriptive name for the check.</li>
<li>Select your operating system.</li>
<li>Enter the domain you want to check for, such as <code>example.com</code>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5919.md")
</aside>
7. Select **Save**.
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the Domain Joined check is returning the expected results.</p>
<h2 id="validate-the-domain-value">Validate the domain value</h2>
<p>To check the domain value on your Windows device:</p>
<ol>
<li>Open a PowerShell window.</li>
<li>Run the following command:</li>
</ol>
<pre><code class="language-powershell">(Get-WmiObject Win32_ComputerSystem).Domain&#10;</code></pre>
<p>The command will return the Active Directory domain to which your device belongs.</p>
