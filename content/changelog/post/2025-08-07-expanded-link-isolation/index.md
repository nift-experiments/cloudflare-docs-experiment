<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 8, 2025</time><h2 id="post-title">Expanded Email Link Isolation</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.</p>
<p>For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.</p>
<p><img src="/assets/upstream/images/changelog/email-security/expanded-link-actions.jpg" alt="Expanded Email Link Isolation Configuration" /></p>
<p>To isolate all links within a message based on the disposition, select <strong>Settings</strong> &gt; <strong>Link Actions</strong> &gt; <strong>View</strong> and select <strong>Configure</strong>. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on <a href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">Configure link actions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div></article></div>
