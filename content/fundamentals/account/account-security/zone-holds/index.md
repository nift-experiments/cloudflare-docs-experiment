<p>Zone holds prevent other teams in your organization from adding zones that are already active in another account.</p>
<p>For example, you might already have an active Cloudflare zone for <code>example.com</code>. If another team does not realize this, they could add and activate <code>example.com</code> in another Cloudflare account, which may cause downtimes or security issues until the original zone could be re-activated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8939.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-zone-holds">Enable zone holds</h2>
<p>When you enable a zone hold, no one else can <a href="/fundamentals/manage-domains/add-site/">add your zone</a> to their Cloudflare account. If they attempt to, they will receive the following message:</p>
<p><em>The zone name provided is subject to a hold which disallows the creation of this zone. Please contact the domain owner to have this hold removed.</em></p>
<p>To enable a zone hold:</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Select your account and zone.</li>
<li>On the zone homepage, go to <strong>Quick Actions</strong>.</li>
<li>For <strong>Zone Hold</strong>, switch the toggle to <strong>On</strong>.</li>
</ol>
<p>You also have the option to <strong>Also prevent subdomains</strong>, which prevents anyone in your organization from creating subdomains or custom hostnames related to your zone.</p>
<h2 id="release-zone-holds">Release zone holds</h2>
<p>You may want to temporarily release a zone hold to allow another team to <a href="/dns/zone-setups/subdomain-setup/">register a subdomain</a> in a separate Cloudflare account, such as <code>docs.example.com</code>.</p>
<p>To release a zone hold:</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Select your account and zone.</li>
<li>On the zone homepage, go to <strong>Quick Actions</strong>.</li>
<li>For <strong>Zone Hold</strong>, switch the toggle to <strong>Off</strong>.</li>
<li>Choose the length of your release.</li>
<li>Select <strong>Release hold</strong>.</li>
</ol>
