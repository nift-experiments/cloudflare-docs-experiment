<h1 id="changelog">Changelog</h1>

<h2 id="resource-tagging-enters-public-beta"><a href="/changelog/post/2026-04-27-resource-tagging-public-beta/">Resource Tagging enters public beta</a></h2>
<p><em>2026-04-27</em></p>
<p>Resource Tagging is now in public beta and rolling out to all Cloudflare accounts over the coming days. You can attach custom key-value metadata to your Cloudflare resources and query across your entire account to find what you need.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-included">What's included</h4>
<ul>
<li><strong>Broad resource type support</strong> — Tag zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, Durable Object namespaces, Queues, Stream videos, Images, Access applications, Gateway rules, AI Gateways, and more. Refer to the <a href="/resource-tagging/reference/resource-types/">full list of supported resource types</a>.</li>
<li><strong>Powerful filtering</strong> — Query tagged resources using AND/OR logic, negation, and key-only matching. Combine up to 20 filters per query to build precise resource views.</li>
<li><strong>Account and zone-level endpoints</strong> — Full CRUD operations across both scopes.</li>
<li><strong>Token-based authentication</strong> — Tagging supports <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens</a> that persist independently of individual users, so your automation keeps running through credential rotations and team changes.</li>
<li><strong>Flexible role support</strong> — Super Administrators, Workers Admins, and Tag Admins can all manage tags.</li>
</ul>
<h4 id="2026-04-27-resource-tagging-public-beta-api-first-by-design">API-first by design</h4>
<p>The API is the primary interface for Resource Tagging and the recommended path for all workflows — scripting tag assignments, building CI/CD pipelines, or integrating with your infrastructure-as-code toolchain.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-dashboard-ui">Dashboard UI</h4>
<p>You can also view and manage tagged resources directly in the Cloudflare dashboard. Navigate to <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong> to see all tagged resources across your account, filter by resource name or tag, and add or edit tags inline.</p>
<p><img src="/assets/upstream/images/changelog/resource-tagging/tagged-resources-dashboard.png" alt="Tagged Resources dashboard" /></p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-coming-next">What's coming next</h4>
<p>In future releases, expect support for additional resource types across the Cloudflare platform, tag-based access control policies for scoping user permissions to tagged resources, billing and usage attribution by tag for breaking down costs by team, project, or environment, and Terraform provider support for managing tags declaratively.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-current-limitations">Current limitations</h4>
<ul>
<li><code>PUT</code> replaces all tags on a resource (no partial update). Use the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag">GET, merge, PUT workflow</a> to modify individual tags safely.</li>
<li><code>DELETE</code> removes all tags from a resource. To remove a single tag, PUT the remaining tags back.</li>
<li>Querying tags for a resource that has never been tagged returns <code>500</code> instead of <code>404</code>. This is a known beta limitation.</li>
</ul>
<p>To get started, refer to the <a href="/resource-tagging/">Resource Tagging documentation</a>.</p>



