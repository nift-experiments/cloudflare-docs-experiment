<p>When troubleshooting most <code>5XX</code> errors, the correct course of action is to first contact your hosting provider or site administrator to troubleshoot and gather data. The following sections outline:</p>
<ul>
<li>The <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">information</a> to provide your hosting provider to help resolve the errors</li>
<li>The steps to access <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#error-analytics">error analytics</a> in the Cloudflare dashboard.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14722.md")
</aside>
<h3 id="required-error-details-for-hosting-provider">Required error details for hosting provider</h3>
<p>When contacting your hosting provider, share the following information:</p>
<ul>
<li>The specific <code>5XX</code> error code and message.</li>
<li>The time and timezone when the <code>5XX</code> error occurred.</li>
<li>The URL that resulted in the HTTP <code>5XX</code> error (for example, <code>https://www.example.com/images/icons/image1.png</code>).</li>
</ul>
<p>The cause of the error is not always found in the origin server's error logs. Be sure to check the logs of any load balancers, caches, proxies, or firewalls between Cloudflare and the origin web server.</p>
<p>Additional details to provide to your hosting provider or site administrator can be found in the error descriptions below. Note that Cloudflare <a href="/rules/custom-errors/">Custom Errors</a> can alter the appearance of default error pages discussed in this page.</p>
<h3 id="error-analytics">Error analytics</h3>
<p>Error analytics per domain are available within <a href="/analytics/account-and-zone-analytics/zone-analytics/">Zone Analytics</a>. Error analytics provides insights into overall errors by HTTP error code and offers details such as the URLs, source IP addresses, and Cloudflare data centers needed to diagnose and resolve issues. Error Analytics are based on a 1% traffic sample.</p>
<p>To view Error Analytics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>HTTP Traffic</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add filter</strong>, select <strong>Edge status code</strong> or <strong>Origin status code</strong> and choose any <code>5xx</code> error code that you want to diagnose.</li>
</ol>
<h3 id="log-explorer">Log Explorer</h3>
<p><a href="/log-explorer/">Log Explorer</a> provides access to Cloudflare logs with all the context available within the Cloudflare platform.
You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search.
Log explorer <a href="/log-explorer/log-search/">allows you to build queries</a> filtering for a specific Ray ID, which can be useful to investigate HTTP Errors.</p>
<hr />
<h2 id="error-500-internal-server-error">Error 500: internal server error</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/">Error 500</a> page.</p>
<h2 id="error-501-not-implemented">Error 501: not implemented</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/">Error 501</a> page.</p>
<h2 id="error-502-bad-gateway-or-error-504-gateway-timeout">Error 502 bad gateway or error 504 gateway timeout</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/">Error 502/504</a> page.</p>
<h2 id="error-503-service-temporarily-unavailable">Error 503: service temporarily unavailable</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/">Error 503</a> page.</p>
<h2 id="error-520-web-server-returns-an-unknown-error">Error 520: web server returns an unknown error</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">Error 520</a> page.</p>
<h2 id="error-521-web-server-is-down">Error 521: web server is down</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/">Error 521</a> page.</p>
<h2 id="error-522-connection-timed-out">Error 522: connection timed out</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/">Error 522</a> page.</p>
<h2 id="error-523-origin-is-unreachable">Error 523: origin is unreachable</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-523/">Error 523</a> page.</p>
<h2 id="error-524-a-timeout-occurred">Error 524: a timeout occurred</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">Error 524</a> page.</p>
<h2 id="error-525-ssl-handshake-failed">Error 525: SSL handshake failed</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/">Error 525</a> page.</p>
<h2 id="error-526-invalid-ssl-certificate">Error 526: invalid SSL certificate</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/">Error 526</a> page.</p>
<h2 id="error-530">Error 530</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-530/">Error 530</a> page.</p>
