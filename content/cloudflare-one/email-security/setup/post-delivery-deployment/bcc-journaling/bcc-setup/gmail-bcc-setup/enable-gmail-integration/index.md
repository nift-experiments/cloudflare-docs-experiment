<p>This guide describes the process for enabling Email security with Google Workspace. It requires setting up a <a href="https://docs.cloud.google.com/iam/docs/service-account-overview">service account</a> and a JSON key in Google Cloud Platform (GCP), followed by configuring domain-wide delegation in the Google Workspace Admin Console to authorize the integration.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Email security, you will need to have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a></li>
<li>A domain to protect</li>
</ul>
<h2 id="enable-gmail-bcc-integration">Enable Gmail BCC integration:</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Overview</strong>. Select one of the following options:</li>
</ol>
<ul>
<li>If you have not purchased Email security, select <strong>Contact sales</strong>.</li>
<li>If you have not associated any integration:
<ul>
<li>Select <strong>Set up</strong>, then choose <strong>BCC/Journaling</strong>.</li>
<li>Select <strong>Integrate with Google</strong> &gt; <strong>Authorize</strong>.</li>
<li>Name your integration, then select <strong>Next</strong>.</li>
<li>Go to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#1-create-a-service-account-in-your-gcp-project">step 1</a> to continue the process of associating an integration.</li>
</ul>
</li>
<li>If you have associated an integration, but have not connected a domain:
<ul>
<li>Select <strong>Connect a domain</strong>.</li>
<li>Choose <strong>BCC/Journaling</strong> &gt; <strong>Integrate with Google</strong>.</li>
<li>Refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/">Connect your domains</a> to connect your domain(s).</li>
</ul>
</li>
</ul>
<h3 id="1-create-a-service-account-in-your-gcp-project"><ol>
<li>Create a Service Account in your GCP Project</li>
</ol></h3>
<ol>
<li>Once you have named your integration, select <strong>Next</strong>.</li>
<li>On the <a href="https://console.cloud.google.com/welcome/new">Google Cloud Console</a>, go to the sidebar, select <strong>APIs &amp; Services</strong>, then select <strong>Credentials</strong>.</li>
<li>Select <strong>CREATE CREDENTIALS</strong> &gt; <strong>Service account</strong>. Refer to <a href="https://docs.cloud.google.com/iam/docs/service-account-overview">Service accounts overview</a> to learn more about service accounts.</li>
<li>Fill in the details to create a service account:
<ul>
<li><strong>Service account name</strong>: Enter <code>Cloudflare Google Integration</code>.</li>
<li><strong>Service account ID</strong>: Enter <code>cloudflare-google-integration</code>.</li>
<li><strong>Service account description</strong>: Enter <code>Cloudflare Google Integration</code>.</li>
<li>Select <strong>CREATE AND CONTINUE</strong>.</li>
</ul>
</li>
</ol>
<h3 id="2-create-a-json-key-for-your-service-account"><ol start="2">
<li>Create a JSON Key for your Service Account</li>
</ol></h3>
<p>On the <a href="https://console.cloud.google.com/welcome/new">Google Cloud Console</a>:</p>
<ol>
<li>On the sidebar, select <strong>IAM &amp; Admin</strong> &gt; <strong>Service Accounts</strong>.</li>
<li>Locate your email, select the three dots, then select <strong>Manage keys</strong>.</li>
<li>Select <strong>Add key</strong> &gt; <strong>Create new key</strong>.</li>
<li>Select <strong>JSON</strong> &gt; Select <strong>CREATE</strong>. This downloads a <code>.json</code> file which you will use when <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#3-upload-json-key">uploading a JSON key</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4953.md")
</aside>
<h3 id="3-upload-json-key"><ol start="3">
<li>Upload JSON Key</li>
</ol></h3>
<p>On the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, upload the <code>.json</code> file downloaded on step 3.</p>
<h3 id="4-enable-necessary-google-workspace-apis-in-gcp"><ol start="4">
<li>Enable Necessary Google Workspace APIs in GCP</li>
</ol></h3>
<p>Enable the following APIs on the Google Cloud Console:</p>
<ul>
<li><a href="https://console.cloud.google.com/apis/library/calendar-json.googleapis.com?project=winter-surf-439414-h1">Google Calendar API</a></li>
<li><a href="https://console.cloud.google.com/apis/library/drive.googleapis.com?project=winter-surf-439414-h1">Google Drive API</a></li>
<li><a href="https://console.cloud.google.com/apis/library/admin.googleapis.com?project=winter-surf-439414-h1">Google Admin SDK API</a></li>
<li><a href="https://console.cloud.google.com/apis/library/gmail.googleapis.com?project=winter-surf-439414-h1">Gmail API</a></li>
<li><a href="https://console.cloud.google.com/apis/library/serviceusage.googleapis.com?project=winter-surf-439414-h1">Google Service Usage API</a></li>
</ul>
<h3 id="5-log-in-to-google-workspace-admin-console"><ol start="5">
<li>Log in to Google Workspace Admin Console</li>
</ol></h3>
<p>Log in to Google Workspace Admin Console: Enter your password and log in to the Google Workspace Admin Console.</p>
<h3 id="6-create-a-domain-wide-delegation-api-client"><ol start="6">
<li>Create a Domain-Wide Delegation API Client</li>
</ol></h3>
<ol>
<li>Copy the <strong>Client ID</strong> and <strong>Scopes</strong> displayed on the Cloudflare One dashboard.</li>
<li>On Google Admin, go to <strong>Security</strong> &gt; <strong>Access and data control</strong> &gt; <strong>API controls</strong>.</li>
<li>Select <strong>MANAGE DOMAIN WIDE DELEGATION</strong> &gt; <strong>Add new</strong>.</li>
<li>Use the Client ID and copy the scopes to create a new API client. Refer to <a href="https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-alert-center?_gl=1*skktsb*_ga*MTMxODg5NDExMy4xNzI5NjA1MzYy*_ga_WH2QY8WWF5*MTcyOTc3MDg2Ny40LjEuMTcyOTc3MDg5OC4yOS4wLjA.#delegate_domain-wide_authority_to_your_service_account">Delegate domain-wide authority to your service account</a>. Then, select <strong>Next</strong>.</li>
</ol>
<h3 id="7-confirm-workspace-administrator-email"><ol start="7">
<li>Confirm Workspace Administrator Email</li>
</ol></h3>
<p>Enter the email associated with the Google Workspace Administrator account. Your email must match the email associated with your Google Workspace account, or else your integration will not work.</p>
<h3 id="8-create-integration"><ol start="8">
<li>Create integration</li>
</ol></h3>
<ol>
<li>Select <strong>Create integration</strong>.</li>
<li>Once you created your integration, you will be redirected to the <strong>Review details</strong> page, where you will be able to review <strong>Integration details</strong>.</li>
<li>Review your details, then select <strong>Complete Email security set up</strong> &gt; <strong>Continue to Email security</strong>.</li>
</ol>
<h2 id="verify-integration">Verify integration</h2>
<p>To verify that the integration has been successful:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong>.</li>
<li>Under <strong>Your integrations</strong>, locate your integration, and ensure that the integration displays <strong>CASB+EMAIL</strong> under <strong>Type</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4952.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have created an integration:</p>
<ul>
<li><a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/">Connect your domains</a> for Email security to start scanning your inbox.</li>
<li><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Enable logs</a> to send detection data to an endpoint of your choice.</li>
</ul>
