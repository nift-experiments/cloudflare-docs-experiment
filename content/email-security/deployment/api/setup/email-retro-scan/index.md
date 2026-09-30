<p>Email Retro Scan allows you to scan up to 14 days of old messages in your Office 365 (O365) inboxes and check if your current email security solution missed any threats. Contact your account manager to enable this feature.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8519.md")
</aside>
<h2 id="scan-for-threats">Scan for threats</h2>
<p>To scan for threats in your Office 365 inbox:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email security</strong> &gt; <strong>Retro Scan</strong>.</li>
<li>Select <strong>Generate report</strong>.</li>
<li>Cloudflare needs authorization to access your O365 messages. Select <strong>Authenticate with Microsoft</strong>, and give Cloudflare the required permissions.</li>
<li>Back to Cloudflare dashboard, select <strong>Grant mail access</strong>. Then, select your account and give Cloudflare the required permissions.</li>
<li>Select <strong>Grant directory sync access</strong>.</li>
<li>Select your account and give Cloudflare the required permissions.</li>
<li>Select <strong>Continue</strong>.</li>
<li>In <strong>Configure your report</strong>, choose one or more domains to scan.</li>
<li>Under <strong>Scan date range</strong>, select the date range to perform the scan from the drop-down menu.</li>
<li>Choose your current email security system, from <strong>Current email security system</strong>.</li>
<li>Select <strong>Continue</strong>.</li>
<li>Select <strong>Done</strong>. Cloudflare will begin the task of analyzing all your emails for the chosen domains. This might take some time depending on the size of the inbox and number of domains chosen. You do not need to wait for the scan to complete. Cloudflare will send you an email alert when the scan is complete. If you decide to wait, select <strong>View report</strong> when the scan finishes.</li>
</ol>
<h2 id="analyze-results">Analyze results</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email security</strong> &gt; <strong>Retro Scan</strong>.</li>
<li>Select <strong>Scan report</strong>. This tab shows the total number of emails scanned, a breakdown of the <a href="/email-security/reference/dispositions-and-attributes/">threat types</a> found within the domains selected, the <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/">top targeted employees</a>, and the most common places where threats originate from.</li>
<li>To create an offline copy of the threat report, select <strong>Download Report</strong>.</li>
<li>Select <strong>View detections</strong> to inspect emails found by Retro Scan. You can filter emails by threat type (for example, malicious).</li>
</ol>
