<p>To help avoid <a href="/ssl/troubleshooting/version-cipher-mismatch/"><code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code></a> errors, Cloudflare automatically shows an error message - <code>This hostname is not covered by a certificate</code> - on proxied DNS records not covered by a TLS certificate.</p>
<h2 id="pending-domains">Pending domains</h2>
<p>If you recently <a href="/fundamentals/manage-domains/add-site/">added your domain</a> to Cloudflare - meaning that your zone is in a <a href="/dns/zone-setups/reference/domain-status/">pending state</a> - you can often ignore this warning.</p>
<p>Once most domains becomes <strong>Active</strong>, Cloudflare will automatically issue a Universal SSL certificate, which will provide SSL/TLS coverage and remove the warning message.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14157.md")
</aside>
<h2 id="active-domains">Active domains</h2>
<p>If your zone is already active on Cloudflare, this warning identifies subdomains that are not covered by your current SSL/TLS certificate.</p>
<p>By default, Cloudflare <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificates</a> only cover your apex domain and one level of subdomain.</p>
<table>
<thead>
<tr>
<th>Hostname</th>
<th>Covered by Universal certificate?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>www.example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>docs.example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>dev.docs.example.com</code></td>
<td>No</td>
</tr>
<tr>
<td><code>test.dev.api.example.com</code></td>
<td>No</td>
</tr>
</tbody>
</table>
<p>To prevent insecure connections on a multi-level subdomain, do one of the following:</p>
<ul>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a>, which automatically issues individual certificates to your proxied hostnames not covered by a Universal certificate.</li>
<li>Order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">Advanced Certificate</a> covering the subdomain.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates/">Custom Certificate</a> covering the subdomain.</li>
</ul>
<p>If none of these solutions work, you could also remove the multi-level subdomain.</p>
