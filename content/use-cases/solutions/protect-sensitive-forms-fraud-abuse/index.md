<p>Contact, registration, and checkout forms are common targets for automated abuse. This guide covers form protection: verifying that visitors are human, limiting repeated submissions, and blocking known attack patterns. The core workflow uses features available on all plans. Pro and Business plan features are included as callouts.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15144.md")
</aside>
<h2 id="add-turnstile-to-your-forms">Add Turnstile to your forms</h2>
<p>Turnstile verifies visitors are human without visible challenges. This guide uses Managed mode, which automatically chooses between a non-interactive or checkbox challenge based on visitor risk level. For other widget modes, refer to <a href="/turnstile/concepts/widget/">Widget types</a>.</p>
<p>Adding Turnstile involves three steps: create a widget in the dashboard, add the client-side snippet to your form page, and validate the token on your server before processing the submission.</p>
<h3 id="create-a-turnstile-widget">Create a Turnstile widget</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15145.md")
</div>
<p>Store the sitekey and secret key. You will use the sitekey in the client-side snippet and the secret key for server-side validation.</p>
<h3 id="add-the-client-side-snippet">Add the client-side snippet</h3>
<p>Add the Turnstile script and widget <code>div</code> element to each form you want to protect. Replace <code>&lt;YOUR-SITE-KEY&gt;</code> with the sitekey from the previous step.</p>
<pre><code class="language-html">&lt;form id=&quot;contact-form&quot; action=&quot;/submit&quot; method=&quot;POST&quot;&gt;&#10;  &lt;input type=&quot;text&quot; name=&quot;name&quot; placeholder=&quot;Name&quot; required /&gt;&#10;  &lt;input type=&quot;email&quot; name=&quot;email&quot; placeholder=&quot;Email&quot; required /&gt;&#10;  &lt;textarea name=&quot;message&quot; placeholder=&quot;Message&quot; required&gt;&lt;/textarea&gt;&#10;  &lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&gt;&lt;/div&gt;&#10;  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;&#10;&lt;/form&gt;&#10;&#10;&lt;script src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot; async defer&gt;&lt;/script&gt;&#10;</code></pre>
<p>The widget renders in the form and generates a token when the visitor passes verification. The token is included in the form submission as the <code>cf-turnstile-response</code> field.</p>
<h3 id="validate-the-token-on-your-server">Validate the token on your server</h3>
<p>Server-side validation is required. The client-side widget alone does not protect your forms because attackers can submit directly to your form endpoint. Tokens can only be validated once.</p>
<p>Call the Siteverify API before processing any form submission:</p>
<pre><code class="language-js">const SECRET_KEY = &quot;&lt;YOUR-SECRET-KEY&gt;&quot;;&#10;&#10;async function validateTurnstile(token, remoteip) {&#10;  try {&#10;    const response = await fetch(&#10;      &quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;      {&#10;        method: &quot;POST&quot;,&#10;        headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;        body: JSON.stringify({&#10;          secret: SECRET_KEY,&#10;          response: token,&#10;          remoteip: remoteip,&#10;        }),&#10;      },&#10;    );&#10;&#10;    const result = await response.json();&#10;    return result;&#10;  } catch (error) {&#10;    console.error(&quot;Turnstile validation error:&quot;, error);&#10;    return { success: false, &quot;error-codes&quot;: [&quot;internal-error&quot;] };&#10;  }&#10;}&#10;</code></pre>
<p>Replace <code>&quot;&lt;YOUR-SECRET-KEY&gt;&quot;</code> with your Turnstile secret key. The endpoint returns a JSON object with a <code>success</code> field. Only process the form submission if <code>success</code> is <code>true</code>.</p>
<p>For validation examples in PHP, Python, Java, and C#, refer to <a href="/turnstile/get-started/server-side-validation/">Validate the token</a>.</p>
<h2 id="rate-limit-form-submission-endpoints">Rate limit form submission endpoints</h2>
<p>Some abuse scripts skip the browser entirely and POST directly to your form endpoints. Application Security <a href="/waf/rate-limiting-rules/">rate limiting rules</a> catch these requests because client-side verification only runs in a browser.</p>
<h3 id="find-your-baseline-request-rate">Find your baseline request rate</h3>
<p>Before creating a rate limiting rule, check the normal submission rate for your form endpoints. Your rate limit threshold should be above this baseline to avoid blocking legitimate traffic.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15146.md")
</div>
<p>If you do not have enough traffic data to establish a baseline, start with a conservative threshold and adjust based on Security Events after deployment.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enterprise-request-rate-analysis">Enterprise: Request rate analysis</h3>
@markup("md", "content/.markup/bodies/15143.md")
</aside>
<h3 id="create-a-rate-limiting-rule">Create a rate limiting rule</h3>
<p>Create a rule that limits how many times a single IP address can submit to your form endpoint within a given period. Adjust the path, threshold, and period for your site.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15147.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15142.md")
</aside>
<h3 id="configure-a-custom-response-for-blocked-requests-pro-and-above">Configure a custom response for blocked requests (Pro and above)</h3>
<p>Instead of showing the default Cloudflare error page when a rate limit is reached, you can configure a custom response. For details, refer to <a href="/waf/rate-limiting-rules/create-zone-dashboard/#configure-a-custom-response-for-blocked-requests">Create a rate limiting rule in the dashboard</a>.</p>
<h2 id="add-application-security-rules-for-known-abuse-patterns">Add Application Security rules for known abuse patterns</h2>
<p>Rate limiting alone does not catch targeted attack patterns like SQL injection or cross-site scripting (XSS) in form fields. Application Security <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/managed-rules/">managed rulesets</a> let you block these specific patterns targeting your form endpoints. Custom rules run before rate limiting rules and managed rulesets in the <a href="/waf/feature-interoperability/">execution order</a>.</p>
<h3 id="challenge-non-bot-requests-to-form-endpoints">Challenge non-bot requests to form endpoints</h3>
<p>Create a custom rule that challenges POST requests to your form endpoints from sources that are not verified bots.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15148.md")
</div>
<p>After deploying, review <a href="/waf/analytics/security-events/">Security Events</a> to check whether the rule is matching legitimate traffic. If legitimate users are being challenged, narrow the expression or switch to a less aggressive action.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pro-plans-and-above-managed-rulesets">Pro plans and above: Managed rulesets</h3>
@markup("md", "content/.markup/bodies/15141.md")
</aside>
<h2 id="turn-on-bot-protection">Turn on bot protection</h2>
<p>Bot Fight Mode challenges requests that match known bot patterns across your entire domain. It is available on all plans and requires no configuration beyond turning it on.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15149.md")
</div>
<p>Bot Fight Mode protects your entire domain without endpoint restrictions. You cannot create exceptions using custom rules to bypass Bot Fight Mode.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pro-business-and-enterprise">Pro, Business, and Enterprise</h3>
@markup("md", "content/.markup/bodies/15140.md")
</aside>
<h2 id="monitor-your-form-endpoints">Monitor your form endpoints</h2>
<p>After deploying Turnstile, rate limiting rules, and Application Security rules, monitor your form endpoints to verify your rules are working and to detect new attack patterns.</p>
<h3 id="review-security-events">Review Security Events</h3>
<p><a href="/waf/analytics/security-events/">Security Events</a> shows requests that Cloudflare security products acted on or flagged, including blocks, challenges, and skips. Filter by your form endpoint paths to see what is being blocked and what is getting through. A high volume of blocked or challenged requests to your form paths confirms the rules are active.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15150.md")
</div>
<p>If legitimate users are being challenged, narrow the rule expression or switch to a less aggressive action.</p>
<h3 id="set-up-security-event-alerts">Set up security event alerts</h3>
<p>Configure a notification to receive alerts when there is an unusual spike in security events on your domain.</p>
<p>For alert types, trigger thresholds, and setup instructions, refer to <a href="/waf/reference/alerts/">Alerts for security events</a>.</p>
<h3 id="turn-on-client-side-resource-monitoring">Turn on client-side resource monitoring</h3>
<p>If a third-party script is injected into your form page, it can exfiltrate submitted data, including payment information. Client-Side Security monitors third-party scripts on your pages for changes and potential supply chain attacks.</p>
<p>To enable monitoring:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15151.md")
</div>
<p>After enabling, review detected scripts on the <strong>Web assets</strong> page under the <strong>Client-side resources</strong> tab to identify any unexpected scripts on your form pages. For the full setup workflow, refer to <a href="/client-side-security/get-started/">Get started with client-side security</a>.</p>
<h2 id="related-resources">Related resources</h2>
<p><strong>Turnstile</strong></p>
<ul>
<li><a href="/turnstile/get-started/">Get started with Turnstile</a> — create widgets, add the client snippet, and validate tokens</li>
<li><a href="/turnstile/get-started/server-side-validation/">Validate the token</a> — server-side validation examples in multiple languages</li>
<li><a href="/turnstile/tutorials/integrating-turnstile-waf-and-bot-management/">Integrate Turnstile, WAF, and Bot Management</a> — tutorial combining all three products for login protection</li>
</ul>
<p><strong>Application Security</strong></p>
<ul>
<li><a href="/waf/custom-rules/">Custom rules</a> — create rules targeting specific request patterns</li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> — protect endpoints from high-volume abuse</li>
<li><a href="/waf/feature-interoperability/">Security features interoperability</a> — execution order and interaction between security features</li>
</ul>
<p><strong>Bots</strong></p>
<ul>
<li><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> — challenge requests matching bot patterns on Free plans</li>
<li><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> — granular bot controls for Pro and above</li>
</ul>
<p><strong>Client-Side Security</strong></p>
<ul>
<li><a href="/client-side-security/get-started/">Get started with client-side security</a> — enable monitoring and review detected scripts</li>
</ul>
