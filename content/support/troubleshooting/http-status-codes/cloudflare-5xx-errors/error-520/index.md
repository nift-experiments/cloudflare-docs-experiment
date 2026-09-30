<h2 id="error-520-web-server-returns-an-unknown-error">Error 520: web server returns an unknown error</h2>
<p>This error occurs when the origin server returns an empty, unknown, or unexpected response to Cloudflare.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error is often triggered by:</p>
<ul>
<li>Origin server crashes or misconfigurations.</li>
<li>Firewalls or security plugins blocking <a href="https://www.cloudflare.com/ips">Cloudflare IPs</a> at your origin.</li>
<li>Headers exceeding 128 KB (often due to excessive cookies).</li>
<li>Empty or malformed responses lacking an HTTP status code or response body.</li>
<li>Missing response headers or origin web server not returning <a href="https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml">proper HTTP error responses</a>.</li>
<li>Incorrect HTTP/2 configuration at the origin server.</li>
<li>Authentication Origin Pull enabled on Cloudflare but the origin is <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/global/#2-configure-origin-to-accept-client-certificates">not configured as expected</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14730.md")
</aside>
<h3 id="resolution">Resolution</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14729.md")
</aside>
<ul>
<li>
<p>Contact your hosting provider or site administrator and share the necessary <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">error details</a> to assist with troubleshooting. Request a review of your origin web server error logs for crashes and check for <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/#common-causes">common causes</a> mentioned in the previous section.</p>
</li>
<li>
<p>If HTTP/2 is enabled at your origin server, ensure it is correctly set up. Cloudflare connects to servers who announce support of HTTP/2 connections via <a href="https://blog.cloudflare.com/introducing-http2">ALPN</a>. If the origin web server accepts the HTTP/2 connection but then does not respect or support the protocol, an HTTP <code>520</code> error will be returned. You can disable the <a href="/speed/optimization/protocol/http2-to-origin/#disable-http2-to-origin">HTTP/2 to Origin</a> in <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Protocol Optimization</strong> on the Cloudflare dashboard.</p>
</li>
<li>
<p>If <code>520</code> errors continue after contacting your hosting provider or site administrator, provide the following information to <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>:</p>
<ul>
<li>Full URL(s) of the resource requested when the error occurred.</li>
<li>Cloudflare <a href="/fundamentals/reference/cloudflare-ray-id/"><strong>cf-ray</strong></a> from the <code>520</code> error message.</li>
<li>Output from <code>http://&lt;YOUR_DOMAIN&gt;/cdn-cgi/trace</code>.</li>
<li>Two <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">HAR files</a>:
<ul>
<li>One with Cloudflare enabled on your website.</li>
<li>Another with <a href="/fundamentals/manage-domains/pause-cloudflare/">Cloudflare temporarily disabled</a>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="diagnosing-origin-connectivity-using-originresponsestatus-in-logs">Diagnosing origin connectivity using OriginResponseStatus in logs</h2>
<p>When reviewing Cloudflare Logs (via <a href="/logs/logpush/">Logpush</a> <code>http_requests</code> dataset), the <code>OriginResponseStatus</code> field shows the HTTP status code returned by your origin.</p>
<p>An <code>OriginResponseStatus</code> value of <strong><code>0</code></strong> has two distinct meanings depending on context:</p>
<ul>
<li><strong>No origin contact (cache hit or revalidated response):</strong> The request was served from cache and Cloudflare did not contact the origin. Filter these out when calculating origin error rates — they do not indicate an origin problem.</li>
<li><strong>Failed origin connection:</strong> Cloudflare attempted to contact the origin but received no HTTP response. The origin either dropped the TCP connection before sending response headers, timed out before sending headers, or sent a malformed response that Cloudflare could not parse. Cloudflare generates the error page itself (typically a 520 or 500).</li>
</ul>
<p>To distinguish between the two, check the <code>CacheStatus</code> field in the same log record:</p>
<ul>
<li><code>CacheStatus</code> is <code>hit</code> or <code>revalidated</code> → no origin contact; <code>OriginResponseStatus = 0</code> is expected</li>
<li><code>CacheStatus</code> is <code>miss</code> or <code>expired</code> → Cloudflare contacted the origin; <code>OriginResponseStatus = 0</code> indicates a failed connection</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14728.md")
</aside>
<h2 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h2>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to compare what your origin returned (<code>originResponseStatus</code>) with what Cloudflare served to the end user (<code>edgeResponseStatus</code>). If your origin returned a <code>200</code> but Cloudflare served a <code>520</code>, the response was likely malformed — for example, oversized headers or an early connection close. The <strong>Top endpoints</strong> table can help you identify which paths are producing <code>520</code> errors.</p>
