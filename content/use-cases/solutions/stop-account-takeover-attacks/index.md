---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/
  description: Block credential stuffing and brute force attacks on login endpoints using a layered defense.
  full_title: Stop account takeover attacks (Free, Pro, and Business) · Cloudflare use cases
  head_html: <title>Stop account takeover attacks (Free, Pro, and Business) · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Block credential stuffing and brute force attacks on login endpoints using a layered defense."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/index.md"><meta property="og:title" content="Stop account takeover attacks (Free, Pro, and Business) · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block credential stuffing and brute force attacks on login endpoints using a layered defense."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Solution guide"><meta name="algolia_content_type" content="Solution guide"><meta name="pcx_additional_products" content="Bots,SSL/TLS,Turnstile,WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/#page","headline":"Stop account takeover attacks (Free, Pro, and Business) \u00b7 Cloudflare use cases","description":"Block credential stuffing and brute force attacks on login endpoints using a layered defense.","url":"https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/solutions/stop-account-takeover-attacks/
  schema: 1
---
<p>When your site has login pages, you need to decide how to verify that visitors are human, how aggressively to limit failed attempts, and which request patterns to block. This guide covers five stages: enforce HTTPS, turn on bot protection, add <a href="/turnstile/">Turnstile</a> to your login form, create Application Security <a href="/waf/rate-limiting-rules/">rate limiting rules</a> and <a href="/waf/custom-rules/">custom rules</a> for suspicious patterns, and monitor for ongoing attacks using <a href="/ssl/">SSL/TLS</a> transport security and <a href="/bots/">Cloudflare bot solutions</a>. The core workflow covers features available on Free, Pro, and Business plans. Enterprise features such as leaked credentials custom detection locations and Bot Management custom rules are included as callouts.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15122.md")
</aside>
<h2 id="enforce-https-to-protect-credentials-in-transit">Enforce HTTPS to protect credentials in transit</h2>
<p>Credentials sent over plain HTTP are visible to anyone on the network path between the visitor and your origin server. Cloudflare <a href="/ssl/">SSL/TLS</a> provides two settings that enforce HTTPS connections: <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> and <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">HTTP Strict Transport Security (HSTS)</a>. For additional control over which encryption standards your domain accepts, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/">Cipher suites</a>.</p>
<h3 id="turn-on-always-use-https">Turn on Always Use HTTPS</h3>
<p>Always Use HTTPS redirects all visitor requests from <code>http</code> to <code>https</code> for all subdomains and hosts.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15125.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15121.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="optional-http-strict-transport-security-hsts">Optional: HTTP Strict Transport Security (HSTS)</h3>
@markup("md", "content/.markup/bodies/15120.md")
</aside>
<h2 id="turn-on-bot-protection">Turn on bot protection</h2>
<p>Cloudflare provides bot protection on all plans, with features that vary by plan tier. Turning on bot protection before configuring login-specific rules gives you a baseline filter against automated traffic across your entire domain.</p>
<h3 id="bot-fight-mode-free">Bot Fight Mode (Free)</h3>
<p>Bot Fight Mode challenges requests that match known bot patterns. It applies to all traffic on your domain and cannot be customized with exceptions or path-specific rules.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15126.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15119.md")
</aside>
<h3 id="super-bot-fight-mode-pro-business-and-enterprise">Super Bot Fight Mode (Pro, Business, and Enterprise)</h3>
<p>Super Bot Fight Mode identifies traffic matching patterns of known bots, can challenge or block bots, and offers protection for static resources. You configure a separate action for each bot grouping: <strong>Definitely automated</strong>, <strong>Likely automated</strong>, and <strong>Verified bots</strong>. You can also <a href="/bots/get-started/super-bot-fight-mode/#configure-exceptions-to-super-bot-fight-mode">configure exceptions</a> using Application Security <a href="/waf/custom-rules/">custom rules</a> with the Skip action.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15118.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15127.md")
</div>
<p>For login protection, the following are recommended starting values. Adjust based on your traffic patterns.</p>
<ul>
<li><strong>Definitely automated</strong>: <em>Managed Challenge</em>. After reviewing Security Events to confirm the setting does not affect legitimate traffic, switch to <em>Block</em>.</li>
<li><strong>Likely automated</strong>: <em>Managed Challenge</em>.</li>
<li><strong>Verified bots</strong>: <em>Allow</em>.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15117.md")
</aside>
<p><a href="/waf/custom-rules/">Custom rules</a> are executed before Super Bot Fight Mode. To create exceptions for specific paths or traffic, create a custom rule with the <a href="/waf/custom-rules/skip/">Skip action</a>. The Skip action allows the request to bypass the Super Bot Fight Mode phase without terminating the request, enabling it to continue through the rest of the security stack.</p>
<h2 id="protect-your-login-form-with-turnstile-and-rate-limiting">Protect your login form with Turnstile and rate limiting</h2>
<p>Two tools protect login endpoints from automated abuse, and they cover different attack vectors:</p>
<ul>
<li><strong><a href="/turnstile/">Turnstile</a></strong> verifies that visitors are human without showing a CAPTCHA. It can be embedded into any website without sending traffic through Cloudflare. Use Turnstile to challenge automated form submissions.</li>
<li><strong>Application Security <a href="/waf/rate-limiting-rules/">rate limiting rules</a></strong> define rate limits for requests matching an expression and the action to perform when those limits are reached. Use rate limiting to protect login endpoints from abuse, such as brute-force attacks.</li>
</ul>
<p>Both together provide the strongest coverage. Turnstile challenges automated submissions at the form level. Rate limiting catches high-volume attacks that bypass or do not encounter the form, such as direct <code>POST</code> requests to the endpoint.</p>
<h3 id="add-turnstile-to-your-login-form">Add Turnstile to your login form</h3>
<p>Implementing Turnstile involves three steps: create a widget, add the client-side snippet to your login form, and validate the token on your server. Turnstile supports multiple <a href="/turnstile/get-started/client-side-rendering/">rendering methods</a> including explicit and implicit rendering. You can also <a href="/workers/examples/turnstile-html-rewriter/">inject Turnstile into HTML using a Cloudflare Worker</a> if you do not control the login form source code.</p>
<h4 id="1-create-a-turnstile-widget"><ol>
<li>Create a Turnstile widget</li>
</ol></h4>
<p>Turnstile is configured at the account level.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15128.md")
</div>
<p>You need both the sitekey and secret key in the following steps.</p>
<h4 id="2-add-the-client-side-snippet"><ol start="2">
<li>Add the client-side snippet</li>
</ol></h4>
<p>Add the Turnstile script and widget container to your login form. Replace <code>&lt;YOUR-SITE-KEY&gt;</code> with the sitekey from the previous step.</p>
<pre tabindex="0"><code class="language-html">&lt;form id=&quot;login-form&quot;&gt;&#10;	&lt;input type=&quot;text&quot; id=&quot;username&quot; placeholder=&quot;Username&quot; required /&gt;&#10;	&lt;input type=&quot;password&quot; id=&quot;password&quot; placeholder=&quot;Password&quot; autocomplete=&quot;off&quot; required /&gt;&#10;	&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&gt;&lt;/div&gt;&#10;	&lt;button type=&quot;submit&quot;&gt;Log in&lt;/button&gt;&#10;&lt;/form&gt;&#10;&#10;&lt;script&#10;	src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;&#10;	async&#10;	defer&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<p>The widget renders inside the <code>div</code> and produces a token when the visitor passes the challenge. When the form is submitted, a <code>cf-turnstile-response</code> token is included in the form data.</p>
<h4 id="3-validate-the-token-on-your-server"><ol start="3">
<li>Validate the token on your server</li>
</ol></h4>
<p>Before processing the form submission, send the token to the Turnstile siteverify endpoint to confirm the visitor passed the challenge.</p>
<pre tabindex="0"><code class="language-js">const SECRET_KEY = &quot;&lt;YOUR-SECRET-KEY&gt;&quot;;&#10;&#10;async function validateTurnstile(token, remoteip) {&#10;	try {&#10;		const response = await fetch(&#10;			&quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;			{&#10;				method: &quot;POST&quot;,&#10;				headers: {&#10;					&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				},&#10;				body: JSON.stringify({&#10;					secret: SECRET_KEY,&#10;					response: token,&#10;					remoteip: remoteip,&#10;				}),&#10;			},&#10;		);&#10;&#10;		const result = await response.json();&#10;		return result;&#10;	} catch (error) {&#10;		console.error(&quot;Turnstile validation error:&quot;, error);&#10;		return { success: false, &quot;error-codes&quot;: [&quot;internal-error&quot;] };&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>&quot;&lt;YOUR-SECRET-KEY&gt;&quot;</code> with your Turnstile secret key. The endpoint returns a JSON object with a <code>success</code> field. Only process the form submission if <code>success</code> is <code>true</code>.</p>
<p>For additional fraud detection, Turnstile supports <a href="/turnstile/tutorials/fraud-detection-with-ephemeral-ids/">Ephemeral IDs</a> that provide a unique, temporary identifier for each visitor session without storing personal data.</p>
<p>For the complete response format, error codes, and examples in other languages, refer to <a href="/turnstile/get-started/server-side-validation/">Validate the token</a>.</p>
<h4 id="test-your-implementation">Test your implementation</h4>
<p>Turnstile provides test site keys that return predictable results without contacting the Siteverify API.</p>
<ul>
<li><strong>Always passes</strong>: Use site key <code>1x00000000000000000000AA</code> and secret key <code>1x0000000000000000000000000000000AA</code> to simulate a successful challenge.</li>
<li><strong>Always blocks</strong>: Use site key <code>2x00000000000000000000AB</code> and secret key <code>2x0000000000000000000000000000000AA</code> to simulate a failed challenge.</li>
<li><strong>Forces interactive challenge</strong>: Use site key <code>3x00000000000000000000FF</code> to test the interactive challenge flow.</li>
</ul>
<p>For the full list of test keys and expected behaviors, refer to <a href="/turnstile/troubleshooting/testing/">Test your Turnstile implementation</a>.</p>
<h3 id="rate-limit-your-login-endpoint">Rate limit your login endpoint</h3>
<h4 id="create-a-rate-limiting-rule-for-your-login-endpoint">Create a rate limiting rule for your login endpoint</h4>
<p>The following example creates a rate limiting rule that issues a Managed Challenge after more than five POST requests to your login path from the same IP within one minute. Start with Managed Challenge rather than Block. Managed Challenge allows legitimate users who trigger the limit to pass by completing a challenge, while blocking automated traffic that cannot solve it. After monitoring <a href="/waf/analytics/security-events/">Security Events</a> to confirm the rule is not producing false positives, switch to Block. Adjust the path (<code>/login</code>), threshold, and period for your site.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15116.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15129.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15115.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="advanced-rate-limiting-enterprise">Advanced Rate Limiting (Enterprise)</h3>
@markup("md", "content/.markup/bodies/15114.md")
</aside>
<h4 id="escalating-rate-limits-for-persistent-attackers">Escalating rate limits for persistent attackers</h4>
<p>For sites that experience sustained credential stuffing campaigns, consider deploying multiple rate limiting rules with increasing severity. The <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> page describes an escalating penalty pattern that uses three rules: a short-window rule for quick bursts, a medium-window rule for slower distributed attacks, and a long-window rule that blocks persistent attackers from the entire domain. The counting expressions use response status codes, so successful logins do not count against the limit. Refer to the best practices page for the recommended thresholds and expression syntax.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15113.md")
</aside>
<h2 id="add-application-security-rules-for-suspicious-login-patterns">Add Application Security rules for suspicious login patterns</h2>
<p>Application Security <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/detections/">traffic detections</a> give you additional signals beyond request rate to identify and act on suspicious login traffic. Detections populate request fields (such as leaked credential status and bot score) that your custom rules can then reference.</p>
<h3 id="turn-on-leaked-credentials-detection">Turn on leaked credentials detection</h3>
<p>Leaked credentials detection scans incoming login requests for usernames and passwords that appear in known data breach databases. Cloudflare hashes credentials before comparison and does not store plaintext passwords. When a match is found, the detection populates fields you can use in custom rules and rate limiting rules.</p>
<p>The <code>cf.waf.credential_check.password_leaked</code> field is available on all plans.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15112.md")
</aside>
<p>On Free plans, the leaked credentials detection is enabled by default, and no action is required. On paid plans, you can turn on the detection in the Cloudflare dashboard, via API, or using Terraform.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15134.md")
</div></div>
<p>After turning on the detection, your origin server can receive leaked credential status via the <code>Exposed-Credential-Check</code> request header. To forward this header, turn on the <a href="/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header">Add leaked credentials checks header</a> managed transform. Your origin can then trigger a password reset for affected users.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enterprise-custom-detection-locations">Enterprise: Custom detection locations</h3>
@markup("md", "content/.markup/bodies/15111.md")
</aside>
<h3 id="create-a-skip-rule-for-legitimate-automated-traffic">Create a skip rule for legitimate automated traffic</h3>
<p>Before deploying rules that challenge or block login traffic, create a skip rule that exempts known legitimate automated traffic. This prevents your monitoring tools, health checks, and partner integrations from being blocked by the rules that follow.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15135.md")
</div>
<p>For more information about the Skip action and available skip options, refer to <a href="/waf/custom-rules/skip/">Skip action</a>.</p>
<h3 id="block-requests-with-suspicious-headers">Block requests with suspicious headers</h3>
<p>Credential stuffing tools often send requests without standard browser headers or with known-bad User-Agent patterns. Create a custom rule that issues a Managed Challenge for POST requests to your login path where the User-Agent is empty. This targets direct POST requests from tools like <code>curl</code>, <code>python-requests</code>, or <code>undici</code> that do not set a User-Agent header.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15110.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15136.md")
</div>
<h3 id="create-a-rate-limiting-rule-with-leaked-credentials">Create a rate limiting rule with leaked credentials</h3>
<p>Combine rate limiting with leaked credentials detection to throttle login attempts that use known-compromised passwords. This rule issues a Managed Challenge when the same IP sends more than three requests with leaked passwords within one minute.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15137.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enterprise-bot-management">Enterprise: Bot Management</h3>
@markup("md", "content/.markup/bodies/15109.md")
</aside>
<h2 id="monitor-for-ongoing-compromise-attempts">Monitor for ongoing compromise attempts</h2>
<p>After deploying the rules and configurations from the previous sections, monitor your login endpoint to verify the rules are working and to detect new attack patterns.</p>
<h3 id="review-security-events">Review Security Events</h3>
<p><a href="/waf/analytics/security-events/">Security Events</a> shows requests that Cloudflare security products acted on or flagged, including blocks, challenges, and skips.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15138.md")
</div>
<p>Review the <strong>Sampled logs</strong> to inspect individual requests. Each log entry shows the action taken, the rule that triggered, the source IP, user agent, URI path, and country. Use the <strong>Add filter</strong> button to narrow results by action, source IP, ASN, or other fields.</p>
<p>Look for false positives — legitimate traffic that your rules incorrectly challenged or blocked. Common signs include:</p>
<ul>
<li>Requests from known monitoring services or payment processors appearing in blocked events</li>
<li>High volumes of challenged requests from countries where you have real users</li>
<li>Rate limiting rules triggering on legitimate users during peak traffic</li>
</ul>
<p>If you see legitimate users being affected, adjust your rate limiting thresholds or add skip rules for specific IP ranges.</p>
<h3 id="set-up-notifications-for-security-event-spikes-business-and-enterprise">Set up notifications for security event spikes (Business and Enterprise)</h3>
<p>Set up a <strong>Security Events Alert</strong> notification to receive alerts when security event volume spikes, giving you early warning of a new attack campaign. This notification is in the <strong>WAF</strong> category of the <a href="/notifications/">Notifications</a> page. For setup instructions, refer to <a href="/notifications/get-started/">Create a notification</a>. Enterprise customers can use <strong>Advanced Security Events Alert</strong> for more granular filtering.</p>
<h3 id="review-bot-traffic-patterns-pro-and-above">Review bot traffic patterns (Pro and above)</h3>
<p>Bot traffic analytics show bot score distribution on your login endpoint over time. A sudden spike in low-score traffic (scores 1-29) on your login path is an early signal of a credential stuffing campaign.</p>
<p>Cloudflare classifies bot traffic into categories based on bot scores and verification status:</p>
<ul>
<li><strong>Verified bots</strong>: Crawlers and services that Cloudflare has confirmed as legitimate, such as Googlebot, Bingbot, and uptime monitors. Cloudflare maintains a <a href="/bots/concepts/bot/verified-bots/">verified bot list</a> with strict requirements.</li>
<li><strong>Automated</strong> (score 1): Cloudflare is quite certain the request is automated.</li>
<li><strong>Likely automated</strong> (scores 2-29): Probably a bot. This category and Automated are the primary targets for security rules, including scrapers, credential stuffing tools, and spam submitters.</li>
<li><strong>Likely human</strong> (scores 30-99): These requests appear to come from real users. Do not challenge or block this traffic.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15139.md")
</div>
<p>If you see sustained automated traffic reaching your login endpoint despite the rules deployed in this guide, review the <a href="/waf/feature-interoperability/">Security features interoperability</a> page to verify your rules are executing in the expected order, and consider adjusting thresholds.</p>
<h2 id="related-resources">Related resources</h2>
<p><strong>Application Security</strong></p>
<ul>
<li><a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> — recommended patterns for login protection and credential stuffing</li>
<li><a href="/waf/custom-rules/">Custom rules</a> — create rules using request fields including bot score and leaked credentials</li>
<li><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> — scan incoming requests for credentials from known data breaches</li>
<li><a href="/waf/analytics/security-events/">Security Events</a> — review requests acted on by security products</li>
</ul>
<p><strong>Cloudflare Bots</strong></p>
<ul>
<li><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> — free bot protection that challenges known bot patterns</li>
<li><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> — Pro and Business bot protection with configurable actions</li>
<li><a href="/bots/get-started/bot-management/">Bot Management</a> — Enterprise bot protection with ML-powered scoring and custom rules</li>
</ul>
<p><strong>Turnstile</strong></p>
<ul>
<li><a href="/turnstile/get-started/">Get started with Turnstile</a> — create widgets and implement client-side and server-side validation</li>
<li><a href="/turnstile/get-started/server-side-validation/">Server-side validation</a> — validate Turnstile tokens on your server</li>
<li><a href="/turnstile/additional-configuration/pre-clearance-support/">Turnstile Pre-Clearance</a> — pre-clear visitors for SPA and AJAX login flows</li>
</ul>
<p><strong>SSL/TLS</strong></p>
<ul>
<li><a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> — redirect all HTTP requests to HTTPS</li>
<li><a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">HTTP Strict Transport Security (HSTS)</a> — prevent browser downgrade attacks with HSTS headers</li>
</ul>
