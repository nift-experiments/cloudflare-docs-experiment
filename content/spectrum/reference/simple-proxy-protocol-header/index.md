<p>The client source IP and port is encoded in a fixed-length, 38-octet long header and prepended to the payload of each proxied UDP datagram in the format described below.</p>
<pre><code class="language-txt"> 0                   1                   2                   3&#10; 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|          Magic Number         |                               |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                               +&#10;|                                                               |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;                         Client Address                        +&#10;|                                                               |&#10;&#43;                               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                               |                               |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                               +&#10;|                                                               |&#10;&#43;                                                               +&#10;|                                                               |&#10;&#43;                         Proxy Address                         +&#10;|                                                               |&#10;&#43;                               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|                               |         Client Port           |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;|           Proxy Port          |          Payload...           |&#10;&#43;-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+&#10;</code></pre>
<p>The contents of the header are below.</p>
<h2 id="magic-number">Magic Number</h2>
<p>16-bit fixed value set to 0x56EC for SPP. This field should be used to identify the SPP protocol and its SPP 38-byte header.</p>
<h2 id="client-address">Client Address</h2>
<p>128-bit address of the originator of the proxied UDP datagram, that is, the client. An IPv6 address if the client used IPv6 addressing, or an IPv4-mapped IPv6 address (refer to <a href="https://tools.ietf.org/html/rfc4291">RFC 4291</a>) in case of an IPv4 client.</p>
<h2 id="proxy-address">Proxy address</h2>
<p>128-bit address of the recipient of the proxied UDP datagram, that is the proxy. Contents should be interpreted in the same way as the Client Address.</p>
<h2 id="client-port">Client port</h2>
<p>16-bit source port number of the proxied UDP datagram. In other words, the UDP port number from which the client sent the datagram.</p>
<h2 id="proxy-port">Proxy port</h2>
<p>16-bit destination port number of the proxied UDP datagram. In other words, the UDP port number on which the proxy received the datagram.</p>
<h2 id="payload">Payload</h2>
<p>Data following the header carried by the datagram.
Magic number, addresses, and port numbers are encoded in network byte order.</p>
<p>A corresponding C structure describing the header is:</p>
<pre><code class="language-c">struct {&#10;    uint16_t magic;&#10;    uint8_t  client_addr[16];&#10;    uint8_t  proxy_addr[16];&#10;    uint16_t client_port;&#10;    uint16_t proxy_port;&#10;};&#10;</code></pre>
