<p>The following DLP policies are commonly used to secure sensitive data in uploaded and downloaded files. They are built as <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a> using the <a href="/cloudflare-one/traffic-policies/http-policies/#dlp-profile">DLP Profile</a> selector.</p>
<p>Before using these policies, complete the <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#prerequisites">prerequisites for scanning HTTP traffic</a>.</p>
<h2 id="log-uploads-downloads">Log uploads/downloads</h2>
<p>When you want to monitor where sensitive data is going before enforcing blocks, use the <strong>Allow</strong> action. In a Gateway HTTP policy, all matches — including Allow — are recorded in your <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#4-view-dlp-logs">HTTP request logs</a>. This gives you visibility into sensitive data transfers without disrupting users.</p>
<p>The following example logs any upload or download that matches your enabled <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#financial-information">Financial Information</a> DLP profile entries when users interact with file sharing applications.</p>
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
<td><em>Financial Information</em></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Content Categories</td>
<td>in</td>
<td><em>File Sharing</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="block-file-types">Block file types</h2>
<p>Block the upload or download of files based on their type.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4909.md")
</div></div>
<p>For more information on what file formats DLP can scan, refer to <a href="/cloudflare-one/data-loss-prevention/#supported-file-types">Supported file types</a>.</p>
<h2 id="block-uploads-downloads-for-specific-users">Block uploads/downloads for specific users</h2>
<p>You can configure access on a per-user or group basis by adding <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based conditions</a> to your policies. These selectors match against user attributes from your configured identity provider.</p>
<p>The following example blocks only contractors from uploading/downloading Financial Information to file sharing apps. Users who are not in the <em>Contractors</em> group are not affected by this policy.</p>
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
<td><em>Financial Information</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Content Categories</td>
<td>in</td>
<td><em>File Sharing</em></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>User Group Names</td>
<td>in</td>
<td><em>Contractors</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="exclude-android-applications">Exclude Android applications</h2>
<p>Many Android applications (such as Google Drive) use <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4910.md")
</div>, which is incompatible with Gateway TLS decryption. These applications verify they are connecting directly to their own servers and will reject Gateway's inspection certificate. If needed, you can create a [Do Not Inspect policy](/cloudflare-one/traffic-policies/http-policies/#do-not-inspect) so that the app can continue to function on Android:
<ol>
<li>
<p>Set up an <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/">OS version device posture check</a> that checks for the Android operating system.</p>
</li>
<li>
<p>Create the following HTTP policy in Gateway:</p>
</li>
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
<td>Application</td>
<td>in</td>
<td><em>Google Drive</em></td>
<td>And</td>
<td>Do Not Inspect</td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>in</td>
<td><em>OS Version Android</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Android users can now use the app, but the app traffic will bypass Gateway inspection entirely — including DLP scanning, HTTP logging, and antivirus scanning.</p>
<h2 id="exclude-specific-sites">Exclude specific sites</h2>
<p>In your <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#4-view-dlp-logs">DLP logs</a>, you may find that certain sites routinely trigger DLP detections that do not represent actual data loss (false positives). To exempt these sites from DLP scanning:</p>
<ol>
<li>
<p><a href="/cloudflare-one/reusable-components/lists/">Create a list</a> of hostnames or URLs.</p>
</li>
<li>
<p>Exclude the list from your DLP policy using the <code>not in list</code> operator, which references the list you created in step 1:</p>
</li>
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
<td><em>Financial Information</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Google Drive</em></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Domain</td>
<td>not in list</td>
<td><em>Do not DLP - SSN</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
