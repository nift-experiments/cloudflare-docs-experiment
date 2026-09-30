<p>By default, all DNS requests on the user device are resolved by Cloudflare's <a href="/1.1.1.1/">public DNS resolver</a> except for common top level domains used for local resolution (such as <code>localhost</code>). You can connect an internal DNS resolver to Cloudflare and use it to resolve non-publicly routed domains.</p>
<h2 id="configure-private-dns">Configure private DNS</h2>
<p>To resolve private DNS queries:</p>
<ol>
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">Connect your private network</a> with Cloudflare Tunnel.</p>
</li>
<li>
<p>Under <strong>Networking</strong> &gt; <strong>Routes</strong>, verify that the IP address of your internal DNS resolver is included in the tunnel.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5403.md")
</aside>
<ol start="3">
<li>
<p>Route specific DNS queries to your internal DNS resolver using one of the following options:</p>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Create a Local Domain Fallback entry</a> that points to the internal DNS resolver. For example, you can instruct the Cloudflare One Client to resolve all requests for <code>myorg.privatecorp</code> through an internal resolver at <code>10.0.0.25</code> rather than attempting to resolve this publicly.</li>
<li>Alternatively, <a href="/cloudflare-one/traffic-policies/resolver-policies/#create-a-resolver-policy">create a resolver policy</a> that points to the internal DNS resolver.
<a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver policies</a> provide similar functionality to Local Domain Fallback but occur in Cloudflare Gateway rather than on the local device. This option is recommended if you want more granular control over private DNS resolution. For example, you can ensure that all users in a specific geography use the private DNS server closest to them, ensure that specific conditions are met before resolving private DNS traffic, and apply <a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policies</a> to private DNS traffic.</li>
</ul>
</li>
<li>
<p><a href="/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy">Enable the Gateway proxy</a> for TCP and UDP.</p>
</li>
<li>
<p>Finally, ensure that your tunnel uses QUIC as the default <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol">transport protocol</a>. This will enable <code>cloudflared</code> to proxy UDP-based traffic which is required in most cases to resolve DNS queries.</p>
</li>
</ol>
<p>The Cloudflare One Client will now send DNS queries to your internal DNS resolver for resolution. To learn more, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-warp-client-handles-dns-requests">How the Cloudflare One Client handles DNS requests</a>.</p>
<h2 id="test-the-setup">Test the setup</h2>
<p>For testing, run a <code>dig</code> command for the internal DNS service:</p>
<pre><code class="language-sh">dig AAAA www.myorg.privatecorp&#10;</code></pre>
<p>The <code>dig</code> command will work because <code>myorg.privatecorp</code> was configured above as a fallback domain. If you skip that step, you can still force <code>dig</code> to use your private DNS resolver:</p>
<pre><code class="language-sh">dig @10.0.0.25 AAAA www.myorg.privatecorp&#10;</code></pre>
<p>Both <code>dig</code> commands will fail if the Cloudflare One Client is disabled on your end user's device.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Use the following troubleshooting strategies if you are running into issues while configuring private DNS with Cloudflare Tunnel.</p>
<ul>
<li>
<p>Ensure that <code>cloudflared</code> is connected to Cloudflare by visiting <strong>Networking</strong> &gt; <strong>Tunnels</strong> in the Cloudflare dashboard.</p>
</li>
<li>
<p>Ensure that <code>cloudflared</code> is running with the <code>quic</code> protocol (search for <code>Initial protocol quic</code> in its logs).</p>
</li>
<li>
<p>Ensure that the machine where <code>cloudflared</code> is running is allowed to egress via UDP to port 7844 to talk out to Cloudflare.</p>
</li>
<li>
<p>Ensure that end-user devices are enrolled into the Cloudflare One Client by visiting <a href="https://help.teams.cloudflare.com">https://help.teams.cloudflare.com</a>.</p>
</li>
<li>
<p>Double-check the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">order of precedence</a> for your <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>. Ensure that a more global Block or Allow policy will not supersede application-specific policies.</p>
</li>
<li>
<p>Check your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs">Gateway network logs</a> to see whether your UDP DNS resolutions are being allowed or blocked.</p>
</li>
<li>
<p>Ensure that your internal DNS resolver is available over a routable private IP address. You can check that by trying the <code>dig</code> command on your machine running <code>cloudflared</code>.</p>
</li>
<li>
<p>Check your set up by using <code>dig ... +tcp</code> to force the DNS resolution to use TCP instead of UDP.</p>
</li>
</ul>
