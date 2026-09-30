---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/
  description: Troubleshoot HTTP 526 error responses.
  full_title: Error 526 · Cloudflare Support docs
  head_html: <title>Error 526 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 526 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/index.md"><meta property="og:title" content="Error 526 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 526 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#page","headline":"Error 526 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 526 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/
  schema: 1
---
<h2 id="error-526-invalid-ssl-certificate">Error 526: invalid SSL certificate</h2>
<p>This error indicates that Cloudflare is unable to verify the SSL certificate on your origin server, preventing a secure connection from being established.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when these two conditions are true:</p>
<ul>
<li>Cloudflare cannot validate the SSL certificate at your origin web server.</li>
<li><a href="/ssl/origin-configuration/ssl-modes/full-strict/"><em>Full SSL (Strict)</em></a> <strong>SSL</strong> is set in the <strong>Overview</strong> tab of your Cloudflare <strong>SSL/TLS</strong> app.</li>
</ul>
<h4 id="resolution">Resolution</h4>
<p>Here are some options to fix or workaround this issue:</p>
<ul>
<li>
<p>For a potential quick fix, set <strong>SSL</strong> to <em>Full</em> instead of <em>Full (strict)</em> in the <strong>Overview</strong> tab of your Cloudflare <strong>SSL/TLS</strong> app for the domain.</p>
</li>
<li>
<p>Add your self-signed SSL certificate to the <a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a>. This allows the Cloudflare edge to recognize your self-signed SSL certificate as valid.</p>
</li>
<li>
<p>Use a <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificate</a> at your origin.</p>
</li>
<li>
<p>Request your server administrator or hosting provider to review the origin web server's SSL certificates and verify that:</p>
<ul>
<li>Certificate is not expired.</li>
<li>Certificate is not revoked.</li>
<li>Certificate is signed by a <a href="https://en.wikipedia.org/wiki/Certificate_authority">Certificate Authority</a> (not self-signed).</li>
<li>The requested or target domain name and hostname are in the certificate's <strong>Common Name</strong> or <strong>Subject Alternative Name</strong>.</li>
<li>The certificate chain is complete - the origin server must serve the leaf certificate along with any required intermediate CA certificates so that Cloudflare can build a trusted chain to a root CA.</li>
<li>Your origin web server accepts connections over port SSL port <code>443</code>.</li>
<li><a href="/fundamentals/manage-domains/pause-cloudflare/">Temporarily pause Cloudflare</a> and visit <a href="https://www.sslshopper.com/ssl-checker.html#hostname=www.example.com">https://www.sslshopper.com/ssl-checker.html#hostname=www.example.com</a> (replace <code>www.example.com</code> with your hostname and domain) to verify no issues exists with the origin SSL certificate:</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/support/hc-import-troubleshooting_5xx_errors_sslshopper_output.png" alt="Screen showing an SSL certificate with no errors." /></p>
<h3 id="error-526-in-the-zero-trust-context">Error 526 in the Zero Trust context</h3>
<p>When using <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, an HTTP Error <code>526</code> might be returned in the <a href="/cloudflare-one/traffic-policies/troubleshooting/#error-526-invalid-ssl-certificate">following cases</a>:</p>
<ul>
<li>
<p><strong>An untrusted certificate is presented from the origin to Gateway.</strong> Gateway will consider a certificate is untrusted if any of these conditions are true:</p>
<ul>
<li>The server certificate issuer is unknown or is not trusted by the service.</li>
<li>The server certificate is revoked and fails a CRL check.</li>
<li>There is at least one expired certificate in the certificate chain for the server certificate.</li>
<li>The common name on the certificate does not match the URL you are trying to reach.</li>
<li>The common name on the certificate contains invalid characters (such as underscores). Gateway uses <a href="https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Basic&amp;Vendor=Google&amp;CertificateStatus=Active&amp;ValidationYear=0">BoringSSL</a> to validate certificates. Chrome's <a href="https://chromium.googlesource.com/chromium/src/+/refs/heads/main/net/cert/x509_certificate.cc#429">validation logic</a> allows non-RFC 1305 compliant certificates, which is why the website may load when you turn off WARP.</li>
</ul>
</li>
<li>
<p><strong>The connection from Gateway to the origin is insecure.</strong> Gateway does not trust origins which:</p>
<ul>
<li>Only offer insecure cipher suites (such as RC4, RC4-MD5, or 3DES). You can use the <a href="https://www.ssllabs.com/ssltest/index.html">SSL Server Test tool</a> to check which ciphers are supported by the origin.</li>
<li>Do not support <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#cipher-suites">FIPS-compliant ciphers</a> (if you have enabled <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#fips-compliance">FIPS compliance mode</a>). In order to load the page, you can either disable FIPS mode or create a Do Not Inspect policy for this host (which has the effect of disabling FIPS compliance for this origin).</li>
<li>Redirect all HTTPS requests to HTTP.</li>
</ul>
</li>
</ul>
<h3 id="error-526-in-the-workers-context">Error 526 in the Workers context</h3>
<p>Workers subrequests to any hostname outside your Cloudflare zone that is not proxied by Cloudflare are always made using the <strong><a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict)</a></strong> SSL mode, regardless of the Workers zone configuration.</p>
<h4 id="resolution-1">Resolution</h4>
<ul>
<li>
<p>Make sure the SSL certificate configured at the origin is valid.</p>
</li>
<li>
<p>Add your self-signed SSL certificate to the <a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> and enable the <a href="/workers/configuration/compatibility-flags/#do-not-use-the-custom-origin-trust-store-for-external-subrequests"><code>cots_on_external_fetch</code> compatibility flag</a> in your Worker's configuration.
This flag enables the use of the <a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> when making external (grey-clouded) subrequests from a Cloudflare Worker.</p>
</li>
</ul>
