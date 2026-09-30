<p>Edge certificates are the SSL/TLS certificates that Cloudflare presents to visitors connecting to your domain. These certificates secure the encrypted connection between your visitors and Cloudflare.</p>
<p>Use the guidance below to choose the right certificate type for your use case. If you are not familiar with SSL/TLS certificates, refer to <a href="/ssl/concepts/">Concepts</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14003.md")
</aside>
<h2 id="use-cases">Use cases</h2>
<h3 id="simplify-issuance-and-renewal">Simplify issuance and renewal</h3>
<p>Managing certificate issuance, renewal, and expiration tracking can be time-consuming. Cloudflare can handle this for you:</p>
<ul>
<li><a href="/ssl/edge-certificates/universal-ssl/"><strong>Universal SSL</strong></a>: Automatic, free certificates for your apex domain and first-level subdomains. Provisioned automatically on <a href="/dns/zone-setups/full-setup/">full setups</a>.</li>
<li><a href="/ssl/edge-certificates/advanced-certificate-manager/"><strong>Advanced certificates</strong></a>: Automatic certificates with more control — choose your certificate authority (CA), covered hostnames, and validity period.</li>
<li><a href="/ssl/edge-certificates/custom-certificates/"><strong>Custom certificates</strong></a>: Upload your own certificates for full control over the CA and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/14004.md")
</div>. You handle issuance and renewal.
<h3 id="meet-cipher-suites-requirements">Meet cipher suites requirements</h3>
<p>A cipher suite is a set of encryption algorithms that a visitor's browser and the server negotiate when establishing a secure connection. Some compliance standards (for example, PCI DSS) require specific cipher suites or prohibit older ones.</p>
<p>With <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">cipher suites customization</a>, you can set different cipher suites per hostname. For example, you could allow broader compatibility on <code>www.example.com</code> for legacy devices while enforcing stricter <a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">compliance standards</a> on <code>shop.example.com</code>.</p>
<p>Custom cipher suites apply to any edge certificate serving that hostname. To use this feature, you must <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/acm/">purchase the Advanced Certificate Manager add-on</a>. Refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customize cipher suites</a> for setup instructions.</p>
<h3 id="automate-domain-control-validation-dcv">Automate domain control validation (DCV)</h3>
<p>Before a certificate authority (CA) issues a certificate, it must verify you control the domain. This process is called <a href="/ssl/edge-certificates/changing-dcv-method/">domain control validation (DCV)</a>.</p>
<p>If Cloudflare runs your authoritative DNS (<a href="/dns/zone-setups/full-setup/">full setup</a>), DCV happens automatically. If you manage DNS with another provider (<a href="/dns/zone-setups/partial-setup/">partial setup</a>), you may need to complete DCV manually each time a certificate is issued or renewed.</p>
<p>To automate DCV for partial setups, use <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a> with <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">delegated DCV</a>.</p>
