<p>This page provides a simplified overview of the three main components of the Cloudflare Load Balancing solution and how they relate to one another.</p>
<h2 id="load-balancers">Load balancers</h2>
<p>For a hostname (<code>blog.example.com</code>) to resolve, the Domain Name System (DNS) must return an IP address, where the website or application is hosted (origin).</p>
<p>When you set up a public load balancer, Cloudflare automatically creates an <a href="/load-balancing/load-balancers/dns-records/">LB DNS record</a> for the specified hostname. This means that, according to a <a href="/load-balancing/load-balancers/dns-records/#priority-order">priority order</a>, instead of simply returning an IP address, the logic you introduced using the Cloudflare Load Balancing solution will be considered.</p>
<p>Note that you can use the root domain as a Load Balancer hostname. When doing so, make sure you enter the hostname without including the auto-generated dot that typically precedes your zone's name.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10322.md")
</aside>
<pre><code class="language-mermaid">    flowchart LR&#10;      accTitle: Load balancing flow&#10;      accDescr: Load balancing involves a load balancer, pools, endpoints, monitors, and health monitors.&#10;      B[Request 1] --&gt; A&#10;      C[Request 2] --&gt; A&#10;      D[Request 3] --&gt; A&#10;      A[Load balancer] -- Request 1 --&gt; P1&#10;      A -- Request 2 --&gt; P2&#10;      A -- Request 3 --&gt; P3&#10;      subgraph P1 [Pool 1]&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;      subgraph P2 [Pool 2]&#10;      Endpoint3((Endpoint 3))&#10;      Endpoint4((Endpoint 4))&#10;      end&#10;      subgraph P3 [Pool 3]&#10;      Endpoint5((Endpoint 5))&#10;      Endpoint6((Endpoint 6))&#10;      end&#10;</code></pre>
<h2 id="pools">Pools</h2>
<p>Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint per pool — it depends on what best suits your use case.</p>
<p>For example, if you are only using Cloudflare to globally distribute traffic across regions (<a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">global traffic steering</a>), each pool could represent one region and, within each region, you could have one endpoint that represents the entry point to your data center.</p>
<p>Cloudflare <a href="/load-balancing/private-network/">Private Network Load Balancing</a> solution and <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">endpoint steering</a> capabilities enable you to also load balance traffic between your servers within a data center. In this use case, each pool would represent a data center and contain several endpoints that represent your servers.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-tiered-cache-interaction">Smart Tiered Cache interaction</h3>
@markup("md", "content/.markup/bodies/10321.md")
</aside>
<h2 id="endpoints">Endpoints</h2>
<div class="nb-glossary-definition"><p>Endpoints refer to any service or hardware that intercepts and processes incoming public or private traffic.</p>
<p>Examples of endpoints include origins, hostnames, private or public IP addresses, virtual IP addresses (VIPs), servers, and other dedicated hardware boxes.</p></div>
<h2 id="monitors">Monitors</h2>
<p>Finally, monitors are the component you can use to guarantee only <a href="/load-balancing/understand-basics/health-details/">healthy pools</a> are considered for traffic distribution.</p>
<p>When you configure a monitor and attach it to endpoints, the monitor will issue health monitor requests to your endpoints at regular intervals. This process makes it possible for your load balancer to intelligently handle traffic, considering which endpoints are actually available.</p>
<pre><code class="language-mermaid">    flowchart RL&#10;      accTitle: Load balancing monitor flow&#10;      accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.&#10;      Monitor -- Health Monitor ----&gt; Endpoint2&#10;      Endpoint2 -- Response ----&gt; Monitor&#10;      subgraph Pool&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10320.md")
</aside>
