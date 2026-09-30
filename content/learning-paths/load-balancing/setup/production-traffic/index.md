<p>Now that you have set up your load balancer and verified everything is working correctly, you can put the load balancer on a live domain or subdomain:</p>
<ol>
<li>If you update your pools and monitors, review the pool health again to make sure everything is working as expected.</li>
<li>Confirm that your production hostname has the correct <a href="/load-balancing/load-balancers/dns-records/#priority-order">priority order</a> of DNS records and is covered by an <a href="/load-balancing/load-balancers/dns-records/#ssltls-coverage">SSL/TLS certificate</a>.</li>
<li>Configure your load balancer to receive production traffic, which could involve either:
<ul>
<li>Editing the <strong>Hostname</strong> of your existing load balancer.</li>
<li>Updating the <code>CNAME</code> record sending traffic to your load balancer.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9798.md")
</aside>
