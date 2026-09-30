<h2 id="error-1200-cache-connection-limit">Error 1200: Cache connection limit</h2>
<p>This error indicates that the number of requests queued on Cloudflare's edge exceeds the limit.</p>
<h3 id="common-cause">Common cause</h3>
<p>There are too many requests queued on Cloudflare's edge that are awaiting process by your origin web server. This limit protects Cloudflare's systems.</p>
<h3 id="resolution">Resolution</h3>
<p>Tune your origin webserver to accept incoming connections faster. Adjust your caching settings to improve cache-hit rates so that fewer requests reach your origin web server. Reach out to your hosting provider or web administrator for assistance.</p>
