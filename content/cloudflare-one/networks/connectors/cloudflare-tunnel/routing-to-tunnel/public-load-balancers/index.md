<p>A <a href="/load-balancing/load-balancers/">public load balancer</a> allows you to distribute traffic across the servers that are running your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">published applications</a>.</p>
<p>When you add a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-publish-an-application">published application route</a> to your Cloudflare Tunnel, Cloudflare generates a subdomain of <code>cfargotunnel.com</code> with the UUID of the created tunnel. You can add the application to a load balancer pool by using <code>&lt;UUID&gt;.cfargotunnel.com</code> as the <a href="/load-balancing/understand-basics/load-balancing-components/#endpoints">endpoint address</a> and specifying the application hostname (<code>app.example.com</code>) in the <a href="/load-balancing/additional-options/override-http-host-headers/">endpoint host header</a>. Load Balancer does not support directly adding <code>app.example.com</code> as an endpoint if the service is behind Cloudflare Tunnel.</p>
<h2 id="create-a-public-load-balancer">Create a public load balancer</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>A Cloudflare Tunnel with a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-publish-an-application">published application route</a></li>
</ul>
<h3 id="create-a-load-balancer">Create a load balancer</h3>
<p>To create a load balancer for Cloudflare Tunnel published applications:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create load balancer</strong>, then select <strong>Public load balancer</strong>.</li>
<li>Under <strong>Select website</strong>, select the domain of your published application route.</li>
<li>On the <strong>Hostname</strong> page, enter a hostname for the load balancer (for example, <code>lb.example.com</code>).</li>
<li>On the <strong>Pools</strong> page, select <strong>Create a pool</strong> and enter a descriptive name.</li>
<li>Add a tunnel endpoint with the following values:
<ul>
<li><strong>Endpoint Name</strong>: Name of the server running the application</li>
<li><strong>Endpoint Address</strong>: <code>&lt;UUID&gt;.cfargotunnel.com</code> (find the Tunnel ID in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Networking</strong> &gt; <strong>Tunnels</strong>)</li>
<li><strong>Header value</strong>: Hostname of your published application route (for example, <code>app.example.com</code>)</li>
<li><strong>Weight</strong>: <code>1</code> (if only one endpoint)</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5281.md")
</aside>
<ol start="7">
<li>Choose a <strong>Fallback pool</strong>. Refer to <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policies</a> for routing options.</li>
<li>(Recommended) On the <strong>Monitors</strong> page, attach a monitor to the endpoint. For an HTTP or HTTPS application, create an HTTPS monitor:
<ul>
<li><strong>Type</strong>: <em>HTTPS</em></li>
<li><strong>Path</strong>: <code>/</code></li>
<li><strong>Port</strong>: <code>443</code></li>
<li><strong>Expected Code(s)</strong>: <code>200</code></li>
<li><strong>Header Name</strong>: <code>Host</code></li>
<li><strong>Value</strong>: <code>app.example.com</code></li>
</ul>
</li>
<li>Save and deploy the load balancer.</li>
</ol>
<p>To test, access your application using the load balancer hostname (<code>lb.example.com</code>).</p>
<p>Refer to the <a href="/load-balancing/">Load Balancing documentation</a> for more details on load balancer settings and configurations.</p>
<h3 id="optional-cloudflare-settings">Optional Cloudflare settings</h3>
<p>The application will default to the Cloudflare settings for the load balancer hostname, including <a href="/rules/">Rules</a>, <a href="/cache/how-to/cache-rules/">Cache Rules</a> and <a href="/waf/">WAF rules</a>. You can change the settings for your hostname in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<h2 id="common-architectures">Common architectures</h2>
<p>Review common load balancing configurations for published applications behind Cloudflare Tunnel.</p>
<h3 id="one-app-per-load-balancer">One app per load balancer</h3>
<p>For this example, assume we have a web application that runs on servers in two different data centers. We want to connect the application to Cloudflare so that users can access the application from anywhere in the world. Additionally, we want Cloudflare to load balance between the servers such that if the primary server fails, the secondary server receives all traffic.</p>
<pre><code class="language-mermaid">graph LR&#10;		subgraph LB[&quot;Public load balancer &lt;br&gt; app.example.com &quot;]&#10;			subgraph P1[Pool 2]&#10;				E1([&quot;**Endpoint:** &amp;lt;UUID_1&amp;gt;.cfargotunnel.com&lt;br&gt; **Host header**: server2.example.com&quot;])&#10;			end&#10;			subgraph P2[Pool 1]&#10;				E2([&quot;**Endpoint:** &amp;lt;UUID_2&amp;gt;.cfargotunnel.com&lt;br&gt; **Host header**: server1.example.com&quot;])&#10;			end&#10;		end&#10;		R@{ shape: text, label: &quot;app.example.com&quot; }&#10;		R--&gt; LB&#10;    P1 -- Tunnel 1 --&gt; cf1&#10;    P2 -- Tunnel 2 --&gt; cf2&#10;		subgraph D2[Private network]&#10;			subgraph r1[Region eu-west-1]&#10;			cf1@{ shape: processes, label: &quot;cloudflared &lt;br&gt; **Route:** server2.example.com&quot; }&#10;			S1([&quot;Server 2&lt;br&gt; 10.0.0.1:80&quot;])&#10;			cf1--&gt;S1&#10;			end&#10;			subgraph r2[Region us-east-1]&#10;			cf2@{ shape: processes, label: &quot;cloudflared &lt;br&gt; **Route:** server1.example.com&quot; }&#10;			S3([&quot;Server 1 &lt;br&gt; 10.0.0.2:80&quot;])&#10;			cf2--&gt;S3&#10;			end&#10;		end&#10;&#10;		style r1 stroke-dasharray: 5 5&#10;		style r2 stroke-dasharray: 5 5&#10;</code></pre>
<p>As shown in the diagram, a typical setup includes:</p>
<ul>
<li>A dedicated Cloudflare Tunnel per data center.</li>
<li>One load balancer pool per tunnel. The load balancer hostname is set to the user-facing application hostname (<code>app.example.com</code>).</li>
<li>One load balancer endpoint per pool. The endpoint host header is set to the <code>cloudflared</code> published application hostname (<code>server1.example.com</code>)</li>
<li>At least two <code>cloudflared</code> <a href="#session-affinity-and-replicas">replicas</a> per tunnel in their respective data centers, in case a <code>cloudflared</code> host machine goes down.</li>
</ul>
<p>Users can now connect to the application using the load balancer hostname (<code>app.example.com</code>). Note that this configuration is only valid for <a href="/load-balancing/load-balancers/common-configurations/#active---passive-failover">Active-Passive failover</a>, since each pool only supports one endpoint per tunnel.</p>
<h3 id="multiple-apps-per-load-balancer">Multiple apps per load balancer</h3>
<p>The following diagram illustrates how to steer traffic to two different applications on a private network using a single load balancer.</p>
<pre><code class="language-mermaid">graph LR&#10;		subgraph LB[&quot;Public load balancer &lt;br&gt; lb.example.com&quot;]&#10;			subgraph P1[Pool for App 1]&#10;				E1([&quot;**Endpoint:** &amp;lt;UUID_1&amp;gt;.cfargotunnel.com&lt;br&gt; **Host header**: app1.example.com&quot;])&#10;				E2([&quot;**Endpoint:** &amp;lt;UUID_2&amp;gt;.cfargotunnel.com&lt;br&gt; **Host header**: app1.example.com&quot;])&#10;			end&#10;			subgraph P2[Pool for App 2]&#10;				E3([&quot;**Endpoint:** &amp;lt;UUID_1&amp;gt;.cfargotunnel.com&lt;br&gt; **Host header**: app2.example.com&quot;])&#10;				E4([&quot;**Endpoint:** &amp;lt;UUID_2&amp;gt;.cfargotunnel.com&lt;br&gt; **Host header**: app2.example.com&quot;])&#10;			end&#10;		end&#10;		R@{ shape: text, label: &quot;app1.example.com &lt;br&gt; app2.example.com&quot; }&#10;		R--&gt; LB&#10;    E1 -- Tunnel 1 --&gt;cf1&#10;		E3 -- Tunnel 1 --&gt; cf1&#10;		E2 -- Tunnel 2 --&gt; cf2&#10;		E4 -- Tunnel 2 --&gt; cf2&#10;&#10;		subgraph N[Private network]&#10;			cf2[cloudflared &lt;br&gt; **Route:** app1.example.com &lt;br&gt; **Route:** app2.example.com]&#10;			S3([&quot;App 1 &lt;br&gt; 10.0.0.1:80&quot;])&#10;			cf2--&gt;S3&#10;			cf2--&gt;S1&#10;			cf1[cloudflared &lt;br&gt; **Route:** app1.example.com &lt;br&gt; **Route:** app2.example.com]&#10;			S1([&quot;App 2 &lt;br&gt; 10.0.0.2:80&quot;])&#10;			cf1--&gt;S1&#10;			cf1--&gt;S3&#10;		end&#10;</code></pre>
<p>This load balancing setup includes:</p>
<ul>
<li>Two Cloudflare Tunnels with identical routes to both applications.</li>
<li>One load balancer pool per application.</li>
<li>Each load balancer pool has an endpoint per tunnel.</li>
<li>A <a href="#dns-records">DNS record</a> for each application that points to the load balancer hostname.</li>
</ul>
<p>Users can now access all applications through the load balancer. Since there are multiple tunnel endpoints per pool, this configuration supports <a href="/load-balancing/load-balancers/common-configurations/#active---active-failover">Active-Active Failover</a>. Active-Active uses all available endpoints in the pool to process requests simultaneously, providing better performance and scalability by load balancing traffic across them.</p>
<h4 id="dns-records">DNS records</h4>
<p>When you configure a published application route via the dashboard, Cloudflare will automatically generate a <code>CNAME</code> DNS record that points the application hostname (<code>app1.example.com</code>) to the tunnel subdomain (<code>&lt;UUID&gt;.cfargotunnel.com</code>). You can <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">edit these DNS records</a> so that they point to the load balancer hostname instead.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5280.md")
</aside>
<p>Here is an example of what your DNS records will look like before and after setting up <a href="#multiple-apps-per-load-balancer">Multiple apps per load balancer</a>:</p>
<p><strong>Before</strong>:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td>CNAME</td>
<td>app1</td>
<td><code>&lt;UUID_1&gt;.cfargotunnel.com</code></td>
</tr>
<tr>
<td>CNAME</td>
<td>app2</td>
<td><code>&lt;UUID_1&gt;.cfargotunnel.com</code></td>
</tr>
<tr>
<td>CNAME</td>
<td>app1</td>
<td><code>&lt;UUID_2&gt;.cfargotunnel.com</code></td>
</tr>
<tr>
<td>CNAME</td>
<td>app2</td>
<td><code>&lt;UUID_2&gt;.cfargotunnel.com</code></td>
</tr>
</tbody>
</table>
<p><strong>After</strong>:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td>LB</td>
<td><code>lb.example.com</code></td>
<td>n/a</td>
</tr>
<tr>
<td>CNAME</td>
<td>app1</td>
<td><code>lb.example.com</code></td>
</tr>
<tr>
<td>CNAME</td>
<td>app2</td>
<td><code>lb.example.com</code></td>
</tr>
</tbody>
</table>
<h2 id="known-limitations">Known limitations</h2>
<h3 id="monitors-and-tcp-tunnel-origins">Monitors and TCP tunnel origins</h3>
<p>TCP monitors are not supported for tunnel endpoints. Instead, create a health check endpoint on the <code>cloudflared</code> host and use an HTTPS monitor. For example, you can use <code>cloudflared</code> to return a fixed HTTP status response:</p>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-publish-an-application">Add a published application route</a> for the health check:
<ul>
<li><strong>Hostname</strong>: <code>health-check.example.com</code></li>
<li><strong>Service Type</strong>: <em>HTTP_STATUS</em></li>
<li><strong>HTTP Status Code</strong>: <code>200</code></li>
</ul>
</li>
<li><a href="/load-balancing/monitors/create-monitor/">Create a monitor</a> with these settings:
<ul>
<li><strong>Type</strong>: <em>HTTPS</em></li>
<li><strong>Path</strong>: <code>/</code></li>
<li><strong>Port</strong>: <code>443</code></li>
<li><strong>Expected Code(s)</strong>: <code>200</code></li>
<li><strong>Header Name</strong>: <code>Host</code></li>
<li><strong>Value</strong>: <code>health-check.example.com</code></li>
</ul>
</li>
</ol>
<p>This monitor verifies that <code>cloudflared</code> is reachable. It does not check whether the upstream service is accepting requests.</p>
<h3 id="session-affinity-and-replicas">Session affinity and replicas</h3>
<p>The load balancer does not distinguish between <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> of the same tunnel. If you run the same tunnel UUID on two separate hosts, the load balancer treats both hosts as a single endpoint. To maintain <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a> between a client and a particular host, you will need to connect each host to Cloudflare using a different tunnel UUID.</p>
<h3 id="local-connection-preference">Local connection preference</h3>
<p>If you notice traffic imbalances across endpoints in different locations, you may need to adjust your load balancer configuration.</p>
<p>Cloudflare uses <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">Anycast routing</a> to direct end user requests to the nearest data center. <code>cloudflared</code> prefers to serve requests using connections in the same data center, which can affect how traffic is distributed across endpoints.</p>
<p>If you run <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas</a> on the same tunnel UUID, consider switching to separate tunnels for more granular control over <a href="/load-balancing/understand-basics/traffic-steering/">traffic steering</a>.</p>
