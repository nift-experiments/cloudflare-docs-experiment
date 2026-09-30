---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/cdp/
  description: Create persistent browser sessions, manage tabs, and interact with browsers using Chrome DevTools Protocol (CDP) commands via the /devtools endpoints.
  full_title: Chrome DevTools Protocol (CDP) · Cloudflare Browser Run docs
  head_html: <title>Chrome DevTools Protocol (CDP) · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Create persistent browser sessions, manage tabs, and interact with browsers using Chrome DevTools Protocol (CDP) commands via the /devtools endpoints."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/cdp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/cdp/index.md"><meta property="og:title" content="Chrome DevTools Protocol (CDP) · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create persistent browser sessions, manage tabs, and interact with browsers using Chrome DevTools Protocol (CDP) commands via the /devtools endpoints."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/cdp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/cdp/#page","headline":"Chrome DevTools Protocol (CDP) \u00b7 Cloudflare Browser Run docs","description":"Create persistent browser sessions, manage tabs, and interact with browsers using Chrome DevTools Protocol (CDP) commands via the /devtools endpoints.","url":"https://developers.cloudflare.com/browser-run/cdp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/cdp/
  schema: 1
---
<p>The <code>/devtools</code> endpoints provide session management capabilities that follow the <a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol (CDP)</a>. These endpoints allow you to create persistent browser sessions, manage multiple tabs, and interact with browsers using CDP commands. This is useful for advanced automation, debugging, and remote browser control.</p>
<p>CDP endpoints can be accessed from any environment that supports WebSocket connections, including local development machines, external servers, and CI/CD pipelines. This means you can connect to Browser Run from Node.js scripts, Puppeteer, Playwright, or any CDP-compatible client.</p>
<p>Before you begin, <a href="/fundamentals/api/get-started/create-token/">create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</p>
<h2 id="what-is-cdp">What is CDP?</h2>
<p>The Chrome DevTools Protocol (CDP) is a remote debugging protocol that allows you to instrument, inspect, debug, and profile Chromium-based browsers. It is the same protocol used by Chrome DevTools to control and monitor the browser. Popular browser automation libraries like Puppeteer and Playwright provide high-level APIs over the Chrome DevTools Protocol, making it easier to automate common tasks.</p>
<h2 id="use-cases">Use cases</h2>
<p>The browser sessions endpoints enable you to:</p>
<ul>
<li><strong>Create and manage persistent browser sessions</strong> — Launch browser instances that remain active for extended periods</li>
<li><strong>Open, close, and list browser tabs (targets)</strong> — Manage multiple debuggable targets (pages, iframes, etc.) within a single browser instance</li>
<li><strong>Connect via WebSocket to send CDP commands</strong> — Automate browser actions programmatically</li>
<li><strong>View live browser sessions using Chrome DevTools UI</strong> — Debug and inspect remote browser sessions visually</li>
<li><strong>Integrate with existing CDP clients</strong> — Use standard CDP clients like Puppeteer or custom WebSocket implementations</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Once you acquire a browser session, you can interact with it in two ways:</p>
<h3 id="cdp-over-websocket">CDP over WebSocket</h3>
<p>Connect to the WebSocket endpoint <code>/devtools/browser</code> to acquire a session and send <a href="https://chromedevtools.github.io/devtools-protocol/">CDP commands</a> directly over the connection. This is the standard way to use CDP and works with any CDP client, including <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, and <a href="/browser-run/cdp/mcp-clients/">MCP clients</a>.</p>
<h3 id="http-api">HTTP API</h3>
<p>HTTP endpoints are also available to manage the browser lifecycle without using WebSockets. These follow the standard <a href="https://chromedevtools.github.io/devtools-protocol/#endpoints">CDP HTTP endpoints</a>:</p>
<ol>
<li><strong>Create session</strong> — <code>POST /devtools/browser</code></li>
<li><strong>List tabs</strong> — <code>GET /devtools/browser/{session_id}/json/list</code></li>
<li><strong>Create tab</strong> — <code>PUT /devtools/browser/{session_id}/json/new</code></li>
<li><strong>Close tab</strong> — <code>DELETE /devtools/browser/{session_id}/json/close/{target_id}</code></li>
<li><strong>Close session</strong> — <code>DELETE /devtools/browser/{session_id}</code></li>
</ol>
<p>Check the <a href="/api/resources/browser_rendering/">API reference</a> for the full list of endpoints.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
