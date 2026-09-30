<p>Custom certificates are meant for Business and Enterprise customers who want to use their own SSL certificates.
<br /></p>
<p>Use custom certificates when you need control over the certificate authority (CA) or require Organization Validated (OV) or Extended Validation (EV) certificates that Cloudflare-managed options do not support.</p>
<p>Unlike <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a>, Cloudflare does not manage issuance and renewal for custom certificates. You are responsible for the following:</p>
<ul>
<li><a href="/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate">Upload the certificate</a>.</li>
<li><a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">Update the certificate</a> before it expires.</li>
<li><a href="/ssl/edge-certificates/custom-certificates/renewing/">Monitor the certificate expiration date</a> to avoid downtime.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14094.md")
</aside>
<h2 id="certificate-packs">Certificate packs</h2>
<p>Before deploying custom certificates to Cloudflare's global network, Cloudflare automatically groups the certificates into certificate packs.</p>
<p>A certificate pack is a group of certificates that share the same set of hostnames — for example, <code>example.com</code> and <code>*.example.com</code> — but use different signature algorithms.</p>
<p>Each pack can include up to three certificates, one from each of the following signature algorithms:</p>
<ul>
<li><code>SHA-2/RSA</code></li>
<li><code>SHA-2/ECDSA</code></li>
<li><code>SHA-1/RSA</code></li>
</ul>
<p>Each pack only counts as one SSL certificate against your custom certificate quota.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14093.md")
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
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Certificate packs included</td>
<td>0</td>
<td>0</td>
<td>5 Modern and 1 Legacy</td>
<td>5 Modern (can purchase more) and 1 Legacy (can purchase more)</td>
</tr>
</tbody>
</table>
<h2 id="related-features">Related features</h2>
<h3 id="certificate-signing-requests-csrs">Certificate Signing Requests (CSRs)</h3>
<p>You can use Cloudflare to generate a <a href="/ssl/edge-certificates/additional-options/certificate-signing-requests/">Certificate Signing Request (CSR)</a> for your custom certificate. When you do, Cloudflare generates and securely stores the private key associated with the CSR.</p>
<h3 id="geo-key-manager-private-key-restriction">Geo Key Manager (private key restriction)</h3>
<p>By default, Cloudflare encrypts and securely distributes private keys to all Cloudflare data centers, where they can be used for local SSL/TLS termination. If you want to restrict where your private keys may be used, use <a href="/ssl/edge-certificates/geokey-manager/">Geo Key Manager</a>.</p>
<h3 id="keyless-ssl">Keyless SSL</h3>
<p>If you want to upload a custom certificate but retain your private key on your own infrastructure, consider using <a href="/ssl/keyless-ssl/">Keyless SSL</a>.</p>
<h3 id="certificate-pinning">Certificate pinning</h3>
<p>Custom certificates are the only certificate type where certificate pinning can work on Cloudflare. For guidance on pinning and its risks, refer to <a href="/ssl/reference/certificate-pinning/">Certificate pinning</a>.</p>
