<p>This page details the data security properties of R2, including encryption-at-rest (EAR), encryption-in-transit (EIT), and Cloudflare's compliance certifications.</p>
<h2 id="encryption-at-rest">Encryption at Rest</h2>
<p>All objects stored in R2, including their metadata, are encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of R2.</p>
<p>Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.</p>
<p>Objects are encrypted using <a href="https://www.cloudflare.com/learning/ssl/what-is-encryption/">AES-256</a>, a widely tested, highly performant and industry-standard encryption algorithm. R2 uses GCM (Galois/Counter Mode) as its preferred mode.</p>
<h2 id="encryption-in-transit">Encryption in Transit</h2>
<p>Data transfer between a client and R2 is secured using the same <a href="https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/">Transport Layer Security</a> (TLS/SSL) supported on all Cloudflare domains.</p>
<p>Access over plaintext HTTP (without TLS/SSL) can be disabled by connecting a <a href="/r2/buckets/public-buckets/#custom-domains">custom domain</a> to your R2 bucket and enabling <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11369.md")
</aside>
<h2 id="compliance">Compliance</h2>
<p>To learn more about Cloudflare's adherence to industry-standard security compliance certifications, visit the Cloudflare <a href="https://www.cloudflare.com/trust-hub/compliance-resources/">Trust Hub</a>.</p>
