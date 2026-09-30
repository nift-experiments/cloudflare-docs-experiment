<p>For certificates managed by Cloudflare, attempts to renew start at the auto renewal period and continue up until 24 hours before expiration. The auto renewal period varies according to the certificate validity period, as explained in the sections below.</p>
<p>If a certificate fails to renew and another valid certificate exists for the hostname, Cloudflare will deploy the valid certificate within the last 24 hours before expiration.</p>
<h2 id="certificate-types">Certificate types</h2>
<h3 id="universal-ssl">Universal SSL</h3>
<p>For Universal certificates, Cloudflare controls the validity periods and certificate authorities (CAs), making sure that renewal always occur.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="partial-setup-and-dcv">Partial setup and DCV</h3>
@markup("md", "content/.markup/bodies/13969.md")
</aside>
<p>Universal certificates have a 90-day validity period. The auto renewal period starts 30 days before expiration.</p>
<h3 id="advanced-certificates">Advanced certificates</h3>
<p>When you order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a>, you can select different certificate validity periods. Each certificate validity period has a corresponding auto renewal period, when <a href="/ssl/reference/certificate-validity-periods/">attempts to renew</a> will start.</p>
<table>
<thead>
<tr>
<th>Certificate validity period</th>
<th>Auto renewal period</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 year</td>
<td>30 days</td>
<td>Limited to Enterprise customers using <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a> with <a href="/ssl/reference/certificate-authorities/#sslcom">SSL.com</a></td>
</tr>
<tr>
<td>3 months</td>
<td>30 days</td>
<td></td>
</tr>
<tr>
<td>1 month</td>
<td>7 days</td>
<td>Not supported by <a href="/ssl/reference/certificate-authorities/#lets-encrypt">Let's Encrypt</a></td>
</tr>
<tr>
<td>2 weeks</td>
<td>3 days</td>
<td>Not supported by <a href="/ssl/reference/certificate-authorities/#lets-encrypt">Let's Encrypt</a></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13968.md")
</aside>
<h3 id="custom-certificates">Custom certificates</h3>
<p>For information regarding custom certificates (managed by you), consider this other page on <a href="/ssl/edge-certificates/custom-certificates/renewing/">renewal and expiration</a>.</p>
<h3 id="ssl-for-saas">SSL for SaaS</h3>
<p>For SSL for SaaS certificates, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/">Renew certificates</a>.</p>
<h2 id="domain-control-validation-dcv">Domain control validation (DCV)</h2>
<p>Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).</p>
<p><a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP validation</a> is attempted on renewals but will fall back to TXT validation depending on the certificate validity period:</p>
<ul>
<li>90-days certificates: after failing for 15 days</li>
<li>30-days certificates: after failing for 7 days</li>
<li>14-days certificates: after failing for 3 days</li>
</ul>
<h2 id="benefits-of-shorter-validity-periods">Benefits of shorter validity periods</h2>
<p>Cloudflare only issues certificates with validity periods of three months or less for two reasons.</p>
<p>First, shorter-lived certificates limit the damage from key compromise and mistaken issuance. Any compromised key material will be valid for a shorter period of time.</p>
<p>Second, shorter certificates encourage automation. The more frequently you have to do a task, the more likely you will want to automate it. Automation also means that you are less likely to let a certificate expire in production or give a person access to key material.</p>
<p>For more details on the benefits of shorter validity periods, refer to our <a href="https://blog.cloudflare.com/advanced-certificate-manager/">blog post introducing Advanced Certificate Manager</a>.</p>
