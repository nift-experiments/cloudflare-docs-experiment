<p>When you use a subdomain setup, you can manage the <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare configurations</a> for one or more subdomains separately from those associated with your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7905.md")
</div>. This means that, on your [account homepage](https://dash.cloudflare.com/?to=/:account/), you would find websites like `example.com` or `blog.example.com` listed as separate <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/7906.md")
</div>.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7904.md")
</aside>
<p>You might use this setup when you want to share access to a specific subdomain's settings with different teams, but have stricter controls on your apex domain. For example, a subdomain setup could allow your documentation team to manage the Cloudflare configuration for <code>docs.example.com</code>, while preventing them from adjusting any settings on <code>example.com</code>.</p>
<p>Subdomain setups are also useful when different subdomains require entirely different settings. For example, you may have different requirements for <code>docs.example.com</code>, <code>blog.example.com</code>, and <code>community.example.com</code>.</p>
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
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="setup-combinations">Setup combinations</h3>
@markup("md", "content/.markup/bodies/7903.md")
</aside>
<h3 id="access-applications">Access applications</h3>
<p>To use subdomain setups with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>, note that:</p>
<ul>
<li>
<p>If the child zone is in a pending state when you create the Access application, your configuration will not automatically apply when you activate the zone. You must also re-save the Access application once your subdomain setup is active.</p>
</li>
<li>
<p>If you split out a subdomain which already has an Access application, you will also need to re-save the Access application to associate it with the new child zone.</p>
</li>
</ul>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/dns/zone-setups/subdomain-setup/setup/">Setup</a></li><li><a href="/dns/zone-setups/subdomain-setup/dnssec/">Enable DNSSEC</a></li><li><a href="/dns/zone-setups/subdomain-setup/move-to-new-account/">Migrate to new account</a></li><li><a href="/dns/zone-setups/subdomain-setup/rollback/">Rollback</a></li></ul>
<h2 id="faq">FAQ</h2>
<h3 id="why-does-my-parent-zone-show-dns-queries-for-child-zone-hostnames">Why does my parent zone show DNS queries for child zone hostnames?</h3>
<p>If you have both a parent zone (for example, <code>example.com</code>) and a child subdomain zone (for example, <code>sub.example.com</code>) on Cloudflare, the parent zone's DNS analytics may show queries for hostnames belonging to the child zone.</p>
<p>This is normal DNS behavior — recursive resolvers query the parent zone first to get the referral (NS records) pointing to the child zone's nameservers. These referral queries appear in the parent zone's analytics even though the authoritative answer comes from the child zone.</p>
