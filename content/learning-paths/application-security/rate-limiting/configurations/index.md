<p>Let's step through an example. If your <code>/create-account</code> page is being attacked, you will create a rule to limit the amount of requests, per <code>counting characteristic</code>, that you feel comfortable permitting through to your origin.</p>
<p>The rule below is being created on the <code>free</code> plan, which limits configuration options. The rule will trigger if the URI path matches <code>/create-account</code>, from the same IP address, <em>after</em> 5 requests and within a 10 second window, <a href="/waf/rate-limiting-rules/request-rate/">within each Cloudflare datacenter</a>, globally.</p>
<hr />
<p><img src="/assets/upstream/images/waf/rate-limiting-rules/rl-create-account-endpoint.png" alt="rate-limiting-create-account-endpoint" />
<img src="/assets/upstream/images/waf/rate-limiting-rules/rl-create-account-endpoint-block.png" alt="rate-limiting-create-account-endpoint-block" /></p>
<hr />
<h2 id="advanced-configuration">Advanced configuration</h2>
<p>In the previous module, we reviewed the various configurations available per plan. Using the same endpoint as an example, let us walk through another example, but with the additional advanced configurations.</p>
<p>The rule below is being created on the <code>enterprise</code> plan, so we are no longer limited to default configurations.</p>
<ul>
<li>The rule will also limit the number of requests to <code>/create-account</code>, but will only trigger against <code>POST</code> requests. In the basic example, even requests with the <code>GET</code> method will increment the counter.</li>
<li>Requests that do not have a <a href="/ssl/client-certificates/">client certificate (mTLS)</a>, will increment the counter.</li>
<li>Requests will be counted using the <a href="/waf/rate-limiting-rules/parameters/#use-cases-of-ip-with-nat-support">IP with NAT support</a> characteristic.</li>
<li>Within a 1 minute period, for each counted entity, if the number of requests exceeds 10, then the user will be presented with a <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a> for a custom duration of 1 day.</li>
</ul>
<p><img src="/assets/upstream/images/waf/rate-limiting-rules/rl-advanced-config.png" alt="rate-limiting-advanced-config-1" /></p>
<hr />
<h2 id="best-practices">Best practices</h2>
<p>Rules that match identical criteria can be stacked together. For example, instead of creating just a single rule for <code>/create-account</code>, you can create multiple rules that match the same path but have different <code>counting characteristics</code> or <code>request limits</code> to protect against a threat that might behave dynamically.</p>
