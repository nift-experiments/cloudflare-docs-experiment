<p>The following topics are useful for troubleshooting BYOIP issues.</p>
<h2 id="urpf-filtering-and-packet-loss">uRPF filtering and packet loss</h2>
<p>Routers receive IP packets and forward the packets to the destination IP address. Unicast Reverse Path Forwarding (uRPF) is a security feature that can prevent spoofing attacks. uRPF operates under two modes: strict and loose mode.</p>
<p>Under <strong>strict mode</strong>, the router performs two checks on incoming packets to look for a matching entry in the source routing table and to determine whether the interface that received the packet can be used to reach the source. If the incoming IP packets pass both checks, the packets are forwarded; if the checks do not pass, the packets are dropped.</p>
<p>When uRPF is set to loose mode, the router performs a single check when it receives an IP packet to look for a source's matching entry in the routing table.</p>
<p>If you are experiencing packet loss as a result of an upstream ISP implementing uRPF filtering, contact your ISP and request the link be set to <strong>loose mode</strong>.</p>
<h2 id="non-sni-support">Non-SNI support</h2>
<p>Currently, BYOIP cannot be used with <a href="/ssl/edge-certificates/custom-certificates/uploading/">legacy custom certificates</a> to support <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3725.md")
</div> requests.
<p>Instead, you can use Address Maps to set a default SNI for IPs on your account or zone. Refer to <a href="/byoip/address-maps/setup/#non-sni-support">Setup</a> for further guidance.</p>
<h2 id="self-serve-onboarding-api-errors">Self-serve onboarding API errors</h2>
<p>When onboarding BYOIP prefixes via the API, you may encounter the following errors:</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Meaning</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>prefix_not_valid_and_approved</code></td>
<td>The prefix has not passed IRR validation, RPKI validation, and ownership verification (or manual approval).</td>
<td>Verify all three validation steps have completed. If one or more are failing, check prefix registration with your Regional Internet Registry (RIR) and your RPKI ROA configuration. If validation is passing but you are still seeing this error, contact support for manual approval.</td>
</tr>
<tr>
<td><code>incomplete_bgp_deployment</code></td>
<td>Cannot create a BGP prefix without a default edge service binding configured.</td>
<td>Configure a default edge service binding before creating BGP prefixes.</td>
</tr>
<tr>
<td><code>advertise_state_locked</code></td>
<td>Cannot create a BGP prefix — the default edge service binding is still deploying.</td>
<td>Wait for the edge service binding deployment to complete, then retry.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3724.md")
</aside>
