<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 13, 2026</time><h2 id="post-title">Origin Content Signals for Markdown for Agents</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:</p>
<ul>
<li>Markdown for Agents preserves security headers such as <code>Strict-Transport-Security</code> (HSTS), <code>Content-Security-Policy</code> (CSP), <code>X-Frame-Options</code>, <code>Set-Cookie</code>, and CORS headers (for example, <code>Access-Control-Allow-Origin</code>) on the converted response.</li>
<li>Caching headers (<code>Cache-Control</code>, <code>Expires</code>, <code>Age</code>) continue to pass through.</li>
</ul>
<p>Your origin's <a href="https://contentsignals.org/">Content Signals</a> policy is now authoritative. If your origin sets a <code>content-signal</code> header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default <code>Content-Signal: ai-train=yes, search=yes, ai-input=yes</code>.</p>
<p>This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as <code>../page/</code> could resolve one path segment too high and return a <code>404</code>. Links are now resolved correctly per <a href="https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3">RFC 3986</a>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>
</div></article></div>
