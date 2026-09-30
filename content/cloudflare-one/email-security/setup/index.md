<p>Before you start the onboarding process, you will have to:</p>
<ol>
<li>Choose a deployment path: Email security provides two deployment modes, <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/">post-delivery</a> for API and BCC/Journaling and <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/">pre-delivery</a> for MX/Inline.</li>
<li>Learn about dispositions, impersonation registry, and submissions.</li>
<li>Know the steps to configure your email environment correctly.</li>
</ol>
<p>The following table compares features available across API, BCC/Journaling and MX/Inline:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Microsoft 365</th>
<th>Google Workspace</th>
<th>Others (On-prem/Cloud)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Deployment type</td>
<td>API and MX</td>
<td>BCC and MX</td>
<td>MX only</td>
</tr>
<tr>
<td>API integration</td>
<td>Microsoft Graph API</td>
<td>BCC only</td>
<td>None</td>
</tr>
<tr>
<td>BCC/Journaling</td>
<td>Uses a Journal Rule in the Microsoft Purview portal</td>
<td>Uses BCC rules</td>
<td>Uses journaling</td>
</tr>
<tr>
<td>Inline/MX Mode</td>
<td>MX records point to Cloudflare</td>
<td>MX records point to Cloudflare</td>
<td>MX records point to Cloudflare</td>
</tr>
<tr>
<td>Message remediation</td>
<td>Auto-moves through Read/Write API</td>
<td>Auto-moves through Read/Write API</td>
<td>Messages can be blocked, quarantined, or modified inline</td>
</tr>
</tbody>
</table>
<p>Note that:</p>
<ul>
<li>All email providers support MX/Inline deployment.</li>
<li>Microsoft 365 or Google Workspace users who integrate Email security via API, BCC/Journaling can modify emails primarily through deletion or  post-delivery <a href="/cloudflare-one/email-security/settings/auto-moves/">move</a>.</li>
<li>Microsoft 365 or Google Workspace users who integrate Email security via MX/Inline can modify emails via post-delivery <a href="/cloudflare-one/email-security/settings/auto-moves/">move</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">link actions</a> and <a href="/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/">text add-ons</a>.</li>
</ul>
<h2 id="1-choose-a-deployment"><ol>
<li>Choose a deployment</li>
</ol></h2>
<h3 id="post-delivery-deployment">Post-delivery deployment</h3>
<p>When you choose post-delivery deployment, Cloudflare scans emails <strong>after</strong> they reach a users' inbox.</p>
<p>If you are a Microsoft 365 user, this is done via <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/">Microsoft's Graph API</a> or <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/m365-journaling/">journaling</a>.</p>
<p>If you are a <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/gmail-bcc-setup/">Google Workspace</a> or <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/bcc-microsoft-exchange/">Microsoft Exchange</a> user, this is done via BCC.</p>
<h4 id="why-you-should-consider-post-delivery-deployment">Why you should consider post-delivery deployment</h4>
<p>Post-delivery deployment is time-efficient, because it does not involve MX changes. Post-delivery deployment does not disrupt mail flow. Post-delivery deployment allows you to enable <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move events</a> to hard or soft delete messages, and synchronize your <a href="/cloudflare-one/email-security/directories/">directory</a> when you use Microsoft Graph API or Google Workspace.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4915.md")
</aside>
<h3 id="pre-delivery-deployment">Pre-delivery deployment</h3>
<p>When you choose pre-delivery deployment, Cloudflare scans emails <strong>before</strong> they reach a users' inbox. The MX record points to Cloudflare.</p>
<h4 id="why-you-should-consider-pre-delivery-deployment">Why you should consider pre-delivery deployment</h4>
<p>Pre-delivery deployment provides you with the highest level of protection. It enforces <a href="/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/">text add-ons</a> or link rewrite at delivery.</p>
<p>Pre-delivery blocks threats in transit, and it adds banners or texts before the user views the email.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4914.md")
</aside>
<h2 id="2-understand-dispositions"><ol start="2">
<li>Understand dispositions</li>
</ol></h2>
<p>Dispositions allow you to configure policies and tune reporting. For example, you can configure a policy to move suspicious emails to your junk folder.</p>
<p>Refer to <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">Dispositions</a> to learn more about dispositions.</p>
<h2 id="3-set-up-the-impersonation-registry"><ol start="3">
<li>Set up the impersonation registry</li>
</ol></h2>
<p>Most <a href="https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/">business email compromise (BEC)</a> targets executives or finance roles. You must add addresses of roles who are likely to be impersonated. Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">Impersonation registry</a> to learn how to add a user to the impersonation registry.</p>
<p>Roles you may want to include in the impersonation registry are:</p>
<ul>
<li>C-suites</li>
<li>Finance roles</li>
<li>HR</li>
<li>IT help-desk</li>
<li>Legal</li>
</ul>
<p>You should review your impersonation registry on a quarterly basis as roles change.</p>
<h2 id="4-submit-messages"><ol start="4">
<li>Submit messages</li>
</ol></h2>
<p>A submission is a change to an email's disposition <strong>after</strong> initial scanning. It is Cloudflare's built-in feedback loop for correcting false positives/negatives <strong>and</strong> training the detection models to get smarter over time. Refer to <a href="/cloudflare-one/email-security/submissions/#submit-messages-for-review">Submit messages for review</a> to learn how to reclassify a message.</p>
<h3 id="who-can-reclassify-messages">Who can reclassify messages</h3>
<p><a href="/cloudflare-one/email-security/submissions/team-submissions/">Security teams</a> and <a href="/cloudflare-one/email-security/submissions/user-submissions/">end users</a> can perform a submission.</p>
<h3 id="why-you-should-submit-messages">Why you should submit messages</h3>
<p>Submissions are critical because:</p>
<ul>
<li><strong>They help improve model accuracy</strong>: Every validated submissions teaches Cloudflare's machine learning to recognise new lures, language, infrastructure, and benign patterns.</li>
<li><strong>They reduce alert fatigue</strong>: Correcting Suspicious or Spam emails that users actually want tailors detections to your organization, cutting noise in the dashboard.</li>
<li><strong>They close the remediation loop</strong>: When a disposition is upgraded to Malicious, Cloudflare auto-moves those emails out of every inbox (Graph API or Google Workspace API integrations).</li>
<li><strong>They can help you log activity taken on any submission</strong>: Each submission displays a submission ID, details about original, requested and final dispositions, and more. Refer to <a href="/cloudflare-one/email-security/submissions/#submit-messages-for-review">Submit messages for review</a> to learn more about submissions.</li>
</ul>
<p>To make the most of submissions:</p>
<ol>
<li>Review submissions on a weekly basis.</li>
<li>Ensure you have an integration associated with any MX/Inline deployment. When you associate an integration, you will not need to upload the EMLs every time; Cloudflare can use APIs to receive a copy of your email messages.</li>
<li>Investigate any increase in <a href="/cloudflare-one/email-security/investigation/search-email/#user-submissions">user submissions</a> (users may have found a phish that bypassed filters) and confirm that analyst-final dispositions align with your policies.</li>
</ol>
<p>A correct use of submissions ensures that Email security delivers a stronger protection with less manual tuning.</p>
<h2 id="5-configuration-checklist"><ol start="5">
<li>Configuration checklist</li>
</ol></h2>
<p>Follow the below checklist to ensure your email environment is set up correctly:</p>
<table>
<thead>
<tr>
<th>Step</th>
<th>Post-delivery</th>
<th>Pre-delivery</th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorize integration (<a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">Graph API</a> or <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/">Google Workspace</a>)</td>
<td>Required<sup><a href="#footnote-1">1</a></sup></td>
<td>Required <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Associate an integration with an MX/Inline domain</td>
<td></td>
<td>Required</td>
</tr>
<tr>
<td>Add/verify domains</td>
<td>Required</td>
<td>Required</td>
</tr>
<tr>
<td><a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/">Update MX records/connector</a>, then allow Cloudflare <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">egress IPs</a> on downstream mail server</td>
<td></td>
<td>Required</td>
</tr>
<tr>
<td>Populate <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a> and <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow</a>/<a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">block</a> lists</td>
<td>Required</td>
<td>Required</td>
</tr>
<tr>
<td>Configure <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/">partner domain TLS</a> and admin quarantine</td>
<td></td>
<td>Required</td>
</tr>
<tr>
<td>Configure <a href="/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/">text add-ons</a> and <a href="/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">link actions</a></td>
<td></td>
<td>Required</td>
</tr>
<tr>
<td>Send a test email and verify it appears in <strong>Monitoring</strong> &gt; <a href="/cloudflare-one/email-security/monitoring/#email-activity"><strong>Email activity</strong></a> with expected disposition</td>
<td>Required</td>
<td>Required</td>
</tr>
</tbody>
</table>
<p>Now that you know which deployment path to choose, you can begin your onboarding process.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Associating an integration with BCC/Journaling is required for post-delivery but not for pre-delivery.</li>
<li id="footnote-2">Still used for directory/auto‑move insight if desired as well as authorizing free API CASB.</li></ol></section>
