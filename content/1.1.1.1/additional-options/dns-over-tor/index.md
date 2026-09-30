<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1817.md")
</aside>
<p>When you send a standard DNS query, both your ISP and the DNS resolver can see your IP address and the domains you look up. Cloudflare's Tor onion service routes your DNS queries through the Tor network, which guarantees a significantly higher level of anonymity than making requests directly. The resolver never sees your IP address, and your ISP cannot determine that you attempted to resolve a domain name.</p>
<p>Read more about this service in <a href="https://blog.cloudflare.com/welcome-hidden-resolver/">this blog post</a>.</p>
<h2 id="setting-up-a-tor-client">Setting up a Tor client</h2>
<p>Unlike standard DNS modes where traffic is sent directly to an IP address, the Tor network routes traffic without exposing IP addresses. This means all connections to the hidden resolver must go through a Tor client.</p>
<p>Before you start, head to the <a href="https://www.torproject.org/download/download.html.en">Tor Project website</a> to download and install a Tor client. If you use the Tor Browser, it will automatically start a <a href="https://en.wikipedia.org/wiki/SOCKS">SOCKS proxy</a> at <code>127.0.0.1:9150</code>.</p>
<p>If you use Tor from the command line, create the following configuration file:</p>
<pre><code class="language-txt">SOCKSPort 9150&#10;</code></pre>
<p>Then you can run tor with:</p>
<pre><code class="language-sh">tor -f tor.conf&#10;</code></pre>
<p>Also, if you use the Tor Browser, you can head to the resolver's address to see the usual 1.1.1.1 page:</p>
<pre><code class="language-txt">https://dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion/&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/1816.md")
</aside>
<p>If you ever forget 1.1.1.1's address, use cURL to retrieve it:</p>
<pre><code class="language-sh">curl -sI https://tor.cloudflare-dns.com | grep -i alt-svc&#10;</code></pre>
<pre><code class="language-sh">alt-svc: h2=&quot;dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion:443&quot;; ma=315360000; persist=1&#10;</code></pre>
<h2 id="setting-up-a-local-dns-proxy-using-socat">Setting up a local DNS proxy using socat</h2>
<p>Not all DNS clients support connecting to the Tor network directly. The <a href="http://www.dest-unreach.org/socat/"><code>socat</code></a> utility bridges this gap by forwarding local ports through the Tor proxy, so any DNS-speaking software can reach the hidden resolver.</p>
<h3 id="dns-over-tcp-tls-and-https">DNS over TCP, TLS, and HTTPS</h3>
<p>The hidden resolver listens on TCP port 53 (DNS over TCP) and port 853 (DNS over TLS). After setting up a Tor proxy, run the following <code>socat</code> command as a privileged user, setting <code>PORT</code> to 53 or 853 depending on your protocol:</p>
<pre><code class="language-sh">PORT=853; socat TCP4-LISTEN:${PORT},reuseaddr,fork SOCKS4A:127.0.0.1:dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion:${PORT},socksport=9150&#10;</code></pre>
<p>From here, you can follow the regular guide for <a href="/1.1.1.1/setup/">setting up 1.1.1.1</a>, except you should always use <code>127.0.0.1</code> instead of <code>1.1.1.1</code>. If you need to access the proxy from another device, replace <code>127.0.0.1</code> in the <code>socat</code> command with your local IP address.</p>
<h3 id="dns-over-https">DNS over HTTPS</h3>
<p><a href="https://blog.cloudflare.com/welcome-hidden-resolver/">As explained in the blog post</a>, the preferred method is DNS over HTTPS (DoH), which encrypts the entire DNS query within an HTTPS connection. To set it up:</p>
<ol>
<li>
<p>Download <code>cloudflared</code> by following the guide for <a href="/1.1.1.1/encryption/dns-over-https/dns-over-https-client/">connecting to 1.1.1.1 using DNS over HTTPS clients</a>.</p>
</li>
<li>
<p>Start a Tor SOCKS proxy and use <code>socat</code> to forward port TCP:443 to localhost:</p>
</li>
</ol>
<pre><code class="language-sh">socat TCP4-LISTEN:443,reuseaddr,fork SOCKS4A:127.0.0.1:dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion:443,socksport=9150&#10;</code></pre>
<ol start="3">
<li>Instruct your machine to treat the <code>.onion</code> address as localhost:</li>
</ol>
<pre><code class="language-bash">cat &lt;&lt; EOF &gt;&gt; /etc/hosts&#10;127.0.0.1 dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion&#10;EOF&#10;</code></pre>
<p>If you run this command more than once, remove duplicate entries from <code>/etc/hosts</code> to avoid conflicts.</p>
<ol start="4">
<li>Finally, start a local DNS over UDP daemon:</li>
</ol>
<pre><code class="language-sh">cloudflared proxy-dns --upstream &quot;https://dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion/dns-query&quot;&#10;</code></pre>
<pre><code class="language-sh">INFO[0000] Adding DNS upstream                           url=&quot;https://dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion/dns-query&quot;&#10;INFO[0000] Starting DNS over HTTPS proxy server          addr=&quot;dns://localhost:53&quot;&#10;INFO[0000] Starting metrics server                       addr=&quot;127.0.0.1:35659&quot;&#10;</code></pre>
