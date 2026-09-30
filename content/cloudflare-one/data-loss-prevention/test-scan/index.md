<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4891.md")
</aside>
<p>Use Test scan to check how Cloudflare Data Loss Prevention (DLP) evaluates sample content before you apply a profile to production traffic. You can paste text, upload a file, or upload an HTTP Archive (HAR) file, then review which profiles and detection entries match.</p>
<p>Antivirus scans run as if the content were live traffic. When the scanner detects an image, Optical Character Recognition (OCR) runs even if no profile has OCR turned on, and the extracted text appears in the results.</p>
<p><strong>Content is scanned in real time and never stored.</strong></p>
<p>Content goes directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created.</p>
<h2 id="when-to-use-test-scan">When to use Test scan</h2>
<p>Use this tool to:</p>
<ul>
<li>Check whether a new or updated <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">detection entry</a> matches the content you expect.</li>
<li>Compare sample content against one or more <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> before using them in production.</li>
<li>Investigate false positives and missed detections by reviewing confidence levels, match context, and proximity keywords.</li>
<li>Confirm how DLP identifies a file and review its antivirus and OCR results.</li>
</ul>
<h2 id="run-a-test-scan">Run a test scan</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4892.md")
</div>
<h2 id="review-scan-results">Review scan results</h2>
<p>Depending on the input and scan result, the results can include the following sections:</p>
<table>
<thead>
<tr>
<th>Section</th>
<th>What it shows</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Summary</strong></td>
<td>The number of profiles matched and files scanned, and the overall antivirus status.</td>
</tr>
<tr>
<td><strong>File metadata</strong></td>
<td>The detected file name, size, MIME type, extension, and file categories.</td>
</tr>
<tr>
<td><strong>Antivirus results</strong></td>
<td>Whether each file is clean, suspicious, infected, or was not scanned, along with its SHA-256 hash. Infected files include available malware details.</td>
</tr>
<tr>
<td><strong>OCR results</strong></td>
<td>The text that OCR extracted from each image.</td>
</tr>
<tr>
<td><strong>Profile matches</strong></td>
<td>The profiles, detection entries, data classes, data tags, and sensitivity levels that matched.</td>
</tr>
<tr>
<td><strong>Match contexts</strong></td>
<td>The matched content, confidence level, and proximity keywords that increased or decreased confidence.</td>
</tr>
<tr>
<td><strong>JSON</strong></td>
<td>The complete scanner response, which you can download for further analysis.</td>
</tr>
</tbody>
</table>
<p>To save the complete response as <code>dlp-scan-results.json</code>, open <strong>JSON</strong> and select <strong>Download</strong>. The file can contain sample payloads and match context. Store and share it as sensitive data.</p>
<h2 id="example">Example</h2>
<p>A Gateway policy that uses a custom profile is not blocking a spreadsheet that contains credit card numbers. Use a test scan to find out whether the profile or the policy is responsible.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4893.md")
</div>
<h2 id="troubleshoot-scan-results">Troubleshoot scan results</h2>
<h3 id="expected-content-does-not-match">Expected content does not match</h3>
<p>Confirm that you selected the intended profile and that the profile contains the expected detection entries. A detection may not appear when the content does not meet the entry's matching requirements, when the profile <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#match-count">match count</a> is greater than the number of matches in the sample, or when the detection is below the profile's <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence threshold</a>.</p>
<h3 id="test-scan-matches-content-that-should-not-match">Test scan matches content that should not match</h3>
<p>Raise the profile's <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence threshold</a> so that DLP only triggers on higher confidence detections, or increase the <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#match-count">match count</a> so that a single incidental value does not trigger the profile. For custom entries, narrow the regular expression or dataset.</p>
<p><a href="/cloudflare-one/data-loss-prevention/dlp-settings/#ai-context-analysis">AI context analysis</a> can also reduce false positives in production, but it only supports Gateway HTTP and HTTPS traffic.</p>
<p>If a profile behaves correctly here but blocks legitimate traffic in production, the policy is likely too broad. Refer to <a href="/cloudflare-one/data-loss-prevention/troubleshoot-dlp/">Troubleshoot DLP</a>.</p>
<h3 id="ocr-extracted-text-but-no-entries-matched">OCR extracted text but no entries matched</h3>
<p>OCR runs on images, but DLP only matches the extracted text against profiles that have OCR turned on. If <strong>OCR results</strong> shows the text you expect and no entry triggered, OCR is turned off for the profile you selected.</p>
<p>To apply OCR to every profile, turn on <a href="/cloudflare-one/data-loss-prevention/dlp-settings/#optical-character-recognition-ocr">OCR in DLP settings</a>. You can also turn on OCR for an <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#optical-character-recognition-ocr">individual profile</a>, though profile-level OCR is deprecated.</p>
<h3 id="test-scan-matches-but-gateway-does-not">Test scan matches but Gateway does not</h3>
<p>If the scan detects the content but your Gateway policy does not, the selected profile can detect the sample under Test scan settings. This does not confirm that Gateway can decrypt or inspect the traffic in the same way. Check the Gateway policy, traffic path, TLS decryption, and supported file types. For more information, refer to <a href="/cloudflare-one/data-loss-prevention/troubleshoot-dlp/">Troubleshoot DLP</a>.</p>
<h3 id="a-scan-returns-an-error">A scan returns an error</h3>
<p>For file uploads, confirm that the file is 10 MB or smaller. For HAR files, confirm that the file contains valid HAR data. If the scanner is temporarily unavailable, wait and run the scan again.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>AI prompt profiles are not supported.</strong></li>
<li>Changes to your DLP configuration can take up to two minutes to take effect in a test scan. After you update a profile, detection entry, or data class, wait before testing.</li>
<li>Profile detection is validated, but Gateway policy conditions and actions are not. To verify that a complete policy allows, blocks, or logs traffic as expected, <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#3-test-dlp-policy">test the DLP policy with Gateway traffic</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4890.md")
</aside>
