<h2 id="some-workers-subrequests-are-counted-as-separate-requests">Some Workers subrequests are counted as separate requests</h2>
<p>Cloudflare may count Workers subrequests on the same zone as separate requests, which will cause a rate limiting rule to trigger sooner than expected. This behavior happens when the rate limiting rule is configured with <a href="/waf/rate-limiting-rules/parameters/#also-apply-rate-limiting-to-cached-assets"><strong>Also apply rate limiting to cached assets</strong></a> set to false.</p>
<p>To prevent this behavior, you must exclude any Workers subrequests coming from the same zone from your rate limiting rule using the <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field. For example, you could add the following sub-expression to your <a href="/waf/rate-limiting-rules/parameters/#when-incoming-requests-match">rate limiting rule expression</a>:</p>
<pre><code class="language-txt">and (cf.worker.upstream_zone == &quot;&quot; or cf.worker.upstream_zone != &quot;&lt;YOUR_ZONE&gt;&quot;)&#10;</code></pre>
<p>The first condition (testing for an empty string) will match direct visitor requests, while the second condition will match subrequests not originating from your zone, effectively excluding subrequests from the same zone from the rate limiting rule.</p>
<h2 id="rate-limiting-rules-with-hostname-conditions-and-origin-rules">Rate limiting rules with hostname conditions and Origin Rules</h2>
<p>If you use <a href="/rules/origin-rules/">Origin Rules</a> to rewrite the <code>Host</code> header and your rate limiting rule includes <code>http.host</code> in its expression or counting characteristics, the rule may match incoming requests but fail to increment its counter.</p>
<p>This happens because the rate limiting rule expression is evaluated in two phases:</p>
<ol>
<li><strong>Request phase</strong> (rule matching): The expression is evaluated against the original request, where <code>http.host</code> contains the original hostname. The rule matches as expected.</li>
<li><strong>Response phase</strong> (counter increment): If the rule uses a <a href="/waf/rate-limiting-rules/parameters/#increment-counter-when">counting expression</a> or has <strong>Also apply rate limiting to cached assets</strong> turned off, the counter increment happens after the response. At this point, Origin Rules have already rewritten the <code>Host</code> header to the new value, so an expression containing the original hostname no longer matches.</li>
</ol>
<p>As a result, the rule matches requests but never increments the counter, and the rate limit is never enforced.</p>
<h3 id="resolution">Resolution</h3>
<p>To fix this, do one of the following:</p>
<ul>
<li>Remove <code>http.host</code> conditions from the counting expression and use other fields (such as <code>http.request.uri.path</code>) to scope the counter.</li>
<li>Update the counting expression to use the rewritten hostname instead of the original hostname.</li>
<li>Add both the original and rewritten hostnames to the counting expression using an <code>or</code> condition.</li>
</ul>
<h2 id="rate-limiting-fail-open-behavior">Rate limiting fail-open behavior</h2>
<p>Cloudflare rate limiting rules operate in <strong>fail-open mode</strong> (allowing requests through rather than blocking them) during infrastructure overload. When the underlying infrastructure experiences high load, Cloudflare may skip rate counter updates and rate limit enforcement for affected requests rather than blocking legitimate traffic.</p>
<p>There is no customer-visible signal for fail-open events. If a rate limiting rule is not blocking traffic that it should be catching (a false negative) and the rule configuration is correct, infrastructure load at the affected data center may be a factor.</p>
<p><strong>Per-data-center counting:</strong> Rate limiting counters are maintained per Cloudflare data center. Traffic distributed across many data centers may keep per-data-center rates below the threshold even when the aggregate rate exceeds it. Consider this when setting thresholds for globally distributed traffic.</p>
