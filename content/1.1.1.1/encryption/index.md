<p>When you visit a website, your device first sends a DNS query to translate the domain name (for example, <code>example.com</code>) into an IP address. Traditionally, these queries are sent in plaintext — unencrypted and readable by anyone on the network path.</p>
<p>Unencrypted DNS queries can be monitored, modified, or used for tracking by ISPs, network operators, or malicious actors.</p>
<p>To protect your DNS traffic, 1.1.1.1 supports three encryption standards:</p>
<ul>
<li><a href="/1.1.1.1/encryption/dns-over-tls/">DNS over TLS (DoT)</a> — Encrypts DNS queries over a dedicated TLS connection on port <code>853</code>.</li>
<li><a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS (DoH)</a> — Encrypts DNS queries inside regular HTTPS traffic on port <code>443</code>.</li>
<li><a href="/1.1.1.1/encryption/oblivious-dns-over-https/">Oblivious DNS over HTTPS (ODoH)</a> — Adds a privacy layer to DoH so that no single entity can see both your identity and your query.</li>
</ul>
<p>You can also <a href="/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/">configure your browser</a> to secure your DNS queries.</p>
<p>To secure connections on your smartphone, refer to the 1.1.1.1 <a href="/1.1.1.1/setup/ios/">iOS</a> or <a href="/1.1.1.1/setup/android/">Android</a> apps.</p>
