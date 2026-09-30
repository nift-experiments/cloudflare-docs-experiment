<p>While network infrastructure is shifting towards IPv6-only networks, providers still need to support IPv4 addresses. Dual-stack networks (networks in which all nodes have both IPv4 and IPv6 connectivity capabilities) can understand both IPv4 and IPv6 packets. However, not all networks are dual-stack, and IPv6-only networks need a translation mechanism to reach IPv4 resources.</p>
<p>1.1.1.1 supports DNS64, a mechanism that synthesizes AAAA records (DNS records that map domain names to IPv6 addresses) from A records (DNS records that map domain names to IPv4 addresses) when no AAAA records exist. This allows IPv6-only clients to receive a usable IPv6 address for destinations that only have an IPv4 address, so the client can still connect through the network's NAT64 gateway.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1814.md")
</aside>
<h2 id="configure-dns64">Configure DNS64</h2>
<p>DNS64 is specifically for networks that already have NAT64 (Network Address Translation from IPv6 to IPv4) support. NAT64 translates IPv6 traffic to IPv4 at the network level, while DNS64 provides the corresponding translated addresses through DNS. If you are a network operator who has NAT64, you can test our DNS64 support by updating it to the following IP addresses:</p>
<pre><code class="language-txt">2606:4700:4700::64&#10;2606:4700:4700::6400&#10;</code></pre>
<p>Some devices use separate fields for all eight parts of IPv6 addresses and cannot accept the <code>::</code> IPv6 abbreviation syntax. For such fields enter:</p>
<pre><code class="language-txt">2606:4700:4700:0:0:0:0:64&#10;2606:4700:4700:0:0:0:0:6400&#10;</code></pre>
<h2 id="test-dns64">Test DNS64</h2>
<p>After your configuration, visit an IPv4-only address to check if you can reach it over your IPv6-only network. For example, you can visit <a href="https://ipv4.google.com">https://ipv4.google.com</a>. If the page loads, DNS64 and NAT64 are working together to translate your connection.</p>
<p>Visit <a href="http://test-ipv6.com/">http://test-ipv6.com/</a> to test if it can detect your IPv6 address. If you receive a <code>10/10</code>, your IPv6 is configured correctly.</p>
