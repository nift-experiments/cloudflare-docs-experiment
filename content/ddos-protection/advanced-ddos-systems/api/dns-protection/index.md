<p>Use the <a href="/api/">Cloudflare API</a> to configure Advanced DNS Protection via API.</p>
<p>For examples of API calls, refer to <a href="/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/">Common API calls</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Advanced DNS Protection API endpoints listed below to the Cloudflare API base URL:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{account_id}</code> argument is the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The following table summarizes the available operations.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb + Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>List DNS protection rules</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules</code></p>Fetches all DNS protection rules in the account.</td>
</tr>
<tr>
<td>Add a DNS protection rule</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules</code></p>Adds a DNS protection rule to the account.</td>
</tr>
<tr>
<td>Get a DNS protection rule</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}</code></p>Fetches the details of an existing DNS protection rule in the account.</td>
</tr>
<tr>
<td>Update a DNS protection rule</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}</code></p>Updates an existing DNS protection rule in the account.</td>
</tr>
<tr>
<td>Delete a DNS protection rule</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}</code></p>Deletes an existing DNS protection rule from the account.</td>
</tr>
<tr>
<td>Delete all DNS protection rules</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules</code></p>Deletes all existing DNS protection rules from the account.</td>
</tr>
</tbody>
</table>
