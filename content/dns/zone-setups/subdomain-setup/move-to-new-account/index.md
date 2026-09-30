<p>When using a <a href="/dns/zone-setups/subdomain-setup/">subdomain setup</a>, you can have your subdomain as a separate zone within the same account as the parent domain or within a different account.</p>
<p>If you have already <a href="/dns/zone-setups/subdomain-setup/setup/">created a standalone subdomain zone</a> within the same account, you can still move it to a separate account.</p>
<ol>
<li><a href="/fundamentals/manage-domains/add-site/">Add the subdomain</a> to a new Cloudflare account.</li>
<li>In the original subdomain zone, <a href="/dns/manage-dns-records/how-to/import-and-export/#export-records">export</a> the DNS records.</li>
<li>Review the exported records, delete any unnecessary ones, and <a href="/dns/manage-dns-records/how-to/import-and-export/#import-records">import</a> them into the new subdomain zone.</li>
<li>Update the <code>NS</code> records in the parent zone to refer to the newly assigned nameservers of the child zone.</li>
</ol>
