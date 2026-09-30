<p>Cloudflare Gateway can scan files for malware as users upload or download them. Anti-virus (AV) scanning runs inline — Gateway inspects files as they pass through the proxy and blocks any file that contains a known malicious payload.</p>
<p>In addition to AV scanning, Gateway can quarantine previously unseen files into a sandbox to detect zero-day threats not yet in anti-virus databases. For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">File sandboxing</a>.</p>
<h2 id="get-started">Get started</h2>
<p>To turn on AV scanning:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Policy settings</strong>, turn on <strong>Scan files for malware</strong>.</li>
<li>Choose whether to scan files for malicious payloads during uploads, downloads, or both. You can also block requests containing <a href="#non-scannable-files">non-scannable files</a>.</li>
<li>(Optional) Turn on <strong>Display AV block notification for Cloudflare One Client</strong> to send <a href="#cloudflare-one-client-block-notifications">block notifications</a> to users connected to Gateway with the Cloudflare One Client when AV inspection blocks a file.</li>
</ol>
<p>When a request is blocked due to the presence of malware, Gateway will log the match as a Block decision in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#http-logs">HTTP logs</a>.</p>
<h3 id="cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6591.md")
</div></details>
<p>Turn on <p><strong>Display AV block notification for Cloudflare One Client</strong></p>
to display notifications for Gateway block events. Blocked users will receive an operating system notification from the Cloudflare One Client with a custom message you set. If you do not set a custom message, the Cloudflare One Client will display a default message. Custom messages must be 100 characters or less. The Cloudflare One Client will only display one notification per minute.</p>
<p>Upon selecting the notification, the Cloudflare One Client will direct your users to the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Gateway block page</a> you have configured. Optionally, you can direct users to a custom URL, such as an internal support form.</p>
<p>When you turn on <strong>Send policy context</strong>, Gateway will append details of the matching request to the redirected URL as a query string. Not every context field will be included. Potential policy context fields include:</p>
<details class="nb-details"><summary>Policy context fields</summary><div class="nb-details-body">
@input("content/.markup/bodies/6592.md")
</div></details>
<div class="nb-data-component" data-cf-component="Render"></div>
<h2 id="file-scan-criteria">File scan criteria</h2>
<p>If AV scanning is turned on, Gateway uses the following criteria (in order) to detect and scan files. The first match triggers a scan:</p>
<ol>
<li>The <code>Content-Disposition</code> HTTP header is set to <code>Attachment</code>.</li>
<li>The byte signature of the request or response body matches a known file type:
<ul>
<li><strong>Executable</strong> (for example, <code>.exe</code>, <code>.bat</code>, <code>.dll</code>, and <code>.wasm</code>)</li>
<li><strong>Documents</strong> (for example, <code>.doc</code>, <code>.docx</code>, <code>.pdf</code>, <code>.ppt</code>, and <code>.xls</code>)</li>
<li><strong>Compressed</strong> (for example, <code>.7z</code>, <code>.gz</code>, <code>.zip</code>, and <code>.rar</code>)</li>
</ul>
</li>
<li>The file name in the <code>Content-Disposition</code> header contains a file extension matching one of the above categories.</li>
</ol>
<p>If none of these conditions match, Gateway falls back to the origin's <code>Content-Type</code> header. Gateway will not scan files it determines to be image, video, or audio files. All other files default to being scanned.</p>
<h2 id="opt-content-out-from-scanning">Opt content out from scanning</h2>
<p>When an admin turns on AV scanning for uploads and/or downloads, Gateway will scan every supported file. Admins can selectively choose to disable scanning using HTTP policies. All <a href="/cloudflare-one/traffic-policies/http-policies/#selectors">HTTP selectors</a> can opt HTTP traffic out from AV scanning using the <strong>Do Not Scan</strong> action. When traffic matches a Do Not Scan policy, nothing is scanned, regardless of file size or whether the file type is supported or not. For example, to prevent AV scanning of files uploaded to or downloaded from <code>example.com</code>, you can create the following policy:</p>
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
<td>Hostname</td>
<td>matches regex</td>
<td><code>example.com</code></td>
<td>Do Not Scan</td>
</tr>
</tbody>
</table>
<p>Opting out of AV scanning applies to uploads and/or downloads of files, matching your account's global AV scanning setting. For example, if you have configured Gateway to globally scan uploads only, then opting out of AV scanning will only apply to uploads.</p>
<h2 id="compatibility">Compatibility</h2>
<h3 id="supported-compressed-file-types">Supported compressed file types</h3>
<p>In addition to standard object files like PDFs, Zero Trust supports AV scanning for the following archive types:</p>
<details class="nb-details"><summary>Supported compressed file types</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6593.md")
</div></details>
<p>Gateway cannot scan <a href="#non-scannable-files">certain archive files</a> regardless of file type, such as large or encrypted files.</p>
<h3 id="non-scannable-files">Non-scannable files</h3>
<p>Gateway cannot scan all files for malware. When Gateway encounters a non-scannable file, you can configure AV scanning to either fail open (allow the file to pass through unscanned) or fail closed (deny the file transfer).</p>
<p>Gateway cannot scan requests containing the following files:</p>
<ul>
<li>Files larger than:
<ul>
<li>15 MB on Free plans</li>
<li>25 MB on Pay-as-you-go plans</li>
<li>100 MB on Enterprise plans</li>
</ul>
</li>
<li>PGP encrypted files</li>
<li>Password protected archives</li>
<li>Archives with more than three recursion levels</li>
<li>Archives with more than 300 files</li>
</ul>
