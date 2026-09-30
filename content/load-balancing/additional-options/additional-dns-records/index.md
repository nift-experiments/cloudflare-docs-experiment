<p>In addition to load balancing between DNS records used for IP resolution — <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records — Enterprise customers can also load balance between <strong>MX</strong> and <strong>SRV</strong> records.</p>
<h2 id="mx-records">MX records</h2>
<p>To load balance between multiple mail servers:</p>
<ol>
<li>Make sure you have the <a href="/dns/manage-dns-records/how-to/email-records/#send-and-receive-email">required DNS records</a> for your mail servers.</li>
<li><a href="/load-balancing/monitors/create-monitor/">Create a monitor</a> with a <strong>Type</strong> of <em>SMTP</em>.</li>
<li><a href="/load-balancing/pools/create-pool/">Create a pool</a> with your mail servers and attach the newly created monitor.</li>
<li><a href="/load-balancing/load-balancers/create-load-balancer/">Create a load balancer</a> that includes your newly created pools. Since it will forward SMTP traffic, the load balancer should be <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">unproxied (DNS-only)</a>.</li>
</ol>
<h2 id="srv-records">SRV records</h2>
<p>To load balance between different <strong>SRV</strong> records, which contain significantly more information than many other DNS records:</p>
<ol>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create your SRV records</a>.</li>
<li><a href="/load-balancing/monitors/create-monitor/">Create a monitor</a> with a <strong>Type</strong> of <em>UDP-ICMP</em> or <em>TCP</em>.</li>
<li><a href="/load-balancing/pools/create-pool/">Create a pool</a> with your various SRV records and attach the newly created monitor.</li>
<li><a href="/load-balancing/load-balancers/create-load-balancer/">Create a load balancer</a> that includes your newly created pools. This load balancer should be <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">unproxied (DNS-only)</a>.</li>
</ol>
