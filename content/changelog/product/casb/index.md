<h1 id="changelog">Changelog</h1>

<h2 id="new-casb-integration-for-zoom"><a href="/changelog/post/2026-09-09-casb-zoom-integration/">New CASB integration for Zoom</a></h2>
<p><em>2026-09-09</em></p>
<p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> now integrates with <a href="/cloudflare-one/integrations/cloud-and-saas/zoom/">Zoom</a>. The integration connects through Cloudflare's pre-built OAuth application — no manual app setup in Zoom is required. After an initial scan, CASB continuously scans your Zoom account to surface new findings as your environment changes.</p>
<p>Zoom is widely used for meetings, webinars, and collaboration. Misconfigurations in account settings, meeting security controls, and recording access can expose organizations to data leakage, unauthorized access, and compliance risk. Cloudflare CASB ingests Zoom account data via API to surface security findings across these areas.</p>
<h4 id="2026-09-09-casb-zoom-integration-key-capabilities">Key capabilities</h4>
<p>Starting today, security teams can scan for security findings across the following assets:</p>
<ul>
<li><strong>Account settings</strong> — Detect weak password policies, unlocked security controls, and two-factor authentication gaps across your Zoom account</li>
<li><strong>User accounts</strong> — Identify users not enforcing SSO, accounts with insecure host keys, unverified or inactive users, and unsafe overrides of account-level security settings</li>
<li><strong>Meetings</strong> — Surface meetings without passwords or waiting rooms, meetings using Personal Meeting IDs (PMIs), and meetings with external domain hosts</li>
<li><strong>Recordings</strong> — Detect publicly accessible cloud recordings, recordings without passcodes, and weak recording password configurations</li>
<li><strong>Content</strong> — Identify sensitive information in meeting and recording content via DLP Profile matching</li>
</ul>
<h4 id="2026-09-09-casb-zoom-integration-learn-more">Learn more</h4>
<p>This <a href="/cloudflare-one/integrations/cloud-and-saas/zoom/">integration</a> is available to all Cloudflare Zero Trust customers today. New customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the Cloudflare One dashboard under <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.</p>


<h2 id="automatically-remediate-microsoft-365-and-google-workspace-findings-with-api-based-casb-remediation-policies"><a href="/changelog/post/2026-08-21-casb-policies/">Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies</a></h2>
<p><em>2026-08-21</em></p>
<p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> is an API-based (agentless) tool that continuously scans your SaaS and cloud applications for security misconfigurations and data exposure. You can now use <strong>CASB remediation policies</strong> to automatically fix a finding or send a webhook the moment CASB detects it, without manual triage.</p>
<h4 id="2026-08-21-casb-policies-remediate-microsoft-365-and-google-workspace-findings">Remediate Microsoft 365 and Google Workspace findings</h4>
<p>A policy can perform a first-party remediation action directly against the SaaS integration API. When a policy triggers, Cloudflare revokes the external sharing configuration without human intervention.</p>
<p>Remediation is currently supported for file-sharing findings in Microsoft 365 and Google Workspace. Support for additional finding types and integrations is coming soon. For the full list of supported finding types, refer to <a href="/cloudflare-one/cloud-and-saas-findings/policies/#run-remediations">Run remediations</a> in the CASB remediation policies documentation.</p>
<h4 id="2026-08-21-casb-policies-send-webhooks">Send webhooks</h4>
<p>A policy can send posture finding data to Slack, ServiceNow, or any other webhook destination. Webhook actions are supported for all posture finding types across CASB integrations.</p>
<p>A single policy can perform both actions: remediate a finding and send a webhook.</p>
<h4 id="2026-08-21-casb-policies-get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Under <strong>Basic information</strong>, enter a <strong>Policy name</strong> and, optionally, a <strong>Description</strong>.</li>
<li>Under <strong>Choose how you want to trigger the policy</strong>, select a <strong>Vendor</strong>, <strong>Integration</strong>, and <strong>Finding type</strong>.</li>
<li>Under <strong>Define what to do with findings that match your trigger</strong>, choose <strong>Run Remediation</strong>, <strong>Send webhooks</strong>, or both.</li>
<li>Under <strong>Status</strong>, turn on <strong>Enable policy</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h4 id="2026-08-21-casb-policies-learn-more">Learn more</h4>
<ul>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/policies/">create and manage CASB remediation policies</a> in Cloudflare One.</li>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> as a policy destination.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare One.</li>
</ul>
<p>CASB remediation policies are now available in Cloudflare One.</p>


