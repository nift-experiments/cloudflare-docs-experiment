<p>If your customers need to provide their own key material, you may want to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/">upload a custom certificate</a>. Cloudflare will automatically bundle the certificate with a certificate chain <a href="/ssl/edge-certificates/custom-certificates/bundling-methodologies/#compatible">optimized for maximum browser compatibility</a>.</p>
<p>As part of this process, you may also want to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/certificate-signing-requests/">generate a Certificate Signing Request (CSR)</a> for your customer so they do not have to manage the private key on their own.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4152.md")
</aside>
<h2 id="use-cases">Use cases</h2>
<p>This situation commonly occurs when your customers use Extended Validation (EV) certificates (the “green bar”) or when their information security policy prohibits third parties from generating private keys on their behalf.</p>
<h2 id="limitations">Limitations</h2>
<p>If you use custom certificates, you are responsible for the entire certificate lifecycle (initial upload, renewal, subsequent upload).</p>
<p>Cloudflare also only accepts publicly trusted certificates of these types:</p>
<ul>
<li><code>SHA256WithRSA</code></li>
<li><code>SHA1WithRSA</code></li>
<li><code>ECDSAWithSHA256</code></li>
</ul>
<p>If you attempt to upload another type of certificate or a certificate that has been self-signed, it will be rejected.</p>
