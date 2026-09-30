<p>For publicly trusted certificates, Cloudflare partners with different certificate authorities (CAs). Refer to this page to check what CAs are used for each Cloudflare offering and for more details about the CAs <a href="#features-limitations-and-browser-compatibility">features, limitations, and browser compatibility</a>.</p>
<h2 id="availability-per-certificate-type-and-encryption-algorithm">Availability per certificate type and encryption algorithm</h2>
<table>
<thead>
<tr>
<th>Certificate</th>
<th>Algorithm</th>
<th><a href="#lets-encrypt">Let's Encrypt</a></th>
<th><a href="#google-trust-services">Google Trust Services</a></th>
<th><a href="#sslcom">SSL.com</a></th>
<th><a href="#sectigo">Sectigo</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ssl/edge-certificates/universal-ssl/">Universal</a></td>
<td>ECDSA<br /><br /><br />RSA<br /><sub>(Paid plans only)</sub></td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /><br />✅</td>
<td>N/A<br /><br /><br />N/A</td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced</a></td>
<td>ECDSA<br /><br /><br />RSA</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /> <br /> ✅<br /><br /></td>
<td>N/A<br /><br /><br />N/A</td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a></td>
<td>ECDSA<br /><br /><br />RSA</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /> <br /> ✅<br /><br /></td>
<td>N/A<br /><br /><br />N/A</td>
</tr>
<tr>
<td><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">SSL for SaaS</a></td>
<td>ECDSA<br /><br /><br />RSA</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /><br />✅</td>
<td>✅<br /><br /> <br /> ✅<br /><br /></td>
<td>N/A<br /><br /><br />N/A</td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/backup-certificates/">Backup</a></td>
<td>ECDSA<br /><br />RSA</td>
<td>✅<br /><br />✅</td>
<td>✅<br /><br />✅</td>
<td>✅<br /><br />✅</td>
<td>✅<br /><br />✅</td>
</tr>
</tbody>
</table>
<h2 id="features-limitations-and-browser-compatibility">Features, limitations, and browser compatibility</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="universal-ssl">Universal SSL</h3>
@markup("md", "content/.markup/bodies/13983.md")
</aside>
<hr />
<h3 id="let-s-encrypt">Let's Encrypt</h3>
<ul>
<li>Supports <a href="/ssl/reference/certificate-validity-periods/">validity periods</a> of 90 days.</li>
<li><a href="/ssl/edge-certificates/changing-dcv-method/">DCV tokens</a> are valid for 7 days.</li>
</ul>
<h4 id="limitations">Limitations</h4>
<ul>
<li>Hostname on certificate can contain up to 10 levels of subdomains.</li>
<li>Duplicate certificate limit of <a href="https://letsencrypt.org/docs/rate-limits/">5 certificates</a> per week.</li>
<li>Redsys<sup><a href="#footnote-1">1</a></sup> is not compatible with Let's Encrypt certificates. If you use Redsys and find issues with Let's Encrypt certificates, order an advanced certificate or upload a custom certificate to use a different CA.</li>
</ul>
<h4 id="browser-compatibility">Browser compatibility</h4>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/13982.md")
</aside>
<p>The main determining factor for whether a platform can validate Let's Encrypt certificates is whether that platform trusts the self-signed ISRG Root X1 certificate. As Let's Encrypt announced a <a href="https://blog.cloudflare.com/shortening-lets-encrypt-change-of-trust-no-impact-to-cloudflare-customers/">change in its chain of trust in 2024</a>, older devices (for example Android 7.0 and earlier) that only trust the cross-signed version of the ISRG Root X1 are no longer compatible.</p>
<p>You can find the full list of supported clients in the <a href="https://letsencrypt.org/docs/certificate-compatibility/">Let's Encrypt documentation</a>. Older versions of Android and Java clients might not be compatible with Let's Encrypt certificates.</p>
<h4 id="other-resources">Other resources</h4>
<p><a href="https://letsencrypt.org/certificates/">Let's Encrypt Root CAs</a>: For checking compatibility between chain and client. As explained in <a href="/ssl/reference/certificate-pinning/">Certificate pinning</a>, you should <strong>not</strong> use this list for pinning against.</p>
<hr />
<h3 id="google-trust-services">Google Trust Services</h3>
<ul>
<li>Supports <a href="/ssl/reference/certificate-validity-periods/">validity periods</a> of 14, 30, and 90 days.</li>
<li><a href="/ssl/edge-certificates/changing-dcv-method/">DCV tokens</a> are valid for 14 days.</li>
</ul>
<h4 id="browser-compatibility-most-compatible">Browser compatibility (most compatible)</h4>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-1">Warning</h3>
@markup("md", "content/.markup/bodies/13981.md")
</aside>
<p>By cross-signing with a <a href="https://valid.r1.roots.globalsign.com/">GlobalSign root CA</a> that has been installed in client devices for more than 20 years, Google Trust Services can ensure optimal support across a wide range of devices.</p>
<p>Currently trusted by Microsoft, Mozilla, Safari, Cisco, Oracle Java, and Qihoo’s 360 browser, all browsers or operating systems that depend on these root programs are covered.</p>
<p>You can use the <a href="https://pki.goog/faq/#connecting-to-google">root CAs list</a> for checking compatibility between chain and client but, as explained in <a href="/ssl/reference/certificate-pinning/">Certificate pinning</a>, you should <strong>not</strong> use this list for pinning against.</p>
<hr />
<h3 id="ssl-com">SSL.com</h3>
<ul>
<li>Supports <a href="/ssl/reference/certificate-validity-periods/">validity periods</a> of 14, 30, and 90 days. Enterprise customers using <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a> can also choose a validity period of one year.</li>
<li><a href="/ssl/edge-certificates/changing-dcv-method/">DCV tokens</a> are valid for 14 days.</li>
</ul>
<h4 id="limitations-1">Limitations</h4>
<p>SSL.com DCV tokens are specific for RSA certificates and ECDSA certificates. This means that, for cases where you have to <a href="/ssl/edge-certificates/changing-dcv-method/#partial-dns-setup---action-sometimes-required">manually perform DCV</a>, you will have to place two validation tokens per certificate order. To avoid management overhead, consider using a <a href="/ssl/edge-certificates/changing-dcv-method/#full-dns-setup---no-action-required">full setup</a>, or setting up <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>.</p>
<h4 id="browser-compatibility-1">Browser compatibility</h4>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-2">Warning</h3>
@markup("md", "content/.markup/bodies/13980.md")
</aside>
<p>SSL.com is highly compatible, being accepted by over 99.9% of browsers, tablets, and mobile devices.</p>
<p>SSL.com certificates are <a href="https://www.ssl.com/repository/">cross-signed with Certum</a> and the <a href="https://crt.sh/?caid=840">CA that cross-signs intermediates</a> is from 2004.</p>
<h4 id="other-resources-1">Other resources</h4>
<p><a href="https://www.ssl.com/acceptable-top-level-domains-tlds-for-ssl-certificates/">Acceptable top level domains (TLDs) and current restrictions</a></p>
<hr />
<h3 id="sectigo">Sectigo</h3>
<ul>
<li>Only used for <a href="/ssl/edge-certificates/backup-certificates/">Backup certificates</a>.</li>
<li>Backup certificates are valid for 90 days.</li>
</ul>
<h4 id="browser-compatibility-2">Browser compatibility</h4>
<p>Refer to <a href="https://www.sectigo.com/resource-library/sectigo-certificate-authority-root-keys">Sectigo documentation</a>.</p>
<hr />
<h2 id="caa-records">CAA records</h2>
<p>A Certificate Authority Authorization (CAA) DNS record specifies which certificate authorities (CAs) are allowed to issue certificates for a domain. This record reduces the chance of unauthorized certificate issuance and promotes standardization across your organization.
<br /></p>
<p>If you are using Cloudflare as your DNS provider, then the CAA records will be added on your behalf. If you need to add CAA records, refer to <a href="/ssl/edge-certificates/caa-records/">Add CAA records</a>.</p>
<p>The following table lists the CAA record content for each CA:</p>
<table>
<thead>
<tr>
<th>Certificate authority</th>
<th>CAA record content</th>
</tr>
</thead>
<tbody>
<tr>
<td>Let's Encrypt</td>
<td><code>letsencrypt.org</code></td>
</tr>
<tr>
<td>Google Trust Services</td>
<td><code>pki.goog; cansignhttpexchanges=yes</code></td>
</tr>
<tr>
<td>SSL.com</td>
<td><code>ssl.com</code></td>
</tr>
<tr>
<td>Sectigo</td>
<td><code>sectigo.com</code></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A payment gateway used with some ecommerce plugins.</li></ol></section>
