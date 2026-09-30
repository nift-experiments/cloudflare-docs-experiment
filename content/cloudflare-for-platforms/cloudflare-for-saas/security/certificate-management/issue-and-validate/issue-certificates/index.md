<p>Cloudflare automatically issues certificates when you <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/">create a custom hostname</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4146.md")
</aside>
<h2 id="certificate-authorities">Certificate authorities</h2>
<p>If you create the custom hostname via API, you can leave the <code>certificate_authority</code> parameter empty to set it to “default CA”. With this option, Cloudflare checks the CAA records before requesting the certificates, which helps ensure the certificates can be issued from the CA.</p>
<p>Refer to <a href="/ssl/reference/certificate-authorities/">this certificate authorities reference page</a> to learn more about the CAs that Cloudflare uses to issue SSL/TLS certificates.</p>
<h2 id="certificate-details-and-compatibility">Certificate details and compatibility</h2>
<p>For each custom hostname, Cloudflare issues two certificates bundled in chains that maximize browser compatibility (unless you <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/">upload custom certificates</a>).</p>
<p>The primary certificate uses a <code>P-256</code> key, is <code>SHA-2/ECDSA</code> signed, and will be presented to browsers that support elliptic curve cryptography (ECC). The secondary or fallback certificate uses an <code>RSA 2048-bit</code> key, is <code>SHA-2/RSA</code> signed, and will be presented to browsers that do not support ECC.</p>
