<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 8, 2024</time><h2 id="post-title">Use Logpush for Email security user actions</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.</p>
<p>When creating a new Logpush job, remember to select <strong>Audit logs</strong> as the dataset and filter by:</p>
<ul>
<li><strong>Field</strong>: <code>&quot;ResourceType&quot;</code></li>
<li><strong>Operator</strong>: <code>&quot;starts with&quot;</code></li>
<li><strong>Value</strong>: <code>&quot;email_security&quot;</code>.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-User-Actions.png" alt="Logpush-user-actions" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs">Enable user action logs</a>.</p>
<p>This feature is available across all Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div></article></div>
