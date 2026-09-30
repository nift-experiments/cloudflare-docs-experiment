<p>The OpenAI integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated OpenAI account that could leave you and your organization vulnerable.</p>
<p>This integration covers the following OpenAI products:</p>
<ul>
<li>ChatGPT Enterprise (Workspaces)</li>
<li>OpenAI Platform Projects (API keys)</li>
<li>GPTs (custom GPTs)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5094.md")
</aside>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>An OpenAI organization with a ChatGPT Enterprise workspace</li>
<li>Organization-level admin privileges to create and manage Admin API keys</li>
<li>(Optional) A Project API key and the corresponding Project ID if you plan to include OpenAI Platform Projects in the scan scope</li>
</ul>
<h3 id="enable-compliance-api-access">Enable Compliance API access</h3>
<p>Compliance API access is required to use the OpenAI CASB integration. To enable Compliance API access:</p>
<ol>
<li>Contact <code>support@openai.com</code> to request access to the Compliance API for your organization and for the API key you will use with Cloudflare CASB. In your request, include:
<ul>
<li>The last four characters of the API key</li>
<li>The name of the API key</li>
<li>The name of the user who created the key</li>
<li>The requested scope (<code>read</code>, <code>write</code>, or both)</li>
</ul>
</li>
<li>OpenAI will verify the key and grant the requested Compliance API scopes.</li>
<li>After the scopes are granted, <a href="/cloudflare-one/integrations/cloud-and-saas/">add the OpenAI integration to CASB</a>. When prompted, enter your Open AI Admin API key, Organization ID, and Workspace ID (available at <code>https://chatgpt.com/admin/settings</code>).</li>
</ol>
<p>For more information, refer to the <a href="https://help.openai.com/articles/9261474-compliance-api-for-enterprise-customers">OpenAI Help Center</a>.</p>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the OpenAI integration to function, Cloudflare CASB requires the following authorization via API keys:</p>
<ul>
<li><code>Admin API key (organization-level)</code>: Grants read-only access to organization/workspace metadata, GPTs, users, invites, and audit/compliance objects exposed by the ChatGPT Enterprise Compliance API.</li>
<li>(Optional) <code>Project API key (project-level)</code>: Grants read-only access to OpenAI Platform project metadata and keys.</li>
</ul>
<p>These credentials follow the principle of least privilege so that only the minimum required access is granted.</p>
<h2 id="security-findings">Security findings</h2>
<p>The OpenAI integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/openai.mdx.atom">RSS feed</a>.</p>
<h3 id="model-and-tool-governance">Model and tool governance</h3>
<p>Flag risky tool and capability settings on custom GPTs.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>ChatGPT Enterprise required</th>
</tr>
</thead>
<tbody>
<tr>
<td>OpenAI: GPT with Custom Actions enabled</td>
<td><code>5a2995f5-0cc1-4af3-9045-cdf7e6601f7b</code></td>
<td>High</td>
<td>✅</td>
</tr>
<tr>
<td>OpenAI: GPT with Code Interpreter enabled</td>
<td><code>d368036a-be90-49f0-b7da-5092a3f8beb4</code></td>
<td>Medium</td>
<td>✅</td>
</tr>
<tr>
<td>OpenAI: GPT with web browsing enabled</td>
<td><code>3af14358-5ff2-4502-921e-7ffd9a310093</code></td>
<td>Medium</td>
<td>✅</td>
</tr>
</tbody>
</table>
<h3 id="publishing-and-sharing">Publishing and sharing</h3>
<p>Identify GPTs that are externally visible beyond your organization.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>ChatGPT Enterprise required</th>
</tr>
</thead>
<tbody>
<tr>
<td>OpenAI: GPT publicly accessible via GPT Store</td>
<td><code>c69adfa6-2362-4939-86ec-49ff34093cfd</code></td>
<td>High</td>
<td>✅</td>
</tr>
<tr>
<td>OpenAI: GPT publicly accessible via public link</td>
<td><code>de460c9f-55c0-4131-9cdf-e4c3b84f9549</code></td>
<td>High</td>
<td>✅</td>
</tr>
</tbody>
</table>
<h3 id="api-key-hygiene">API key hygiene</h3>
<p>Detect API keys that may be stale, unused, or overdue for rotation.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>ChatGPT Enterprise required</th>
</tr>
</thead>
<tbody>
<tr>
<td>OpenAI: Admin API key not rotated</td>
<td><code>b72e971d-f5b9-4cf3-96f4-ef82bdf38453</code></td>
<td>High</td>
<td>❌</td>
</tr>
<tr>
<td>OpenAI: Project API key not rotated</td>
<td><code>2c079fe8-6188-43e1-a2e5-d0e2dd8c7686</code></td>
<td>High</td>
<td>❌</td>
</tr>
<tr>
<td>OpenAI: Unused admin API key</td>
<td><code>49c75a36-1e64-437b-98a1-e54ec35d0a64</code></td>
<td>Medium</td>
<td>❌</td>
</tr>
<tr>
<td>OpenAI: Unused project API key</td>
<td><code>c8fd231b-de51-43cc-8c3f-e1e57114c5f5</code></td>
<td>Medium</td>
<td>❌</td>
</tr>
</tbody>
</table>
<h3 id="access-security">Access security</h3>
<p>Flag user/invite issues to help enforce best practices.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>ChatGPT Enterprise required</th>
</tr>
</thead>
<tbody>
<tr>
<td>OpenAI: High-privilege invite</td>
<td><code>776ceb93-fa9a-4ca0-83db-668a67c09936</code></td>
<td>High</td>
<td>❌</td>
</tr>
<tr>
<td>OpenAI: Inactive user</td>
<td><code>20ab9ddb-fd48-46a8-9fdf-9bb9b9061f21</code></td>
<td>Medium</td>
<td>❌</td>
</tr>
<tr>
<td>OpenAI: Stale pending invite</td>
<td><code>18fd5b21-8489-485e-9c93-0bd4a696e724</code></td>
<td>Low</td>
<td>❌</td>
</tr>
</tbody>
</table>
<h3 id="data-loss-prevention-optional">Data Loss Prevention (optional)</h3>
<p>These findings will only appear if you <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">added DLP profiles</a> to your CASB integration.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>ChatGPT Enterprise required</th>
</tr>
</thead>
<tbody>
<tr>
<td>OpenAI: File in ChatGPT Conversation with DLP Profile match</td>
<td><code>9aca654d-b331-4052-a5b4-2ceecced8676</code></td>
<td>High</td>
<td>✅</td>
</tr>
<tr>
<td>OpenAI: File in ChatGPT GPT with DLP Profile match</td>
<td><code>520200f5-7dcc-42c9-bc3c-423019159d45</code></td>
<td>High</td>
<td>✅</td>
</tr>
<tr>
<td>OpenAI: File in ChatGPT Project with DLP Profile match</td>
<td><code>8e46ec69-e5c1-4f53-ab00-a92f2050ec33</code></td>
<td>High</td>
<td>❌</td>
</tr>
</tbody>
</table>
