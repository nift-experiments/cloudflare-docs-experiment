<p>Smart Shield reduces the number of connections between Cloudflare and your origin server by batching multiple requests through shared connections. When requests from an <a href="/smart-shield/configuration/smart-tiered-cache/">upper-tier data center</a> — the layer of Cloudflare's cache that sits closest to your origin — need to reach your server, Smart Shield sends them over a single connection instead of opening a new connection for each request. This reduces overall connections to your origin by 30% on average, which lowers resource consumption on your origin and reduces the risk of connection exhaustion under high traffic.</p>
<p>For more information, refer to the <a href="https://blog.cloudflare.com/introducing-observatory-and-smart-shield/#protecting-and-accelerating-origins-with-smart-connection-reuse">Smart Shield announcement blog post</a>.</p>
<h2 id="about-connection-reuse">About connection reuse</h2>
<p>Every HTTP request requires a TCP connection between a client and a server. Each connection is identified by a pair of network addresses: the source IP address and port, and the destination IP address and port. Opening a new TCP connection has overhead — it requires a handshake between client and server, and a TLS negotiation if the connection is encrypted.</p>
<p>Connection reuse (also called persistent connections or keep-alive) avoids this overhead by sending multiple HTTP requests over a single TCP connection instead of opening a new connection for each request. HTTP/1.1 made this the default behavior.</p>
<p>For example, when a browser opens a connection to <code>shop.example.com</code>, the page may reference dozens of additional resources — stylesheets, images, scripts, and other files. Without connection reuse, each resource would require its own TCP connection. With connection reuse, all of these requests flow through the same connection.</p>
<h3 id="connection-coalescing-http-2">Connection coalescing (HTTP/2)</h3>
<p>With HTTP/2, connection reuse extends further through connection coalescing. This allows requests for different hostnames to share a single connection, as long as two conditions are met:</p>
<ul>
<li>The hostnames resolve to the same destination IP address and port.</li>
<li>The TLS certificate on the server covers both hostnames (for example, a certificate that lists both <code>shop.example.com</code> and <code>blog.example.com</code> in its Subject Alternative Names).</li>
</ul>
<p>This means a connection originally opened for <code>shop.example.com</code> can also carry requests for <code>blog.example.com</code>, reducing the total number of connections to your origin even further.</p>
<h2 id="connection-reuse-and-dedicated-cdn-egress-ips">Connection reuse and Dedicated CDN Egress IPs</h2>
<p>Connection reuse and connection coalescing are also considered when allocating your <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a>.</p>
