<p>Even with an active SSL/TLS certificate, visitors can still access resources over unsecured HTTP connections.</p>
<p>It is best to redirect this traffic over HTTPS, as well as ensure other resources (such as images) are also loaded over HTTPS.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before trying to enforce HTTPS connections, make sure that your application has an active <a href="/ssl/get-started/#choose-an-edge-certificate">edge certificate</a>. Otherwise, visitors will not be able to access your application at all.</p>
<p>Also, make sure that your <a href="/ssl/origin-configuration/ssl-modes/">SSL encryption mode</a> is not set to <strong>Off</strong>. Otherwise, Cloudflare will redirect all visitor connections automatically to HTTP.</p>
<h2 id="1-evaluate-existing-redirects"><ol>
<li>Evaluate existing redirects</li>
</ol></h2>
<p>To make sure that your visitors do not get stuck in a <a href="/ssl/troubleshooting/too-many-redirects/">redirect loop</a>, evaluate existing redirects at your origin server and within the Cloudflare dashboard.</p>
<p>You should generally avoid redirects at your origin server. Not only are you likely to forget about them, but they also reduce application performance. It is much faster for Cloudflare to redirect requests before they ever reach your origin.</p>
<p>Make sure that your redirects within Cloudflare are not forwarding traffic to URLs starting with <code>http</code>.</p>
<h2 id="2-rewrite-http-urls"><ol start="2">
<li>Rewrite HTTP URLs</li>
</ol></h2>
<p>If your application contains links or references to HTTP URLs, your visitors might see <a href="/ssl/troubleshooting/mixed-content-errors/">mixed content errors</a> when accessing an HTTPS page.</p>
<p>To avoid these issues, enable <a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a> and pay attention to which HTTP requests are still reaching your origin server.</p>
<h2 id="3-redirect-traffic-to-https"><ol start="3">
<li>Redirect traffic to HTTPS</li>
</ol></h2>
<p>If your entire application can support HTTPS traffic, enable <a href="/ssl/edge-certificates/additional-options/always-use-https/#encrypt-all-visitor-traffic">Always Use HTTPS</a>.</p>
<p>If only some parts of your application can support HTTPS traffic, do not enable <strong>Always Use HTTPS</strong> and use a <a href="/rules/url-forwarding/single-redirects/">single redirect</a> to selectively perform the redirect to HTTPS. Refer to <a href="/rules/url-forwarding/examples/redirect-admin-https/">Redirect admin area requests to HTTPS</a> for an example.</p>
