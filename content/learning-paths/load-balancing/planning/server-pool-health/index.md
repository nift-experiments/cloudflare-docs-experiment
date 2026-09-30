<p>As discussed before, a monitor issues health checks periodically to evaluate the health of each server within a pool.</p>
<pre><code class="language-mermaid">    flowchart RL&#10;      accTitle: Load balancing monitor flow&#10;      accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.&#10;      Monitor -- Health Monitor ----&gt; Endpoint2&#10;      Endpoint2 -- Response ----&gt; Monitor&#10;      subgraph Pool&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;</code></pre>
<br/>
<div class="nb-glossary-definition"><p>Requests issued by a monitor at regular interval and — depending on the monitor settings — return a <strong>pass</strong> or <strong>fail</strong> value to make sure an endpoint is still able to receive traffic.</p>
<p>Each health monitor request is trying to answer two questions:</p>
<ol>
<li><strong>Is the endpoint offline?</strong>: Does the endpoint respond to the health monitor request at all? If so, does it respond quickly enough (as specified in the monitor's <strong>Timeout</strong> field)?</li>
<li><strong>Is the endpoint working as expected?</strong>: Does the endpoint respond with the expected HTTP response codes? Does it include specific information in the response body?</li>
</ol>
<p>If the answer to either of these questions is &quot;No&quot;, then the endpoint fails the health monitor request.</p></div>
<hr />
<h2 id="customizations">Customizations</h2>
<p>Based on the characteristics of your server pools, you have several customization options that affect how and whether a server is considered unhealthy.</p>
<h3 id="pool-level-settings">Pool-level settings</h3>
<h4 id="health-threshold">Health threshold</h4>
<p>The Health Threshold is the number of healthy endpoints for the pool as a whole to be considered <em>Healthy</em> and receive traffic based on pool order in a load balancer. Increasing this number makes the pool more reliable, but also more likely to become unhealthy.
<br/></p>
<h4 id="health-monitor-regions">Health monitor regions</h4>
<p>For each option selected in a pool's <strong>Health Monitor Regions</strong>, Cloudflare sends health monitor requests from three separate data centers in that region.</p>
<p><img src="/assets/upstream/images/load-balancing/health-check-component.png" alt="Health monitor requests come from three data centers within each selected region." /></p>
<p>If the majority of data centers for that region pass the health monitor requests, that region is considered healthy. If the majority of regions is healthy, then the endpoint itself will be considered healthy.</p>
<h5 id="configurations">Configurations</h5>
<p><strong>All Data Centers (Enterprise only)</strong></p>
<p>Health monitor probes are sent from every single data center in Cloudflare’s network to the endpoints within the associated pool. This allows probes to hit each endpoint during intervals set by the customer.</p>
<p><strong>All Regions (Enterprise only)</strong></p>
<p>Three health monitor probes per region are sent to each endpoint in the associated pool. There are a total of 13 regions, resulting in 39 probes.</p>
<p><strong>Regional</strong></p>
<p>Three health monitor probes are sent from each specified region within the pool configuration.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9819.md")
</aside>
<hr />
<h3 id="monitor-level-settings">Monitor-level settings</h3>
<p>When you <a href="/load-balancing/monitors/create-monitor/">create a monitor</a>, there are several configuration settings you can adjust based on the characteristics of the attached pools:</p>
<details class="nb-details"><summary>Basic settings</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9820.md")
</div></details>
<details class="nb-details"><summary>Advanced settings</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9821.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/9818.md")
</aside>
<hr />
<h3 id="fallback-pool">Fallback pool</h3>
<p>You also need to decide which of the associated pools in a load balancer should be the fallback pool.</p>
<p>This pool is meant to be the pool of last resort, meaning that its health is not taken into account when directing traffic.</p>
<p>Fallback pools are important because traffic still might be coming to your load balancer even when all the pools are unreachable (disabled or unhealthy). Your load balancer needs somewhere to route this traffic, so it will send it to the fallback pool.</p>
