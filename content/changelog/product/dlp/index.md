---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/dlp/
  description: '2026-09-14'
  full_title: dlp changelog | Cloudflare Docs
  head_html: <title>dlp changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-14"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/dlp/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="dlp changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-14"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/dlp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/dlp/#page","headline":"dlp changelog | Cloudflare Docs","description":"2026-09-14","url":"https://developers.cloudflare.com/changelog/product/dlp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/dlp/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="discover-where-sensitive-data-goes-before-you-create-a-data-loss-prevention-policy"><a href="/changelog/post/2026-09-14-passive-detection/">Discover where sensitive data goes before you create a Data Loss Prevention policy</a></h2>
<p><em>2026-09-14</em></p>
<p><strong>Passive Detection</strong> for <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a> lets you learn from your Gateway traffic before deciding what to log or block. Discover the sensitive data types in sampled traffic, explore their destinations, and use the findings to build policies around your organization's needs.</p>
<p>The dashboard brings together detections from sampled HTTP request and response bodies. Select an entry to follow its detections over time, review destinations, and check policy coverage. You do not need a Gateway DLP policy to get these insights, and existing Gateway policies continue to apply.</p>
<p><img src="/assets/upstream/images/changelog/dlp/passive-detection.gif" alt="Passive Detection dashboard showing detection totals, data type distribution, policy coverage, and detection entries" /></p>
<p>Passive Detection is generally available. The detection entries available to your account depend on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>To get started, refer to the <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection documentation</a>.</p>


<h2 id="test-data-loss-prevention-profiles-without-sending-traffic-through-gateway"><a href="/changelog/post/2026-08-21-dlp-test-scan/">Test Data Loss Prevention profiles without sending traffic through Gateway</a></h2>
<p><em>2026-08-21</em></p>
<p><strong>Test scan</strong> lets you check how <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.</p>
<p><img src="/assets/upstream/images/changelog/dlp/dlp-test-scan.gif" alt="Test scan results showing matched profiles, detection entries, and match context" /></p>
<p>Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.</p>
<p>Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan documentation</a>.</p>


<h2 id="source-code-detection-improvements"><a href="/changelog/post/2026-07-10-source-code-detection-improvements/">Source code detection improvements</a></h2>
<p><em>2026-07-10</em></p>
<p>Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.</p>
<p>Source code detection requires a minimum of 500 characters to evaluate a file. Files below this threshold are not flagged to reduce noise. This threshold filters out small fragments that lack enough context for reliable classification.</p>
<p>Enable and set <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence levels</a> to tune match sensitivity. A higher confidence level reduces false positives by requiring stronger signals that the content is truly source code. A lower confidence level catches more files at the cost of additional noise.</p>
<p>Source code detection applies to standalone source code files in <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a>. It does not detect source code embedded within other file types or payloads, such as <code>.docx</code> files or chat messages.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">Source Code predefined profiles</a>.</p>


<h2 id="define-custom-topics-for-ai-prompt-protection"><a href="/changelog/post/2026-06-11-custom-ai-prompt-topics/">Define custom topics for AI prompt protection</a></h2>
<p><em>2026-06-11</em></p>
<p>You can now define custom topics for AI prompt protection. Predefined <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a> cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.</p>
<p>You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom wordlist or pattern entry</a> instead.</p>
<p>Custom topics run through the same <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a> path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.</p>
<h4 id="2026-06-11-custom-ai-prompt-topics-create-a-custom-ai-prompt-topic">Create a custom AI prompt topic</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>Select <strong>AI prompt topics</strong>, then select <strong>Custom Prompt Topic</strong>.</li>
<li>Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.</li>
<li>Add this detection entry to an existing DLP profile, or <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">create a new DLP profile</a>.</li>
<li>Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17715.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>


<h2 id="classify-sensitive-content-with-data-classification"><a href="/changelog/post/2026-04-30-data-classification/">Classify sensitive content with Data Classification</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare DLP now includes <strong>Data Classification</strong>, which lets administrators organize and label sensitive content using labels, templates, and reusable data classes.</p>
<p>With Data Classification, administrators can define labels such as sensitivity schemas and levels, and data tag groups and tags. Administrators can also build from Cloudflare-managed templates and create reusable data classes that combine detection entries, other data classes, sensitivity levels, and data tags.</p>
<p>You can then use those classifications in custom DLP profiles to identify the severity of sensitive content, understand where it exists, and apply that logic consistently across DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>.</p>


