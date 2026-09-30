<p><a href="/waf/tools/ip-access-rules/">IP Access Rules</a> specify an action based on the origin of your user across a single domain or all of the domains in your account.</p>
<p>IP Access Rules can be applied based on:</p>
<ul>
<li>IPv4 address or range: Specified in CIDR notation as <code>/16</code> or <code>/24</code></li>
<li>IPv6 address or range: Specified in CIDR notation as <code>/32</code>, <code>/48</code>, <code>/64</code></li>
<li>ASN</li>
<li>Country or the Tor network</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10275.md")
</aside>
<p>Actions:</p>
<ul>
<li>Block: Ensures that an IP address will never be allowed to access your site.</li>
<li>Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before allowed access.</li>
<li>Interactive Challenge: Visitors will be shown an interactive challenge before allowed access.</li>
<li>Allowlist: Ensures that an IP address will never be blocked from accessing your site. This supersedes any Cloudflare security profile.</li>
</ul>
