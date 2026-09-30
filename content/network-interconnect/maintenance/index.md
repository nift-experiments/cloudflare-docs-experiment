<h2 id="planned-maintenance">Planned maintenance</h2>
<p>Routine CNI-disruptive maintenance is planned work that can interrupt traffic on an affected CNI connection. Cloudflare coordinates this work across resilient Cloudflare Network Interconnect (CNI) deployments, including across CNI locations.</p>
<h3 id="timing-and-scheduling">Timing and scheduling</h3>
<p>For Dataplane v2 connectivity in multi-homed PoPs only:</p>
<ul>
<li><strong>Routine maintenance</strong>: Minimum one week notice.</li>
<li><strong>Emergency maintenance</strong>: Best-effort notice, which may be less than one week.</li>
<li>Routine maintenance on redundant devices at the same location will occur on different days.</li>
<li>Routine maintenance is not rescheduled to accommodate customer schedule preferences.</li>
</ul>
<table>
<thead>
<tr>
<th>CNI deployment</th>
<th>During routine CNI-disruptive maintenance</th>
</tr>
</thead>
<tbody>
<tr>
<td>One CNI connection at one location</td>
<td>The connection can be interrupted.</td>
</tr>
<tr>
<td>Two CNI connections on separate devices at one location</td>
<td>One connection remains in service.</td>
</tr>
<tr>
<td>Four CNI connections across two coordinated locations, with two connections on separate devices at each location</td>
<td>Three connections remain in service.</td>
</tr>
</tbody>
</table>
<h2 id="emergency-and-non-routine-maintenance">Emergency and non-routine maintenance</h2>
<p>Non-routine maintenance, such as maintenance that affects an entire PoP, can affect all CNI connections at the affected location. For the four-connection deployment with two connections at each of two locations, a full-PoP non-routine event at one location can interrupt two connections, leaving two in service. Cloudflare avoids performing non-routine maintenance at multiple coordinated locations at the same time.</p>
<p>Cloudflare coordinates emergency maintenance across locations where feasible.</p>
<h2 id="receive-maintenance-notifications">Receive maintenance notifications</h2>
<p>To configure circuit-specific or point-of-presence (PoP) maintenance notifications, refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>
