<p>Consider the following common issues and troubleshooting steps when using <a href="/ssl/origin-configuration/origin-ca/">Cloudflare origin CA</a>.</p>
<h2 id="net-err-cert-authority-invalid">NET::ERR_CERT_AUTHORITY_INVALID</h2>
<h3 id="cause">Cause</h3>
<p>Site visitors may see untrusted certificate errors if you <a href="/fundamentals/manage-domains/pause-cloudflare/">pause Cloudflare</a> or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14271.md")
</div> on subdomains that use Cloudflare origin CA certificates. These certificates only encrypt traffic between Cloudflare and your origin server, not traffic from client browsers to your origin.
<p>This also means that SSL Labs or similar SSL validators are expected to flag the certificate as invalid.</p>
<h3 id="solutions">Solutions</h3>
<ul>
<li>Make sure the <a href="/dns/proxy-status/">proxy status</a> of your DNS records and any <a href="/rules/page-rules/">page rules</a> (if existing) are set up correctly. If so, you can try to turn proxying off and then on again and wait a few minutes.</li>
<li>If you must have direct connections between clients and your origin server, consider installing a publicly trusted certificate at your origin instead. This process is done outside of Cloudflare, where you should issue the certificate directly from a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/14272.md")
</div> of your choice. You can still use Full (strict) [encryption mode](/ssl/origin-configuration/ssl-modes/), as long as the CA is listed on the [Cloudflare trust store](https://github.com/cloudflare/cfssl_trust).
<h2 id="the-issuer-of-this-certificate-could-not-be-found">The issuer of this certificate could not be found</h2>
<h3 id="cause-1">Cause</h3>
<p>Some origin web servers require that you upload the Cloudflare origin CA root certificate or certificate chain.</p>
<h3 id="solution">Solution</h3>
<p>Use the following links to download either an ECC or an RSA version and upload to your origin web server:</p>
<ul>
<li><a href="/ssl/static/origin_ca_ecc_root.pem">Cloudflare Origin ECC PEM</a> (do not use with Apache cPanel)</li>
<li><a href="/ssl/static/origin_ca_rsa_root.pem">Cloudflare Origin RSA PEM</a></li>
</ul>
<h2 id="the-certificate-is-not-trusted-in-all-web-browsers">The certificate is not trusted in all web browsers</h2>
<h3 id="cause-2">Cause</h3>
<p>Apache cPanel requires that you upload the Cloudflare origin CA root certificate or certificate chain.</p>
<h3 id="solution-1">Solution</h3>
<p>Use the following link to download an RSA version of the root certificate and upload it to your origin web server:</p>
<ul>
<li><a href="/ssl/static/origin_ca_rsa_root.pem">Cloudflare Origin RSA PEM</a></li>
</ul>
<h2 id="this-zone-is-either-not-part-of-your-account-or-you-do-not-have-access-to-it">This zone is either not part of your account, or you do not have access to it</h2>
<p>When trying to generate an Origin CA on the dashboard, you find the error <code>Failed to validate requested hostname &lt;hostname&gt;: This zone is either not part of your account, or you do not have access to it</code>.</p>
<h3 id="cause-3">Cause</h3>
<p>This is a known issue where, whilst being created on the Cloudflare dashboard, Origin CA requires API access for the user creating the origin certificate.
If the user does not have <strong>API Access</strong>, this error is returned.</p>
<h3 id="solution-2">Solution</h3>
<p>Make sure that the user creating the certificate has access to the API. You can check in the account <strong>Members</strong> page.</p>
<div class="nb-dash-button"></div>
<ul>
<li>The default setting for the account is specified in the card <strong>Enable API Access</strong>.</li>
<li>Specific user API Access (which can override the default setting) is presented after selecting the user in the list of members.</li>
</ul>
