<p>Cloudflare Logpull is a REST API for consuming request logs over HTTP. These logs contain data related to the connecting client, the request path through the Cloudflare network, and the response from the origin web server. This data is useful for enriching existing logs on an origin server. Logpull is available to customers on the Enterprise plan.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10479.md")
</aside>
<p>Review the following content to learn more about Logpull.</p>
<ul class="directory-listing"><li><a href="/logs/logpull/understanding-the-basics/">Understanding the basics</a></li><li><a href="/logs/logpull/enabling-log-retention/">Enabling log retention</a></li><li><a href="/logs/logpull/requesting-logs/">Requesting logs</a></li><li><a href="/logs/logpull/additional-details/">Additional details</a></li></ul>
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
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h3 id="limitation">Limitation</h3>
<p>Logpull is unavailable when the Customer Metadata Boundary (CMB) is set outside the US region. Specifically, it does not work when CMB is restricted to the EU-only setting. For more details, refer to the <a href="/data-localization/">Cloudflare Data Localization</a> documentation.</p>
