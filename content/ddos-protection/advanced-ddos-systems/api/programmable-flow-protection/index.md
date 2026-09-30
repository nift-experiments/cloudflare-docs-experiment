<p>Use the <a href="/api/">Cloudflare API</a> to configure Programmable Flow Protection.</p>
<p>For examples of API calls, refer to <a href="/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/">Common API calls</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Programmable Flow Protection API endpoints listed below to the Cloudflare API base URL:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{account_id}</code> argument is the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The tables in the following sections summarize the available operations.</p>
<h3 id="program-operations">Program operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List programs</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/programs</code></p>Fetches all Programmable Flow Protection programs in the account.</td>
</tr>
<tr>
<td>Upload a program</td>
<td><p><code>POST accounts/{account_id}/magic/programmable_flow_protection/configs/programs</code></p>Uploads a new program to the account. Include the optional <code>X-Program-Name</code> header to specify a human-readable program name. If omitted, the API generates a UUID as the program name.</td>
</tr>
<tr>
<td>Get a program</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}</code></p>Fetches the details of an existing program.</td>
</tr>
<tr>
<td>Update a program</td>
<td><p><code>PATCH accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}</code></p>Updates an existing program.</td>
</tr>
<tr>
<td>Delete a program</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}</code></p>Deletes an existing program from the account.</td>
</tr>
<tr>
<td>Delete all programs</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/programs</code></p>Deletes all existing programs from the account.</td>
</tr>
</tbody>
</table>
<h3 id="rule-operations">Rule operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List rules</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/rules</code></p>Fetches all Programmable Flow Protection rules in the account.</td>
</tr>
<tr>
<td>Create a rule</td>
<td><p><code>POST accounts/{account_id}/magic/programmable_flow_protection/configs/rules</code></p>Creates a new rule in the account.</td>
</tr>
<tr>
<td>Get a rule</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}</code></p>Fetches the details of an existing rule.</td>
</tr>
<tr>
<td>Update a rule</td>
<td><p><code>PATCH accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}</code></p>Updates an existing rule in the account.</td>
</tr>
<tr>
<td>Delete a rule</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}</code></p>Deletes an existing rule from the account.</td>
</tr>
<tr>
<td>Delete all rules</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/rules</code></p>Deletes all existing rules from the account.</td>
</tr>
</tbody>
</table>
<h3 id="debug-operations">Debug operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Debug with PCAP</td>
<td><p><code>POST accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}/pcap</code></p>Runs a program against a PCAP file and returns an annotated PCAP with program verdicts.</td>
</tr>
</tbody>
</table>
<h2 id="pagination">Pagination</h2>
<p>The API operations that return a list of items use pagination. For more information on the available pagination query parameters, refer to <a href="/fundamentals/api/how-to/make-api-calls/#pagination">Pagination</a>.</p>
