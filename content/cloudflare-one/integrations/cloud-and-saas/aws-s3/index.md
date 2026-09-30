<p>The Amazon Web Services (AWS) S3 integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated AWS account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>An AWS account using AWS S3 (Simple Storage Service)</li>
<li>For initial setup, access to the AWS account with permission to create a new IAM Role with the scopes listed below.</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the AWS S3 integration to function, Cloudflare CASB requires the following access scopes via an IAM Role with cross-account access:</p>
<ul>
<li><code>s3:PutBucketNotification</code></li>
<li><code>s3:GetObject</code></li>
<li><code>s3:ListBucket</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission scope, refer to the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html">AWS S3 Permissions documentation</a>.</p>
<h2 id="compute-account">Compute account</h2>
<p>You can connect an AWS compute account to your CASB integration to perform <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a> scans within your S3 bucket and avoid data egress. CASB will scan any objects that exist in the bucket at the time of configuration.</p>
<h3 id="add-a-compute-account">Add a compute account</h3>
<p>To connect a compute account to your AWS integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find and select your AWS integration.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to connect a new compute account.</li>
<li>Select <strong>Refresh</strong>.</li>
</ol>
<p>You can only connect one computer account to an integration. To remove a compute account, select <strong>Manage compute accounts</strong>.</p>
<h3 id="configure-compute-account-scanning">Configure compute account scanning</h3>
<p>Once your AWS compute account has successfully connected to your CASB integration, you can configure where and how to scan for sensitive data:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Find and select your AWS integration.</li>
<li>Select <strong>Create new configuration</strong>.</li>
<li>In <strong>Resources</strong>, choose the buckets you want to scan. Select <strong>Continue</strong>.</li>
<li>Choose the file types, sampling percentage, and <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to scan for.</li>
<li>(Optional) Configure additional settings, such as the limit of API calls over time for CASB to adhere to.</li>
<li>Select <strong>Continue</strong>.</li>
<li>Review the details of the scan, then select <strong>Start scan</strong>.</li>
</ol>
<p>CASB will take up to an hour to begin scanning. To view the scan results, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Content Findings</strong>.</p>
<p>To manage your resources, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>, then find and select your AWS integration. From here, you can pause all or individual scans, add or remove resources, and change scan settings.</p>
<p>For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#content-findings">Content findings</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The AWS S3 integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/aws-s3.mdx.atom">RSS feed</a>.</p>
<h3 id="s3-bucket-security">S3 Bucket security</h3>
<p>Flag security issues in S3 Buckets, including overpermissioning, access policies, and user security best practices.</p>
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
<td>S3 Bucket ACL Allows Any Authenticated User to Write</td>
<td><code>09bc7d1f-e682-43bc-a4ce-e6e03b408244</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Any Authenticated User to Write ACP</td>
<td><code>9392a460-c566-4e0d-b06b-01d87dc84d7c</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Public ACP Write</td>
<td><code>5b792c7f-2546-4fcd-96dc-a58a53fea7e0</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Public Write</td>
<td><code>f50ae197-fa0a-4caa-be95-79aed91eed63</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Any Authenticated User to Write</td>
<td><code>70fe0596-28bc-41dd-a2c3-1486fb0fb1dd</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Public Write</td>
<td><code>5e2aac4b-d8be-43dc-b324-84fdf63f760e</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket Publicly Accessible</td>
<td><code>6b1276e3-88e8-4150-a4d5-1b8273f11078</code></td>
<td>Critical</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Any Authenticated User to Read</td>
<td><code>fda31c4d-24dc-43d4-8a84-a1a9e1df01a1</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Any Authenticated User to Read ACP</td>
<td><code>7232e46b-3539-4080-b905-022f1091556c</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Public ACP Read</td>
<td><code>e324242c-5feb-41a3-8d91-f70611471fad</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Public Read</td>
<td><code>f8c9f979-29f0-4ada-b09e-a149937a55d4</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Any Authenticated User to Read</td>
<td><code>c6b3a745-b535-45ea-b2c0-ba8a139ca634</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Public Read</td>
<td><code>f3915412-eef9-47d9-8448-e04462de8ba2</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket Without MFA Delete Enabled</td>
<td><code>f108bd28-9870-453f-a439-01818e85bdc7</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket Without Server-Side Encryption (SSE)</td>
<td><code>7817b383-79c3-44ca-8d5d-e01748afe75b</code></td>
<td>High</td>
</tr>
<tr>
<td>S3 Bucket Encryption in Transit Disabled</td>
<td><code>0b3227dd-63d3-46bc-97b3-e62d9c11567a</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket MFA Delete Disabled</td>
<td><code>518697ff-3f7e-463e-acf3-79d106599f0e</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket ACL Allows Public List</td>
<td><code>e3c8a170-7817-4151-bd01-55442f4416ea</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Objects Can Be Public</td>
<td><code>0ff170dc-be6b-46fa-a1cf-95ca7d067f4b</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Any Authenticated AWS User</td>
<td><code>264be783-7fe1-4f50-aee7-d8df370b7b77</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Any Authenticated User to Delete</td>
<td><code>4431eaeb-63e3-43c1-a4bc-029f09da66fd</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Any Authenticated User to List</td>
<td><code>319c9715-b86d-4215-bdfa-c5d9b3a5cc83</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Public Delete</td>
<td><code>bbbeacbc-6692-4121-a785-d634da1e5c56</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Policy Allows Public List</td>
<td><code>f7ae03e3-1303-4404-b6f5-a7f97e52105e</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Server Side Encryption Disabled</td>
<td><code>d69ab398-fba8-4e71-bf49-60af48d00cbc</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Access Logging</td>
<td><code>67d0995d-7b4a-40c5-a43f-7a98d20faac6</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without AWS CloudTrail Logging</td>
<td><code>89366ebe-ca0b-45fc-a9cb-135674e0a49b</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Cross-Region Replication</td>
<td><code>d4e5c815-33e3-4a01-b852-fe040d51ee55</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Default Encryption</td>
<td><code>fb7a41af-294c-4e9b-a6ca-a1fed35542d6</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Lifecycle Policies</td>
<td><code>2df6f1b8-e41c-4ab5-a466-992ce485a367</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Object-Level Logging</td>
<td><code>9af2594c-3999-49c9-bd3d-2f4b091f99c0</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Replication Enabled</td>
<td><code>cb61ef18-a498-456c-985c-78a45e19f4fe</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Without Versioning Enabled</td>
<td><code>95e1284f-a514-4396-bf64-cd003818790c</code></td>
<td>Medium</td>
</tr>
<tr>
<td>S3 Bucket Access Logging Disabled</td>
<td><code>84ba76fa-4703-490e-ab75-1b554993c054</code></td>
<td>Low</td>
</tr>
<tr>
<td>S3 Bucket Lifecycle Disabled</td>
<td><code>970d2ca8-e189-42a8-8e86-9f674fcb1aea</code></td>
<td>Low</td>
</tr>
<tr>
<td>S3 Bucket Policy Not Existent</td>
<td><code>3e1d0535-d82f-4ed1-9664-d2c50905db17</code></td>
<td>Low</td>
</tr>
<tr>
<td>S3 Bucket Versioning Disabled</td>
<td><code>4e976e0d-b545-4c4a-99c5-a2f5d9a6f3d8</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="iam-policies">IAM Policies</h3>
<p>Identify AWS IAM-related security issues that could affect S3 Bucket and Object security.</p>
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
<td>IAM Account Password Policy Does Not Exist</td>
<td><code>e39ee4da-eed5-49d0-95f7-b423884b858c</code></td>
<td>Critical</td>
</tr>
<tr>
<td>IAM Account Password Policy Doesn't Require Lowercase Letters</td>
<td><code>9278444b-0c38-4ed0-8127-f3f25444811c</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Account Password Policy Doesn't Require Passwords to Expire</td>
<td><code>5be79a96-4570-45cf-8ba3-1abe62802d16</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Account Password Policy Doesn't Require Symbols</td>
<td><code>dd17afa3-4d4c-49e4-84c3-e829af9fff97</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Account Password Policy Doesn't Require Uppercase Letters</td>
<td><code>e4976e53-bab5-4276-a1d3-1d85ebfd4d57</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Account Password Policy Max Age is greater than 90 days</td>
<td><code>4e1092a0-7092-405f-a991-537d8c371440</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Account Password Policy Minimum Length is less than 8</td>
<td><code>2a2fa181-7beb-48ba-bc8d-8f1170c6062c</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Account Password Policy Re-use Prevention is less than 5</td>
<td><code>a4791a20-373f-44d3-9f6e-e61f1685fe05</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Role with Cross-Account Access</td>
<td><code>8de72710-b23a-4d94-915e-26ef7249d21e</code></td>
<td>High</td>
</tr>
<tr>
<td>IAM Access Key Inactive over 90 Days</td>
<td><code>37d1adb1-8e37-4708-a849-e06945c60802</code></td>
<td>Medium</td>
</tr>
<tr>
<td>IAM Access Key Not Rotated over 90 Days</td>
<td><code>d2caf571-4c99-4da7-a21c-4384f8cb4e5c</code></td>
<td>Medium</td>
</tr>
<tr>
<td>IAM User Console Login Inactive Over 90 Days</td>
<td><code>82b50a4d-8582-4766-9bad-f41b441bf336</code></td>
<td>Medium</td>
</tr>
<tr>
<td>IAM User MFA Disabled</td>
<td><code>4679563f-5975-4c68-9dbf-896810ec8de9</code></td>
<td>Medium</td>
</tr>
<tr>
<td>IAM User Password Older Than 90 Days</td>
<td><code>c5376384-e4e4-4b2c-af84-12d6740939f0</code></td>
<td>Medium</td>
</tr>
<tr>
<td>IAM Account Password Policy Doesn't Require Numbers</td>
<td><code>15c65813-c7e6-4b22-95b3-b3942c8b8924</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="root-user-management">Root User Management</h3>
<p>Detect security issues related to the use of an IAM Root User, which has the ability to access and configure important settings.</p>
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
<td>AWS Root User Access Key Used within Last 90 Days</td>
<td><code>9d23c002-aece-42b5-b082-2b51fab8d7c1</code></td>
<td>Critical</td>
</tr>
<tr>
<td>AWS Root User has Access Keys</td>
<td><code>1b788d31-ed56-4008-b136-6993f38e4d1c</code></td>
<td>Critical</td>
</tr>
<tr>
<td>AWS Root User Logged in within Last 90 Days</td>
<td><code>e9959d6e-edc9-4ea3-9113-3c30b02a811e</code></td>
<td>Critical</td>
</tr>
<tr>
<td>AWS Root User MFA Disabled</td>
<td><code>19abe0ee-e8bd-4e3b-9ee9-ea5c64fe769c</code></td>
<td>Critical</td>
</tr>
</tbody>
</table>
<h3 id="certificates">Certificates</h3>
<p>Catch certificate-related issues and risks to prevent malicious compromise of internal resources.</p>
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
<td>ACM Certificate Expired</td>
<td><code>30ce0a22-eb3d-457d-bc59-6468f9bb4c4f</code></td>
<td>Critical</td>
</tr>
<tr>
<td>ACM Certificate Has Domain Wildcard</td>
<td><code>d313bc0c-a2fb-41d8-b5a8-ef2704bb5570</code></td>
<td>High</td>
</tr>
<tr>
<td>ACM Certificate Expires within 30 days</td>
<td><code>cd93f2c1-9b07-4e6c-964c-79f3a64d56ac</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
