<hr />
<hr />
<p>You can restart, reboot, or shut down a Cloudflare One Appliance (formerly Magic WAN Connector) from the dashboard or via API. Operations are asynchronous — the appliance executes them the next time it checks in.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Restart</strong></td>
<td>Restart managed services. Purges temporary and (optionally) persistent state.</td>
</tr>
<tr>
<td><strong>Reboot</strong></td>
<td>Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</td>
</tr>
<tr>
<td><strong>Shutdown</strong></td>
<td>Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5757.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5761.md")
</div></div>
