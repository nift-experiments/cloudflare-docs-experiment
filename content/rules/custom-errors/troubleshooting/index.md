<h2 id="cannot-preview-error-page">Cannot preview error page</h2>
<p>If Cloudflare cannot load your site or you have blocked the United States (US) via <a href="/waf/tools/ip-access-rules/">IP Access rules</a> or <a href="/waf/custom-rules/">WAF custom rules</a>, publishing and previewing a custom error page might not work.</p>
<p>A common error might look like the following: <code>Error fetching page: Fetch failed, https://example.com/ipcountryblock.html returned 403 (Code: 1202)</code>.</p>
<p>Make sure that no WAF rule is blocking or challenging Custom Errors product when it is fetching the content of your custom error page.</p>
<h2 id="error-pages-for-blocked-requests">Error pages for blocked requests</h2>
<p>If you block countries or IP addresses with an <a href="/waf/tools/ip-access-rules/">IP Access rule</a>, affected visitors will get a <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1005/">1005 error</a> and your <strong>IP/Country Block</strong> custom page.</p>
<p>If you block countries or IP addresses with a <a href="/waf/custom-rules/">WAF custom rule</a> and you do not configure a <a href="/rules/custom-errors/create-rules/#create-a-custom-error-rule-dashboard">custom error rule</a> or a <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">WAF custom response</a> for blocked requests, affected visitors will get your <strong>WAF Block</strong> page.</p>
<p>If you block requests due to a <a href="/waf/rate-limiting-rules/">rate limiting rule</a> and you do not configure a <a href="/rules/custom-errors/create-rules/#create-a-custom-error-rule-dashboard">custom error rule</a> or a <a href="/waf/rate-limiting-rules/create-zone-dashboard/#configure-a-custom-response-for-blocked-requests">WAF custom response</a> for blocked requests, affected visitors will get your <strong>429 Errors</strong> page displaying a Cloudflare <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/">1015 error</a>.</p>
<p>If you block countries or IP addresses with a firewall rule (now deprecated), affected visitors will get your <strong>1000 Class Errors</strong> page.</p>
<h2 id="1xxx-errors">1XXX errors</h2>
<p>You cannot customize the following 1XXX errors via Error Pages:</p>
<ul>
<li><code>1001</code> - Unable to resolve</li>
<li><code>1003</code> - Bad Host header</li>
<li><code>1018</code> - Unable to resolve because of ownership lookup failure</li>
<li><code>1023</code> - Unable to resolve because of feature lookup failure</li>
</ul>
<h2 id="custom-error-page-size">Custom error page size</h2>
<p>Your custom error page cannot be blank and the combined size of all page assets cannot exceed 1.5 MB (1,500,000 characters). To avoid exceeding the custom error page limit, preview your page to check its size before publishing.</p>
<h2 id="general-troubleshooting-advice">General troubleshooting advice</h2>
<p>If you encounter errors while attempting to preview or publish your custom error page, use an <a href="https://validator.w3.org/">HTML validator</a> to ensure that your code resolves properly.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/">HTTP Status Codes</a></li>
<li><a href="/cloudflare-challenges/">Challenges</a></li>
</ul>
