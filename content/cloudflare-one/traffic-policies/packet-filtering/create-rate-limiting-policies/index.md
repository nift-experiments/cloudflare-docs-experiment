<p>Rate limiting policies (beta) allow you to set maximum traffic thresholds - measured in packets or bits per second — for incoming traffic destined for your network as it arrives at specific Cloudflare data centers. When traffic to a location exceeds your defined limit, the policy takes action.</p>
<p>This guide walks you through creating a policy that matches incoming packets and triggers when the traffic rate exceeds your configured threshold.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6419.md")
</aside>
<h2 id="add-a-policy">Add a policy</h2>
<p>To add a policy:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>In the <strong>Rate limiting</strong> tab, select <strong>Add a policy</strong>.</li>
<li>Fill out the information for your new policy:
<ul>
<li>Select the <strong>Field</strong>: At the moment, you can only choose a <a href="/cloudflare-network-firewall/reference/network-firewall-fields/">data center name</a> (for example, <code>ORD</code> for Chicago).</li>
<li>Select the <strong>Operator</strong>: Choose among <strong>equals</strong> or <strong>is in</strong>.</li>
<li>Select the <strong>Value</strong>.</li>
</ul>
</li>
<li>When you are done, select <strong>Save policy</strong>.</li>
</ol>
<h2 id="edit-an-existing-policy">Edit an existing policy</h2>
<p>To edit a policy:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Select the <strong>Rate limiting</strong> tab.</li>
<li>Locate the policy you want to edit in the list and select <strong>Edit</strong>.</li>
<li>Edit the policy with your changes and select <strong>Edit policy</strong>.</li>
</ol>
<h2 id="delete-an-existing-policy">Delete an existing policy</h2>
<p>To delete an existing policy:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Select the <strong>Rate limiting</strong> tab.</li>
<li>Locate the policy you want to delete from the list.</li>
<li>Select the three dots, then select <strong>Remove</strong>.</li>
</ol>
