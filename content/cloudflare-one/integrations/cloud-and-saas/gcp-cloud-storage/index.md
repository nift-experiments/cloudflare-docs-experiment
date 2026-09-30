<p>The Google Cloud Platform (GCP) Cloud Storage integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated GCP account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A GCP account using Cloud Storage.</li>
<li>For initial setup, access to the GCP account with permission to create a new Service Account with the scopes listed below.</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the GCP Cloud Storage integration to function, Cloudflare CASB requires the following access scopes via a Service Account:</p>
<ul>
<li><code>roles/viewer</code></li>
<li><code>roles/storage.admin</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission scope, refer to the <a href="https://cloud.google.com/storage/docs/access-control/iam-roles">GCP IAM roles for Cloud Storage documentation</a>.</p>
<h2 id="compute-account">Compute account</h2>
<p>You can connect a GCP compute account to your CASB integration to perform <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a> scans within your Cloud Storage bucket and avoid data egress. CASB will scan any objects that exist in the bucket at the time of configuration.</p>
<h3 id="add-a-compute-account">Add a compute account</h3>
<p>To connect a compute account to your GCP integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Find and select your GCP integration.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to connect a new compute account.</li>
<li>Select <strong>Refresh</strong>.</li>
</ol>
<p>You can only connect one compute account to an integration. To remove a compute account, select <strong>Manage compute accounts</strong>.</p>
<h3 id="configure-compute-account-scanning">Configure compute account scanning</h3>
<p>Once your GCP compute account has successfully connected to your CASB integration, you can configure where and how to scan for sensitive data:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Find and select your GCP integration.</li>
<li>Select <strong>Create new configuration</strong>.</li>
<li>In <strong>Resources</strong>, choose the buckets you want to scan. Select <strong>Continue</strong>.</li>
<li>Choose the file types, sampling percentage, and <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to scan for.</li>
<li>(Optional) Configure additional settings, such as the limit of API calls over time for CASB to adhere to.</li>
<li>Select <strong>Continue</strong>.</li>
<li>Review the details of the scan, then select <strong>Start scan</strong>.</li>
</ol>
<p>CASB will take up to one hour to begin scanning. To view the scan results, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Content Findings</strong>.</p>
<p>To manage your resources, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>, then find and select your GCP integration. From here, you can pause all or individual scans, add or remove resources, and change scan settings.</p>
<p>For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#content-findings">Content findings</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The GCP Cloud Storage integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/gcp-cloud-storage.mdx.atom">RSS feed</a>.</p>
<h3 id="cloud-storage-bucket-security">Cloud Storage Bucket security</h3>
<p>Flag security issues in Cloud Storage Buckets, including overpermissioning, access policies, and user security best practices.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Cloud Platform: GCS Bucket Allows Public Write</td>
<td><code>4583f5a9-a343-4e2f-a8b3-9237a911f337</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket IAM Policy Allows Public Access</td>
<td><code>032c1e88-0cff-47f6-8d75-046e0a7330de</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Publicly Accessible</td>
<td><code>cc028a95-46d4-4156-ac11-bc5713529824</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: Public Access Prevention Enabled But Policy Grants Public</td>
<td><code>cc02680e-9cc3-49d1-99d5-29d425bf142f</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket ACL Grants All Authenticated Users Access</td>
<td><code>e1a588af-0500-482e-b59d-fd2693ce7fc0</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket ACL Grants All Users Public Access</td>
<td><code>1904c004-8d4f-470e-9460-e77db23d6a86</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: Public Access Prevention but ACL Grants allUsers</td>
<td><code>fcf2e27e-673f-4cd2-9b76-ec89c4c5872c</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Versioning Disabled</td>
<td><code>bd66e214-f205-4e00-bd68-121dad0a7988</code></td>
<td>High</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Without KMS Encryption</td>
<td><code>0105d9c4-1a01-4b65-b33e-df6c55905147</code></td>
<td>High</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Uniform Bucket-Level Access Disabled</td>
<td><code>6960b459-aa9e-4b41-84f6-26cdb75a1995</code></td>
<td>High</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket IAM Policy Allows Public Read</td>
<td><code>10420f34-8fdd-49cb-8d38-096a2de5824f</code></td>
<td>High</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Lacks Lifecycle Rules</td>
<td><code>edcd5a8b-b128-404b-8207-23a80f669b65</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Logging Disabled</td>
<td><code>d26f43c8-9406-481c-8c8b-1a7f05f3cc27</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Not Using 'Soft Delete'</td>
<td><code>5542ed8e-77a6-43c1-8b9e-935e66009d34</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket Retention Policy Disabled</td>
<td><code>2d4a247c-8adb-4f2b-ae58-3568d633cb81</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket IAM Policy Not Version 3</td>
<td><code>ade2ede6-08c7-4962-b084-f6a29ee4a5b8</code></td>
<td>Low</td>
</tr>
<tr>
<td>Google Cloud Platform: GCS Bucket IAM Policy Using Legacy Roles</td>
<td><code>11a592b9-4f51-4a1a-9925-a48a5ed01521</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
