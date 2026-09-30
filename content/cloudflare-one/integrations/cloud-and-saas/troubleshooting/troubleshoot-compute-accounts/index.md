<p>Cloudflare CASB detects when compute accounts are unhealthy or outdated. Common compute account issues include security or functionality updates and API token misconfigurations.</p>
<h2 id="identify-unhealthy-compute-accounts">Identify unhealthy compute accounts</h2>
<p>To identify unhealthy compute accounts:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Choose the integration you created for cloud scanning.</li>
<li>Select <strong>Manage compute accounts</strong>.</li>
</ol>
<p>CASB will display the status of each compute account next to its name. If a compute account is broken or outdated, CASB will set its status to <strong>Unhealthy</strong>. If the status is <strong>Healthy</strong>, no action is required.</p>
<h2 id="repair-an-unhealthy-compute-account">Repair an unhealthy compute account</h2>
<p>When CASB marks a compute account as <strong>Unhealthy</strong>, CASB will not use new scan configuration changes and new scan results will not appear in the dashboard.</p>
<p>To repair a compute account marked as <strong>Unhealthy</strong>, first <a href="#upgrade-a-compute-account">upgrade the compute account</a>. If the compute account is still unhealthy, <a href="#roll-api-tokens">roll your API token</a>.</p>
<h2 id="upgrade-a-compute-account">Upgrade a compute account</h2>
<p>Upgrading a compute account applies the latest software features, bug fixes, and infrastructure changes to a cloud compute account. You should run upgrades periodically to keep the compute account software up to date or when recommended by Cloudflare to address an issue. CASB deploys compute account upgrades through Terraform updates.</p>
<p>To upgrade a compute account:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Choose the integration you created for cloud scanning.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to validate your local Terraform and CLI configuration.</li>
<li>Under <strong>Step 2: Deploy Terraform Configuration</strong>, copy the template to your local configuration. This template will be the most up to date version of the integration's Terraform configuration.</li>
<li>In a local terminal, update the cached version of the CDS Terraform modules:</li>
</ol>
<pre><code class="language-bash">terraform init --upgrade&#10;</code></pre>
<ol start="7">
<li>Apply the upgraded Terraform configuration to your compute account:</li>
</ol>
<pre><code class="language-bash">terraform apply&#10;</code></pre>
<h2 id="roll-api-tokens">Roll API tokens</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5100.md")
</aside>
<p>You may need to roll the Cloudflare API token used for your compute account if a security or operational issue appears, your API token is compromised, or your API token is removed from your compute account.</p>
<p>If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<p>To roll your API token:</p>
<ol>
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Next to the API token you want to roll, select the <strong>three dot icon</strong> &gt; <strong>Roll</strong>.</p>
</li>
<li>
<p>Select <strong>Confirm</strong> to generate a new API token.</p>
</li>
<li>
<p>Copy your API token.</p>
</li>
</ol>
<p>Once you roll your API token in Cloudflare, you can update the API token value in your secrets manager for <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret-value.html">Amazon Web Services (AWS)</a> or <a href="https://cloud.google.com/secret-manager/docs/edit-secrets">Google Cloud Platform (GCP)</a>.</p>
<h3 id="common-token-issues">Common token issues</h3>
<h4 id="cloudflare-cds-secrets-does-not-exist-in-the-compute-account-s-secrets-manager"><code>cloudflare-cds-secrets</code> does not exist in the compute account's secrets manager</h4>
<p>To recreate the secret in your compute account:</p>
<ol>
<li>Validate that you selected the correct region.</li>
<li><a href="#upgrade-a-compute-account">Upgrade the compute account</a> to recreate the secret.</li>
<li><a href="#roll-api-tokens">Update the secret value</a> in your compute account.</li>
</ol>
<h4 id="i-no-longer-have-access-to-the-cloudflare-api-token-i-created">I no longer have access to the Cloudflare API token I created</h4>
<p><a href="#roll-api-tokens">Roll your Cloudflare API token</a> and add it to your compute account. If the <a href="#identify-unhealthy-compute-accounts">status of the compute account</a> is set to <strong>Healthy</strong>, the issue has been solved.</p>
