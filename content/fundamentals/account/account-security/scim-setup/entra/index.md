<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8962.md")
</aside>
<p>Once you have <a href="/fundamentals/account/account-security/scim-setup/#gather-the-required-data">gathered the required data</a>, the following steps will be required to finish the provisioning with Entra.</p>
<h2 id="set-up-the-enterprise-application">Set up the Enterprise application</h2>
<ol>
<li>Go to the Entra admin center and select <strong>Applications</strong> &gt; <strong>Enterprise Applications</strong>.</li>
<li>In the Microsoft Entra Gallery, select <strong>New application</strong> &gt; <strong>Create your own application</strong>, then choose a name.</li>
<li>Select <strong>Integrate any other application you don't find in the gallery (Non-gallery)</strong>.</li>
<li><strong>Create</strong> an application.</li>
</ol>
<h2 id="provision-the-enterprise-application">Provision the Enterprise application</h2>
<ol>
<li>Inside the newly created application under <strong>Manage</strong> from the sidebar menu, select <strong>Provisioning</strong>.</li>
<li>Select <strong>New configuration</strong> and enter the <strong>Tenant URL</strong>: <code>https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/scim/v2</code>. Replace <code>&lt;ACCOUNT_ID&gt;</code> with your own account ID.</li>
<li>Paste the SCIM provisioning API token value as <strong>Secret token</strong>.</li>
<li>Select <strong>Test Connection</strong> then <strong>Save</strong> the configuration.</li>
</ol>
<h2 id="configure-user-and-group-synchronization">Configure user and group synchronization</h2>
<ol>
<li>Navigate to the newly created application under <strong>Manage</strong> from the sidebar menu, select <strong>Users and groups</strong>.</li>
<li><a href="https://learn.microsoft.com/entra/identity/enterprise-apps/assign-user-or-group-access-portal">Assign users and groups to the application</a>.</li>
<li>After the users are assigned, navigate to <strong>Provisioning</strong> on the sidebar menu and select <strong>Start Provisioning</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8961.md")
</aside>
<ol start="4">
<li>To validate which users and groups have been synchronized, navigate to <strong>Provisioning logs</strong> on the sidebar menu. You can also <a href="/fundamentals/account/account-security/review-audit-logs/">review the Cloudflare Audit Logs</a>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="read-only-group">Read-only group</h3>
@markup("md", "content/.markup/bodies/8960.md")
</aside>
<ol start="5">
<li>To grant permissions to users and groups at Cloudflare, refer to <a href="/fundamentals/manage-members/roles/">Roles</a> and <a href="/fundamentals/manage-members/policies/">Policies</a>.</li>
</ol>
<h2 id="optional-automate-cloudflare-s-scim-integration">(Optional) Automate Cloudflare's SCIM integration</h2>
<p>Cloudflare's SCIM integration requires one external application per account. Customers with multiple accounts may want to automate part of the setup to save time and reduce the amount of time spent in the Entra administrative UI.</p>
<p>The initial setup of creating the non-gallery applications and adding the provisioning URL and API key are scriptable via API, but the rest of the setup is dependent on your specific need and IDP configuration.</p>
<p><strong>1. Get an access token</strong></p>
<p>Get an Entra access token. Note that the example below is using the Azure CLI.</p>
<pre><code>&#35; Using azure-cli&#10;az login&#10;az account get-access-token --resource https://graph.microsoft.com&#10;&#10;(payload with accessToken returned)&#10;</code></pre>
<p><strong>2. Create a new application via template.</strong></p>
<p>The template ID 8adf8e6e-67b2-4cf2-a259-e3dc5476c621 is the suggested template to create non-gallery apps in the Entra docs. Replace <code>&lt;accessToken&gt;</code> and <code>displayName</code> with your values.</p>
<pre><code class="language-curl">curl -X POST &#x27;https://graph.microsoft.com/v1.0/applicationTemplates/8adf8e6e-67b2-4cf2-a259-e3dc5476c621/instantiate&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;accessToken&gt;&#x27; \&#10;  &#45;-data-raw &#x27;{&#10;    &quot;displayName&quot;: &quot;Entra API create application test&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-curl">{&#10;  &quot;@odata.context&quot;: &quot;https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.applicationServicePrincipal&quot;,&#10;  &quot;application&quot;: {&#10;    &quot;id&quot;: &quot;343a8552-f9d9-471c-b677-d37062117cc8&quot;, //&#10;    &quot;appId&quot;: &quot;03d8207b-e837-4be9-b4e6-180492eb3b61&quot;,&#10;    &quot;applicationTemplateId&quot;: &quot;8adf8e6e-67b2-4cf2-a259-e3dc5476c621&quot;,&#10;    &quot;createdDateTime&quot;: &quot;2025-01-30T00:37:44Z&quot;,&#10;    &quot;deletedDateTime&quot;: null,&#10;    &quot;displayName&quot;: &quot;Entra API create application test&quot;,&#10;    &quot;description&quot;: null,&#10;    // ... snipped rest of large application payload&#10;  },&#10;  &quot;servicePrincipal&quot;: {&#10;    &quot;id&quot;: &quot;a8cb133d-f841-4eb9-8bc9-c8e9e8c0d417&quot;, // Note this ID for the subsequent request&#10;    &quot;deletedDateTime&quot;: null,&#10;    &quot;accountEnabled&quot;: true,&#10;    &quot;appId&quot;: &quot;03d8207b-e837-4be9-b4e6-180492eb3b61&quot;,&#10;    &quot;applicationTemplateId&quot;: &quot;8adf8e6e-67b2-4cf2-a259-e3dc5476c621&quot;,&#10;    &quot;appDisplayName&quot;: &quot;Entra API create application test&quot;,&#10;	// ...snipped rest of JSON payload&#10;}&#10;}&#10;</code></pre>
<p><strong>3. Create a provisioning job</strong></p>
<p>To enable provisioning, you will also need to create a job. Note the SERVICE_PRINCIPAL_ID in the previous request will be used in the request below. The SCIM templateId is an Entra provided template.</p>
<pre><code class="language-curl">curl -X POST &#x27;https://graph.microsoft.com/v1.0/servicePrincipals/&lt;SERVICE_PRINCIPAL_ID&gt;/synchronization/jobs&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;accessToken&gt;&#x27; \&#10;  &#45;-data-raw &#x27;{&#10;    &quot;templateId&quot;: &quot;scim&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-curl">{&#10;  &quot;@odata.context&quot;: &quot;https://graph.microsoft.com/v1.0/$metadata#servicePrincipals(&#x27;a8cb133d-f841-4eb9-8bc9-c8e9e8c0d417&#x27;)/synchronization/jobs/$entity&quot;,&#10;  &quot;id&quot;: &quot;scim.5b223a2cc249463bbd9a791550f11c76.03d8207b-e837-4be9-b4e6-180492eb3b61&quot;,&#10;  &quot;templateId&quot;: &quot;scim&quot;,&#10;  &quot;schedule&quot;: {&#10;    &quot;expiration&quot;: null,&#10;    &quot;interval&quot;: &quot;PT40M&quot;,&#10;    &quot;state&quot;: &quot;Disabled&quot;&#10;  },&#10;}&#10;// ... snipped rest of JSON payload&#10;</code></pre>
<p><strong>4. Configure the SCIM provisioning URL and API token</strong></p>
<p>Next, configure the Tenant URL (Cloudflare SCIM endpoint) and API token (SCIM Provisioning API Token).</p>
<p>Replace <code>&lt;accessToken&gt;</code>, <code>&lt;ACCOUNT_ID&gt;</code>, <code>&lt;SCIM_PROVISIONING_API_TOKEN_VALUE&gt;</code> with your values.</p>
<pre><code class="language-curl"> &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;accessToken&gt;&#x27; \&#10;  &#45;-data-raw &#x27;{&#10;  &quot;value&quot;: [&#10;    {&#10;      &quot;key&quot;: &quot;BaseAddress&quot;,&#10;      &quot;value&quot;: &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/scim/v2&quot;&#10;    },&#10;    {&#10;      &quot;key&quot;: &quot;SecretToken&quot;,&#10;      &quot;value&quot;: &quot;&lt;SCIM_PROVISIONING_API_TOKEN_VALUE&gt;&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<p>After completing the tasks above, the next steps in Entra include:</p>
<ul>
<li>Additional group/provisioning configuration</li>
<li>Test and save after updating the config.</li>
<li>Provisioning after configuration is complete</li>
</ul>
