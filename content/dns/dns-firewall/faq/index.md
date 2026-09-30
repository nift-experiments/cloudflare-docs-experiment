<p>Consider the answers for frequently asked questions about Cloudflare DNS Firewall.</p>
<h2 id="how-does-dns-firewall-choose-a-backend-nameserver-to-query-upstream">How does DNS Firewall choose a backend nameserver to query upstream?</h2>
<p>DNS Firewall alternates between a customer's nameservers, using an algorithm that is more likely to send queries to the faster upstream nameservers than slower nameservers.</p>
<h2 id="how-long-does-dns-firewall-cache-a-stale-object">How long does DNS Firewall cache a stale object?</h2>
<p>DNS Firewall sets cache longevity according to allocated memory.</p>
<p>As long as there is enough allocated memory, Cloudflare does not clear items from the cache forcefully, even when the TTL expires. This feature allows Cloudflare to serve stale objects from cache if your nameservers are offline.</p>
<h2 id="does-the-dns-firewall-cache-servfail">Does the DNS Firewall cache SERVFAIL?</h2>
<p>Yes. <code>SERVFAIL</code> is treated like any other negative answer for caching purposes. The default TTL is 30 seconds. You can set a different negative cache TTL on your cluster in the Cloudflare dashboard, or via the <a href="/api/resources/dns_firewall/methods/edit/">API</a> (<code>negative_cache_ttl</code> parameter).</p>
<h2 id="does-dns-firewall-support-edns-client-subnet-ecs">Does DNS Firewall support EDNS Client Subnet (ECS)?</h2>
<p>Yes. Often, DNS providers want to see a client's IP via <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7704.md")
</div> ([RFC 7871](https://www.rfc-editor.org/rfc/rfc7871.html)) because they serve geographically specific DNS answers based on the client's IP. With EDNS Client Subnet enabled, the DNS Firewall will forward the client's IP subnet along with the DNS query to the upstream nameserver.
<p>When EDNS is enabled, the DNS Firewall gives out the geographically correct answer in cache based on the client IP subnet. To do this, the DNS Firewall segments its cache. For example:</p>
<ol>
<li>A resolver says it is looking for an answer for client <code>192.0.2.0/24</code>.</li>
<li>The DNS Firewall will proxy the request to the upstream nameserver for the answer.</li>
<li>The DNS Firewall will cache the answer from the upstream nameserver, but only for that <code>/24</code>.</li>
<li><code>203.0.113.0/24</code> now asks the same DNS question and the answer is again returned from the upstream nameserver instead of the cache.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7703.md")
</aside>
<p>Some resolvers might not be sending any EDNS data. When you enable ECS fallback on your cluster in the Cloudflare dashboard — or set the <code>ecs_fallback</code> parameter to <code>true</code> via the <a href="/api/resources/dns_firewall/methods/edit/">API</a> — DNS Firewall will forward the IP subnet of the resolver instead, only if there is no EDNS data present in the incoming DNS query.</p>
<h2 id="does-dns-firewall-cache-negative-answers">Does DNS Firewall cache negative answers?</h2>
<p>Yes. The default TTL is 30 seconds. You can configure the negative cache TTL on your cluster in the Cloudflare dashboard, or via the <a href="/api/resources/dns_firewall/methods/edit/">API</a> (<code>negative_cache_ttl</code> parameter). This will affect the TTL of responses with status <code>REFUSED</code>, <code>NXDOMAIN</code>, or <code>SERVFAIL</code>.</p>
<h2 id="how-can-i-set-ptr-records-for-nameserver-hostnames">How can I set PTR records for nameserver hostnames?</h2>
<p>To set up PTR records for the DNS Firewall cluster IPs that point to your nameserver hostnames, use the following API endpoints:</p>
<ul>
<li><a href="/api/resources/dns_firewall/subresources/reverse_dns/methods/get/">Show DNS Firewall Cluster Reverse DNS</a></li>
<li><a href="/api/resources/dns_firewall/subresources/reverse_dns/methods/edit/">Update DNS Firewall Cluster Reverse DNS</a></li>
</ul>
