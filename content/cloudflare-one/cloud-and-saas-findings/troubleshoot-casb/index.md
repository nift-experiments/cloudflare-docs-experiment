<p>Use this guide to troubleshoot common issues with Cloud Access Security Broker (CASB).</p>
<p>This guide covers troubleshooting steps for CASB integrations and webhooks. For integration-specific issues, refer to the integration's documentation.</p>
<h2 id="integration-fails-to-connect-or-returns-an-error">Integration fails to connect or returns an error</h2>
<p>Integration connection problems are the most common issue during CASB setup. If you receive an error such as &quot;There was an error creating the integration&quot; or are redirected back to the dashboard without the integration appearing, follow these steps.</p>
<h3 id="check-permissions-in-the-third-party-application">Check permissions in the third-party application</h3>
<p>Ensure the account you are using to authorize the integration has the necessary administrative privileges in the third-party application (for example, <strong>Global Administrator</strong> for Microsoft 365, <strong>Super Admin</strong> for Google Workspace, or <strong>Organization Owner</strong> for GitHub). Insufficient permissions are the leading cause of setup failures.</p>
<h3 id="clear-previous-installations">Clear previous installations</h3>
<p>If the SaaS application was previously integrated with a different Cloudflare account, you must manually revoke the old Cloudflare application from within the SaaS provider's admin console.</p>
<ul>
<li><strong>For Microsoft 365</strong>: Go to <strong>Microsoft 365 admin center</strong> &gt; <strong>Enterprise applications</strong> and delete the existing Cloudflare One application.</li>
<li><strong>For Google Workspace</strong>: Go to <strong>Google Admin Console</strong> &gt; <strong>Security</strong> &gt; <strong>Access and data control</strong> &gt; <strong>API controls</strong> and remove the Cloudflare app from third-party app access.</li>
<li><strong>For GitHub</strong>: Go to your organization's <strong>Settings</strong> &gt; <strong>Third-party access</strong> and revoke the Cloudflare CASB application.</li>
</ul>
<p>After cleaning up the old app, wait a few minutes and then try the integration process again from the Cloudflare One dashboard.</p>
<h3 id="verify-oauth-permissions">Verify OAuth permissions</h3>
<p>During setup, CASB will ask you to approve a set of permissions. The permissions requested are required for the CASB service to scan for misconfigurations and, if you choose, to take remediation actions. While some permissions may seem broad (for example, <code>write</code> access), they are necessary for actions like quarantining a file or modifying sharing settings. Refer to the specific integration guide for a detailed list of required permissions.</p>
<h2 id="findings-are-stale-or-not-updating-after-remediation">Findings are stale or not updating after remediation</h2>
<p>A common point of confusion is when a resolved issue (for example, when a file is made private, or when a user is suspended) continues to appear as an active finding in the CASB dashboard.</p>
<h3 id="understand-scan-frequency">Understand scan frequency</h3>
<p>CASB integrations do not provide real-time updates. Scans are performed periodically to discover new findings and validate the status of existing ones. The initial scan can take several hours, and subsequent scans run approximately every 24-48 hours.</p>
<h3 id="force-a-re-scan">Force a re-scan</h3>
<p>To trigger a new scan:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find your integration and select <strong>Configure</strong>.</li>
<li>Turn off <strong>Scan for findings</strong>.</li>
<li>After a few minutes, turn on <strong>Scan for findings</strong> again.</li>
</ol>
<p>This action will queue a fresh scan of your integration. Allow several hours for your findings to reflect the new results.</p>
<h2 id="remediation-action-fails-in-the-dashboard">Remediation action fails in the dashboard</h2>
<p>If you attempt to use a one-click remediation action (such as &quot;Make private&quot;) on a finding, it may result in a <strong>Failed</strong> status, often with a timeout error.</p>
<h3 id="verify-permissions">Verify permissions</h3>
<p>The remediation failure may be due to the permissions for the Cloudflare app being changed or revoked in the SaaS application after the initial setup. Re-validate the integration to ensure all required permissions are still granted.</p>
<h3 id="remediate-manually">Remediate manually</h3>
<p>As a workaround, remediate the finding directly within the SaaS application (for example, change the file's sharing settings in Google Drive). CASB will clear the finding from the dashboard after the next successful scan.</p>
<h2 id="webhook-test-or-delivery-fails">Webhook test or delivery fails</h2>
<p>If Cloudflare cannot deliver a test request or a posture finding instance to your destination, follow these steps.</p>
<h3 id="check-destination-requirements">Check destination requirements</h3>
<p>Verify that the destination URL uses <code>https://</code> and is publicly reachable. Cloudflare rejects destinations that resolve to localhost, loopback, private, or other reserved addresses.</p>
<h3 id="check-authentication-settings">Check authentication settings</h3>
<p>Ensure that the webhook's authentication method matches what your receiver expects. Re-enter any bearer token, Basic auth credentials, static headers, or signing secret if needed.</p>
<h3 id="understand-delivery-timing">Understand delivery timing</h3>
<p>Test delivery sends a test request immediately, but posture finding instance sends are queued in the background. A success message means that Cloudflare accepted the request for delivery.</p>
<h2 id="casb-is-generating-false-positives">CASB is generating false positives</h2>
<p>CASB may incorrectly flag items, such as flagging internally-shared files as public or archived Google Workspace users as inactive.</p>
<h3 id="review-finding-details">Review finding details</h3>
<p>Carefully examine the evidence provided in the finding. An object's status in the SaaS platform may not be accurate.</p>
<h3 id="report-the-issue">Report the issue</h3>
<p>If you confirm the finding is a false positive, report the behavior to Cloudflare Support. Provide the finding ID (visible in the finding's detail view) and as much detail as possible. This helps the Support team refine the detection logic for all customers.</p>
<h3 id="hide-the-finding">Hide the finding</h3>
<p>While Cloudflare investigates the issue, you can <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#hide-findings">ignore the finding or hide individual instances</a> to remove it from your active list and reduce noise.</p>
