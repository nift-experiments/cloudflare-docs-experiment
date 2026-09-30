<p>VPC Networks allow your Workers to access any service in your private network without pre-registering individual hosts or ports. You can bind to a specific <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a> to reach any service behind that tunnel, or bind to <a href="/mesh/">Cloudflare Mesh</a> to reach any Mesh node, client device, subnet route or hostname route announced through Cloudflare Tunnel or Mesh, or destination reachable through a <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramp (GRE, IPsec, or CNI).</p>
<p>At runtime, the URL you pass to <code>fetch()</code> or the address you pass to <code>connect()</code> determines the destination — any hostname or IP address reachable through the bound Cloudflare Tunnel or through Cloudflare Mesh. Use <code>fetch()</code> for HTTP traffic, and <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> for raw TCP connections (Redis, MQTT, custom protocols, and other non-HTTP services). This differs from <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a>, which require you to create a separate binding for each target host and port combination.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15896.md")
</aside>
<h2 id="bind-to-a-cloudflare-tunnel">Bind to a Cloudflare Tunnel</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15895.md")
</aside>
<p>Reference a specific Cloudflare Tunnel directly by its UUID:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15897.md")
</div>
<p>The <code>remote</code> flag must be set to <code>true</code> to enable remote bindings during local development.</p>
<h2 id="bind-to-cloudflare-mesh">Bind to Cloudflare Mesh</h2>
<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) connects your services, devices, and Workers through Cloudflare's global network. When you bind a Worker to Cloudflare Mesh using <code>network_id: &quot;cf1:network&quot;</code>, your Worker can reach:</p>
<ul>
<li>Any Mesh node or client device in your account</li>
<li>Subnet routes and hostname routes announced through Cloudflare Tunnel or Cloudflare Mesh</li>
<li>Destinations reachable through <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramps (GRE, IPsec, and CNI)</li>
<li>Public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> — with your existing Zero Trust traffic policies enforced and traffic logged in DNS, HTTP, and Network logs</li>
</ul>
<p>All of this without specifying a particular Cloudflare Tunnel UUID.</p>
<p>Use <code>cf1:network</code> when:</p>
<ul>
<li>Your Workers need to reach private services across multiple Cloudflare Tunnels, Mesh nodes, or Cloudflare WAN on-ramps</li>
<li>You want to access your entire private network from a Worker without managing individual Cloudflare Tunnel bindings</li>
<li>Your private network topology may change (new connections, new nodes, new routes) and you do not want to update Worker configuration each time</li>
<li>You want Worker egress to public destinations to flow through Cloudflare Gateway for policy enforcement and visibility</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15894.md")
</aside>
<p>Bind to Cloudflare Mesh using <code>network_id: &quot;cf1:network&quot;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15898.md")
</div>
<h2 id="runtime-usage">Runtime usage</h2>
<h3 id="http-via-fetch">HTTP via <code>fetch()</code></h3>
<p>Access any HTTP service in your network at runtime using <code>fetch()</code>:</p>
<pre><code class="language-typescript">export default {&#10;	async fetch(request: Request, env: Env) {&#10;		// Access a service by private IP&#10;		const response = await env.MY_VPC.fetch(&quot;http://10.0.1.50/data&quot;);&#10;&#10;		// Access another service on a different port&#10;		const dbResponse = await env.MY_VPC.fetch(&quot;http://10.0.5.42:5432&quot;);&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<p>When a VPC Network cannot establish a connection to your target service, <code>fetch()</code> throws an exception.</p>
<h3 id="tcp-via-connect">TCP via <code>connect()</code></h3>
<p>Open raw TCP connections to any private destination using <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a>. This is useful for non-HTTP protocols like Redis, Memcached, MQTT, or custom binary protocols:</p>
<pre><code class="language-typescript">export default {&#10;	async fetch(request: Request, env: Env) {&#10;		// Open a TCP connection to a private Redis instance&#10;		const socket = await env.MY_VPC.connect(&quot;10.0.1.50:6379&quot;);&#10;&#10;		// Write a Redis PING command&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<p>When a VPC Network cannot establish a TCP connection, <code>connect()</code> throws an exception.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15893.md")
</aside>
<h2 id="vpc-networks-vs-vpc-services">VPC Networks vs VPC Services</h2>
<p>VPC Networks and <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a> both connect Workers to private infrastructure, but they make different trade-offs.</p>
<ul>
<li><strong>Use VPC Services</strong> when you have a known set of targets and want each binding scoped to a specific host and port.</li>
<li><strong>Use VPC Networks</strong> when you need broader access — an entire Cloudflare Tunnel or all of Cloudflare Mesh — and want the URL in your <code>fetch()</code> call to control routing at runtime.</li>
</ul>
<p>The following table summarizes the differences:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>VPC Networks</th>
<th>VPC Services</th>
</tr>
</thead>
<tbody>
<tr>
<td>Scope</td>
<td>A single Cloudflare Tunnel, or Cloudflare Mesh and Cloudflare WAN routes</td>
<td>Specific host + port</td>
</tr>
<tr>
<td>Configuration</td>
<td><code>tunnel_id</code> (single Cloudflare Tunnel) or <code>cf1:network</code> (account-wide)</td>
<td><code>service_id</code></td>
</tr>
<tr>
<td>Protocols</td>
<td>HTTP (<code>fetch()</code>) and TCP (<code>connect()</code>)</td>
<td>HTTP (<code>fetch()</code>) or TCP (via <a href="/hyperdrive/">Hyperdrive</a>)</td>
</tr>
<tr>
<td>Service registration</td>
<td>Not required</td>
<td>Required for each target</td>
</tr>
<tr>
<td>Use when</td>
<td>Dynamic discovery, network-wide access, reaching services across your account</td>
<td>Fixed, cataloged services</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Set up <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/mesh/get-started/">Set up Cloudflare Mesh</a></li>
<li><a href="/cloudflare-wan/get-started/">Set up Cloudflare WAN</a></li>
<li>Try the <a href="/workers-vpc/examples/connect-to-cloudflare-mesh/">Connect Workers to Cloudflare Mesh</a> example</li>
<li>Learn about the <a href="/workers-vpc/api/">Workers Binding API</a></li>
</ul>
