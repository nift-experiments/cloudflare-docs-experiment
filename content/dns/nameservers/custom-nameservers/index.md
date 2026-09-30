<p>With custom (or vanity) nameservers, a domain can use Cloudflare DNS without using Cloudflare-branded nameservers. For instance, you can configure <code>ns1.example.com</code> and <code>ns2.example.com</code> as nameservers for <code>example.com</code>.</p>
<p>To use custom nameservers, a zone must be using Cloudflare as Primary (<a href="/dns/zone-setups/full-setup/">Full setup</a>) or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a> DNS provider.</p>
<h2 id="configuration-scope">Configuration scope</h2>
<ul class="directory-listing"><li><a href="/dns/nameservers/custom-nameservers/zone-custom-nameservers/">Set up zone custom nameservers</a></li><li><a href="/dns/nameservers/custom-nameservers/account-custom-nameservers/">Set up account custom nameservers</a></li><li><a href="/dns/nameservers/custom-nameservers/tenant-custom-nameservers/">Set up tenant custom nameservers</a></li></ul>
<h2 id="availability">Availability</h2>
<ul>
<li>Zone custom nameservers are available for zones on Business or Enterprise plans. Via API or on the dashboard.</li>
<li>Account custom nameservers are available for customers on Business (after <a href="/support/contacting-cloudflare-support/">contacting Cloudflare Support</a>) or Enterprise plans. Once configured, account custom nameservers can be used by all zones in the account, regardless of the zone plan. Via API or on the dashboard.</li>
<li>Tenant custom nameservers, if created by the tenant owner, will be available to all zones belonging to any account that is part of the tenant. Via API only.</li>
</ul>
<h2 id="restrictions">Restrictions</h2>
<p>Custom nameservers are organized in different sets (<code>ns_set</code>). Each namesever set must have at least two and no more than five custom nameserver names.</p>
<p>The advantages that come with Foundation DNS <a href="/dns/foundation-dns/advanced-nameservers/">advanced nameservers</a> are currently not available for <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>. Make sure you only use one at a time.</p>
