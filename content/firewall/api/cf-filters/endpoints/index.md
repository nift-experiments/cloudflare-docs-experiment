<p>To invoke a Cloudflare Filters API operation, append the endpoint to the Cloudflare API base URL:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/&#10;</code></pre>
<p>For authentication instructions, refer to <a href="/fundamentals/api/">Getting Started: Requests</a> in the Cloudflare API documentation.</p>
<p>For help with endpoints and pagination, refer to <a href="/fundamentals/api/">Getting Started: Endpoints</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8709.md")
</aside>
<p>The Cloudflare Filters API supports the operations outlined below. Visit the pages in this section for examples.</p>
<table>
<thead>
<tr>
<th style="width: 20%">Operation</th>
<th>Method & Endpoint</th>
<th style="width: 30%">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>
        <a href="/api/resources/filters/methods/create/">Create filters</a>
</td>
<td>
        <code>POST zones/&lt;ZONE_ID&gt;/filters</code>
</td>
<td>Handled as a single transaction. If there is an error, the entire operation fails.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/filters/methods/list/">Get filters</a>
</td>
<td>
        <code>GET zones/&lt;ZONE_ID&gt;/filters</code>
</td>
<td>
        Lists all current filters. Results return paginated with 25 items per page by default. Use
        optional parameters to narrow results.
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/filters/methods/get/">Get a filter</a>
</td>
<td>
        <code>GET zones/&lt;ZONE_ID&gt;/filters/&lt;FILTER_ID&gt;</code>
</td>
<td>Retrieve a single filter by ID.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/filters/methods/bulk_update/">Update filters</a>
</td>
<td>
        <code>PUT zones/&lt;ZONE_ID&gt;/filters</code>
</td>
<td>
        Handled as a single transaction. All filters must exist for operation to succeed. If there
        is an error, the entire operation fails.
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/filters/methods/update/">Update a filter</a>
</td>
<td>
        <code>PUT zones/&lt;ZONE_ID&gt;/filters/&lt;FILTER_ID&gt;</code>
</td>
<td>Update a single filter by ID.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/filters/methods/bulk_delete/">Delete filters</a>
</td>
<td>
        <code>DELETE zones/&lt;ZONE_ID&gt;/filters</code>
</td>
<td>
        <p>Delete existing filters. Must specify list of filter IDs.</p>
        <p>
          Empty requests result in no deletion. Returns HTTP status code 200 if a specified filter
          does not exist.
        </p>
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/filters/methods/delete/">Delete a filter</a>
</td>
<td>
        <code>DELETE zones/&lt;ZONE_ID&gt;/filters/&lt;FILTER_ID&gt;</code>
</td>
<td>Delete a filter by ID.</td>
</tr>
</tbody>
</table>
