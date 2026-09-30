<p>When you choose HTTP DCV, Cloudflare automatically adds a verification HTTP token to your domain.</p>
<p>Only use this method if your domain can tolerate a few minutes of downtime.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14191.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>HTTP DCV is only available for <a href="/dns/proxy-status/">proxied domains</a>. It is possible to manually add the DCV token to the <code>.well-known/pki-validation/</code> directory on your origin web server to pre-validate your certificates.</p>
<p>HTTP DCV validation does not work for wildcard certificates. If you want to use wildcard certificates, use <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT validation</a>.</p>
<p>Based on your chosen certificate authority (CA), you may also not be able to use HTTP verification with <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a>.</p>
<h2 id="setup">Setup</h2>
<h3 id="specify-dcv-method">Specify DCV method</h3>
<p>If you want to use a <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/">Universal SSL certificate</a>, you will need to edit the <code>validation_method</code> <a href="/api/resources/ssl/subresources/verification/methods/edit/">via the API</a> and specify your chosen validation method.</p>
<p>Alternatively, you could <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate">order an advanced certificate</a> via the API.</p>
<p>In either case, you would need to set a <code>&quot;validation_method&quot;:&quot;http&quot;</code> parameter.</p>
<h3 id="review-other-cloudflare-settings">Review other Cloudflare settings</h3>
<p>To make sure your domain does not accidentally block HTTP DCV, review your Cloudflare settings for <a href="/ssl/edge-certificates/changing-dcv-method/troubleshooting/">common setup issues</a>.</p>
<h3 id="complete-dcv">Complete DCV</h3>
<p>Your HTTP token will be available for the certificate authority as soon as you finish your <a href="/dns/zone-setups/partial-setup/setup/#3-add-dns-records">partial domain setup</a>.</p>
<p>This means that you need to add a CNAME record to Cloudflare in your authoritative DNS and create <a href="/dns/proxy-status/">proxied DNS records</a> for your hostname within Cloudflare.</p>
<p>This process may involve a few minutes of downtime.</p>
<details class="nb-details"><summary>What happens after you create your records</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14192.md")
</div></details>
<p>To check whether your certificates have been validated and reissued:</p>
<ul>
<li><strong>Dashboard</strong>: Find the certificate(s) on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page and make sure that the <strong>Status</strong> is <strong>Active</strong>.</li>
<li><strong>API</strong>: Send a <a href="/api/resources/ssl/subresources/certificate_packs/methods/list/"><code>GET</code></a> request and confirm that your certificate(s) have <code>&quot;status&quot;: &quot;active&quot;</code>.</li>
</ul>
<h2 id="renewal">Renewal</h2>
<p>Even if you manually handle DCV when issuing certificates in a <a href="/dns/zone-setups/partial-setup/">partial DNS setup</a>, at certificate renewal, Cloudflare will attempt to automatically perform DCV via HTTP.</p>
<p>If all of the following conditions are confirmed at the first attempt, the renewal happens automatically via <a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP</a>.</p>
<ul>
<li>Hostnames are proxied.</li>
<li>Hostnames on the certificate resolve to the IPs assigned to the zone.</li>
<li>The certificate does not contain wildcards.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14190.md")
</aside>
<p>If the conditions are met but HTTP DCV fails successively, the process will fall back to TXT. This schedule varies according to the certificate validity period.</p>
<ul>
<li>90-days certificates: after failing for 15 days</li>
<li>30-days certificates: after failing for 7 days</li>
<li>14-days certificates: after failing for 3 days</li>
</ul>
