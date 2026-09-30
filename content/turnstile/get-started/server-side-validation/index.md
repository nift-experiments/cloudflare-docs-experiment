---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
  description: Validate Turnstile tokens on your server with the siteverify API.
  full_title: Validate the token · Cloudflare Turnstile docs
  head_html: <title>Validate the token · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Validate Turnstile tokens on your server with the siteverify API."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/get-started/server-side-validation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/get-started/server-side-validation/index.md"><meta property="og:title" content="Validate the token · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Validate Turnstile tokens on your server with the siteverify API."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/get-started/server-side-validation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#page","headline":"Validate the token \u00b7 Cloudflare Turnstile docs","description":"Validate Turnstile tokens on your server with the siteverify API.","url":"https://developers.cloudflare.com/turnstile/get-started/server-side-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/get-started/server-side-validation/
  schema: 1
---
<p>Learn how to securely validate Turnstile tokens on your server using the Siteverify API.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="mandatory-server-side-validation">Mandatory server-side validation</h3>
@markup("md", "content/.markup/bodies/15006.md")
</aside>
<h2 id="process">Process</h2>
<ol>
<li>Client generates token: Visitor completes Turnstile challenge on your webpage.</li>
<li>Token sent to server: Form submission includes the Turnstile token.</li>
<li>Server validates token: Your server calls Cloudflare's Siteverify API.</li>
<li>Cloudflare responds: Returns <code>success</code> or <code>failure</code> and additional data.</li>
<li>Server takes action: Allow or reject the original request based on validation.</li>
</ol>
<h2 id="siteverify-api-overview">Siteverify API overview</h2>
<pre tabindex="0"><code class="language-shell">POST https://challenges.cloudflare.com/turnstile/v0/siteverify&#10;</code></pre>
<h3 id="request-format">Request format</h3>
<p>The API accepts both <code>application/x-www-form-urlencoded</code> and <code>application/json</code> requests, but always returns JSON responses.</p>
<h4 id="required-parameters">Required parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>secret</code></td>
<td>Yes</td>
<td>Your widget's secret key from the Cloudflare dashboard</td>
</tr>
<tr>
<td><code>response</code></td>
<td>Yes</td>
<td>The token from the client-side widget</td>
</tr>
<tr>
<td><code>remoteip</code></td>
<td>No</td>
<td>The visitor's IP address</td>
</tr>
<tr>
<td><code>idempotency_key</code></td>
<td>No</td>
<td>A UUID you generate to safely retry validation requests</td>
</tr>
</tbody>
</table>
<h4 id="token-characteristics">Token characteristics</h4>
<ul>
<li>Maximum length: 2048 characters</li>
<li>Validity period: 300 seconds (5 minutes) from generation</li>
<li>Single use: Each token can only be validated once</li>
<li>Automatic expiry: Tokens automatically expire and cannot be reused</li>
</ul>
<p>The validation token issued by Turnstile is valid for five minutes. If a user submits the form after this period, the token is considered expired. In this scenario, the server-side verification API will return a failure, and the <code>error-codes</code> field in the response will include <code>timeout-or-duplicate</code>.</p>
<p>To ensure a successful validation, the visitor must initiate the request and submit the token to your backend within the five-minute window. Otherwise, the Turnstile widget needs to be refreshed to generate a new token. This can be done using the <code>turnstile.reset</code> function.</p>
<hr />
<h2 id="basic-validation-examples">Basic validation examples</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15012.md")
</div></div>
<hr />
<h2 id="advanced-validation-techniques">Advanced validation techniques</h2>
<pre tabindex="0"><code class="language-js">const crypto = require(&quot;crypto&quot;);&#10;&#10;async function validateWithRetry(token, remoteip, maxRetries = 3) {&#10;	const idempotencyKey = crypto.randomUUID();&#10;&#10;	for (let attempt = 1; attempt &lt;= maxRetries; attempt++) {&#10;		try {&#10;			const formData = new FormData();&#10;			formData.append(&quot;secret&quot;, SECRET_KEY);&#10;			formData.append(&quot;response&quot;, token);&#10;			formData.append(&quot;remoteip&quot;, remoteip);&#10;			formData.append(&quot;idempotency_key&quot;, idempotencyKey);&#10;&#10;			const response = await fetch(&#10;				&quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;				{&#10;					method: &quot;POST&quot;,&#10;					body: formData,&#10;				},&#10;			);&#10;&#10;			const result = await response.json();&#10;&#10;			if (response.ok) {&#10;				return result;&#10;			}&#10;&#10;			// If this is the last attempt, return the error&#10;			if (attempt === maxRetries) {&#10;				return result;&#10;			}&#10;&#10;			// Wait before retrying (exponential backoff)&#10;			await new Promise((resolve) =&gt;&#10;				setTimeout(resolve, Math.pow(2, attempt) * 1000),&#10;			);&#10;		} catch (error) {&#10;			if (attempt === maxRetries) {&#10;				return { success: false, &quot;error-codes&quot;: [&quot;internal-error&quot;] };&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-js">async function validateTurnstileEnhanced(&#10;	token,&#10;	remoteip,&#10;	expectedAction = null,&#10;	expectedHostname = null,&#10;) {&#10;	const validation = await validateTurnstile(token, remoteip);&#10;&#10;	if (!validation.success) {&#10;		return {&#10;			valid: false,&#10;			reason: &quot;turnstile_failed&quot;,&#10;			errors: validation[&quot;error-codes&quot;],&#10;		};&#10;	}&#10;&#10;	// Check if action matches expected value (if specified)&#10;	if (expectedAction &amp;&amp; validation.action !== expectedAction) {&#10;		return {&#10;			valid: false,&#10;			reason: &quot;action_mismatch&quot;,&#10;			expected: expectedAction,&#10;			received: validation.action,&#10;		};&#10;	}&#10;&#10;	// Check if hostname matches expected value (if specified)&#10;	if (expectedHostname &amp;&amp; validation.hostname !== expectedHostname) {&#10;		return {&#10;			valid: false,&#10;			reason: &quot;hostname_mismatch&quot;,&#10;			expected: expectedHostname,&#10;			received: validation.hostname,&#10;		};&#10;	}&#10;&#10;	// Check token age (warn if older than 4 minutes)&#10;	const challengeTime = new Date(validation.challenge_ts);&#10;	const now = new Date();&#10;	const ageMinutes = (now - challengeTime) / (1000 * 60);&#10;&#10;	if (ageMinutes &gt; 4) {&#10;		console.warn(`Token is ${ageMinutes.toFixed(1)} minutes old`);&#10;	}&#10;&#10;	return {&#10;		valid: true,&#10;		data: validation,&#10;		tokenAge: ageMinutes,&#10;	};&#10;}&#10;&#10;// Usage&#10;const result = await validateTurnstileEnhanced(&#10;	token,&#10;	remoteip,&#10;	&quot;login&quot;, // expected action&#10;	&quot;example.com&quot;, // expected hostname&#10;);&#10;&#10;if (result.valid) {&#10;	// Process the request&#10;	console.log(&quot;Validation successful:&quot;, result.data);&#10;} else {&#10;	// Handle validation failure&#10;	console.log(&quot;Validation failed:&quot;, result.reason);&#10;}&#10;</code></pre>
<hr />
<h2 id="api-response-format">API response format</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15015.md")
</div></div>
<h3 id="response-fields">Response fields</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>success</code></td>
<td>Boolean indicating if validation was successful</td>
</tr>
<tr>
<td><code>challenge_ts</code></td>
<td>ISO 8601 timestamp when the challenge was solved</td>
</tr>
<tr>
<td><code>hostname</code></td>
<td>Hostname where the challenge was served</td>
</tr>
<tr>
<td><code>error-codes</code></td>
<td>Array of error codes (if validation failed)</td>
</tr>
<tr>
<td><code>action</code></td>
<td>Custom action identifier from client-side</td>
</tr>
<tr>
<td><code>cdata</code></td>
<td>Custom data payload from client-side</td>
</tr>
<tr>
<td><code>metadata.ephemeral_id</code></td>
<td>Device fingerprint ID (Enterprise only)</td>
</tr>
</tbody>
</table>
<h3 id="error-codes-reference">Error codes reference</h3>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Description</th>
<th>Action required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>missing-input-secret</code></td>
<td>Secret parameter not provided</td>
<td>Ensure secret key is included</td>
</tr>
<tr>
<td><code>invalid-input-secret</code></td>
<td>Secret key is invalid or expired</td>
<td>Check your secret key in the Cloudflare dashboard</td>
</tr>
<tr>
<td><code>missing-input-response</code></td>
<td>Response parameter was not provided</td>
<td>Ensure token is included</td>
</tr>
<tr>
<td><code>invalid-input-response</code></td>
<td>Token is invalid, malformed, or expired</td>
<td>User should retry the challenge</td>
</tr>
<tr>
<td><code>bad-request</code></td>
<td>Request is malformed</td>
<td>Check request format and parameters</td>
</tr>
<tr>
<td><code>timeout-or-duplicate</code></td>
<td>Token has already been validated</td>
<td>Each token can only be used once</td>
</tr>
<tr>
<td><code>internal-error</code></td>
<td>Internal error occurred</td>
<td>Retry the request</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="implementation">Implementation</h2>
<pre tabindex="0"><code class="language-js">class TurnstileValidator {&#10;	constructor(secretKey, timeout = 10000) {&#10;		this.secretKey = secretKey;&#10;		this.timeout = timeout;&#10;	}&#10;&#10;	async validate(token, remoteip, options = {}) {&#10;		// Input validation&#10;		if (!token || typeof token !== &quot;string&quot;) {&#10;			return { success: false, error: &quot;Invalid token format&quot; };&#10;		}&#10;&#10;		if (token.length &gt; 2048) {&#10;			return { success: false, error: &quot;Token too long&quot; };&#10;		}&#10;&#10;		// Prepare request&#10;		const controller = new AbortController();&#10;		const timeoutId = setTimeout(() =&gt; controller.abort(), this.timeout);&#10;&#10;		try {&#10;			const formData = new FormData();&#10;			formData.append(&quot;secret&quot;, this.secretKey);&#10;			formData.append(&quot;response&quot;, token);&#10;&#10;			if (remoteip) {&#10;				formData.append(&quot;remoteip&quot;, remoteip);&#10;			}&#10;&#10;			if (options.idempotencyKey) {&#10;				formData.append(&quot;idempotency_key&quot;, options.idempotencyKey);&#10;			}&#10;&#10;			const response = await fetch(&#10;				&quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;				{&#10;					method: &quot;POST&quot;,&#10;					body: formData,&#10;					signal: controller.signal,&#10;				},&#10;			);&#10;&#10;			const result = await response.json();&#10;&#10;			// Additional validation&#10;			if (result.success) {&#10;				if (&#10;					options.expectedAction &amp;&amp;&#10;					result.action !== options.expectedAction&#10;				) {&#10;					return {&#10;						success: false,&#10;						error: &quot;Action mismatch&quot;,&#10;						expected: options.expectedAction,&#10;						received: result.action,&#10;					};&#10;				}&#10;&#10;				if (&#10;					options.expectedHostname &amp;&amp;&#10;					result.hostname !== options.expectedHostname&#10;				) {&#10;					return {&#10;						success: false,&#10;						error: &quot;Hostname mismatch&quot;,&#10;						expected: options.expectedHostname,&#10;						received: result.hostname,&#10;					};&#10;				}&#10;			}&#10;&#10;			return result;&#10;		} catch (error) {&#10;			if (error.name === &quot;AbortError&quot;) {&#10;				return { success: false, error: &quot;Validation timeout&quot; };&#10;			}&#10;&#10;			console.error(&quot;Turnstile validation error:&quot;, error);&#10;			return { success: false, error: &quot;Internal error&quot; };&#10;		} finally {&#10;			clearTimeout(timeoutId);&#10;		}&#10;	}&#10;}&#10;&#10;// Usage&#10;const validator = new TurnstileValidator(process.env.TURNSTILE_SECRET_KEY);&#10;&#10;const result = await validator.validate(token, remoteip, {&#10;	expectedAction: &quot;login&quot;,&#10;	expectedHostname: &quot;example.com&quot;,&#10;});&#10;&#10;if (result.success) {&#10;	// Process the request&#10;} else {&#10;	// Handle failure&#10;	console.log(&quot;Validation failed:&quot;, result.error);&#10;}&#10;</code></pre>
<hr />
<h2 id="testing">Testing</h2>
<p>You can test the dummy token generated with testing sitekey via Siteverify API with the testing secret key. Your production secret keys will reject dummy tokens.</p>
<p>Refer to <a href="/turnstile/troubleshooting/testing/">Testing</a> for more information.</p>
<hr />
<h2 id="best-practices">Best practices</h2>
<h3 id="security">Security</h3>
<ul>
<li>Store your secret keys securely. Use environment variables or secure key management.</li>
<li>Validate the token on every request. Never trust client-side validation alone.</li>
<li>Check additional fields. Validate the action and hostname when specified.</li>
<li>Monitor for abuse and log failed validations and unusual patterns.</li>
<li>Use HTTPS. Always validate over secure connections.</li>
<li>Only call the Siteverify API in your backend environment. If you expose the secret key in the front-end client code to call Siteverify, attackers can bypass the security check. Ensure that your client-side code sends the validation token to your backend, and that your backend is the sole caller of the Siteverify API.</li>
</ul>
<h3 id="performance">Performance</h3>
<ul>
<li>Set reasonable timeouts. Do not wait indefinitely for Siteverify responses.</li>
<li>Implement retry logic and handle temporary network issues.</li>
<li>Cache validation results for the same token, if it is needed for your flow.</li>
<li>Monitor your API latency. Track the Siteverify response time.</li>
</ul>
<h3 id="error-handling">Error handling</h3>
<ul>
<li>Have fallback behavior for API failures.</li>
<li>Use user-friendly messaging. Do not expose internal error details to users.</li>
<li>Properly log errors for debugging without exposing secrets.</li>
<li>Rate limit to protect against validation flooding.</li>
</ul>
