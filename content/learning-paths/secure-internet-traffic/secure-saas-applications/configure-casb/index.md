<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10039.md")
</aside>
<div class="nb-glossary-definition"><p>Cloudflare CASB provides comprehensive visibility and control over SaaS apps to prevent data leaks and compliance violations. It helps detect insider threats, shadow IT, risky data sharing, and bad actors.</p></div>
<p>Cloudflare's API-implemented CASB addresses the final, common security concern for administrators of SaaS applications or security organizations: How can I get insights into the existing configurations of my SaaS tools and proactively address issues before there is an incident? CASB integrates with a number of leading SaaS applications and surfaces instant security insights related to misconfiguration and potential for data loss. CASB also powers <a href="/cloudflare-one/team-and-resources/users/risk-score/">risk score heuristics</a> organized by severity.</p>
<p>For more information on Cloudflare CASB, including available SaaS integrations, refer to <a href="/cloudflare-one/integrations/cloud-and-saas/">Scan SaaS applications</a>.</p>
<h2 id="manage-casb-integrations">Manage CASB integrations</h2>
<p>When you integrate a third-party SaaS application or cloud environment with Cloudflare CASB, you allow CASB to make API calls to its endpoint and read relevant data on your behalf. The CASB integration permissions are read-only and follow the least privileged model. In other words, only the minimum access required to perform a scan is granted.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before you can integrate a SaaS application or cloud environment with CASB, your account with that integration must meet certain requirements. Refer to the SaaS application or cloud environment's <a href="/cloudflare-one/integrations/cloud-and-saas/">integration guide</a> to learn more about the prerequisites and permissions.</p>
<h3 id="add-an-integration">Add an integration</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Select <strong>Connect an integration</strong> or <strong>Add integration</strong>.</li>
<li>Browse the available integrations and select the application you would like to add.</li>
<li>Follow the step-by-step integration instructions in the UI.</li>
<li>To run your first scan, select <strong>Save integration</strong>.</li>
</ol>
<p>After the first scan, CASB will automatically scan your SaaS application or cloud environment on a frequent basis to keep up with any changes. Scan intervals will vary due to each application having their own set of requirements, but the frequency is typically between every 1 hour and every 24 hours.</p>
<p>Once CASB detects at least one finding, you can <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">view and manage your findings</a>.</p>
<h3 id="pause-an-integration">Pause an integration</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find the integration you would like to pause and select <strong>Configure</strong>.</li>
<li>To stop scanning the application, turn off <strong>Scan for findings</strong>.</li>
<li>Select <strong>Save integration</strong>.</li>
</ol>
<p>You can resume CASB scanning at any time by turning on <strong>Scan for findings</strong>.</p>
<h3 id="delete-an-integration">Delete an integration</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10038.md")
</aside>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find the integration you would like to delete and select <strong>Configure</strong>.</li>
<li>Select <strong>Disenroll</strong>.</li>
</ol>
<p>To resume scanning the integration for findings, you will need to <a href="#add-an-integration">add the integration</a> again.</p>
<h3 id="integrate-dlp-policies">Integrate DLP policies</h3>
<p>If you use both Cloudflare CASB and Cloudflare Data Loss Prevention (DLP), you can use DLP to discover if files stored in your SaaS application contain sensitive data. CASB integrations supported by DLP include:</p>
<ul>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/">Amazon Web Services (AWS) S3</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/box/">Box</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/dropbox/">Dropbox</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/gcp-cloud-storage">Google Cloud Platform (GCP) Cloud Storage</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive/">Google Drive</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/onedrive/">Microsoft OneDrive</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint/">Microsoft SharePoint</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/">Microsoft 365 Copilot</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/openai/">OpenAI</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">Anthropic</a></li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">Scan SaaS applications with DLP</a>.</p>
