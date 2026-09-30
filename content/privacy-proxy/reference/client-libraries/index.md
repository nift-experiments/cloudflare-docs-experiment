<p>This page lists open source libraries and tools you can use to connect to Privacy Proxy.</p>
<h2 id="tokio-quiche">tokio-quiche</h2>
<p><a href="https://github.com/cloudflare/quiche/tree/master/tokio-quiche">tokio-quiche</a> is Cloudflare's open source async QUIC and HTTP/3 library for Rust. It combines the <a href="https://github.com/cloudflare/quiche">quiche</a> QUIC implementation with the <a href="https://tokio.rs/">Tokio</a> async runtime.</p>
<p>tokio-quiche powers Privacy Proxy infrastructure, including Proxy B for iCloud Private Relay and Cloudflare's Oxy-based proxies. It handles millions of HTTP/3 requests per second in production.</p>
<h3 id="features">Features</h3>
<ul>
<li>Async QUIC client and server</li>
<li>HTTP/3 support via <code>H3Driver</code></li>
<li>MASQUE CONNECT and CONNECT-UDP support</li>
<li>Battle-tested at scale on Cloudflare's network</li>
</ul>
<h3 id="installation">Installation</h3>
<p>Add tokio-quiche to your <code>Cargo.toml</code>:</p>
<pre><code class="language-toml">[dependencies]&#10;tokio-quiche = &quot;0.1&quot;&#10;</code></pre>
<h3 id="resources">Resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/quiche/tree/master/tokio-quiche">GitHub repository</a></li>
<li><a href="https://crates.io/crates/tokio-quiche">crates.io</a></li>
<li><a href="https://blog.cloudflare.com/async-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source/">Blog post: Async QUIC and HTTP/3 made easy</a></li>
</ul>
<hr />
<h2 id="quiche">quiche</h2>
<p><a href="https://github.com/cloudflare/quiche">quiche</a> is Cloudflare's low-level QUIC and HTTP/3 implementation in Rust. It provides a sans-io design that can integrate into any application architecture.</p>
<p>quiche is the foundation that tokio-quiche builds upon. Use quiche directly if you need fine-grained control over I/O or are integrating with a non-Tokio runtime.</p>
<h3 id="resources-1">Resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/quiche">GitHub repository</a></li>
<li><a href="https://docs.quic.tech/quiche/">Documentation</a></li>
<li><a href="https://crates.io/crates/quiche">crates.io</a></li>
</ul>
<hr />
<h2 id="chaussette">Chaussette</h2>
<p><a href="https://github.com/cloudflare/chaussette">Chaussette</a> is a SOCKS5-to-CONNECT proxy designed for Privacy Proxy. It accepts local SOCKS5 connections and forwards them as HTTP CONNECT requests to Privacy Proxy.</p>
<p>Chaussette is useful for integrating applications that support SOCKS5 but not HTTP CONNECT proxying.</p>
<h3 id="features-1">Features</h3>
<ul>
<li>SOCKS5 to HTTP CONNECT conversion</li>
<li>Pre-shared key authentication</li>
<li>Geohash support for geolocation hints</li>
<li>Optional mTLS authentication</li>
</ul>
<h3 id="usage">Usage</h3>
<pre><code class="language-sh">MASQUE_PRESHARED_KEY=&lt;YOUR_PSK&gt; chaussette \&#10;  &#45;-listen 127.0.0.1:1987 \&#10;  &#45;-proxy https://your-proxy.example.com:443 \&#10;  &#45;-geohash xn76c-JP&#10;</code></pre>
<p>Then configure your application to use <code>socks5://127.0.0.1:1987</code> as its proxy.</p>
<h3 id="resources-2">Resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/chaussette">GitHub repository</a></li>
</ul>
<hr />
<h2 id="curl">curl</h2>
<p>For basic testing over HTTP/2, standard curl supports CONNECT proxying:</p>
<pre><code class="language-sh">curl -v \&#10;  &#45;-proxy https://your-proxy.example.com \&#10;  &#45;-proxy-header &quot;Proxy-Authorization: Preshared &lt;YOUR_PSK&gt;&quot; \&#10;  https://example.com&#10;</code></pre>
<p>curl can also be <a href="https://github.com/curl/curl/blob/master/docs/HTTP3.md#quiche-version">built with quiche</a> for HTTP/3 support.</p>
<hr />
<h2 id="privacypass-ts">privacypass-ts</h2>
<p><a href="https://github.com/cloudflare/privacypass-ts">privacypass-ts</a> is Cloudflare's TypeScript implementation of the Privacy Pass protocol. Use this library to issue and redeem Privacy Pass tokens for authenticating with Privacy Proxy.</p>
<h3 id="features-2">Features</h3>
<ul>
<li>Privacy Pass token issuance and redemption</li>
<li>Support for publicly verifiable and rate-limited token types</li>
<li>Compatible with browser and Node.js environments</li>
</ul>
<h3 id="installation-1">Installation</h3>
<pre><code class="language-sh">npm install @cloudflare/privacypass-ts&#10;</code></pre>
<h3 id="resources-3">Resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/privacypass-ts">GitHub repository</a></li>
<li><a href="https://www.npmjs.com/package/@cloudflare/privacypass-ts">npm package</a></li>
</ul>
