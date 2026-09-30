<p>DHCP Relay provides a way for DHCP clients to communicate with DHCP servers that are not available on the same local subnet/broadcast domain. When you enable DHCP Relay, Cloudflare One Appliance (formerly Magic WAN Connector) forwards DHCP discover messages to a predefined DHCP server, and routes the responses back to the original device that sent the discover message.</p>
<pre class="mermaid">&#10;&#10;	{`&#10;		flowchart LR&#10;		accTitle: DHCP Relay diagram&#10;		accDescr: The graph shows Cloudflare One Appliance sending DHCP discover messages to a DHCP server offsite.&#10;				a(Cloudflare One Appliance) <--> b(Cloudflare/Cloudflare WAN) <--> c(DHCP server)&#10;&#10;				subgraph Site A&#10;				d[LAN 1] <--> a&#10;				e[LAN 2] <--> a&#10;				end&#10;&#10;				subgraph Site B&#10;				c&#10;				end&#10;				classDef orange fill:#f48120,color: black&#10;				class a,b,c orange&#10;	`}&#10;&#10;</pre>
<p><em>The graph shows Cloudflare One Appliance sending DHCP discover messages to a DHCP server offsite.</em></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5790.md")
</aside>
<p>To configure DHCP relay:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5793.md")
</div></div>