<h2 id="new-predefined-detection-entries-are-available"><a href="/changelog/post/2026-04-30-standalone-predefined-detection-entries/">New predefined detection entries are available</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare DLP now includes new predefined detection entries.</p>
<p>The expanded catalog includes detections for specific credential types, webhooks, addresses, tax identifiers, national IDs, financial data, and crypto wallets.</p>
<p>Examples include <code>GitHub PAT</code>, <code>OpenAI API Key</code>, <code>Slack Webhook</code>, <code>Discord Webhook</code>, <code>US Physical Address</code>, and <code>Bitcoin Wallet</code>.</p>
<p>For the full list, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/">Predefined detection entries</a>.</p>


<h2 id="create-and-manage-dlp-detection-entries-outside-of-profiles"><a href="/changelog/post/2026-04-28-detection-entries-outside-profiles/">Create and manage DLP detection entries outside of profiles</a></h2>
<p><em>2026-04-28</em></p>
<p>You can now create, view, and manage DLP detection entries outside of profiles.</p>
<p>Detection entries are no longer hidden inside individual profiles. Administrators can manage detection entries directly from the <strong>Detection entries</strong> section and use them in custom DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">Configure detection entries</a>.</p>


<h2 id="detect-pii-records-with-a-new-predefined-dlp-profile"><a href="/changelog/post/2026-04-28-pii-record-profile/">Detect PII records with a new predefined DLP profile</a></h2>
<p><em>2026-04-28</em></p>
<p>Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: <strong>Personally Identifiable Information (PII) Record</strong>.</p>
<p>Most predefined and custom DLP profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.</p>
<p>Detection entries included in the profile:</p>
<ul>
<li>AU Passport Number</li>
<li>American Express Card Number</li>
<li>Diners Club Card Number</li>
<li>US Driver's License Number</li>
<li>Email Address</li>
<li>Full Name</li>
<li>US Mailing Address</li>
<li>Mastercard Card Number</li>
<li>US Individual Tax Identification Number (ITIN)</li>
<li>US Passport Number</li>
<li>US Phone Number</li>
<li>Union Pay Card Number</li>
<li>United States SSN Numeric Detection</li>
<li>Visa Card Number</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>


<h2 id="dlp-account-level-settings"><a href="/changelog/post/2025-04-14-account-level-dlp-settings/">DLP account-level settings</a></h2>
<p><em>2026-04-14T12:00:00+00:00</em></p>
<p><strong>Account-level DLP settings are now available</strong> in Cloudflare One. You can now configure advanced DLP settings at the account level, including OCR, AI context analysis, and payload masking. This provides consistent enforcement across all DLP profiles and simplifies configuration management.</p>
<p>Key changes:</p>
<ul>
<li><strong>Consistent enforcement</strong>: Settings configured at the account level apply to all DLP profiles</li>
<li><strong>Simplified migration</strong>: Settings enabled on any profile are automatically migrated to account level</li>
<li><strong>Deprecation notice</strong>: Profile-level advanced settings will be deprecated in a future release</li>
</ul>
<p><strong>Migration details:</strong></p>
<p>During the migration period, if a setting is enabled on any profile, it will automatically be enabled at the account level. This means profiles that previously had a setting disabled may now have it enabled if another profile in the account had it enabled.</p>
<p>Settings are evaluated using OR logic - a setting is enabled if it is turned on at either the account level or the profile level. However, profile-level settings cannot be enabled when the account-level setting is off.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/dlp-settings/">DLP settings documentation</a>.</p>


<h2 id="detect-cloudflare-api-tokens-with-dlp"><a href="/changelog/post/2026-04-14-cloudflare-api-token-detections/">Detect Cloudflare API tokens with DLP</a></h2>
<p><em>2026-04-14</em></p>
<p>The <strong>Credentials and Secrets</strong> DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:</p>
<table>
<thead>
<tr>
<th>Entry name</th>
<th>Token prefix</th>
<th>Detects</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare User API Key</td>
<td><code>cfk_</code></td>
<td>User-scoped API keys</td>
</tr>
<tr>
<td>Cloudflare User API Token</td>
<td><code>cfut_</code></td>
<td>User-scoped API tokens</td>
</tr>
<tr>
<td>Cloudflare Account Owned API Token</td>
<td><code>cfat_</code></td>
<td>Account-scoped API tokens</td>
</tr>
</tbody>
</table>
<p>These detections target the new <a href="/fundamentals/api/get-started/token-formats/">Cloudflare API credential format</a>, which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as <code>Authorization: Bearer</code> headers is required.</p>
<p>Credentials generated before this format change will not be matched by these entries.</p>
<h4 id="2026-04-14-cloudflare-api-token-detections-how-to-enable-cloudflare-api-token-detections">How to enable Cloudflare API token detections</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>DLP</strong> &gt; <strong>DLP Profiles</strong>.</li>
<li>Select the <strong>Credentials and Secrets</strong> profile.</li>
<li>Turn on one or more of the new Cloudflare API token entries.</li>
<li>Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.</li>
</ol>
<p>Example policy:</p>
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
<td><em>Credentials and Secrets</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>You can also enable individual entries to scope detection to specific credential types — for example, enabling <strong>Account Owned API Token</strong> detection without enabling <strong>User API Key</strong> detection.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>


