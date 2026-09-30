<p>Before setting up anything related to your load balancer, make sure you test that production hostnames meet the following criteria:</p>
<ul>
<li>Based on the <a href="/load-balancing/load-balancers/dns-records/#priority-order">priority order</a> of DNS records, they will receive the intended amount of traffic.</li>
<li>Each hostname is covered by an <a href="/load-balancing/load-balancers/dns-records/#ssltls-coverage">SSL/TLS certificate</a>.</li>
</ul>
<p>After confirming each of these conditions are met, you can proceed with setting up your load balancer.</p>
<h2 id="routing-strategy">Routing strategy</h2>
<p>Depending on your preferences and infrastructure, you might route traffic to your load balancer in different ways:</p>
<ul>
<li>For most customers, it's simpler to create the load balancer on the hostname directly (<code>www.example.com</code>).</li>
<li>However, you could also create the load balancer on another hostname (<code>lb.example.com</code>) and then route traffic using a <code>CNAME</code> record on <code>test.example.com</code> that points to <code>lb.example.com</code>.</li>
</ul>
