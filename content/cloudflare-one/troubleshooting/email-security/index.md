<p>Review common troubleshooting scenarios for Cloudflare Email Security.</p>
<h2 id="email-headers-and-attributes">Email headers and attributes</h2>
<p>Email Security identifies threats using detections that result in a final disposition. You can inspect email headers to understand why a specific disposition was applied.</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CUSTOM_BLOCK_LIST</code></td>
<td>Matches a value defined in your custom block list.</td>
</tr>
<tr>
<td><code>NEW_DOMAIN_SENDER</code></td>
<td>The email was sent from a newly registered domain.</td>
</tr>
<tr>
<td><code>NEW_DOMAIN_LINK</code></td>
<td>The email contains links to a newly registered domain.</td>
</tr>
<tr>
<td><code>ENCRYPTED</code></td>
<td>The email message is encrypted.</td>
</tr>
<tr>
<td><code>BEC</code></td>
<td>The sender address is in your <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a>.</td>
</tr>
</tbody>
</table>
<h2 id="detections-and-reclassification">Detections and reclassification</h2>
<h3 id="handle-a-false-positive">Handle a false positive</h3>
A false positive occurs when a legitimate email is incorrectly flagged as malicious or spam. 
<p><strong>Solution</strong>:</p>
<ol>
<li>In the Email Security dashboard, go to <strong>Investigation</strong>.</li>
<li>Find the email and select <strong>Submit for reclassification</strong>.</li>
<li>Choose the correct disposition (for example, <code>Clean</code>).</li>
<li>To prevent future blocks, add the sender to your <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">Acceptable Senders</a> list.</li>
</ol>
<h3 id="handle-a-false-negative">Handle a false negative</h3>
A false negative occurs when a malicious email is not detected by Email Security.
<p><strong>Solution</strong>:</p>
<ol>
<li>Ensure the email actually passed through Email Security by checking for the <code>X-CFEmailSecurity-Disposition</code> header.</li>
<li>Submit the email for reclassification in the dashboard. This is the preferred method for reporting missed detections.</li>
</ol>
<h2 id="authentication-errors">Authentication errors</h2>
<h3 id="dmarc-failures">DMARC failures</h3>
Email Security may mark an email as **SPAM** if it fails DMARC authentication and the sending domain has a `p=reject` or `p=quarantine` policy.
<p><strong>Solution</strong>:</p>
<ul>
<li>Ask the sender to fix their DMARC/SPF/DKIM records.</li>
<li>Configure an <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">Acceptable Sender</a> entry to suppress the failure for that specific sender.</li>
</ul>
<h2 id="delivery-issues">Delivery issues</h2>
<h3 id="emails-are-delayed-or-not-arriving">Emails are delayed or not arriving</h3>
If emails are not being delivered or are arriving with significant latency:
<ol>
<li><strong>Check MX records</strong>: Ensure your <a href="/cloudflare-one/email-security/setup/">MX records</a> are correctly configured and pointing to Cloudflare.</li>
<li><strong>Verify connectivity</strong>: From your sending mail server, verify you can connect to Cloudflare's mailstream endpoints on port 25.</li>
<li><strong>Check outbound logs</strong>: In the dashboard, use the <strong>Mail Trace</strong> feature to confirm if Email Security successfully delivered the email to your downstream mail server (for example, Google Workspace or Microsoft 365).</li>
</ol>
<hr />
<h2 id="more-email-security-resources">More Email Security resources</h2>
<p>For more information, refer to the full Email Security documentation.</p>
<p><a class="nb-link-button" href="/cloudflare-one/email-security/troubleshooting/">Email Security troubleshooting ❯</a></p>
