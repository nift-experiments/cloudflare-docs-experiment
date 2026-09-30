<p>This page details the data security properties of D1, including:</p>
<ul>
<li>Encryption-at-rest (EAR).</li>
<li>Encryption-in-transit (EIT).</li>
<li>Cloudflare's compliance certifications.</li>
</ul>
<h2 id="encryption-at-rest">Encryption at Rest</h2>
<p>All objects stored in D1, including metadata, live databases, and inactive databases are encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of D1.</p>
<p>Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.</p>
<p>Objects are encrypted using <a href="https://www.cloudflare.com/learning/ssl/what-is-encryption/">AES-256</a>, a widely tested, highly performant and industry-standard encryption algorithm. D1 uses GCM (Galois/Counter Mode) as its preferred mode.</p>
<h2 id="encryption-in-transit">Encryption in Transit</h2>
<p>Data transfer between a Cloudflare Worker, and/or between nodes within the Cloudflare network and D1 is secured using the same <a href="https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/">Transport Layer Security</a> (TLS/SSL).</p>
<p>API access via the HTTP API or using the <a href="/workers/wrangler/install-and-update/">wrangler</a> command-line interface is also over TLS/SSL (HTTPS).</p>
<h2 id="compliance">Compliance</h2>
<p>To learn more about Cloudflare's adherence to industry-standard security compliance certifications, visit the Cloudflare <a href="https://www.cloudflare.com/trust-hub/compliance-resources/">Trust Hub</a>.</p>
