<p>There's more to a load balancer than just distributing traffic, however.</p>
<p>After all, what good would it be if your load balancer and pools send a request to a server that's offline? Or one that's already overloaded with traffic? Ideally, your load balancer should only forward requests that a server can take care of.</p>
<p>That's where another part of the load balancing equation comes in: monitors and health checks.</p>
<pre><code class="language-mermaid">    flowchart RL&#10;      accTitle: Load balancing monitor flow&#10;      accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.&#10;      Monitor -- Health Monitor ----&gt; Endpoint2&#10;      Endpoint2 -- Response ----&gt; Monitor&#10;      subgraph Pool&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;</code></pre>
<h2 id="how-it-works">How it works</h2>
<p>A monitor issues health checks periodically to evaluate the health of each server within a pool.</p>
<div class="nb-glossary-definition"><p>Requests issued by a monitor at regular interval and — depending on the monitor settings — return a <strong>pass</strong> or <strong>fail</strong> value to make sure an endpoint is still able to receive traffic.</p>
<p>Each health monitor request is trying to answer two questions:</p>
<ol>
<li><strong>Is the endpoint offline?</strong>: Does the endpoint respond to the health monitor request at all? If so, does it respond quickly enough (as specified in the monitor's <strong>Timeout</strong> field)?</li>
<li><strong>Is the endpoint working as expected?</strong>: Does the endpoint respond with the expected HTTP response codes? Does it include specific information in the response body?</li>
</ol>
<p>If the answer to either of these questions is &quot;No&quot;, then the endpoint fails the health monitor request.</p></div>
<p>This system of request and response ensures that a load balancer knows which servers can handle incoming requests.</p>
