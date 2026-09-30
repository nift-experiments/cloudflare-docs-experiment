<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 21, 2026</time><h2 id="post-title">Account Role API deprecated</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>The <a href="/api/resources/accounts/subresources/roles/">Account Roles API</a> is deprecated and is being replaced by the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a>. An end of life date has not yet been established.</p>
<h4 id="what-you-need-to-do">What you need to do</h4>
<p>Review the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a> documentation; the response schema differs from the legacy Roles response.</p>
<h4 id="highlights">Highlights</h4>
<ul>
<li>Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.</li>
<li>The legacy <code>Role</code> response includes a top-level <code>description</code> and a <code>permissions</code> object keyed by resource type with edit/read flags.</li>
<li>The <code>PermissionGroup</code> response replaces those with a <code>meta</code> object containing <code>label</code> and <code>scopes</code>. Individual permissions are not returned as part of the permission group.</li>
<li>The new API supports the <a href="/fundamentals/api/get-started/create-token/">API Token</a> authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div></article></div>
