<h2 id="errors-1005-access-denied-autonomous-system-number-asn-banned">Errors 1005 Access Denied: Autonomous System Number (ASN) banned</h2>
<p>This error indicates that access to the website is denied due to the banning of the Autonomous System Number (ASN).</p>
<h3 id="common-causes">Common causes</h3>
<p>The owner of the website (for example, <code>example.com</code>) has banned the autonomous system number (ASN) from accessing the website.</p>
<h3 id="resolution">Resolution</h3>
<p>If you are not the website owner, provide the website owner with a screenshot of the 1005 error message you received.</p>
<p>If you are the website owner:</p>
<ol>
<li>Retrieve a screenshot of the <code>1005</code> error from your customer</li>
<li>Search the <a href="/waf/analytics/security-events/"><strong>Security Events log</strong></a> (available at <strong>Security</strong> &gt; <strong>Events</strong>) for the <a href="/fundamentals/reference/cloudflare-ray-id/"><strong>Ray ID</strong></a>, or client IP Address from the visitor's 1005 error message.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14742.md")
</aside>
<ol start="3">
<li>Assess the cause of the block and ensure the ASN is allowed under the <a href="/waf/tools/ip-access-rules/">IP Access Rules</a> security feature.</li>
</ol>
