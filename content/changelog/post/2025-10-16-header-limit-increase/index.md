<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 16, 2025</time><h2 id="post-title">Increased HTTP header size limit to 128 KB</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><h4 id="cdn-now-supports-128-kb-request-and-response-headers">CDN now supports 128 KB request and response headers 🚀</h4>
<p>We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to <strong>128 KB</strong> for both <strong>request and response headers</strong>.</p>
<p>Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with <code>HTTP 413</code> (Request Header Fields Too Large) errors.</p>
<hr />
<h4 id="what-s-new">What's new?</h4>
<ul>
<li><strong>Support for large headers:</strong> You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.</li>
<li><strong>Reduces <code>413</code> and <code>520</code> HTTP errors:</strong> This change drastically reduces the likelihood of customers encountering <code>HTTP 413</code> errors from large request headers or <code>HTTP 520</code> errors caused by oversized response headers, improving the overall reliability of your web applications.</li>
<li><strong>Enhanced functionality:</strong> This is especially beneficial for applications that rely on:
<ul>
<li>A large number of cookies.</li>
<li>Large Content-Security-Policy (CSP) response headers.</li>
<li>Advanced use cases with Cloudflare Workers that generate large response headers.</li>
</ul>
</li>
</ul>
<p>This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.</p>
<hr />
<p>To learn more and get started, refer to the <a href="/fundamentals/reference/connection-limits/#request-limits">Cloudflare Fundamentals documentation</a>.</p>
</div></article></div>
