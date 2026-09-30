<p>Cloudflare WAN (formerly Magic WAN) typically connects to Cloudflare through IPsec or GRE tunnels over the public Internet. Cloudflare Network Interconnect (CNI) is an alternative that provides a private, dedicated link — useful when you need lower latency, more consistent throughput, or want to avoid public Internet transit entirely.</p>
<p>Cloudflare Network Interconnect (CNI) provides a private, dedicated connection between your network and Cloudflare — bypassing the public Internet entirely. This is useful when you need consistent latency, higher throughput, or an additional layer of security that public Internet paths cannot guarantee.</p>
<p>With CNI, you get the same Cloudflare network services (firewall, routing, traffic management) applied to your traffic, but over a connection that does not traverse shared Internet infrastructure.</p>
<p>For more information about Network Interconnect, refer to the <a href="/network-interconnect/">Cloudflare Network Interconnect documentation</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="run-traceroute">Run <code>traceroute</code></h3>
@markup("md", "content/.markup/bodies/1266.md")
</aside>
