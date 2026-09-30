<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 19, 2026</time><h2 id="post-title">Enhanced HTTP/3 request cancellation visibility</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><h4 id="enhanced-http-3-request-cancellation-visibility">Enhanced HTTP/3 request cancellation visibility</h4>
<p>Cloudflare now provides more accurate visibility into HTTP/3 client request cancellations, giving you better insight into real client behavior and reducing unnecessary load on your origins.</p>
<p>Previously, when an HTTP/3 client cancelled a request, the cancellation was not always actioned immediately. This meant requests could continue through the CDN — potentially all the way to your origin — even after the client had abandoned them. In these cases, logs would show the upstream response status (such as <code>200</code> or a timeout-related code) rather than reflecting the client cancellation.</p>
<p>Now, Cloudflare terminates cancelled HTTP/3 requests immediately and accurately logs them with a <code>499</code> status code.</p>
<hr />
<h4 id="better-observability-for-client-behavior">Better observability for client behavior</h4>
<p>When HTTP/3 clients cancel requests, Cloudflare now immediately reflects this in your logs with a <code>499</code> status code. This gives you:</p>
<ul>
<li><strong>More accurate traffic analysis</strong>: Understand exactly when and how often clients cancel requests.</li>
<li><strong>Clearer debugging</strong>: Distinguish between true errors and intentional client cancellations.</li>
<li><strong>Better availability metrics</strong>: Separate client-initiated cancellations from server-side issues.</li>
</ul>
<hr />
<h4 id="reduced-origin-load">Reduced origin load</h4>
<p>Cloudflare now terminates cancelled requests faster, which means:</p>
<ul>
<li><strong>Less wasted compute</strong>: Your origin no longer processes requests that clients have already abandoned.</li>
<li><strong>Lower bandwidth usage</strong>: Responses are no longer generated and transmitted for cancelled requests.</li>
<li><strong>Improved efficiency</strong>: Resources are freed up to handle active requests.</li>
</ul>
<hr />
<h4 id="what-to-expect-in-your-logs">What to expect in your logs</h4>
<p>You may notice an increase in <code>499</code> status codes for HTTP/3 traffic. For HTTP/3, a <code>499</code> indicates the client <a href="https://datatracker.ietf.org/doc/html/rfc9114#section-4.1.1">cancelled the request stream</a> before receiving a complete response — the underlying connection may remain open. This is a normal part of web traffic.</p>
<p><strong>Tip</strong>: If you use <code>499</code> codes in availability calculations, consider whether client-initiated cancellations should be excluded from error rates. These typically represent normal user behavior — such as closing a browser, navigating away from a page, mobile network drops, or cancelling a download — rather than service issues.</p>
<hr />
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-499/">Error 499</a>.</p>
</div></article></div>
