<p>Secure Web Gateway allows you to apply policies at the network level to control which websites and non-HTTP applications users can access. This is useful when you need to control traffic that is not web browsing — for example, blocking remote desktop connections or restricting file-transfer tools across your organization.</p>
<p>Network policies inspect individual TCP and UDP packets (the low-level data units that carry all Internet traffic), which means you can filter traffic that <a href="/cloudflare-one/traffic-policies/get-started/dns/">DNS</a> and <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP</a> policies cannot reach. DNS policies only see domain lookups, and HTTP policies only see web requests — network policies go deeper and can catch protocols like SSH (remote terminal access), RDP (remote desktop), and custom applications running on non-standard ports.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6594.md")
</aside>
<h2 id="1-connect-to-gateway"><ol>
<li>Connect to Gateway</li>
</ol></h2>
<h3 id="connect-devices">Connect devices</h3>
<p>To filter network traffic from a device such as a laptop or phone:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Install the Cloudflare One Client</a> on your device.</li>
<li>In the Cloudflare One Client Settings, log in to your organization's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/6595.md")
</div>.
3. (Optional) If you want to display a [custom block page](/cloudflare-one/reusable-components/custom-pages/gateway-block-page/) when users are blocked, [install the Cloudflare root certificate](/cloudflare-one/team-and-resources/devices/user-side-certificates/) on your device. Without the certificate, blocked users will see a generic browser connection error instead of an informative page.
4. [Enable the Gateway proxy](/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy) for TCP. The Gateway proxy is what routes your device's traffic through Cloudflare so network policies can inspect it — without it enabled, your policies will have no effect. Optionally, enable the UDP proxy to also inspect QUIC traffic (a newer protocol used by HTTP/3 connections) on port 443.
<h3 id="connect-private-networks">Connect private networks</h3>
<p>To filter traffic from private networks (internal corporate networks not exposed to the public Internet), refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel guide</a>.</p>
<h2 id="2-verify-device-connectivity"><ol start="2">
<li>Verify device connectivity</li>
</ol></h2>
<p>Verifying connectivity ensures that traffic from your device is actually flowing through Cloudflare before you build policies against it.</p>
<p>To verify your device is connected to Cloudflare One:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Under <strong>Log traffic activity</strong>, enable activity logging for all Network logs. This tells Cloudflare to record network-level traffic so you can confirm your device appears in the logs.</li>
<li>On your Cloudflare One Client device, open a browser and visit any website. This generates traffic that should appear in the logs.</li>
<li>Determine the <strong>Source IP</strong> for your device (the public-facing address Cloudflare sees for your connection):</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6598.md")
</div></div>
<ol start="5">
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Network logs</strong>. Before building network policies, make sure you see network logs from the Source IP assigned to your device.</li>
</ol>
<p>If no logs appear after a few minutes, check two things: first, verify that the <a href="/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy">Gateway proxy is turned on</a>. Second, confirm that the device is enrolled in your Zero Trust organization by checking the Cloudflare One Client connection status.</p>
<h2 id="3-create-your-first-network-policy"><ol start="3">
<li>Create your first network policy</li>
</ol></h2>
<p>A network policy has two parts: a matcher that selects which traffic to act on (for example, all packets destined for port 22, the default port for SSH) and an action that decides what to do with it (for example, block the connection).</p>
<p>To create a new network policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6601.md")
</div></div>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/network-policies/">network policies</a>.</p>
<h2 id="4-add-optional-policies"><ol start="4">
<li>Add optional policies</li>
</ol></h2>
<p>Refer to our list of <a href="/cloudflare-one/traffic-policies/network-policies/common-policies">common network policies</a> for policies you may want to create. Common additions include blocking traffic to specific IP ranges, restricting access to non-standard ports (ports other than well-known ones like 80 for HTTP and 443 for HTTPS), and using protocol detection to identify applications like BitTorrent based on their traffic patterns rather than port numbers alone.</p>
