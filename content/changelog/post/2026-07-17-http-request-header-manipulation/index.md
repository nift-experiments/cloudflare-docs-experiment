<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 17, 2026</time><h2 id="post-title">New header control options for Gateway HTTP policies</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare Gateway now supports advanced header control on <a href="/cloudflare-one/traffic-policies/http-policies/#allow">Allow policies</a>. Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.</p>
<h4 id="header-operations">Header operations</h4>
<p>Gateway HTTP policies using the Allow action support three operations in <code>rule_settings</code>:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>API field</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Add</td>
<td><code>add_headers</code></td>
<td>Appends a value to the header. Existing values are preserved.</td>
</tr>
<tr>
<td>Overwrite</td>
<td><code>set_headers</code></td>
<td>Replaces the header value. Creates the header if it does not exist.</td>
</tr>
<tr>
<td>Delete</td>
<td><code>delete_headers</code></td>
<td>Removes the header from the request.</td>
</tr>
</tbody>
</table>
<p>Gateway applies operations in order: delete, then overwrite, then add.</p>
<h4 id="dynamic-variables">Dynamic variables</h4>
<p>Header values can include dynamic variables using the <code>@{...}</code> syntax. Gateway resolves variables at request time from identity, device, and network context.</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@{identity.email}</code></td>
<td>User email from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.name}</code></td>
<td>User display name from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.id}</code></td>
<td>Cloudflare identity UUID</td>
</tr>
<tr>
<td><code>@{identity.groups}</code></td>
<td>Identity provider group memberships</td>
</tr>
<tr>
<td><code>@{identity.SAML}</code></td>
<td>SAML attributes (if configured)</td>
</tr>
<tr>
<td><code>@{identity.OIDC}</code></td>
<td>OIDC claims (if configured)</td>
</tr>
<tr>
<td><code>@{source.ip}</code></td>
<td>Source IP of the connection</td>
</tr>
<tr>
<td><code>@{destination.ip}</code></td>
<td>Destination IP of the request</td>
</tr>
<tr>
<td><code>@{device.id}</code></td>
<td>Cloudflare One Client device UUID</td>
</tr>
<tr>
<td><code>@{device.posture}</code></td>
<td>Device posture check results (JSON string)</td>
</tr>
</tbody>
</table>
<p>You can mix static text and dynamic variables in a single header value. For example, <code>user-@{identity.email}</code> resolves to <code>user-jdoe@example.com</code>.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tenant-control/">Custom headers</a>.</p>
</div></article></div>
