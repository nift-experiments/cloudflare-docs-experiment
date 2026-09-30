<p>The Application Check device posture attribute checks that a specific application process is running on a device. You can create multiple application checks for each operating system you need to run it on, or if you need to check for multiple applications.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="configure-an-application-check">Configure an application check</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Application Check</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ol>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select your operating system.</li>
<li><strong>Application path</strong>: Enter the file path for the executable that will be running (for example, <code>C:\Program Files\myfolder\myfile.exe</code>).</li>
</ol>
</li>
</ol>
<details class="nb-details" open><summary>Environment variables</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5933.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5932.md")
</aside>
<ol start="5">
<li>
<p><strong>Signing certificate thumbprint (recommended)</strong>: Enter the <a href="#determine-the-signing-thumbprint">thumbprint of the publishing certificate</a> used to sign the binary. Adding this information will enable the check to ensure that the application was signed by the expected software developer.</p>
</li>
<li>
<p><strong>SHA-256 (optional)</strong>: Enter the <a href="#determine-the-sha-256-value">SHA-256 value</a> of the binary. This is used to ensure the integrity of the binary file on the device.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the application check is returning the expected results.</p>
<h2 id="determine-the-signing-thumbprint">Determine the signing thumbprint</h2>
<p>The process to determine the signing thumbprint of an application varies depending on the operating system. This is how you would look up the signing thumbprint of the Cloudflare One Client application on macOS and Windows.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5931.md")
</aside>
<h3 id="macos">macOS</h3>
<ol>
<li>Create a directory.</li>
</ol>
<pre><code class="language-bash">~/Desktop $ mkdir tmp&#10;&#10;~/Desktop $ cd tmp&#10;</code></pre>
<ol start="2">
<li>Run the following command to extract certificates for the Cloudflare One Client application:</li>
</ol>
<pre><code class="language-sh">~/Desktop/tmp $ codesign -d --extract-certificates &quot;/Applications/Cloudflare WARP.app/Contents/Resources/CloudflareWARP&quot;&#10;Executable=/Applications/Cloudflare WARP.app/Contents/Resources/CloudflareWARP&#10;</code></pre>
<ol start="3">
<li>Next, run the following command to extract the SHA1 thumbprint:</li>
</ol>
<pre><code class="language-sh">~/Desktop/tmp $ openssl x509 -inform DER -in codesign0 -fingerprint -sha1 -noout | tr -d :&#10;SHA1 Fingerprint=FE2C359D79D4CEAE6BDF7EFB507326C6B4E2436E&#10;</code></pre>
<h3 id="windows">Windows</h3>
<ol>
<li>Open a PowerShell window.</li>
<li>Use the <code>Get-AuthenticodeSignature</code> command to find the thumbprint. For example:</li>
</ol>
<pre><code class="language-powershell">Get-AuthenticodeSignature -FilePath c:\myfile.exe&#10;</code></pre>
<h2 id="determine-the-sha-256-value">Determine the SHA-256 value</h2>
<p>The SHA-256 value almost always changes between versions of a file/application.</p>
<h3 id="macos-1">macOS</h3>
<ol>
<li>Open a Terminal window.</li>
<li>Use the <code>shasum</code> command to find the SHA256 value of the file. For example:</li>
</ol>
<pre><code class="language-sh">shasum -a 256 myfile&#10;</code></pre>
<h3 id="windows-1">Windows</h3>
<ol>
<li>Open a PowerShell window.</li>
<li>Use the <code>get-filehash</code> command to find the SHA256 value of the file. For example:</li>
</ol>
<pre><code class="language-powershell">get-filehash -path &quot;C:\myfile.exe&quot; -Algorithm SHA256 | format-list&#10;</code></pre>
<h2 id="how-warp-checks-for-an-application">How WARP checks for an application</h2>
<p>Learn how the Cloudflare One Client determines if an application is running on various systems.</p>
<h3 id="macos-2">macOS</h3>
<p>To get the list of active processes, run the following command:</p>
<pre><code class="language-sh">ps -eo comm | xargs -I {} which &quot;{}&quot; | sort | uniq | xargs -I {} realpath &quot;{}&quot;&#10;</code></pre>
<p>The application path must appear in the output for the check to pass.</p>
<h3 id="linux">Linux</h3>
<p>The Cloudflare One Client gets the list of running binaries by following the soft links in <code>/proc/&lt;pid&gt;/exe</code>. To view all active processes and their soft links:</p>
<pre><code class="language-sh">ps -eo pid | awk &#x27;{print &quot;/proc/&quot;$1&quot;/exe&quot;}&#x27; | xargs readlink -f | awk &#x27;{print $1}&#x27; | sort | uniq&#10;</code></pre>
<p>The application path must appear in the <code>/proc/&lt;pid&gt;/exe</code> output for the check to pass.</p>
<h3 id="windows-2">Windows</h3>
<p>To get the list of active processes, run the following command:</p>
<pre><code class="language-powershell">Get-Process | Select-Object ProcessName, Path | Format-Table -AutoSize&#10;</code></pre>
<p>The application path must appear in the output for the check to pass.</p>
