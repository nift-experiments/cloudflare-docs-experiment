<p>Rate limiting is composed of the following parameters:</p>
<ul>
<li>An <a href="/ruleset-engine/rules-language/expressions/">expression</a> that specifies the criteria you are matching traffic on using the <a href="/ruleset-engine/rules-language/">Rules language</a>.</li>
<li>An <a href="/ruleset-engine/rules-language/actions/">action</a> that specifies what to perform when there is a match for the rule and any additional conditions are met. In the case of rate limiting rules, the action occurs when the rate reaches the specified limit.</li>
</ul>
<p>Besides these two parameters, rate limiting rules require the following additional parameters:</p>
<ul>
<li><strong>Characteristics</strong>: The set of parameters that define how Cloudflare tracks the rate for this rule.</li>
<li><strong>Period</strong>: The period of time to consider (in seconds) when evaluating the rate.</li>
<li><strong>Requests per period</strong>: The number of requests over the period of time that will trigger the rate limiting rule.</li>
<li><strong>Duration</strong> (or mitigation timeout): Once the rate is reached, the rate limiting rule blocks further requests for the period of time defined in this field.</li>
<li><strong>Action behavior</strong>: By default, Cloudflare will apply the rule action for the configured duration (or mitigation timeout), regardless of the request rate during this period. Some Enterprise customers can configure the rule to <a href="/waf/rate-limiting-rules/parameters/#with-the-following-behavior">throttle requests</a> over the maximum rate, allowing incoming requests when the rate is lower than the configured limit.</li>
</ul>
<h2 id="features-by-plan-type">Features by plan type</h2>
<p>Features vary by plan type.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise with app security</th>
<th>Enterprise with Advanced Rate Limiting</th>
</tr>
</thead>
<tbody>
<tr>
<td>Available fields<br/>in rule expression</td>
<td>Path, <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/">Verified Bot</a></td>
<td>Host, URI, Path, Full URI, Query, Verified Bot</td>
<td>Host, URI, Path, Full URI, Query, Method, Source IP, User Agent, Verified Bot</td>
<td>General request fields, request header fields, Verified Bot, Bot Management fields<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-1">1</a></sup></td>
<td>General request fields, request header fields, Verified Bot, Bot Management fields<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-1">1</a></sup>, request body fields<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup></td>
</tr>
<tr>
<td>Cache exclusion</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
<td>IP</td>
<td>IP, IP with NAT support</td>
<td>IP, IP with NAT support</td>
<td>IP, IP with NAT support, Query, Host, Headers, Cookie, ASN, Country, Path, JA3/JA4 Fingerprint<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-1">1</a></sup>, JSON field value<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup>, Body<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup>, Form input value<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup>, Custom</td>
</tr>
<tr>
<td>Custom counting expression</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Available fields<br/>in counting expression</td>
<td>N/A</td>
<td>N/A</td>
<td>All rule expression fields, Response code, Response headers</td>
<td>All rule expression fields, Response code, Response headers</td>
<td>All rule expression fields, Response code, Response headers</td>
</tr>
<tr>
<td>Counting model</td>
<td>Number of requests</td>
<td>Number of requests</td>
<td>Number of requests</td>
<td>Number of requests</td>
<td>Number of requests, <a href="/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting">complexity score</a></td>
</tr>
<tr>
<td>Rate limiting<br/>action behavior</td>
<td>Perform action during mitigation period</td>
<td>Perform action during mitigation period</td>
<td>Perform action during mitigation period</td>
<td>Perform action during mitigation period, Throttle requests above rate with block action</td>
<td>Perform action during mitigation period, Throttle requests above rate with block action</td>
</tr>
<tr>
<td>Counting periods</td>
<td>10 s</td>
<td>All supported values up to 1 min<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 10 min<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 65,535 s<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 65,535 s<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
</tr>
<tr>
<td>Mitigation timeout periods</td>
<td>10 s</td>
<td>All supported values up to 1 h<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 1 day<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 1 day<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup> <sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-4">4</a></sup></td>
<td>All supported values up to 1 day<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup> <sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-4">4</a></sup></td>
</tr>
<tr>
<td>Number of rules</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>100<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-5">5</a></sup></td>
<td>100</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9625.md")
</div></details>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-waf-rate-limiting-availability-by-plan-mdx-1">Only available to Enterprise customers who have purchased [Bot Management](/bots/plans/bm-subscription/).</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-2">Availability depends on your WAF plan.</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-3">Supported period values in seconds:<br/> 10, 15, 20, 30, 40, 45, 60 (1 min), 90, 120 (2 min), 180 (3 min), 240 (4 min), 300 (5 min), 480, 600 (10 min), 900, 1200 (20 min), 1800, 2400, 3600 (1 h), 65535, 86400 (1 day).</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-4">Enterprise customers can specify a custom mitigation timeout period via API.</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-5">Enterprise customers must have application security on their contract to get access to rate limiting rules. The number of rules depends on the exact contract terms.</li></ol></section>
