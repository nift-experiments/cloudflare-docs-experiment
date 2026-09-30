<p>You can configure Advanced TCP Protection using the Advanced TCP Protection API.</p>
<p>The Advanced TCP Protection API only supports <a href="/fundamentals/api/get-started/create-token/">API token authentication</a>.</p>
<p>For examples of API calls, refer to <a href="/ddos-protection/advanced-ddos-systems/api/tcp-protection/examples/">Common API calls</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Advanced TCP Protection API endpoints listed below to the Cloudflare API base URL.</p>
<p>The Cloudflare API base URL is:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{account_id}</code> argument is the account ID (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The tables in the following sections summarize the available operations.</p>
<h3 id="general-operations">General operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get Advanced TCP Protection status</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status</code></p>Gets the global Advanced TCP Protection status (enabled or disabled).</td>
</tr>
<tr>
<td>Update Advanced TCP Protection status</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status</code></p>Enables or disables Advanced TCP Protection.</td>
</tr>
</tbody>
</table>
<h3 id="prefix-operations">Prefix operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List prefixes</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes</code></p>Fetches all Advanced TCP Protection prefixes in the account.</td>
</tr>
<tr>
<td>Add prefixes in bulk</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/bulk</code></p>Adds prefixes in bulk to the account (up to 300 prefixes per request).</td>
</tr>
<tr>
<td>Get a prefix</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}</code></p>Fetches the details of an existing prefix.</td>
</tr>
<tr>
<td>Update a prefix</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}</code></p>Updates an existing prefix.</td>
</tr>
<tr>
<td>Delete a prefix</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}</code></p>Deletes an existing prefix.</td>
</tr>
<tr>
<td>Delete all prefixes</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes</code></p>Deletes all existing prefixes from the account.</td>
</tr>
</tbody>
</table>
<h3 id="allowlist-operations">Allowlist operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List allowlisted prefixes</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist</code></p>Fetches all prefixes in the account allowlist.</td>
</tr>
<tr>
<td>Add an allowlisted prefix</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist</code></p>Adds a prefix to the allowlist.</td>
</tr>
<tr>
<td>Get an allowlisted prefix</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{allowlist_id}</code></p>Fetches the details of an existing prefix in the allowlist.</td>
</tr>
<tr>
<td>Update an allowlisted prefix</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{allowlist_id}</code></p>Updates an existing prefix in the allowlist.</td>
</tr>
<tr>
<td>Delete an allowlisted prefix</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{allowlist_id}</code></p>Deletes an existing prefix from the allowlist.</td>
</tr>
<tr>
<td>Delete all allowlisted prefixes</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist</code></p>Deletes all existing prefixes from the allowlist.</td>
</tr>
</tbody>
</table>
<h3 id="syn-flood-protection-operations">SYN Flood Protection operations</h3>
<h4 id="rules">Rules</h4>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List SYN flood rules</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules</code></p>Fetches all SYN flood rules in the account.</td>
</tr>
<tr>
<td>Add a SYN flood rule</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules</code></p>Adds a SYN flood rule to the account.</td>
</tr>
<tr>
<td>Get a SYN flood rule</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}</code></p>Fetches the details of an existing SYN flood rule in the account.</td>
</tr>
<tr>
<td>Update a SYN flood rule</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}</code></p>Updates an existing SYN flood rule in the account.</td>
</tr>
<tr>
<td>Delete a SYN flood rule</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}</code></p>Deletes an existing SYN flood rule from the account.</td>
</tr>
<tr>
<td>Delete all SYN flood rules</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules</code></p>Deletes all existing SYN flood rules from the account.</td>
</tr>
</tbody>
</table>
<h4 id="filters">Filters</h4>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List SYN flood filters</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters</code></p>Fetches all SYN flood filters in the account.</td>
</tr>
<tr>
<td>Add a SYN flood filter</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters</code></p>Adds a SYN flood filter to the account.</td>
</tr>
<tr>
<td>Get a SYN flood filter</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}</code></p>Fetches the details of an existing SYN flood filter in the account.</td>
</tr>
<tr>
<td>Update a SYN flood filter</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}</code></p>Updates an existing SYN flood filter in the account.</td>
</tr>
<tr>
<td>Delete a SYN flood filter</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}</code></p>Deletes an existing SYN flood filter from the account.</td>
</tr>
<tr>
<td>Delete all SYN flood filters</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters</code></p>Deletes all existing SYN flood filters from the account.</td>
</tr>
</tbody>
</table>
<h3 id="out-of-state-tcp-protection-operations">Out-of-state TCP Protection operations</h3>
<h4 id="rules-1">Rules</h4>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List out-of-state TCP rules</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules</code></p>Fetches all out-of-state TCP rules in the account.</td>
</tr>
<tr>
<td>Add an out-of-state TCP rule</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules</code></p>Adds an out-of-state TCP rule to the account.</td>
</tr>
<tr>
<td>Get an out-of-state TCP rule</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}</code></p>Fetches the details of an existing out-of-state TCP rule in the account.</td>
</tr>
<tr>
<td>Update an out-of-state TCP rule</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}</code></p>Updates an existing out-of-state TCP rule in the account.</td>
</tr>
<tr>
<td>Delete an out-of-state TCP rule</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}</code></p>Deletes an existing out-of-state TCP rule from the account.</td>
</tr>
<tr>
<td>Delete all out-of-state TCP rules</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules</code></p>Deletes all existing out-of-state TCP rules from the account.</td>
</tr>
</tbody>
</table>
<h4 id="filters-1">Filters</h4>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List out-of-state TCP filters</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters</code></p>Fetches all out-of-state TCP filters in the account.</td>
</tr>
<tr>
<td>Add an out-of-state TCP filter</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters</code></p>Adds an out-of-state TCP filter to the account.</td>
</tr>
<tr>
<td>Get an out-of-state TCP filter</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}</code></p>Fetches the details of an existing out-of-state TCP filter in the account.</td>
</tr>
<tr>
<td>Update an out-of-state TCP filter</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}</code></p>Updates an existing out-of-state TCP filter in the account.</td>
</tr>
<tr>
<td>Delete an out-of-state TCP filter</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}</code></p>Deletes an existing out-of-state TCP filter from the account.</td>
</tr>
<tr>
<td>Delete all out-of-state TCP filters</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters</code></p>Deletes all existing out-of-state TCP filters from the account.</td>
</tr>
</tbody>
</table>
<h2 id="pagination">Pagination</h2>
<p>The API operations that return a list of items use pagination. For more information on the available pagination query parameters, refer to <a href="/fundamentals/api/how-to/make-api-calls/#pagination">Pagination</a>.</p>