<h2 id="casb-adds-support-for-claude-compliance-api"><a href="/changelog/post/2026-05-19-casb-claude-compliance-api/">CASB adds support for Claude Compliance API</a></h2>
<p><em>2026-05-19</em></p>
<p><a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">Cloudflare CASB</a> now integrates with the <a href="https://support.claude.com/en/articles/13015708-access-the-compliance-api">Claude Compliance API</a>. This enhancement gives security teams visibility into Claude usage patterns, admin activity, and compliance-relevant events across their organization.</p>
<p>The Claude Compliance API provides structured access to audit logs and administrative actions within Claude Enterprise and Claude Platform. Cloudflare CASB ingests this data to surface security findings that help organizations enhance their security posture and enforce AI governance.</p>
<h4 id="2026-05-19-casb-claude-compliance-api-key-capabilities">Key capabilities</h4>
<p>Starting today, security teams can scan for security findings across the following assets:</p>
<ul>
<li><strong>Public projects</strong> — Projects set to public visibility</li>
<li><strong>Project attachment</strong> — Files and documents added to projects that violate DLP policies</li>
<li><strong>Chat files</strong> — User-uploaded and provider-generated files that violate DLP policies</li>
<li><strong>Chat messages</strong> — User prompts and provider responses that violate DLP policies</li>
<li><strong>Artifacts</strong> — Provider-generated documents and files that violate DLP policies</li>
</ul>
<h4 id="2026-05-19-casb-claude-compliance-api-learn-more">Learn more</h4>
<p>This <a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">integration</a> is available to all Cloudflare One customers. New Cloudflare customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the dashboard. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.</p>


<h2 id="send-casb-posture-finding-instances-with-webhooks"><a href="/changelog/post/2026-04-09-casb-webhooks/">Send CASB posture finding instances with webhooks</a></h2>
<p><em>2026-04-09</em></p>
<p>You can now use <strong>CASB webhooks</strong> in Cloudflare One to send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.</p>
<p>This gives security teams a simple way to route CASB posture findings into the tools and workflows they already use for triage and response.</p>
<p>To get started, go to <strong>Integrations</strong> &gt; <strong>Webhooks</strong> in the Cloudflare One dashboard to create a webhook destination. After you configure a webhook, open a posture finding instance and select <strong>Send webhook</strong> to send it.</p>
<h4 id="2026-04-09-casb-webhooks-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Flexible authentication</strong> — Configure destinations using <strong>None</strong>, <strong>Basic Auth</strong>, <strong>Bearer Auth</strong>, <strong>Static Headers</strong>, or <strong>HMAC-Signing</strong>.</li>
<li><strong>Built-in testing</strong> — Use <strong>Test delivery</strong> to send a test request before sending a live finding instance.</li>
<li><strong>Posture finding workflows</strong> — Send posture finding instances directly from the finding details workflow in <strong>Cloud &amp; SaaS findings</strong>.</li>
<li><strong>HTTPS destinations</strong> — Configure webhook destinations with public <code>https://</code> URLs.</li>
</ul>
<h4 id="2026-04-09-casb-webhooks-learn-more">Learn more</h4>
<ul>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> in Cloudflare.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare.</li>
</ul>
<p>CASB webhooks are now available in Cloudflare One.</p>


<h2 id="understand-casb-findings-instantly-with-cloudy-summaries"><a href="/changelog/post/2026-02-20-cloudy-in-casb/">Understand CASB findings instantly with Cloudy Summaries</a></h2>
<p><em>2026-02-20</em></p>
<p>You can now easily understand your SaaS security posture findings and why they were detected with <strong>Cloudy Summaries in CASB</strong>. This feature integrates Cloudflare's Cloudy AI directly into your CASB Posture Findings to automatically generate clear, plain-language summaries of complex security misconfigurations, third-party app risks, and data exposures.</p>
<p>This allows security teams and IT administrators to drastically reduce triage time by immediately understanding the context, potential impact, and necessary remediation steps for any given finding—without needing to be an expert in every connected SaaS application.</p>
<p>To view a summary, simply navigate to your Posture Findings in the Cloudflare One dashboard (under <strong>Cloud and SaaS findings</strong>) and open the finding details of a specific instance of a Finding.</p>
<p>Cloudy Summaries are supported on all available integrations, including Microsoft 365, Google Workspace, Salesforce, GitHub, AWS, Slack, and Dropbox. See the full list of supported integrations <a href="/cloudflare-one/integrations/cloud-and-saas/">here</a>.</p>
<h4 id="2026-02-20-cloudy-in-casb-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Contextual explanations</strong> — Quickly understand the specifics of a finding with plain-language summaries detailing exactly what was detected, from publicly shared sensitive files to risky third-party app scopes.</li>
<li><strong>Clear risk assessment</strong> — Instantly grasp the potential security impact of the finding, such as data breach risks, unauthorized account access, or email spoofing vulnerabilities.</li>
<li><strong>Actionable guidance</strong> — Get clear recommendations and next steps on how to effectively remediate the issue and secure your environment.</li>
<li><strong>Built-in feedback</strong> — Help improve future AI summarization accuracy by submitting feedback directly using the thumbs-up and thumbs-down buttons.</li>
</ul>
<h4 id="2026-02-20-cloudy-in-casb-learn-more">Learn more</h4>
<ul>
<li>Learn more about managing <a href="/cloudflare-one/cloud-and-saas-findings/">CASB Posture Findings</a> in Cloudflare.</li>
</ul>
<p>Cloudy Summaries in CASB are available to all Cloudflare CASB users today.</p>


