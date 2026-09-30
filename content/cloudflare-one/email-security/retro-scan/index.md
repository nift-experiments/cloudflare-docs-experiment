<p>Use Retro Scan to check whether your current email security provider has missed any threats. Cloudflare scans up to 14 days of emails in your Microsoft 365 mailbox and generates a report of malicious messages. Once the scan is complete, you will receive an email notification with a link to the report.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4502.md")
</aside>
<p>To start a free scan:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong> &gt; <strong>Overview</strong>.</li>
<li>Select <strong>Start a free scan</strong> &gt; <strong>Generate report</strong>.</li>
<li>Enable your <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">Microsoft integration</a>. Once you have enabled your Microsoft integration, you will be redirected to a page where you will add your domains and specify your current email security system.</li>
<li>Generate Retro Scan report:
<ul>
<li><strong>Connect domains</strong>: Select at least one domain from your integration, then select <strong>Continue</strong>.</li>
<li><strong>Select current solution</strong>: Select the email security tool you are currently using, then select <strong>Continue</strong>.</li>
<li><strong>Review details</strong>: Confirm the domain and current solution you selected, then select <strong>Continue</strong>. You will receive an email notification once the report is ready.</li>
</ul>
</li>
<li>When you receive the notification email, select the link to view the full report.</li>
<li>On the Cloudflare dashboard, select <strong>View report</strong>.</li>
</ol>
<p>The dashboard will display <strong>Overview</strong> and <strong>Details</strong> pages.</p>
<h3 id="overview">Overview</h3>
<p>The <strong>Overview</strong> page shows a summary of the scan results across your selected domains, including:</p>
<ul>
<li><a href="/cloudflare-one/email-security/monitoring/#disposition-evaluation">Disposition evaluation</a>, the verdict assigned to each scanned message (for example: malicious, suspicious, or spam)</li>
<li>Malicious threat types</li>
<li>Malicious targets, the top recipients targeted by malicious messages</li>
<li>Malicious threat origins</li>
</ul>
<h3 id="details">Details</h3>
<p>The <strong>Details</strong> page lists up to 1,000 emails that were assigned a disposition during the scan. Select any email to review <a href="/cloudflare-one/email-security/investigation/search-email/#details">details</a> about the message.</p>
