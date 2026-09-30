---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/
  description: Generate Cloudflare API tokens with pre-configured permissions using template URLs. Learn how to create and customize template URLs for any use case.
  full_title: API token template URLs · Cloudflare Fundamentals docs
  head_html: <title>API token template URLs · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate Cloudflare API tokens with pre-configured permissions using template URLs. Learn how to create and customize template URLs for any use case."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/index.md"><meta property="og:title" content="API token template URLs · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate Cloudflare API tokens with pre-configured permissions using template URLs. Learn how to create and customize template URLs for any use case."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/#page","headline":"API token template URLs \u00b7 Cloudflare Fundamentals docs","description":"Generate Cloudflare API tokens with pre-configured permissions using template URLs. Learn how to create and customize template URLs for any use case.","url":"https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/how-to/account-owned-token-template/
  schema: 1
---
<p>Use template URLs to generate Cloudflare API tokens with pre-configured permissions. Template URLs allow you to share token requirements with users without manually selecting permissions in the dashboard.</p>
<p>Template URLs use query parameters to pre-fill the API token creation page in the Cloudflare dashboard. When a user opens a template URL, the dashboard automatically configures the specified permissions and settings.</p>
<p>Cloudflare supports template URLs for both <a href="#user-token-url-format">user API tokens</a> and <a href="#account-token-url-format">account API tokens</a>. For more information on the difference between these token types, refer to <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8998.md")
</aside>
<h2 id="user-token-url-format">User token URL format</h2>
<p>User token template URLs open the token creation form at the user profile level (<code>/profile/api-tokens</code>). Tokens created this way are owned by the user.</p>
<p>The basic template URL structure is:</p>
<pre tabindex="0"><code class="language-txt">https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=[ENCODED_PERMISSIONS]&amp;accountId=*&amp;zoneId=all&amp;name=[TOKEN_NAME]&#10;</code></pre>
<h3 id="url-components">URL components</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>permissionGroupKeys</code></td>
<td>Yes</td>
<td>URL-encoded JSON array of permission objects</td>
</tr>
<tr>
<td><code>accountId</code></td>
<td>Yes</td>
<td>Account scope (use <code>*</code> for all accounts)</td>
</tr>
<tr>
<td><code>zoneId</code></td>
<td>Yes</td>
<td>Zone scope (use <code>all</code> for all zones)</td>
</tr>
<tr>
<td><code>name</code></td>
<td>No</td>
<td>Pre-filled token name</td>
</tr>
</tbody>
</table>
<h2 id="account-token-url-format">Account token URL format</h2>
<p>Account token template URLs open the token creation form at the account level. Tokens created this way are owned by the account (service principal tokens) and are not tied to any individual user. Creating account tokens requires Super Administrator or Administrator permissions.</p>
<p>The basic template URL structure is:</p>
<pre tabindex="0"><code class="language-txt">https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=[ENCODED_PERMISSIONS]&amp;name=[TOKEN_NAME]&#10;</code></pre>
<p>The <code>:account</code> segment is a placeholder. When a user opens the URL, the dashboard prompts them to select an account if they have access to more than one.</p>
<h3 id="url-components-1">URL components</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>permissionGroupKeys</code></td>
<td>Yes</td>
<td>URL-encoded JSON array of permission objects</td>
</tr>
<tr>
<td><code>name</code></td>
<td>No</td>
<td>Pre-filled token name</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8997.md")
</aside>
<h2 id="permission-format">Permission format</h2>
<p>Both user token and account token template URLs use the same permission encoding. Permissions are encoded as a JSON array with the following structure:</p>
<pre tabindex="0"><code class="language-json">[{ &quot;key&quot;: &quot;permission_name&quot;, &quot;type&quot;: &quot;read|edit|revoke|run|purge&quot; }]&#10;</code></pre>
<h3 id="permission-types">Permission types</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>read</code></td>
<td>Read-only access</td>
</tr>
<tr>
<td><code>edit</code></td>
<td>Full access (create, read, update, delete)</td>
</tr>
<tr>
<td><code>revoke</code></td>
<td>Revoke permissions</td>
</tr>
<tr>
<td><code>run</code></td>
<td>Execute permissions</td>
</tr>
<tr>
<td><code>purge</code></td>
<td>Purge permissions</td>
</tr>
</tbody>
</table>
<h2 id="create-custom-templates">Create custom templates</h2>
<h3 id="1-identify-required-permissions"><ol>
<li>Identify required permissions</li>
</ol></h3>
<p>List the permissions your use case needs. Refer to the <a href="#permission-reference">permission reference</a> table.</p>
<h3 id="2-create-the-permission-json"><ol start="2">
<li>Create the permission JSON</li>
</ol></h3>
<p>Format your permissions as a JSON array:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{ &quot;key&quot;: &quot;dns&quot;, &quot;type&quot;: &quot;edit&quot; },&#10;	{ &quot;key&quot;: &quot;analytics&quot;, &quot;type&quot;: &quot;read&quot; }&#10;]&#10;</code></pre>
<h3 id="3-url-encode-the-json"><ol start="3">
<li>URL-encode the JSON</li>
</ol></h3>
<p>Use a URL encoder to convert the JSON string:</p>
<pre tabindex="0"><code class="language-text">%5B%7B%22key%22%3A%22dns%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22analytics%22%2C%22type%22%3A%22read%22%7D%5D&#10;</code></pre>
<h3 id="4-build-the-complete-url"><ol start="4">
<li>Build the complete URL</li>
</ol></h3>
<p>For a <strong>user token</strong>, combine all components into the final template URL:</p>
<pre tabindex="0"><code class="language-txt">https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=[ENCODED_JSON]&amp;accountId=*&amp;zoneId=all&amp;name=Custom%20Token&#10;</code></pre>
<p>For an <strong>account token</strong>, use the account-level path instead:</p>
<pre tabindex="0"><code class="language-txt">https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=[ENCODED_JSON]&amp;name=Custom%20Token&#10;</code></pre>
<h2 id="permission-reference">Permission reference</h2>
<p>Use this table to find permission keys for your custom templates.</p>
<h3 id="account-permissions">Account permissions</h3>
<table>
<thead>
<tr>
<th>Permission key</th>
<th>Description</th>
<th>Common use cases</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>account_analytics</code></td>
<td>Account analytics</td>
<td>Reporting, monitoring</td>
</tr>
<tr>
<td><code>account_api_tokens</code></td>
<td>API token management</td>
<td>Token automation</td>
</tr>
<tr>
<td><code>account_settings</code></td>
<td>Account configuration</td>
<td>Account management</td>
</tr>
<tr>
<td><code>billing</code></td>
<td>Billing information</td>
<td>Cost tracking, invoicing</td>
</tr>
<tr>
<td><code>workers_scripts</code></td>
<td>Workers scripts</td>
<td>Serverless functions</td>
</tr>
<tr>
<td><code>workers_kv_storage</code></td>
<td>Workers KV storage</td>
<td>Data storage</td>
</tr>
<tr>
<td><code>workers_routes</code></td>
<td>Workers routes</td>
<td>Traffic routing</td>
</tr>
<tr>
<td><code>workers_r2</code></td>
<td>R2 storage</td>
<td>Object storage</td>
</tr>
<tr>
<td><code>d1</code></td>
<td>D1 database</td>
<td>SQL databases</td>
</tr>
<tr>
<td><code>queues</code></td>
<td>Queues</td>
<td>Message queuing</td>
</tr>
<tr>
<td><code>page</code></td>
<td>Cloudflare Pages</td>
<td>Page deployments</td>
</tr>
<tr>
<td><code>stream</code></td>
<td>Stream</td>
<td>Video streaming</td>
</tr>
<tr>
<td><code>images</code></td>
<td>Images</td>
<td>Image optimization</td>
</tr>
<tr>
<td><code>logs</code></td>
<td>Logs</td>
<td>Log management</td>
</tr>
</tbody>
</table>
<h3 id="zone-permissions">Zone permissions</h3>
<table>
<thead>
<tr>
<th>Permission key</th>
<th>Description</th>
<th>Common use cases</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dns</code></td>
<td>DNS records</td>
<td>Domain management</td>
</tr>
<tr>
<td><code>zone</code></td>
<td>Zone management</td>
<td>Domain configuration</td>
</tr>
<tr>
<td><code>zone_settings</code></td>
<td>Zone settings</td>
<td>Zone configuration</td>
</tr>
<tr>
<td><code>analytics</code></td>
<td>Zone analytics</td>
<td>Performance monitoring</td>
</tr>
<tr>
<td><code>firewall_services</code></td>
<td>Firewall rules</td>
<td>Security management</td>
</tr>
<tr>
<td><code>page_rules</code></td>
<td>Page rules</td>
<td>Traffic control</td>
</tr>
<tr>
<td><code>cache</code></td>
<td>Cache purging</td>
<td>Content updates</td>
</tr>
<tr>
<td><code>ssl_and_certificates</code></td>
<td>SSL/TLS certificates</td>
<td>Certificate management</td>
</tr>
</tbody>
</table>
<h3 id="access-permissions">Access permissions</h3>
<table>
<thead>
<tr>
<th>Permission key</th>
<th>Description</th>
<th>Common use cases</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>access</code></td>
<td>Access applications</td>
<td>Zero Trust apps</td>
</tr>
<tr>
<td><code>access_acct</code></td>
<td>Access organizations</td>
<td>Identity management</td>
</tr>
<tr>
<td><code>access_audit_log</code></td>
<td>Access audit logs</td>
<td>Compliance, security</td>
</tr>
<tr>
<td><code>access_custom_page</code></td>
<td>Custom pages</td>
<td>Branding, user experience</td>
</tr>
<tr>
<td><code>teams</code></td>
<td>Zero Trust</td>
<td>Gateway, CASB, DLP</td>
</tr>
</tbody>
</table>
<h2 id="common-permission-templates">Common permission templates</h2>
<p>Use these ready-to-use template URLs for common scenarios. Each example provides both a user token URL and an account token URL.</p>
<h3 id="dns-management">DNS management</h3>
<p>Create tokens for DNS record management.</p>
<h4 id="user-token">User token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS read-only</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22dns%22%2C%22type%22%3A%22read%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=DNS%20Read%20Token</code></td>
</tr>
<tr>
<td>DNS read/write</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22dns%22%2C%22type%22%3A%22edit%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=DNS%20Management%20Token</code></td>
</tr>
</tbody>
</table>
<h4 id="account-token">Account token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS read-only</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22dns%22%2C%22type%22%3A%22read%22%7D%5D&amp;name=DNS%20Read%20Token</code></td>
</tr>
<tr>
<td>DNS read/write</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22dns%22%2C%22type%22%3A%22edit%22%7D%5D&amp;name=DNS%20Management%20Token</code></td>
</tr>
</tbody>
</table>
<h3 id="workers-development">Workers development</h3>
<p>Create tokens for Workers, KV storage, and related services.</p>
<h4 id="user-token-1">User token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers scripts only</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22edit%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=Workers%20Scripts%20Token</code></td>
</tr>
<tr>
<td>Workers full access</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22workers_kv_storage%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22workers_routes%22%2C%22type%22%3A%22edit%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=Workers%20Full%20Access%20Token</code></td>
</tr>
</tbody>
</table>
<h4 id="account-token-1">Account token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers scripts only</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22edit%22%7D%5D&amp;name=Workers%20Scripts%20Token</code></td>
</tr>
<tr>
<td>Workers full access</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22workers_kv_storage%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22workers_routes%22%2C%22type%22%3A%22edit%22%7D%5D&amp;name=Workers%20Full%20Access%20Token</code></td>
</tr>
</tbody>
</table>
<h3 id="analytics-and-monitoring">Analytics and monitoring</h3>
<p>Create tokens for accessing analytics and logs.</p>
<h4 id="user-token-2">User token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account analytics</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22account_analytics%22%2C%22type%22%3A%22read%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=Account%20Analytics%20Token</code></td>
</tr>
<tr>
<td>Zone analytics</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22analytics%22%2C%22type%22%3A%22read%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=Zone%20Analytics%20Token</code></td>
</tr>
</tbody>
</table>
<h4 id="account-token-2">Account token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account analytics</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22account_analytics%22%2C%22type%22%3A%22read%22%7D%5D&amp;name=Account%20Analytics%20Token</code></td>
</tr>
<tr>
<td>Zone analytics</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22analytics%22%2C%22type%22%3A%22read%22%7D%5D&amp;name=Zone%20Analytics%20Token</code></td>
</tr>
</tbody>
</table>
<h3 id="zero-trust-administration">Zero Trust administration</h3>
<p>Create tokens for Cloudflare Zero Trust management.</p>
<h4 id="user-token-3">User token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access applications read</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22access%22%2C%22type%22%3A%22read%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=Access%20Read%20Token</code></td>
</tr>
<tr>
<td>Access full management</td>
<td><code>https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22access%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22access_acct%22%2C%22type%22%3A%22edit%22%7D%5D&amp;accountId=%2A&amp;zoneId=all&amp;name=Access%20Management%20Token</code></td>
</tr>
</tbody>
</table>
<h4 id="account-token-3">Account token</h4>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Template URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access applications read</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22access%22%2C%22type%22%3A%22read%22%7D%5D&amp;name=Access%20Read%20Token</code></td>
</tr>
<tr>
<td>Access full management</td>
<td><code>https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22%3A%22access%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22access_acct%22%2C%22type%22%3A%22edit%22%7D%5D&amp;name=Access%20Management%20Token</code></td>
</tr>
</tbody>
</table>
<h2 id="best-practices">Best practices</h2>
<p>Follow these guidelines when creating and sharing template URLs.</p>
<ul>
<li>Principle of least privilege: Only request the minimum permissions necessary for your use case. This reduces security risks if a token is compromised.</li>
<li>Use descriptive token names: Include clear, descriptive names in your template URLs to help users understand the token's purpose.</li>
<li>Document token usage: Provide clear documentation about what each token is used for and how to revoke it when no longer needed.</li>
<li>Regular token rotation: Encourage users to regularly rotate tokens and review permissions.</li>
<li>Test before sharing: Always test template URLs in a staging environment before sharing them with users.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Review the list of common issues and solutions.</p>
<table>
<thead>
<tr>
<th>Issue</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL does not pre-fill permissions</td>
<td>Verify the JSON is properly URL-encoded</td>
</tr>
<tr>
<td>Permissions are missing</td>
<td>Check permission keys in the reference table</td>
</tr>
<tr>
<td>Token name does not appear</td>
<td>Ensure the name parameter is URL-encoded</td>
</tr>
<tr>
<td>Access denied error</td>
<td>Verify the user has required permissions in their account</td>
</tr>
</tbody>
</table>
<p>Additionally, review the checklist before sharing a template URL.</p>
<ul>
<li>All permission keys are correct</li>
<li>JSON syntax is valid</li>
<li>URL encoding is proper</li>
<li>Token name is descriptive</li>
<li>Permissions follow least privilege principle</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/api/reference/permissions/">API token permissions</a></li>
<li><a href="/fundamentals/api/get-started/create-token/">Create API tokens</a></li>
<li><a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a></li>
<li><a href="/fundamentals/api/how-to/make-api-calls/">API authentication</a></li>
</ul>
