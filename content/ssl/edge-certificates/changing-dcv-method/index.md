<p>Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).</p>
<p>If DCV is not completed, the CA cannot issue or renew the certificate, and visitors to your site will see SSL/TLS errors.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14106.md")
</aside>
<p>For <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a>, you handle DCV directly with the CA when requesting or renewing the certificate.</p>
<p>For certificates issued through Cloudflare, whether DCV is automatic depends on your DNS setup.</p>
<hr />
<h2 id="full-dns-setup-no-action-required">Full DNS setup - no action required</h2>
<p>If your domain is on a <a href="/dns/zone-setups/full-setup/"><strong>full setup</strong></a> — meaning that Cloudflare runs your authoritative nameservers — Cloudflare handles DCV automatically on your behalf using a TXT record. For more details, refer to <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#full-dns-setup">Enable Universal SSL</a>.</p>
<hr />
<h2 id="partial-dns-setup-action-sometimes-required">Partial DNS setup - action sometimes required</h2>
<p>If your application is on a <a href="/dns/zone-setups/partial-setup/">partial DNS setup</a> — meaning that Cloudflare does not run your authoritative nameservers — you may need to perform additional steps to complete DCV.</p>
<h3 id="non-wildcard-certificates">Non-wildcard certificates</h3>
<p>If every hostname on a non-wildcard certificate is <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14107.md")
</div> through Cloudflare and the DCV method is [HTTP](/ssl/edge-certificates/changing-dcv-method/methods/http/), Cloudflare can automatically complete DCV on your behalf.
<p>This applies to customers using <a href="/ssl/edge-certificates/universal-ssl/">Universal</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificates</a>.</p>
<p>If one of the hostnames on the certificate is not proxying traffic through Cloudflare, certificate issuance and renewal will vary based on the type of certificate you are using:</p>
<ul>
<li><strong>Universal</strong>: Perform DCV using one of the available <a href="/ssl/edge-certificates/changing-dcv-method/methods/">methods</a>.</li>
<li><strong>Advanced</strong>: In most cases, you can opt for <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>, which greatly simplifies certificate management.</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/14105.md")
</aside>
<h3 id="wildcard-certificates">Wildcard certificates</h3>
<p>For wildcard hostname certificates, certificate issuance and renewal varies based on the type of certificate you are using:</p>
<ul>
<li><strong>Universal</strong>: Perform DCV using <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT validation method</a>.</li>
<li><strong>Advanced</strong>: In most cases, you can opt for <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>, which greatly simplifies certificate management.</li>
</ul>
<p>If you cannot use Delegated DCV, you need to use <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT based DCV</a> for certificate issuance and renewal. This means you will need to place one TXT DCV token for every hostname on the certificate. If one or more of the hostnames on the certificate fails to validate, the certificate will not be issued or renewed.</p>
<p>This means that a wildcard certificate covering <code>example.com</code> and <code>*.example.com</code> will require two DCV tokens to be placed at the authoritative DNS provider. Similarly, a certificate with five hostnames in the SAN (including a wildcard) will require five DCV tokens to be placed at the authoritative DNS provider.</p>
