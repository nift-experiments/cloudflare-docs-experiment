<h2 id="error-524-a-timeout-occurred">Error 524: a timeout occurred</h2>
<p>Error <code>524</code> indicates that Cloudflare successfully connected to the origin web server, but the origin did not provide an HTTP response before the default 125 seconds <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a>.</p>
<h3 id="common-causes">Common causes</h3>
<p>This can happen if the origin server is taking too long because it has too much work to do, for example, a large data query, or because the server is struggling for resources and cannot return any data in time.
The error <code>524</code> occurs if the origin web server acknowledges (ACK) the resource request after the connection has been established, but does not send a timely response (within the <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a> delay, 125 seconds by default).</p>
<p>Error <code>524</code> can also indicate that Cloudflare successfully connected to the origin web server to write data, but the write did not complete before the 30 seconds <a href="/fundamentals/reference/connection-limits/">Proxy Write Timeout</a> (or 6.5 seconds in the case of <a href="/images/">Cloudflare Images</a>). This timeout cannot be adjusted.</p>
<h3 id="resolution-at-your-origin">Resolution at your origin</h3>
<p>Here are the options we suggest to work around this issue:</p>
<ul>
<li>
<p><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">Contact your hosting provider</a> to exclude the following common causes at your origin web server:</p>
<ul>
<li>A long-running process on the origin web server.</li>
<li>An overloaded origin web server.</li>
</ul>
</li>
<li>
<p>Implement status polling of large HTTP processes to avoid hitting this error.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14727.md")
</aside>
<h3 id="resolution-on-cloudflare">Resolution on Cloudflare</h3>
<p>Here are some other actions you can take on the Cloudflare side:</p>
<ul>
<li>If you regularly run HTTP requests that take over 125 seconds to complete (for example, large data exports), move those processes behind a <a href="/dns/proxy-status/#dns-only-records">subdomain not proxied (DNS-only, grey clouded)</a> in the Cloudflare <strong>DNS</strong> app.</li>
<li>Enterprise customers can increase the <code>524</code> timeout up to 6,000 seconds:
<ul>
<li>If your content can be cached, you can create a <a href="/cache/how-to/cache-rules/settings/#proxy-read-timeout-enterprise-only">Cache Rule</a> with the <code>Proxy Read Timeout</code> setting. The content needs to be cacheable for the rule to be triggered, but does not need to be cached.</li>
<li>You can increase the <code>proxy_read_timeout</code> setting for the whole zone using the <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit zone setting API endpoint</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14726.md")
</aside>
<h3 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h3>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to monitor origin response times and catch requests approaching your timeout threshold before they result in <code>524</code> errors. If P95 response times are near the <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a>, identify the slow paths in the <strong>Top endpoints</strong> table and optimize them — or increase the timeout for Enterprise zones.</p>
