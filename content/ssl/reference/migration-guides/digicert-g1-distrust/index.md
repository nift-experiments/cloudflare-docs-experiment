<p>Browsers and operating systems are completing the removal of DigiCert's legacy G1 root certificates from their trust stores, effective <strong>April 15, 2026</strong>.</p>
<p>DigiCert announced this planned deprecation in 2023 and has been issuing certificates from their newer G2 roots since 2020.</p>
<p>Since DigiCert is not within the <a href="/ssl/reference/certificate-authorities/">certificate authorities</a> used by Cloudflare, this change may only affect customers who upload <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a> issued from DigiCert G1 roots.</p>
<h2 id="the-change">The change</h2>
<p>The primary root being distrusted is <strong>DigiCert Global Root CA</strong>. The distrust also affects other legacy G1 intermediates cross-signed from this root.</p>
<p>DigiCert Global Root G2 and G3 remain fully trusted. Certificates that chain to G2 are unaffected.</p>
<p>Refer to <a href="https://knowledge.digicert.com/general-information/digicert-root-and-intermediate-ca-certificate-updates-2023">DigiCert's root and intermediate CA certificate updates</a> for the full list of affected roots.</p>
<h2 id="digicert-s-recommendation">DigiCert's recommendation</h2>
<p>DigiCert recommends reissuing any affected certificates from a G2 intermediate. This is a standard reissuance — you do not need to generate a new key in most cases.</p>
<h2 id="cloudflare-managed-certificates">Cloudflare-managed certificates</h2>
<p>Since Cloudflare does not use DigiCert roots, you can avoid this dependency entirely by switching to Cloudflare-managed certificates:</p>
<ul>
<li>Use <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificates</a> for more control and flexibility with automatic renewals.</li>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> to automatically issue certificates for your <a href="/dns/proxy-status/">proxied hostnames</a>.</li>
<li>Use <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a> to reduce manual intervention when renewing certificates for <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setup</a> zones.</li>
</ul>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="https://knowledge.digicert.com/general-information/digicert-root-and-intermediate-ca-certificate-updates-2023">DigiCert root and intermediate CA certificate updates</a></li>
<li><a href="/ssl/edge-certificates/custom-certificates/">Custom certificates</a></li>
<li><a href="/ssl/edge-certificates/custom-certificates/bundling-methodologies/">Certificate bundling methodologies</a></li>
</ul>
