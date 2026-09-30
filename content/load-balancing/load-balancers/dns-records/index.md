<p>When you <a href="/load-balancing/load-balancers/create-load-balancer/">create a load balancer</a>, Cloudflare automatically creates an LB DNS record for the specified <strong>Hostname</strong>. This functionality allows you to use a hostname with or without an existing DNS record. Private load balancers do not receive an automatic DNS record. Instead, you can configure a hostname using your internal DNS system or by applying a <a href="/cloudflare-one/traffic-policies/dns-policies/#override">Gateway Firewall override</a> to a hostname.</p>
<h2 id="supported-records">Supported records</h2>
<p>For customers on non-Enterprise plans, Cloudflare supports load balancing for <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records.</p>
<p>For customers on Enterprise plans, Cloudflare supports load balancing for <code>A</code>, <code>AAAA</code>, <code>CNAME</code>, <strong>MX</strong>, and <strong>SRV</strong> records.</p>
<h2 id="priority-order">Priority order</h2>
<p>For hostnames with existing DNS records, the LB record takes precedence when it is more or equally specific:</p>
<ul>
<li>
<p><strong>Scenario 1</strong>:</p>
<ul>
<li><strong>A, AAAA, or CNAME</strong>: <code>x.example.com</code></li>
<li><strong>LB record</strong>: <code>x.example.com</code></li>
<li><strong>Outcome</strong>: LB record takes precedence because it is as specific as the DNS record.</li>
</ul>
</li>
<li>
<p><strong>Scenario 2</strong>:</p>
<ul>
<li><strong>A, AAAA, or CNAME</strong>: <code>y.example.com</code></li>
<li><strong>LB record</strong>: <code>*.example.com</code> (wildcard record)</li>
<li><strong>Outcome</strong>: DNS record takes precedence because it is more specific.</li>
</ul>
</li>
<li>
<p><strong>Scenario 3</strong>:</p>
<ul>
<li><strong>A, AAAA, or CNAME</strong>: <code>*.example.com</code></li>
<li><strong>LB record</strong>: <code>*.example.com</code></li>
<li><strong>Outcome</strong>: LB record takes precedence because it is as specific as the DNS record.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10389.md")
</aside>
<p>If the DNS record points to a <a href="/cloudflare-for-platforms/cloudflare-for-saas/">SaaS provider</a> and an active <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostname</a> exists, the custom hostname will take precedence over the Load Balancing record:</p>
<ul>
<li><strong>Scenario 4</strong>:
<ul>
<li><strong>CNAME</strong>: <code>x.example.com</code> with target to a Cloudflare for SaaS provider</li>
<li><strong>LB record</strong>: <code>x.example.com</code></li>
<li><strong>Active custom hostname on the SaaS provider side</strong>: <code>x.example.com</code></li>
<li><strong>Outcome</strong>: Custom hostname takes precedence.</li>
</ul>
</li>
</ul>
<h2 id="disabling-a-load-balancer">Disabling a load balancer</h2>
<p>When you disable a load balancer, requests to a specific hostname depend on your existing DNS records:</p>
<ul>
<li>If you have existing DNS records, these records will be served.</li>
<li>If there are no existing records, requests to the hostname will fail.</li>
</ul>
<p>In both cases, disabling your load balancer prevents traffic from going to any associated endpoint or fallback pools.</p>
<p>If you already have an existing <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record, be aware that the change may take some time to propagate due to <a href="/dns/manage-dns-records/reference/ttl/">Time to Live (TTL)</a> and any record changes is affected, as your local DNS cache may take longer to update.</p>
<h2 id="ssl-tls-coverage">SSL/TLS coverage</h2>
<p>Due to internal limitations, on <a href="/dns/zone-setups/partial-setup/">Partial (CNAME) setup</a> the Cloudflare <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificates</a> do not cover load balancing hostnames by default. This behavior will be corrected in the future.</p>
<p>As a current workaround for a domain or first-level subdomain (<code>lb.example.com</code>), create a <a href="/dns/manage-dns-records/how-to/create-dns-records/">proxied <code>CNAME</code>/<code>A</code>/<code>AAAA</code> record</a> for that hostname.</p>
<p>For example, if your load balancer hostname was <code>lb.example.com</code>, you could create the following record solely for the purpose of SSL/TLS coverage.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>IPv4 address</th>
<th>Proxy status</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>lb</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<p>Based on the <a href="#priority-order">priority order</a>, it would not receive any traffic because it is as equally specific as the LB hostname.</p>
<p>To get coverage for any deeper subdomain (<code>lb.dev.example.com</code>), purchase an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a>.</p>
