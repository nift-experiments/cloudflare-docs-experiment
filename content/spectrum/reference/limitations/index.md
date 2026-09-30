<p>The following limitations apply to Spectrum applications.</p>
<h2 id="ipv4-hostname-quota">IPv4 hostname quota</h2>
<p>By default, an account is limited to <strong>10 unique Spectrum hostnames</strong> using Cloudflare-managed IPv4 addresses, across all zones on the account. Each hostname is backed by a dedicated IPv4 address, and this quota is applied at the account level — not per zone.</p>
<p>IPv6-only Spectrum applications do not count against this quota.</p>
<p>If you need more than 10 IPv4-backed Spectrum hostnames, you can:</p>
<ul>
<li><strong>Use <a href="/spectrum/about/byoip/">BYOIP</a></strong> — bring your own IP space so Spectrum applications are not constrained by the default shared-IPv4 allocation.</li>
<li><strong>Use IPv6-only Spectrum applications</strong> — IPv6 addresses are not subject to the same scarcity as IPv4.</li>
<li><strong>CNAME multiple subdomains to a single Spectrum application</strong> — point several DNS-only (gray-clouded) <code>CNAME</code> records at one Spectrum application hostname. This works only when those hostnames share the same origin (one origin per application).</li>
<li><strong>Use <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a></strong> — configure the Spectrum application as the target (fallback origin) for Custom Hostnames.</li>
</ul>
<p>Contact your account team if you expect to exceed the quota.</p>
<h2 id="https">HTTPS</h2>
<p>At the moment, HTTPS applications do not support HTTP/3.</p>
<h2 id="udp">UDP</h2>
<p>Cloudflare does not support packet fragmentation for UDP packets. If packets are fragmented, they will be dropped at Cloudflare’s edge.</p>
<p>Spectrum UDP applications are supported with <a href="/spectrum/about/byoip/">BYOIP</a>, including <a href="/byoip/service-bindings/cdn-and-spectrum/">CDN and Spectrum service bindings</a>. They are not currently supported with <a href="/byoip/service-bindings/">Magic Transit service bindings</a>.</p>
<h2 id="minecraft">Minecraft</h2>
<p>Minecraft Java Edition is supported but Minecraft Bedrock Edition is not supported.</p>
<h2 id="universal-ssl">Universal SSL</h2>
<p><a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> is not compatible with Cloudflare Spectrum. Use either an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a> or a <a href="/ssl/edge-certificates/custom-certificates/">custom certificate</a> instead.</p>
<h2 id="private-network-load-balancing">Private Network Load Balancing</h2>
<p>When using <a href="/load-balancing/private-network/#on-ramps">Spectrum</a> as an on-ramp into Private Network Load Balancing, the <a href="/spectrum/how-to/enable-proxy-protocol/">proxy protocol</a> setting in Spectrum is not supported. This applies regardless of the <a href="/load-balancing/private-network/">off-ramp</a> used to reach your private origin, including Cloudflare WAN and Cloudflare Tunnel.</p>
<h2 id="cloudflare-tunnel">Cloudflare Tunnel</h2>
<p>Integrating Spectrum with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is only supported for <strong>HTTP/HTTPS</strong> applications. This is because Spectrum must upstream the request through the <a href="/spectrum/reference/layer-7-analytics/#the-overlap-layer-7-traffic-being-proxied-through-spectrum">Layer 7 CDN products</a> to reach the Tunnel service.</p>
<p>To correctly route traffic from Spectrum through a Cloudflare Tunnel, you must:</p>
<ol>
<li>Configure your Spectrum application with the type set to <strong>HTTP</strong> or <strong>HTTPS</strong>.</li>
<li>Point the Spectrum application's origin to a hostname that is already <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">routing traffic</a> through your Cloudflare Tunnel (for example, via a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/">DNS record</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/">Cloudflare Load Balancer</a>).</li>
</ol>
<p>Using a Spectrum application of any other type (for example, TCP) with a Cloudflare Tunnel origin directly is not supported. Pointing a Spectrum application's origin directly to your Tunnel's subdomain (<code>&lt;UUID&gt;.cfargotunnel.com</code>) is also not a valid configuration and will not work.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="alternative-l4-routing">Alternative L4 routing</h3>
@markup("md", "content/.markup/bodies/13865.md")
</aside>
<h2 id="listen-on-ports-configuration">Listen on ports configuration</h2>
<p>By default, Spectrum is configured to listen on all ports, which can raise concerns for security auditors. However, it is important to note that Spectrum will only proxy connections from edge ports that are specifically configured within Cloudflare.</p>
<p>When a TCP handshake is initiated to any port for a Spectrum IP, the handshake will always be completed. If there is a Spectrum application configured for the port, the connection will be proxied to origin. If no application is configured, the connection is immediately terminated and no origin connection will be opened.</p>
<p>Spectrum will only ever proxy traffic to an origin if there is a Spectrum application configured for that port.</p>
<h2 id="ip-access-control">IP access control</h2>
<p>Currently, <a href="/waf/custom-rules/">custom rules</a> do not work with Spectrum applications. Use <a href="/waf/tools/ip-access-rules/">IP Access rules</a> to allowlist, block, and challenge traffic for Spectrum applications based on the request's IP address, Autonomous System Number (ASN), or country.</p>
<p>Refer to <a href="/spectrum/reference/configuration-options/#ip-access-rules">Configuration options</a> for more information.</p>
