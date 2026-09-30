<p>To get started with Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta) you need to give Cloudflare permission to interact with cloud providers on your behalf. You might have multiple provider accounts for the same cloud provider — for example, you might want Cloudflare to manage virtual private clouds (VPCs) belonging to two different AWS accounts.</p>
<p>Once Cloudflare has the credentials required to access your cloud environments, Multi-Cloud Networking will automatically begin discovering your cloud resources — like routing tables and virtual private networks. Discovered resources appear in your <a href="/multi-cloud-networking/manage-resources/#cloud-resource-catalog">Cloud resource catalog</a>.</p>
<h2 id="set-up-amazon-aws">Set up Amazon AWS</h2>
<h3 id="1-create-integration"><ol>
<li>Create integration</li>
</ol></h3>
<ol>
<li>Go to the <strong>Cloud integrations (beta)</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong> &gt; <strong>AWS integration</strong>.</li>
<li>Give a descriptive name to your integration. Optionally, you can also add a description for it.</li>
<li>Select <strong>Create integration</strong>.</li>
<li>Select <strong>Authorize access</strong> to start the process of connecting your Cloudflare account to Amazon AWS.</li>
</ol>
<h3 id="2-create-iam-policy"><ol start="2">
<li>Create IAM policy</li>
</ol></h3>
<ol>
<li>Create a <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html">custom IAM policy</a> in your AWS account, and take note of the name you entered. Then, paste the following <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html">JSON code</a> in the JSON tab:</li>
</ol>
<pre><code class="language-json">{&#10;    &quot;Version&quot;: &quot;2012-10-17&quot;,&#10;    &quot;Statement&quot;: [&#10;        {&#10;            &quot;Effect&quot;: &quot;Allow&quot;,&#10;            &quot;Action&quot;: [&#10;                &quot;ec2:AcceptTransitGatewayPeeringAttachment&quot;,&#10;                &quot;ec2:CreateTransitGatewayPeeringAttachment&quot;,&#10;                &quot;ec2:DeleteTransitGatewayPeeringAttachment&quot;,&#10;                &quot;ec2:DescribeRegions&quot;,&#10;                &quot;ec2:DescribeTransitGatewayPeeringAttachments&quot;,&#10;                &quot;ec2:RejectTransitGatewayPeeringAttachment&quot;,&#10;                &quot;ec2:GetManagedPrefixListEntries&quot;,&#10;                &quot;ec2:CreateManagedPrefixList&quot;,&#10;                &quot;ec2:ModifyManagedPrefixList&quot;,&#10;                &quot;ec2:DeleteManagedPrefixList&quot;,&#10;                &quot;ec2:CreateTransitGatewayPrefixListReference&quot;,&#10;                &quot;ec2:DeleteTransitGatewayPrefixListReference&quot;,&#10;                &quot;ec2:GetTransitGatewayPrefixListReferences&quot;,&#10;                &quot;ec2:ModifyTransitGatewayPrefixListReference&quot;&#10;            ],&#10;            &quot;Resource&quot;: &quot;*&quot;&#10;        }&#10;    ]&#10;}&#10;</code></pre>
<h3 id="3-authorize-access-to-your-aws-account"><ol start="3">
<li>Authorize access to your AWS account</li>
</ol></h3>
<ol>
<li>Create an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html">AWS role</a> with the following settings:
<ul>
<li><strong>Trusted entity type</strong>: Select <strong>Custom trust policy</strong>, and paste the custom trust policy returned by the Cloudflare dashboard.</li>
<li><strong>Permissions</strong>: Add the IAM policy you created in the previous step, along with these AWS-managed policies:
<ul>
<li><code>NetworkAdministrator</code></li>
<li><code>AmazonEC2ReadOnlyAccess</code></li>
<li><code>AmazonVPCReadOnlyAccess</code></li>
<li><code>IAMReadOnlyAccess</code></li>
</ul>
</li>
<li><strong>ARN</strong>: Copy the ARN for your newly created user.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/736.md")
</aside>
<ol start="2">
<li>Select <strong>I authorize Cloudflare to access my AWS account.</strong></li>
<li>Select <strong>Authorize</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/735.md")
</aside>
<h2 id="set-up-microsoft-azure">Set up Microsoft Azure</h2>
<h3 id="1-create-integration-1"><ol>
<li>Create integration</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Cloud integrations (beta)</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong> &gt; <strong>Azure integration</strong>.</li>
<li>Give a descriptive name to your integration. Optionally, you can also add a description for it.</li>
<li>Select <strong>Create integration</strong>.</li>
<li>Select <strong>Authorize access</strong> to start the process of connecting your Cloudflare account to Microsoft Azure.</li>
</ol>
<h3 id="2-authorize-access-to-your-azure-account"><ol start="2">
<li>Authorize access to your Azure account</li>
</ol></h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/734.md")
</aside>
<ol>
<li>Select <strong>Create service principal</strong>. You will be redirected to Microsoft's login page.</li>
<li>Enter your Azure credentials. If your account does not have administrator privileges, you may need to pass this link to an account that has administrator privileges.</li>
<li>The next screen lists Cloudflare required permissions to access your account. Select <strong>Accept</strong>.</li>
<li><a href="https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal">Add a role assignment</a>. The purpose of this step is to give the app that you registered in step 1 permission to access your Azure Subscription.
<ul>
<li>In step 3 of the linked document, select the <strong>Contributor</strong> role from the <strong>Privileged administrator roles</strong> tab.</li>
<li>In step 4 of the linked document, search for <code>mcn-provider-integrations-bot-prod</code> when selecting members.</li>
</ul>
</li>
<li>In <strong>Provide account information</strong>, enter your <strong>Tenant ID</strong> and <strong>Subscription ID</strong>.</li>
<li>In <strong>Verify account ownership</strong>, <a href="https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-portal">add the tags displayed in the Cloudflare dashboard</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/733.md")
</aside>
<ol start="7">
<li>Select <strong>I authorize Cloudflare to access my Azure account.</strong> If your account does not have administrator privileges, you may need to pass this link to an account that has administrator privileges.</li>
<li>Select <strong>Authorize</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/732.md")
</aside>
<h2 id="set-up-google-cloud">Set up Google Cloud</h2>
<h3 id="1-create-integration-2"><ol>
<li>Create integration</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Cloud integrations (beta)</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong> &gt; <strong>Google integration</strong>.</li>
<li>Give a descriptive name to your integration. Optionally, you can also add a description for it.</li>
<li>Select <strong>Create integration</strong>.</li>
<li>Select <strong>Authorize access</strong> to start the process of connecting your Cloudflare account to Google Cloud.</li>
</ol>
<h3 id="2-authorize-access-to-your-google-account"><ol start="2">
<li>Authorize access to your Google account</li>
</ol></h3>
<ol>
<li>Create a new <a href="https://cloud.google.com/iam/docs/service-accounts-create">GCP service account</a> in your <strong>Google account</strong> &gt; <strong>GCP Console</strong> &gt; <strong>IAM &amp; Admin</strong> &gt; <strong>Service Accounts</strong>.</li>
<li>Grant the new service account these roles:
<ul>
<li><code>Compute Network Admin</code></li>
<li><code>Compute Viewer</code></li>
</ul>
</li>
<li>Under <strong>IAM &amp; Admin</strong> &gt; <strong>Service Accounts</strong>, select the service account you just created, and navigate to the <strong>Permissions</strong> tab.</li>
<li>Grant the <strong>Service Account Token Creator</strong> role to our bot account to allow it to impersonate this service account. Learn how to grant a specific role <a href="https://cloud.google.com/iam/docs/manage-access-service-accounts#grant-single-role">in Google's documentation</a>:
<ul>
<li><code>mcn-integrations-bot-prod@mcn-gcp-01.iam.gserviceaccount.com</code></li>
</ul>
</li>
<li>In the <strong>service account email field</strong>, enter the email account that you used to create the GCP service account.</li>
<li>In the <strong>Project ID field</strong>, enter the <a href="https://support.google.com/googleapi/answer/7014113?hl=en">project ID</a> associated with your project.</li>
<li><a href="https://cloud.google.com/resource-manager/docs/creating-managing-labels#create-labels">Add the label</a> displayed in the dashboard of your project.</li>
<li>Select <strong>I authorize Cloudflare to access my GCP account.</strong> If your account does not have administrator privileges, you may need to pass this link to an account that has administrator privileges.</li>
<li>Select <strong>Authorize</strong>.</li>
</ol>
<p>You have successfully connected your cloud provider to Multi-Cloud Networking. Cloud resources found by Multi-Cloud Networking are available in the <a href="/multi-cloud-networking/manage-resources/#cloud-resource-catalog">Cloud resource catalog</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/731.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/multi-cloud-networking/cloud-on-ramps/">Set up Cloudflare WAN</a> as an on-ramp to your cloud.</li>
<li><a href="/multi-cloud-networking/manage-resources/">Manage resources</a> found by Multi-Cloud Networking.</li>
<li><a href="/multi-cloud-networking/manage-resources/#edit-cloud-integrations">Edit</a> cloud integrations.</li>
</ul>
