<p>We recommend following these best practices when you deploy Cloudflare Tunnel for clientless access.</p>
<h2 id="deploy-another-instance-of-cloudflared">Deploy another instance of cloudflared</h2>
<p>For an additional point of availability, add a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replica</a> to another host machine in your network.</p>
<h2 id="standardize-public-hostnames">Standardize public hostnames</h2>
<p>To make your applications easier to manage, standardize the public hostnames that you publish your applications on. Here are a few examples of how customers manage their public hostnames:</p>
<ul>
<li>Delegate a subdomain of your primary public website to use for internal applications (for example, <code>tools.dev.customer.com</code>).</li>
<li>If your internal DNS infrastructure is available for public use, register your internal primary DNS record on Cloudflare and use this domain for your public hostname routes. This allows you to present applications on identical private and public hostnames.</li>
<li>Specify some sort of internal logic that generates hostnames based on the type of tool you are connecting. For example, if you have a set of applications in a US-East datacenter allocated explicitly for production resources, you could create subdomains of <code>tools.us-east.prod.ztproject.com</code>.</li>
</ul>
<h2 id="configure-tls-verification">Configure TLS verification</h2>
<p>If your public hostname route serves an <code>HTTPS</code> application, keep TLS certificate verification enabled. If the service URL uses <code>localhost</code> or an IP address but the certificate covers a hostname, set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#originservername"><strong>Origin Server Name</strong></a> to the hostname covered by the certificate. If the origin uses a private certificate authority, set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#capool"><strong>CA Pool</strong></a>.</p>
<p>Turn on <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify"><strong>Disable TLS certificate verification</strong></a> only for temporary testing while you fix the certificate configuration. For a complete HTTPS origin decision tree, refer to <a href="/tunnel/troubleshooting/https-origins/">Troubleshoot HTTPS origins with Cloudflare Tunnel</a>.</p>
<h2 id="optional-add-host-header-to-accommodate-local-traffic-management-tools">(Optional) Add <code>Host</code> header to accommodate local traffic management tools</h2>
<p>If your target application sits behind a load balancer or similar, you may need to set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#httphostheader"><strong>HTTP Host Header</strong></a> to the service hostname. Load balancers in between the origin service and <code>cloudflared</code> can be difficult to troubleshoot, and you can typically resolve the issue by adding a request header to match the way that the load balancer typically identifies traffic.</p>
<h2 id="enable-tunnel-notifications">Enable tunnel notifications</h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/">Enable notifications</a> in the Cloudflare dashboard to monitor tunnel health.</p>
<h2 id="update-cloudflared">Update cloudflared</h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/">Update <code>cloudflared</code></a> regularly to get the latest features and bug fixes.</p>
