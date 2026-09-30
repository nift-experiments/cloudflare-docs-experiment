<p>The sections below summarize third-party software support for the post-quantum algorithms Cloudflare has deployed, organized by software category. <a href="/style-guide/contributions/">Contributions</a> to keep the listing up-to-date are welcome.</p>
<p>Two classes of algorithm are tracked:</p>
<ul>
<li><strong>Key agreement</strong> — the <a href="https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/">X25519MLKEM768</a> hybrid, which protects against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now-decrypt-later</a> attacks on encrypted traffic. Refer to <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">hybrid key agreement</a> for background.</li>
<li><strong>Signatures</strong> — <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a>, the post-quantum digital signature algorithm standardized by NIST, defined with three parameter sets (ML-DSA-44, ML-DSA-65, ML-DSA-87). Refer to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the list of products that support ML-DSA, and to <a href="/ssl/post-quantum-cryptography/#post-quantum-signatures">post-quantum signatures</a> for background.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13991.md")
</aside>
<h2 id="browsers">Browsers</h2>
<p>Browsers are grouped by the underlying rendering engine and TLS stack. Browsers sharing an engine generally share the same post-quantum support, but derivative browsers can lag the upstream engine or disable post-quantum features by policy. Verify behavior in the specific browser version you care about before assuming derivative support. <a href="https://radar.cloudflare.com/post-quantum#browser-support">Cloudflare Radar's browser support check</a> is a quick way to confirm whether a given browser negotiates post-quantum key agreement with Cloudflare.</p>
<h3 id="chromium-based-boringssl">Chromium-based (BoringSSL)</h3>
<h4 id="brave">Brave</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Brave 1.73.86+ (Chromium 131)</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://brave.com">Brave</a></li>
</ul>
<h4 id="chrome">Chrome</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Chrome 131+</li>
<li><strong>Signatures:</strong> 📝 Planned via <a href="https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/">Merkle Tree Certificates</a></li>
<li><strong>Reference:</strong> <a href="https://www.google.com/chrome/">Chrome</a>, <a href="https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html">Cultivating a robust and efficient quantum-safe HTTPS</a></li>
</ul>
<p>Chrome is not planning to add standard X.509 post-quantum certificates to the public Chrome Root Store. Instead, Chrome is developing MTCs in the IETF PLANTS working group, currently in a feasibility study phase with Cloudflare.</p>
<h4 id="edge">Edge</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Edge 131+</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://microsoft.com/edge/">Edge</a></li>
</ul>
<h4 id="opera">Opera</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Opera 116+ (Chromium 131)</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://opera.com">Opera</a></li>
</ul>
<h3 id="gecko-based-firefox-nss">Gecko-based (Firefox / NSS)</h3>
<h4 id="firefox">Firefox</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Firefox 132+ (Desktop), 145+ (Android)</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://www.mozilla.org/firefox/">Firefox</a></li>
</ul>
<p>For QUIC/HTTP3, Firefox 135+ (Desktop).</p>
<h4 id="tor-browser">Tor Browser</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Tor Browser 15.0+</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://www.torproject.org/">Tor Browser</a></li>
</ul>
<p>Based on Firefox ESR with additional hardening.</p>
<h3 id="webkit-based-safari">WebKit-based (Safari)</h3>
<h4 id="safari">Safari</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Safari 26+</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://www.apple.com/safari/">Safari</a></li>
</ul>
<p>System-wide in iOS 26, macOS Tahoe 26, and other <a href="https://support.apple.com/122756">Apple operating systems</a>.</p>
<h2 id="libraries">Libraries</h2>
<p>This section splits into the foundational native libraries (written in C/C++) and the language bindings and higher-level libraries that build on top of them.</p>
<h3 id="native-libraries">Native libraries</h3>
<h4 id="aws-lc">AWS-LC</h4>
<ul>
<li><strong>Key agreement:</strong> ✅</li>
<li><strong>Signatures:</strong> ✅</li>
<li><strong>Reference:</strong> <a href="https://github.com/aws/aws-lc">aws-lc</a>, <a href="https://github.com/aws/aws-lc/blob/main/crypto/fipsmodule/PQREADME.md">Post-Quantum Cryptography in AWS-LC</a></li>
</ul>
<p>ML-KEM-512/768/1024 and hybrids <code>X25519MLKEM768</code>, <code>SecP256r1MLKEM768</code>, <code>SecP384r1MLKEM1024</code>; ML-DSA-44/65/87.</p>
<h4 id="boringssl">BoringSSL</h4>
<ul>
<li><strong>Key agreement:</strong> ✅</li>
<li><strong>Signatures:</strong> ✅</li>
<li><strong>Reference:</strong> <a href="https://boringssl.googlesource.com/boringssl/">BoringSSL</a></li>
</ul>
<p>ML-DSA-44/65/87.</p>
<h4 id="botan-c">Botan C++</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in TLS since 3.7.0</li>
<li><strong>Signatures:</strong> ✅ 3.6.0+</li>
<li><strong>Reference:</strong> <a href="https://botan.randombit.net/">Botan</a></li>
</ul>
<p>ML-DSA-44/65/87.</p>
<h4 id="gnutls">GnuTLS</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ 3.8.9+ compiled with leancrypto 1.2.0+ (or 3.8.8–3.8.9 with liboqs 0.11.0+)</li>
<li><strong>Signatures:</strong> ✅ 3.8.10+ — usable in TLS handshakes</li>
<li><strong>Reference:</strong> <a href="https://www.gnutls.org">GnuTLS</a></li>
</ul>
<p>Hybrids <code>X25519MLKEM768</code> and <code>SecP256r1MLKEM768</code> from 3.8.8+; <code>SecP384r1MLKEM1024</code> added in 3.8.9+. ML-DSA-44/65/87.</p>
<h4 id="openssl">OpenSSL</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in 3.5.0+</li>
<li><strong>Signatures:</strong> ✅ 3.5.0+</li>
<li><strong>Reference:</strong> <a href="https://www.openssl.org/">OpenSSL</a></li>
</ul>
<p>Hybrid <code>X25519MLKEM768</code> in 3.5.0+; <code>SecP256r1MLKEM768</code> and <code>curveSM2MLKEM768</code> added in 3.6.0+. ML-DSA-44/65/87.</p>
<h4 id="open-quantum-safe">Open Quantum Safe</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ liboqs 0.10.0+, oqs-provider 0.7.0+</li>
<li><strong>Signatures:</strong> ✅ liboqs 0.14.0+, oqs-provider 0.9.0+</li>
<li><strong>Reference:</strong> <a href="https://openquantumsafe.org/">Open Quantum Safe</a></li>
</ul>
<p>Reference implementations, not recommended for production.</p>
<h4 id="s2n-tls">s2n-tls</h4>
<ul>
<li><strong>Key agreement:</strong> ✅</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://github.com/aws/s2n-tls">s2n-tls</a></li>
</ul>
<p>AWS's open-source TLS implementation built on <a href="#aws-lc">AWS-LC</a>.</p>
<h3 id="language-bindings-and-higher-level-libraries">Language bindings and higher-level libraries</h3>
<h4 id="aws-lc-rs-rust">aws-lc-rs (Rust)</h4>
<ul>
<li><strong>Key agreement:</strong> ✅</li>
<li><strong>Signatures:</strong> 🚧 Behind <code>unstable</code> feature</li>
<li><strong>Reference:</strong> <a href="https://crates.io/crates/aws-lc-rs">aws-lc-rs</a></li>
</ul>
<p>Rust bindings around <a href="#aws-lc">AWS-LC</a>; underlies <a href="#rustls-post-quantum-rust"><code>rustls-post-quantum</code></a>'s ML-DSA support. ML-KEM via <a href="https://docs.rs/aws-lc-rs/latest/aws_lc_rs/kem/"><code>aws-lc-rs::kem</code></a>; ML-DSA-44/65/87 via <a href="https://docs.rs/aws-lc-rs/latest/aws_lc_rs/unstable/signature/"><code>unstable::signature</code></a>.</p>
<h4 id="circl-cloudflare">CIRCL (Cloudflare)</h4>
<ul>
<li><strong>Key agreement:</strong> ✅</li>
<li><strong>Signatures:</strong> ✅ 1.5.0+ via <a href="https://github.com/cloudflare/circl/tree/main/sign/mldsa"><code>sign/mldsa</code></a></li>
<li><strong>Reference:</strong> <a href="https://github.com/cloudflare/circl">CIRCL</a></li>
</ul>
<p>Pure-Go cryptographic primitives library. ML-KEM-512/768/1024 and ML-DSA-44/65/87.</p>
<h4 id="go">Go</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Go 1.24+</li>
<li><strong>Signatures:</strong> 🚧 Internal implementation in Go 1.26; public <a href="https://github.com/golang/go/issues/77626"><code>crypto/mldsa</code></a> proposed for Go 1.27</li>
<li><strong>Reference:</strong> <a href="https://go.dev">Go</a></li>
</ul>
<p>Cloudflare's <a href="https://github.com/cloudflare/go">fork of Go</a> also supports key agreement via <a href="#circl-cloudflare">CIRCL</a>.</p>
<h4 id="java-openjdk">Java (OpenJDK)</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Java 27+ (<a href="https://openjdk.org/jeps/527">JEP 527</a>)</li>
<li><strong>Signatures:</strong> 🚧 Java 24+ provides ML-DSA APIs (<a href="https://openjdk.org/jeps/497">JEP 497</a>) but they are not yet integrated into <code>javax.net.ssl</code> TLS</li>
<li><strong>Reference:</strong> <a href="https://openjdk.org/">OpenJDK</a></li>
</ul>
<h4 id="node-js">Node.js</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in 24.5.0+ and 22.20.0+ (<a href="https://nodejs.org/en/blog/release/v22.20.0#openssl-updated-to-352">backported</a>)</li>
<li><strong>Signatures:</strong> ✅ 24.5.0+</li>
<li><strong>Reference:</strong> <a href="https://nodejs.org/">Node.js</a></li>
</ul>
<p>Uses bundled <a href="#openssl">OpenSSL</a> 3.5. ML-DSA-44/65/87.</p>
<h4 id="rustcrypto-rust">RustCrypto (Rust)</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ <a href="https://crates.io/crates/ml-kem"><code>ml-kem</code></a></li>
<li><strong>Signatures:</strong> ✅ <a href="https://crates.io/crates/ml-dsa"><code>ml-dsa</code></a></li>
<li><strong>Reference:</strong> <a href="https://github.com/RustCrypto">RustCrypto</a></li>
</ul>
<p>Pure-Rust crates, independent of <a href="#aws-lc">AWS-LC</a>. ML-DSA-44/65/87.</p>
<h4 id="rustls-rust">rustls (Rust)</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Enabled by default since rustls 0.23.27</li>
<li><strong>Signatures:</strong> 🚧 Unstable</li>
<li><strong>Reference:</strong> <a href="https://crates.io/crates/rustls">rustls</a></li>
</ul>
<p>TLS library built on top of <a href="#rustls-post-quantum-rust"><code>rustls-post-quantum</code></a>.</p>
<h4 id="rustls-post-quantum-rust">rustls-post-quantum (Rust)</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ <code>X25519MLKEM768</code></li>
<li><strong>Signatures:</strong> 🚧 Unstable ML-DSA support (behind <code>aws-lc-rs-unstable</code> feature)</li>
<li><strong>Reference:</strong> <a href="https://crates.io/crates/rustls-post-quantum">rustls-post-quantum</a></li>
</ul>
<p>Extension crate for <a href="#rustls-rust">rustls</a> that provides post-quantum algorithms using <a href="#aws-lc-rs-rust">aws-lc-rs</a> under the hood.</p>
<h4 id="zig">Zig</h4>
<ul>
<li><strong>Key agreement:</strong> ✅ Zig 0.14.0+ (client)</li>
<li><strong>Signatures:</strong> Not yet</li>
<li><strong>Reference:</strong> <a href="https://ziglang.org/">Zig</a></li>
</ul>
<h2 id="servers">Servers</h2>
<h3 id="caddy">Caddy</h3>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in Caddy 2.10.0+</li>
<li><strong>Signatures:</strong> Blocked on Go <code>crypto/mldsa</code></li>
<li><strong>Reference:</strong> <a href="https://caddyserver.com/">Caddy</a></li>
</ul>
<h3 id="nginx">NGINX</h3>
<ul>
<li><strong>Key agreement:</strong> ✅ Default when compiled with OpenSSL 3.5+ (<a href="https://github.com/nginx/nginx/issues/288">instructions</a>)</li>
<li><strong>Signatures:</strong> ✅ When compiled with OpenSSL 3.5+</li>
<li><strong>Reference:</strong> <a href="https://github.com/nginx/nginx">NGINX</a></li>
</ul>
<h3 id="rpxy">rpxy</h3>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in 0.9.4+</li>
<li><strong>Signatures:</strong> Blocked on Rust PQ signature support</li>
<li><strong>Reference:</strong> <a href="https://github.com/junkurihara/rust-rpxy">rpxy</a></li>
</ul>
<h3 id="traefik">Traefik</h3>
<ul>
<li><strong>Key agreement:</strong> ✅ Default in 3.4.2+, 2.11.26+ (<a href="https://github.com/traefik/traefik/commit/cd16321dd9c25bb47a2e9417b2a4a75959be63d0">commit</a>); configurable via <code>curvePreferences</code> in 3.5.0-rc.1+</li>
<li><strong>Signatures:</strong> Blocked on Go <code>crypto/mldsa</code></li>
<li><strong>Reference:</strong> <a href="https://traefik.io/traefik/">Traefik</a></li>
</ul>
