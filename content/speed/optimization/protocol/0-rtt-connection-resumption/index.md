<p>Zero round trip time resumption (0-RTT) improves performance for clients who have previously connected to your website, reducing latency for returning users. This feature is especially beneficial for those who frequently visit your application or connect over mobile networks.</p>
<p>We support 0-RTT for GET, HEAD, and OPTIONS requests, facilitating faster responses for these types of requests. Note that 0-RTT is not supported for POST requests.</p>
<p>In line with 0-RTT standards, we add the <code>Early-Data: 1</code> header to 0-RTT requests, which allows origin servers to identify when a request has used 0-RTT resumption. Customers should be able to see the <code>Early-Data: 1</code> header for any 0-RTT requests connecting to their origin.</p>
<p>For more information on 0-RTT, including its functionality and potential limitations, refer to our <a href="https://blog.cloudflare.com/even-faster-connection-establishment-with-quic-0-rtt-resumption/">blog post</a>.</p>
<h2 id="availability">Availability</h2>
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
</tbody>
</table>
<h2 id="enable-0-rtt-connection-resumption">Enable 0-RTT Connection Resumption</h2>
<p>By default, 0-RTT Connection Resumption is not enabled on your Cloudflare application.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13924.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13921.md")
</aside>
