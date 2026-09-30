<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Email obfuscation decode script is now non-render-blocking</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>The decode script injected by <a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a> now loads with the <code>defer</code> attribute. This means the script no longer blocks page rendering. It downloads in parallel with HTML parsing and executes after the document is fully parsed, before the <code>DOMContentLoaded</code> event.</p>
<p>This improves page loading performance, contributing to better Core Web Vitals, for all zones with Email Address Obfuscation on. No action is required.</p>
<p>If you have custom JavaScript that depends on email addresses being decoded at a specific point during page load, note that the decode script now executes after HTML parsing completes rather than inline during parsing.</p>
</div></article></div>
