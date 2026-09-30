<p>With Email security, you can use different screen criteria to search through your email, reclassify and move a certain volume of messages, find similar emails, and export messages.</p>
<h2 id="screen-criteria">Screen criteria</h2>
<p>Email security allows you to use popular, regular, and advanced screening criteria to search through your inbox. Advanced screening will give you the most in-depth investigation of your inbox.</p>
<p>To screen through your email traffic:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Investigation</strong>, then <strong>Run new screen</strong>.</li>
<li>Choose between <strong>Popular</strong>, <strong>Regular</strong>, and <strong>Advanced</strong> screen methods. Refer to the explanation below to learn what each method does.</li>
</ol>
<p>The results will be displayed on a table. The table allows you to review and take action on the messages that match your chosen screening criteria.</p>
<h3 id="popular-screen">Popular screen</h3>
<p>A popular screen allows you to view messages based on common pre-defined criteria.</p>
<p>To use a popular screen criteria:</p>
<ol>
<li>Under <strong>Method</strong>, select <strong>Popular screens</strong>.</li>
<li>Select one of the following criteria:
<ul>
<li><strong>Moved emails</strong>: View emails automatically or manually moved within the last seven days.</li>
<li><strong>Reclassified emails</strong>: Emails that had their disposition reclassified within the last seven days.</li>
<li><strong>Malicious emails</strong>: Emails assigned the malicious disposition within the last seven days.</li>
<li><strong>Spoof emails</strong>: Emails assigned the spoof disposition within the last seven days.</li>
<li><strong>Suspicious emails</strong>: Emails assigned the suspicious disposition within the last seven days.</li>
<li><strong>Spam emails</strong>: Emails assigned to the spam disposition within the last seven days.</li>
</ul>
</li>
<li>Select <strong>Run screen</strong>.</li>
</ol>
<p>To modify your screening criteria, under <strong>Active screen criteria</strong>, select <strong>Modify</strong>.</p>
<h3 id="regular-screen">Regular screen</h3>
<p>A regular screen allows you to investigate your inbox by inserting a term to screen across all criteria.</p>
<p>To use a regular screen criteria:</p>
<ol>
<li>Under <strong>Method</strong>, select <strong>Regular screen</strong>.</li>
<li>Select a <strong>Date range</strong>.</li>
<li>Enter a keyword.</li>
<li>Select <strong>Run screen</strong>.</li>
</ol>
<p>To include all emails as part of the search, enable <strong>Include all mail</strong>.</p>
<p>To modify your screening criteria, under <strong>Active screen criteria</strong>, select <strong>Modify</strong>.</p>
<p>To reset your screening criteria, select <strong>Reset</strong>.</p>
<h3 id="advanced-screen">Advanced screen</h3>
<p>The advanced screen criteria gives you the option to narrow message results based on specific criteria. The advanced screen has several options (such as keywords, subject keywords, sender domain, and more) to scan your inbox.</p>
<p>To use advanced screen criteria:</p>
<ol>
<li>Under <strong>Method</strong>, select <strong>Advanced screen</strong>.</li>
<li>(Required) Select a date range.</li>
<li>(Optional) Fill in the other fields. All fields, except for Subject, must be filled with one value only.</li>
<li>Select <strong>Run screen</strong>.</li>
</ol>
<p>To include all emails as part of the search, enable <strong>Include all mail</strong>.</p>
<p>To modify your screening criteria, under <strong>Active screen criteria</strong>, select <strong>Modify</strong>.</p>
<p>To reset your screening criteria, select <strong>Reset</strong>.</p>
<h2 id="move-messages">Move messages</h2>
<p>Moving messages allows you to move messages to a specific folder. You can move up to 1,000 messages at a time.</p>
<p>To move messages:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong>, and select <strong>Investigation</strong>.</li>
<li>On the Investigation page, select all the messages you want to move.</li>
<li>Select the <strong>Action</strong> dropdown, then select <strong>Move</strong>.</li>
<li>Select among one of the following folders:
<ul>
<li><strong>Inbox</strong>: Move messages to the primary email folder.</li>
<li><strong>Junk email</strong>: Move messages to the junk or spam folder.</li>
<li><strong>Trash</strong>: Move messages to the trash or deleted items email folder.</li>
<li><strong>Soft delete (user recoverable)</strong>: Move messages to the user's Deleted Items folder. This option is for Microsoft 365 only.</li>
<li><strong>Hard delete (admin recoverable)</strong>: Delete messages from a user's inbox.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To move messages in bulk, select <strong>Select all messages</strong> &gt; <strong>Action</strong> &gt; <strong>Move</strong>.</p>
<h2 id="find-similar-emails">Find similar emails</h2>
<p>Each detection has an Email Detection Fingerprint (EDF) hash that Email security sends to the Search API to retrieve similar detections.</p>
<p>To find similar detection results:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong>, and select <strong>Investigation</strong>.</li>
<li>On the Investigation page, under <strong>Your matching messages</strong>, search for the <strong>Similar emails</strong> column.</li>
<li>Select the number of similar emails. Selecting the number will show you a list of similar emails.</li>
</ol>
<h2 id="export-messages">Export messages</h2>
<p>With Email security, you can export messages to a CSV file.</p>
<p>To export messages:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong>, and select <strong>Investigation</strong>.</li>
<li>On the Investigation page, under <strong>Your matching messages</strong>, select <strong>Export to CSV</strong>.</li>
<li>Select <strong>Export messages</strong> on the pop-up message. You can export up to 500 messages from the dashboard. To export up to 1,000 matching messages, use the <a href="/api/resources/email_security/subresources/investigate/methods/get/">API</a>.</li>
</ol>
<p>To export messages in bulk, select <strong>Select all messages</strong> &gt; <strong>Export to CSV</strong>.</p>
<h2 id="email-status">Email status</h2>
<p>Email security allows you to review the status and actions of each email.</p>
<p>To view status and actions for each email:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong>, and select <strong>Investigation</strong>.</li>
<li>On the Investigation page, select the three dots.</li>
<li>Selecting the three dots will show you the following options:</li>
</ol>
<ul>
<li>
<p>If the email is quarantined:</p>
<ul>
<li><strong>View details</strong>: Refer to <a href="#email-details">Email details</a> to learn more.</li>
<li><strong>View similar emails</strong>: Find similar emails based on the <code>value_edf_hash</code> (Electronic Detection Fingerprint hash).</li>
<li><strong>Release</strong>: Email security will no longer quarantine your chosen messages.</li>
<li><strong>Submit for review</strong>: Choose the dispositions of your messages if they are incorrect. Refer to <a href="#reclassify-messages">Reclassify messages</a> to learn more.</li>
</ul>
</li>
<li>
<p>If the email is not quarantined:</p>
<ul>
<li><strong>View details</strong>.</li>
<li><strong>View similar emails</strong>.</li>
<li><strong>View submission detail</strong>.</li>
<li><strong><a href="/cloudflare-one/email-security/settings/auto-moves/">Move</a></strong> (only available if you authorized moves).</li>
<li><strong><a href="#reclassify-messages">Submit for review</a></strong>.</li>
</ul>
</li>
</ul>
<h2 id="email-details">Email details</h2>
<p>Email security shows you the following email detail information:</p>
<ul>
<li>Details</li>
<li>Action log</li>
<li>Raw message</li>
<li>Mail trace</li>
</ul>
<h3 id="details">Details</h3>
<p>Email security displays the following details:</p>
<ol>
<li><strong>Threat type</strong>: Threat type of the email, for example, <a href="/cloudflare-one/email-security/reference/how-es-detects-phish/">credential harvester</a>, and <a href="/cloudflare-one/email-security/reference/how-es-detects-phish/">IP-based spam</a>.</li>
<li><strong>Validation</strong>: Email validation methods <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>. The dashboard will display Pass if SPF, DKIM and DMARC checks have passed.</li>
<li><strong>Sender details</strong>: Information include:
<ul>
<li>IP address</li>
<li>Registered domain</li>
<li>Autonomous sys number: This number identifies your <a href="https://www.cloudflare.com/en-gb/learning/network-layer/what-is-an-autonomous-system/">autonomous system (AS)</a>.</li>
<li>Autonomous sys name: This name identifies your autonomous system (AS).</li>
<li>Country</li>
</ul>
</li>
<li><strong>Links identified</strong>: A list of malicious links identified by Email security. Refer to <a href="#open-links">Open links</a> to open links in Security Center, Browser Isolation or an external tool of your choice.</li>
<li><strong>Attachments</strong>: If an email has an attachment, the Cloudflare dashboard will display the filename, and the disposition assigned. You can open attachments in <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>. Only PDF files are currently supported.</li>
<li><strong>Reasons for disposition</strong>: Description of why the email was deemed as malicious, suspicious, or spam. The dashboard also displays <a href="/cloudflare-one/email-security/investigation/search-email/#cloudy-summaries">Cloudy summaries</a>.</li>
</ol>
<h4 id="cloudy-summaries">Cloudy summaries</h4>
<p>The Cloudflare dashboard uses <a href="/fundamentals/reference/cloudy-ai-agent/">Cloudy</a> to explain why an email was classified as unwanted.</p>
<p>Cloudy analyzes the underlying detection code and generates a description of the specific detection logic that led to an email final disposition. Each summary provides a rating option that allows you to provide feedback to the Email security team. Cloudy summaries are only available for emails with a final <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#available-values">disposition</a>.</p>
<p><strong>View all signatures</strong> allows you to view all the detections that triggered on the email, including detections that did not determine the final disposition.</p>
<h4 id="open-links">Open links</h4>
<p>You can open links in Security Center or <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>, or copy and paste the link so you can investigate content in external tools.</p>
<p>When you select a link in a suspicious email, you risk exposing your device and your company's network to malware, ransomware, and credential harvesting.</p>
<p>Browser Isolation eliminates any risk of your device being compromised by opening all web content from unverified or suspicious sources in a safe, disposable remote browser session hosted by Cloudflare.</p>
<p>To open links in Security Center:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Investigation</strong>.</li>
<li>Locate the message you want to open links for, select the three dots, then select <strong>View details</strong>.</li>
<li>Under <strong>Details</strong>, go to <strong>Links identified</strong>.</li>
<li>Locate the link you want to open, and select <strong>Open in Security Center</strong>.</li>
<li>You will be redirected to Investigate in the Cloudflare dashboard.</li>
<li>Select <strong>Scan now</strong>.</li>
<li>The dashboard will generate a report for your link.</li>
</ol>
<p>To open links in Browser Isolation:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Investigation</strong>.</li>
<li>Locate the message you want to open links for, select the three dots, then select <strong>View details</strong>.</li>
<li>Under <strong>Details</strong>, go to <strong>Links identified</strong>.</li>
<li>Locate the link you want to open, and select <strong>Open in Browser Isolation</strong>.</li>
<li>The link will open in a separate window where you will be able to browse the content securely.</li>
</ol>
<p>Alternatively, you can directly <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#open-links-in-browser-isolation">open links in Browser Isolation</a>.</p>
<p>When you open a link from an email, Cloudflare will present you with a blue bar. This indicates that the page is isolated and that you are protected from any potential malicious content on that page.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4923.md")
</aside>
<p>To open and investigate a link in an external tool:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Investigation</strong>.</li>
<li>Locate the message you want to open links for, select the three dots, then select <strong>View details</strong>.</li>
<li>Under <strong>Details</strong>, go to <strong>Links identified</strong>.</li>
<li>Locate the link you want to open, and select <strong>Copy URL</strong>.</li>
<li>Paste the link in your external tool.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4922.md")
</aside>
<p>If you encounter this error:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Settings</strong> &gt; <strong>Resources</strong>.</li>
<li>Select <strong>Generate certificate</strong>.</li>
<li>Choose the <strong>Expiration</strong> (5 years is recommended), then select <strong>Generate certificate</strong>. Your certificate is now generated, and the dashboard will display its Deployment Status as INACTIVE.</li>
<li>Select the three dots, and then select <strong>Activate</strong> to activate your certificate.</li>
<li>Select the three dots, and then select <strong>Mark as in-use</strong>.</li>
<li>Your certificate deployment status should display AVAILABLE IN-USE.</li>
</ol>
<h3 id="action-log">Action log</h3>
<p>Action log allows you to review post-delivery actions performed on your selected message. The action log displays:</p>
<ul>
<li><strong>Date</strong>: Date when the post-delivery action was performed.</li>
<li><strong>Activity</strong>: The activity taken on an email. For example, moving the email to the trash folder, releasing a quarantined email, and more.</li>
</ul>
<h3 id="raw-message">Raw message</h3>
<p>Raw message allows you to view the raw details of the message. You can also choose to download the email message. To download the message, select <strong>Download .EML</strong>.</p>
<h3 id="mail-trace">Mail trace</h3>
<p>Mail trace allows you to track the path your selected message took from the sender to the recipient. Mail trace displays:</p>
<ul>
<li><strong>Date</strong>: The date and time when the mail was tracked.</li>
<li><strong>Type</strong>: An email can be inbound (email sent to you from another email), or outbound (emails sent from your email address).</li>
<li><strong>Activity</strong>: The activity taken on an email. For example, moving the email to the trash folder, releasing a quarantined email, and more.</li>
</ul>
