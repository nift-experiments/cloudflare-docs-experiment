<p>You can define policies in your Cloudflare One Appliance (formerly Magic WAN Connector) to either allow traffic to flow between your LANs without it leaving your local premises or to forward it via the Cloudflare network where you can add additional security features. The default behavior is to drop all LAN-to-LAN traffic. These policies can be created for specific subnets, and link two LANs.</p>
<pre class="mermaid">&#10;&#10;	{`&#10;		flowchart LR&#10;		accTitle: LAN-to-LAN traffic flow&#10;		accDescr: In this example, the red path shows traffic that stays in the customer's premises (allowing direct communication between LAN 3 and LAN 4), and the orange path shows traffic that goes to Cloudflare before returning to the customer's premises (processing traffic between LAN 1 and LAN 2 in Cloudflare).&#10;				a(Cloudflare One Appliance) <---> b(Internet) <---> c(Cloudflare)&#10;&#10;				subgraph Customer site&#10;				d[LAN 1] <---> a&#10;				e[LAN 2] <---> a&#10;				g[LAN 3] <---> a&#10;				h[LAN 4] <---> a&#10;				end&#10;				classDef orange fill:#f48120,color: black&#10;				class a,c orange&#10;&#10;				linkStyle 0,1,2,3 stroke:#f48120,stroke-width:3px&#10;				linkStyle 4,5 stroke:red,stroke-width:3px&#10;	`}&#10;&#10;</pre>
<p><em>In this example, the red path shows traffic that stays in the customer's premises (allowing direct communication between LAN 3 and LAN 4), and the orange path shows traffic that goes to Cloudflare before returning to the customer's premises (processing traffic between LAN 1 and LAN 2 in Cloudflare).</em></p>
<br />
<p>As a best practice for security, we recommend sending all traffic through Cloudflare's network for Zero Trust security filtering. Use these policies with care and only for scenarios where you have a hard requirement for LAN-to-LAN traffic flows.</p>
<p>If you enable LAN to LAN traffic flows, communications can only be initiated from origin to destination — for example, LAN 1 to LAN 2 — and not the other way around. This is by design and prevents potential exfiltration of information. This does not mean bidirectional communication on TCP is not possible. It only means that the origin is the only one authorized to initiate communications.</p>
<p>Unidirectional communication can be enabled for UDP and ICMP, but it is not available for TCP, as it would break that protocol.</p>
<p>The following guide assumes you have already created a site and configured your Cloudflare One Appliance. For instructions to create a site and configure your Cloudflare One Appliance, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/">Configure hardware Appliance</a> or <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure Virtual Appliance</a>, depending on the type of Cloudflare One Appliance you have on your premises.</p>
<h2 id="create-a-policy">Create a policy</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6985.md")
</div></div>
<p>The new policy will ensure that traffic between the specified LANs flows locally, bypassing Cloudflare.</p>
<h2 id="edit-a-policy">Edit a policy</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6988.md")
</div></div>
<h2 id="delete-a-policy">Delete a policy</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6991.md")
</div></div>
