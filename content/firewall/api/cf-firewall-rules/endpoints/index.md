<p>To invoke a Cloudflare Firewall Rules API operation, append the endpoint to the Cloudflare API base URL:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/&#10;</code></pre>
<p>For authentication instructions, refer to <a href="/fundamentals/api/">Getting Started: Requests</a> in the Cloudflare API documentation.</p>
<p>For help with endpoints and pagination, refer to <a href="/fundamentals/api/">Getting Started: Endpoints</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8706.md")
</aside>
<p>The Cloudflare Firewall Rules API supports the operations outlined below. Visit the pages in this section for examples.</p>
<table style="table-layout:fixed; width:100%">
<thead>
<tr>
<th>Operation</th>
<th style="width: 60%">Method & Endpoint</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/create/">
          Create firewall rules
        </a>
</td>
<td>`POST zones/<ZONE_ID>/firewall/rules`</td>
<td>Handled as a single transaction. If there is an error, the entire operation fails.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/list/">
          List firewall rules
        </a>
</td>
<td>`GET zones/<ZONE_ID>/firewall/rules`</td>
<td>
        Lists all current firewall rules. Results return paginated with 25 items per page by default. Use optional parameters to narrow results.
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/get/">
          Get a firewall rule
        </a>
</td>
<td>`GET zones/<ZONE_ID>/firewall/rules/<RULE_ID>`</td>
<td>Retrieve a single firewall rule by ID.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/bulk_update/">
          Update firewall rules
        </a>
</td>
<td>`PUT zones/<ZONE_ID>/firewall/rules`</td>
<td>
        Handled as a single transaction. All rules must exist for operation to succeed. If there is
        an error, the entire operation fails.
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/update/">
          Update a firewall rule
        </a>
</td>
<td>`PUT zones/<ZONE_ID>/firewall/rules/<RULE_ID>`</td>
<td>Update a single firewall rule by ID.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/bulk_delete/">
          Delete firewall rules
        </a>
</td>
<td>`DELETE zones/<ZONE_ID>/firewall/rules`</td>
<td>
        <p>Delete existing firewall rules. Must specify list of firewall rule IDs.</p>
        <p>
          Empty requests result in no deletion. Returns HTTP status code 200 if a specified rule
          does not exist.
        </p>
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/delete/">
          Delete a firewall rule
        </a>
</td>
<td>`DELETE zones/<ZONE_ID>/firewall/rules/<RULE_ID>`</td>
<td>
        <p>Delete a firewall rule by ID.</p>
</td>
</tr>
</tbody>
</table>
