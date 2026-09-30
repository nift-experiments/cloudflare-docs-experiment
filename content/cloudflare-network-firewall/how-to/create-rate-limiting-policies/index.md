<p>Rate limiting policies (beta) allow you to manage incoming traffic to your network for specific locations.</p>
<p>This guide will teach you how to create a policy for when incoming packets match, and in cases where your rate exceeds a certain value (in packets or bits).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4272.md")
</aside>
<h2 id="add-a-policy">Add a policy</h2>
<p>To add a policy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>Select the <strong>Rate limiting</strong> tab, then select <strong>Add a policy</strong>.</li>
<li>Fill out the information for your new policy:
<ul>
<li>Select the <strong>Field</strong>: At the moment, you can only choose a <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/cloudflare-network-firewall/">colo name</a>.</li>
<li>Select the <strong>Operator</strong>: Choose among <strong>equals</strong> or <strong>is in</strong>.</li>
<li>Select the <strong>Value</strong>.</li>
</ul>
</li>
<li>When you are done, select <strong>Save policy</strong>.</li>
</ol>
<h2 id="edit-an-existing-policy">Edit an existing policy</h2>
<p>To edit a policy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>Select the <strong>Rate limiting</strong> tab.</li>
<li>Locate the policy you want to edit in the list and select <strong>Edit</strong>.</li>
<li>Edit the policy with your changes and select <strong>Edit policy</strong>.</li>
</ol>
<h2 id="delete-an-existing-policy">Delete an existing policy</h2>
<p>To delete an existing policy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>Select the <strong>Rate limiting</strong> tab.</li>
<li>Locate the policy you want to delete from the list.</li>
<li>Select the three dots, then select <strong>Remove</strong>.</li>
</ol>
