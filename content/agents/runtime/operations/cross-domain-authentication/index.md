---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/
  description: Authenticate WebSocket connections to Cloudflare Agents across domains using signed tokens.
  full_title: Cross-domain authentication · Cloudflare Agents docs
  head_html: <title>Cross-domain authentication · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Authenticate WebSocket connections to Cloudflare Agents across domains using signed tokens."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/index.md"><meta property="og:title" content="Cross-domain authentication · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Authenticate WebSocket connections to Cloudflare Agents across domains using signed tokens."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/#page","headline":"Cross-domain authentication \u00b7 Cloudflare Agents docs","description":"Authenticate WebSocket connections to Cloudflare Agents across domains using signed tokens.","url":"https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/operations/cross-domain-authentication/
  schema: 1
---
<p>When your Agents are deployed, to keep things secure, send a token from the client, then verify it on the server. This guide covers authentication patterns for WebSocket connections to agents.</p>
<h2 id="websocket-authentication">WebSocket authentication</h2>
<p>WebSockets are not HTTP, so the handshake is limited when making cross-domain connections.</p>
<p>You cannot send:</p>
<ul>
<li>Custom headers during the upgrade</li>
<li><code>Authorization: Bearer ...</code> on connect</li>
</ul>
<p>You can:</p>
<ul>
<li>Put a signed, short-lived token in the connection URL as query parameters</li>
<li>Verify the token in your server's connect path</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2300.md")
</aside>
<h3 id="same-origin">Same origin</h3>
<p>If the client and server share the origin, the browser will send cookies during the WebSocket handshake. Session-based auth can work here. Prefer HTTP-only cookies.</p>
<h3 id="cross-origin">Cross origin</h3>
<p>Cross-origin cookie behavior depends on the cookie's domain and <code>SameSite</code> attributes, whether the two origins are same-site, and browser third-party cookie policy. If you cannot rely on a cookie, pass a short-lived credential in the URL query and verify it on the server.</p>
<h2 id="usage-examples">Usage examples</h2>
<h3 id="static-authentication">Static authentication</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2301.md")
</div>
<h3 id="async-authentication">Async authentication</h3>
<p>Build query values right before connect. Use Suspense for async setup.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2302.md")
</div>
<h3 id="jwt-refresh-pattern">JWT refresh pattern</h3>
<p><code>useAgent</code> resolves an async query before connecting and reevaluates it when reconnecting. Return a fresh, short-lived application token each time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2303.md")
</div>
<h2 id="cross-domain-authentication">Cross-domain authentication</h2>
<p>Pass credentials in the URL when connecting to another host, then verify on the server.</p>
<h3 id="static-cross-domain-auth">Static cross-domain auth</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2304.md")
</div>
<h3 id="async-cross-domain-auth">Async cross-domain auth</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2305.md")
</div>
<h2 id="server-side-verification">Server-side verification</h2>
<p>On the server side, verify the token in the <code>onConnect</code> handler:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2306.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ol>
<li>
<p><strong>Use short-lived tokens</strong> - Tokens in URLs may be logged. Keep expiration times short (minutes, not hours).</p>
</li>
<li>
<p><strong>Scope tokens appropriately</strong> - Include the agent name or instance in the token claims to prevent token reuse across agents.</p>
</li>
<li>
<p><strong>Validate on every connection</strong> - Always verify tokens in <code>onConnect</code>, not just once.</p>
</li>
<li>
<p><strong>Use HTTPS</strong> - Always use secure WebSocket connections (<code>wss://</code>) in production.</p>
</li>
<li>
<p><strong>Rotate secrets</strong> - Regularly rotate your JWT signing keys or token secrets.</p>
</li>
<li>
<p><strong>Log authentication failures</strong> - Track failed authentication attempts for security monitoring.</p>
</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-routing-agents-runtime-communication-routing"><a href="/agents/runtime/communication/routing/">Routing</a></h3><p>Routing and authentication hooks.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-websockets-agents-runtime-communication-websockets"><a href="/agents/runtime/communication/websockets/">WebSockets</a></h3><p>Real-time bidirectional communication.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-github-oauth-agent-example-https-github-com-cloudflare-agents-tree-main-examples-auth-agent"><a href="https://github.com/cloudflare/agents/tree/main/examples/auth-agent">GitHub OAuth agent example</a></h3><p>Protect an app built with Agents using GitHub OAuth, HTTP-only cookies, and server-owned Durable Object routing.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
