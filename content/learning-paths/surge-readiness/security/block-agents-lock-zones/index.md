<p><a href="/waf/tools/user-agent-blocking/">User Agent (UA) Blocking</a> rules match against specific User-Agent request headers sent by the browser or application accessing your site. UA rules are applied against the entire domain, and after a rule is triggered, you can decide which action to take against the visitor.</p>
<p>Actions:</p>
<ul>
<li>Block: Ensures that an IP address will never be allowed to access your site</li>
<li>Interactive Challenge: Visitors will be shown an interactive challenge before allowed access</li>
<li>Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before allowed access</li>
</ul>
<h2 id="zone-lockdown">Zone Lockdown</h2>
<p><a href="/waf/tools/zone-lockdown/">Zone Lockdown</a> rules allow you to define paths and only allow specific, trusted IPs to those paths. Any requests to those paths from non-whitelisted IPs will be automatically blocked with an 1106 HTTP code. This ability is particularly useful for locking down administrative or staging portions of your application.</p>
