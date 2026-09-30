<p>The OS Version device posture attribute checks whether the version of a device's operating system matches, is greater than or lesser than the configured value.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-os-version-check">Enable the OS version check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>OS version</strong>.</li>
<li>Configure the <strong>Operating system</strong>, <strong>Operator</strong>, and <strong>Version</strong> fields to specify the <a href="#determine-the-os-version">OS version</a> you want devices to match.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5911.md")
</aside>
<ol start="5">
<li>(Optional) Configure additional OS-specific fields:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5916.md")
</div></div>
<ol start="6">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the OS version check is returning the expected results.</p>
<h2 id="determine-the-os-version">Determine the OS version</h2>
<p>Operating systems display version numbers in different ways. This section covers how to retrieve the version number in each OS, in a format matching what the OS version posture check expects.</p>
<h3 id="macos">macOS</h3>
<ol>
<li>Open a terminal window.</li>
<li>Use the <code>defaults</code> command to check for the value of <code>SystemVersionStampAsString</code>.</li>
</ol>
<pre><code class="language-sh">defaults read loginwindow SystemVersionStampAsString&#10;</code></pre>
<h3 id="windows">Windows</h3>
<p>Windows version numbers consist of four parts: <code>Major.Minor.Build.UBR</code>. For example, <code>10.0.19045.3803</code> where:</p>
<ul>
<li><code>10.0</code> is the <strong>Version</strong> (Major.Minor)</li>
<li><code>19045</code> is the <strong>Build</strong> number</li>
<li><code>3803</code> is the <strong>UBR</strong> (Update Build Revision)</li>
</ul>
<p>To determine the Windows version on your device:</p>
<ol>
<li>Open a PowerShell window.</li>
<li>Get the <strong>Version</strong> (Major.Minor.Build):</li>
</ol>
<pre><code class="language-bash">(Get-CimInstance Win32_OperatingSystem).version&#10;</code></pre>
<p>This returns the version in the format <code>Major.Minor.Build</code> (for example, <code>10.0.19045</code>).</p>
<ol start="3">
<li>Get the <strong>UBR</strong> (Update Build Revision):</li>
</ol>
<pre><code class="language-bash">(Get-ItemProperty -Path &quot;HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion&quot; -Name UBR).UBR&#10;</code></pre>
<p>This returns the UBR value (for example, <code>3803</code>).</p>
<h3 id="linux">Linux</h3>
<h4 id="os-version">OS version</h4>
<p>The Linux OS version check reads the system kernel version.</p>
<ol>
<li>
<p>Open a Terminal window.</p>
</li>
<li>
<p>Run the <code>uname -r</code> command to get the complete kernel version. For example,</p>
</li>
</ol>
<pre><code class="language-sh">$ uname -r&#10;5.14.0-25.el9.x86_64&#10;</code></pre>
<ol start="3">
<li>
<p><strong>Version</strong> is the first three numbers of the output in SemVer format (<code>5.14.0</code>).</p>
</li>
<li>
<p><strong>Patch Version</strong> is the first number after the SemVer (<code>25</code>).</p>
</li>
</ol>
<h4 id="distro-version">Distro version</h4>
<p>The Cloudflare One Client reads <strong>Distro name</strong> and <strong>Distro revision</strong> from the <code>/etc/os-release</code> file. The name comes from the <strong>ID</strong> field, and the revision comes from the <strong>VERSION_ID</strong> field.</p>
<p>To determine the Linux distro version on your device:</p>
<ol>
<li>
<p>Open a Terminal window.</p>
</li>
<li>
<p>Get the OS identification fields that contain <code>ID</code>:</p>
</li>
</ol>
<pre><code class="language-sh">cat /etc/os-release | grep &quot;ID&quot;&#10;</code></pre>
<ol start="3">
<li>If the output of the above command contained <code>ID=ubuntu</code> and <code>VERSION_ID=22.04</code>, <strong>Distro name</strong> would be <code>ubuntu</code> and <strong>Distro revision</strong> would be <code>22.04</code>. The Cloudflare One Client will check these strings for an exact match.</li>
</ol>
<h3 id="chromeos">ChromeOS</h3>
<p>ChromeOS version numbers consist of <a href="https://www.chromium.org/developers/version-numbers/">four parts</a>: <code>MAJOR.MINOR.BUILD.PATCH</code>. The OS version posture check returns <code>MAJOR.MINOR.BUILD</code>.</p>
<p>To determine the ChromeOS version on your device:</p>
<ol>
<li>Open Chrome browser and go to <code>chrome://system</code>.</li>
<li>Find the following values:</li>
</ol>
<table>
<thead>
<tr>
<th>Property</th>
<th>OS version component</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CHROMEOS_RELEASE_CHROME_MILESTONE</code></td>
<td><code>MAJOR</code></td>
</tr>
<tr>
<td><code>CHROMEOS_RELEASE_BUILD_NUMBER</code></td>
<td><code>MINOR</code></td>
</tr>
<tr>
<td><code>CHROMEOS_RELEASE_BRANCH_NUMBER</code></td>
<td><code>BUILD</code></td>
</tr>
</tbody>
</table>
3. The OS version in Semver format is `MAJOR.MINOR.BUILD` (for example, `103.14816.131`).
