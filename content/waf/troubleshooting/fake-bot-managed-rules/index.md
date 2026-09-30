<p>The Cloudflare Managed Ruleset includes rules that detect requests impersonating well-known bots such as Googlebot and Bingbot. These rules compare the request's <code>User-Agent</code> header against known bot patterns and then verify the source using methods like reverse DNS lookup or IP validation. If the <code>User-Agent</code> matches a known bot but the source cannot be verified, the rule flags the request as a fake bot.</p>
<h2 id="fake-bot-rules">Fake bot rules</h2>
<p>The following table lists the fake bot detection rules in the Cloudflare Managed Ruleset:</p>
<table>
<thead>
<tr>
<th>Rule name</th>
<th>Rule ID</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anomaly:Header:User-Agent - Fake Google Bot</td>
<td><code class="nb-rule-id" title="ce11be543594412bb4bb92516aa0bef8">6aa0bef8</code></td>
</tr>
<tr>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td><code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code></td>
</tr>
</tbody>
</table>
<h2 id="common-false-positive-scenarios">Common false positive scenarios</h2>
<p>Fake bot rules may trigger false positives for legitimate services that share infrastructure or user agent patterns with known bots but use different IP ranges. Common examples include:</p>
<ul>
<li><strong>Google Cloud services</strong>: Services such as Google Cloud Workflows or Cloud Functions may send requests with a Google-related <code>User-Agent</code> header from IP addresses outside the standard Googlebot range. These requests fail the IP verification check and are flagged as fake Google bots.</li>
<li><strong>Bing Webmaster Tools Site Scan</strong>: Site Scan does not use the same IP range as Bingbot, causing the fake Bing bot rule to trigger. For specific guidance on this scenario, refer to <a href="/waf/troubleshooting/blocked-bing-site-scans/">Bing's Site Scan blocked by a managed rule</a>.</li>
<li><strong>Monitoring and testing tools</strong>: Third-party uptime monitors or automated testing tools that set a bot-like <code>User-Agent</code> header may also be flagged.</li>
</ul>
<h2 id="resolution">Resolution</h2>
<p>If a fake bot rule is blocking legitimate traffic, create an <a href="/waf/managed-rules/waf-exceptions/">exception</a> to skip the specific managed rule for the affected requests.</p>
<p>When defining the exception expression, use request properties that identify the legitimate traffic without broadly disabling the rule. For example:</p>
<ul>
<li>Filter by source IP address or IP range if the service uses a known set of addresses.</li>
<li>Filter by a specific URI path if the service only accesses certain endpoints.</li>
<li>Filter by ASN if the service originates from a specific network.</li>
</ul>
<p>The exception must appear in the rules list before the rule that executes the Cloudflare Managed Ruleset, or it will have no effect.</p>
<p>For instructions on creating exceptions, refer to <a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a>.</p>
