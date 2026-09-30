<p>The right defense against malicious bot traffic depends on the traffic patterns on your site and your plan. This guide covers a layered approach using <a href="/bots/">Cloudflare Bots</a>, <a href="/waf/">Cloudflare Application Security</a> (also known as Web Application Firewall or WAF), and <a href="/turnstile/">Turnstile</a>, from baseline protection to targeted custom rules. The core workflow uses features on Free, Pro, and Business plans, with callouts for Enterprise options.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15098.md")
</aside>
<h2 id="review-your-bot-traffic">Review your bot traffic</h2>
<p>Before you change any bot settings, review your traffic data to understand what bots are doing on your site.</p>
<h3 id="find-your-bot-analytics">Find your bot analytics</h3>
<p><a href="/bots/bot-analytics/">Bot analytics</a> show you how much of your traffic is automated, which pages bots target, and how Cloudflare scores each request.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bot-analytics-requires-a-business-plan-or-above">Bot Analytics requires a Business plan or above</h3>
@markup("md", "content/.markup/bodies/15097.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Bot analysis</strong> tab.</li>
</ol>
<p>Review the following:</p>
<ul>
<li><strong>Bot score distribution chart</strong>: Scores closer to 1 indicate automated traffic. Scores closer to 99 indicate human traffic.</li>
<li><strong>Top requested paths</strong>: Which endpoints receive the most bot traffic. Login pages, API endpoints, and checkout flows are common targets.</li>
<li><strong>Traffic patterns</strong>: Sudden spikes in low-score traffic, specific user agents appearing at high volume, or geographic concentration of requests can indicate bot activity worth investigating.</li>
</ul>
<h3 id="understand-bot-categories">Understand bot categories</h3>
<p>Cloudflare classifies bot traffic into categories based on bot scores and verification status:</p>
<ul>
<li><strong>Verified bots</strong>: Crawlers and services that Cloudflare has confirmed as legitimate, such as Googlebot, Bingbot, and uptime monitors. Cloudflare maintains a <a href="/bots/concepts/bot/verified-bots/">verified bot list</a> with strict requirements.</li>
<li><strong>Automated</strong> (score 1): Cloudflare is quite certain the request is automated.</li>
<li><strong>Likely automated</strong> (scores 2-29): Probably a bot. This category and Automated are the primary targets for security rules, including scrapers, credential stuffing tools, and spam submitters.</li>
<li><strong>Likely human</strong> (scores 30-99): These requests appear to come from real users. Do not challenge or block this traffic.</li>
</ul>
<h2 id="block-automated-traffic-with-bot-fight-mode">Block automated traffic with Bot Fight Mode</h2>
<p><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> identifies requests that match known bot patterns and issues a computational challenge. It reduces automated traffic across your entire site without requiring you to write any rules.</p>
<h3 id="what-bot-fight-mode-does">What Bot Fight Mode does</h3>
<p>Bot Fight Mode is included with Free plans. When enabled, it:</p>
<ul>
<li>Identifies traffic matching patterns of known bots</li>
<li>Issues computationally expensive challenges in response to these bots</li>
<li>Protects entire domains without endpoint restrictions</li>
<li>Cannot be customized, adjusted, or reconfigured via custom rules</li>
<li>Cannot be bypassed with <a href="/waf/custom-rules/">custom rule</a> Skip actions. If Bot Fight Mode challenges a request you want to allow, you can turn off Bot Fight Mode or upgrade to <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> for more granular control.</li>
</ul>
<p>For more details, refer to <a href="/bots/get-started/bot-fight-mode/#considerations">Bot Fight Mode considerations</a>.</p>
<h3 id="turn-on-bot-fight-mode-free-plan">Turn on Bot Fight Mode (Free plan)</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15099.md")
</div>
<h3 id="enable-super-bot-fight-mode-pro-business-and-enterprise">Enable Super Bot Fight Mode (Pro, Business, and Enterprise)</h3>
<p>Super Bot Fight Mode adds verified bot allowlisting, per-category actions, static resource protection, and JavaScript detections.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15096.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15100.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="plan-availability">Plan availability</h3>
@markup("md", "content/.markup/bodies/15095.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15094.md")
</aside>
<h2 id="protect-forms-from-automated-abuse">Protect forms from automated abuse</h2>
<p><a href="/turnstile/">Turnstile</a> and Application Security <a href="/waf/rate-limiting-rules/">rate limiting rules</a> protect form endpoints in different ways and work best together.</p>
<h3 id="turnstile-versus-rate-limiting">Turnstile versus rate limiting</h3>
<p>Turnstile challenges suspected bots before they can submit a form (login, signup, contact, or checkout), without showing visitors a CAPTCHA. It can be embedded into any website without sending traffic through Cloudflare. Use Turnstile when you need to challenge automated form submissions.</p>
<p>Rate limiting allows you to define rate limits for requests matching an expression and the action to perform when those limits are reached. Use rate limiting to protect endpoints from abuse, such as brute-force attacks on a login page or excessive API calls from a single client.</p>
<p>Both together provide the strongest coverage. Turnstile challenges automated submissions at the form level. Rate limiting catches high-volume attacks that bypass or do not encounter the form, such as direct <code>POST</code> requests to the endpoint that skip the client-side widget.</p>
<h3 id="add-turnstile-to-a-form">Add Turnstile to a form</h3>
<p>Adding Turnstile involves three steps: create a widget, add the client-side snippet, and validate the token on your server.</p>
<h4 id="1-create-a-turnstile-widget"><ol>
<li>Create a Turnstile widget</li>
</ol></h4>
<p>Turnstile is configured at the account level.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15101.md")
</div>
<p>You need both the sitekey and secret key in the following steps.</p>
<h4 id="2-add-the-client-side-snippet"><ol start="2">
<li>Add the client-side snippet</li>
</ol></h4>
<p>Add the Turnstile script and widget container to your form HTML:</p>
<pre><code class="language-html">&lt;script&#10;	src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;&#10;	async&#10;	defer&#10;&gt;&lt;/script&gt;&#10;&#10;&lt;form action=&quot;/submit&quot; method=&quot;POST&quot;&gt;&#10;	&lt;!-- Your existing form fields --&gt;&#10;	&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR_SITE_KEY&gt;&quot;&gt;&lt;/div&gt;&#10;	&lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;&#10;&lt;/form&gt;&#10;</code></pre>
<p>Replace <code>&lt;YOUR_SITE_KEY&gt;</code> with the sitekey from the previous step. The widget renders inside the <code>div</code> and produces a token when the visitor passes the challenge.</p>
<h4 id="3-validate-the-token-on-your-server"><ol start="3">
<li>Validate the token on your server</li>
</ol></h4>
<p>Before processing the form submission, send the token to the Turnstile siteverify endpoint to confirm the visitor passed the challenge:</p>
<pre><code class="language-bash">curl https://challenges.cloudflare.com/turnstile/v0/siteverify \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;  &quot;secret&quot;: &quot;&lt;YOUR_SECRET_KEY&gt;&quot;,&#10;  &quot;response&quot;: &quot;&lt;TURNSTILE_RESPONSE_TOKEN&gt;&quot;&#10;}&#x27;&#10;</code></pre>
<p>Replace <code>&lt;YOUR_SECRET_KEY&gt;</code> with your secret key and <code>&lt;TURNSTILE_RESPONSE_TOKEN&gt;</code> with the <code>cf-turnstile-response</code> value from the form submission. The endpoint returns a JSON object with a <code>success</code> field. Only process the form submission if <code>success</code> is <code>true</code>.</p>
<p>For complete integration details, refer to <a href="/turnstile/get-started/">Turnstile get started</a>.</p>
<h3 id="limit-request-volume-on-form-endpoints-with-rate-limiting">Limit request volume on form endpoints with rate limiting</h3>
<p>For login endpoints, a tiered rate limiting approach works well alongside Turnstile. The following example from the <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> shows two rules that escalate the response based on the volume of failed attempts. Adjust the thresholds for your site's traffic patterns.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tiered-rate-limiting-rules-require-a-business-plan-or-above">Tiered rate limiting rules require a Business plan or above</h3>
@markup("md", "content/.markup/bodies/15093.md")
</aside>
<p><strong>Short-window rule:</strong> Challenge an IP that sends too many failed login requests in a short window.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15102.md")
</div>
<p><strong>Long-window rule:</strong> Block an IP that accumulates failed login attempts over a longer period.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15103.md")
</div>
<p>This pattern uses a counting expression that only counts <code>POST</code> requests returning authentication failure codes. Legitimate users who log in successfully on the first attempt never trigger the rule. Review the results in <a href="/waf/analytics/security-events/">Security Events</a> to confirm the thresholds are not catching legitimate users.</p>
<p>For the full tiered credential stuffing example with three rules, refer to <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a>.</p>
<h2 id="target-bot-patterns-with-custom-rules-and-rate-limiting">Target bot patterns with custom rules and rate limiting</h2>
<p>Application Security <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> let you target specific traffic patterns that built-in bot protection does not catch. Cloudflare separates detection (scoring traffic) from mitigation (acting on those scores). You write rules that reference detection signals to decide what action to take.</p>
<h3 id="block-requests-with-missing-or-suspicious-headers">Block requests with missing or suspicious headers</h3>
<p>Legitimate browsers typically send headers like <code>User-Agent</code>, <code>Accept</code>, and <code>Accept-Language</code>. Many bots omit these headers or send non-browser values. A custom rule targeting requests with empty or suspicious headers catches bots that evade score-based detection.</p>
<p>Before creating custom rules, review the built-in bot settings in <strong>Security</strong> &gt; <strong>Settings</strong> (filter by <em>Bot traffic</em>). These settings handle common scenarios like blocking AI crawlers, challenging automated traffic, and allowing verified bots without requiring you to write expressions. For the full list of built-in settings, refer to <a href="/waf/custom-rules/use-cases/challenge-bad-bots/">Challenge bad bots</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="plan-availability-1">Plan availability</h3>
@markup("md", "content/.markup/bodies/15092.md")
</aside>
<p>If the built-in settings do not cover your needs, create custom rules. Start by creating an exception for verified bots so they are protected before you deploy any blocking rules.</p>
<p>Navigate to custom rules, then create both rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15104.md")
</div>
<p><strong>First, create a verified bot exception:</strong></p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15105.md")
</div>
<p>This ensures verified bots (search engine crawlers, monitoring services) bypass your custom rules. If you have internal APIs, partner integrations, or monitoring tools that send automated traffic, create additional Skip rules for their IP addresses or user agents before deploying blocking rules. Review your expected automated traffic in <a href="/waf/analytics/security-events/">Security Events</a> to identify what to allowlist.</p>
<p><strong>Then, create a blocking rule:</strong></p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15106.md")
</div>
<p>For additional custom rule options including the visual field builder, refer to <a href="/waf/custom-rules/create-dashboard/">Create a custom rule in the dashboard</a>.</p>
<p>If your bot traffic is concentrated from countries where you have no real users, you can combine geographic filters with the rules above. Add <code>ip.src.country</code> to your expression to restrict the rule to specific regions. For examples, refer to <a href="/waf/custom-rules/use-cases/block-by-geographical-location/">Block traffic by geographical location</a>.</p>
<h3 id="protect-high-frequency-paths-with-rate-limiting">Protect high-frequency paths with rate limiting</h3>
<p>Beyond form endpoints, bots also target checkout flows, API endpoints, and other high-value paths. Rate limiting rules cap the number of requests a single client can make to these paths within a time window.</p>
<p>The following example creates a rate limiting rule for a checkout endpoint. Adjust the path, rate, and action for your site.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="rate-limiting-options-vary-by-plan">Rate limiting options vary by plan</h3>
@markup("md", "content/.markup/bodies/15091.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15107.md")
</div>
<p>For additional patterns and thresholds, refer to <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="security-analytics-rate-analysis-requires-an-enterprise-plan">Security Analytics rate analysis requires an Enterprise plan</h3>
@markup("md", "content/.markup/bodies/15090.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enterprise-bot-management-bot-score-in-custom-rules">Enterprise Bot Management: bot score in custom rules</h3>
@markup("md", "content/.markup/bodies/15089.md")
</aside>
<h2 id="verify-and-tune-your-rules">Verify and tune your rules</h2>
<p>After you deploy bot protection rules, use <a href="/waf/analytics/security-events/">Security Events</a> to verify they are working as intended and adjust thresholds based on the results.</p>
<h3 id="check-security-events">Check Security Events</h3>
<p>Security Events displays requests that Cloudflare security products acted on or flagged, including blocks, challenges, and flags.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Events</strong> tab.</li>
</ol>
<p>Review the <strong>Sampled logs</strong> to inspect individual requests. Each log entry shows the action taken, the rule that triggered, the source IP, user agent, URI path, and country. Available dashboard sections vary by plan. Refer to <a href="/waf/analytics/security-events/#availability">Security Events availability</a> for your plan's features.</p>
<p>Look for false positives (legitimate traffic that your rules incorrectly challenged or blocked). Common signs include:</p>
<ul>
<li>Requests from known monitoring services or payment processors appearing in blocked events</li>
<li>User agents matching legitimate browsers but receiving challenges</li>
<li>High volumes of challenged requests from countries where you have real users</li>
</ul>
<p>For rules using the Managed Challenge action, check the <a href="/cloudflare-challenges/reference/challenge-solve-rate/">challenge solve rate (CSR)</a>. A low CSR likely indicates the rule is effectively filtering automated traffic rather than legitimate users.</p>
<p><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> and <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> are aggressive by design. False positives are expected, especially in the first few days after turning them on. The key difference between the two is how you handle exceptions:</p>
<ul>
<li><strong>Bot Fight Mode</strong> (Free) cannot be bypassed with custom rule Skip actions. You can turn off Bot Fight Mode or upgrade to Super Bot Fight Mode for more control.</li>
<li><strong>Super Bot Fight Mode</strong> (Pro and above) can be bypassed with custom rules using the Skip action, giving you more flexibility to create exceptions.</li>
</ul>
<p>For more information on handling false positives, refer to <a href="/bots/troubleshooting/false-positives/">False positives</a>.</p>
<h3 id="adjust-your-rules">Adjust your rules</h3>
<p>After reviewing Security Events, adjust your rules based on the results.</p>
<p><strong>Scenario 1: Your monitoring tools or services are being blocked.</strong></p>
<p>Internal monitoring tools, health check services, or partner APIs appear in blocked events. The fix depends on which feature is blocking them:</p>
<ul>
<li>If <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> (Pro and above) is blocking the traffic, create a custom rule with a Skip action matching the tool IP address or user agent:
<ol>
<li>Go to the <strong>Security rules</strong> page.</li>
</ol>
</li>
</ul>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> &gt; <strong>Custom rules</strong>.</li>
<li>Enter a descriptive name.</li>
<li>Under <strong>When incoming requests match</strong>, select <strong>Edit expression</strong> and enter: <code>(ip.src eq 192.0.2.1)</code> (replace with your tool's IP address).</li>
<li>Under <strong>Then take action</strong>, select <em>Skip</em>. Then select <strong>All Super Bot Fight Mode rules</strong>.</li>
<li>Select <strong>Deploy</strong>.</li>
</ol>
<ul>
<li>If <a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> (Free) is blocking the traffic, turn off Bot Fight Mode or upgrade to <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> for granular exception rules.</li>
</ul>
<p>For details on Skip action configuration, refer to <a href="/waf/custom-rules/skip/">Configure a rule with the Skip action</a>.</p>
<p><strong>Scenario 2: Malicious traffic is still getting through.</strong></p>
<p>Bot activity appears in Security Events that your current rules do not catch. Bots that stay under rate limits or evade single-signal rules require combining multiple signals. For example, to challenge <code>POST</code> requests to <code>/login</code> that are not from verified bots:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15108.md")
</div>
<p>For more expression fields and examples, refer to <a href="/waf/custom-rules/use-cases/">Custom rules use cases</a>.</p>
<p>If bots are staying under your rate limiting thresholds, edit the rate limiting rule and reduce the request count or shorten the time window.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15088.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enterprise-bot-management">Enterprise Bot Management</h3>
@markup("md", "content/.markup/bodies/15087.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<p><strong>Bots</strong></p>
<ul>
<li><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> — Baseline bot protection available on all plans</li>
<li><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> — Granular bot controls for Pro, Business, and Enterprise plans</li>
<li><a href="/bots/plans/bm-subscription/">Enterprise Bot Management</a> — Machine learning-based bot scoring and behavioral analysis</li>
<li><a href="/bots/bot-analytics/">Bot Analytics</a> — Monitor bot traffic patterns across your domain</li>
</ul>
<p><strong>Application Security</strong></p>
<ul>
<li><a href="/waf/custom-rules/">Custom rules</a> — Write targeted rules using traffic signals and bot scores</li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> — Control request volume to protect endpoints from abuse</li>
<li><a href="/waf/analytics/security-events/">Security Events</a> — Review and investigate mitigated requests</li>
</ul>
<p><strong>Turnstile</strong></p>
<ul>
<li><a href="/turnstile/">Turnstile</a> — Free, privacy-preserving challenge for forms and user interactions</li>
</ul>
