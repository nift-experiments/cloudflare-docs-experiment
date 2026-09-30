<p>You can load balance your traffic at different levels of the networking stack, such as:</p>
<ul>
<li><a href="#layer-7-load-balancing">Layer 7 (HTTP/HTTPS)</a> (most common)</li>
<li><a href="#dns-only-load-balancing">DNS-only</a></li>
<li><a href="#layer-4-load-balancing">Layer 4 (TCP)</a></li>
</ul>
<hr />
<h2 id="layer-7-load-balancing">Layer 7 load balancing</h2>
<p>Layer 7 load balancers direct traffic to specific endpoints based on information present in each HTTP/HTTPS request (HTTP headers, URI, cookies, type of data, etc.).</p>
<p>When a client visits your application, Cloudflare directs their request to a healthy endpoint (determined by your <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policy</a> and <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights">endpoint weights</a>).</p>
<p>Cloudflare performs layer 7 load balancing when traffic to your hostname is <strong>proxied</strong> through Cloudflare. In the <strong>Load Balancing</strong> dashboard, these load balancers are marked with an orange cloud.</p>
<p><img src="/assets/upstream/images/load-balancing/proxied-load-balancer.png" alt="DNS-only load balancers are marked with an orange cloud" /></p>
<aside class="nb-aside warning">
@markup("md", "content/.markup/bodies/10319.md")
</aside>
<h3 id="benefits">Benefits</h3>
<p>In comparison to DNS-only load balancing, layer 7 load balancing:</p>
<ul>
<li>Protects endpoints from DDoS attacks by hiding their IP addresses.</li>
<li>Offers faster failover and more accurate routing, which can otherwise be affected by DNS caching.</li>
<li>Integrates with other Cloudflare features such as caching, Workers, and the WAF.</li>
<li>Reduces authoritative queries against Cloudflare, which can potentially save money for customers with usage-based billing.</li>
<li>Supports customized <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a> and <a href="/load-balancing/understand-basics/session-affinity/#endpoint-drain">endpoint drain</a>.</li>
<li>More accurately geo-locates traffic, using the data center associated with the user making the request instead of the data center associated with a user's recursive resolver.</li>
<li>Supports private IP addresses with <a href="/load-balancing/private-network/">Private Network Load Balancing</a>.</li>
</ul>
<hr />
<h2 id="dns-only-load-balancing">DNS-only load balancing</h2>
<p>DNS-only load balancers route traffic by returning specific IP addresses in response to a client's DNS query.</p>
<p>When a client visits your application, Cloudflare provides the address for a healthy endpoint (determined by your <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policy</a> and <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">endpoint-level steering policy</a>). However, Cloudflare relies on DNS resolvers respecting the short TTL to re-query Cloudflare's DNS for an updated list of healthy addresses. If a client has a cached DNS response, they will go to their previous destination, potentially ignoring your load balancer.</p>
<p>Cloudflare performs DNS-only load balancing when traffic to your hostname is <strong>not proxied</strong> through Cloudflare. In the <strong>Load Balancing</strong> dashboard, these load balancers are marked with a gray cloud.</p>
<p><img src="/assets/upstream/images/load-balancing/dns-only-load-balancer.png" alt="DNS-only load balancers are marked with a gray cloud" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10318.md")
</aside>
<h3 id="benefits-1">Benefits</h3>
<p>If your load balancer is attached to a hostname used for an <a href="/load-balancing/additional-options/additional-dns-records/"><code>MX</code> or <code>SRV</code> record</a> — and not an <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record — its proxy mode should be <strong>DNS-only</strong>.
<br /></p>
<h3 id="limitations">Limitations</h3>
<p>In comparison to proxied, layer 7 load balancing, DNS-only load balancing:</p>
<ul>
<li>Does not hide the IP addresses of your endpoints, leaving them vulnerable to DDoS attacks.</li>
<li>Performs slower failover and less accurate routing, because it has to rely on DNS resolvers and cache settings.</li>
<li>Cannot integrate with other Cloudflare features such as caching, Workers, and the WAF.</li>
<li>Increases authoritative queries against Cloudflare, which can potentially cost more for customers with usage-based billing.</li>
<li>Does not support <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>. Alternatively, you can use <a href="/load-balancing/additional-options/dns-persistence/">DNS persistence</a>.</li>
<li>Geo-locates traffic based on the data center associated with the ECS source address, if available. If not available, geo-locates based on a user's recursive resolver, which can sometimes cause issues with <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/">latency-based steering</a>.</li>
<li>Does not support <a href="/load-balancing/private-network/">Private Network Load Balancing</a>.</li>
</ul>
<hr />
<h2 id="layer-4-load-balancing">Layer 4 load balancing</h2>
<p>Layer 4 load balancers route traffic by forwarding traffic to certain ports or IP addresses.</p>
<p>Cloudflare currently only supports layer 4 load balancing as part of <a href="/spectrum/about/load-balancer/">Cloudflare Spectrum</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10317.md")
</aside>
