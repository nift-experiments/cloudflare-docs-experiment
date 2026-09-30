<p>You can bundle multiple physical LAN ports on a Cloudflare One Appliance into a single logical port called a Link Aggregation Group (LAG). This increases LAN bandwidth and provides redundancy. If a member port fails, traffic automatically shifts to the remaining ports in under one second.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5756.md")
</aside>
<p>The following guide assumes you have already created a site and configured your Cloudflare One Appliance. For instructions, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/">Configure hardware Appliance</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure virtual Appliance</a>.</p>
<h2 id="create-a-lag">Create a LAG</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance you want to configure &gt; <strong>Edit</strong>.</li>
<li>Go to the <strong>Appliances</strong> tab.</li>
<li>In <strong>Link aggregation groups (LAGs)</strong>, select <strong>Create A LAG</strong>.</li>
<li>Select the LAN ports you want to bundle. You can add up to six ports per LAG. All ports must be the same type and speed.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="assign-a-lan-to-a-lag">Assign a LAN to a LAG</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance you want to edit &gt; <strong>Edit</strong>.</li>
<li>Go to <strong>Network Configuration</strong> &gt; <strong>LAN configuration</strong>.</li>
<li>Select or create a LAN &gt; <strong>Edit</strong>.</li>
<li>In <strong>Interface</strong> &gt; <strong>Interface type</strong>, select <strong>Aggregate</strong> as your LAG instead of a single port.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="monitor-lag-status">Monitor LAG status</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance &gt; <strong>Edit</strong>.</li>
<li>Go to the <strong>Appliances</strong> tab.</li>
</ol>
<p>The page displays each configured LAG and the status of its member ports.</p>
<h2 id="delete-a-lag">Delete a LAG</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance &gt; <strong>Edit</strong>.</li>
<li>Go to the <strong>Appliances</strong> tab.</li>
<li>Next to the LAG you want to delete, select the three-dot menu &gt; <strong>Delete</strong>.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