<h2 id="configure-how-sensitive-data-appears-in-dlp-payload-logs"><a href="/changelog/post/2026-04-14-configurable-payload-log-masking/">Configure how sensitive data appears in DLP payload logs</a></h2>
<p><em>2026-04-14</em></p>
<p>You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong> and find the <strong>Payload log masking</strong> card.</p>
<p>Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:</p>
<ul>
<li><strong>Full Mask (default):</strong> Masks the match while preserving character count and visual formatting (for example, <code>***-**-****</code> for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.</li>
<li><strong>Partial Mask:</strong> Reveals 25% of the matched content while masking the remainder (for example, <code>***-**-6789</code>).</li>
<li><strong>Clear Text:</strong> Stores the full, unmasked violation for deep investigation (for example, <code>123-45-6789</code>).</li>
</ul>
<p><strong>Important:</strong> The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.</p>
<p><strong>Applies to all enabled detections:</strong> When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">DLP logging options</a>.</p>


<h2 id="streaming-zip-file-scanning-removes-per-file-size-limits"><a href="/changelog/post/2026-03-26-streaming-zip-handler/">Streaming ZIP file scanning removes per-file size limits</a></h2>
<p><em>2026-03-26</em></p>
<p>DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.</p>
<p>Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.</p>
<p>This improvement is automatic — no configuration changes are required.</p>


<h2 id="detect-and-sanitize-har-files"><a href="/changelog/post/2026-03-25-har-file-detection-and-sanitization/">Detect and sanitize HAR files</a></h2>
<p><em>2026-03-25</em></p>
<p>HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.</p>
<p>Gateway now includes a predefined DLP profile called <strong>Unsanitized HAR</strong> that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.</p>
<h4 id="2026-03-25-har-file-detection-and-sanitization-how-to-configure-a-har-file-policy">How to configure a HAR file policy</h4>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to  <strong>Zero Trust</strong> &gt;  <strong>Traffic policies</strong> &gt; <strong>Firewall Policies</strong> &gt; <strong>HTTP</strong> and create a new HTTP policy using the <strong>DLP Profile</strong> selector:</p>
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
<td><em>Unsanitized HAR</em></td>
<td></td>
</tr>
</tbody>
</table>
<p>Then choose one of the following actions:</p>
<ul>
<li><strong>Block</strong>: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.</li>
<li><strong>Block</strong> with <strong>Gateway Redirect</strong>: Intercepts the upload and redirects the user to <code>https://har-sanitizer.pages.dev/</code>, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.</li>
</ul>
<h4 id="2026-03-25-har-file-detection-and-sanitization-sanitized-har-recognition">Sanitized HAR recognition</h4>
<p>HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.</p>
<h4 id="2026-03-25-har-file-detection-and-sanitization-visibility-in-gateway-logs">Visibility in Gateway logs</h4>
<p>Gateway logs will reflect whether a detected HAR file was classified as <strong>Unsanitized</strong> or <strong>Sanitized</strong>, giving your security team full visibility into HAR file activity across your organization.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>


<h2 id="expanded-file-type-controls-for-executables-and-disk-images"><a href="/changelog/post/2025-10-01-new-file-type-support/">Expanded File Type Controls for Executables and Disk Images</a></h2>
<p><em>2025-10-01</em></p>
<p>You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.</p>
<p>We have expanded Gateway's file type controls to include:</p>
<ul>
<li>Apple Disk Image (dmg)</li>
<li>Microsoft Software Installer (msix, appx)</li>
<li>Apple Software Package (pkg)</li>
</ul>
<p>You can find these new options within the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types"><em>Upload File Types</em> and <em>Download File Types</em> selectors</a> when creating or editing an HTTP policy. The file types are categorized as follows:</p>
<ul>
<li><strong>System</strong>: <em>Apple Disk Image (dmg)</em></li>
<li><strong>Executable</strong>: <em>Microsoft Software Installer (msix)</em>, <em>Microsoft Software Installer (appx)</em>, <em>Apple Software Package (pkg)</em></li>
</ul>
<p>To ensure these file types are blocked effectively, please note the following behaviors:</p>
<ul>
<li>DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.</li>
<li>MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type <em>Unscannable</em>. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.</li>
</ul>
<p>To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#supported-file-types">supported file types</a>.</p>


<h2 id="refine-dlp-scans-with-new-body-phase-selector"><a href="/changelog/post/2025-09-25-body-phase-selector/">Refine DLP Scans with New Body Phase Selector</a></h2>
<p><em>2025-09-25</em></p>
<p>You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.</p>
<p>In the Gateway HTTP policy builder, you will find a new selector called <em>Body Phase</em>. This allows you to define the direction of traffic the DLP engine will inspect:</p>
<ul>
<li><em>Request Body</em>: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.</li>
<li><em>Response Body</em>: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.</li>
</ul>
<p>For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the <strong>Body Phase</strong> to <em>Request Body</em>, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.</p>
<p>All policies without this selector will continue to scan both request and response bodies to ensure continued protection.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#body-phase">Gateway HTTP policy selectors</a>.</p>


<h2 id="new-dlp-topic-based-detection-entries-for-ai-prompt-protection"><a href="/changelog/post/2025-08-25-ai-prompt-protection/">New DLP topic based detection entries for AI prompt protection</a></h2>
<p><em>2025-08-25</em></p>
<p>You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.</p>
<ol>
<li><strong>Prompt Detection for AI Applications</strong></li>
</ol>
<p>DLP can now natively detect and inspect user prompts submitted to popular AI applications, including <strong>Google Gemini</strong>, <strong>ChatGPT</strong>, <strong>Claude</strong>, and <strong>Perplexity</strong>.</p>
<ol start="2">
<li><strong>Prompt Analysis and Topic Classification</strong></li>
</ol>
<p>Our DLP engine performs deep analysis on each prompt, applying <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">topic classification</a>. These topics are grouped into two evaluation categories:</p>
<pre tabindex="0"><code>    - **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.&#10;&#10;    - **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.&#10;</code></pre>
<p>To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.</p>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-detection-entry.png" alt="DLP" /></p>
<ol start="3">
<li>
<p><strong>Granular Guardrails</strong></p>
<p>You can now build guardrails using Gateway HTTP policies with <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a>. Apply a DLP profile containing an <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topic detection</a> to individual AI applications (for example, <code>ChatGPT</code>) and specific user actions (for example, <code>SendPrompt</code>) to block sensitive prompts.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-policy.png" alt="DLP" /></p>
<ol start="4">
<li>
<p><strong>Full Prompt Logging</strong></p>
<p>To aid in incident investigation, an optional setting in your Gateway policy allows you to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content">capture prompt logs</a> to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by <code>conversation_id</code>, allowing you to reconstruct the full context of an interaction that led to a policy violation.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-log.png" alt="DLP" /></p>
<p>AI prompt protection is now available in open beta. To learn more about it, read the <a href="https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging">blog</a> or refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>


<h2 id="new-detection-entry-type-document-matching-for-dlp"><a href="/changelog/post/2025-07-17-document-matching/">New detection entry type: Document Matching for DLP</a></h2>
<p><em>2025-07-17</em></p>
<p>You can now create <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries">document-based</a> detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.</p>
<p><img src="/assets/upstream/images/changelog/dlp/document-match.png" alt="DLP" /></p>
<p><strong>Key features and benefits:</strong></p>
<ul>
<li>
<p><strong>Upload documents, forms, or templates:</strong> Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.</p>
</li>
<li>
<p><strong>Granular control with similarity percentage:</strong> Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.</p>
</li>
<li>
<p><strong>Comprehensive coverage:</strong> Apply these document-based detection entries in:</p>
<ul>
<li>
<p><strong>Gateway policies:</strong> To inspect network traffic for sensitive documents as they are uploaded or shared.</p>
</li>
<li>
<p><strong>CASB (Cloud Access Security Broker):</strong> To scan files stored in cloud applications for sensitive documents at rest.</p>
</li>
</ul>
</li>
<li>
<p><strong>Identify sensitive data:</strong> This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.</p>
</li>
</ul>
<p>Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.</p>


<h2 id="data-security-analytics-in-the-zero-trust-dashboard"><a href="/changelog/post/cf1-data-security-analytics-v1/">Data Security Analytics in the Zero Trust dashboard</a></h2>
<p><em>2025-06-23T09:00:00+00:00</em></p>
<p>Zero Trust now includes <strong>Data security analytics</strong>, providing you with unprecedented visibility into your organization sensitive data.</p>
<p>The new dashboard includes:</p>
<ul>
<li>
<p><strong>Sensitive Data Movement Over Time:</strong></p>
<ul>
<li>See patterns and trends in how sensitive data moves across your environment. This helps understand where data is flowing and identify common paths.</li>
</ul>
</li>
<li>
<p><strong>Sensitive Data at Rest in SaaS &amp; Cloud:</strong></p>
<ul>
<li>View an inventory of sensitive data stored within your corporate SaaS applications (for example, Google Drive, Microsoft 365) and cloud accounts (such as AWS S3).</li>
</ul>
</li>
<li>
<p><strong>DLP Policy Activity:</strong></p>
<ul>
<li>Identify which of your Data Loss Prevention (DLP) policies are being triggered most often.</li>
<li>See which specific users are responsible for triggering DLP policies.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-data-security-analytics-v1.png" alt="Data Security Analytics" /></p>
<p>To access the new dashboard, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong> on the sidebar.</p>


<h2 id="case-sensitive-custom-word-lists"><a href="/changelog/post/2025-05-12-case-sensitive-cwl/">Case Sensitive Custom Word Lists</a></h2>
<p><em>2025-05-12</em></p>
<p>You can now configure <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom word lists</a> to enforce case sensitivity. This setting supports flexibility where needed and aims to reduce false positives where letter casing is critical.</p>
<p><img src="/assets/upstream/images/changelog/dlp/case-sesitive-cwl.png" alt="dlp" /></p>


<h2 id="send-forensic-copies-to-storage-without-dlp-profiles"><a href="/changelog/post/2025-05-07-forensic-copy-update/">Send forensic copies to storage without DLP profiles</a></h2>
<p><em>2025-05-07</em></p>
<p>You can now <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination">send DLP forensic copies</a> to third-party storage for any HTTP policy with an <code>Allow</code> or <code>Block</code> action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.</p>
<p>By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.</p>
<p><img src="/assets/upstream/images/changelog/dlp/forensic-copies-for-all.png" alt="DLP" /></p>


<h2 id="new-predefined-detection-entry-for-icd-11"><a href="/changelog/post/2025-04-14-icd11-support/">New predefined detection entry for ICD-11</a></h2>
<p><em>2025-04-14</em></p>
<p>You now have access to the World Health Organization (WHO) 2025 edition of the <a href="https://www.who.int/news/item/14-02-2025-who-releases-2025-update-to-the-international-classification-of-diseases-%28icd-11%29">International Classification of Diseases 11th Revision (ICD-11)</a> as a predefined detection entry. The new dataset can be found in the <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#health-information">Health Information</a> predefined profile.</p>
<p>ICD-10 dataset remains available for use.</p>


<h2 id="block-files-that-are-password-protected-compressed-or-otherwise-unscannable"><a href="/changelog/post/2025-02-13-improvements-unscannable-files/">Block files that are password-protected, compressed, or otherwise unscannable.</a></h2>
<p><em>2025-02-03</em></p>
<p>Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.</p>
<p>These unscannable files are now matched with the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">Download and Upload File Types traffic selectors</a> for HTTP policies:</p>
<ul>
<li>Password-protected Microsoft Office document</li>
<li>Password-protected PDF</li>
<li>Password-protected ZIP archive</li>
<li>Unscannable ZIP archive</li>
</ul>
<p>To get started inspecting and modifying behavior based on these and other rules, refer to <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a>.</p>


<h2 id="detect-source-code-leaks-with-data-loss-prevention"><a href="/changelog/post/2025-01-03-source-code-confidence-level/">Detect source code leaks with Data Loss Prevention</a></h2>
<p><em>2025-01-20</em></p>
<p>You can now detect source code leaks with Data Loss Prevention (DLP) with predefined checks against common programming languages.</p>
<p>The following programming languages are validated with natural language processing (NLP).</p>
<ul>
<li>C</li>
<li>C++</li>
<li>C#</li>
<li>Go</li>
<li>Haskell</li>
<li>Java</li>
<li>JavaScript</li>
<li>Lua</li>
<li>Python</li>
<li>R</li>
<li>Rust</li>
<li>Swift</li>
</ul>
<p>DLP also supports confidence level for <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">source code profiles</a>.</p>
<p>For more details, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a>.</p>


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>



