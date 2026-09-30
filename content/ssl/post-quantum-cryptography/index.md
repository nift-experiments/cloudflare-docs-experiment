<p>Post-quantum cryptography (PQC) refers to cryptographic algorithms that have been designed to resist attacks from <a href="https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/">quantum computers</a>. Cloudflare has been researching and <a href="https://blog.cloudflare.com/tag/post-quantum/">writing about post-quantum</a> since 2017, and is targeting 2029 to be fully post-quantum secure across its entire product suite — refer to <a href="https://blog.cloudflare.com/post-quantum-roadmap/">Cloudflare targets 2029 for full post-quantum security</a> for the full roadmap.</p>
<p>To protect you against the risk of <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later attacks</a>, and considering all the <a href="#three-connections-in-the-life-of-a-request">connections</a> that take place when your website or application is on Cloudflare, we have deployed and are actively expanding the use of <a href="#hybrid-key-agreement">post-quantum hybrid key agreement</a>. In parallel, Cloudflare is beginning to deploy <a href="#post-quantum-signatures">post-quantum signatures</a> to protect authentication against future quantum attacks.</p>
<p>Refer to <a href="https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption-adoption">Cloudflare Radar</a> for current statistics on the adoption of PQ encryption in requests to Cloudflare, and visit <a href="https://radar.cloudflare.com/post-quantum#browser-support">Cloudflare Radar's browser support check</a> to check if your browser is secured using PQ key agreement.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="tls-1-3">TLS 1.3</h3>
@markup("md", "content/.markup/bodies/13993.md")
</aside>
<h2 id="three-building-blocks-of-tls">Three building blocks of TLS</h2>
<p>Before TLS can protect your communications, three cryptographic algorithms have to be agreed on during the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">TLS handshake</a>:</p>
<ul>
<li><strong>Symmetric ciphers:</strong> Algorithms used to encrypt and decrypt data, ensuring confidentiality and integrity (such as <code>CHACHA20-POLY1305</code>).</li>
<li><strong>Key agreement:</strong> A cryptographic protocol that allows client and server to safely agree on a shared key (such as <code>ECDH</code>).</li>
<li><strong>Signature algorithms:</strong> Cryptographic algorithms used to generate the digital signatures in TLS certificates (such as <code>RSA</code> and <code>ECDSA</code>).</li>
</ul>
<p>As explained in our <a href="https://blog.cloudflare.com/pq-2025/#already-post-quantum-secure-symmetric-cryptography">blog post</a>, symmetric ciphers are already post-quantum secure, which means there are two migrations left to occur.</p>
<h3 id="hybrid-key-agreement">Hybrid key agreement</h3>
<p>With TLS 1.3, <a href="https://en.wikipedia.org/wiki/Curve25519">X25519</a> - an Elliptic Curve Diffie-Hellman (ECDH) protocol - is the most commonly used algorithm in key agreement. However, its security can be broken by quantum computers using <a href="https://en.wikipedia.org/wiki/Shor%27s_algorithm">Shor's algorithm</a>.</p>
<p>It is urgent to migrate key agreement to post-quantum algorithms as soon as possible. The objective is to protect against an adversary capable of harvesting today's encrypted communications and storing it until some time in the future when they can gain access to a sufficiently powerful quantum computer to decrypt it.</p>
<p>In response to this, Cloudflare has deployed support for ML-KEM, the post-quantum key agreement selected by the US National Institute of Standards and Technology (NIST). Refer to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the current deployment status across products. For a detailed timeline and more background information refer to <a href="https://blog.cloudflare.com/pq-2025/">State of the post-quantum Internet in 2025</a>.</p>
<p>Cloudflare has deployed the following hybrid key agreements:</p>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/">X25519MLKEM768</a> (Recommended)
<ul>
<li>TLS identifier: <code>0x11ec</code></li>
</ul>
</li>
<li><a href="https://datatracker.ietf.org/doc/draft-tls-westerbaan-xyber768d00/">X25519Kyber768Draft00</a> (Obsolete)
<ul>
<li>TLS identifier: <code>0x6399</code></li>
</ul>
</li>
</ul>
<p>A hybrid key agreement lays the groundwork as more and more <a href="#1-visitor-to-cloudflare">clients</a> adopt post-quantum cryptography, while also maintaining the current security provided by X25519. It is a safer path in case of an unexpected breakthrough that renders all variants of ML-KEM insecure.</p>
<h3 id="post-quantum-signatures">Post-quantum signatures</h3>
<p>Recent advances in quantum hardware and algorithms have accelerated the timeline on which a cryptographically relevant quantum computer might exist, which in turn elevates the priority of migrating authentication (signatures) to post-quantum algorithms. Refer to <a href="https://blog.cloudflare.com/post-quantum-roadmap/">Cloudflare targets 2029 for full post-quantum security</a> for context.</p>
<p>Cloudflare has deployed support for <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a>, the post-quantum digital signature algorithm selected by NIST (FIPS 204). Today this support covers authentication on the connection between Cloudflare and your origin server (see <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">PQC to your origin</a>). Post-quantum authentication on the connection from the visitor to Cloudflare's edge and for internal Cloudflare connections is still under development. Refer to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the products that support ML-DSA today.</p>
<p>For background on the post-quantum signature landscape, refer to <a href="https://blog.cloudflare.com/another-look-at-pq-signatures/">A look at the latest post-quantum signature standardization candidates</a>.</p>
<h2 id="three-connections-in-the-life-of-a-request">Three connections in the life of a request</h2>
<pre><code class="language-mermaid">flowchart LR&#10;        accTitle: Three connections - from visitor to Cloudflare to origin server&#10;        accDescr: Diagram showing connections for an uncached request.&#10;        A[Visitor]&#10;        subgraph Cloudflare&#10;        X[(Cloudflare &lt;br /&gt;service A)]&#10;				B[(Cloudflare &lt;br /&gt;service B)]&#10;        end&#10;        C[(Origin server)]&#10;&#10;        A --1--&gt; X&#10;				X --2--&gt; B&#10;        B --3--&gt; C&#10;</code></pre>
<h3 id="1-visitor-to-cloudflare"><ol>
<li>Visitor to Cloudflare</li>
</ol></h3>
<p>As of <a href="https://blog.cloudflare.com/post-quantum-for-all/">October 2022</a>, all websites and APIs served through Cloudflare over TLS 1.3 support post-quantum hybrid key agreement. However, the connection is only post-quantum secured if the client also supports PQC.</p>
<p>Refer to <a href="/ssl/post-quantum-cryptography/pqc-support/">Post-quantum cryptography support</a> for a list of browsers and other clients that are compatible with hybrid key agreements.</p>
<h3 id="2-internal-connections"><ol start="2">
<li>Internal connections</li>
</ol></h3>
<p>As announced in <a href="https://blog.cloudflare.com/post-quantum-cryptography-ga/">September 2023</a>, most internal connections for Cloudflare's products and systems have been upgraded to use PQC.</p>
<h3 id="3-cloudflare-to-your-origin"><ol start="3">
<li>Cloudflare to your origin</li>
</ol></h3>
<p>Finally, Cloudflare also supports <a href="#hybrid-key-agreement">hybrid key agreements</a> when connecting to origins. In this case, post-quantum secured connections will depend on the origin servers also supporting PQC. Customers can also configure connections to origin servers via <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/">PQ Cloudflare Tunnel</a>.</p>
<p>Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/">Post-quantum cryptography between Cloudflare and origin servers</a> for details.</p>
<h2 id="protect-corporate-network-traffic">Protect corporate network traffic</h2>
<p>With <a href="/cloudflare-one/">Zero Trust</a>, Cloudflare allows organizations to upgrade their sensitive network traffic to PQC without the hassle of individually upgrading each and every corporate application, system, or network connection. This includes post-quantum <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">Cloudflare IPsec</a> tunnels with both the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> and validated third-party devices. <a href="https://www.cisco.com/">Cisco</a> and <a href="https://www.fortinet.com/">Fortinet</a> are the first third-party vendors validated to interoperate with Cloudflare IPsec for post-quantum key agreement — refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability">Tested third-party vendor interoperability</a> for the current list. For details on the Cloudflare One configurations, refer to <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/">Post-quantum cryptography in Cloudflare's Zero Trust platform</a>.</p>
