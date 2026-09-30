<h2 id="prerequisites">Prerequisites</h2>
<p>To enable load balancers to be deployed to the <a href="/china-network/">China Network</a>, your zone will need to meet the following two criteria:</p>
<ol>
<li>A valid <a href="/china-network/concepts/icp/">ICP license</a> for the zone in question.</li>
<li>The zone must be provisioned with access to the China Network.</li>
</ol>
<p>Once these two criteria are met, any newly created load balancer will be automatically deployed to the China Network. When choosing a region for a pool's health checks, <code>China</code> is now available to be selected in both the dashboard and API.</p>
<p>You can also create a load balancer by sending a <code>POST</code> request to the following endpoint. To deploy to the China Network with the API, the <code>networks</code> array in the API call must contain <code>jdcloud</code> as a value in addition to <code>cloudflare</code>. Refer to the <a href="/api/resources/load_balancers/methods/create/">Cloudflare API documentation</a> for details on the required fields and their formats.</p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p>Load balancers deployed to the China Network currently have the following limitations:</p>
<ul>
<li>Only cookie-based session affinity is supported.</li>
<li>Private network off-ramps (Tunnel, GRE, IPsec) are not supported.</li>
<li>Private Network Load Balancing is not available on the China Network.</li>
</ul>
