<p>Standard DNS has no built-in way to verify that a response actually came from the authoritative server for a domain. An attacker could return a forged answer, and a resolver would have no way to detect it.</p>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/">DNSSEC</a> solves this by adding cryptographic signatures to DNS records. Domain owners sign their DNS records with a private key, and resolvers like 1.1.1.1 verify those signatures using the corresponding public key. This proves the response is authentic and has not been modified in transit.</p>
<p>DNSSEC uses two DNS record types to distribute the public keys needed for verification:</p>
<ul>
<li><strong>DNSKEY</strong> records contain the public signing keys for a domain.</li>
<li><strong>DS</strong> (Delegation Signer) records link a child zone's keys to its parent zone, creating a chain of trust.</li>
</ul>
<p>Resolvers use these keys to verify the signatures stored in <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">RRSIG records</a>.</p>
<h2 id="supported-signature-algorithms">Supported signature algorithms</h2>
<p>1.1.1.1 supports the following DNSSEC signature algorithms:</p>
<ul>
<li>RSA/SHA-1</li>
<li>RSA/SHA-256</li>
<li>RSA/SHA-512</li>
<li>RSASHA1-NSEC3-SHA1</li>
<li>ECDSA Curve P-256 with SHA-256 (ECDSAP256SHA256)</li>
<li>ECDSA Curve P-384 with SHA-384 (ECDSAP384SHA384)</li>
<li>ED25519</li>
</ul>
