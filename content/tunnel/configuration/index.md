<p>This page covers the most common configuration options for <code>cloudflared</code> tunnels, including high availability, firewall rules, and runtime parameters.</p>
<h2 id="replicas-and-high-availability">Replicas and high availability</h2>
<p>When you run a tunnel, <code>cloudflared</code> establishes four outbound-only, <a href="/ssl/post-quantum-cryptography/">post-quantum encrypted</a> connections to at least two distinct Cloudflare data centers. If any connection, server, or data center goes offline, your resources remain available.</p>
<p>A replica is an additional <code>cloudflared</code> instance that points to the same tunnel. Each replica creates four new connections, providing additional ingress points to your origin. You can run up to 25 replicas (100 connections) per tunnel. Traffic routes to the geographically closest replica.</p>
<pre><code class="language-mermaid">graph LR&#10;    C((Cloudflare))&#10;    subgraph E[Your network]&#10;        cf1[&quot;cloudflared &lt;br&gt; (Replica for tunnel-01)&quot;]&#10;        cf2[&quot;cloudflared &lt;br&gt; (Replica for tunnel-01)&quot;]&#10;        S1[Application]&#10;        cf1--&gt;S1&#10;        cf2--&gt;S1&#10;    end&#10;    C -- &quot;Connections x 4 &lt;br&gt;&quot;--&gt; cf1&#10;    C --&gt; cf1&#10;    C --&gt; cf1&#10;    C --&gt; cf1&#10;    C -- Connections x 4--&gt; cf2&#10;    C --&gt; cf2&#10;    C --&gt; cf2&#10;    C --&gt; cf2&#10;</code></pre>
<h3 id="deploy-a-replica">Deploy a replica</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14956.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14953.md")
</aside>
<h2 id="firewall-rules">Firewall rules</h2>
<p><code>cloudflared</code> connects outbound to Cloudflare on port <code>7844</code>. Your firewall must allow egress to the following destinations. Block all ingress traffic for a positive security model — only the services in your tunnel configuration will be exposed.</p>
<h3 id="required-ports">Required ports</h3>
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
<details class="nb-details"><summary>US region IPs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14957.md")
</div></details>
<details class="nb-details"><summary>FedRAMP High IPs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14958.md")
</div></details>
<details class="nb-details"><summary>SNI-enforcing firewalls</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14959.md")
</div></details>
<details class="nb-details"><summary>Optional port 443 destinations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14960.md")
</div></details>
<p>To verify your firewall allows tunnel traffic, refer to <a href="/tunnel/troubleshooting/#connection-errors">Connection errors</a>.</p>
<h2 id="run-parameters">Run parameters</h2>
<p>These flags apply to the <code>cloudflared tunnel run</code> command. They control how the tunnel runs on your operating system.</p>
<p>The most commonly used parameters:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/tunnel/reference/run-parameters/#loglevel"><code>--loglevel</code></a></td>
<td><code>info</code></td>
<td>Log verbosity: <code>debug</code>, <code>info</code>, <code>warn</code>, <code>error</code>, <code>fatal</code></td>
</tr>
<tr>
<td><a href="/tunnel/reference/run-parameters/#logfile"><code>--logfile</code></a></td>
<td>stdout</td>
<td>Path to write log output</td>
</tr>
<tr>
<td><a href="/tunnel/reference/run-parameters/#metrics"><code>--metrics</code></a></td>
<td><code>127.0.0.1:20241</code>–<code>20245</code></td>
<td>Prometheus metrics endpoint address (first available port in range)</td>
</tr>
<tr>
<td><a href="/tunnel/reference/run-parameters/#protocol"><code>--protocol</code></a></td>
<td><code>auto</code></td>
<td>Connection protocol: <code>auto</code>, <code>quic</code>, <code>http2</code></td>
</tr>
<tr>
<td><a href="/tunnel/reference/run-parameters/#region"><code>--region</code></a></td>
<td>global</td>
<td>Route through US-only data centers with <code>us</code></td>
</tr>
<tr>
<td><a href="/tunnel/reference/run-parameters/#token"><code>--token</code></a></td>
<td>—</td>
<td>Tunnel token (remotely-managed tunnels)</td>
</tr>
</tbody>
</table>
<p>The following example shows how to manually run a tunnel with configuration flags:</p>
<pre><code class="language-sh">cloudflared tunnel --loglevel info --logfile /var/log/cloudflared/cloudflared.log run --token &lt;TOKEN VALUE&gt;&#10;</code></pre>
<p>For the complete list of run parameters and instructions on how to add them to a tunnel service, refer to <a href="/tunnel/reference/run-parameters/">Run parameters</a>.</p>
<h2 id="origin-parameters">Origin parameters</h2>
<p>Origin configuration parameters control how <code>cloudflared</code> proxies traffic to your origin server.</p>
<p>The most commonly used parameters:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/tunnel/reference/origin-parameters/#originservername"><code>originServerName</code></a></td>
<td><code>&quot;&quot;</code></td>
<td>Hostname expected from origin certificate</td>
</tr>
<tr>
<td><a href="/tunnel/reference/origin-parameters/#notlsverify"><code>noTLSVerify</code></a></td>
<td><code>false</code></td>
<td>Disable TLS certificate verification</td>
</tr>
<tr>
<td><a href="/tunnel/reference/origin-parameters/#httphostheader"><code>httpHostHeader</code></a></td>
<td><code>&quot;&quot;</code></td>
<td>Override HTTP Host header</td>
</tr>
<tr>
<td><a href="/tunnel/reference/origin-parameters/#connecttimeout"><code>connectTimeout</code></a></td>
<td><code>30s</code></td>
<td>TCP connection timeout to origin</td>
</tr>
</tbody>
</table>
<p>For the complete list of origin parameters and setup instructions, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>
<h2 id="permissions">Permissions</h2>
<p>You can scope Cloudflare member permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances instead of granting account-wide access. This lets you delegate management of specific Tunnels — for example, letting an application team manage one Tunnel without exposing the rest of your account.</p>
<p>Refer to <a href="/tunnel/guides/granular-permissions/">Granular permissions</a>.</p>
