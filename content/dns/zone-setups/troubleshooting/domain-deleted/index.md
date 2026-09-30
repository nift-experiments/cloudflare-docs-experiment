<p>Domain deletion commonly occurs for the following reasons:</p>
<ul>
<li>A user with access to the domain removed it.</li>
<li>The nameservers no longer point to Cloudflare. Cloudflare continuously monitors domain registration.</li>
<li>The domain was not authenticated (pending for 28 days).</li>
</ul>
<hr />
<h2 id="check-audit-logs">Check Audit Logs</h2>
<p>Cloudflare <a href="/fundamentals/account/account-security/review-audit-logs/">Audit Logs</a> contain information about domain deletion.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7898.md")
</aside>
<hr />
<h2 id="check-registrar-for-cloudflare-nameservers">Check registrar for Cloudflare nameservers</h2>
<p>If your domain was using a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a>, your registrar needs to use Cloudflare nameservers as the authoritative nameservers for your domain.</p>
<ol>
<li>
<p>Use either the command-line based <code>whois</code> application provided with your operating system or a website such as <a href="https://lookup.icann.org/">ICANN Lookup</a>.</p>
<ul>
<li>If you are unable to find the nameserver details for your domain, reach out to your domain registrar or domain provider to provide the domain registration information.</li>
<li>Ensure Cloudflare's nameservers are the only two nameservers listed in the domain registration details.</li>
<li>Ensure nameservers are spelled correctly in the domain registration.</li>
</ul>
</li>
<li>
<p>Confirm that the nameservers exactly match the nameservers provided within the <strong>Cloudflare Nameservers</strong> card on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page.</p>
</li>
<li>
<p>If you identify incorrect information, log in to your domain provider's portal to make updates or contact your domain provider for assistance.</p>
</li>
</ol>
<hr />
<h2 id="recover-a-deleted-domain">Recover a deleted domain</h2>
<p>To recover a deleted domain, <a href="/fundamentals/manage-domains/add-site/">re-add it in Cloudflare</a> just like you would for a new domain.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7897.md")
</aside>