<h2 id="new-saas-security-weekly-digests-with-api-casb"><a href="/changelog/post/2025-11-14-casb-digest/">New SaaS Security weekly digests with API CASB</a></h2>
<p><em>2025-11-14</em></p>
<p>You can now stay on top of your SaaS security posture with the new <strong>CASB Weekly Digest</strong> notification. This opt-in email digest is delivered to your inbox every Monday morning and provides a high-level summary of your organization's Cloudflare API CASB findings from the previous week.</p>
<p>This allows security teams and IT administrators to get proactive, at-a-glance visibility into new risks and integration health without having to log in to the dashboard.</p>
<p>To opt in, navigate to <strong>Manage Account</strong> &gt; <strong>Notifications</strong> in the Cloudflare dashboard to configure the <strong>CASB Weekly Digest</strong> alert type.</p>
<h4 id="2025-11-14-casb-digest-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>At-a-glance summary</strong> — Review new high/critical findings, most frequent finding types, and new content exposures from the past 7 days.</li>
<li><strong>Integration health</strong> — Instantly see the status of all your connected SaaS integrations (Healthy, Unhealthy, or Paused) to spot API connection issues.</li>
<li><strong>Proactive alerting</strong> — The digest is sent automatically to all subscribed users every Monday morning.</li>
<li><strong>Easy to configure</strong> — Users can opt in by enabling the notification in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Notifications</strong>.</li>
</ul>
<h4 id="2025-11-14-casb-digest-learn-more">Learn more</h4>
<ul>
<li>Configure <a href="/notifications/">notification preferences</a> in Cloudflare.</li>
</ul>
<p>The CASB Weekly Digest notification is available to all Cloudflare users today.</p>


<h2 id="casb-introduces-new-granular-roles"><a href="/changelog/post/2025-10-28-casb-roles/">CASB introduces new granular roles</a></h2>
<p><em>2025-10-28</em></p>
<p>Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:</p>
<ul>
<li><strong>Cloudflare CASB Read:</strong> Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.</li>
<li><strong>Cloudflare CASB:</strong> Provides full administrative access to configure and manage all aspects of the CASB product.</li>
</ul>
<p>These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the <strong>Super Administrator</strong> or <strong>Administrator</strong> roles.</p>
<p>To enable <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Data Loss Prevention (DLP)</a>, scans in CASB, account members will need the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Members</strong>.</p>
<p>To learn more about managing roles and permissions, refer to the <a href="/fundamentals/manage-members/roles/">Manage account members and roles documentation</a>.</p>


<h2 id="new-casb-integrations-for-chatgpt-claude-and-gemini"><a href="/changelog/post/2025-08-26-casb-ai-integrations/">New CASB integrations for ChatGPT, Claude, and Gemini</a></h2>
<p><em>2025-08-26 16:00:00 UTC</em></p>
<p><a href="https://www.cloudflare.com/zero-trust/products/casb/">Cloudflare CASB</a> now supports three of the most widely used GenAI platforms — <strong>OpenAI ChatGPT</strong>, <strong>Anthropic Claude</strong>, and <strong>Google Gemini</strong>. These API-based integrations give security teams agentless visibility into posture, data, and compliance risks across their organization’s use of generative AI.</p>
<p><img src="/assets/upstream/images/casb/changelog/casb-ai-integrations-preview.png" alt="Cloudflare CASB showing selection of new findings for ChatGPT, Claude, and Gemini integrations." /></p>
<h4 id="2025-08-26-casb-ai-integrations-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Agentless connections</strong> — connect ChatGPT, Claude, and Gemini tenants via API; no endpoint software required</li>
<li><strong>Posture management</strong> — detect insecure settings and misconfigurations that could lead to data exposure</li>
<li><strong>DLP detection</strong> — identify sensitive data in uploaded chat attachments or files</li>
<li><strong>GenAI-specific insights</strong> — surface risks unique to each provider’s capabilities</li>
</ul>
<h4 id="2025-08-26-casb-ai-integrations-learn-more">Learn more</h4>
<ul>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/openai/">ChatGPT integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/">Claude integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/">Gemini integration docs</a></li>
</ul>
<p>These integrations are available to all Cloudflare One customers today.</p>


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


<h2 id="find-security-misconfigurations-in-your-aws-cloud-environment"><a href="/changelog/post/2024-11-22-cloud-data-extraction-aws/">Find security misconfigurations in your AWS cloud environment</a></h2>
<p><em>2024-11-22</em></p>
<p>You can now use CASB to find security misconfigurations in your AWS cloud environment using <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a>.</p>
<p>You can also <a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account">connect your AWS compute account</a> to extract and scan your S3 buckets for sensitive data while avoiding egress fees. CASB will scan any objects that exist in the bucket at the time of configuration.</p>
<p>To connect a compute account to your AWS integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find and select your AWS integration.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to connect a new compute account.</li>
<li>Select <strong>Refresh</strong>.</li>
</ol>


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>



