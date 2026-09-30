<p>This page documents error codes returned by Queues when using the <a href="/api/resources/queues/methods/create/">Queues Cloudflare API</a>.</p>
<h2 id="how-errors-are-returned">How errors are returned</h2>
<p>For the <a href="/queues/configuration/javascript-apis/">JavaScript APIs</a>, Queues operations throw exceptions that you can catch. The error code is included at the end of the <code>message</code> property:</p>
<pre><code class="language-js">try {&#10;	await env.MY_QUEUE.send(&quot;message&quot;, { delaySeconds: 999999 });&#10;    return new Response(&quot;Sent message to the queue&quot;);&#10;} catch (error) {&#10;	console.error(error);&#10;	return new Response(&quot;Failed to send message to the queue&quot;, { status: 500 });&#10;}&#10;</code></pre>
<p>For the <a href="/api/resources/queues/subresources/messages/">Cloudflare API via HTTP</a>, the response will include an <code>errors</code> object which has both a <code>message</code> and <code>code</code> field:</p>
<pre><code class="language-json">{&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 7003,&#10;      &quot;message&quot;: &quot;No route for the URI&quot;,&#10;      &quot;documentation_url&quot;: &quot;documentation_url&quot;,&#10;      &quot;source&quot;: {&#10;        &quot;pointer&quot;: &quot;pointer&quot;&#10;      }&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [&#10;    &quot;string&quot;&#10;  ],&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<h2 id="error-code-reference">Error code reference</h2>
<h3 id="client-side-errors">Client side errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Error</th>
<th>Details</th>
<th>Recommended actions</th>
</tr>
</thead>
<tbody>
<tr>
<td>10104</td>
<td>QueueNotFound</td>
<td>Queue does not exist</td>
<td>Check for existence of <code>queue_id</code> in <a href="/api/resources/queues/">List Queues endpoint</a></td>
</tr>
<tr>
<td>10106</td>
<td>Unauthorized</td>
<td>Unauthorized request</td>
<td>Ensure that current user has permission to push to that queue.</td>
</tr>
<tr>
<td>10107</td>
<td>QueueIDMalformed</td>
<td>The queue ID in the request URL is not a valid queue identifier</td>
<td>Ensure that <code>queue_id</code> contains only alphanumeric characters.</td>
</tr>
<tr>
<td>10201</td>
<td>ClientDisconnected</td>
<td>Client disconnected during request processing</td>
<td>Consider increasing timeout and retry message send.</td>
</tr>
<tr>
<td>10202</td>
<td>BatchDelayInvalid</td>
<td>Invalid batch delay</td>
<td>Ensure that <code>batch_delay</code> is within 1 and 86400 seconds</td>
</tr>
<tr>
<td>10203</td>
<td>MessageMetadataInvalid</td>
<td>Invalid message metadata (includes invalid content type and invalid delay)</td>
<td>Ensure <code>contentType</code> is one of <code>text</code>, <code>bytes</code>, <code>json</code>, or <code>v8</code>. Ensure the message delay does not exceed the <a href="/queues/platform/limits/">maximum of 24 hours</a></td>
</tr>
<tr>
<td>10204</td>
<td>MessageSizeOutOfBounds</td>
<td>Message size out of bounds</td>
<td>Ensure that message size is within 0 and 128 KB</td>
</tr>
<tr>
<td>10205</td>
<td>BatchSizeOutOfBounds</td>
<td>Batch size out of bounds</td>
<td>Ensure that batch size is within 0 and 256 KB</td>
</tr>
<tr>
<td>10206</td>
<td>BatchCountOutOfBounds</td>
<td>Batch count out of bounds</td>
<td>Ensure that batch count is within 0 and 100 messages</td>
</tr>
<tr>
<td>10207</td>
<td>JSONRequestBodyInvalid</td>
<td>Request JSON body does not match expected schema</td>
<td>Ensure that JSON body matches the expected schema</td>
</tr>
<tr>
<td>10208</td>
<td>JSONRequestBodyMalformed</td>
<td>Request body is not valid JSON</td>
<td><a href="/api/resources/queues/methods/create/">REST API</a> request body is not valid. Look at error message for additional details.</td>
</tr>
</tbody>
</table>
<h3 id="429-type-errors">429 type errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Error</th>
<th>Details</th>
<th>Recommended actions</th>
</tr>
</thead>
<tbody>
<tr>
<td>10250</td>
<td>QueueOverloaded</td>
<td>Queue is overloaded</td>
<td>Temporarily back off sending messages to the queue.</td>
</tr>
<tr>
<td>10251</td>
<td>QueueStorageLimitExceeded</td>
<td>Queue storage limit exceeded</td>
<td><a href="/queues/configuration/pause-purge/#purge-queue">Purge queue</a> or wait for queue to process backlog</td>
</tr>
<tr>
<td>10252</td>
<td>QueueDisabled</td>
<td>Queue disabled</td>
<td><a href="/queues/configuration/pause-purge/#pause-delivery">Unpause queue</a></td>
</tr>
<tr>
<td>10253</td>
<td>FreeTierLimitExceeded</td>
<td>Free tier limit exceeded</td>
<td>Upgrade to Workers Paid</td>
</tr>
</tbody>
</table>
<h3 id="500-type-errors">500 type errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Error</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>15000</td>
<td>UnknownInternalError</td>
<td>Unknown error</td>
</tr>
</tbody>
</table>
