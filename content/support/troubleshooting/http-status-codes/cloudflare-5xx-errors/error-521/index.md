<h2 id="error-521-web-server-is-down">Error 521: web server is down</h2>
<p>Error <code>521</code> occurs when the origin web server refuses connections from Cloudflare. Security solutions at your origin may block legitimate connections from certain <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a>.</p>
<h3 id="common-causes">Common causes</h3>
<p>The two most common causes of <code>521</code> errors are:</p>
<ul>
<li>Offlined origin web server application.</li>
<li>Blocked Cloudflare requests.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>Contact your hosting provider or site administrator and share the necessary <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">error details</a> to assist in troubleshooting these common causes:</p>
<ul>
<li>Ensure your origin web server is responsive.</li>
<li>Review origin web server error logs to identify web server application crashes or outages.</li>
<li>Confirm <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a> are not blocked or rate limited.</li>
<li>Allow all <a href="https://www.cloudflare.com/ips">Cloudflare IP ranges</a> in your origin web server's firewall or other security software.</li>
<li>Confirm that — if you have your <strong>SSL/TLS mode</strong> set to <strong>Full</strong> or <strong>Full (Strict</strong>) — your origin supports HTTPS and/or you have installed a <a href="/ssl/origin-configuration/origin-ca">Cloudflare Origin Certificate</a> or a certificate matching the <a href="/ssl/origin-configuration/ssl-modes/#custom-ssltls">requirements for these modes</a>.</li>
<li>Ensure that your origin web server application is actively bound and listening on the port required by your SSL/TLS mode: Port 80 for <strong>Flexible</strong>, or Port 443 for <strong>Full</strong> and <strong>Full (Strict)</strong>.</li>
<li>Find additional troubleshooting information on the <a href="https://community.cloudflare.com/t/community-tip-fixing-error-521-web-server-is-down/42461">Cloudflare Community</a>.</li>
</ul>
