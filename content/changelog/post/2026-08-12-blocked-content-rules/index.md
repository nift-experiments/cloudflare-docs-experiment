<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 12, 2026</time><h2 id="post-title">Block emails by content with blocked content rules</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email security now lets administrators write their own content-based blocking rules. A new <strong>Blocked content</strong> area under <strong>Policies &amp; rules</strong> lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.</p>
<ul>
<li>Create rules using either <strong>plaintext</strong> matches or <strong>regular expressions</strong> — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.</li>
<li>Choose the <strong>search location</strong> for each rule: <strong>subject</strong>, <strong>body</strong>, or <strong>subject and body</strong>.</li>
<li>Use the built-in <strong>regular expression checker</strong> to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.</li>
<li>Matching messages are marked with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> and prevented from reaching users' inboxes.</li>
</ul>
<p>Blocked content rules currently only support the block action.</p>
<p>This feature is available for the following Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-content/">Blocked content</a>.</p>
</div></article></div>
