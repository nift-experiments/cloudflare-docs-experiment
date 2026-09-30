<p>A bot score is a score from <em>1</em> to <em>99</em> that indicates how likely that request came from a bot.</p>
<p>For example, a score of 1 means Cloudflare is quite certain the request was automated, while a score of 99 means Cloudflare is quite certain the request came from a human.</p>
<p>You can use bot scores in <a href="/waf/custom-rules/">WAF custom rules</a> to block, challenge, or allow requests based on their score. Bot scores are also available in <a href="/workers/">Workers</a> to customize application behavior. For more details, refer to <a href="/bots/reference/bot-management-variables/">Bot Management variables</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3519.md")
</aside>
<h2 id="bot-groupings">Bot groupings</h2>
<p>Customers with a Pro plan or higher can automatically see bot traffic divided into groups by going to <strong>Security</strong> &gt; <strong>Bots</strong>.</p>
<table>
<thead>
<tr>
<th>Category</th>
<th>Range</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Not computed</strong></td>
<td>Bot scores of 0.</td>
</tr>
<tr>
<td><strong>Automated</strong></td>
<td>Bot scores of 1.</td>
</tr>
<tr>
<td><strong>Likely automated</strong></td>
<td>Bot scores of 2 through 29.</td>
</tr>
<tr>
<td><strong>Likely human</strong></td>
<td>Bot scores of 30 through 99.</td>
</tr>
<tr>
<td><strong>Verified bot</strong></td>
<td>Non-malicious automated traffic (used to power search engines and other applications).</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3518.md")
</aside>
<h2 id="how-cloudflare-generates-bot-scores">How Cloudflare generates bot scores</h2>
<p>The following detection engines only apply to Enterprise Bot Management. For specific details about the engines included in your plan, refer to <a href="/bots/plans/">Plans</a>.</p>
<h3 id="heuristics">Heuristics</h3>
<p>Catches automated traffic through pattern matching against a database of known malicious fingerprints.</p>
<p>The <strong>Heuristics</strong> engine processes all requests. Cloudflare conducts a number of heuristic checks to identify automated traffic, and requests are matched against a growing database of malicious fingerprints.</p>
<p>The Heuristics engine gives automated requests a score of 1 for high-confidence, deterministic detections. Occasionally, heuristics will set a score of 29 in cases where Cloudflare has identified automated traffic and is still assessing traffic overlap.</p>
<h3 id="machine-learning">Machine learning</h3>
<p>Catches sophisticated bots by analyzing request features across billions of daily requests. Produces most scores between 2 and 99.</p>
<p>The <strong>Machine Learning (ML)</strong> engine accounts for the majority of all detections, distinguishing between human and bot traffic. This approach leverages our global network, which proxies billions of requests daily, to identify both automated and human traffic.</p>
<p>The ML system uses a supervised machine learning methodology to determine the final Bot Score (1–99).</p>
<p>The core model relies on the following process:</p>
<ul>
<li>Input Variables (X): Various request features (headers, session characteristics, and browser signals) collected from traffic across the Cloudflare network.</li>
<li>Output Variable (Y): The predicted probability that a client is human (such as the probability of successfully solving a Challenge). This probability is mapped to the final 1–99 Bot Score.</li>
</ul>
<p>We constantly train the ML engine on a periodic basis using vast, anonymized data to ensure it remains accurate and adapts to new threats. Customers can analyze the request features used by these models via their own logs, such as Cloudflare <a href="/logs/logpull/">Logpull</a> or <a href="/logs/logpush/">Logpush</a>.</p>
<h3 id="anomaly-detection">Anomaly detection</h3>
<p>Detects outlier requests by comparing traffic against a learned baseline for your specific site.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/3517.md")
</aside>
<p>The <strong>Anomaly Detection (AD)</strong> engine is an optional detection engine that uses a form of unsupervised learning. Cloudflare records a baseline of your domain's traffic and uses the baseline to intelligently detect outlier requests. This approach is user agent-agnostic and can be turned on or off by your account team.</p>
<p>Cloudflare does not recommend AD for domains that use <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">Cloudflare for SaaS</a> or expect large amounts of API traffic. The AD engine immediately gives automated requests a score of one.</p>
<h3 id="javascript-detections">JavaScript detections</h3>
<p>Catches headless browsers (browsers controlled by software, with no visible window or human operator) and other automation tools.</p>
<p>The <a href="/bots/additional-configurations/javascript-detections/"><strong>JavaScript Detections (JSD)</strong></a> engine identifies headless browsers and other malicious fingerprints. This engine performs a lightweight, invisible JavaScript injection on the client side of any request while honoring our <a href="https://www.cloudflare.com/privacypolicy/">strict privacy standards</a>. We do not collect any personally identifiable information during the process. The JSD engine either blocks, challenges, or passes requests to other engines.</p>
<p>JSD is enabled by default but completely optional. To adjust your settings, open the Bot Management Configuration page from <strong>Security</strong> &gt; <strong>Bots</strong>.</p>
<h3 id="cloudflare-service">Cloudflare service</h3>
<p><strong>Cloudflare Service</strong> is a special <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3520.md")
</div> source for Enterprise Zero Trust to avoid false positives.
<h3 id="not-computed">Not computed</h3>
<p>A bot score of 0 means Bot Management did not evaluate the request. This applies to internal Cloudflare service requests and requests that were redirected or handled by another feature (such as <a href="/rules/url-forwarding/">Redirect Rules</a>) before Bot Management could run. A score of 0 does not indicate the request is safe or human.</p>
<h3 id="notes-on-detection">Notes on detection</h3>
<p>Cloudflare uses the <code>__cf_bm</code> cookie to smooth out the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3521.md")
</div> and reduce false positives for actual user sessions.
<p>The Bot Management cookie measures a single user's request pattern and applies it to the machine learning data to generate a reliable bot score for all of that user's requests.</p>
<p>For more details, refer to <a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/">Cloudflare Cookies</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3516.md")
</aside>
