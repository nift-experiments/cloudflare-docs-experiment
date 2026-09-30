<p>Profile settings control detection behavior for an individual DLP profile. You configure these settings when you <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">build a custom profile</a> or edit an existing <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined</a> or custom profile.</p>
<p>Profile settings are distinct from <a href="/cloudflare-one/data-loss-prevention/dlp-settings/">DLP settings</a>, which are account-level settings that apply across all profiles and policies.</p>
<h2 id="edit-profile-settings">Edit profile settings</h2>
<p>To edit profile settings for an existing predefined or custom DLP profile:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Choose a profile, then select <strong>Edit</strong>.</li>
<li>In <strong>Settings</strong>, configure the <a href="#available-settings">settings</a> for your profile.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<h2 id="available-settings">Available settings</h2>
<p>The following advanced detection settings are available for predefined and custom DLP profiles.</p>
<h3 id="match-count">Match count</h3>
<p>Match count sets a minimum threshold for the number of detections required to trigger an action. DLP does not block or log content until the detection count reaches this threshold.</p>
<p>For example, if you set a match count of <code>10</code>, DLP takes action when it finds 10 or more matches in a single file or HTTP body. Matches do not have to be unique — the same credit card number appearing 10 times counts as 10 matches.</p>
<h3 id="optical-character-recognition-ocr">Optical Character Recognition (OCR)</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/4902.md")
</aside>
<p>Optical Character Recognition (OCR) extracts and analyzes text within image files. When enabled, DLP can detect sensitive data within images that users upload or download.</p>
<p>OCR supports scanning <code>.jpg</code>/<code>.jpeg</code> and <code>.png</code> files between 4 KB and 1 MB in size. Text is encoded in UTF-8 format, including support for non-Latin characters.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-settings/#optical-character-recognition-ocr">DLP settings</a>.</p>
<h3 id="ai-context-analysis-ai-context-analysis">AI context analysis </h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="deprecation-notice-1">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/4901.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4900.md")
</aside>
<p>AI context analysis uses a machine learning model to evaluate the surrounding context of a detection and adjust its confidence level. The model examines nearby text to determine whether a pattern match is likely to be genuine sensitive data or a false positive.</p>
<p>For example, a 16-digit number that matches a credit card pattern may receive a lower confidence score if it appears in a context where credit card numbers are unlikely (such as a product SKU list). Conversely, the same number appearing near terms like &quot;payment&quot; or &quot;billing&quot; would receive a higher confidence score. DLP logs matches that meet or exceed your configured <a href="#confidence-thresholds">confidence threshold</a>.</p>
<p>For full documentation on AI context analysis, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-settings/#ai-context-analysis">DLP settings</a>.</p>
<h3 id="confidence-thresholds">Confidence thresholds</h3>
<p>Confidence thresholds indicate how confident Cloudflare DLP is in a detection. DLP determines the confidence level by inspecting the content for proximity keywords — related terms that appear near the detected data. For example, the word &quot;SSN&quot; appearing near a 9-digit number increases confidence that the number is a Social Security number.</p>
<p>When you set a confidence threshold on a profile, DLP only triggers on detections at that level or higher:</p>
<ul>
<li><strong>Low</strong> (default) — Based on regular expressions with few proximity keywords. This is the most inclusive setting, with high tolerance for false positives</li>
<li><strong>Medium</strong> — Applies additional validations, to filter out low confidence detections. This setting has a medium tolerance for false positives.</li>
<li><strong>Medium</strong> — Applies additional validations to filter out low confidence detections. This setting has a medium tolerance for false positives.</li>
</ul>
<p>Confidence threshold is set on the DLP profile. Not all detection entries support confidence thresholds — when you select a threshold in the dashboard, entries that support confidence scoring display their current level. Entries without a displayed confidence level either do not support this feature or use detection methods (such as exact match) where confidence scoring does not apply.</p>
<p>To change the confidence threshold of a DLP profile:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Select the profile, then select <strong>Edit</strong>.</li>
<li>In <strong>Settings</strong> &gt; <strong>Confidence threshold</strong>, choose a new confidence threshold from the dropdown menu.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<h2 id="gateway-detections">Gateway detections</h2>
<p>For inline detections in Gateway, you can log lower-confidence matches while blocking only high-confidence detections. This approach requires two HTTP policies with different DLP profiles:</p>
<ol>
<li>A Low or Medium confidence profile with an Allow action — logs the detection without blocking.</li>
<li>A High confidence profile with a Block action — blocks the request.</li>
</ol>
<p>For example:</p>
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
<td>DLP Profile</td>
<td>in</td>
<td><em>Low Confidence Detections</em></td>
<td>Allow</td>
</tr>
</tbody>
</table>
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
<td>DLP Profile</td>
<td>in</td>
<td><em>Medium Confidence Detections</em></td>
<td>Allow</td>
</tr>
</tbody>
</table>
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
<td>DLP Profile</td>
<td>in</td>
<td><em>High Confidence Detections</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
