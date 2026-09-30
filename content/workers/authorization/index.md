---
cp9:
  canonical: https://developers.cloudflare.com/workers/authorization/
  description: Learn how Developer Platform roles and permissions apply across platform, product, and resource scopes.
  full_title: Roles and permissions · Cloudflare Workers docs
  head_html: <title>Roles and permissions · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Developer Platform roles and permissions apply across platform, product, and resource scopes."><link rel="canonical" href="https://developers.cloudflare.com/workers/authorization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/authorization/index.md"><meta property="og:title" content="Roles and permissions · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Developer Platform roles and permissions apply across platform, product, and resource scopes."><meta property="og:url" content="https://developers.cloudflare.com/workers/authorization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/authorization/#page","headline":"Roles and permissions \u00b7 Cloudflare Workers docs","description":"Learn how Developer Platform roles and permissions apply across platform, product, and resource scopes.","url":"https://developers.cloudflare.com/workers/authorization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/authorization/
  schema: 1
---
<p>You can control who can access your Developer Platform resources and what they can do with them by assigning <a href="/fundamentals/manage-members/roles/">roles</a> and <a href="/fundamentals/manage-members/scope/">scopes</a> through <a href="/fundamentals/manage-members/policies/">permission policies</a>. Each policy combines a role, which defines the actions allowed, with a scope, which defines where those actions apply.</p>
<p>For Developer Platform products, scopes can be set at three levels:</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Scope</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Platform</td>
<td>All products on an account</td>
<td>You want to grant access across Workers, R2, D1, KV, Durable Objects, Queues, Workers AI, Vectorize, Hyperdrive, and other Developer Platform resources.</td>
</tr>
<tr>
<td>Product</td>
<td>All resources in one product</td>
<td>You want to grant access to all Workers, all R2 buckets, or all D1 databases, without granting access to other products.</td>
</tr>
<tr>
<td>Resource</td>
<td>One resource inside a product</td>
<td>You want to grant access to a specific resource, such as an individual Worker or R2 bucket.</td>
</tr>
</tbody>
</table>
<h2 id="roles">Roles</h2>
<p>Assign one of these roles to define the level of permission you want to grant:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>What it allows</th>
</tr>
</thead>
<tbody>
<tr>
<td>Metadata Read-Only</td>
<td>View resource lists, settings, metrics, logs, and traces. Cannot view product content such as code, data, or stored objects.</td>
</tr>
<tr>
<td>Content Read-Only</td>
<td>Everything in Metadata Read-Only, plus read product content such as Worker code, D1 database rows, or R2 objects. Cannot make changes.</td>
</tr>
<tr>
<td>Editor</td>
<td>Everything in Content Read-Only, plus update product content and settings. Cannot create or delete resources.</td>
</tr>
<tr>
<td>Admin</td>
<td>Full control, including creating and deleting resources.</td>
</tr>
</tbody>
</table>
<h2 id="members-user-groups-and-api-tokens">Members, User Groups, and API tokens</h2>
<p>Developer Platform permissions can be granted in two ways:</p>
<table>
<thead>
<tr>
<th>Grant type</th>
<th>Best for</th>
<th>How it works</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/fundamentals/manage-members/manage/">Members</a> and <a href="/fundamentals/manage-members/user-groups/">User Groups</a></td>
<td>People using the dashboard or API</td>
<td>Permissions are inherited when the member signs in to the dashboard or authenticates to the API.</td>
</tr>
<tr>
<td><a href="/fundamentals/api/get-started/create-token/">API tokens</a></td>
<td>CI/CD systems, automation, and service accounts</td>
<td>The token receives only the product and resource permissions selected when the token is created.</td>
</tr>
</tbody>
</table>
<h3 id="members-and-user-groups">Members and User Groups</h3>
<p>When you assign a <a href="/fundamentals/manage-members/roles/">role</a> to a <a href="/fundamentals/manage-members/manage/">member</a> or <a href="/fundamentals/manage-members/user-groups/">User Group</a>, that permission applies whenever the user uses the Cloudflare dashboard or API.</p>
<p>For example, if you assign a member <strong>Metadata Read-Only</strong> at the platform level, they can view settings, metrics, logs, and traces for all Developer Platform products on the account — Workers, R2, D1, and everything else — but cannot view product content like code, data, or stored objects.</p>
<p>If you assign <strong>Metadata Read-Only</strong> at the Workers product level, they can view settings and observability data for all Workers on the account, but have no visibility into R2, D1, or other products.</p>
<p>If you assign <strong>Metadata Read-Only</strong> for a single Worker, they can only see settings and observability data for that one Worker. They will not see any other Workers or any other products.</p>
<h3 id="manage-team-access-with-user-groups">Manage team access with User Groups</h3>
<p>If several people on the same team or project need the same access, create a <a href="/fundamentals/manage-members/user-groups/">User Group</a> instead of assigning permissions to each member.</p>
<p>Assign the permission policy to the group, then add the relevant members. Each member automatically inherits the group's policy.</p>
<h3 id="api-tokens">API tokens</h3>
<p>Use <a href="/fundamentals/api/get-started/create-token/">API tokens</a> for CI/CD pipelines, agents, scripts, and other automated systems that need to access Developer Platform resources programmatically.</p>
<p>For example, create an API token with <strong>Workers Editor</strong> for a deployment pipeline that needs to update and deploy Worker code.</p>
<p>API tokens support product-level and, where available, resource-level permissions. They do not support platform-level permissions. To grant an API token broad Developer Platform access, select the product-level permissions for each product the token needs.</p>
<h3 id="use-granular-permissions-with-wrangler">Use granular permissions with Wrangler</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16762.md")
</aside>
<p>To use granular permissions with <a href="/workers/wrangler/">Wrangler</a>, authenticate with an account-owned API token.</p>
<p>To authenticate Wrangler with an account-owned API token, create a token with only the permissions you need, then set these environment variables:</p>
<pre tabindex="0"><code class="language-bash">export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export CLOUDFLARE_ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;</code></pre>
<p>Wrangler uses the token's permissions. If the token is scoped to a specific Worker, Wrangler can only perform actions allowed for that Worker.</p>
<p>Wrangler commands can require different permissions depending on what they manage:</p>
<table>
<thead>
<tr>
<th>What you want to do</th>
<th>Example Wrangler command</th>
<th>Required access</th>
</tr>
</thead>
<tbody>
<tr>
<td>Deploy an existing Worker</td>
<td><code>wrangler deploy</code></td>
<td><code>Editor</code> scoped to that Worker, or <code>Editor</code> at the Workers product scope.</td>
</tr>
<tr>
<td>Create a new Worker</td>
<td><code>wrangler deploy</code> for a Worker that does not exist yet</td>
<td><code>Admin</code> at the Workers product scope.</td>
</tr>
<tr>
<td>Tail logs for one Worker</td>
<td><code>wrangler tail</code></td>
<td><code>Metadata Read-Only</code> scoped to that Worker, or <code>Metadata Read-Only</code> at the Workers product scope.</td>
</tr>
<tr>
<td>List KV namespaces</td>
<td><code>wrangler kv namespace list</code></td>
<td>Developer Platform <code>Metadata Read-Only</code> at a scope that includes KV.</td>
</tr>
<tr>
<td>Create a KV namespace</td>
<td><code>wrangler kv namespace create</code></td>
<td>Developer Platform <code>Admin</code> at a scope that includes KV.</td>
</tr>
<tr>
<td>Change Routes or Custom Domains during deployment</td>
<td><code>wrangler deploy</code></td>
<td><code>Editor</code> for the Worker, plus <a href="/workers/authorization/workers/#routes-and-custom-domains"><code>Workers Routes Write</code></a> for every affected zone.</td>
</tr>
</tbody>
</table>
<h2 id="bindings">Bindings</h2>
<p>To deploy a Worker that has <a href="/workers/runtime-apis/bindings/">bindings</a> to resources like <a href="/kv/">Workers KV</a>, <a href="/r2/">R2</a>, or <a href="/d1/">D1</a>, you need <strong>Editor</strong> access to the Worker. You do not need separate permissions on the bound resources to deploy the Worker.</p>
<p>Permissions on bound resources are only required if you need to access those resources directly, for example, reading KV keys, querying a D1 database, or listing R2 objects.</p>
<h2 id="common-access-patterns">Common access patterns</h2>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Scope</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td>View settings, logs, and metrics across all products</td>
<td>Platform</td>
<td>Metadata Read-Only</td>
</tr>
<tr>
<td>Read Worker code without modifying it</td>
<td>Workers product</td>
<td>Content Read-Only</td>
</tr>
<tr>
<td>Deploy any existing Worker, no access to other products</td>
<td>Workers product</td>
<td>Editor</td>
</tr>
<tr>
<td>Change Routes or Custom Domains during deployment</td>
<td>Workers product and each affected zone</td>
<td>Editor and <a href="/workers/authorization/workers/#routes-and-custom-domains"><code>Workers Routes Write</code></a></td>
</tr>
<tr>
<td>Rename an existing Worker</td>
<td>Individual Worker or Workers product</td>
<td>Editor</td>
</tr>
<tr>
<td>Create or delete Workers</td>
<td>Workers product</td>
<td>Admin</td>
</tr>
<tr>
<td>Automated deployments from CI/CD or agents</td>
<td>API token with Workers product</td>
<td>Editor</td>
</tr>
<tr>
<td>Automated deployments to one specific Worker</td>
<td>API token with individual Worker</td>
<td>Editor</td>
</tr>
</tbody>
</table>
