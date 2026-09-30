<p>The examples below include sample rate limiting rule configurations.</p>
<h2 id="example-1">Example 1</h2>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs rate limiting on incoming requests from the US addressed at the login page, except for one allowed IP address.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/15346.md")
</div>
<h2 id="example-2">Example 2</h2>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs rate limiting on incoming requests with a given base URI path, incrementing on the IP address and the provided API key.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/15347.md")
</div>
<h2 id="example-3-1">Example 3</h2>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs rate limiting on requests targeting multiple URI paths in two hosts, excluding known bots. The request rate is based on IP address and <code>User-Agent</code> values.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@markup("md", "content/.markup/bodies/15348.md")
</div>
<h2 id="example-4-1">Example 4</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15345.md")
</aside>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs complexity-based rate limiting. The rule takes into account the <code>my-score</code> HTTP response header provided by the origin server to calculate a total complexity score for the client with the provided API key.</p>
<p>The counter with the total score is updated when there is a match for the rate limiting rule's <a href="/waf/rate-limiting-rules/parameters/#increment-counter-when">counting expression</a> (in this case, the same as the rule expression since a counting expression was not provided). When this total score becomes larger than <code>400</code> during a period of one minute, any later client requests will be blocked for a period of 10 minutes.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-5">Example</h3>
@markup("md", "content/.markup/bodies/15349.md")
</div>
<p>For an API example with this rule configuration, refer to <a href="/waf/rate-limiting-rules/create-api/#example-d---complexity-based-rate-limiting-rule">Create a rate limiting rule via API</a>.</p>
