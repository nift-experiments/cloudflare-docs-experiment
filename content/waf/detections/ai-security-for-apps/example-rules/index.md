---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/
  description: Example mitigation rules for AI Security for Apps detections.
  full_title: Example mitigation rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Example mitigation rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Example mitigation rules for AI Security for Apps detections."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/index.md"><meta property="og:title" content="Example mitigation rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example mitigation rules for AI Security for Apps detections."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/#page","headline":"Example mitigation rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Example mitigation rules for AI Security for Apps detections.","url":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/ai-security-for-apps/example-rules/
  schema: 1
---
<h2 id="return-a-custom-error-when-a-user-asks-about-violent-or-hateful-content">Return a custom error when a user asks about violent or hateful content</h2>
<p>A customer support chatbot should not engage with prompts about violent crimes or hate speech. This <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks the request and returns a JSON response that your application can parse and display to the user.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>LLM Unsafe topic categories</td>
<td>is in</td>
<td><code>S1: Violent Crimes</code> <code>S10: Hate</code></td>
</tr>
</tbody>
</table>
<p>Expression when using the editor:<br />
<code>(any(cf.llm.prompt.unsafe_topic_categories[*] in {&quot;S1&quot; &quot;S10&quot;}))</code></p>
<ul>
<li><strong>Action</strong>: <em>Block</em></li>
<li><strong>With response type</strong>: Custom JSON</li>
<li><strong>Response body</strong>:</li>
</ul>
<pre tabindex="0"><code class="language-txt">{ &quot;error&quot;: &quot;content_policy&quot;, &quot;message&quot;: &quot;Your message could not be processed because it touches on a topic outside this assistant&#x27;s scope. Please rephrase your question.&quot; }&#10;</code></pre>
<p>Your application can check for a non-200 response and display the <code>message</code> field to the user, keeping the experience conversational instead of showing a raw block page.</p>
<h2 id="block-prompt-injection-attempts-from-automated-sources-outside-your-country">Block prompt injection attempts from automated sources outside your country</h2>
<p>This rule combines AI Security for Apps's <a href="/waf/detections/ai-security-for-apps/prompt-injection/">injection score</a> with <a href="/bots/get-started/">Bot Management</a> and the request's country to focus on high-confidence attacks from automated sources. This layered approach significantly reduces false positives compared to using any single signal alone.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Enter the following expression in the editor:<br />
<code>(cf.llm.prompt.injection_score lt 25 and cf.bot_management.score lt 10 and ip.geoip.country ne &quot;US&quot;)</code></p>
</li>
<li>
<p><strong>Action</strong>: <em>Block</em></p>
</li>
</ul>
<p>The rule targets requests that are simultaneously:</p>
<ol>
<li>Likely prompt injection attempts (score below 25).</li>
<li>Coming from automated tooling, not a real browser (bot score below 10).</li>
<li>Originating from outside the US — adjust the country code to match where your users are.</li>
</ol>
<p>Any single signal might produce false positives on its own. Together, they identify a pattern strongly associated with automated prompt injection attacks.</p>
<h2 id="allow-financial-pii-only-from-your-internal-network">Allow financial PII only from your internal network</h2>
<p>A financial services application legitimately handles credit card and bank account numbers from internal agents, but should block those PII types from external users. This rule uses the request's <a href="/ruleset-engine/rules-language/fields/reference/ip.src.asnum/">autonomous system number (ASN)</a> to distinguish internal traffic from public traffic.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Enter the following expression in the editor:<br />
<code>(any(cf.llm.prompt.pii_categories[*] in {&quot;CREDIT_CARD&quot; &quot;BANK_ACCOUNT&quot;}) and ip.src.asnum ne 13335)</code></p>
<p>Replace <code>13335</code> with your organization's ASN.</p>
</li>
<li>
<p><strong>Action</strong>: <em>Block</em></p>
</li>
<li>
<p><strong>With response type</strong>: Custom JSON</p>
</li>
<li>
<p><strong>Response body</strong>:</p>
</li>
</ul>
<pre tabindex="0"><code class="language-txt">{ &quot;error&quot;: &quot;pii_blocked&quot;, &quot;message&quot;: &quot;Financial account information cannot be submitted from external networks. If you are an internal agent, connect to the corporate network and try again.&quot; }&#10;</code></pre>
<p>Internal agents on your corporate network (identified by ASN) can submit financial PII to the AI assistant as part of their workflow, while external users are blocked. You could further refine this by combining with <a href="/cloudflare-one/access-controls/policies/">Access</a> service tokens or <a href="/ssl/client-certificates/">mTLS</a> for stronger identity verification.</p>
<h2 id="handle-block-responses-in-your-application">Handle block responses in your application</h2>
<p>When a WAF rule blocks a request, Cloudflare sends the block response back to your application — not to the end user. Your application needs to handle that response and decide what to show. Without error handling, your users may see a raw HTML error page or a broken UI.</p>
<p>Here are two things you can do to keep the experience smooth.</p>
<h3 id="set-a-fallback-message">Set a fallback message</h3>
<p>Define a friendly default message that your application displays whenever it receives a non-successful response. This works regardless of how the block rule is configured — including the default Cloudflare block page, which returns HTML that would otherwise break a JSON-based chat UI.</p>
<pre tabindex="0"><code class="language-js">// Define a user-friendly fallback message. This is what the user will see&#10;// any time the request is blocked or something unexpected happens.&#10;const FALLBACK = &quot;Sorry, I can&#x27;t process that request. Please try rephrasing.&quot;;&#10;&#10;const resp = await fetch(&quot;/api/chat&quot;, {&#10;	method: &quot;POST&quot;,&#10;	headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;	body: JSON.stringify({ prompt: userMessage }),&#10;});&#10;&#10;// If the response is not 2xx, show the fallback instead of trying to parse&#10;// the body. This safely handles the default Cloudflare block page (which is&#10;// HTML) without breaking your UI.&#10;if (!resp.ok) {&#10;	await resp.text(); // consume the body so the connection is released&#10;	showError(FALLBACK);&#10;	return;&#10;}&#10;&#10;const data = await resp.json();&#10;showMessage(data.message);&#10;</code></pre>
<h3 id="display-custom-error-messages-from-the-waf">Display custom error messages from the WAF</h3>
<p>For more control, configure your block rules with a <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">custom JSON response</a> — for example, <code>{ &quot;message&quot;: &quot;That question is outside this assistant's scope.&quot; }</code>. Your application can then parse the response and show the custom message when available, falling back to the default when it is not.</p>
<pre tabindex="0"><code class="language-js">const FALLBACK = &quot;Sorry, I can&#x27;t process that request. Please try rephrasing.&quot;;&#10;&#10;const resp = await fetch(&quot;/api/chat&quot;, {&#10;	method: &quot;POST&quot;,&#10;	headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;	body: JSON.stringify({ prompt: userMessage }),&#10;});&#10;&#10;if (!resp.ok) {&#10;	// Check the content type to determine if the response contains a custom&#10;	// JSON error from your WAF rule, or something else (like the default&#10;	// Cloudflare HTML block page, or a DDoS / Bot Management challenge).&#10;	const ct = (resp.headers.get(&quot;content-type&quot;) || &quot;&quot;).toLowerCase();&#10;&#10;	if (ct.includes(&quot;application/json&quot;)) {&#10;		// The WAF returned your custom JSON response. Parse it and show the&#10;		// message you configured in the rule. Fall back to the default if the&#10;		// field is missing or empty.&#10;		const data = await resp.json();&#10;		showError(data.message || FALLBACK);&#10;	} else {&#10;		// The response is not JSON — most likely the default Cloudflare HTML&#10;		// block page. Discard the body and show the friendly fallback.&#10;		await resp.text();&#10;		showError(FALLBACK);&#10;	}&#10;	return;&#10;}&#10;&#10;const data = await resp.json();&#10;showMessage(data.message);&#10;</code></pre>
