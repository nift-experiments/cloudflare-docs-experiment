<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-to-expose-public-applications">Looking to expose public applications?</h3>
@markup("md", "content/.markup/bodies/5155.md")
</aside>
<p>Cloudflare Tunnel provides you with a secure way to connect your resources to Cloudflare without a publicly routable IP address. With Tunnel, you do not send traffic to an external IP — instead, a lightweight daemon in your infrastructure (<code>cloudflared</code>) creates <a href="#outbound-only-connections">outbound-only connections</a> to Cloudflare's global network. Cloudflare Tunnel can connect HTTP web servers, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">SSH servers</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/">remote desktops</a>, and other protocols safely to Cloudflare. This way, your origins can serve traffic through Cloudflare without being vulnerable to attacks that bypass Cloudflare.</p>
<p>Refer to our <a href="/reference-architecture/architectures/sase/">reference architecture</a> for details on how to implement Cloudflare Tunnel into your existing infrastructure.</p>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/ecc233ab-9a33-46e3-b339-b2d592fc0d00/public" alt="What is Cloudflare Tunnel?"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/4fa0fe257187f18929c07754a4a4df09/iframe?preload=true&amp;letterboxColor=transparent" title="What is Cloudflare Tunnel?" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="how-it-works">How it works</h2>
<p><code>cloudflared</code> establishes <a href="#outbound-only-connections">outbound connections</a> (tunnels) between your resources and Cloudflare's global network. A tunnel is a persistent object identified by a UUID — it serves as the logical link between your origin and Cloudflare. Within the same tunnel, you can run as many <code>cloudflared</code> processes (<a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/#connector">connectors</a>) as needed. Each connector sends traffic to the nearest Cloudflare data center.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/handshake.jpg" alt="How an HTTP request reaches a private application connected with Cloudflare Tunnel" /></p>
<h3 id="outbound-only-connections">Outbound-only connections</h3>
<p>Cloudflare Tunnel uses an outbound-only connection model to enable bidirectional communication. When you install and run <code>cloudflared</code>, <code>cloudflared</code> initiates an outbound connection through your firewall from the origin to the Cloudflare global network.</p>
<p>Once the connection is established, traffic flows in both directions over the tunnel between your origin and Cloudflare. Most firewalls allow outbound traffic by default. <code>cloudflared</code> takes advantage of this standard by connecting out to the Cloudflare network from the server you installed <code>cloudflared</code> on. You can then configure your firewall to allow only these outbound connections and block all inbound traffic, effectively blocking access to your origin from anything other than Cloudflare. This setup ensures that all traffic to your origin is securely routed through the tunnel.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="authenticated-origin-pulls-does-not-apply">Authenticated Origin Pulls does not apply</h3>
@markup("md", "content/.markup/bodies/5154.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Create a tunnel using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Cloudflare dashboard</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/">API</a>.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Download <code>cloudflared</code></a>, the server-side daemon that connects your infrastructure to Cloudflare.</li>
<li>Review useful <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/">Tunnel terms</a> to familiarize yourself with the concepts used in Tunnel documentation.</li>
</ul>
