<p>The available rate limiting rule parameters are described in the following sections.</p>
<p>For more information on the current rule configuration restrictions, refer to <a href="#configuration-restrictions">Configuration restrictions</a>.</p>
<h2 id="parameter-reference">Parameter reference</h2>
<h3 id="when-incoming-requests-match">When incoming requests match</h3>
<ul>
<li>Data type: <span class="nb-type">String</span></li>
<li>Field name in the API: <code>expression</code> (rule field)</li>
</ul>
<p>Defines the criteria for the rate limiting rule to match a request.</p>
<h3 id="also-apply-rate-limiting-to-cached-assets">Also apply rate limiting to cached assets</h3>
<ul>
<li>Data type: <span class="nb-type">Boolean</span></li>
<li>Field name in the API: <code>requests_to_origin</code> (optional, with the opposite meaning of the Cloudflare dashboard option)</li>
</ul>
<p>If this parameter is disabled (or when the <code>requests_to_origin</code> API field is set to <code>true</code>), only the requests going to the origin (that is, requests that are not cached) will be considered when determining the request rate.</p>
<p>In some cases, you cannot disable the <strong>Also apply rate limiting to cached assets</strong> parameter due to configuration restrictions. Refer to <a href="#configuration-restrictions">Configuration restrictions</a> for details.</p>
<p>Depending on your <a href="/waf/rate-limiting-rules/#availability">Cloudflare plan</a>, this rule parameter might not be available. In that case, Cloudflare will also apply rate limiting to cached assets (the parameter is enabled by default).</p>
<h3 id="with-the-same-characteristics">With the same characteristics</h3>
<ul>
<li>Data type: <span class="nb-type">Array&lt;String&gt;</span></li>
<li>Field name in the API: <code>characteristics</code></li>
</ul>
<p>Set of parameters defining how Cloudflare tracks the request rate for the rule.</p>
<p>Use one or more of the following characteristics:</p>
<table>
<thead>
<tr>
<th>Dashboard value</th>
<th>API value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>N/A (implicitly included)</td>
<td><code>cf.colo.id</code>(mandatory)</td>
<td><a href="#do-not-use-cfcoloid-as-a-field-in-expressions">Do not use in expressions</a></td>
</tr>
<tr>
<td>IP</td>
<td><code>ip.src</code></td>
<td><a href="#incompatible-characteristics">Incompatible with <strong>IP with NAT support</strong></a></td>
</tr>
<tr>
<td>IP with NAT support</td>
<td><code>cf.unique_visitor_id</code></td>
<td><a href="#incompatible-characteristics">Incompatible with <strong>IP</strong></a></td>
</tr>
<tr>
<td><strong>Header value of</strong> (enter header name)</td>
<td><code>http.request.headers[&quot;&lt;header_name&gt;&quot;]</code></td>
<td><a href="#use-a-lowercased-header-name-for-api-users">Use lowercased header name in API</a> and <a href="#missing-field-versus-empty-value">Missing field versus empty value</a></td>
</tr>
<tr>
<td><strong>Cookie value of</strong> (enter cookie name)</td>
<td><code>http.request.cookies[&quot;&lt;cookie_name&gt;&quot;]</code></td>
<td><a href="#recommended-configurations-when-using-cookie-value-of">Recommended configurations</a> and <a href="#missing-field-versus-empty-value">Missing field versus empty value</a></td>
</tr>
<tr>
<td><strong>Query value of</strong> (enter parameter name)</td>
<td><code>http.request.uri.args[&quot;&lt;query_param_name&gt;&quot;]</code></td>
<td><a href="#missing-field-versus-empty-value">Missing field versus empty value</a></td>
</tr>
<tr>
<td><strong>Host</strong></td>
<td><code>http.host</code></td>
<td></td>
</tr>
<tr>
<td><strong>Path</strong></td>
<td><code>http.request.uri.path</code></td>
<td></td>
</tr>
<tr>
<td><strong>AS Num</strong></td>
<td><code>ip.src.asnum</code></td>
<td></td>
</tr>
<tr>
<td><strong>Country</strong></td>
<td><code>ip.src.country</code></td>
<td></td>
</tr>
<tr>
<td><strong>JA3 Fingerprint</strong></td>
<td><code>cf.bot_management.ja3_hash</code></td>
<td></td>
</tr>
<tr>
<td><strong>JA4</strong></td>
<td><code>cf.bot_management.ja4</code></td>
<td></td>
</tr>
<tr>
<td><strong>JSON string value of</strong> (enter key)</td>
<td><code>lookup_json_string(http.request.body.raw, &quot;&lt;key&gt;&quot;)</code></td>
<td><a href="#missing-field-versus-empty-value">Missing field versus empty value</a> and <a href="/ruleset-engine/rules-language/functions/#lookup_json_string"><code>lookup_json_string()</code> function reference</a></td>
</tr>
<tr>
<td><strong>JSON integer value of</strong> (enter key)</td>
<td><code>lookup_json_integer(http.request.body.raw, &quot;&lt;key&gt;&quot;)</code></td>
<td><a href="#missing-field-versus-empty-value">Missing field versus empty value</a> and <a href="/ruleset-engine/rules-language/functions/#lookup_json_integer"><code>lookup_json_integer()</code> function reference</a></td>
</tr>
<tr>
<td><strong>Form input value of</strong> (enter field name)</td>
<td><code>http.request.body.form[&quot;&lt;input_field_name&gt;&quot;]</code></td>
<td><a href="#missing-field-versus-empty-value">Missing field versus empty value</a></td>
</tr>
<tr>
<td><strong>JWT claim of</strong> (enter token configuration ID, claim name)</td>
<td><code>lookup_json_string( http.request.jwt.claims[&quot;&lt;token_configuration_id&gt;&quot;][0], &quot;&lt;claim_name&gt;&quot;)</code></td>
<td><a href="#requirements-for-using-claims-inside-a-json-web-token-jwt">Requirements for claims in JWT</a>, <a href="#missing-field-versus-empty-value">missing field versus empty value</a> and <a href="/api-shield/security/jwt-validation/transform-rules/">JWT Validation reference</a></td>
</tr>
<tr>
<td><strong>Body</strong></td>
<td><code>http.request.body.raw</code></td>
<td></td>
</tr>
<tr>
<td><strong>Body size</strong> (select operator, enter size)</td>
<td><code>http.request.body.size</code></td>
<td></td>
</tr>
<tr>
<td><strong>Custom</strong> (enter expression)</td>
<td>Enter a custom expression. You can use a function such as <code>substring()</code> or <code>lower()</code>, or enter a more complex expression.</td>
<td><a href="/ruleset-engine/rules-language/functions/">Functions</a></td>
</tr>
</tbody>
</table>
<p>The available characteristics depend on your Cloudflare plan. Refer to <a href="/waf/rate-limiting-rules/#availability">Availability</a> for more information.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15359.md")
</aside>
<h3 id="increment-counter-when">Increment counter when</h3>
<ul>
<li>Data type: <span class="nb-type">String</span></li>
<li>Field name in the API: <code>counting_expression</code> (optional)</li>
</ul>
<p>Only available in the Cloudflare dashboard when you enable <strong>Use custom counting expression</strong>.</p>
<p>Defines the criteria used for determining the request rate. By default, the counting expression is the same as the rule matching expression (defined in <strong>When incoming requests match</strong>). This default is also applied when you set this field to an empty string (<code>&quot;&quot;</code>).</p>
<p>The counting expression can include <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Response">HTTP response fields</a>. When there are response fields in the counting expression, the counting will happen after the response is sent.</p>
<p>In some cases, you cannot include HTTP response fields in the counting expression due to configuration restrictions. Refer to <a href="#configuration-restrictions">Configuration restrictions</a> for details.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="the-counting-expression-does-not-extend-the-rule-expression">The counting expression does not extend the rule expression</h3>
@markup("md", "content/.markup/bodies/15358.md")
</aside>
<h3 id="when-rate-exceeds">When rate exceeds</h3>
<ul>
<li>Field name in the API: <em>N/A</em> (different API fields required according to the selected option)</li>
</ul>
<p>The rate limiting counting can be:</p>
<ul>
<li><strong>Request based</strong>: Performs rate limiting based on the number of incoming requests during a given period. This is the only counting method when complexity-based rate limiting is not available.</li>
<li><strong>Complexity based</strong>: Performs rate limiting based on the <a href="/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting">complexity</a> or cost of handling requests during a given period. Only available to Enterprise customers with Advanced Rate Limiting.</li>
</ul>
<h3 id="when-rate-exceeds-requests">When rate exceeds &gt; Requests</h3>
<ul>
<li>Data type: <span class="nb-type">Integer</span></li>
<li>Field name in the API: <code>requests_per_period</code></li>
</ul>
<p>The number of requests over the period of time that will trigger the rule. Applies to request-based rate limiting.</p>
<h3 id="when-rate-exceeds-period">When rate exceeds &gt; Period</h3>
<ul>
<li>Data type: <span class="nb-type">Integer</span></li>
<li>Field name in the API: <code>period</code></li>
</ul>
<p>The period of time to consider (in seconds) when evaluating the request rate. The available values <a href="/waf/rate-limiting-rules/#availability">vary according to your Cloudflare plan</a>.</p>
<p>The available API values are: <code>10</code>, <code>60</code> (one minute), <code>120</code> (two minutes), <code>300</code> (five minutes), <code>600</code> (10 minutes), or <code>3600</code> (one hour).</p>
<h3 id="when-rate-exceeds-score-per-period">When rate exceeds &gt; Score per period</h3>
<ul>
<li>Data type: <span class="nb-type">Integer</span></li>
<li>Field name in the API: <code>score_per_period</code></li>
</ul>
<p>Maximum score per period. When this value is exceeded, the rule action will execute. Applies to <a href="/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting">complexity-based rate limiting</a>.</p>
<h3 id="when-rate-exceeds-response-header-name">When rate exceeds &gt; Response header name</h3>
<ul>
<li>Data type: <span class="nb-type">String</span></li>
<li>Field name in the API: <code>score_response_header_name</code></li>
</ul>
<p>Name of HTTP header in the response, set by the origin server, with the score for the current request. Applies to <a href="/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting">complexity-based rate limiting</a>.</p>
<h3 id="then-take-action">Then take action</h3>
<ul>
<li>Data type: <span class="nb-type">String</span></li>
<li>Field name in the API: <code>action</code> (rule field)</li>
</ul>
<p>Action to perform when the rate specified in the rule is reached.</p>
<p>Use one of the following values in the API: <code>block</code>, <code>js_challenge</code> (Non-Interactive Challenge), <code>managed_challenge</code> (Managed Challenge), <code>challenge</code> (Interactive Challenge), or <code>log</code>.</p>
<p>If you select the <em>Block</em> action, you can define a custom response using the following parameters:</p>
<ul>
<li><a href="#with-response-type-for-block-action">With response type</a></li>
<li><a href="#with-response-code-for-block-action">With response code</a></li>
<li><a href="#response-body-for-block-action">Response body</a></li>
</ul>
<h4 id="with-response-type-for-block-action">With response type (for <em>Block</em> action)</h4>
<ul>
<li>Data type: <span class="nb-type">String</span></li>
<li>Field name in the API: <code>response</code> &gt; <code>content_type</code> (optional)</li>
</ul>
<p>Defines the content type of a custom response when blocking a request due to rate limiting. Only available when you set the <a href="#then-take-action">rule action</a> to <em>Block</em>.</p>
<p>Available API values: <code>application/json</code>, <code>text/html</code>, <code>text/xml</code>, or <code>text/plain</code>.</p>
<h4 id="with-response-code-for-block-action">With response code (for <em>Block</em> action)</h4>
<ul>
<li>Data type: <span class="nb-type">Integer</span></li>
<li>Field name in the API: <code>response</code> &gt; <code>status_code</code> (optional)</li>
</ul>
<p>Defines the HTTP status code returned to the visitor when blocking the request due to rate limiting. Only available when you set the <a href="#then-take-action">rule action</a> to <em>Block</em>.</p>
<p>You must enter a value between <code>400</code> and <code>499</code>. The default value is <code>429</code> (<code>Too many requests</code>).</p>
<h4 id="response-body-for-block-action">Response body (for <em>Block</em> action)</h4>
<ul>
<li>Data type: <span class="nb-type">String</span></li>
<li>Field name in the API: <code>response</code> &gt; <code>content</code> (optional)</li>
</ul>
<p>Defines the body of the returned HTTP response when the request is blocked due to rate limiting. Only available when you set the <a href="#then-take-action">rule action</a> to <em>Block</em>.</p>
<p>The maximum field size is 30 KB.</p>
<h3 id="for-duration">For duration</h3>
<ul>
<li>Data type: <span class="nb-type">Integer</span></li>
<li>Field name in the API: <code>mitigation_timeout</code></li>
</ul>
<p>Once the rate is reached, the rate limiting rule applies the rule action to further requests for the period of time defined in this field (in seconds).</p>
<p>In the dashboard, select one of the available values, which <a href="/waf/rate-limiting-rules/#availability">vary according to your Cloudflare plan</a>. The available API values are: <code>0</code>, <code>10</code>, <code>60</code> (one minute), <code>120</code> (two minutes), <code>300</code> (five minutes), <code>600</code> (10 minutes), <code>3600</code> (one hour), or <code>86400</code> (one day).</p>
<p>Customers on Free, Pro, and Business plans cannot select a duration when using a <a href="/cloudflare-challenges/challenge-types/challenge-pages/#actions">challenge action</a> — their rate limiting rule will always perform request throttling for these actions. With request throttling, you do not define a duration. When visitors pass a challenge, their corresponding <a href="/waf/rate-limiting-rules/request-rate/">request counter</a> is set to zero. When visitors with the same values for the rule characteristics make enough requests to trigger the rate limiting rule again, they will receive a new challenge.</p>
<p>Enterprise customers can always configure a duration (or mitigation timeout), even when using one of the challenge actions.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes-for-api-users">Notes for API users</h3>
@markup("md", "content/.markup/bodies/15357.md")
</aside>
<h3 id="with-the-following-behavior">With the following behavior</h3>
<ul>
<li>Data type: <span class="nb-type">Integer</span></li>
<li>Field name in the API: <code>mitigation_timeout</code></li>
</ul>
<p>Defines the exact behavior of the selected action.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15356.md")
</aside>
<p>The action behavior can be one of the following:</p>
<ul>
<li><strong>Perform action during the selected duration</strong>: Applies the configured action to all requests received during the selected duration. To configure this behavior via API, set <code>mitigation_timeout</code> to a value greater than zero. Refer to <a href="#for-duration">For duration</a> for more information.</li>
</ul>
<p><img src="/assets/upstream/images/waf/rate-limiting-rules/behavior-apply-action-for-duration.png" alt="Chart displaying the action of a rate limiting rule configured to apply its action during the entire mitigation period" /></p>
<ul>
<li><strong>Throttle requests over the maximum configured rate</strong>: Applies the selected action to incoming requests over the configured limit, allowing other requests. To configure this behavior via API, set <code>mitigation_timeout</code> to <code>0</code> (zero).</li>
</ul>
<p><img src="/assets/upstream/images/waf/rate-limiting-rules/behavior-throttle.png" alt="Chart displaying the behavior of a rate limiting configured to throttle requests above the configured limit" /></p>
<h2 id="notes-about-rate-limiting-characteristics">Notes about rate limiting characteristics</h2>
<h3 id="use-cases-of-ip-with-nat-support">Use cases of IP with NAT support</h3>
<p>Use <strong>IP with NAT support</strong> to handle situations such as requests under NAT sharing the same IP address. Cloudflare uses a variety of privacy-preserving techniques to identify unique visitors, which may include use of session cookies. Refer to <a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/">Cloudflare Cookies</a> for details.</p>
<h4 id="considerations-when-using-ip-with-nat-support">Considerations when using IP with NAT support</h4>
<p><strong>IP with NAT support</strong> relies on a cookie-based visitor identification mechanism (<a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/#_cfuvid-for-rate-limiting-rules"><code>_cfuvid</code> cookie</a>). Keep the following in mind:</p>
<ul>
<li>Visitors who clear cookies, use private browsing, or do not accept cookies will not be individually identified. Requests from these visitors share a single counter bucket, which can cause false positives in high-traffic NAT environments.</li>
<li>For security-critical rate limiting (such as protecting login or payment endpoints), combine <strong>IP with NAT support</strong> with other characteristics like <strong>Path</strong> or <strong>Header value of</strong> to reduce the impact of identification gaps.</li>
</ul>
<h3 id="incompatible-characteristics">Incompatible characteristics</h3>
<p>You cannot use both <strong>IP with NAT support</strong> and <strong>IP</strong> as characteristics of the same rate limiting rule.</p>
<h3 id="do-not-use-cf-colo-id-as-a-field-in-expressions">Do not use <code>cf.colo.id</code> as a field in expressions</h3>
<p>You should not use the <code>cf.colo.id</code> characteristic (data center ID) as a field in rule expressions. Additionally, <code>cf.colo.id</code> values may change without warning. For more information about this rate limiting characteristic, refer to <a href="/waf/rate-limiting-rules/request-rate/">Request rate calculation</a>.</p>
<h3 id="use-a-lowercased-header-name-for-api-users">Use a lowercased header name (for API users)</h3>
<p>If you use the <strong>Header value of</strong> characteristic in an API request (with <code>http.request.headers[&quot;&lt;header_name&gt;&quot;]</code>), you must enter the header name in lower case, since Cloudflare normalizes header names on the Cloudflare global network.</p>
<h3 id="missing-field-versus-empty-value">Missing field versus empty value</h3>
<p>If you use the <strong>Header value of</strong>, <strong>Cookie value of</strong>, <strong>Query value of</strong>, <strong>JSON string value of</strong>, <code>lookup_json_integer(...)</code>, or <strong>Form input value of</strong> characteristic and the specific header/cookie/parameter/JSON key/form field name is not present in the request, the rate limiting rule may still apply to the request, depending on your counting expression.</p>
<p>If you do not filter out such requests, there will be a specific <a href="/waf/rate-limiting-rules/request-rate/">request counter</a> for requests where the field is not present, which will be different from the request counter where the field is present with an empty value.</p>
<p>For example, to consider only requests where a specific HTTP header is present in the context of a specific rate limiting rule, adjust the rule counting expression so it contains something similar to the following:</p>
<p><code>and len(http.request.headers[&quot;&lt;header_name&gt;&quot;]) &gt; 0</code></p>
<p>Where <code>&lt;header_name&gt;</code> is the same header name used as a rate limiting characteristic.</p>
<h3 id="recommended-configurations-when-using-cookie-value-of">Recommended configurations when using Cookie value of</h3>
<p>If you use <strong>Cookie value of</strong> as a rate limiting rule characteristic, follow these recommendations:</p>
<ul>
<li>Create a <a href="/waf/custom-rules/">custom rule</a> that blocks requests with more than one value for the cookie.</li>
<li>Validate the cookie value at the origin before performing any demanding server operations.</li>
</ul>
<h3 id="requirements-for-using-claims-inside-a-json-web-token-jwt">Requirements for using claims inside a JSON Web Token (JWT)</h3>
<p>To use claims inside a JSON Web Token (JWT), you must first set up a <a href="/api-shield/security/jwt-validation/api/">token validation configuration</a> in API Shield.</p>
<h2 id="configuration-restrictions">Configuration restrictions</h2>
<ul>
<li>
<p>If the rule filter expression, defined in the <strong>When incoming requests match</strong> parameter, includes <a href="/waf/tools/lists/custom-lists/">custom lists</a>, you must enable the <strong>Also apply rate limiting to cached assets</strong> parameter.</p>
</li>
<li>
<p>The rule filter expression cannot contain <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Response">HTTP response fields</a>.</p>
</li>
<li>
<p>The rule counting expression, defined in the <strong>Increment counter when</strong> parameter, cannot include both <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Response">HTTP response fields</a> and <a href="/waf/tools/lists/custom-lists/">custom lists</a>. If you use custom lists, you must enable the <strong>Also apply rate limiting to cached assets</strong> parameter.</p>
</li>
<li>
<p>When creating a rate limiting ruleset <a href="/waf/account/rate-limiting-rulesets/">at the account level</a>, the ruleset deployment expression (defining the scope) cannot contain <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Response">HTTP response fields</a> or <a href="/waf/tools/lists/custom-lists/">custom lists</a>.</p>
</li>
</ul>
