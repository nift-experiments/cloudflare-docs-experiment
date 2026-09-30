<p>Learn how to manage custom certificates for your Cloudflare for SaaS custom hostnames. For use cases and limitations, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/">custom certificates</a>.</p>
<h2 id="upload-certificates">Upload certificates</h2>
<p>This section describes the general process for uploading a custom certificate corresponding to one of the <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/#limitations">supported types</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4148.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4151.md")
</div></div>
<h2 id="use-certificate-packs-rsa-and-ecdsa">Use certificate packs: RSA and ECDSA</h2>
<p>A certificate pack allows you to upload up to one RSA and one ECDSA custom certificates to a custom hostname. This process is currently only supported via API.</p>
<p>To upload an RSA and ECDSA certificate to a custom hostname, set the <code>bundle_method</code> to <code>force</code> and define the <code>custom_cert_bundle</code> property when <a href="/api/resources/custom_hostnames/methods/create/">creating a custom hostname via API</a>.</p>
<p>You can also use <code>&quot;bundle_method&quot;: &quot;force&quot;</code> and <code>custom_cert_bundle</code> with a <code>PATCH</code> request to the <a href="/api/resources/custom_hostnames/methods/edit/">Edit Custom Hostname</a> endpoint.</p>
<h3 id="delete-a-custom-certificate-and-private-key">Delete a custom certificate and private key</h3>
<p>Use the <a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/">Delete Single Certificate And Key For Custom Hostname</a> endpoint to remove one of the custom certificates and corresponding key from a certificate pack.</p>
<p>You cannot delete a certificate if it is the only remaining certificate in the pack.</p>
<h3 id="replace-a-custom-certificate-and-private-key">Replace a custom certificate and private key</h3>
<p>To replace a single custom certificate within a certificate pack that contains two bundled certificates, use the <a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/">Replace Custom Certificate And Custom Key In Custom Hostname</a> endpoint.</p>
<p>You can only replace an RSA certificate with another RSA certificate, or an ECDSA certificate with another ECDSA certificate.</p>
<hr />
<h2 id="move-to-a-cloudflare-certificate">Move to a Cloudflare certificate</h2>
<p>If you want to switch from maintaining a custom certificate to using one issued by Cloudflare, you can migrate that certificate with zero downtime.</p>
<p>Send a <a href="/api/resources/custom_hostnames/methods/edit/"><code>PATCH</code> request</a> to your custom hostname with a value for the DCV <code>method</code>. As soon as the <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">certificate is validated</a> and the <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">hostname is validated</a>, Cloudflare will remove the old custom certificate and begin serving the new one.</p>
