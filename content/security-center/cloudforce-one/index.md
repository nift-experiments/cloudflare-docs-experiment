<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13827.md")
</aside>
<p>Cloudforce One is Cloudflare's Threat Intelligence Platform (TIP). It collects and correlates threat data from Cloudflare telemetry, then surfaces that data as visualizations, automated rules, and analyst-reviewed intelligence.</p>
<p>Security Operations Center (<a href="https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-a-security-operations-center-soc/">SOC</a>) teams use Cloudforce One to investigate threats, track adversaries, and take action — such as pushing firewall rules or exporting indicators.</p>
<h2 id="access-cloudforce-one">Access Cloudforce One</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13826.md")
</aside>
<p>To access Cloudforce One:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Threat intelligence</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<p>You can also use Cloudforce One via the <a href="/api/resources/cloudforce_one/subresources/requests/subresources/assets/">REST API</a>.</p>
<p>The Threat Intelligence page contains four sections:</p>
<ul>
<li><strong>Threat Events</strong> — View and analyze threat intelligence data collected across the Cloudflare network.</li>
<li><strong>Priority Intelligence Requirements (PIRs)</strong> — Define the intelligence topics your organization needs to track. PIRs help you identify gaps in your threat coverage.</li>
<li><strong>Requests for Information (RFIs)</strong> — Submit specific queries to the Cloudforce One analysis team.</li>
<li><strong>Reports</strong> — Read the latest threat reports published by Cloudforce One.</li>
</ul>
<h2 id="analyze-threat-events">Analyze threat events</h2>
<p>Threat events represent Cloudflare telemetry and threat actor activity observed on the Cloudflare network. Use threat events to investigate threats targeting your organization or your industry.</p>
<p>To access threat events, go to the <strong>Threat intelligence</strong> page in the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>You can also access threat events via the <a href="/api/resources/cloudforce_one/subresources/threat_events/">API</a>.</p>
<p>Cloudforce One customers have access to the following datasets:</p>
<ul>
<li>Advanced Persistent Threats (APTs) — the default dataset</li>
<li><a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">DDoS</a> attacks</li>
<li>Cybercrime</li>
<li>Compromised devices</li>
<li>Residential proxies</li>
<li><a href="/waf/">WAF</a> attacks</li>
</ul>
<h3 id="identify-the-adversary">Identify the adversary</h3>
<p>The Cloudflare dashboard provides visualizations that include:</p>
<ul>
<li><strong>Sankey diagrams</strong> — Flow diagrams that visualize the distribution of attacks across origins and targets. Use these to trace attack flows from origin infrastructure to targets.</li>
<li><strong>Industry distribution</strong> — Identify whether campaigns are targeting your specific sector (for example, finance or retail).</li>
</ul>
<h3 id="search-for-indicators">Search for indicators</h3>
<p>Search across global datasets for specific indicators, including:</p>
<ul>
<li>IP addresses and domains</li>
<li>File hashes</li>
<li><a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3 fingerprints</a> — TLS client fingerprints used to profile specific SSL/TLS clients across different destinations</li>
<li>Threat insights — Link events to specific campaigns or threat actor names (for example, APT28).</li>
</ul>
<h3 id="create-waf-rules-and-receive-notifications">Create WAF Rules and receive notifications</h3>
<ul>
<li><strong>Saved views</strong> — Save custom filters for recurring threat event investigations.</li>
<li><strong>Automated rules</strong> — Generate security rules from threat data and push them to your Cloudflare <a href="/waf/">WAF</a> or firewall.</li>
<li><strong><a href="https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/">STIX2</a> exports</strong> — Export threat intelligence in STIX2 format for integration with third-party <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-siem/">SIEM</a> (Security Information and Event Management) or SOAR (Security Orchestration, Automation, and Response) platforms.</li>
</ul>
<h2 id="use-cloudy-to-analyze-threat-events">Use Cloudy to analyze threat events</h2>
<p>You can use Cloudy, Cloudflare's AI Agent, to receive an analysis and summary of threat events.</p>
<p>To analyze threat events using Cloudy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Threat intelligence</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Threat Events</strong> &gt; <strong>Analyze with Cloudy</strong>.</li>
</ol>
<p>Cloudy will show you the top threat events, analyze them, and give you a summary of threat events. You can also decide to receive an analysis based on <strong>Attacker</strong>, <strong>Indicator</strong>, and more. For example, you can enter &quot;Give me a summary of threat events for ABC Attacker&quot;. Cloudy will then summarize threat events for ABC attacker.</p>
<h2 id="submit-rfis">Submit RFIs</h2>
<p>To submit RFIs (Request for Information):</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Threat Intelligence</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Requests for Information</strong>.</li>
<li>Select <strong>New Request</strong>.</li>
<li>Fill in the required fields, then select <strong>Save</strong>.</li>
</ol>
<details class="nb-details"><summary>List of RFI types</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13828.md")
</div></details>
<p>Once you select <strong>Save</strong>, the dashboard will display an overview of the shared information consisting of:</p>
<ul>
<li><strong>Status</strong>: When you submit the RFI, the status is <code>Open</code>. Once the team accepts the RFI, the status changes to <code>Accept</code>. When the team commits to answer your RFI, the status changes to <code>Complete</code>.</li>
<li><strong>Priority</strong>: Priority of request.</li>
<li><strong>Request type</strong>: Choose among a selection of request types, such as DDos Attack, Passive DNS Resolution, and more.</li>
<li><strong>Request content</strong>: The content of the request.</li>
</ul>
<p>The <strong>Responses</strong> section allows you to add clarifying questions and comments.</p>
<p>To view your RFI, select <strong>Cloudforce One Requests</strong> on the sidebar, locate your RFI, then select <strong>View</strong>. From here, you can also choose to edit your existing RFI by selecting <strong>Edit</strong>.</p>
<p>To delete your RFI, the status must be <code>Open</code>. Go to the RFI you want to delete, and select <strong>Delete</strong>. On the pop-up, select <strong>Delete</strong> to confirm deletion. Once Cloudflare accepts and begins processing RFIs, you will not be able to delete RFIs.</p>
<h3 id="upload-and-download-attachment">Upload and download attachment</h3>
<p>You can also choose to upload and download an attachment.</p>
<p>Under <strong>Attachments</strong>, select the file you want to upload, then select <strong>Save</strong>.</p>
<p>To download an attachment, select <strong>Download</strong> on the attachment.</p>
<h2 id="improve-your-security-posture-or-recover-from-a-past-incident">Improve your security posture or recover from a past incident</h2>
<p>Use Cloudforce One to improve your security posture or recover from a past incident.</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to <strong>Application security</strong> &gt; <strong>Incident Response</strong>.</p>
</li>
<li>
<p><strong>Choose service</strong>: Select one of the services.</p>
</li>
<li>
<p><strong>Provide request details</strong>:</p>
</li>
</ol>
<ul>
<li>Fill in the required information for the service you selected. Select <strong>Next</strong>.</li>
<li>Review your request, then select <strong>Submit</strong>.</li>
<li>After you submit your request, the Cloudforce One team will respond.</li>
</ul>
<h2 id="request-help-for-active-attack">Request help for active attack</h2>
<p>If you want to stop an active cyber attack, you can request assistance via the Cloudflare dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>On the top bar, select <strong>Support</strong> &gt; <strong>Get help</strong> &gt; <strong>Under attack</strong>.</li>
<li>Under <strong>Request help to stop active cyberattacks</strong>, select <strong>Request help</strong>.</li>
<li>The dashboard will show you a pop-up where you will need to enter and confirm your phone number.</li>
<li>Once you have entered your phone number, select <strong>Confirm number and request help</strong>. Requesting help from the dashboard will page an incident responder and you can expect a call-back as soon as possible. We advise you to wait for the call-back, and only use the phone-line in case you have not heard back from the team within 10 minutes.</li>
</ol>
