<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 29, 2026</time><h2 id="post-title">TLS bug detection in the Cloudflare Radar post-quantum checker</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p>The <a href="/radar/"><strong>Radar</strong></a> <a href="https://radar.cloudflare.com/post-quantum#website-support">post-quantum TLS support checker</a> now also reports TLS bugs detected during the handshake test. When a scanned host exhibits compatibility issues, the results include details on the specific bugs detected, along with guidance on how to investigate and remediate each issue. The bugs section only appears for hosts where issues are found.</p>
<p>The following TLS bugs are detected:</p>
<ul>
<li><strong>Split ClientHello</strong> — The connection fails with a fragmented post-quantum <code>ClientHello</code> but succeeds with classical handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS messages.</li>
<li><strong>HRR Failure</strong> — The server sends a <code>HelloRetryRequest</code> but fails to complete the handshake afterward.</li>
<li><strong>Unknown Keyshare</strong> — The server cannot handle unknown key exchange algorithms and fails instead of responding with a <code>HelloRetryRequest</code> as required by the TLS 1.3 specification.</li>
</ul>
<p><img src="/assets/upstream/images/radar/pq-tls-bug-detection.png" alt="TLS bug detection results in the Radar post-quantum checker" /></p>
<p>Bug detection data is available through the existing <a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> endpoint.</p>
<p>Visit the <a href="https://radar.cloudflare.com/post-quantum#website-support">Post-Quantum Encryption</a> page to test a host.</p>
</div></article></div>
