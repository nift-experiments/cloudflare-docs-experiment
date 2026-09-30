<p>With standard <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS (DoH)</a>, your DNS queries are encrypted, but the resolver still sees both your IP address and the domain you are looking up. Oblivious DNS over HTTPS (ODoH) adds a privacy layer so that no single entity can see both pieces of information at the same time.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1815.md")
</aside>
<h2 id="how-odoh-works">How ODoH works</h2>
<p>ODoH introduces two roles between your device and the DNS resolver:</p>
<ul>
<li><strong>Proxy</strong> — Forwards your encrypted DNS query to the target. The proxy can see your IP address but cannot read the query because it is encrypted.</li>
<li><strong>Target</strong> — Receives and decrypts the DNS query, then sends it to the upstream resolver. The target can read the query but only sees the proxy's IP address, not yours.</li>
</ul>
<p>Because the query is encrypted before it reaches the proxy, and the target never learns your IP address:</p>
<ul>
<li>The proxy has no visibility into the DNS messages, with no ability to identify, read, or modify either the query being sent by the client or the answer being returned by the target.</li>
<li>The target only has access to the encrypted query and the proxy's IP address, while not having visibility over the client's IP address.</li>
<li>Only the intended target can read the content of the query and produce a response, which is also encrypted.</li>
</ul>
<p>This means that, as long as the proxy and the target do not collude, no single entity can have access to both the DNS messages and the client IP address at the same time. Clients are in complete control of proxy and target selection, so you can choose a proxy and target operated by different organizations to reduce collusion risk.</p>
<p>Clients encrypt their query for the target using Hybrid Public Key Encryption (<a href="https://blog.cloudflare.com/hybrid-public-key-encryption/">HPKE</a>), a standard for encrypting messages to a recipient using their public key. A target's public key is obtained via DNS, where it is bundled into an HTTPS resource record and protected by DNSSEC.</p>
<h2 id="cloudflare-and-third-party-products">Cloudflare and third-party products</h2>
<p>Cloudflare 1.1.1.1 supports ODoH by acting as a target that can be reached at <code>odoh.cloudflare-dns.com</code>.</p>
<p>To make ODoH queries you can use open source clients such as <a href="https://github.com/DNSCrypt/dnscrypt-proxy">dnscrypt-proxy</a>.</p>
<p><a href="https://support.apple.com/102602">iCloud Private Relay</a> uses similar privacy-separation principles and uses <a href="https://blog.cloudflare.com/icloud-private-relay/">Cloudflare as one of their partners</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/hybrid-public-key-encryption/">HPKE: Standardizing public-key encryption</a> blog post</li>
<li><a href="/privacy-gateway/">Privacy Gateway</a></li>
</ul>
