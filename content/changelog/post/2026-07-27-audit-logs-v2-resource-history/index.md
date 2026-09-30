<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 27, 2026</time><h2 id="post-title">Audit Logs v2 — Resource History</h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>Audit Logs v2 now includes <strong>Resource History</strong>. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.</p>
<p>Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_resource_history.png" alt="Resource History in Audit Logs v2" /></p>
<p><strong>Dashboard:</strong></p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</li>
<li>Open any audit log entry.</li>
<li>Select the <strong>History</strong> tab to see the full history for that resource.</li>
<li>Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.</li>
</ol>
<p><strong>API:</strong></p>
<p>Use the History endpoint to retrieve the change history for any audit log entry:</p>
<pre><code class="language-txt">GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history&#10;</code></pre>
<p>The endpoint is also available for organization-scoped audit logs at <code>/organizations/{organization_id}/logs/audit/{id}/history</code>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/#resource-history">Resource History documentation</a>.</p>
</div></article></div>
