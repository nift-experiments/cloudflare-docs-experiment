<p>To randomly distribute traffic across multiple servers, set up multiple DNS <code>A</code> or <code>AAAA</code> records for the same hostname.</p>
<p>Use this setup for simple, <a href="https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/">round-robin load balancing</a>. If you need more fine-grained control over traffic distribution — including automatic failover, intelligent routing, and more — set up our <a href="/load-balancing/">add-on load balancing service</a>.</p>
<h2 id="example-scenario">Example scenario</h2>
<p>The following example illustrates how you would distribute traffic intended for <code>www.example.com</code>. Though the example uses <code>A</code> records, you could also use <code>AAAA</code> records.</p>
<p>After <a href="/fundamentals/account/create-account/">creating an account</a> and <a href="/dns/zone-setups/full-setup/setup/">updating your nameservers</a> for <code>example.com</code>, you might <a href="/dns/manage-dns-records/how-to/create-dns-records/">create multiple subdomain DNS records</a> for <code>www</code>:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>IPv4 address</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.1</code></td>
</tr>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.2</code></td>
</tr>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.3</code></td>
</tr>
</tbody>
</table>
<p>The exact behavior of your DNS routing would depend on the <a href="/dns/proxy-status/">proxy status</a> of each record.</p>
<h3 id="all-records-unproxied">All records unproxied</h3>
<p>If all associated records were unproxied, any request to Cloudflare's nameservers would return the three <code>A</code> records you previously added.</p>
<p>Each client (oftentimes a browser), would decide which IP address to send the request to. If one IP address fails, the client would choose another option. All requests would be sent directly to the origin server (either <code>192.0.2.1</code>, <code>192.0.2.2</code>, or <code>192.0.2.3</code>, using the example above).</p>
<h3 id="all-records-proxied-recommended">All records proxied (recommended)</h3>
<p>If all associated records were proxied, any request to Cloudflare's nameservers would return two <code>A</code> records from Cloudflare's list of IP addresses.</p>
<p>Each client (oftentimes a browser) would decide which Cloudflare IP address to send the request to. Cloudflare would then receive that request and — if Cloudflare needed to contact your origin server — we would pick one of the three IP addresses specified in your DNS records (either <code>192.0.2.1</code>, <code>192.0.2.2</code>, or <code>192.0.2.3</code>, using the example above).</p>
<p>Beyond reducing requests to your origin server, this setup allows your application to take advantage of Cloudflare's <a href="/fundamentals/security/protect-your-origin-server/#zero-downtime-failover">Zero downtime failover</a>. When a request to one IP address fails, Cloudflare automatically retries the request to other IP addresses associated with the same hostname. This behavior prevents end users from experiencing downtime.</p>
<h3 id="unproxied-and-proxied-records">Unproxied and proxied records</h3>
<p>If you have a mix of proxied and unproxied records associated with the same hostname, requests happen as if you had <a href="#all-records-proxied-recommended">all proxied records</a>.</p>
<p>This approach is not typically recommended because it can lead to unexpected behavior. For example, if you had two unproxied records and one proxied record, Cloudflare would treat all records as proxied. However, if you deleted the single proxied record, your remaining two unproxied records would immediately be treated as unproxied.</p>
<p>We recommend either using all proxied or all unproxied records to avoid surprises when you make changes to your DNS records.</p>
