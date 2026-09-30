---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/guides/browser-terminals/
  description: Connect browser-based terminals to sandbox shells using xterm.js or raw WebSockets.
  full_title: Browser terminals · Cloudflare Sandbox SDK docs
  head_html: <title>Browser terminals · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect browser-based terminals to sandbox shells using xterm.js or raw WebSockets."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/guides/browser-terminals/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/guides/browser-terminals/index.md"><meta property="og:title" content="Browser terminals · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect browser-based terminals to sandbox shells using xterm.js or raw WebSockets."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/guides/browser-terminals/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/guides/browser-terminals/#page","headline":"Browser terminals \u00b7 Cloudflare Sandbox SDK docs","description":"Connect browser-based terminals to sandbox shells using xterm.js or raw WebSockets.","url":"https://developers.cloudflare.com/sandbox/guides/browser-terminals/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/guides/browser-terminals/
  schema: 1
---
<p>This guide shows you how to connect a browser-based terminal to a sandbox shell. You can use the <code>SandboxAddon</code> with xterm.js, or connect directly over WebSockets.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13484.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need an existing Cloudflare Worker with a sandbox binding. Refer to <a href="/sandbox/get-started/">Getting started</a> if you do not have one.</p>
<p>Install the terminal dependencies in your frontend project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div></div>
<p>If you are not using xterm.js, you only need <code>@cloudflare/sandbox</code> for types.</p>
<h2 id="handle-websocket-upgrades-in-the-worker">Handle WebSocket upgrades in the Worker</h2>
<p>Add a route that proxies WebSocket connections to the sandbox terminal. The example below supports both the default session and named sessions via a query parameter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13485.md")
</div>
<h2 id="connect-with-xterm-js-and-sandboxaddon">Connect with xterm.js and SandboxAddon</h2>
<p>Create the terminal in your browser code and attach the <code>SandboxAddon</code>. The addon manages the WebSocket connection, automatic reconnection, and resize forwarding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13486.md")
</div>
<p>For the full addon API, refer to the <a href="/sandbox/api/terminal/">Terminal API reference</a>.</p>
<h2 id="connect-without-xterm-js">Connect without xterm.js</h2>
<p>If you are building a custom terminal UI or running in an environment without xterm.js, connect directly over WebSockets. The protocol uses binary frames for terminal data and JSON text frames for control messages.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13487.md")
</div>
<p>Key protocol details:</p>
<ul>
<li>Set <code>binaryType</code> to <code>arraybuffer</code> before connecting.</li>
<li>Buffered output from a previous connection arrives as binary frames before the <code>ready</code> message.</li>
<li>Send keystrokes as binary (UTF-8). Send control messages (<code>resize</code>) as JSON text.</li>
<li>The PTY stays alive when a client disconnects. Reconnecting replays buffered output.</li>
</ul>
<p>For the full protocol specification, refer to the <a href="/sandbox/api/terminal/#websocket-protocol">WebSocket protocol section</a> in the API reference.</p>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Always use FitAddon</strong> — Without it, terminal dimensions do not match the container and text wraps incorrectly.</li>
<li><strong>Handle resize events</strong> — Call <code>fitAddon.fit()</code> on window resize so the terminal and PTY stay in sync.</li>
<li><strong>Clean up on unmount</strong> — Call <code>addon.disconnect()</code> when removing the terminal from the page.</li>
<li><strong>Scope terminals to a user sandbox</strong> — Use sessions for multiple terminal contexts in the same workspace. Use separate sandboxes for separate users.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/terminal/">Terminal API reference</a> — Method signatures, addon API, and WebSocket protocol</li>
<li><a href="/sandbox/concepts/terminal/">Terminal connections</a> — How terminal connections work</li>
<li><a href="/sandbox/concepts/sessions/">Session management</a> — How sessions work</li>
</ul>
