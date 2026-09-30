---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/features/human-in-the-loop/
  description: Temporarily hand off browser control to a human operator for authentication, sensitive actions, or tasks that are difficult to fully automate.
  full_title: Human in the Loop · Cloudflare Browser Run docs
  head_html: <title>Human in the Loop · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Temporarily hand off browser control to a human operator for authentication, sensitive actions, or tasks that are difficult to fully automate."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/features/human-in-the-loop/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/features/human-in-the-loop/index.md"><meta property="og:title" content="Human in the Loop · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Temporarily hand off browser control to a human operator for authentication, sensitive actions, or tasks that are difficult to fully automate."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/features/human-in-the-loop/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/features/human-in-the-loop/#page","headline":"Human in the Loop \u00b7 Cloudflare Browser Run docs","description":"Temporarily hand off browser control to a human operator for authentication, sensitive actions, or tasks that are difficult to fully automate.","url":"https://developers.cloudflare.com/browser-run/features/human-in-the-loop/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/features/human-in-the-loop/
  schema: 1
---
<p>Some browser automation workflows require manual intervention. A login page may need multi-factor authentication, a form may require sensitive credentials you do not want to pass to an automation script, or a task may be too complex to fully automate. Human in the Loop lets a human step into a live browser session through <a href="/browser-run/features/live-view/">Live View</a> to handle what automation cannot, then hand control back to the script.</p>
<h2 id="use-cases">Use cases</h2>
<ul>
<li><strong>Authentication flows</strong>: Login pages with MFA, SSO, or CAPTCHA that cannot be bypassed programmatically</li>
<li><strong>Sensitive data entry</strong>: Forms requiring credentials or personal information you do not want to pass to an automation script</li>
<li><strong>Complex interactions</strong>: One-off tasks that are too difficult or not worth fully automating, such as configuring a dashboard or approving a workflow</li>
<li><strong>Verification steps</strong>: Confirming an order, reviewing generated content, or approving an action before the script proceeds</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Human in the Loop works with any <a href="/browser-run/#integration-methods">Browser Session</a> and provides two approaches for human intervention:</p>
<h3 id="structured-handoff-recommended">Structured handoff (recommended)</h3>
<p>Your script uses Cloudflare CDP commands to formally request human intervention and wait for completion:</p>
<ol>
<li>Your automation script encounters a scenario requiring human input.</li>
<li>The script subscribes to the <code>Cloudflare.handoffComplete</code> event.</li>
<li>The script sends <code>Cloudflare.getLiveView</code> with mode: <code>tab</code> and shares the returned URL with the human operator.</li>
<li>The script sends the <code>Cloudflare.handoff</code> CDP command with instructions for the human operator, then waits for <code>Cloudflare.handoffComplete</code>.</li>
<li>The operator opens the Live View (/browser-run/features/live-view/) URL, completes the required actions, and selects &quot;Done&quot; or &quot;Failed&quot;.</li>
<li><code>Cloudflare.handoffComplete</code> fires when the human marks the handoff as complete or the handoff times out.</li>
<li>The automation resumes with knowledge of whether the intervention succeeded.</li>
</ol>
<p>Refer to <a href="#example-structured-handoff">Example: structured handoff</a> for a complete code sample.</p>
<h3 id="manual-detection">Manual detection</h3>
<p>For simpler use cases, you can manually manage the handoff:</p>
<ol>
<li>Your automation script goes to a page that needs human input.</li>
<li>The script retrieves the <a href="/browser-run/features/live-view/">Live View</a> URL from the session's target list and shares it with a human operator.</li>
<li>The human operator opens the Live View URL and completes the required action.</li>
<li>The automation script detects completion by polling for page elements or waiting for navigation events.</li>
</ol>
<p>Refer to <a href="#example-manual-detection">Example: manual detection</a> for a complete code sample.</p>
<h2 id="cloudflare-cdp-commands">Cloudflare CDP commands</h2>
<p>Browser Run extends the standard <a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol (CDP)</a> with Cloudflare-specific commands under the <code>Cloudflare.*</code> namespace. These commands are only available when connected to a Browser Run session and provide capabilities that do not exist in the standard CDP specification, such as requesting human intervention, generating <a href="/browser-run/features/live-view/">Live View</a> URLs, and tracking handoff state.</p>
<p>You send these commands through a CDP session the same way you would send any standard CDP command. For full parameter and return type details, refer to the <a href="/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/protocol/">protocol reference</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="typescript-types">TypeScript types</h3>
@markup("md", "content/.markup/bodies/3704.md")
</aside>
<h3 id="cloudflare-handoff"><code>Cloudflare.handoff</code></h3>
<p>Requests human intervention for the current page. The target is automatically resolved from the CDP session.</p>
<pre tabindex="0"><code class="language-js">const cdp = await page.createCDPSession();&#10;const { handoffId } = await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	// targetId will automatically be resolved from the CDP session&#10;	instructions: &quot;Please log in&quot;,&#10;	timeout: 1800000, // optional, max 30 minutes, if undefined handoff will have no timeout&#10;});&#10;</code></pre>
<p>To request a handoff for a specific target when your browser has multiple pages:</p>
<pre tabindex="0"><code class="language-js">// Get all targets&#10;const { targetInfos } = await cdp.send(&quot;Target.getTargets&quot;);&#10;&#10;// Find a specific target (for example, a page with a specific URL)&#10;const target = targetInfos.find(&#10;	(t) =&gt; t.type === &quot;page&quot; &amp;&amp; t.url.includes(&quot;example.com&quot;),&#10;);&#10;&#10;if (!target) {&#10;	throw new Error(&quot;Target not found&quot;);&#10;}&#10;&#10;// Request handoff for the selected target&#10;const { handoffId } = await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	targetId: target.targetId,&#10;	instructions: &quot;Please complete the CAPTCHA on this page&quot;,&#10;});&#10;</code></pre>
<h3 id="cloudflare-handoffcomplete-event"><code>Cloudflare.handoffComplete</code> event</h3>
<p>Emitted when human intervention completes or times out. Listen for this event to resume automation once the human is done.</p>
<pre tabindex="0"><code class="language-js">cdp.once(&quot;Cloudflare.handoffComplete&quot;, (result) =&gt; {&#10;	if (result.success) {&#10;		console.log(&quot;Handoff completed successfully&quot;);&#10;	} else {&#10;		console.log(`Handoff failed: ${result.reason}`);&#10;	}&#10;});&#10;</code></pre>
<h3 id="cloudflare-gethandoffstate"><code>Cloudflare.getHandoffState</code></h3>
<p>Checks whether a handoff is currently active for the current page.</p>
<pre tabindex="0"><code class="language-js">const state = await cdp.send(&quot;Cloudflare.getHandoffState&quot;, {&#10;	targetId, // optional, defaults to the current page&#10;});&#10;if (state.active) {&#10;	console.log(&#10;		`Handoff ${state.handoffId} has been active for ${state.durationMs}ms`,&#10;	);&#10;}&#10;</code></pre>
<h3 id="cloudflare-getliveview"><code>Cloudflare.getLiveView</code></h3>
<p>Generates a <a href="/browser-run/features/live-view/">Live View</a> URL for the browser session. Use this alongside <code>Cloudflare.handoff</code> to give the human operator access to the live browser.</p>
<pre tabindex="0"><code class="language-js">const { devtoolsFrontendUrl } = await cdp.send(&quot;Cloudflare.getLiveView&quot;, {&#10;	targetId, // optional, defaults to the current page&#10;	mode: &quot;tab&quot;, // optional, one of &quot;tab&quot;, &quot;full&quot;, or &quot;devtools&quot; (default)&#10;	expiresInMs: 300000, // optional, default 5 minutes, max 1 hour&#10;});&#10;console.log(`Live View URL: ${devtoolsFrontendUrl}`);&#10;</code></pre>
<h2 id="example-structured-handoff">Example: structured handoff</h2>
<p>This example demonstrates the structured handoff flow. The script requests human intervention using the Cloudflare CDP commands and waits for a completion event before resuming:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="browser-driver"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3707.md")
</div></div>
<h2 id="example-manual-detection">Example: manual detection</h2>
<p>This example uses the manual approach of sharing a Live View URL and polling for completion:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="browser-driver"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3710.md")
</div></div>
<h2 id="best-practices">Best practices</h2>
<h3 id="provide-clear-instructions">Provide clear instructions</h3>
<p>Give human operators specific, actionable guidance:</p>
<pre tabindex="0"><code class="language-js">// Good: specific and actionable&#10;await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	instructions:&#10;		&quot;Review the items in the cart and if approved for checkout, click &#x27;Done&#x27;. Otherwise, click &#x27;Failed&#x27; and provide a reason.&quot;,&#10;});&#10;</code></pre>
<h3 id="set-appropriate-timeouts">Set appropriate timeouts</h3>
<p>Match timeout duration to task complexity:</p>
<pre tabindex="0"><code class="language-js">// Quick tasks — 2-3 minutes&#10;await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	instructions: &quot;Click the &#x27;I agree&#x27; checkbox and submit&quot;,&#10;	timeout: 120000,&#10;});&#10;&#10;// Complex tasks - 10-15 minutes&#10;await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	instructions: &quot;Complete the multi-page application form with test data&quot;,&#10;	timeout: 900000,&#10;});&#10;</code></pre>
<h3 id="monitor-handoff-state">Monitor handoff state</h3>
<p>Check handoff status when needed:</p>
<pre tabindex="0"><code class="language-js">// Check if a handoff is already active before requesting a new one&#10;const currentState = await cdp.send(&quot;Cloudflare.getHandoffState&quot;);&#10;if (currentState.active) {&#10;	console.log(`Handoff already active: ${currentState.handoffId}`);&#10;	// Wait for current handoff or handle appropriately&#10;} else {&#10;	// Safe to start new handoff&#10;	await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;		/* ... */&#10;	});&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bot-detection">Bot detection</h3>
@markup("md", "content/.markup/bodies/3703.md")
</aside>
