---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/cdp/session-management/
  description: Manage browser sessions and tabs using HTTP endpoints, including creating sessions, listing targets, and opening the Chrome DevTools UI.
  full_title: Session management (HTTP) · Cloudflare Browser Run docs
  head_html: <title>Session management (HTTP) · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage browser sessions and tabs using HTTP endpoints, including creating sessions, listing targets, and opening the Chrome DevTools UI."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/cdp/session-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/cdp/session-management/index.md"><meta property="og:title" content="Session management (HTTP) · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage browser sessions and tabs using HTTP endpoints, including creating sessions, listing targets, and opening the Chrome DevTools UI."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/cdp/session-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/cdp/session-management/#page","headline":"Session management (HTTP) \u00b7 Cloudflare Browser Run docs","description":"Manage browser sessions and tabs using HTTP endpoints, including creating sessions, listing targets, and opening the Chrome DevTools UI.","url":"https://developers.cloudflare.com/browser-run/cdp/session-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/cdp/session-management/
  schema: 1
---
<p>Use the HTTP API to manage browser sessions and tabs without using WebSocket connections. This is useful for session lifecycle operations like creating sessions, listing tabs, and cleaning up resources.</p>
<p>Before you begin, <a href="/fundamentals/api/get-started/create-token/">create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</p>
<p>The <a href="/api/resources/browser_rendering/">API reference</a> documents all session management endpoints under <code>/devtools</code>.</p>
<h2 id="step-1-acquire-a-browser-session">Step 1: Acquire a browser session</h2>
<p>Create a new browser session using the <code>POST /devtools/browser</code> endpoint. The session will remain active for the specified keep-alive time (in this example, 10 minutes).</p>
<pre tabindex="0"><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-rendering/devtools/browser</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;sessionId&quot;: &quot;1909cef7-23e8-4394-bc31-27404bf4348f&quot;,&#10;	&quot;webSocketDebuggerUrl&quot;: &quot;wss://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f&quot;&#10;}&#10;</code></pre>
<p>Save the <code>sessionId</code> from the response. You will use it in subsequent requests.</p>
<h2 id="step-2-create-a-tab-with-a-specific-url">Step 2: Create a tab with a specific URL</h2>
<p>Open a new tab in your browser session and navigate to a specific URL using the <code>PUT /devtools/browser/{session_id}/json/new</code> endpoint.</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-rendering/devtools/browser/SESSION_ID/json/new</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;8E598E996530FB09E46A22B8B7754F7F&quot;,&#10;	&quot;type&quot;: &quot;page&quot;,&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;title&quot;: &quot;Example Domain&quot;,&#10;	&quot;description&quot;: &quot;&quot;,&#10;	&quot;devtoolsFrontendUrl&quot;: &quot;https://live.browser.run/ui/view?wss=live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=...&quot;,&#10;	&quot;webSocketDebuggerUrl&quot;: &quot;wss://live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=...&quot;&#10;}&#10;</code></pre>
<h2 id="step-3-list-all-targets">Step 3: List all targets</h2>
<p>List all targets (tabs) in your session to verify the tab was created and get the <code>devtoolsFrontendUrl</code>.</p>
<pre tabindex="0"><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-rendering/devtools/browser/SESSION_ID/json/list</code></pre>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;8E598E996530FB09E46A22B8B7754F7F&quot;,&#10;		&quot;type&quot;: &quot;page&quot;,&#10;		&quot;url&quot;: &quot;https://example.com&quot;,&#10;		&quot;title&quot;: &quot;Example Domain&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;devtoolsFrontendUrl&quot;: &quot;https://live.browser.run/ui/view?wss=live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=...&quot;,&#10;		&quot;webSocketDebuggerUrl&quot;: &quot;wss://live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=...&quot;&#10;	}&#10;]&#10;</code></pre>
<h2 id="step-4-open-the-devtools-ui">Step 4: Open the DevTools UI</h2>
<p>Copy the <code>devtoolsFrontendUrl</code> from the response and open it in Chrome. This URL provides direct access to the Chrome DevTools UI connected to your remote browser session.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="url-validity">URL validity</h3>
@markup("md", "content/.markup/bodies/3721.md")
</aside>
<p>Once opened, the DevTools UI will load and you can:</p>
<ul>
<li>Inspect the DOM and CSS</li>
<li>Debug JavaScript with breakpoints</li>
<li>Monitor network requests</li>
<li>View console messages</li>
<li>Execute JavaScript in the console</li>
<li>Navigate to different URLs</li>
</ul>
<h2 id="step-5-clean-up">Step 5: Clean up</h2>
<p>When you are done, close the browser session to release resources.</p>
<pre tabindex="0"><code class="language-bash">curl --request DELETE --url https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-rendering/devtools/browser/SESSION_ID</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;status&quot;: &quot;closing&quot;&#10;}&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
