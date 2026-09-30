<p>Cloudflare Mesh is available in beta to Cloudflare One accounts, including accounts on the Free plan.</p>
<h2 id="platform-requirements">Platform requirements</h2>
<ul>
<li>Mesh nodes require a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#linux">supported Linux distribution</a> or the <a href="/mesh/guides/run-mesh-in-containers/"><code>cloudflare/mesh</code> container image</a>.</li>
<li>Client devices can use any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">operating system supported by the Cloudflare One Client</a>.</li>
<li>Mesh nodes must use the MASQUE device tunnel protocol. Hostname routes, IPv6 CIDR routes, and high availability do not work with WireGuard.</li>
<li>Using Cloudflare Mesh with Cloudflare WAN requires <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing mode</a>.</li>
</ul>
<p>For deployment recommendations and interoperability constraints, refer to <a href="/mesh/best-practices/">Best practices</a>.</p>
