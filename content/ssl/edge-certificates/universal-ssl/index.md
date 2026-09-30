<div class="nb-glossary-definition"><p>By default, Cloudflare issues — and <a href="/ssl/reference/certificate-validity-periods/#universal-ssl">renews</a> — free, unshared, publicly trusted SSL certificates to all domains <a href="/fundamentals/manage-domains/add-site/">added to</a> and <a href="/dns/zone-setups/reference/domain-status/">activated on</a> Cloudflare.</p></div>
<p>On a <a href="/dns/zone-setups/full-setup/">full setup</a>, Universal SSL certificates cover your root domain (for example, <code>example.com</code>) and first-level subdomains (for example, <code>www.example.com</code>). On a <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setup</a>, each proxied subdomain receives its own certificate regardless of depth. Cloudflare handles issuance, renewal, and deployment automatically.</p>
<p>For full setup zones that need coverage beyond first-level subdomains, use <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a>.</p>
<p>Universal certificates are <a href="/ssl/concepts/#validation-level">Domain Validated (DV)</a>, which means the certificate authority verifies domain ownership but does not validate organization identity. For setup details, refer to <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/">Enable Universal SSL</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14051.md")
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ssl/edge-certificates/universal-ssl/limitations/">Limitations</a></li>
<li><a href="/ssl/edge-certificates/backup-certificates/">Backup certificates</a></li>
<li><a href="/ssl/reference/certificate-validity-periods/#universal-ssl">Validity period and renewal</a></li>
</ul>
