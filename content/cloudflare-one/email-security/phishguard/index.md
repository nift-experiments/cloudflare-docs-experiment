<p>PhishGuard is a team of analysts that routinely inspects your email environment and responds to threats that come through your email inbox.</p>
<p>While Email security uses advanced technologies to protect your email inbox, PhishGuard offers an additional human component to protect your email environment against impersonation events, suspicious items, false negatives/false positives, and any new event that automated intelligent systems may miss due to a lack of context (for example, a compromised account activity).</p>
<p>PhishGuard only works on a post-delivery environment (only emails that have already landed in your email inbox are reviewed). As a result, PhishGuard analysts may <a href="/cloudflare-one/email-security/submissions/#submit-messages-for-review">submit a message for review</a> or <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> based on their findings.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4503.md")
</aside>
<p>PhishGuard coordinates with the email detections team, allowing you to directly request immediate detection for specific items and implement custom detections unique to your needs. An example of this is requesting to block all PayPal traffic if you do not use PayPal for invoicing. This capability allows you to take ownership over the rules governing your email environment through PhishGuard's human intervention.</p>
<p>Additionally, PhishGuard analysts:</p>
<ul>
<li>Use real-time threat data to identify malicious activity. Email-based threats are responded to rapidly, and immediately reported and documented.</li>
<li>Review every <a href="/cloudflare-one/email-security/investigation/search-email/#user-submissions">user</a> and <a href="/cloudflare-one/email-security/investigation/search-email/#team-submissions">team</a> submission so your security team can focus on more critical activities.</li>
<li>Help you detect and mitigate threats faster, reducing the time attacks have access to your network. This also helps reducing business impact, because it prevents data breaches, financial loss, and reputational damage.</li>
</ul>
<p>To use PhishGuard:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>PhishGuard</strong>.</li>
</ol>
<p>The dashboard will display the following metrics:</p>
<ul>
<li>ROI Calculator</li>
<li>Insider threat defense</li>
<li>Email threat hunting</li>
<li>Actions</li>
<li>API Status</li>
<li>Managed email security operations</li>
<li>Reports</li>
</ul>
<h2 id="roi-calculator">ROI Calculator</h2>
<p>Use the ROI Calculator to compare triage durations and hourly rates to calculate PhishGuard's return on investment.</p>
<p>The ROI Calculator displays:</p>
<ul>
<li>Total aggregated saved number in USD dollars.</li>
<li>Triage duration: The amount of time in minutes spent triaging the message.</li>
<li>Hourly rate.</li>
</ul>
<h2 id="insider-threat-defense">Insider threat defense</h2>
<p>An <a href="https://www.cloudflare.com/en-gb/learning/access-management/what-is-an-insider-threat/">insider threat</a> is a risk to an organization's security stemming from someone associated with the organization. PhishGuard looks for threat actor groups.</p>
<p>Insider threat defense on the dashboard displays <strong>Insider leads</strong> and <strong>Insider reports generated</strong>. <strong>Insider leads</strong> displays the number of emails identified as potential insider threat email. <strong>Insider reports generated</strong> displays the number of reports created based on insider leads.</p>
<h2 id="email-threat-hunting">Email threat hunting</h2>
<p>PhishGuard reviews suspicious and highly malicious activity in your email environment.</p>
<p>On the Cloudflare One dashboard, email threat hunting displays previously unknown phishing attacks.</p>
<p>Email threat hunting also gives you information on <strong>Threat leads generated</strong> and <strong>Total reposts generated</strong>.</p>
<h2 id="actions">Actions</h2>
<p><strong>Actions</strong> allows you to review the most common actions taken by the PhishGuard team, such as escalations, threat hunts, and moves.</p>
<h2 id="api-status">API Status</h2>
<p>API Status allows you to monitor and configure the current status of API message auto-moves and directory integrations.</p>
<p>Select <strong>Message moves</strong> to <a href="/cloudflare-one/email-security/settings/auto-moves/">configure auto-moves</a>. Select <strong>Directory integration</strong> to <a href="/cloudflare-one/email-security/directories/">configure directories</a>.</p>
<h2 id="managed-email-security-operations">Managed email security operations</h2>
<p>Managed email security operations allows you to review the results of phish submissions reviewed by the PhishGuard team.</p>
<p>It displays the following:</p>
<ul>
<li>Total <a href="/cloudflare-one/email-security/settings/phish-submissions/">phish submissions</a></li>
<li>Tracked incidents</li>
<li>Median time to resolve</li>
<li>Resolved track incidents</li>
</ul>
<h2 id="reports">Reports</h2>
<p>Under Reports, you can review reports of threats discovered and resolved by the PhishGuard team.</p>
<p>If you select the three dots, you can:</p>
<ul>
<li><strong>View report details</strong>: Report Details gives you the following information about each report:
<ul>
<li><strong>Overview</strong>: An Overview of the report. This includes date and time of the report, type of attack performed, and more.</li>
<li><strong>Target and victimology</strong>: Company targeted.</li>
<li><strong>Details</strong>: Displays information such as delivery disposition, current disposition, ES Alert ID, Message-ID, Timestamp, Subject, and Attempted Fraudulent Amount.</li>
<li><strong>Indicators of compromise (IOC)</strong>: <a href="https://www.cloudflare.com/en-gb/learning/security/what-are-indicators-of-compromise/">Indicators of compromise (IOC)</a> are information about a specific security breach that can help security teams determine if an attack has taken place.</li>
</ul>
</li>
<li>Preview email.</li>
<li><a href="/cloudflare-one/email-security/settings/auto-moves/">Move email</a>.</li>
</ul>
