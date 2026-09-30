<p>You can implement a positive security model with Cloudflare Tunnel by blocking all ingress traffic and allowing only egress traffic from <code>cloudflared</code>. Only the services specified in your tunnel configuration will be exposed to the outside world.</p>
<h2 id="ports">Ports</h2>
<p>The parameters below can be configured for egress traffic inside of a firewall.</p>
<p>How you configure your firewall depends on the firewall type:</p>
<ul>
<li>If your firewall supports domain-based rules (FQDN allowlists), you can allow outbound connections to the hostnames listed below.</li>
<li>If your firewall requires IP-based rules, allow outbound connections to all listed IP addresses for each domain.</li>
</ul>
<p>Ensure port <code>7844</code> is allowed for both TCP and UDP protocols (for <code>http2</code> and <code>quic</code>).</p>
<h3 id="required-for-tunnel-operation">Required for tunnel operation</h3>
<p><code>cloudflared</code> connects to Cloudflare's global network on port <code>7844</code>. To use Cloudflare Tunnel, your firewall must allow outbound connections to the following destinations on port <code>7844</code> (via UDP if using the <code>quic</code> protocol or TCP if using the <code>http2</code> protocol).</p>
<hr />
<hr />
<h4 id="region1-v2-argotunnel-com"><code>region1.v2.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>198.41.192.167</code> <code>198.41.192.67</code> <code>198.41.192.57</code> <code>198.41.192.107</code> <code>198.41.192.27</code> <code>198.41.192.7</code> <code>198.41.192.227</code> <code>198.41.192.47</code> <code>198.41.192.37</code> <code>198.41.192.77</code></td>
<td><code>2606:4700:a0::1</code> <code>2606:4700:a0::2</code> <code>2606:4700:a0::3</code> <code>2606:4700:a0::4</code> <code>2606:4700:a0::5</code> <code>2606:4700:a0::6</code> <code>2606:4700:a0::7</code> <code>2606:4700:a0::8</code> <code>2606:4700:a0::9</code> <code>2606:4700:a0::10</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h4 id="region2-v2-argotunnel-com"><code>region2.v2.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>198.41.200.13</code> <code>198.41.200.193</code> <code>198.41.200.33</code> <code>198.41.200.233</code> <code>198.41.200.53</code> <code>198.41.200.63</code> <code>198.41.200.113</code> <code>198.41.200.73</code> <code>198.41.200.43</code> <code>198.41.200.23</code></td>
<td><code>2606:4700:a8::1</code> <code>2606:4700:a8::2</code> <code>2606:4700:a8::3</code> <code>2606:4700:a8::4</code> <code>2606:4700:a8::5</code> <code>2606:4700:a8::6</code> <code>2606:4700:a8::7</code> <code>2606:4700:a8::8</code> <code>2606:4700:a8::9</code> <code>2606:4700:a8::10</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h4 id="sni-enforcing-firewalls">SNI-enforcing firewalls</h4>
---
---
<p>If your firewall enforces Server Name Indication (SNI), also allow these hostnames on port <code>7844</code>:</p>
<table>
<thead>
<tr>
<th>Hostname</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>_v2-origintunneld._tcp.argotunnel.com</code></td>
<td>7844</td>
<td>TCP (<code>http2</code>)</td>
</tr>
<tr>
<td><code>cftunnel.com</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
<tr>
<td><code>h2.cftunnel.com</code></td>
<td>7844</td>
<td>TCP (<code>http2</code>)</td>
</tr>
<tr>
<td><code>quic.cftunnel.com</code></td>
<td>7844</td>
<td>UDP (<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h3 id="region-us">Region US</h3>
<p>When using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#region"><code>--region us</code></a> flag, ensure your firewall allows outbound connections to these US-region destinations on port <code>7844</code> (TCP/UDP).</p>
<h4 id="us-region1-v2-argotunnel-com"><code>us-region1.v2.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>198.41.218.1</code> <code>198.41.218.2</code> <code>198.41.218.3</code> <code>198.41.218.4</code> <code>198.41.218.5</code> <code>198.41.218.6</code> <code>198.41.218.7</code> <code>198.41.218.8</code> <code>198.41.218.9</code> <code>198.41.218.10</code></td>
<td><code>2606:4700:a1::1</code> <code>2606:4700:a1::2</code> <code>2606:4700:a1::3</code> <code>2606:4700:a1::4</code> <code>2606:4700:a1::5</code> <code>2606:4700:a1::6</code> <code>2606:4700:a1::7</code> <code>2606:4700:a1::8</code> <code>2606:4700:a1::9</code> <code>2606:4700:a1::10</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h4 id="us-region2-v2-argotunnel-com"><code>us-region2.v2.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>198.41.219.1</code> <code>198.41.219.2</code> <code>198.41.219.3</code> <code>198.41.219.4</code> <code>198.41.219.5</code> <code>198.41.219.6</code> <code>198.41.219.7</code> <code>198.41.219.8</code> <code>198.41.219.9</code> <code>198.41.219.10</code></td>
<td><code>2606:4700:a9::1</code> <code>2606:4700:a9::2</code> <code>2606:4700:a9::3</code> <code>2606:4700:a9::4</code> <code>2606:4700:a9::5</code> <code>2606:4700:a9::6</code> <code>2606:4700:a9::7</code> <code>2606:4700:a9::8</code> <code>2606:4700:a9::9</code> <code>2606:4700:a9::10</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h3 id="region-fedramp-high">Region FedRAMP High</h3>
<p>When deploying <code>cloudflared</code> in a <a href="https://www.cloudflare.com/cloudflare-for-government/">FedRAMP High</a> environment, <code>cloudflared</code> automatically routes to FedRAMP data centers based on the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/">tunnel token</a>. Ensure your firewall allows outbound connections to these FedRAMP-specific destinations on port <code>7844</code> (TCP/UDP).</p>
<h4 id="fed-region1-v2-argotunnel-com"><code>fed-region1.v2.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>162.159.234.1</code> <code>162.159.234.2</code> <code>162.159.234.3</code> <code>162.159.234.4</code> <code>162.159.234.5</code> <code>162.159.234.6</code> <code>162.159.234.7</code> <code>162.159.234.8</code> <code>162.159.234.9</code> <code>162.159.234.10</code></td>
<td><code>2a06:98c1:4d::1</code> <code>2a06:98c1:4d::2</code> <code>2a06:98c1:4d::3</code> <code>2a06:98c1:4d::4</code> <code>2a06:98c1:4d::5</code> <code>2a06:98c1:4d::6</code> <code>2a06:98c1:4d::7</code> <code>2a06:98c1:4d::8</code> <code>2a06:98c1:4d::9</code> <code>2a06:98c1:4d::10</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h4 id="fed-region2-v2-argotunnel-com"><code>fed-region2.v2.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>172.64.234.1</code> <code>172.64.234.2</code> <code>172.64.234.3</code> <code>172.64.234.4</code> <code>172.64.234.5</code> <code>172.64.234.6</code> <code>172.64.234.7</code> <code>172.64.234.8</code> <code>172.64.234.9</code> <code>172.64.234.10</code></td>
<td><code>2606:4700:f6::1</code> <code>2606:4700:f6::2</code> <code>2606:4700:f6::3</code> <code>2606:4700:f6::4</code> <code>2606:4700:f6::5</code> <code>2606:4700:f6::6</code> <code>2606:4700:f6::7</code> <code>2606:4700:f6::8</code> <code>2606:4700:f6::9</code> <code>2606:4700:f6::10</code></td>
<td>7844</td>
<td>TCP/UDP (<code>http2</code>/<code>quic</code>)</td>
</tr>
</tbody>
</table>
<h3 id="optional">Optional</h3>
<p>Opening port <code>443</code> enables some optional features. Failure to allow these connections may prompt a log error, but <code>cloudflared</code> will still run correctly.</p>
<h4 id="api-cloudflare-com"><code>api.cloudflare.com</code></h4>
<p>Allows <code>cloudflared</code> to query if software updates are available.</p>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>104.19.192.29</code> <code>104.19.192.177</code> <code>104.19.192.175</code> <code>104.19.193.29</code> <code>104.19.192.174</code> <code>104.19.192.176</code></td>
<td><code>2606:4700:300a::6813:c0af</code> <code>2606:4700:300a::6813:c01d</code> <code>2606:4700:300a::6813:c0ae</code> <code>2606:4700:300a::6813:c11d</code> <code>2606:4700:300a::6813:c0b0</code> <code>2606:4700:300a::6813:c0b1</code></td>
<td>443</td>
<td>TCP (HTTPS)</td>
</tr>
</tbody>
</table>
<h4 id="update-argotunnel-com"><code>update.argotunnel.com</code></h4>
<p>Allows <code>cloudflared</code> to query if software updates are available.</p>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>104.18.25.129</code> <code>104.18.24.129</code></td>
<td><code>2606:4700::6812:1881</code> <code>2606:4700::6812:1981</code></td>
<td>443</td>
<td>TCP (HTTPS)</td>
</tr>
</tbody>
</table>
<h4 id="github-com"><code>github.com</code></h4>
<p>Allows <code>cloudflared</code> to download the latest release and perform a software update.</p>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses">GitHub's IPs</a></td>
<td><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses">GitHub's IPs</a></td>
<td>443</td>
<td>TCP (HTTPS)</td>
</tr>
</tbody>
</table>
<h4 id="cloudflareaccess-com"><code>&lt;your-team-name&gt;.cloudflareaccess.com</code></h4>
<p>Allows <code>cloudflared</code> to validate the Access JWT. Only required if the <a href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cloudflared-parameters/origin-parameters/#access"><code>access</code></a> setting is enabled.</p>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>104.19.194.29</code> <code>104.19.195.29</code></td>
<td><code>2606:4700:300a::6813:c31d</code> <code>2606:4700:300a::6813:c21d</code></td>
<td>443</td>
<td>TCP (HTTPS)</td>
</tr>
</tbody>
</table>
<h4 id="pqtunnels-cloudflareresearch-com"><code>pqtunnels.cloudflareresearch.com</code></h4>
<p>Allows <code>cloudflared</code> to report <a href="https://blog.cloudflare.com/post-quantum-tunnel/">post-quantum key exchange</a> errors to Cloudflare.</p>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>104.18.4.64</code> <code>104.18.5.64</code></td>
<td><code>2606:4700::6812:540</code> <code>2606:4700::6812:440</code></td>
<td>443</td>
<td>TCP (HTTPS)</td>
</tr>
</tbody>
</table>
<h4 id="cfd-features-argotunnel-com"><code>cfd-features.argotunnel.com</code></h4>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
<th>Port</th>
<th>Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td>Not applicable</td>
<td>Not applicable</td>
<td>Not applicable</td>
<td>Not applicable</td>
</tr>
</tbody>
</table>
<p>Performing a DNS query for a <code>TXT</code> record to this hostname allows <code>cloudflared</code> to determine which version of <a href="/changelog/2025-07-15-udp-improvements/">UDP datagram</a> to use when connecting via the <code>quic</code> protocol. If your firewall filters egress DNS queries by FQDN, you may need to allow queries for this domain to ensure optimal <code>quic</code> performance.</p>
<h2 id="firewall-configuration">Firewall configuration</h2>
<h3 id="cloud-vm-firewall">Cloud VM firewall</h3>
<p>If you host your services on a virtual machine (VM) instance in a cloud provider, you may set up instance-level firewall rules to block all ingress traffic and allow only egress traffic. For example, on Google Cloud Platform (GCP), you may delete all ingress rules, leaving only the relevant egress rules. This is because GCP's firewall denies ingress traffic unless it matches an explicit rule.</p>
<h3 id="os-firewall">OS firewall</h3>
<p>Alternatively, you may use operating system (OS)-level firewall rules to block all ingress traffic and allow only egress traffic. For example, if your server runs on Linux, you may use <code>iptables</code> to set up firewall rules:</p>
<ol>
<li>Check your current firewall rules.</li>
</ol>
<pre><code class="language-sh">sudo iptables -L&#10;</code></pre>
<ol start="2">
<li>Allow <code>localhost</code> to communicate with itself.</li>
</ol>
<pre><code class="language-sh">sudo iptables -A INPUT -i lo -j ACCEPT&#10;</code></pre>
<ol start="3">
<li>Allow already established connection and related traffic.</li>
</ol>
<pre><code class="language-sh">sudo iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT&#10;</code></pre>
<ol start="4">
<li>Allow new SSH connections.</li>
</ol>
<pre><code class="language-sh">sudo iptables -A INPUT -p tcp --dport ssh -j ACCEPT&#10;</code></pre>
<ol start="5">
<li>Drop all other ingress traffic.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/5344.md")
</aside>
<pre><code class="language-sh">sudo iptables -A INPUT -j DROP&#10;</code></pre>
<ol start="6">
<li>After setting the firewall rules, use this command to check the current <code>iptables</code> settings:</li>
</ol>
<pre><code class="language-sh">sudo iptables -L&#10;</code></pre>
<ol start="7">
<li>
<p>Run your tunnel and check that all configured services are still accessible to the outside world via the tunnel, but not via the external IP address of the server.</p>
</li>
<li>
<p>By default, rules you add via the <code>iptables</code> command are stored only in memory and do not persist on reboot. There are many different ways to save and reload your firewall rules, depending on your Linux distribution. For example, on Debian you can use the <a href="https://packages.debian.org/sid/iptables-persistent"><code>iptables-persistent</code></a> package:</p>
</li>
</ol>
<pre><code class="language-sh">sudo apt install iptables-persistent&#10;sudo netfilter-persistent save&#10;</code></pre>
<h2 id="test-connectivity">Test connectivity</h2>
<h3 id="test-with-dig">Test with dig</h3>
<p>To test your connectivity to Cloudflare, you can use the <code>dig</code> command to query the hostnames listed above. Note that <code>cloudflared</code> defaults to connecting with IPv4.</p>
<pre><code class="language-sh">dig A region1.v2.argotunnel.com&#10;</code></pre>
<pre><code class="language-sh">;; ANSWER SECTION:&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.167&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.67&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.57&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.107&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.27&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.7&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.227&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.47&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.37&#10;region1.v2.argotunnel.com. 86400 IN	A	198.41.192.77&#10;...&#10;</code></pre>
<pre><code class="language-sh">dig AAAA region1.v2.argotunnel.com&#10;</code></pre>
<pre><code class="language-sh">...&#10;;; ANSWER SECTION:&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::1&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::2&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::3&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::4&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::5&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::6&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::7&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::8&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::9&#10;region1.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a0::10&#10;...&#10;</code></pre>
<pre><code class="language-sh">dig A region2.v2.argotunnel.com&#10;</code></pre>
<pre><code class="language-sh">;; ANSWER SECTION:&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.13&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.193&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.33&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.233&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.53&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.63&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.113&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.73&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.43&#10;region2.v2.argotunnel.com. 86400 IN	A	198.41.200.23&#10;...&#10;</code></pre>
<pre><code class="language-sh">dig AAAA region2.v2.argotunnel.com&#10;</code></pre>
<pre><code class="language-sh">...&#10;;; ANSWER SECTION:&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::1&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::2&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::3&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::4&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::5&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::6&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::7&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::8&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::9&#10;region2.v2.argotunnel.com. 86400 IN	AAAA	2606:4700:a8::10&#10;...&#10;</code></pre>
<h3 id="test-with-powershell">Test with PowerShell</h3>
<p>On Windows, you can use PowerShell commands if <code>dig</code> is not available.</p>
<p>To test DNS:</p>
<pre><code class="language-powershell">Resolve-DnsName -Name _v2-origintunneld._tcp.argotunnel.com SRV&#10;</code></pre>
<pre><code class="language-txt">Name                                     Type   TTL   Section    NameTarget                     Priority Weight Port&#10;&#45;---                                     ----   ---   -------    ----------                     -------- ------ ----&#10;_v2-origintunneld._tcp.argotunnel.com       SRV    112   Answer     region2.v2.argotunnel.com         2        1      7844&#10;_v2-origintunneld._tcp.argotunnel.com       SRV    112   Answer     region1.v2.argotunnel.com         1        1      7844&#10;</code></pre>
<p>To test ports:</p>
<pre><code class="language-powershell">tnc region1.v2.argotunnel.com -port 443&#10;</code></pre>
<pre><code class="language-txt">ComputerName     : region1.v2.argotunnel.com&#10;RemoteAddress    : 198.41.192.227&#10;RemotePort       : 443&#10;InterfaceAlias   : Ethernet&#10;SourceAddress    : 10.0.2.15&#10;TcpTestSucceeded : True&#10;</code></pre>
<pre><code class="language-powershell">tnc region1.v2.argotunnel.com -port 7844&#10;</code></pre>
<pre><code class="language-txt">ComputerName     : region1.v2.argotunnel.com&#10;RemoteAddress    : 198.41.192.227&#10;RemotePort       : 7844&#10;InterfaceAlias   : Ethernet&#10;SourceAddress    : 10.0.2.15&#10;TcpTestSucceeded : True&#10;</code></pre>
