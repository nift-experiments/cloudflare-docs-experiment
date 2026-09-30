<p>Use advanced certificates when you want something more customizable than <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> but still want the convenience of SSL certificate issuance and renewal.</p>
<br />
<p>To order advanced certificates, you must purchase the Advanced Certificate Manager add-on. This add-on also unlocks the features listed below.</p>
<h2 id="what-the-add-on-includes">What the add-on includes</h2>
<p>Advanced Certificate Manager allows you to:</p>
<ul>
<li>Order advanced certificates that can:
<ul>
<li>Include up to 50 hosts as covered hostnames (the zone apex must be one of these 50).</li>
<li>Cover more than one level of subdomain.</li>
<li>Be issued by the certificate authority (CA) you choose.</li>
<li>Use your preferred validation method.</li>
<li>Have the validity period you choose.</li>
</ul>
</li>
<li>Automate <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/14121.md")
</div> for zones on a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/14122.md")
</div> using [delegated DCV](/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/).
- Enable [Total TLS](/ssl/edge-certificates/additional-options/total-tls/) to automatically protect proxied hostnames.
- Select a [custom trust store](/ssl/origin-configuration/custom-origin-trust-store/) for origin authentication.
- Control [cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/) and [per-hostname minimum TLS version](/ssl/edge-certificates/additional-options/minimum-tls/#per-hostname).
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14120.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14118.md")
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
<td>Paid add-on</td>
<td>Paid add-on</td>
<td>Paid add-on</td>
<td>Paid add-on</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14117.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Advanced certificates do not apply to <a href="/pages/">Cloudflare Pages</a> or <a href="/r2/">R2</a> custom domains. Due to <a href="/ssl/reference/certificate-and-hostname-priority/">certificate prioritization</a>, these products use Cloudflare for SaaS certificates instead.</p>
<p>Advanced certificates are <a href="/ssl/concepts/#validation-level">Domain Validated (DV)</a>. If your organization needs Organization Validated (OV) or Extended Validation (EV) certificates, refer to <a href="/ssl/edge-certificates/custom-certificates/">Custom certificates</a>. <br/></p>
<p>Advanced certificates cover hostnames within a single domain. If you need a certificate that spans multiple domains (a multi-domain certificate), use <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>. For architecture guidance, refer to <a href="/reference-architecture/design-guides/leveraging-cloudflare-for-your-saas-applications/">Leveraging Cloudflare for your SaaS applications</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14116.md")
</aside>
<h2 id="multi-level-subdomain-support">Multi-level subdomain support</h2>
<p>Advanced Certificate Manager supports deep, multi-level subdomains (for example, <code>api.staging.example.com</code>). There is no arbitrary limit on the number of subdomain levels, but you must consider the following constraints.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14115.md")
</aside>
<h3 id="domain-name-length-limits">Domain name length limits</h3>
<p>These limits are defined by internet standards (<a href="https://www.rfc-editor.org/rfc/rfc1035">RFC 1035</a> and <a href="https://www.rfc-editor.org/rfc/rfc5280">RFC 5280</a>) and apply to all certificates, regardless of the certificate authority:</p>
<ul>
<li><strong>Total domain length</strong>: The entire domain name cannot exceed 253 characters.</li>
<li><strong>Label length</strong>: Each individual level (the text between dots) cannot exceed 63 characters.</li>
<li><strong>Common Name (CN) length</strong>: The Common Name field of a certificate cannot exceed 64 characters. If a hostname on your certificate exceeds 64 characters, you must order the certificate via the <a href="/api/resources/ssl/subresources/certificate_packs/methods/create/">API</a> and set the <code>cloudflare_branding</code> option to <code>true</code>. This places <code>sni.cloudflaressl.com</code> in the CN field and your long hostname in the SAN field. The dashboard does not support ordering certificates with hostnames longer than 64 characters.</li>
</ul>
<h3 id="wildcard-coverage">Wildcard coverage</h3>
<p>Wildcard certificates only cover <strong>one subdomain level</strong>:</p>
<ul>
<li>A certificate for <code>*.example.com</code> covers <code>www.example.com</code> and <code>api.example.com</code> but <strong>not</strong> <code>api.staging.example.com</code>.</li>
<li>To cover multiple levels, you must explicitly add a wildcard for each level to your certificate (for example, <code>*.example.com</code>, <code>*.staging.example.com</code>).</li>
</ul>
<h3 id="hostnames-per-certificate">Hostnames per certificate</h3>
<p>A single advanced certificate can include up to <strong>50 hosts</strong> (SANs) total. The zone apex must be one of these 50, leaving room for up to 49 additional hostnames or wildcards.</p>
<h3 id="consistency-across-certificate-authorities">Consistency across certificate authorities</h3>
<p>The character-length limits above (253-character total, 63-character label, 64-character CN) are defined by IETF standards (<a href="https://www.rfc-editor.org/rfc/rfc1035">RFC 1035</a>, <a href="https://www.rfc-editor.org/rfc/rfc5280">RFC 5280</a>) and apply uniformly across all CAs. Other constraints, such as the per-certificate SAN count and supported validity periods, are Cloudflare advanced certificates limits or vary by CA. Refer to <a href="/ssl/reference/certificate-authorities/">Certificate authorities</a> for CA-specific details.</p>
<h2 id="related-resources">Related resources</h2>
<ul class="directory-listing"><li><a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">Manage advanced certificates</a></li><li><a href="/ssl/edge-certificates/advanced-certificate-manager/api-commands/">API commands</a></li></ul>
