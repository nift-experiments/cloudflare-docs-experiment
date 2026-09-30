---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/
  description: Ingest Cloudflare logs into Microsoft Sentinel.
  full_title: Sentinel · Cloudflare Analytics docs
  head_html: <title>Sentinel · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Ingest Cloudflare logs into Microsoft Sentinel."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/index.md"><meta property="og:title" content="Sentinel · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Ingest Cloudflare logs into Microsoft Sentinel."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Analytics,Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#page","headline":"Sentinel \u00b7 Cloudflare Analytics docs","description":"Ingest Cloudflare logs into Microsoft Sentinel.","url":"https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-integrations/sentinel/
  schema: 1
---
<p>Cloudflare has integrations with Microsoft Sentinel to make analyzing your Cloudflare data easier and in a centralized space. Cloudflare has two versions of this connector available. We recommend utilizing the latest Codeless Connector integration as it provides easier setup, cost management, and integrates with <a href="https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview">Sentinel Data Lake</a>.</p>
<p><strong><a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Sentinel CCF Solution</a></strong> (recommended): The Codeless Connector Framework (CCF) provides partners, advanced users, and developers the ability to create custom connectors for ingesting data to Microsoft Sentinel.</p>
<p><strong><a href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cloudflare.cloudflare_sentinel?tab=Overview">Sentinel Function Based Connector</a></strong>: The Cloudflare connector for Microsoft Sentinel uses <a href="https://azure.microsoft.com/en-us/products/functions">Azure Functions</a> to process security logs from Cloudflare's Logpush service and ingest them directly into the SIEM platform.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="legacy-connector-deprecation">Legacy connector deprecation</h3>
@markup("md", "content/.markup/bodies/3155.md")
</aside>
<p>This guide provides clear, step-by-step instructions for integrating Cloudflare logs with the CCF connector for Microsoft Sentinel using Azure Blob Storage. By following these steps, you will be able to securely collect, store, and analyze your Cloudflare logs within Microsoft Sentinel, enhancing your organization's security monitoring and incident response capabilities.</p>
<h2 id="step-1-prerequisites">Step 1: Prerequisites</h2>
<p>Before you begin, make sure the following prerequisites are met.</p>
<h3 id="azure-resources">Azure resources</h3>
<ul>
<li><strong>Azure subscription</strong> with permission to create and manage resources (<code>Contributor</code> or <code>Owner</code> role recommended).</li>
<li><strong>Azure Storage account</strong> with <a href="https://learn.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account">Azure Data Lake Storage Gen2 enabled</a> (hierarchical namespace on). Although the generic Logpush Azure destination supports standard Blob Storage, the CCF connector requires hierarchical namespace. Logpush writes the Cloudflare log files to this account.</li>
<li><strong>Azure Blob container</strong> inside the storage account, dedicated to receiving Cloudflare Logpush files. The CCF connector monitors this container for new files via Event Grid.</li>
<li><strong>Microsoft Sentinel workspace</strong> already deployed on top of a Log Analytics workspace. The connector's Data Collection Rule (DCR) and Data Collection Endpoint (DCE) are tied to this Log Analytics workspace, and all ingested Cloudflare log records land in tables within it.</li>
<li><strong>Cloudflare account</strong> with access to the domain or account whose logs you want to export, and permission to configure Logpush jobs.</li>
</ul>
<h3 id="rbac-roles">RBAC roles</h3>
<p>The CCF connector authenticates to Azure using a service principal that belongs to the Cloudflare CCF connector application, registered as a multi-tenant Microsoft Entra application. The ARM template that deploys the connector assigns the required roles to this service principal automatically.</p>
<p>The deploying user must have <strong>Microsoft Sentinel Contributor</strong>, <code>Contributor</code>, or <code>Owner</code> on the Microsoft Sentinel workspace to deploy the connector resources. Because the ARM template creates role assignments for the service principal, the user must also have <code>Owner</code> or <code>User Access Administrator</code> at the storage account scope. <code>Contributor</code> and <strong>Microsoft Sentinel Contributor</strong> alone cannot create role assignments.</p>
<p>At deployment time, the Cloudflare CCF connector service principal receives <code>Storage Blob Data Reader</code> on the storage account to read log files from the Blob container and <code>Storage Queue Data Contributor</code> to read and delete pointer messages from the Storage Queue.</p>
<p>Refer to the Microsoft documentation on <a href="https://learn.microsoft.com/en-us/azure/sentinel/roles">Azure roles for Microsoft Sentinel</a> and <a href="https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access">Azure roles for storage</a> for details.</p>
<h3 id="event-grid-resource-provider">Event Grid resource provider</h3>
<p>The <code>Microsoft.EventGrid</code> resource provider must be registered in the subscription that hosts the storage account. Verify the registration state in the Azure portal under <strong>Subscriptions</strong> &gt; select the subscription &gt; <strong>Settings</strong> &gt; <strong>Resource providers</strong> &gt; search for <code>Microsoft.EventGrid</code>.</p>
<p>Alternatively, run the following Azure CLI commands:</p>
<pre tabindex="0"><code class="language-sh">az provider register --namespace Microsoft.EventGrid --subscription &lt;subscription-id&gt;&#10;az provider show --namespace Microsoft.EventGrid --subscription &lt;subscription-id&gt; --query &quot;registrationState&quot;&#10;</code></pre>
<p>The registration state should report <code>Registered</code> before you continue.</p>
<h3 id="network-access-configuration">Network access configuration</h3>
<p>By default, the storage account must allow public network access so that the connector's managed resources can reach both the Blob container endpoint and the Storage Queue endpoint.</p>
<ul>
<li>If you are not restricting access with a Network Security Perimeter (NSP), open the storage account's <strong>Networking</strong> blade and set <strong>Public network access</strong> to <strong>Enabled from all networks</strong>.</li>
<li>Restricting access using selected virtual networks or IPv4 CIDR ranges is not supported for this connector, because of Azure Storage firewall limitations around IP ranges and caller region affinity.</li>
<li>If network restrictions are required for compliance, use an <a href="https://learn.microsoft.com/en-us/azure/private-link/network-security-perimeter-concepts">Azure Network Security Perimeter (NSP)</a> instead. Include the Sentinel service tag inbound ranges in the NSP rules and configure the Event Grid system topic subscription to use system-assigned managed identity delivery.</li>
</ul>
<p>Refer to Microsoft's guidance on <a href="https://learn.microsoft.com/en-us/azure/sentinel/enable-storage-network-security">enabling storage network security for Sentinel</a> for the full options.</p>
<h3 id="storage-account-and-sentinel-co-location">Storage account and Sentinel co-location</h3>
<p>The Azure Blob Storage account and the Microsoft Sentinel workspace must live in the <strong>same Azure subscription and the same resource group</strong>. Deployments where these resources are split across subscriptions or resource groups fail during ARM template validation. Refer to <a href="#troubleshooting">Troubleshooting</a> for details.</p>
<h2 id="step-2-set-up-a-logpush-job">Step 2: Set up a Logpush job</h2>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</p>
</li>
<li>
<p>Go to <strong>Analytics</strong> &gt; <strong>Logs</strong> and select <strong>Logpush</strong>.</p>
</li>
<li>
<p>Select <strong>Create Logpush Job</strong>. Choose the log type you want to export (for example, <strong>HTTP requests</strong>).</p>
</li>
<li>
<p>For the destination, select <strong>Azure Blob Storage</strong>.</p>
</li>
<li>
<p>Enter your Azure Blob Storage details:</p>
<ul>
<li>SAS Token (Shared Access Signature)</li>
</ul>
<p>To generate a SAS token from the Azure portal, first navigate to your storage account. Under the <strong>Data Storage</strong> section, select <strong>Containers</strong> and choose the relevant container. Within the settings, locate and select <strong>Shared access signature</strong>. Configure the required permissions, such as <code>write</code> and <code>create</code>, and specify the start and expiration dates for the token. Once configured, generate the SAS token accordingly.</p>
</li>
<li>
<p>Save and activate the Logpush job.</p>
</li>
</ol>
<p>For complete details, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/azure/">Cloudflare Logpush to Azure documentation</a>.</p>
<h2 id="step-3-install-the-cloudflare-ccf-solution">Step 3: Install the Cloudflare CCF solution</h2>
<ol>
<li>Log in to the Azure portal and open your Microsoft Sentinel workspace. If you do not have one yet, follow Microsoft's <a href="https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard">onboarding guide</a> to create a Log Analytics workspace and enable Microsoft Sentinel on it.</li>
<li>In the left navigation pane, under <strong>Content management</strong>, select <strong>Content hub</strong>. If the page appears empty, refresh and wait for the content list to load.</li>
<li>In the search bar, enter <code>Cloudflare</code> and press <strong>Enter</strong>.</li>
<li>Select the <strong>Cloudflare CCF</strong> solution and select <strong>Install</strong>.</li>
<li>After you install the solution, select <strong>Manage</strong>.</li>
<li>Select <strong>Cloudflare (Using Blob Container) (via Codeless Connector Framework)</strong> and select <strong>Open connector page</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/azure-portal.png" alt="Azure portal" /></p>
<h2 id="step-4-configure-the-ccf-connector">Step 4: Configure the CCF connector</h2>
<p>On the connector page, fill in the following fields:</p>
<ul>
<li><strong>Service Principal ID</strong>: this field is prepopulated with the object ID of the Cloudflare CCF connector service principal in your tenant. If it is empty, ensure that admin consent has been granted for the Cloudflare CCF connector application in your Microsoft Entra tenant, then reload the page. Refer to Microsoft's <a href="https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow">admin consent workflow</a> for details.</li>
<li><strong>Blob Container URL</strong>: in the Azure portal, open the storage account that receives Cloudflare logs. Under <strong>Data storage</strong> &gt; <strong>Containers</strong>, open the target container, go to <strong>Properties</strong>, and copy the URL.</li>
<li><strong>Storage Account Resource Group Name</strong>, <strong>Storage Account Location</strong>, and <strong>Storage Account Subscription ID</strong>: available on the storage account's <strong>Overview</strong> page.</li>
<li><strong>Event Grid System Topic Name</strong>: leave this field blank on the first deployment. The ARM template creates the topic automatically. If you are reconfiguring an existing deployment, open <strong>Event Grid</strong> &gt; <strong>System topics</strong> in the Azure portal, filter by location, and copy the name of the topic whose <strong>Source</strong> matches your storage account.</li>
</ul>
<p>Select <strong>Connect</strong> to start the deployment. When the deployment completes, the Azure portal shows a <code>Deployment succeeded</code> notification and the button changes to <strong>Disconnect</strong>.</p>
<p><img src="/assets/upstream/images/analytics/configuration.png" alt="Configuration fields" /></p>
<h2 id="step-5-verify-log-ingestion">Step 5: Verify log ingestion</h2>
<ol>
<li>In the Azure portal, open the Log Analytics workspace backing your Sentinel instance.</li>
<li>In the left navigation pane, select <strong>Logs</strong>.</li>
<li>Enter the following query in the editor and select <strong>Run</strong>:</li>
</ol>
<pre tabindex="0"><code class="language-kusto">CloudflareV2_CL&#10;| take 10&#10;</code></pre>
<ol start="4">
<li>Confirm that Cloudflare log records are returned.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3154.md")
</aside>
<p><img src="/assets/upstream/images/analytics/data-connectors.png" alt="Data connectors" /></p>
<p><img src="/assets/upstream/images/analytics/traffic-overview.png" alt="Cloudflare traffic overview" /></p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="createdataflowresources-deployment-error"><code>CreateDataFlowResources</code> deployment error</h3>
<p>The ARM template deployment fails with an error similar to:</p>
<pre tabindex="0"><code class="language-txt">InvalidTemplate: Deployment template validation failed:&#10;&#x27;The resource &#x27;Microsoft.Resources/deployments/CreateDataFlowResources&#x27; is not defined in the template.&#x27;&#10;</code></pre>
<p>The CCF connector's ARM template operates within a single resource group scope and cross-references the storage account, Blob container, Event Grid system topic, Storage Queue, Data Collection Rule (DCR), Data Collection Endpoint (DCE), and Microsoft Sentinel workspace as co-located resources. If any of those resources live outside the deployment scope, the template cannot resolve the references and validation fails before anything is created.</p>
<p>To resolve the error:</p>
<ol>
<li><strong>Verify co-location</strong>: in the Azure portal, open both the storage account and the Microsoft Sentinel workspace (or its underlying Log Analytics workspace) and confirm that <strong>Resource group</strong> and <strong>Subscription</strong> match on the <strong>Overview</strong> blade. If they differ, move the storage account into the resource group that hosts Sentinel, or create a new storage account in that resource group.</li>
<li><strong>Verify network access</strong>: confirm that public network access is enabled on the storage account, or that a Network Security Perimeter is configured as described in <a href="#network-access-configuration">Prerequisites</a>. Selected network limits using IPv4 CIDR addresses are not supported.</li>
<li><strong>Retry the deployment</strong>: after you align the resources, re-run the ARM template deployment. The <code>CreateDataFlowResources</code> error should not recur.</li>
</ol>
<p>For the full list of storage-related failure modes and mitigations, refer to Microsoft's <a href="https://learn.microsoft.com/en-us/azure/sentinel/azure-storage-blob-connector-troubleshoot">Azure Storage Blob connector troubleshooting guide</a>.</p>
<h2 id="supported-logs">Supported Logs</h2>
<p>We support the following fields to be utilized within the Sentinel Connectors (CCF &amp; Function based). You can push all log fields to Azure using our logpush function as described in <a href="/logs/logpush/logpush-job/enable-destinations/azure/">Enable Microsoft Azure</a> documentation.</p>
<p>The CCF connector normalizes Cloudflare log fields to the <a href="https://learn.microsoft.com/en-us/azure/sentinel/normalization">Microsoft Sentinel ASIM schema</a> where a canonical equivalent exists (for example, <code>ClientIP</code> becomes <code>SrcIpAddr</code>, <code>EdgeResponseStatus</code> becomes <code>HttpStatusCode</code>), and preserves Cloudflare-native names for fields that do not have a schema equivalent. Use the field names in the following tables in your KQL queries against the connector's output table.</p>
<details class="nb-details"><summary>Parser fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3156.md")
</div></details>
<details class="nb-details"><summary>Workbook fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3157.md")
</div></details>
<details class="nb-details"><summary>Analytic rules</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3158.md")
</div></details>
<details class="nb-details"><summary>Hunting queries</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3159.md")
</div></details>
<h2 id="resources">Resources</h2>
<p><a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Download Cloudflare's CCF Sentinel Solution</a><br />
<a href="https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview">Microsoft Data Lake Overview</a><br />
<a href="https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector">About the CCF Platform</a></p>
