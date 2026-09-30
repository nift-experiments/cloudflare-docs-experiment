<p>Data Loss Prevention allows you to capture, store, and view the data that triggered a specific DLP policy for use as forensic evidence. DLP offers three logging approaches, each suited to different needs:</p>
<table>
<thead>
<tr>
<th>Approach</th>
<th>What it captures</th>
<th>Encryption</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#log-the-payload-of-matched-rules">Payload logging</a></td>
<td>Redacted match + 75 bytes of surrounding context</td>
<td>Encrypted with your public key</td>
<td>All plans</td>
</tr>
<tr>
<td><a href="#log-generative-ai-prompt-content">AI prompt logging</a></td>
<td>Generative AI prompt topic, user prompt, and model response</td>
<td>Encrypted with your public key</td>
<td>All plans</td>
</tr>
<tr>
<td><a href="#send-dlp-forensic-copies-to-logpush-destination">Logpush forensic copies</a></td>
<td>Complete HTTP request (headers + body)</td>
<td>Encrypted in transit only (TLS)</td>
<td>Enterprise</td>
</tr>
</tbody>
</table>
<p>Users on all plans can log the <a href="#log-the-payload-of-matched-rules">payload</a> or <a href="#log-generative-ai-prompt-content">generative AI prompt content</a> of matched HTTP requests in their Cloudflare logs. Additionally, Enterprise users can <a href="#send-dlp-forensic-copies-to-logpush-destination">configure a Logpush job</a> to send copies of entire matched HTTP requests to storage destinations.</p>
<p>The data that triggers a DLP policy is stored in the body of the HTTP request — the part that carries content such as file uploads, form submissions, and chat messages. This body is referred to as the payload. Payload logging is especially useful when diagnosing the behavior of DLP policies. Since the values that triggered a rule may contain sensitive data, they are encrypted with a customer-provided public key so that only you can examine them later. The stored data will include a redacted version of the match, plus 75 bytes of additional context on both sides of the match.</p>
<h2 id="set-a-dlp-payload-encryption-public-key">Set a DLP payload encryption public key</h2>
<p>Before you begin logging DLP payloads, you will need to <a href="/cloudflare-one/data-loss-prevention/dlp-settings/#payload-encryption-key">set a DLP payload encryption public key</a>. DLP uses public-key encryption so that matched sensitive data is readable only by you — Cloudflare does not have access to your private key and cannot decrypt your logs.</p>
<p>You can also <a href="/cloudflare-one/data-loss-prevention/dlp-settings/#payload-log-masking">configure payload log masking</a> to control how DLP redacts sensitive data in logs.</p>
<h2 id="log-the-payload-of-matched-rules">Log the payload of matched rules</h2>
<p>DLP can log the payload of matched HTTP requests in your Cloudflare logs. Use payload logging to verify what content triggered a DLP detection — for example, to confirm whether a match was a real finding or a false positive.</p>
<h3 id="turn-on-payload-logging-for-a-dlp-policy">Turn on payload logging for a DLP policy</h3>
<p>You can enable payload logging for any Allow or Block HTTP policy that uses the <a href="/cloudflare-one/traffic-policies/http-policies/#dlp-profile"><em>DLP Profile</em></a> selector — the filter condition that matches traffic against your DLP detection profiles.</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Edit an existing Allow or Block DLP policy, or <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy">create a new policy</a>.</li>
<li>In the policy builder, scroll down to <strong>Configure policy settings</strong> and turn on <strong>Log the payload of matched rules</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Data Loss Prevention will now store a portion of the payload for HTTP requests that match this policy.</p>
<h3 id="view-payload-logs">View payload logs</h3>
<p>To view DLP payload logs:</p>
<ol>
<li>Go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>HTTP request logs</strong>.</li>
<li>Go to the DLP log you are interested in reviewing and expand the row.</li>
<li>Select <strong>Decrypt payload log</strong>.</li>
<li>Enter your private key and select <strong>Decrypt</strong>.</li>
</ol>
<p>You will see the <a href="/api/resources/zero_trust/subresources/dlp/subresources/profiles/methods/list/">ID of the matched DLP Profile</a> followed by the decrypted payload.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4904.md")
</aside>
<h3 id="report-false-and-true-positives-to-ai-context-analysis">Report false and true positives to AI context analysis</h3>
<p>When you have <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#ai-context-analysis">AI context analysis</a> turned on for a DLP profile, you can improve detection accuracy over time by reporting false and true positives. A false positive is a match that DLP flagged incorrectly (the content was not actually sensitive). A true positive confirms that DLP correctly identified sensitive data. These reports train the AI model to adjust its confidence threshold.</p>
<p>To report a DLP match payload as a false or true positive:</p>
<ol>
<li><a href="#view-payload-logs">Find and decrypt</a> the payload log you want to report.</li>
<li>In <strong>Log details</strong>, choose a detected context match.</li>
<li>In <strong>Context</strong>, select the redacted match data.</li>
<li>In <strong>Match details</strong>, choose whether you want to report the match as a false positive or a true positive.</li>
</ol>
<p>Based on your report, DLP's machine learning will adjust its confidence in future matches for the associated profile.</p>
<h3 id="data-privacy">Data privacy</h3>
<ul>
<li>All Cloudflare logs are encrypted at rest (encrypted while stored on disk). Encrypting the payload content adds a second layer of encryption for the matched values that triggered a DLP rule.</li>
<li>Cloudflare cannot decrypt encrypted payloads, since this operation requires your private key. Cloudflare staff will never ask for the private key.</li>
<li>By default, DLP uses Full Mask to redact alphanumeric characters in the matched pattern, replacing them with <code>*</code> while preserving the format. For example, <code>123-45-6789</code> becomes <code>***-**-****</code>. You can <a href="#configure-payload-log-masking">configure the masking level</a> to show partial or full matches if your incident response workflow requires more context.
<ul>
<li>You can define sensitive data with <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#exact-data-match-datasets">Exact Data Match (EDM)</a>. EDM match logs will redact your defined strings.</li>
</ul>
</li>
</ul>
<h2 id="log-generative-ai-prompt-content">Log generative AI prompt content</h2>
<p>DLP can detect and log the prompt topic sent to an AI tool.</p>
<h3 id="turn-on-ai-prompt-content-logging-for-a-dlp-policy">Turn on AI prompt content logging for a DLP policy</h3>
<p>You can enable AI prompt content logging for any Allow or Block HTTP policy that uses the <a href="/cloudflare-one/traffic-policies/http-policies/#application"><em>Application</em></a> selector with a supported <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">Application Granular Controls</a> application. This means your policy must target a specific AI application (such as ChatGPT) that Gateway can inspect at a granular level.</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Edit an existing Allow or Block DLP policy, or <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy">create a new policy</a>.</li>
<li>In the policy builder, scroll down to <strong>Configure policy settings</strong> and turn on <strong>Capture generative AI prompt content in logs</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Data Loss Prevention will now store the user prompt and AI model response for requests that match this policy.</p>
<h3 id="view-prompt-logs">View prompt logs</h3>
<p>To view generative AI prompt log details:</p>
<ol>
<li>Go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>HTTP request logs</strong>.</li>
<li>Go to the DLP log you are interested in reviewing and expand the row.</li>
<li>Select <strong>Decrypt payload log</strong>.</li>
<li>Enter your private key and select <strong>Decrypt</strong>.</li>
<li>In <strong>Summary</strong> &gt; <strong>GenAI prompt captured</strong>, select <strong>View prompt</strong>.</li>
</ol>
<p>Gateway logs will provide a summary of the conversation, including the topic and AI model used, and the user prompt and AI model's raw response if available. A text prompt must be present for DLP to capture the prompt.</p>
<h2 id="send-dlp-forensic-copies-to-logpush-destination">Send DLP forensic copies to Logpush destination</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4903.md")
</aside>
<p>Unlike payload logging (which stores encrypted excerpts of matched content), forensic copies send the complete, unaltered HTTP request — including all headers and the full body — to an external storage destination.</p>
<p>Gateway allows you to send copies of entire HTTP requests matched in HTTP Allow and Block policies to storage destinations configured in <a href="/logs/logpush/">Logpush</a> (Cloudflare's log delivery service), including third-party destinations. Forensic copies include unaltered payloads and headers which may include sensitive data. Logpush logs are encrypted in transit only, such as when sent as TLS traffic. Once the data reaches your storage destination, it is stored according to that destination's encryption policies — not encrypted by Cloudflare.</p>
<p>To set up the DLP Forensic Copy Logpush job:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt;<strong>Logs</strong>, and select <strong>Manage Logpush</strong>.</li>
<li>In Logpush, select <strong>Create a Logpush job</strong>.</li>
<li>Choose a <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a>.</li>
<li>In <strong>Configure logpush job</strong>, choose the <em>DLP forensic copies</em> dataset. Select <strong>Create Logpush job</strong>.</li>
<li>Return to <strong>Zero Trust</strong> and go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Edit an existing Allow or Block policy, or <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy">create a new policy</a>. Your policy does not need to include a DLP profile — any Gateway HTTP policy can send forensic copies.</li>
<li>In the policy builder, scroll down to <strong>Configure policy settings</strong> and turn on <strong>Send DLP forensic copies to storage</strong>.</li>
<li>Select a storage destination. Gateway will list any configured Logpush jobs or integrations that can receive HTTP requests.</li>
<li>Select <strong>Save policy</strong>.</li>
</ol>
<p>DLP will now send a copy of HTTP requests that match this policy to your Logpush destination.</p>
<p>Logpush supports up to four DLP Forensic Copy Logpush jobs per account. By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs. To send specific policy matches to specific jobs, configure <a href="/logs/logpush/logpush-job/filters/">Log filters</a>. If the request contains an archive file, DLP will only send up to 100 MB of uncompressed content to your configured storage.</p>
