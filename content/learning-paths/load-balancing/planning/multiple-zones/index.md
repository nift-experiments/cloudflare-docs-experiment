<p>If you want to set up load balancing for multiple hostnames or domains within your account, your approach would depend on the requirements for each hostname.</p>
<h2 id="shared-configurations">Shared configurations</h2>
<p>If you want to share a load balancing configuration across multiple hostnames, you can use the same load balancer through <code>CNAME</code> routing.</p>
<ol>
<li>When you <a href="/learning-paths/load-balancing/setup/">set up</a> the load balancer, create the load balancer on a new hostname (<code>lb.example.com</code>).</li>
<li>When you are ready to <a href="/learning-paths/load-balancing/setup/production-traffic/">route production traffic</a>, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create</a> a <code>CNAME</code> record on a hostname that points to the load balancer created in step 1 (<code>lb.example.com</code>).</li>
<li>Repeat steps 1 and 2 with all other hostnames.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9825.md")
</aside>
<h2 id="unique-configurations">Unique configurations</h2>
<p>If each zone needs unique load balancer configurations (failover order, routing), you should create separate load balancers. Since pools and monitors are configured at the account level, even different load balancers can share the same pools and monitors.</p>
<p>For simpler routing, create a load balancer on each hostname.</p>
<p>For more advanced routing, create multiple load balancers and then set up <a href="/rules/origin-rules/">Origin Rules</a> to route traffic to each load balancer based on specific characteristics of the request.</p>
