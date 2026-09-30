<p>You must keep your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3789.md")
</div> entries up to date so that it is public information that Cloudflare has permission to advertise your prefix or prefixes, and to ensure that your traffic can be properly routed on the Internet.
<h2 id="configure-an-irr-entry">Configure an IRR entry</h2>
<p>You can add or update an IRR entry by following the directions of your routing registry. Each routing registry has its own set of instructions to configure an IRR entry.</p>
<p>The recommended registries are AFRINIC, APNIC, ARIN, LACNIC, and RIPE. Refer to the table below for more information.</p>
<table>
<thead>
<tr>
<th>Route registry</th>
<th>URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>AFRINIC</td>
<td><a href="https://afrinic.net/internet-routing-registry#guide">https://afrinic.net/internet-routing-registry#guide</a></td>
</tr>
<tr>
<td>APNIC</td>
<td><a href="https://www.apnic.net/manage-ip/apnic-services/routing-registry/">https://www.apnic.net/manage-ip/apnic-services/routing-registry/</a></td>
</tr>
<tr>
<td>ARIN</td>
<td><a href="https://www.arin.net/resources/manage/irr/quickstart/">https://www.arin.net/resources/manage/irr/quickstart/</a></td>
</tr>
<tr>
<td>LACNIC</td>
<td><a href="https://lacnic.zendesk.com/hc/articles/360038667154-What-are-a-route-and-a-route-6-objects">https://lacnic.zendesk.com/hc/articles/360038667154-What-are-a-route-and-a-route-6-objects</a></td>
</tr>
<tr>
<td>RIPE</td>
<td><a href="https://www.ripe.net/manage-ips-and-asns/db/support/managing-route-objects-in-the-irr">https://www.ripe.net/manage-ips-and-asns/db/support/managing-route-objects-in-the-irr</a></td>
</tr>
</tbody>
</table>
<h2 id="verify-an-irr-entry">Verify an IRR entry</h2>
<p>Verify your Internet Routing Registry (IRR) entries to ensure that the IP prefixes Cloudflare advertises for you match the correct <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3790.md")
</div>.
<p>Each IRR entry record must include the following information:</p>
<ul>
<li><strong>Route</strong>: Each IP prefix Cloudflare advertises for you.</li>
<li><strong>Origin ASN</strong>: The Cloudflare ASN (AS13335) or your own ASN.</li>
<li><strong>Source</strong>: The name of the routing registry (for example, ARIN).</li>
</ul>
<p>Add or update IRR entries when they meet any of these criteria:</p>
<ul>
<li>The entry is missing.</li>
<li>The entry is incomplete or inaccurate — for example, when the route object does not show the correct origin.</li>
<li>The entry is complete but requires updating — for example, when they correspond to supernets but need to correspond to subnets used in Magic Transit.</li>
</ul>
<h3 id="subnet-prefix-verification">Subnet prefix verification</h3>
<p>Use <a href="https://irrexplorer.nlnog.net">IRR Explorer</a> to verify which ASN is associated with a subnet prefix.</p>
<p><strong>Method:</strong> Search for the subnet prefix IP, for example, <code>162.211.156.0/24</code>.</p>
<p><strong>Output:</strong> List of ASN numbers, source (route registry), and any associated errors.</p>
<h3 id="asn-verification">ASN verification</h3>
<p>Use <a href="https://irrexplorer.nlnog.net">IRR Explorer</a> to verify which prefixes are associated with an ASN.</p>
<p><strong>Method:</strong> Search for the ASN, for example <code>AS13335</code>.</p>
<p><strong>Output:</strong> List of prefixes, source, and any associated errors.</p>
<h3 id="whois-lookup">WHOIS lookup</h3>
<p>Use WHOIS lookup to verify your origin ASN and routing data.</p>
<p><strong>Method:</strong> In a terminal, use the following <code>whois</code> command, replacing <code>&lt;NETWORK_PREFIX&gt;</code> with your network prefix. The host <code>rr.ntt.net</code> is the primary server for the Global IP network.</p>
<pre><code class="language-sh">whois -h rr.ntt.net &lt;NETWORK_PREFIX&gt;&#10;</code></pre>
<p><strong>Output:</strong> IRR route, origin, and source information.</p>
<details class="nb-details"><summary>WHOIS output example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3791.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3788.md")
</aside>
