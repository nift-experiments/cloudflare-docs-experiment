<h2 id="413-payload-too-large">413 Payload Too Large</h2>
<p>The <code>413 Payload Too Large</code> status code indicates that the server refuses to process the request because the payload sent by the client exceeds the server's acceptable size limit. The server may optionally close the connection. If this refusal would only happen temporarily, then the server should send a <code>Retry-After</code> header to specify when the client should try the request again.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>The <code>413 Payload Too Large</code> status code often occurs when clients attempt to upload large files, such as videos or images, or send oversized request bodies, like JSON or XML payloads, that exceed the server's size limits. This can also happen during file transfers or API requests involving large datasets, prompting the server to reject the request.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>The upload limit for the Cloudflare API depends on your plan. If you exceed this limit, your API call will receive a <code>413 Request Entity Too Large</code> error.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Max upload size</td>
<td>100 MB</td>
<td>100 MB</td>
<td>200 MB</td>
<td>Up to 5 GB</td>
</tr>
</tbody>
</table>
<p>Keep in mind, customers can adjust the <strong>Maximum Upload Size</strong> from the zone's <strong>Network</strong> page. Enterprise customers can self-serve any value up to 5 GB; uploads larger than 5 GB require additional configuration — contact your account team. Setting the limit below the size of an incoming request causes a <code>413</code>.</p>
<p>If you require a larger upload, break up requests into smaller chunks, change your DNS record to <a href="/dns/proxy-status/#dns-only-records">DNS-only</a>, or <a href="/billing/manage/change-plan/">upgrade your plan</a>.</p>
