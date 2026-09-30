<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 16, 2026</time><h2 id="post-title">Unlimited result paging in Investigations</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.</p>
<p>In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The <a href="/api/resources/email_security/subresources/investigate/methods/list">Investigations API</a> now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.</p>
<p>For high-volume use cases, we recommend:</p>
<ul>
<li><strong><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Logpush</a> to a SIEM</strong> for full-fidelity datasets and long-term retention.</li>
<li><strong>SOAR playbooks</strong> against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.</li>
<li><strong>The Investigations API</strong> for report exports larger than 1,000 results, which is the dashboard download cap.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div></article></div>
