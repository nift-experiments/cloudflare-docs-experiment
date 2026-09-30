<p>Below is a list of the different layers that makes up the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">open systems interconnection (OSI) model</a> and the associated Cloudflare products.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8782.md")
</aside>
<table>
<thead>
<tr>
<th>Network layer</th>
<th>Protocol and related products</th>
</tr>
</thead>
<tbody>
<tr>
<td>7 Application layer</td>
<td><strong>HTTP, DNS</strong><br/> <a href="/dns">Authoritative DNS</a>, <a href="/bots">Bot Management</a>, <a href="/cache/">CDN</a>, <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>, <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> (outbound only), <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>, <a href="/load-balancing/understand-basics/proxy-modes/">Load Balancing</a>, <a href="/stream/">Stream</a>, <a href="/waf/">WAF</a></td>
</tr>
<tr>
<td>6 Presentation layer</td>
<td></td>
</tr>
<tr>
<td>5 Session layer</td>
<td></td>
</tr>
<tr>
<td>4 Transport layer</td>
<td><strong>TCP/UDP</strong><br/> <a href="/argo-smart-routing/">Argo Smart Routing</a>, <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> (outbound only), <a href="/load-balancing/understand-basics/proxy-modes/">Load Balancing</a>, <a href="/spectrum/">Spectrum</a></td>
</tr>
<tr>
<td>3 Network layer</td>
<td><strong>IP, GRE, any packet/protocol</strong><br/> <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>, <a href="/magic-transit">Magic Transit</a>, <a href="/cloudflare-wan">Cloudflare WAN</a></td>
</tr>
<tr>
<td>2 Datalink layer</td>
<td><strong>Direct connection</strong><br/> <a href="/network-interconnect">Cloudflare Network Interconnect (CNI)</a></td>
</tr>
<tr>
<td>1 Physical layer</td>
<td><strong>Direct connection</strong><br/> <a href="/network-interconnect">Cloudflare Network Interconnect (CNI)</a></td>
</tr>
</tbody>
</table>
