<p>Because Cloudflare intercepts packets before forwarding them to your server, if you were to look up the client IP, you would see Cloudflare's IP rather than the true client IP.</p>
<p>Some services you run may require knowledge of the true client IP. In those cases, you can use a proxy protocol for Cloudflare to pass on the client IP to your service. Sending proxy information along is dependent on whether TCP or UDP is used. For TCP, Spectrum supports adding <a href="https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt">Proxy Protocol v1</a>, which is the human readable version supported by Amazon ELB and <a href="https://docs.nginx.com/nginx/admin-guide/load-balancer/using-proxy-protocol/">NGINX</a>. For UDP applications, Cloudflare has developed a custom proxy protocol called Simple Proxy Protocol. Be aware that Proxy Protocol is not supported for Spectrum egresses to Cloudflare WAN (formerly Magic WAN).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13874.md")
</aside>
<h2 id="enable-proxy-protocol-v1-for-tcp">Enable Proxy Protocol v1 for TCP</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Spectrum</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Locate the application that will use the PROXY protocol and select <strong>Configure</strong>.</li>
<li>From the dropdown, select <strong>PROXY Protocol v1</strong>.</li>
</ol>
<p>When TCP applications are configured to use <strong>PROXY Protocol v1</strong>, Cloudflare will prepend each inbound TCP connection with the PROXY Protocol plain-text header.</p>
<h3 id="the-proxy-protocol-v1-header">The Proxy Protocol v1 Header</h3>
<p>PROXY Protocol prepends every connection with a header reporting the client IP address and port. A PROXY Protocol plain-text header has the format:</p>
<pre><code>PROXY_STRING + single space + INET_PROTOCOL + single space + CLIENT_IP + single space + PROXY_IP + single space + CLIENT_PORT + single space + PROXY_PORT + &quot;\r\n&quot;&#10;</code></pre>
<p>An example PROXY Protocol line for an IPv4 address would look like:</p>
<pre><code>PROXY TCP4 192.0.2.0 192.0.2.255 42300 443\r\n&#10;</code></pre>
<p>An example PROXY Protocol line for an IPv6 address would look like:</p>
<pre><code>PROXY TCP6 2001:db8:: 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff 42300 443\r\n&#10;</code></pre>
<h2 id="enable-proxy-protocol-v2-for-tcp-udp">Enable Proxy Protocol v2 for TCP/UDP</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Spectrum</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Locate the application that will use the PROXY protocol and select <strong>Configure</strong>.</li>
<li>From the dropdown, select <strong>PROXY Protocol v2</strong>.</li>
</ol>
<p>When TCP applications are configured to use <strong>PROXY Protocol v2</strong>, Cloudflare will prepend each inbound TCP connection with the PROXY Protocol binary header.</p>
<p>When UDP applications are configured to use <strong>PROXY Protocol v2</strong>, Cloudflare will prepend the first UDP datagram on a stream with a PROXY Protocol binary header.</p>
<h3 id="the-proxy-protocol-v2-header">The Proxy Protocol v2 Header</h3>
<p>PROXY Protocol prepends every connection with a header reporting the client IP address and port.</p>
<p>A PROXY Protocol binary header for a IPv4 incoming address has the format:</p>
<pre><code class="language-txt"> 0                   1                   2                   3&#10; 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                                                               |&#10;&#43;                                                               +&#10;|                  Proxy Protocol v2 Signature                  |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|Version|Command|   AF  | Proto.|         Address Length        |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                      IPv4 Source Address                      |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                    IPv4 Destination Address                   |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|          Source Port          |        Destination Port       |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;</code></pre>
<p>A PROXY Protocol binary header for a IPv6 incoming address has the format:</p>
<pre><code class="language-txt"> 0                   1                   2                   3&#10; 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                                                               |&#10;&#43;                                                               +&#10;|                  Proxy Protocol v2 Signature                  |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|Version|Command|   AF  | Proto.|         Address Length        |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                                                               |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;                      IPv6 Source Address                      +&#10;|                                                               |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                                                               |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;                    IPv6 Destination Address                   +&#10;|                                                               |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|          Source Port          |        Destination Port       |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;</code></pre>
<h2 id="enable-simple-proxy-protocol-for-udp">Enable Simple Proxy Protocol for UDP</h2>
<p>When using Spectrum for UDP, the client source IP and port information can be obtained by using Simple Proxy Protocol, a lightweight protocol developed specifically for UDP.</p>
<p>To enable it, select <strong>Configure</strong> on a Spectrum application and toggle the setting for Simple Proxy Protocol to <strong>On</strong>.</p>
<p>Simple Proxy Protocol dictates that your origin must also prepend packets meant for the client with the same header, including original client source information. This is done to validate that packets coming in are in fact intended for the client.</p>
<p>For more information about Simple Proxy Protocol headers, refer to <a href="/spectrum/reference/simple-proxy-protocol-header/">Simple Proxy Protocol headers</a>.</p>
