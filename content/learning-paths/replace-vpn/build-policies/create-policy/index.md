<p>To ensure holistic security precautions, we recommend securing each distinct private application with at least two policies:</p>
<ul>
<li>
<p>A <a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policy</a> with the appropriate identity and device posture values, targeting the domain list that defines your application. Policy enforcement happens at the request resolution event, before the user's device makes a connection request to the application itself; if denied here, no traffic will reach your private network.</p>
</li>
<li>
<p>A <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policy</a> with the same identity and device posture values as the DNS policy, targeting the IP list that defines your application. You can optionally include the domain list by matching the SNI header. Then, you can include any combinations of ports or protocols that are relevant for application access. Network policy enforcement happens after the user passes the DNS policy, when the user's device attempts to connect to the target application.</p>
</li>
</ul>
<h2 id="create-a-gateway-policy">Create a Gateway policy</h2>
<p>To create a new policy, open the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</p>
<h2 id="example-dns-policy">Example DNS policy</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9974.md")
</div></div>
<h2 id="example-network-policy">Example network policy</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9978.md")
</div></div>
<h3 id="catch-all-policy">Catch-all policy</h3>
<p>We recommend adding a catch-all policy to the bottom of your network policy list. An effective Zero Trust model should prioritize default-deny actions to avoid any overly permissive policy building. For example,</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9982.md")
</div></div>
<p>Network policies are evaluated in <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">top-down order</a>, so if a user does not match an explicitly defined policy for an application, they will be blocked.
To learn how multiple policies interact, refer to <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Order of enforcement</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9970.md")
</aside>
