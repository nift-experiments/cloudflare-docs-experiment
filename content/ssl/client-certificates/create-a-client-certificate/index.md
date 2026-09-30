<p>Use Cloudflare's public key infrastructure (PKI) to create client certificates issued from a Cloudflare-managed CA. You can then complete your mTLS configuration, as explained in <a href="/ssl/client-certificates/#how-it-works">How mTLS works</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-issued-or-byoca">Cloudflare-issued or BYOCA</h3>
@markup("md", "content/.markup/bodies/14028.md")
</aside>
<h2 id="quota-and-limits">Quota and limits</h2>
<p>By default, each zone allows up to <strong>100 active client certificates</strong> issued by the Cloudflare-managed CA. Only active certificates count toward this limit — revoking a certificate frees its slot immediately.</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Default limit</th>
<th>Increase available</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free, Pro, Business</td>
<td>100 per zone</td>
<td>No</td>
</tr>
<tr>
<td>Enterprise (with API Shield)</td>
<td>100,000 per zone</td>
<td>Yes, via account team</td>
</tr>
</tbody>
</table>
<p>If you reach the limit, the API returns error <code>1445</code> with the message <code>Hit maximum certificate allocation: 100 certificates per zone are allowed</code>. To request an increase, contact your account team. Increases require an Enterprise plan with API Shield.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="high-churn-workloads">High-churn workloads</h3>
@markup("md", "content/.markup/bodies/14027.md")
</aside>
<p>To create a client certificate on the Cloudflare dashboard:</p>
<ol>
<li>Go to the <strong>Client Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add Certificate</strong>. The Cloudflare-managed CA is the default <strong>Certificate Authority</strong>.</li>
<li>Fill in the required fields. You can choose one of the following options:</li>
</ol>
<ul>
<li>
<p>Generate a private key and Certificate Signing Request (CSR) with Cloudflare.</p>
</li>
<li>
<p>Use your own private key and CSR. This option allows you to also <a href="/ssl/client-certificates/label-client-certificate/">label client certificates</a>.</p>
<details class="nb-details"><summary>Example OpenSSL command</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/14029.md")
</div></details>
<ol start="3">
<li>
<p>Select a value for <strong>Certificate Validity</strong>, and choose <strong>Continue</strong>.</p>
</li>
<li>
<p>Make sure to copy the certificate and private key as they will no longer be displayed after creation.</p>
</li>
<li>
<p>(Optional) Specify hostnames where you wish to <a href="/ssl/client-certificates/enable-mtls/">enable mTLS</a>.</p>
<p>When associating hostnames via this form, they should be in fully qualified domain name (FQDN) format and correspond to a hostname that exists in the zone you are in. For example, if you are in zone <code>example.com</code>, you can specify <code>host.example.com</code> but not <code>host.example.net</code>.</p>
</li>
<li>
<p>Select <strong>Save</strong> to confirm.</p>
</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>After creating the client certificate, make sure it is installed on the client devices and <a href="/ssl/client-certificates/enable-mtls/">enable mTLS</a> for each hostname that should require a certificate from clients.</p>
<p>Refer to our <a href="/learning-paths/mtls/concepts/">mTLS at Cloudflare learning path</a> for further context.</p>
