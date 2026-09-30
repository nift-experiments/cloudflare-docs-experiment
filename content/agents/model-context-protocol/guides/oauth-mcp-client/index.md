---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/
  description: Implement OAuth authentication flows in Cloudflare Agents to connect to protected MCP servers.
  full_title: Handle OAuth with MCP servers · Cloudflare Agents docs
  head_html: <title>Handle OAuth with MCP servers · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Implement OAuth authentication flows in Cloudflare Agents to connect to protected MCP servers."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/index.md"><meta property="og:title" content="Handle OAuth with MCP servers · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Implement OAuth authentication flows in Cloudflare Agents to connect to protected MCP servers."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/#page","headline":"Handle OAuth with MCP servers \u00b7 Cloudflare Agents docs","description":"Implement OAuth authentication flows in Cloudflare Agents to connect to protected MCP servers.","url":"https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/guides/oauth-mcp-client/
  schema: 1
---
<p>When connecting to OAuth-protected MCP servers (like Slack or Notion), your users need to authenticate before your Agent can access their data. This guide covers implementing OAuth flows for seamless authorization.</p>
<h2 id="how-it-works">How it works</h2>
<ol>
<li>Call <code>addMcpServer()</code> with the server URL</li>
<li>If OAuth is required, an <code>authUrl</code> is returned instead of connecting immediately</li>
<li>Present the <code>authUrl</code> to your user (redirect, popup, or link)</li>
<li>User authenticates on the provider's site</li>
<li>Provider redirects back to your Agent's callback URL</li>
<li>Your Agent completes the connection automatically</li>
</ol>
<p>The MCP client uses a built-in <code>DurableObjectOAuthClientProvider</code> to manage OAuth state securely — storing a nonce and server ID, validating on callback, and cleaning up after use or expiration.</p>
<h2 id="initiate-oauth">Initiate OAuth</h2>
<p>When connecting to an OAuth-protected server, check if <code>authUrl</code> is returned. If present, redirect your user to complete authorization:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2215.md")
</div>
<h3 id="alternative-approaches">Alternative approaches</h3>
<p>Instead of an automatic redirect, you can present the <code>authUrl</code> to your user as a:</p>
<ul>
<li><strong>Popup window</strong>: <code>window.open(authUrl, '_blank', 'width=600,height=700')</code> for dashboard-style apps</li>
<li><strong>Clickable link</strong>: Display as a button or link for multi-step flows</li>
<li><strong>Deep link</strong>: Use custom URL schemes for mobile apps</li>
</ul>
<h2 id="configure-callback-behavior">Configure callback behavior</h2>
<p>After OAuth completes, the provider redirects back to your Agent's callback URL. By default, successful authentication redirects to your application origin, while failed authentication displays an HTML error page with the error message.</p>
<h3 id="redirect-to-your-application">Redirect to your application</h3>
<p>Redirect users back to your application after OAuth completes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2216.md")
</div>
<p>Users return to <code>/dashboard</code> on success or <code>/auth-error?error=&lt;message&gt;</code> on failure.</p>
<h3 id="close-popup-window">Close popup window</h3>
<p>If you opened OAuth in a popup, close it automatically when complete:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2217.md")
</div>
<p>Your main application can detect the popup closing and refresh the connection status. If OAuth fails, the connection state becomes <code>&quot;failed&quot;</code> and the error message is stored in <code>server.error</code> for display in your UI.</p>
<h2 id="monitor-connection-status">Monitor connection status</h2>
<h3 id="react-applications">React applications</h3>
<p>Use the <code>useAgent</code> hook for real-time updates via WebSocket:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2218.md")
</div>
<p>The <code>onMcpUpdate</code> callback fires automatically when MCP state changes — no polling needed.</p>
<h3 id="other-frameworks">Other frameworks</h3>
<p>Poll the connection status via an endpoint:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2219.md")
</div>
<p>Connection states flow: <code>authenticating</code> (needs OAuth) → <code>connecting</code> (completing setup) → <code>ready</code> (available for use)</p>
<h2 id="handle-failures">Handle failures</h2>
<p>When OAuth fails, the connection state becomes <code>&quot;failed&quot;</code> and the error message is stored in the <code>server.error</code> field. Display this error in your UI and allow users to retry:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2220.md")
</div>
<p>Common failure reasons:</p>
<ul>
<li><strong>User canceled</strong>: Closed OAuth window before completing authorization</li>
<li><strong>Invalid credentials</strong>: Provider credentials were incorrect</li>
<li><strong>Permission denied</strong>: User lacks required permissions</li>
<li><strong>Expired session</strong>: OAuth session timed out</li>
</ul>
<p>Failed connections remain in state until removed with <code>removeMcpServer(serverId)</code>. The error message is automatically escaped to prevent XSS attacks, so it is safe to display directly in your UI.</p>
<h2 id="complete-example">Complete example</h2>
<p>This example demonstrates a complete OAuth integration with Cloudflare Observability. Users connect, authorize in a popup window, and the connection becomes available. Errors are automatically stored in the connection state for display in your UI.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2221.md")
</div>
<h2 id="related">Related</h2>
<div class="nb-card nb-link-card"><h3 id="card-connect-to-an-mcp-server-agents-model-context-protocol-guides-connect-mcp-client"><a href="/agents/model-context-protocol/guides/connect-mcp-client/">Connect to an MCP server</a></h3><p>Get started without OAuth.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-mcp-client-api-agents-model-context-protocol-apis-client-api"><a href="/agents/model-context-protocol/apis/client-api/">MCP Client API</a></h3><p>Complete API documentation for MCP clients.</p></div>
