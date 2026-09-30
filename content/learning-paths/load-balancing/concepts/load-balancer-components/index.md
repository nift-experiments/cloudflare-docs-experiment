<p>At it's most basic, load balancing is made up of three components:</p>
<ul>
<li><strong>Pools</strong>: Which contain one or more endpoints.</li>
<li><strong>Endpoints</strong>: Which respond to individual requests.</li>
<li><strong>A load balancer</strong>: Which decides which traffic goes to each pool.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Normally, requests to your application would go to individual servers directly.</p>
<p>With a load balancer, requests first go through the load balancer. Your load balancer then routes requests to specific pools.</p>
<pre><code class="language-mermaid">    flowchart LR&#10;      accTitle: Load balancing flow&#10;      accDescr: Load balancing involves a load balancer, pools, endpoints, monitors, and health monitors.&#10;      B[Request 1] --&gt; A&#10;      C[Request 2] --&gt; A&#10;      D[Request 3] --&gt; A&#10;      A[Load balancer] -- Request 1 --&gt; P1&#10;      A -- Request 2 --&gt; P2&#10;      A -- Request 3 --&gt; P3&#10;      subgraph P1 [Pool 1]&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;      subgraph P2 [Pool 2]&#10;      Endpoint3((Endpoint 3))&#10;      Endpoint4((Endpoint 4))&#10;      end&#10;      subgraph P3 [Pool 3]&#10;      Endpoint5((Endpoint 5))&#10;      Endpoint6((Endpoint 6))&#10;      end&#10;</code></pre>
<br/>
<p>Within each pool, requests then go to individual endpoints. And that endpoint is what responds to the request.</p>
<pre><code class="language-mermaid">    flowchart LR&#10;      accTitle: Pool traffic flow&#10;      accDescr: When an incoming request reaches a pool, it then goes to an endpoint within the pool.&#10;    A[Request 1] --Routed by pool--&gt; Endpoint2&#10;      subgraph P1 [Pool]&#10;        Endpoint1((Endpoint 1))&#10;        Endpoint2((Endpoint 2))&#10;      end&#10;</code></pre>
<br/>
<p>This progression of load balancer --&gt; pool --&gt; endpoint is the core part of how a load balancer works.</p>
