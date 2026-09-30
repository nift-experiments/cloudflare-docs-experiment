<p>Split tunnel settings determine which traffic the Cloudflare One Client does and does not proxy.</p>
<p>The Cloudflare One Client offers two different split tunnel modes:</p>
<ul>
<li>If you intend to send all internal and external destination traffic through Cloudflare's global network, opt for <strong>Exclude IPs and domains</strong> mode. This mode will proxy everything through the WARP tunnel with the exception of IPs and hosts defined explicitly within the Split Tunnel list.</li>
<li>If you intend to only use the Cloudflare One Client to proxy private destination traffic, you can operate in <strong>Include IPs and domains</strong> mode, in which you explicitly define which IP ranges and domains should be included in the WARP routing table.</li>
</ul>
<h2 id="update-split-tunnels-mode">Update Split Tunnels mode</h2>
<p>To change your Split Tunnels mode:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10062.md")
</div></div>
<p>All clients with this device profile will now switch to the new mode and its default route configuration. Next, <a href="#add-a-route">add</a> or <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#remove-a-route">remove</a> routes from your Split Tunnel configuration.</p>
<h2 id="add-a-route">Add a route</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10069.md")
</div></div>
<p>It may take up to 10 minutes for newly updated settings to propagate to devices.</p>
<p>We recommend keeping the Split Tunnels list short, as each entry takes time for the client to parse. In particular, domains are slower to action than IP addresses because they require on-the-fly IP lookups and routing table / local firewall changes. A shorter list will also make it easier to understand and debug your configuration. For information on device profile limits, refer to <a href="/cloudflare-one/account-limits/#warp">Account limits</a>.</p>
