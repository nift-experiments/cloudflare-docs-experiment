<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 8, 2025</time><h2 id="post-title">Improved Payload Logging for WAF Managed Rules</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:</p>
<ul>
<li><strong>Targeted logging</strong>: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.</li>
<li><strong>Visual highlighting</strong>: Matched content is visually highlighted in the UI for faster identification.</li>
<li><strong>Enhanced context</strong>: Logs now include surrounding context to make diagnostics more effective.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/waf/2025-05-payload-logging-update.png" alt="Log entry showing payload logging details" /></p>
<p>Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can <a href="/waf/managed-rules/payload-logging/">get started</a>.</p>
<p><strong>Note:</strong> The structure of the <code>encrypted_matched_data</code> field in Logpush has changed from <code>Map&lt;Field, Value&gt;</code> to <code>Map&lt;Field, {Before: bytes, Content: Value, After: bytes}&gt;</code>. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.</p>
</div></article></div>
