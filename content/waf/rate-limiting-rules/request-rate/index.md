<p>Cloudflare tracks request rates by maintaining separate counters for each unique combination of values in a rule's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15352.md")
</div>.
<p>For example, consider a rule with these characteristics:</p>
<ul>
<li>IP address</li>
<li>HTTP header <code>x-api-key</code></li>
</ul>
<p>If two requests share the same <code>x-api-key</code> header value but come from different IP addresses, Cloudflare counts them separately because their characteristic combinations differ.</p>
<p>Counters are not shared across data centers, with the exception of data centers associated with the same geographical location.</p>
<p>By default, request rate is based on the number of incoming requests. Enterprise customers with <a href="/waf/rate-limiting-rules/#availability">Advanced Rate Limiting</a> can also base the rate on the cost of serving each request. Refer to <a href="#complexity-based-rate-limiting">Complexity-based rate limiting</a> for more information.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-notes">Important notes</h3>
@markup("md", "content/.markup/bodies/15351.md")
</aside>
<h2 id="example-a">Example A</h2>
<p>Consider the following configuration for a rate limiting rule:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/15353.md")
</div>
<p>The following diagram shows how Cloudflare handles four incoming requests in the context of the above rate limiting rule.</p>
<p><img src="/assets/upstream/images/waf/custom-rules/rate-limiting-example.png" alt="Rate limiting example with four requests where one of the requests is being rate limited. For details, keep reading." /></p>
<p>Since request 1 matches the rule expression, the rate limiting rule is evaluated. Cloudflare defines a request counter for the values of the characteristics in the context of the rate limiting rule and sets the counter to <code>1</code>. Since the counter value is within the established limits in <strong>Requests</strong>, the request is allowed.</p>
<p>Request 2 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The values of the characteristics do not match any existing counter (the value of the <code>X-API-Key</code> header is different). Therefore, Cloudflare defines a separate counter in the context of this rule and sets it to <code>1</code>. The counter value is within the request limit established in <strong>Requests</strong>, and so this request is allowed.</p>
<p>Request 3 matches the rule expression and has the same values for rule characteristics as request 1. Therefore, Cloudflare increases the value of the existing counter, setting it to <code>2</code>. The counter value is now above the limit defined in <strong>Requests</strong>, and so request 3 gets blocked.</p>
<p>Request 4 does not match the rule expression, since the value for the <code>Content-Type</code> header does not match the value in the expression. Therefore, Cloudflare does not create a new rule counter for this request. Request 4 is not evaluated in the context of this rate limiting rule and is passed on to subsequent rules in the request evaluation workflow.</p>
<h2 id="example-b">Example B</h2>
<p>Consider the following configuration for a rate limiting rule. The rule counting expression defines that the counter will increase by one when the response HTTP status code is <code>400</code>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/15354.md")
</div>
<p>The following diagram shows how Cloudflare handles these four incoming requests received during a 10-second period in the context of the above rate limiting rule.</p>
<p><img src="/assets/upstream/images/waf/custom-rules/rate-limiting-example-response-field.png" alt="Rate limiting example with four requests where the rate limiting rule uses a response field (the HTTP response code) in the counting expression. For details, keep reading." /></p>
<p>Since request 1 matches the rule expression, the rate limiting rule is evaluated. The request is sent to the origin, skipping any cached content, because the rate limiting rule includes a response field (<code>http.response.code</code>) in the counting expression. The origin responds with a <code>400</code> status code. Since there is a match for the counting expression, Cloudflare creates a request counter for the values of the characteristics in the context of the rate limiting rule, and sets this counter to <code>1</code>.</p>
<p>Request 2 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The request counter for the characteristics values is still within the maximum number of requests defined in <strong>Requests</strong>. The origin responds with a <code>200</code> status code. Since the response does not match the counting expression, the counter is not incremented, keeping its value (<code>1</code>).</p>
<p>Request 3 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The request is still within the maximum number of requests defined in <strong>Requests</strong>. The origin responds with a <code>400</code> status code. There is a match for the counting expression, which sets the counter to <code>2</code>.</p>
<p>Request 4 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The request is no longer within the maximum number of requests defined in <strong>Requests</strong> (the counter has the value <code>2</code> and the maximum number of requests is <code>1</code>). Cloudflare applies the action defined in the rate limiting rule configuration, blocking request 4 and any later requests that match the rate limiting rule for ten minutes.</p>
<h2 id="complexity-based-rate-limiting">Complexity-based rate limiting</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15350.md")
</aside>
<p>Not all requests cost the same to serve. A simple API read might use minimal resources, while a complex database query or file export might require significantly more. Request-count-based rate limiting treats these equally — 100 lightweight requests and 100 expensive requests increment the same counter.</p>
<p>Complexity-based rate limiting addresses this by tracking a cost score that your origin server assigns to each request, and enforcing a maximum total score per client over a given period. This way, a client that sends a few expensive requests can be rate limited before reaching a high request count, regardless of the total number of requests sent.</p>
<p>To use complexity-based rate limiting, your origin server must return an HTTP response header containing a numeric score for each request. This score represents the complexity or cost of serving that request. The value must be between 1 and 1,000,000. You configure which header name the rule reads from.</p>
<p>Complexity-based rate limiting rules must contain the following properties:</p>
<ul>
<li><a href="/waf/rate-limiting-rules/parameters/#when-rate-exceeds--score-per-period">Score per period</a>: Maximum total score allowed per period. When the total exceeds this value, the rule action executes.</li>
<li><a href="/waf/rate-limiting-rules/parameters/#when-rate-exceeds--period">Period</a>: The time window for evaluating the total score.</li>
<li><a href="/waf/rate-limiting-rules/parameters/#when-rate-exceeds--response-header-name">Response header name</a>: The HTTP response header, set by your origin server, containing the score for each request.</li>
</ul>
<p>Cloudflare keeps counters with the total score of all requests with the same values for the rule characteristics that match the rule expression. The score increases by the value provided by the origin in the response when there is a match for the counting expression (by default, it is the same as the rule expression). When the total score is larger than the configured maximum score per period, the rule action is applied.</p>
<p>If the origin server does not provide the HTTP response header with a score value or if the score value is outside of the allowed range, the corresponding rate limiting counter will not be updated.</p>
<h3 id="example-c">Example C</h3>
<p>Consider the following configuration for a rate limiting rule. When there is a rule match, the complexity score counter will increase based on the value in the <code>x-score</code> response header provided by the origin server.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/15355.md")
</div>
<p>The following diagram shows how Cloudflare handles four incoming requests received during a one-minute period in the context of the above rate limiting rule.</p>
<p><img src="/assets/upstream/images/waf/custom-rules/rate-limiting-example-complexity-based.png" alt="Rate limiting example with four requests where the rate limiting rule is configured to take into account the complexity score provided in the &quot;x-score&quot; HTTP header. For details, keep reading." /></p>
<p>Since request 1 matches the rule expression, the rate limiting rule is evaluated. The origin responds with a <code>200</code> status code and a complexity score of <code>100</code> in the <code>x-score</code> HTTP response header. Cloudflare creates a request counter for the values of the characteristics in the context of the rate limiting rule, and sets this counter to <code>100</code>.</p>
<p>Request 2 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The request counter for the characteristics values is still within the maximum score per period. The origin responds with a <code>200</code> status code and the request counter is increased by <code>200</code>. The current complexity score for the request is now <code>300</code>.</p>
<p>Request 3 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The request counter for the characteristics values is still within the maximum score per period. The origin responds with a <code>200</code> status code and the request counter is increased by <code>150</code>. The current complexity score for the request is now <code>450</code>.</p>
<p>Request 4 matches the rule expression and therefore Cloudflare evaluates the rate limiting rule. The request is no longer within the maximum score per period defined in the rule (the counter has the value <code>450</code> and the maximum score is <code>400</code>). Cloudflare applies the action defined in the rate limiting rule configuration, blocking request 4 and any later requests that match the rate limiting rule for ten minutes.</p>
