<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>Cloudflare Trace <div class="nb-data-component" data-cf-component="ProductAvailabilityText"></div> simulates an HTTP/S request through Cloudflare's network to your origin server. Use this tool to understand how your Cloudflare configurations (such as rules, caching, and security settings) would affect a specific request. If the hostname you are testing is not <a href="/dns/proxy-status/">proxied by Cloudflare</a>, Cloudflare Trace will still return all the configurations that Cloudflare would have applied to the request.</p>
<p>You can define specific request properties to simulate different conditions for an HTTP/S request. Rules that are turned off in Cloudflare products will not be evaluated.</p>
<p>Cloudflare Trace is available to users with an Administrator or Super Administrator role.</p>
<h2 id="when-to-use-trace">When to use Trace</h2>
<p>Use Trace when you need to test what would happen with a simulated request:</p>
<ul>
<li>Understanding why a rule did not trigger as expected</li>
<li>Testing how your rules handle different request scenarios</li>
<li>Seeing the evaluation order of your rules</li>
<li>Simulating requests from different geolocations or conditions</li>
</ul>
<p>Use <a href="/log-explorer/">Log Explorer</a> when you need to investigate what actually happened with real production traffic:</p>
<ul>
<li>Analyzing historical data and trends</li>
<li>Investigating security incidents after they occur</li>
<li>Searching for patterns across thousands of requests</li>
<li>Monitoring application performance over time</li>
<li>Providing forensic evidence to support teams</li>
</ul>
<p>The key difference is that Trace simulates &quot;what-if&quot; scenarios, while Log Explorer shows actual historical traffic.</p>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/rules/trace-request/how-to/">Use Cloudflare Trace</a></li><li><a href="/rules/trace-request/limitations/">Cloudflare Trace limitations</a></li><li><a href="/rules/trace-request/changelog/">Cloudflare Trace changelog</a></li></ul>
