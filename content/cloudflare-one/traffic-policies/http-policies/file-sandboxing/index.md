<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6533.md")
</aside>
<p>In addition to <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">anti-virus (AV) scanning</a>, Gateway can quarantine previously unseen files downloaded by your users into a sandbox and scan them for malware.</p>
<p>When a file download passes AV scanning without a malware detection, Gateway quarantines the file in the <a href="#sandbox-environment">sandbox</a>. If the file has not been downloaded before, Gateway monitors the file's behavior and compares it to known malware patterns. During this process, Gateway displays an interstitial page in the user's browser. If the sandbox does not detect malicious activity, Gateway releases the file and downloads it to the user's device. If the sandbox detects malicious activity, Gateway blocks the download. For any subsequent downloads of the same file, Gateway remembers and applies its previous allow/block decision.</p>
<p>Gateway will log any file sandbox decisions in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#http-logs">HTTP logs</a>.</p>
<pre><code class="language-mermaid">flowchart TD&#10;    A([&quot;User starts file download&quot;]) --&gt; B[&quot;File sent to AV scanner&quot;]&#10;    B --&gt; C[&quot;Malicious file detected?&quot;]&#10;    C -- Yes --&gt; D[&quot;Download blocked&quot;]&#10;    C -- No --&gt; G[&quot;File sent to sandbox&quot;]&#10;    G --&gt; n1[&quot;First time file downloaded?&quot;]&#10;    K[&quot;Malicious activity detected?&quot;] -- Yes --&gt; N[&quot;Download blocked&quot;]&#10;    K -- No --&gt; n3[&quot;Download allowed&quot;]&#10;    n2[&quot;Interstitial page displayed for user during scan&quot;] --&gt; n4[&quot;File activity monitored&quot;]&#10;    n1 -- Yes --&gt; n2&#10;    n4 --&gt; K&#10;    n1 -- No --&gt; K&#10;&#10;    B@{ shape: subproc}&#10;    C@{ shape: hex}&#10;    D@{ shape: terminal}&#10;    n1@{ shape: hex}&#10;    K@{ shape: hex}&#10;    N@{ shape: terminal}&#10;    n3@{ shape: terminal}&#10;    n2@{ shape: display}&#10;    n4@{ shape: rect}&#10;    style D stroke:#D50000&#10;    style N stroke:#D50000&#10;    style n3 stroke:#00C853&#10;</code></pre>
<h2 id="get-started">Get started</h2>
<p>To begin quarantining downloaded files, turn on file sandboxing:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Policy settings</strong>, turn on <strong>Open previously unseen files in a sandbox environment</strong>.</li>
<li>(Optional) To block requests containing <a href="#non-scannable-files">non-scannable files</a>, select <strong>Block requests for files that cannot be scanned</strong>.</li>
</ol>
<p>You can now create <a href="/cloudflare-one/traffic-policies/http-policies/#quarantine">Quarantine HTTP policies</a> to determine what files to scan in the sandbox.</p>
<h2 id="create-test-policy">Create test policy</h2>
<p>To test if file sandboxing is working, you can create a Quarantine policy that matches the <a href="https://sandbox.cloudflaredemos.com/">Cloudflare Sandbox Test</a>:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Add the following expression:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>is</td>
<td><code>sandbox.cloudflaredemos.com</code></td>
<td>Quarantine</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>In <strong>Sandbox file types</strong>, select <em>ZIP Archive (zip)</em>.</li>
<li>From a device <a href="/cloudflare-one/team-and-resources/devices/">connected to your Zero Trust organization</a>, open a browser and go to the <a href="https://sandbox.cloudflaredemos.com/">Cloudflare Sandbox Test</a>.</li>
<li>Select <strong>Download Test File</strong>.</li>
</ol>
<p>Gateway will quarantine and scan the file, display an interstitial status page in the browser, then release the file for download.</p>
<h2 id="sandbox-environment">Sandbox environment</h2>
<p>Gateway executes quarantined files in a sandboxed Windows operating system environment. Using machine learning, the sandbox compares how files of a certain type behave compared to how these files should behave. The sandbox detects file actions down to the kernel level and compares them against a real-time malware database. In addition, Gateway checks the sandbox's network activity for malicious behavior and data exfiltration.</p>
<h2 id="compatibility">Compatibility</h2>
<h3 id="supported-file-types">Supported file types</h3>
<p>File sandboxing supports scanning the following file types:</p>
<details class="nb-details"><summary>Supported sandboxing file types</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6534.md")
</div></details>
<h3 id="non-scannable-files">Non-scannable files</h3>
<p>Gateway cannot scan requests containing the following files:</p>
<ul>
<li>Files larger than 100 MB</li>
<li>PGP encrypted files</li>
</ul>
