<p>Cloudflare Waiting Room redirect visitors to virtual waiting rooms when they are trying to access web pages that have high volumes of traffic.</p>
<p>The <a href="/api/resources/waiting_rooms/methods/list/">Cloudflare Waiting Room API</a> provides an interface for programmatically managing waiting rooms.</p>
<h2 id="request-url-format">Request URL format</h2>
<p>To invoke a <a href="/api/resources/waiting_rooms/methods/list/">Cloudflare Waiting Room API</a> operation, append the endpoint to the Cloudflare API base URL:</p>
<pre><code class="language-shell">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>For authentication instructions, refer to <a href="/fundamentals/api/">Getting Started: Requests</a> in the Cloudflare API documentation.</p>
<p>For help with endpoints and pagination, refer to <a href="/fundamentals/api/">Getting Started: Endpoints</a>.</p>
<h2 id="manage-your-waiting-room">Manage your waiting room</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method + URL stub</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/list/">List waiting rooms</a></td>
<td><code>GET zones/{:zone_identifier}/waiting_rooms</code></td>
<td>List all waiting rooms for a zone.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/create/">Create waiting room</a></td>
<td><code>POST zones/{:zone_identifier}/waiting_rooms</code></td>
<td>Create a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/get/">Waiting room details</a></td>
<td><code>GET zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Fetch a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/update/">Update waiting room</a></td>
<td><code>PUT zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Update a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/delete/">Delete waiting room</a></td>
<td><code>DELETE zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Delete a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/edit/">Patch waiting room</a></td>
<td><code>PATCH zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Patch a configured waiting room.</td>
</tr>
</tbody>
</table>
<h2 id="fetch-the-current-status-of-a-waiting-room">Fetch the current status of a waiting room</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method + URL stub</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/waiting_rooms/subresources/statuses/methods/get/">Get the current status of a waiting room</a></td>
<td><code>GET zones/{:zone_identifier}/waiting_rooms/{:identifier}/status</code></td>
<td><ul><li>Returns <code>queueing</code> if the queue is activated (clients are put in the waiting room).</li><li>Returns <code>not_queueing</code> if the queue is not activated or if the waiting room is suspended.</li></ul></td>
</tr>
</tbody>
</table>
