<p>Cloudflare offers a range of SSL/TLS options. By default, Cloudflare offers Universal SSL to all domains, but there are many other options available. Cloudflare offers SSL/TLS for free because we believe it is the <a href="https://blog.cloudflare.com/introducing-universal-ssl">right thing to do</a>. Encryption is foundational to the Internet because it prevents data from being manipulated.</p>
<ol>
<li>
<p><a href="/ssl/edge-certificates/universal-ssl/"><strong>Universal SSL</strong></a>: This option covers basic encryption requirements and certificate management needs.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/additional-options/total-tls/"><strong>Total TLS</strong></a>: Automatically issues certificates for all subdomain levels, extending the protection offered by Universal SSL.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/advanced-certificate-manager/"><strong>Advanced Certificates</strong></a>: Offers customizable certificate issuance and management, including options like choosing the certificate authority, certificate validity period, and removing Cloudflare branding from certificates.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/custom-certificates/"><strong>Custom Certificates</strong></a>: For eligible plans, customers can upload their own certificates, with the user managing issuance and renewal.</p>
</li>
<li>
<p><a href="/ssl/client-certificates/"><strong>mTLS Client Certificates</strong></a>: Cloudflare offers a PKI system, used to create client certificates, which can enforce mutual Transport Layer Security (mTLS) encryption.</p>
</li>
<li>
<p><a href="/cloudflare-for-platforms/cloudflare-for-saas/"><strong>Cloudflare for SaaS Custom Hostnames</strong></a>: This feature enables SaaS providers to offer their clients the ability to use their own domains while benefiting from Cloudflare's network.</p>
</li>
<li>
<p><a href="/ssl/keyless-ssl/"><strong>Keyless SSL Certificates</strong></a>: Keyless SSL allows security-conscious clients to upload their own custom certificates and benefit from Cloudflare, but without exposing their TLS private keys.</p>
</li>
<li>
<p><a href="/ssl/origin-configuration/origin-ca/"><strong>Origin Certificates</strong></a>: Origin CA certificates from Cloudflare are used to encrypt traffic between Cloudflare and your origin web server. These certificates are created through the Cloudflare dashboard and can be configured with a choice of RSA or ECC private keys and support for various server types.</p>
</li>
</ol>
