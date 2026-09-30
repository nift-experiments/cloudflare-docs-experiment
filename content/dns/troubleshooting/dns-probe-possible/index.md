<p>If you or your visitors experience <code>DNS_PROBE_POSSIBLE</code> errors after you <a href="/dns/zone-setups/full-setup/setup/">activate your domain on Cloudflare</a>, review your DNS records in Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7557.md")
</aside>
<h2 id="background">Background</h2>
<p><code>DNS_PROBE_POSSIBLE</code> means that the resolver could not find <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7558.md")
</div> for the requested hostname.
<p>Though visitors sometimes encounter this error — or similarly worded messages from Safari, Edge, or Firefox — because of network or local DNS issues, it might point to an issue with your DNS records in Cloudflare.</p>
<h2 id="potential-solutions">Potential solutions</h2>
<p>If you experience <code>DNS_PROBE_POSSIBLE</code> errors with a newly activated domain, review your DNS settings in the Cloudflare dashboard.</p>
<p>Check your expected apex domain (<code>example.com</code>) and any active subdomains (<code>www.example.com</code> or <code>blog.example.com</code>). If they do not resolve correctly, you may need to <a href="/dns/manage-dns-records/how-to/create-zone-apex/">add a record on the zone apex</a> or a <a href="/dns/manage-dns-records/how-to/create-subdomain/">subdomain record</a> in Cloudflare DNS.</p>
<p>If you have the correct records set up, make sure those records are also pointing to the correct origin IP address.</p>
<p>After making changes to your DNS records, you may need to wait a few minutes for those changes to take effect.</p>
