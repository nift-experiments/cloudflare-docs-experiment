<p>If Cloudflare is providing <a href="/dns/zone-setups/full-setup/">authoritative DNS</a> for your domain, Cloudflare will issue a backup <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificate</a> for every standard Universal certificate issued.</p>
<p>Backup certificates are wrapped with a different private key and issued from a different Certificate Authority — either Google Trust Services, Let's Encrypt, Sectigo, or SSL.com — than your domain's primary Universal SSL certificate.</p>
<p>These backup certificates are not normally deployed, but they will be deployed automatically by Cloudflare in the event of a certificate revocation or key compromise.</p>
<p>For additional details, refer to the <a href="https://blog.cloudflare.com/introducing-backup-certificates/">introductory blog post</a>.</p>
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Can opt out?</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="opt-out">Opt out</h2>
<p>Enterprise customers can request to opt out of backup certificates by opening a support case. Opting out removes the backup-certificate redundancy for your domain.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="backup-certificate-deleted-after-turning-universal-ssl-back-on">Backup certificate deleted after turning Universal SSL back on</h3>
<p>After you turn off and quickly turn Universal SSL back on, your domain may end up without a backup certificate.</p>
<p>When Universal SSL is toggled off and on in quick succession, certificate processing jobs are not guaranteed to run in the order they were submitted. This race condition can cause a newly issued backup certificate to be deleted before it becomes active.</p>
<p>To recover your backup certificate:</p>
<ol>
<li>Turn Universal SSL off again.</li>
<li>Wait several minutes.</li>
<li>Turn Universal SSL back on, then allow time for Cloudflare to issue a new backup certificate.</li>
</ol>
<p>If you need uninterrupted certificate coverage, consider ordering an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> certificate before toggling Universal SSL.</p>
<p>For more troubleshooting help, refer to <a href="/ssl/troubleshooting/">Troubleshooting SSL errors</a>.</p>
