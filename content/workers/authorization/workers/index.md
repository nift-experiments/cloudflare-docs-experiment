---
cp9:
  canonical: https://developers.cloudflare.com/workers/authorization/workers/
  description: Manage Workers roles, scopes, Wrangler permissions, and API token access for deploying and managing Workers.
  full_title: Workers roles and permissions · Cloudflare Workers docs
  head_html: <title>Workers roles and permissions · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage Workers roles, scopes, Wrangler permissions, and API token access for deploying and managing Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/authorization/workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/authorization/workers/index.md"><meta property="og:title" content="Workers roles and permissions · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage Workers roles, scopes, Wrangler permissions, and API token access for deploying and managing Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/authorization/workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/authorization/workers/#page","headline":"Workers roles and permissions \u00b7 Cloudflare Workers docs","description":"Manage Workers roles, scopes, Wrangler permissions, and API token access for deploying and managing Workers.","url":"https://developers.cloudflare.com/workers/authorization/workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/authorization/workers/
  schema: 1
---
<p>Workers permissions control who or what can view, deploy, and manage Workers in your Cloudflare account. Access is granted by assigning a Workers role to a member, User Group, or API token at a specific scope.</p>
<p>Workers roles define what actions are allowed. Scopes define where those actions apply: across all Workers in the account or only to selected Workers.</p>
<p>For the platform-wide permission model, refer to the <a href="/workers/authorization/">Roles and permissions overview</a>.</p>
<h2 id="workers-roles">Workers roles</h2>
<p>You can assign Workers roles to members, User Groups, and API tokens.</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Access level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Metadata Read-Only</td>
<td>Read metadata</td>
<td>Can view Workers metadata, settings, and observability data such as metrics, logs, and traces. Cannot view script source content or secret values.</td>
</tr>
<tr>
<td>Content Read-Only</td>
<td>Read content</td>
<td>Can view Workers metadata and script source content. Cannot modify Workers.</td>
</tr>
<tr>
<td>Editor</td>
<td>Edit</td>
<td>Can read, update, deploy, and rename existing Workers, including script content, settings, schedules, versions, deployments, and observability. Cannot create or delete Workers.</td>
</tr>
<tr>
<td>Admin</td>
<td>Full manage</td>
<td>Full control over Workers, including creating, reading, updating, deploying, deleting, and renaming Workers when granted at the product scope. Per-Worker Admin applies only to the selected Worker.</td>
</tr>
</tbody>
</table>
<h2 id="grant-access-to-all-or-selected-workers">Grant access to all or selected Workers</h2>
<p>Workers roles can be granted at different scopes depending on how broadly the access should apply.</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Applies to</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers product</td>
<td>All Workers in the account</td>
<td>A member, User Group, or API token needs the same access across all Workers.</td>
</tr>
<tr>
<td>Individual Workers</td>
<td>Only selected Workers</td>
<td>A member, User Group, or API token should only access specific Workers.</td>
</tr>
</tbody>
</table>
<p>Product-level roles apply to every current and future Worker in the account.</p>
<p>Per-Worker roles apply only to the Workers you select. You cannot grant per-Worker access to a Worker that does not exist yet. Creating new Workers requires product-level <code>Admin</code> access.</p>
<h2 id="combine-product-level-and-per-worker-access">Combine product-level and per-Worker access</h2>
<p>You can combine product-level and per-Worker roles to give broad visibility but limited edit access.</p>
<p>For example, grant <code>Metadata Read-Only</code> at the Workers product scope so someone can browse Workers and view observability data across the account. Then grant <code>Editor</code> only for the specific Workers they should deploy.</p>
<h2 id="members-user-groups-and-api-tokens">Members, User Groups, and API tokens</h2>
<p>You can assign Workers roles to members, User Groups, and API tokens.</p>
<p>Members and User Groups are for people who need dashboard or user-based access. API tokens are for CI/CD pipelines, agents, scripts, and Wrangler automation.</p>
<p>API tokens use the same Workers roles and scopes as members and User Groups, but they have their own permissions. A token can only perform actions allowed by the Workers role and scope assigned to that token.</p>
<h2 id="routes-and-custom-domains">Routes and Custom Domains</h2>
<p>To add, update, or remove Routes or Custom Domains, you need <code>Editor</code> access to the Worker and <code>Workers Routes Write</code> permission for every affected zone.</p>
<p>Members and User Groups need <code>Workers Routes Write</code>, scoped to each affected zone.</p>
<p>API tokens need <em>Zone</em> &gt; <em>Workers Routes</em> &gt; <em>Write</em>, scoped to each affected zone.</p>
<p>After a Route or Custom Domain is configured, you can deploy new Worker versions with only <code>Editor</code> access, as long as the deployment does not add, update, or remove that connection.</p>
<h2 id="wrangler">Wrangler</h2>
<p>Wrangler authorizes commands using the Workers permissions of the authenticated member or API token.</p>
<p>Here are examples of the scope required to run Wrangler commands:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Wrangler command</th>
<th>Minimum role required</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tail logs for a Worker</td>
<td><code>wrangler tail</code></td>
<td><code>Metadata Read-Only</code> for that Worker</td>
</tr>
<tr>
<td>Deploy an existing Worker</td>
<td><code>wrangler deploy</code></td>
<td><code>Editor</code> for that Worker</td>
</tr>
<tr>
<td>Change Routes or Custom Domains during deployment</td>
<td><code>wrangler deploy</code></td>
<td><code>Editor</code> for that Worker, plus <code>Workers Routes Write</code> for each affected zone</td>
</tr>
<tr>
<td>Create a new Worker</td>
<td><code>wrangler deploy</code> for a Worker that does not exist yet</td>
<td>Product-level <code>Admin</code></td>
</tr>
<tr>
<td>Upload a version</td>
<td><code>wrangler versions upload</code></td>
<td><code>Editor</code> for that Worker</td>
</tr>
<tr>
<td>Deploy a version</td>
<td><code>wrangler versions deploy</code></td>
<td><code>Editor</code> for that Worker</td>
</tr>
<tr>
<td>Roll back a deployment</td>
<td><code>wrangler rollback</code></td>
<td><code>Editor</code> for that Worker</td>
</tr>
<tr>
<td>Manage secrets for an existing Worker</td>
<td><code>wrangler secret put</code>, <code>wrangler secret delete</code></td>
<td><code>Editor</code> for that Worker</td>
</tr>
</tbody>
</table>
<h2 id="legacy-workers-permissions">Legacy Workers permissions</h2>
<p>These legacy permissions and roles are being replaced by the new Workers roles. There is no deprecation date right now. Existing permissions and roles continue to work, and customers will receive advance notice before any deprecation.</p>
<p>These legacy permissions and roles were account-level. To preserve the same behavior, assign the replacement role at the scope shown below. Use per-Worker scopes only when you intentionally want to limit access to selected Workers.</p>
<table>
<thead>
<tr>
<th>Legacy permission or role</th>
<th>Replaced by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers Platform (Read-only)</td>
<td><code>Content Read-Only</code> at the Developer Platform scope</td>
</tr>
<tr>
<td>Workers Platform Admin</td>
<td><code>Admin</code> at the Developer Platform scope</td>
</tr>
<tr>
<td>Workers Platform Metadata (Read-Only)</td>
<td><code>Metadata Read-Only</code> at the Developer Platform scope</td>
</tr>
<tr>
<td>Workers CI Read</td>
<td><code>Content Read-Only</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers CI Edit</td>
<td><code>Editor</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers Observability Read</td>
<td><code>Metadata Read-Only</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers Observability Edit</td>
<td><code>Editor</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers Observability Telemetry Edit</td>
<td><code>Editor</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers Tail Read</td>
<td><code>Metadata Read-Only</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers Scripts Read</td>
<td><code>Content Read-Only</code> at the Workers product scope</td>
</tr>
<tr>
<td>Workers Scripts Edit</td>
<td><code>Editor</code> at the Workers product scope</td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-pages">Cloudflare Pages</h2>
<p>For members and User Groups, use <a href="/workers/authorization/">Developer Platform roles</a> to grant <a href="/pages/">Cloudflare Pages</a> access. Do not use Workers product roles or per-Worker roles for Pages access.</p>
<p>For API tokens, use Pages-specific roles. These roles are available when creating account-owned API tokens.</p>
<table>
<thead>
<tr>
<th>API token role</th>
<th>Access</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pages Metadata Read</td>
<td>View Pages metadata and configuration. Does not include Pages content access.</td>
</tr>
<tr>
<td>Pages Read</td>
<td>View Pages metadata and content.</td>
</tr>
<tr>
<td>Pages Write</td>
<td>Create, update, and delete Pages projects and Pages content.</td>
</tr>
</tbody>
</table>
<h2 id="bindings">Bindings</h2>
<p>To deploy a Worker that has <a href="/workers/runtime-apis/bindings/">bindings</a> to resources like <a href="/kv/">Workers KV</a>, <a href="/r2/">R2</a>, or <a href="/d1/">D1</a>, you need <code>Editor</code> access to the Worker. You do not need separate permissions on the bound resources to deploy the Worker.</p>
<p>Permissions on bound resources are only required if you need to access those resources directly, for example, reading KV keys, querying a D1 database, or listing R2 objects.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Product-level Workers roles do not grant access to other Developer Platform products such as <a href="/r2/">R2</a>, <a href="/d1/">D1</a>, <a href="/kv/">KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, or <a href="/hyperdrive/">Hyperdrive</a>.</li>
<li>API tokens do not support platform-level Developer Platform permissions.</li>
<li>Creating a new Worker requires Workers Admin because per-Worker permissions can only apply to Workers that already exist.</li>
<li>Custom Domains do not currently support per-Worker roles. Support is planned.</li>
<li>Legacy Workers permissions may appear in older configuration or API references, but new documentation should use the replacement Workers roles.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/authorization/">Roles and permissions overview</a></li>
<li><a href="/workers/authorization/durable-objects/">Durable Objects roles and permissions</a></li>
<li><a href="/r2/api/tokens/#permissions">R2 roles and permissions</a></li>
<li><a href="/fundamentals/manage-members/roles/">Roles</a></li>
<li><a href="/fundamentals/manage-members/scope/">Role scopes</a></li>
<li><a href="/fundamentals/api/reference/permissions/">API token permissions</a></li>
<li><a href="/fundamentals/manage-members/user-groups/">User Groups</a></li>
<li><a href="/workers/wrangler/commands/general/#login">Wrangler authentication</a></li>
</ul>
