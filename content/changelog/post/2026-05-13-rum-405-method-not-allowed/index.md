<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 13, 2026</time><h2 id="post-title">/cdn-cgi/rum endpoint now returns 405 for non-POST requests</h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>The <code>/cdn-cgi/rum</code> beacon endpoint now returns <code>405 Method Not Allowed</code> for non-POST requests instead of <code>404 Not Found</code>. The response includes an <code>Allow: POST, OPTIONS</code> header per <a href="https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6">RFC 9110 §15.5.6</a>.</p>
<p>Previously, sending a <code>GET</code> or other non-POST request to this endpoint returned a <code>404</code>, which was misleading because it suggested the endpoint did not exist. The new <code>405</code> response clearly indicates that the endpoint exists but only accepts <code>POST</code> requests.</p>
<p>The Web Analytics beacon (<code>beacon.min.js</code>) already uses <code>POST</code> for all metric submissions, so this change does not affect normal beacon operation. <code>OPTIONS</code> requests for CORS preflight continue to work as before.</p>
<p>For more information, refer to the <a href="/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum">Web Analytics FAQ</a>.</p>
</div></article></div>
