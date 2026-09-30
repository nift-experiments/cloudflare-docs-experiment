<p>Universal SSL certificates present some limitations.</p>
<h2 id="proxy-status">Proxy status</h2>
<p>Cloudflare can only serve an SSL/TLS certificate for a DNS record when you set the record's <a href="/dns/proxy-status/">proxy status</a> to <strong>Proxied</strong>. If you do not do this, the origin server your record points to will be responsible for supporting SSL/TLS connections.</p>
<h2 id="hostname-coverage">Hostname coverage</h2>
<h3 id="full-setup">Full setup</h3>
<p>When you rely only on Universal SSL in a full setup zone, coverage is limited to the root domain (for example, <code>example.com</code>) and first-level subdomains (for example, <code>www.example.com</code> or <code>blog.example.com</code>). Deeper subdomains — such as <code>dev.www.example.com</code> or <code>app3.dev.www.example.com</code> — are <strong>not</strong> covered and will not serve a valid certificate.</p>
<p>To enable SSL for deeper subdomains, you can:</p>
<ul>
<li>Purchase <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> — then turn on <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> for automatic certificate coverage of all proxied subdomains, or manually create advanced certificates for specific hostnames.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates/">custom SSL certificate</a> that includes the required subdomains as Subject Alternative Names (SANs).</li>
</ul>
<h3 id="cname-setup">CNAME setup</h3>
<p>On a <a href="/dns/zone-setups/partial-setup/">CNAME setup zone</a>, each subdomain (regardless of level) has its own Universal SSL certificate and does not require additional features or purchases. As long as the subdomains are proxied to Cloudflare, a universal certificate <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#partial-dns-setup">will be provisioned</a>.</p>
<h2 id="certificate-authority">Certificate authority</h2>
<p>For Universal SSL certificates, Cloudflare chooses the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14050.md")
</div> used for your certificate.
<p>Cloudflare can change the <a href="/ssl/reference/certificate-authorities/">certificate authority</a> without prior notification, and will not send any notification as the change happens.</p>
<p>If you want to choose the issuing certificate authority, <a href="/ssl/edge-certificates/advanced-certificate-manager/">order an advanced certificate</a>.</p>
<h2 id="validity-period">Validity period</h2>
<p>For Universal certificates, Cloudflare controls the validity period. Refer to <a href="/ssl/reference/certificate-validity-periods/#universal-ssl">validity periods and renewal</a> for details.</p>
<h2 id="tls-settings">TLS settings</h2>
<p><a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customizing cipher suites</a> is only available with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> or within <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">Cloudflare for SaaS</a>.</p>
<p>You can set up <a href="/ssl/edge-certificates/additional-options/minimum-tls/">minimum TLS version</a> at the zone level, but, for per-hostname settings, you must have <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a>.</p>
<h2 id="delegated-dcv">Delegated DCV</h2>
<p>Delegated DCV allows zones with <a href="/dns/zone-setups/partial-setup/">partial DNS setups</a> to delegate the DCV process to Cloudflare. DCV delegation will not work with Universal SSL certificates and requires the use of an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a>.</p>
<h2 id="spectrum">Spectrum</h2>
<p>Universal SSL is not compatible with <a href="/spectrum/">Cloudflare Spectrum</a>. If you are trying to use Spectrum, use either <a href="/ssl/edge-certificates/advanced-certificate-manager/">an advanced certificate</a> or <a href="/ssl/edge-certificates/custom-certificates/">a custom certificate</a>.</p>
<h2 id="load-balancing">Load balancing</h2>
<p>Due to internal limitations, Universal SSL certificates do not cover <a href="/load-balancing/load-balancers/dns-records/">load balancing hostnames</a> by default. This behavior will be corrected in the future.</p>
<h2 id="browser-support">Browser support</h2>
<p>For more on browser support, see <a href="/ssl/reference/browser-compatibility/">Browser compatibility</a>.</p>
<h2 id="ssl-invalid-brand-check">SSL invalid brand check</h2>
<p>Some domains are not eligible for Universal SSL if they contain words that conflict with trademarked domains.</p>
<p>To resolve this issue, you can:</p>
<ul>
<li>Purchase an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a>.</li>
<li>Upload your own <a href="/ssl/edge-certificates/custom-certificates/uploading/">custom certificate</a>.</li>
</ul>
<h2 id="certificate-pinning">Certificate pinning</h2>
<p>Cloudflare does not support HTTP public key pinning (HPKP) for universal, advanced, or custom hostname certificates. For details and recommended alternatives, refer to <a href="/ssl/reference/certificate-pinning/">Certificate pinning</a>.</p>
