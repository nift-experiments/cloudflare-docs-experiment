<p>Use this guide to resolve common issues when integrating Cloudflare logs with <a href="/analytics/analytics-integrations/sentinel/">Microsoft Sentinel</a> through the Codeless Connector Framework (CCF).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="support-scope">Support scope</h3>
@markup("md", "content/.markup/bodies/3153.md")
</aside>
<h2 id="connector-deployment-fails-with-internalservererror-http-500">Connector deployment fails with <code>InternalServerError (HTTP 500)</code></h2>
<p><strong>Cause:</strong> The Microsoft-managed service principal required by the Cloudflare CCF connector has not been provisioned in your Microsoft Entra ID tenant. This typically happens when the <strong>Grant tenant-wide admin consent</strong> button on the connector configuration page cannot complete the OAuth redirect — for example, due to browser extensions, a cached session, a conflicting signed-in account, a Conditional Access policy, or an unmet Multi-Factor Authentication (MFA) challenge.</p>
<p><strong>Fix:</strong></p>
<ol>
<li>Confirm that the <code>Microsoft.SecurityInsights</code> resource provider is registered on your subscription:</li>
</ol>
<pre><code class="language-sh">az provider show --namespace Microsoft.SecurityInsights --query &quot;{state:registrationState}&quot;&#10;</code></pre>
<p>The output should return <code>&quot;state&quot;: &quot;Registered&quot;</code>.</p>
<ol start="2">
<li>In an <strong>InPrivate/Incognito</strong> browser session, sign in as a user holding one of these Microsoft Entra roles: <strong>Privileged Role Administrator</strong>, <strong>Cloud Application Administrator</strong>, <strong>AI Administrator</strong>, or <strong>Application Administrator</strong>.</li>
<li>Open the direct tenant-wide admin consent URL for the Microsoft-managed application (App ID <code>4f05ce56-95b6-4612-9d98-a45c8cc33f9f</code>), replacing <code>{tenant-id}</code> with your Entra tenant ID:</li>
</ol>
<pre><code class="language-txt">https://login.microsoftonline.com/{tenant-id}/adminconsent?client_id=4f05ce56-95b6-4612-9d98-a45c8cc33f9f&#10;</code></pre>
<ol start="4">
<li>Complete the consent flow, including any MFA challenge.</li>
</ol>
<p><strong>Verify:</strong> Refresh the Cloudflare connector configuration page in Microsoft Sentinel. The <strong>Service Principal ID</strong> field should populate automatically, and the <strong>Grant tenant-wide admin consent</strong> button should no longer be displayed. Retry the connector deployment.</p>
<h2 id="deployment-fails-with-invalidtemplate-on-createdataflowresources">Deployment fails with <code>InvalidTemplate</code> on <code>CreateDataFlowResources</code></h2>
<p>You see a deployment failure with an error similar to:</p>
<pre><code class="language-txt">Deployment template validation failed: &#x27;The resource&#10;&#x27;Microsoft.Resources/deployments/CreateDataFlowResources&#x27;&#10;is not defined in the template.&#x27;&#10;</code></pre>
<p><strong>Cause:</strong> The ARM template requires the Azure Blob Storage account and the Microsoft Sentinel workspace (and its underlying Log Analytics workspace) to reside in the <strong>same Azure subscription and the same resource group</strong>. When they are in different subscriptions or different resource groups, the nested <code>CreateDataFlowResources</code> sub-deployment cannot resolve the required resource references and validation fails.</p>
<p>A less common variant of this error occurs when the <code>Microsoft.EventGrid</code> resource provider is not registered in the target subscription.</p>
<p><strong>Fix:</strong></p>
<ol>
<li>Confirm that both resources are co-located in the same Azure subscription and the same resource group. If they are not, redeploy or migrate them so they share both.</li>
<li>Register the required resource providers on the target subscription:</li>
</ol>
<pre><code class="language-sh">az provider register --namespace Microsoft.SecurityInsights&#10;az provider register --namespace Microsoft.EventGrid&#10;</code></pre>
<ol start="3">
<li>
<p>After deployment, confirm that the Microsoft-managed service principal holds these role assignments on the Storage account:</p>
<ul>
<li><code>Storage Blob Data Reader</code></li>
<li><code>Storage Queue Data Contributor</code></li>
</ul>
</li>
<li>
<p>Confirm that the Storage account's networking configuration allows the connector to access the Azure Storage Queue.</p>
</li>
</ol>
<p><strong>Verify:</strong> Redeploy the connector. The Deployments blade should show status <strong>Succeeded</strong>, and the connector should transition to <strong>Connected</strong>.</p>
<h2 id="connector-update-fails-with-invalid-output-table-schema">Connector update fails with <code>Invalid output table schema</code></h2>
<p>You see a deployment failure with an error similar to:</p>
<pre><code class="language-txt">Failed to create required resources for data connector.&#10;Invalid output table schema: The following columns which exist&#10;in the current schema do not exist in the new schema or have&#10;different types.&#10;</code></pre>
<p><strong>Cause:</strong> An earlier version of the Cloudflare CCF connector created a <code>CloudflareV2_CL</code> table in your Log Analytics workspace. When you deploy a newer connector version, the ARM template attempts to update this table schema. Azure Monitor rejects the update if the new schema omits columns that exist in the current table, or changes an existing column to an incompatible datatype.</p>
<p><strong>Fix:</strong> Update the existing table schema directly through the Azure Monitor REST API before redeploying the connector. Run the update from Azure Cloud Shell using an account that holds the <code>Log Analytics Contributor</code> role on the workspace.</p>
<ol>
<li>Download the latest <code>CloudflareV2_CL.json</code> schema definition from the Cloudflare CCF connector solution package (available in the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Microsoft Sentinel Content Hub</a>) and upload it to your Cloud Shell session.</li>
<li>Request an Azure Resource Manager access token:</li>
</ol>
<pre><code class="language-sh">az account get-access-token --resource https://management.azure.com/&#10;</code></pre>
<ol start="3">
<li>Apply the updated table schema, replacing the placeholders with your values:</li>
</ol>
<pre><code class="language-sh">az rest --method PUT \&#10;  &#45;-url &quot;https://management.azure.com/subscriptions/&lt;subscription-id&gt;/resourceGroups/&lt;resource-group&gt;/providers/Microsoft.OperationalInsights/workspaces/&lt;workspace-name&gt;/tables/CloudflareV2_CL?api-version=2025-07-01&quot; \&#10;  &#45;-headers &quot;Authorization=Bearer &lt;access-token&gt;&quot; &quot;Content-Type=application/json&quot; \&#10;  &#45;-body @CloudflareV2_CL.json&#10;</code></pre>
<p><strong>Verify:</strong> The command returns the updated table definition as JSON. Redeploy the Cloudflare CCF connector — the deployment should complete without a schema validation error.</p>
<h2 id="fields-are-missing-or-null-in-cloudflarev2-cl">Fields are missing or <code>null</code> in <code>CloudflareV2_CL</code></h2>
<p><strong>Cause:</strong> The Data Collection Rule (DCR) schema is out of sync with the Cloudflare Logpush schema being delivered. Two variants are common:</p>
<ul>
<li><strong>Datatype mismatch:</strong> A field is declared with the wrong Sentinel datatype in the DCR <code>streamDeclarations</code> — for example, a numeric field declared as <code>string</code>, or a variable-shape field such as <code>BotDetectionIDs</code> declared as anything other than <code>dynamic</code>. The record is ingested, but the mismatched column is populated with <code>null</code>.</li>
<li><strong>Reserved column name conflict:</strong> A Cloudflare field name collides with a <a href="https://learn.microsoft.com/azure/azure-monitor/logs/create-custom-table?tabs=azure-portal-1%2Cazure-portal-2%2Cazure-portal-3#add-or-delete-a-custom-column">Microsoft Sentinel reserved column name</a>. For example, the Cloudflare Network Error Logging (NEL) dataset contains a <code>Type</code> field, but <code>Type</code> is reserved in Sentinel. Fields with reserved names cannot be stored under their original name.</li>
</ul>
<p><strong>Fix:</strong></p>
<ol>
<li>Upgrade the Cloudflare CCF solution to the latest version from the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Microsoft Sentinel Content Hub</a>. New releases progressively correct field datatypes shipped by the connector and add support for new Cloudflare Logpush fields.</li>
<li>If missing fields persist after upgrading — for example, because the DCR has been customized — apply a manual fix:
<ul>
<li><strong>For datatype mismatches:</strong> Update the field's datatype in both the DCR <code>streamDeclarations</code> and the <code>CloudflareV2_CL</code> table definition to match the Cloudflare Logpush schema (for example, <code>real</code> for floating-point values such as <code>EdgeResponseCompressionRatio</code>, or <code>dynamic</code> for <code>BotDetectionIDs</code>).</li>
<li><strong>For reserved name conflicts:</strong> Rename the field in the DCR <code>transformKql</code> transformation and add the renamed column to the <code>CloudflareV2_CL</code> table definition. For example, to preserve the NEL <code>Type</code> value:</li>
</ul>
</li>
</ol>
<pre><code class="language-kusto">source&#10;| extend NELType = Type&#10;| project-away Type&#10;</code></pre>
<pre><code> Add a `NELType` column to `CloudflareV2_CL` with datatype `string`.&#10;</code></pre>
<p><strong>Verify:</strong> Send a fresh Logpush batch and query <code>CloudflareV2_CL</code> for the affected fields. Values should now be populated and no longer <code>null</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="known-unsupported-fields">Known unsupported fields</h3>
@markup("md", "content/.markup/bodies/3152.md")
</aside>
<h2 id="the-cloudflare-ccf-solution-workbook-does-not-populate">The Cloudflare CCF solution workbook does not populate</h2>
<p>The Cloudflare workbook shipped with the CCF solution loads but shows no data, or its queries fail with an error indicating that the referenced table or connector does not exist.</p>
<p><strong>Cause:</strong> In earlier releases, the workbook shipped with the Cloudflare CCF solution referenced the legacy <code>Cloudflare_CL</code> table and the legacy <code>CloudflareDataConnector</code>. The CCF connector ingests into <code>CloudflareV2_CL</code> through a parser, so workbook queries against the legacy table return no results even when logs are ingesting correctly.</p>
<p><strong>Fix:</strong> Upgrade the Cloudflare CCF solution to a version whose workbook references the CCF connector's parser and the <code>CloudflareV2_CL</code> table. The latest solution release is available from the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Microsoft Sentinel Content Hub</a>.</p>
<p><strong>Verify:</strong> Reopen the workbook. Panels should populate with recent Cloudflare log data.</p>
<h2 id="still-not-resolved">Still not resolved</h2>
<p>If your issue is not covered here:</p>
<ul>
<li>Consult the <a href="https://azuremarketplace.microsoft.com/marketplace/apps/cloudflare.azure-sentinel-solution-cloudflare-ccf">Cloudflare CCF solution page</a> on the Azure Marketplace for the latest solution version and deployment prerequisites.</li>
<li>Review the <a href="/logs/reference/change-notices/">Cloudflare Logs change notices</a> for recent schema changes that may affect your DCR or table definitions.</li>
<li><a href="/support/contacting-cloudflare-support/">Contact Cloudflare Support</a> for issues involving Cloudflare-side log delivery.</li>
<li>Contact Microsoft Support for issues isolated to Microsoft Azure or the Microsoft Sentinel CCF environment.</li>
</ul>
