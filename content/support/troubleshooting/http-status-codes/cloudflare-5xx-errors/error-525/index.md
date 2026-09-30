<h2 id="error-525-ssl-handshake-failed">Error 525: SSL handshake failed</h2>
<p>This error indicates that the SSL handshake between Cloudflare and the origin web server failed.</p>
<h3 id="common-causes">Common causes</h3>
<p>Error <code>525</code> occurs when these two conditions are true:</p>
<ul>
<li>The <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">SSL handshake</a> fails between Cloudflare and the origin web server.</li>
<li><a href="/ssl/origin-configuration/ssl-modes"><em>Full</em> or <em>Full (Strict)</em></a> <strong>SSL</strong> is set in the <strong>Overview</strong> tab of your Cloudflare <strong>SSL/TLS</strong> app.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14724.md")
</aside>
<h3 id="resolution">Resolution</h3>
<p>Contact your hosting provider to exclude the following common causes at your origin web server:</p>
<ul>
<li>No valid SSL certificate is installed.</li>
<li>Port <code>443</code> (or another custom secure port) is not open.</li>
<li>No <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/14725.md")
</div> support.
- The [cipher suites](/ssl/origin-configuration/cipher-suites/) used by Cloudflare do not match the cipher suites supported by the origin web server.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14723.md")
</aside>
<ul>
<li>
<p>Verify that a certificate is installed on your origin server. For details on running tests, refer to <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#troubleshoot-requests-with-curl">Troubleshoot requests with curl</a>. If no certificate is installed, you can generate and install a free <a href="/ssl/origin-configuration/origin-ca">Cloudflare origin CA certificate</a> to encrypt traffic between Cloudflare and your origin web server.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/additional-options/cipher-suites/">Review the cipher suites</a> used by your server to ensure they are compatible with Cloudflare.</p>
</li>
<li>
<p>Check your server's error logs from the timestamps when <code>525</code> errors occur to identify any issues causing the connection to be reset during the SSL handshake.</p>
</li>
</ul>
<h3 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h3>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to check whether SSL handshake failures are affecting specific endpoints. The <strong>Origin status codes</strong> chart shows when Cloudflare received no HTTP response from your origin (<code>originResponseStatus</code> of <code>0</code>), which can indicate TLS negotiation failures. Cross-reference these timestamps with your origin SSL error logs to pinpoint the cause.</p>
