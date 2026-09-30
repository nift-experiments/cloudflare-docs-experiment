<h2 id="error-1020-access-denied">Error 1020: Access denied</h2>
<p>This error indicates that access to the website is denied by a Cloudflare firewall rule.</p>
<h3 id="common-cause">Common cause</h3>
<p>A client or browser is blocked by a Cloudflare customer's Firewall Rules (deprecated).</p>
<h3 id="resolution">Resolution</h3>
<p>If you are not the website owner, provide the website owner with a screenshot of the <code>1020</code> error message you received.</p>
<p>If you are the website owner:</p>
<ol>
<li>Retrieve a screenshot of the 1020 error from your customer.</li>
<li>Search the <a href="/waf/analytics/security-events/">Security Events log</a> (available at <strong>Security</strong> &gt; <strong>Analytics</strong>, in the <strong>Events</strong> tab) for the <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a> or client IP address from the visitor's 1020 error message.</li>
</ol>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14734.md")
</aside>
<ol start="3">
<li>Assess the cause of the block and either update the Firewall Rule or allow the visitor's IP address in <a href="/waf/tools/ip-access-rules/">IP Access Rules</a>.</li>
</ol>
