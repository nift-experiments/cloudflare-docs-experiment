<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Test Data Loss Prevention profiles without sending traffic through Gateway</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p><strong>Test scan</strong> lets you check how <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.</p>
<p><img src="/assets/upstream/images/changelog/dlp/dlp-test-scan.gif" alt="Test scan results showing matched profiles, detection entries, and match context" /></p>
<p>Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.</p>
<p>Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan documentation</a>.</p>
</div></article></div>
