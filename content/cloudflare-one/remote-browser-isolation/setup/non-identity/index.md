<p>On-ramps are the methods used to route traffic from your network to Cloudflare for inspection. With Cloudflare One, you can isolate HTTP traffic from on-ramps such as <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints</a> (which your browser connects to via PAC files to send traffic through Gateway) or <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a> (formerly Magic WAN, which connects your network to Cloudflare through GRE or IPsec tunnels). Since these on-ramps do not require users to log in to the Cloudflare One Client, <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> are not supported.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5887.md")
</aside>
<h2 id="set-up-non-identity-browser-isolation">Set up non-identity browser isolation</h2>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install a Cloudflare certificate</a> on your devices.</li>
<li>Connect your infrastructure to Gateway using one of the following on-ramps:
<ul>
<li>Configure your browser to forward traffic to a Gateway proxy endpoint with <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a> (Proxy Auto-Configuration files that tell the browser which traffic to route through the proxy).</li>
<li>Connect your enterprise site router to Gateway with the <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">anycast GRE or IPsec tunnel on-ramp to Cloudflare WAN</a> (site-to-site encrypted tunnels between your network and Cloudflare).</li>
</ul>
</li>
<li>Enable non-identity browser isolation:
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</li>
<li>Turn on <strong>Allow isolated HTTP traffic when user identity is unknown</strong>.</li>
</ol>
</li>
<li>Build a non-identity <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">HTTP policy</a> to isolate websites in a remote browser.</li>
</ol>
