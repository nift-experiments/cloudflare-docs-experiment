<p>If you have an alias domain that only forwards traffic to another domain (that is, the domain does not have an associated origin server of its own), you can set up redirects directly within Cloudflare.</p>
<ol>
<li>
<p><a href="/fundamentals/manage-domains/#add-a-domain-to-cloudflare">Add</a> your alias domain (for example, <code>previous.com</code>) to Cloudflare.</p>
</li>
<li>
<p>Make sure that your alias domain has a proxied <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS A or CNAME record</a> that properly resolves DNS queries. You may also want to include a subdomain DNS record for <code>www</code>.</p>
<p>Use the IP address <code>192.0.2.1</code> for the <code>A</code> record. This address does not route traffic to an origin server but allows Cloudflare to apply rules, redirects, and Workers to incoming traffic. The equivalent IP address for an <code>AAAA</code> record is <code>100::</code>.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>IPv4 address</strong></th>
<th><strong>Proxy status</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>@</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Use <a href="/rules/url-forwarding/">Redirect rules</a> to forward traffic from your alias domain to your other domain.</li>
</ol>
<p>This example will redirect all requests for <code>smallshop.example.com</code> to a different hostname using HTTPS, keeping the original path and query string.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8901.md")
</div>
<p>For example, the redirect rule would perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>Target URL</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>http://smallshop.example.com/</code></td>
<td><code>https://globalstore.example.net/</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://smallshop.example.com/admin/?logged_out=true</code></td>
<td><code>https://globalstore.example.net/admin/?logged_out=true</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>https://smallshop.example.com/?all_items=1</code></td>
<td><code>https://globalstore.example.net/?all_items=1</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>http://example.com/about/</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
