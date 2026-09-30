<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 15, 2026</time><h2 id="post-title">Deprecate legacy Workers KV namespace API routes</h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>The legacy Workers KV API routes under <code>/accounts/{account_id}/workers/namespaces/*</code> are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented <a href="/api/resources/kv/">Workers KV API</a> routes under <code>/accounts/{account_id}/storage/kv/namespaces/*</code> before that date.</p>
<p>The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code>.</p>
<h4 id="what-you-need-to-do">What you need to do</h4>
<p>Update any integration that calls a route under <code>/accounts/{account_id}/workers/namespaces/</code> to use the equivalent route under <code>/accounts/{account_id}/storage/kv/namespaces/</code>. The migration is a direct URL path substitution — request parameters and response payloads are identical:</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/workers/namespaces</code> → <code>GET</code> and <code>POST /accounts/{account_id}/storage/kv/namespaces</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}</code></li>
</ul>
<p>For more information about the deprecation timeline, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div></article></div>
