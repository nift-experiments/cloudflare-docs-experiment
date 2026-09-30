<p>Consider the following steps to learn how to configure Private Network Load Balancing solution, using <a href="/cloudflare-wan/">Cloudflare WAN</a> (formerly Magic WAN) as the on-ramp and off-ramp to securely connect to your private or internal services.</p>
<p>One of the pre-requisites to using Private Network Load Balancing (PNLB) with Cloudflare WAN is having Cloudflare WAN set up in your account and having completed onboarding. You can connect with a Cloudflare One Appliance, or your own hardware via an IPsec or GRE tunnel. Check out the <a href="/cloudflare-wan/get-started/">Cloudflare WAN documentation</a> for more details or to get started.</p>
<h2 id="1-create-load-balancer-pools"><ol>
<li>Create Load Balancer Pools</li>
</ol></h2>
<p>Load Balancer Pools are logical groupings of endpoints — typically organized by physical datacenter or geographic region. The endpoints in the pool are the destinations where traffic is ultimately routed.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10353.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10352.md")
</aside>
<p>Pools can be created using either the Cloudflare dashboard or the API. Refer to the <a href="/load-balancing/pools/create-pool/#create-a-pool">Create a pool</a> documentation section for more information.</p>
<h2 id="2-create-an-account-load-balancer-with-a-private-ip"><ol start="2">
<li>Create an Account Load Balancer with a Private IP</li>
</ol></h2>
<ol>
<li>Go to <strong>Load Balancing</strong> at the account level and select <strong>Create a Load Balancer</strong>.</li>
<li>Select <strong>Private Load Balancer</strong>.</li>
<li>On the next step you can choose to associate this load balancer with either:</li>
</ol>
<ul>
<li>A CGNAT IP from the Cloudflare range or</li>
<li>A custom <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC1918 address</a>.</li>
</ul>
<ol start="4">
<li>Add a descriptive name to identify your Load Balancer.</li>
<li>Proceed through the setup.</li>
</ol>
<p>After selecting an IP address and completing the setup, you will be redirected to the Load Balancing dashboard. You can locate your load balancer using the search bar or by filtering for <strong>Private</strong> load balancers. Be sure to note the assigned IP address, as it will be required in the following steps.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10351.md")
</aside>
<h2 id="3-fqdn-override-optional"><ol start="3">
<li>FQDN override (optional)</li>
</ol></h2>
<p>If you want your load balancer and its endpoints to be transparently accessible to users via a hostname, you can create a DNS record in your internal DNS system or create an override in Cloudflare that maps the hostname to the Load Balancer's IP address. This ensures that traffic destined for the hostname resolves to the correct IP.</p>
<p>To create the override, follow these steps:</p>
<ol>
<li>In <strong>Gateway</strong>, select <strong>Firewall policies</strong>.</li>
<li>In the <strong>DNS</strong> tab, create an override where:
<ul>
<li>The <strong>Selector</strong> equals <code>Host</code></li>
<li>The <strong>Operator</strong> equals <code>is</code></li>
<li>The <strong>Value</strong> is the hostname you wish to associate with your load balancer.</li>
</ul>
</li>
<li>Set the <strong>Action</strong> to <em>Override</em>, and in <strong>Override Hostname</strong>, enter the IP address of your Private Load Balancer.</li>
</ol>
<p>Requests to the hostname will now resolve to your private load balancer.</p>
