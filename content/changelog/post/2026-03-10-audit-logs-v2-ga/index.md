<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 10, 2026</time><h2 id="post-title">Audit logs (version 2) - General Availability</h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>Audit Logs v2 is now generally available to all Cloudflare customers.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/auditlogsv2.gif" alt="Audit Logs v2 GA" /></p>
<p>Audit Logs v2 provides a unified and standardized system for tracking and recording all user and system actions across Cloudflare products. Built on Cloudflare's API Shield / OpenAPI gateway, logs are generated automatically without requiring manual instrumentation from individual product teams, ensuring consistency across ~95% of Cloudflare products.</p>
<p><strong>What's available at GA:</strong></p>
<ul>
<li><strong>Standardized logging</strong> — Audit logs follow a consistent format across all Cloudflare products, making it easier to search, filter, and investigate activity.</li>
<li><strong>Expanded product coverage</strong> — ~95% of Cloudflare products covered, up from ~75% in v1.</li>
<li><strong>Granular filtering</strong> — Filter by actor, action type, action result, resource, raw HTTP method, zone, and more. Over 20 filter parameters available via the API.</li>
<li><strong>Enhanced context</strong> — Each log entry includes authentication method, interface (API or dashboard), Cloudflare Ray ID, and actor token details.</li>
<li><strong>18-month retention</strong> — Logs are retained for 18 months. Full history is accessible via the API or Logpush.</li>
</ul>
<p><strong>Access:</strong></p>
<ul>
<li><strong>Dashboard</strong>: Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>. Audit Logs v2 is shown by default.</li>
<li><strong>API</strong>: <code>GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit</code></li>
<li><strong>Logpush</strong>: Available via the <code>audit_logs_v2</code> account-scoped dataset.</li>
</ul>
<p><strong>Important notes:</strong></p>
<ul>
<li>Approximately 30 days of logs from the Beta period (back to ~February 8, 2026) are available at GA. These Beta logs will expire on ~April 9, 2026. Logs generated after GA will be retained for the full 18 months. Older logs remain available in Audit Logs v1.</li>
<li>The UI query window is limited to 90 days for performance reasons. Use the API or Logpush for access to the full 18-month history.</li>
<li><code>GET</code> requests (view actions) and <code>4xx</code> error responses are not logged at GA. <code>GET</code> logging will be selectively re-enabled for sensitive read operations in a future release.</li>
<li>Audit Logs v1 continues to run in parallel. A deprecation timeline will be communicated separately.</li>
<li>Before and after values — the ability to see what a value changed from and to — is a highly requested feature and is on our roadmap for a post-GA release. In the meantime, we recommend using Audit Logs v1 for before and after values. Audit Logs v1 will continue to run in parallel until this feature is available in v2.</li>
</ul>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>
</div></article></div>
