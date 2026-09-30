<p>The malicious uploads detection is a <a href="/waf/concepts/#detection-versus-mitigation">traffic detection</a> that scans files and other content uploaded to your application for malware.</p>
<p>When you turn on this detection, the WAF inspects incoming uploads and checks them for malicious signatures. The scan results are available as <a href="#content-scanning-fields">fields</a> you can use in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to act on requests containing malicious content.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15497.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Once you turn on this detection, Cloudflare inspects all incoming traffic and identifies <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15498.md")
</div> automatically.
<p>When Cloudflare detects one or more content objects in a request, it sends them to an antivirus (AV) scanner for analysis. The AV scanner is the same one used in <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">Cloudflare Zero Trust</a>.</p>
<p>Based on the scan results, the detection populates <a href="#content-scanning-fields">fields</a> you can reference in rule expressions. For example, you can create a rule to block requests with malicious files, or a more specific rule that also matches on file size, file type, or URI path.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15496.md")
</aside>
<h2 id="what-is-a-content-object">What is a content object?</h2>
<p>A content object is a file or binary payload in a request that Cloudflare identifies as scannable content. The malicious uploads detection uses heuristics to find content objects automatically, without relying on the request's <code>Content-Type</code> header (since this header can be manipulated).</p>
<p>The following content types are excluded from scanning: <code>text/html</code>, <code>text/x-shellscript</code>, <code>application/json</code>, <code>text/csv</code>, and <code>text/xml</code>. All other detected content is treated as a content object. Common examples include:</p>
<ul>
<li>Executable files (for example, <code>.exe</code>, <code>.bat</code>, <code>.dll</code>, and <code>.wasm</code>)</li>
<li>Documents (for example, <code>.doc</code>, <code>.docx</code>, <code>.pdf</code>, <code>.ppt</code>, and <code>.xls</code>)</li>
<li>Compressed files (for example, <code>.gz</code>, <code>.zip</code>, and <code>.rar</code>)</li>
<li>Image files (for example, <code>.jpg</code>, <code>.png</code>, <code>.gif</code>, <code>.webp</code>, and <code>.tif</code>)</li>
<li>Video and audio files</li>
</ul>
<p>If Cloudflare detects a malicious object but cannot determine its exact content type, it reports the object as <code>application/octet-stream</code>.</p>
<h2 id="scanned-content">Scanned content</h2>
<p>Content scanning can check the following content objects for malicious content:</p>
<ul>
<li>Uploaded files in a request</li>
<li>Portions of the request body for multipart requests encoded as <code>multipart/form-data</code> or <code>multipart/mixed</code></li>
<li>Specific JSON properties in the request body (containing, for example, files encoded in Base64) according to the <a href="#custom-scan-expressions">custom scan expressions</a> you provide</li>
</ul>
<p>All content objects in an incoming request will be checked, namely for requests with multiple uploaded files (for example, a submitted HTML form with several file inputs).</p>
<p>The content scanner will fully check content objects with a size up to 50 MB. For larger content objects, the scanner will analyze the first 50 MB and provide scan results based on that portion of the object.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes-1">Notes</h3>
@markup("md", "content/.markup/bodies/15495.md")
</aside>
<h2 id="custom-scan-expressions">Custom scan expressions</h2>
<p>Sometimes, you may want to specify where to find the content objects, such as when the content is a Base64-encoded string within a JSON payload. For example:</p>
<pre><code class="language-json">{ &quot;file&quot;: &quot;&lt;BASE64_ENCODED_STRING&gt;&quot; }&#10;</code></pre>
<p>In these situations, configure a custom scan expression to tell the content scanner where to find the content objects. For more information, refer to <a href="/waf/detections/malicious-uploads/get-started/#4-optional-configure-a-custom-scan-expression">Configure a custom scan expression</a>.</p>
<p>For more information and additional examples of looking up fields in nested JSON payloads, refer to the <a href="/ruleset-engine/rules-language/functions/#lookup_json_string"><code>lookup_json_string()</code></a> function documentation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15494.md")
</aside>
<h2 id="content-scanning-fields">Content scanning fields</h2>
<p>When content scanning is enabled, you can use the following fields in WAF rules:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Has content object <br/> [<code>cf.waf.content_scan.has_obj</code>][1] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the request contains at least one content object.</td>
</tr>
<tr>
<td>Has malicious content object <br/> [<code>cf.waf.content_scan.has_malicious_obj</code>][2] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the request contains at least one malicious content object.</td>
</tr>
<tr>
<td>Number of malicious content objects <br/> [<code>cf.waf.content_scan.num_malicious_obj</code>][3] <br/> <span class="nb-type">Integer</span></td>
<td>The number of malicious content objects detected in the request (zero or greater).</td>
</tr>
<tr>
<td>Content scan has failed <br/> [<code>cf.waf.content_scan.has_failed</code>][4] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the file scanner was unable to scan any of the content objects detected in the request.</td>
</tr>
<tr>
<td>Number of content objects <br/> [<code>cf.waf.content_scan.num_obj</code>][5] <br/> <span class="nb-type">Integer</span></td>
<td>The number of content objects detected in the request (zero or greater).</td>
</tr>
<tr>
<td>Content object size <br/> [<code>cf.waf.content_scan.obj_sizes</code>][6] <br/> <span class="nb-type">Array&lt;Integer&gt;</span></td>
<td>An array of file sizes in bytes, in the order the content objects were detected in the request.</td>
</tr>
<tr>
<td>Content object type <br/> [<code>cf.waf.content_scan.obj_types</code>][7] <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>An array of file types in the order the content objects were detected in the request.</td>
</tr>
<tr>
<td>Content object result <br/> [<code>cf.waf.content_scan.obj_results</code>][8] <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>An array of scan results in the order the content objects were detected in the request. <br/> Possible values: <code>clean</code>, <code>suspicious</code>, <code>infected</code>, and <code>not scanned</code>.</td>
</tr>
</tbody>
</table>
<p>For examples of rule expressions using these fields, refer to <a href="/waf/detections/malicious-uploads/example-rules/">Example rules</a>.</p>
