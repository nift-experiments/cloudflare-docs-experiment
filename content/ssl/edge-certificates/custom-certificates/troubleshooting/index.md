---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/
  description: Troubleshoot issues with custom certificates.
  full_title: Troubleshooting · Cloudflare SSL/TLS docs
  head_html: <title>Troubleshooting · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot issues with custom certificates."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot issues with custom certificates."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare SSL/TLS docs","description":"Troubleshoot issues with custom certificates.","url":"https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/custom-certificates/troubleshooting/
  schema: 1
---
<h2 id="generic-troubleshooting">Generic troubleshooting</h2>
<h3 id="make-sure-your-key-and-certificate-match">Make sure your key and certificate match</h3>
<p>You can use an external tool such as the <a href="https://www.sslshopper.com/certificate-key-matcher.html">SSLShopper Certificate Key Matcher</a> to check your certificate and make sure the key matches.</p>
<p>Alternatively, use <code>openssl</code> to verify the match by comparing the public key hash of both files. This method works for both RSA and ECDSA certificates:</p>
<pre tabindex="0"><code class="language-bash">openssl x509 -noout -pubkey -in certificate.crt | openssl md5&#10;openssl pkey -pubout -in private.key | openssl md5&#10;</code></pre>
<p>If the two outputs match, the certificate and key are a valid pair.</p>
<h3 id="check-the-certificate-details">Check the certificate details</h3>
<p>You can use <code>openssl</code> to check all the details of your certificate:</p>
<pre tabindex="0"><code class="language-bash">openssl x509 -in certificate.crt -noout -text&#10;</code></pre>
<p>Then, make sure all the information is correct before uploading.</p>
<h3 id="remove-password-from-private-key">Remove password from private key</h3>
<p>Cloudflare does not accept password-protected private keys. If your private key requires a password, remove it before uploading. The following command works for both RSA and ECDSA keys:</p>
<pre tabindex="0"><code class="language-bash">openssl pkey -in protected.key -out unprotected.key&#10;</code></pre>
<p>Use the <code>unprotected.key</code> file when uploading to Cloudflare. For detailed instructions, refer to <a href="/ssl/edge-certificates/custom-certificates/remove-file-key-password/">Remove key file password</a>.</p>
<h3 id="private-key-format-requirements">Private key format requirements</h3>
<p>Private keys must be in one of the following unencrypted formats:</p>
<ul>
<li>PKCS#8</li>
<li>PKCS#1</li>
<li>Elliptic Curve</li>
</ul>
<h2 id="moved-domains">Moved domains</h2>
<p>If you move a domain without deleting the custom certificate from the previous zone, the certificate may still <a href="/ssl/reference/certificate-and-hostname-priority/">take precedence</a> and be presented to your visitors, until the previous zone is <a href="/dns/zone-setups/reference/domain-status/">deleted</a>.</p>
<p>Refer to <a href="/fundamentals/manage-domains/move-domain/#issue-new-certificates">Move a domain between Cloudflare accounts</a> for details.</p>
<h2 id="let-s-encrypt-chain-update">Let's Encrypt chain update</h2>
<p>As Let's Encrypt - one of the <a href="/ssl/reference/certificate-authorities/">certificate authorities (CAs)</a> used by Cloudflare - has announced changes in its <a href="/ssl/concepts/#chain-of-trust">chain of trust</a>, you may face issues.</p>
<p>If you are using a Let's Encrypt certificate uploaded by yourself as a custom certificate, consider the following:</p>
<ul>
<li>If you use <strong>compatible</strong> or <strong>modern</strong> <a href="/ssl/edge-certificates/custom-certificates/bundling-methodologies/">bundle method</a> and have uploaded your certificate before September 9, 2024, <a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">update your custom certificate</a> so that it can be bundled with the new chain.</li>
<li>If you use <strong>user-defined</strong> bundle method, make sure that your certificates uploaded after September 30, 2024, do not use the Let's Encrypt cross-signed chain.</li>
</ul>
<h2 id="error-codes">Error codes</h2>
<h3 id="invalid-certificate-code-1002">Invalid certificate. (Code: 1002)</h3>
<p><strong>Root cause</strong></p>
<p>The certificate you are trying to upload is invalid. For example, there might be extra lines, or the BEGIN/END text is not correct, or extra characters are added following a copy/paste.</p>
<p>In the case of an update with the <a href="/api/resources/custom_certificates/methods/edit/">PATCH API call</a>, it can mean the path parameter <code>{custom_certificate_id}</code> is invalid.</p>
<p><strong>Solution</strong></p>
<p>Carefully check the content of the certificate. You may use <code>openssl</code> to check all the details of your certificate:</p>
<pre tabindex="0"><code class="language-bash">openssl x509 -in certificate.crt -noout -text&#10;</code></pre>
<p>When using the API, carefully check the <code>{custom_certificate_id}</code> path parameter. You can confirm the certificate ID by <a href="/api/resources/custom_certificates/methods/list/">listing the existing custom certificates</a> (<code>id</code> in the response).</p>
<h3 id="you-have-reached-the-maximum-number-of-custom-certificates-code-1212">You have reached the maximum number of custom certificates. (Code: 1212)</h3>
<p><strong>Root cause</strong></p>
<p>You have used up your custom certificate quota.</p>
<p><strong>Solution</strong></p>
<p>If you are renewing an existing certificate, <a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">update the existing certificate</a> instead of uploading a new one. Updating an existing certificate via the dashboard (or the API <code>PATCH</code> method) reuses its quota slot and avoids downtime.</p>
<p>If you genuinely need a new certificate for a different hostname, delete an unused certificate first or contact your account team (Enterprise) to increase your quota.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14087.md")
</aside>
<h3 id="this-certificate-has-already-been-submitted-code-1220">This certificate has already been submitted. (Code: 1220)</h3>
<p><strong>Root cause</strong></p>
<p>You are trying to upload a custom certificate that you have already uploaded.</p>
<p><strong>Solution</strong></p>
<p>If you are renewing the certificate with updated expiry or key material, <a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">update the existing certificate</a> instead of uploading a new one. Updating via the dashboard (or the API <code>PATCH</code> method) avoids downtime and does not consume an additional quota slot.</p>
<h3 id="you-already-have-a-certificate-of-this-signature-type-code-1228">You already have a certificate of this signature type. (Code: 1228)</h3>
<p><strong>Root cause</strong></p>
<p>A custom certificate pack can only have one certificate per signature algorithm (for example, one RSA and one ECDSA certificate).</p>
<p><strong>Solution</strong></p>
<p>Instead of uploading a new certificate, update the existing certificate using the edit option in the dashboard or the <a href="/api/resources/custom_certificates/methods/edit/">PATCH API endpoint</a>.</p>
<h3 id="this-certificate-cannot-be-deleted-at-this-time-code-1305">This certificate cannot be deleted at this time. (Code: 1305)</h3>
<p><strong>Root cause</strong></p>
<p>This error occurs when there is an issue with the certificate pack structure. You must delete other certificates in the pack before deleting this one.</p>
<p><strong>Solution</strong></p>
<p>Delete the other certificates in the certificate pack first, then delete this certificate. If the issue persists, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>.</p>
<h3 id="only-root-ca-certificate-is-allowed-code-1411">Only root CA certificate is allowed. (Code: 1411)</h3>
<p><strong>Root cause</strong></p>
<p>You are trying to upload a certificate to the <a href="/ssl/origin-configuration/origin-ca/#custom-origin-trust-store">custom origin trust store</a>, but the certificate is not a valid root CA certificate.</p>
<p><strong>Solution</strong></p>
<p>When creating a self-signed root CA certificate, ensure you use the <code>-extensions v3_ca</code> option with OpenSSL. Refer to <a href="https://community.cloudflare.com/t/only-root-ca-certificate-is-allowed-code-1411/505318">this community post</a> for more details.</p>
<h3 id="the-ssl-attribute-is-invalid-please-refer-to-the-api-documentation-check-your-input-and-try-again-code-1434">The SSL attribute is invalid. Please refer to the API documentation, check your input and try again. (Code: 1434)</h3>
<p><strong>Root cause</strong></p>
<p>You are trying to upload a custom certificate that does not support any cipher that is needed by Chromium-based browsers.</p>
<p><strong>Solution</strong></p>
<p>Modify the certificate so that it supports chromium-supported ciphers and try again.</p>
<h3 id="you-have-reached-your-quota-for-the-requested-resource-code-2005">You have reached your quota for the requested resource. (Code: 2005)</h3>
<p><strong>Root cause</strong></p>
<p>The quota for custom certificates depends on the <strong>type</strong> of certificate (<strong>Custom Legacy</strong> vs <strong>Custom Modern</strong>).</p>
<p>If you try to upload a certificate <strong>type</strong> but have already reached your quota, you will receive this error.</p>
<p><strong>Solution</strong></p>
<p>First, check your custom certificate entitlements on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page.</p>
<p>Then, when actually uploading or editing the certificate, make sure you select the appropriate option for <strong>Legacy Client Support</strong>.</p>
<h3 id="the-certificate-chain-you-uploaded-cannot-be-bundled-using-cloudflare-s-trust-store-please-check-your-input-and-try-again-code-2100">The certificate chain you uploaded cannot be bundled using Cloudflare's trust store. Please check your input and try again. (Code: 2100)</h3>
<p><strong>Root cause</strong></p>
<p>You are trying to upload a custom certificate that contains the root and leaf certificate at the same time.</p>
<p><strong>Solution</strong></p>
<p>Upload the leaf certificate only.</p>
<h3 id="the-certificate-chain-you-uploaded-has-no-leaf-certificates-please-check-your-input-and-try-again-code-2101">The certificate chain you uploaded has no leaf certificates. Please check your input and try again. (Code: 2101)</h3>
<p><strong>Root cause</strong></p>
<p>You are trying to upload a root + intermediate + intermediate <code>.crt</code> file, but the actual leaf certificate is in a separate file.</p>
<p><strong>Solution</strong></p>
<p>Add the leaf to the <code>.crt</code> file, or just use the leaf by itself since the Certificate Authority has a public chain of trust in our trust store.</p>
<h3 id="the-certificate-chain-you-uploaded-does-not-include-any-hostnames-from-your-zone-please-check-your-input-and-try-again-code-2103">The certificate chain you uploaded does not include any hostnames from your zone. Please check your input and try again. (Code: 2103)</h3>
<p><strong>Root cause</strong></p>
<p>Cloudflare verifies that uploaded custom certificates include a hostname for the associated zone. Moreover, this hostname must be included as a Subject Alternative Name (SAN). This is following the standard set by the <a href="https://cabforum.org/wp-content/uploads/BRv1.2.5.pdf#page=16">CA/Browser Forum</a>.</p>
<p><strong>Solution</strong></p>
<p>Make sure your certificate contains a Subject Alternative Name (SAN) specifying a hostname in your zone. You can use the <code>openssl</code> command below and look for <code>Subject Alternative Name</code> in the output.</p>
<pre tabindex="0"><code class="language-bash">openssl x509 -in certificateFile.pem -noout -text&#10;</code></pre>
<p>If it does not exist, you will need to request a new certificate.</p>
<h3 id="the-private-key-you-uploaded-is-invalid-please-check-your-input-and-try-again-code-2106">The private key you uploaded is invalid. Please check your input and try again. (Code: 2106)</h3>
<p><strong>Root cause</strong></p>
<p>Cloudflare requires separate, pem-encoded files for the SSL private key and certificate.</p>
<p><strong>Solution</strong></p>
<p>Contact your Certificate Authority (CA) to confirm whether your current certificate meets this requirement or request your CA to assist with certificate format conversion.</p>
<p>Make sure your certificate complies with these <a href="/ssl/edge-certificates/custom-certificates/uploading/#certificate-requirements">requirements</a>.</p>
<p>Check that the certificate and private keys match before uploading the certificate in the Cloudflare dashboard. This <a href="https://www.sslshopper.com/article-most-common-openssl-commands.html">external resource</a> might help.</p>
<h3 id="the-certificate-and-private-key-pair-you-uploaded-is-invalid-code-2200">The certificate and private key pair you uploaded is invalid. (Code: 2200)</h3>
<p><strong>Root cause</strong></p>
<p>The certificate and private key you uploaded do not form a valid pair. The private key does not correspond to the public key in the certificate. This can happen when the wrong key file is selected during upload.</p>
<p><strong>Solution</strong></p>
<p>Ensure the private key corresponds to the certificate you are uploading. You can verify this by comparing the public key hash of both files. This method works for both RSA and ECDSA certificates:</p>
<pre tabindex="0"><code class="language-bash">openssl x509 -noout -pubkey -in certificate.crt | openssl md5&#10;openssl pkey -pubout -in private.key | openssl md5&#10;</code></pre>
<p>If the outputs do not match, you have mismatched the certificate and key.</p>
<h3 id="an-unknown-error-has-occurred-code-2000">An unknown error has occurred. (Code: 2000)</h3>
<p><strong>Root cause</strong></p>
<p>An internal error occurred while processing your request.</p>
<p><strong>Solution</strong></p>
<p>Wait a few minutes and try again. If the issue persists, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> with a <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">HAR file</a> capturing the failed upload attempt.</p>
