<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 12, 2026</time><h2 id="post-title">Enhanced visibility for post-delivery actions</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17721.md")</aside>
<p><img src="/assets/upstream/images/changelog/email-security/enhanced-visibility-post-delivery-actions.png" alt="failure-log-example" /></p>
<p>This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div></article></div>
