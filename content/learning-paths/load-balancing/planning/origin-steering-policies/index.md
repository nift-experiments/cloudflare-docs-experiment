<p>Endpoint steering customizes how each <a href="/load-balancing/pools/">pool</a> distributes requests to its associated endpoints.</p>
<p>These distributions are a combination of two properties:</p>
<ul>
<li>The endpoint steering <a href="#policies">policy</a> chosen for your pool.</li>
<li>The <a href="#weights">weights</a> assigned to each endpoint.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9823.md")
</aside>
<hr />
<h2 id="policies">Policies</h2>
<p>When you <a href="/load-balancing/pools/create-pool/">create a pool</a>, you have to choose an option for <strong>Endpoint Steering</strong>.</p>
<hr />
<h2 id="weights">Weights</h2>
<p>The weight assigned to an endpoint controls the percentage of pool traffic sent to that endpoint. By default, all endpoints within a pool have a weight of <strong>1</strong>.</p>
<p>If you leave each endpoint with the default setting and choose a <strong>Random</strong> endpoint steering policy, each endpoint will receive the same percentage of traffic. If you use a <strong>Hash</strong> policy, that percentage will vary based on the IP distribution of your requests.</p>
<h3 id="customize-weights">Customize weights</h3>
<p>To customize weights when you <a href="/load-balancing/pools/create-pool/">create or edit a pool</a>, set the <strong>Weight</strong> to a number between 0 and 1 (expressed in increments of .01). Cloudflare will then send traffic to that pool based on a combination of your endpoint steering policy and the following formula.</p>
<pre><code class="language-txt">% of traffic to endpoint = endpoint weight ÷ sum of all weights in the pool&#10;</code></pre>
<details class="nb-details"><summary>Endpoint weight example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9824.md")
</div></details>
<p>An endpoint with a weight of <strong>0</strong> should not receive any traffic sent to that pool (though the endpoint will still receive health monitor requests).</p>
<p>You can also see this value in the <strong>Percent</strong> field when creating or editing a pool in the dashboard.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/9822.md")
</aside>
<h3 id="limitations">Limitations</h3>
<p>If you choose <strong>Hash</strong> for your <strong>Endpoint Steering</strong> or enable <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>, these options can affect traffic distribution.</p>
<p>Additionally, session affinity takes precedence over any selected weight or endpoint steering policy.</p>
<p>When using <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">DNS-only load balancing</a>, DNS resolvers may cache resolved IPs for clients and affect traffic distribution.</p>
