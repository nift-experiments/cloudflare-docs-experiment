<p>A DoH client is a software that runs on your device and sends DNS queries to a resolver like 1.1.1.1 over an encrypted HTTPS connection. Once configured, the client handles DNS resolution for your device or network.</p>
<h2 id="cloudflare-warp-client">Cloudflare WARP client</h2>
<p>Refer to <a href="/warp-client/">WARP client</a> for guidance on WARP modes and get-started information for different <a href="/warp-client/get-started/">operating systems</a>.</p>
<h2 id="dnscrypt-proxy">DNSCrypt-Proxy</h2>
<p><a href="https://dnscrypt.info">DNSCrypt-Proxy</a> 2.0+ supports DoH out of the box. It supports both 1.1.1.1 and other services. It also includes more advanced features, such as load balancing and local filtering.</p>
<ol>
<li>
<p><a href="https://github.com/DNSCrypt/dnscrypt-proxy/wiki/installation">Install DNSCrypt-Proxy</a>.</p>
</li>
<li>
<p>Verify that <code>dnscrypt-proxy</code> is installed and the version is 2.0 or later:</p>
</li>
</ol>
<pre><code class="language-sh">dnscrypt-proxy -version&#10;</code></pre>
<pre><code class="language-sh">2.0.8&#10;</code></pre>
<ol start="3">
<li>Set up the configuration file using the <a href="https://github.com/DNSCrypt/dnscrypt-proxy/wiki/installation#setting-up-dnscrypt-proxy">official instructions</a>, and add <code>cloudflare</code> and <code>cloudflare-ipv6</code> to the server list in <code>dnscrypt-proxy.toml</code>:</li>
</ol>
<pre><code class="language-toml">server_names = [&#x27;cloudflare&#x27;, &#x27;cloudflare-ipv6&#x27;]&#10;</code></pre>
<ol start="4">
<li>Make sure that nothing else is running on <code>localhost:53</code> (port <code>53</code> is the standard DNS port on your local machine), and check that everything works as expected:</li>
</ol>
<pre><code class="language-sh">dnscrypt-proxy -resolve cloudflare-dns.com&#10;</code></pre>
<pre><code class="language-sh">Resolving [cloudflare-dns.com]&#10;&#10;Domain exists:  yes, 3 name servers found&#10;Canonical name: cloudflare-dns.com.&#10;IP addresses:   2400:cb00:2048:1::6810:6f19, 2400:cb00:2048:1::6810:7019, 104.16.111.25, 104.16.112.25&#10;TXT records:    -&#10;Resolver IP:    172.68.140.217&#10;</code></pre>
<ol start="5">
<li>Register it as a system service so that it starts automatically when your device boots. Follow the <a href="https://github.com/DNSCrypt/dnscrypt-proxy/wiki/installation">DNSCrypt-Proxy installation instructions</a>.</li>
</ol>
