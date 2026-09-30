<p>Refer to the following process to understand how you can rollback a <a href="/dns/zone-setups/subdomain-setup/">subdomain setup</a> and recreate the corresponding subdomain DNS records in an existing parent zone within Cloudflare.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>This guide assumes both your child domain (<code>blog.example.com</code>) and its parent domain (<code>example.com</code>) are in Cloudflare.</li>
<li>In the child zone, review and <a href="/dns/manage-dns-records/how-to/import-and-export/#export-records">export</a> the DNS records.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7902.md")
</aside>
<h2 id="steps">Steps</h2>
<ol>
<li>(Optional) In the parent zone, migrate over any settings - <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/">Rules</a>, <a href="/workers/">Workers</a>, and more - that might be needed for the child domain.</li>
<li>(Optional) If necessary, <a href="/ssl/edge-certificates/advanced-certificate-manager/">order an advanced SSL certificate</a> that covers the child domain and any deeper subdomains.</li>
<li>In the parent zone, go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page.</li>
<li>Delete one of the <code>NS</code> records defined for the child domain.</li>
<li>Edit the remaining <code>NS</code> record to create the subdomain address record.</li>
<li><a href="/dns/manage-dns-records/how-to/import-and-export/#import-records">Import</a> the records you had obtained <a href="#before-you-begin">before you began</a>.</li>
</ol>
