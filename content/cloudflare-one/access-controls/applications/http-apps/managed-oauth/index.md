---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/
  description: Allow non-browser clients to authenticate with Access-protected applications using a standard OAuth 2.0 flow.
  full_title: Managed OAuth · Cloudflare One docs
  head_html: <title>Managed OAuth · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Allow non-browser clients to authenticate with Access-protected applications using a standard OAuth 2.0 flow."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/index.md"><meta property="og:title" content="Managed OAuth · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Allow non-browser clients to authenticate with Access-protected applications using a standard OAuth 2.0 flow."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Authentication,REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#page","headline":"Managed OAuth \u00b7 Cloudflare One docs","description":"Allow non-browser clients to authenticate with Access-protected applications using a standard OAuth 2.0 flow.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication","REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/managed-oauth/
  schema: 1
---
<p>When you protect an application with Cloudflare Access, by default non-browser clients — such as CLIs, AI agents, SDKs, and scripts — cannot complete the browser-based login redirect. They receive a <code>302</code> redirect with no usable token or authorization endpoint.</p>
<p>Managed OAuth solves this by turning Access into a standard OAuth 2.0 authorization server for your application. Access enforces the same policies as a browser login, and your origin sees no difference.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4825.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access application</a>, <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/">MCP server application</a>, or <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a></li>
<li>An OAuth client that supports <a href="https://datatracker.ietf.org/doc/html/rfc8707">RFC 8707</a></li>
</ul>
<h2 id="enable-managed-oauth-on-a-self-hosted-application">Enable managed OAuth on a self-hosted application</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4828.md")
</div></div>
<p>To test, open an RFC 8707-compliant OAuth client and make a request to your application. The client should open a browser window prompting you to log in to Access. Refer to the <a href="#authorization-flow">Authorization flow</a> section for more details.</p>
<h2 id="enable-managed-oauth-on-an-mcp-server-application">Enable managed OAuth on an MCP server application</h2>
<p>Managed OAuth is available on <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/">MCP server applications</a> and allows MCP clients to authenticate users through Access using a standard OAuth 2.0 flow. Use this flow for MCP servers served through Cloudflare in the same account as your Zero Trust organization. The MCP server must validate the Access JWT sent in the <code>Cf-Access-Jwt-Assertion</code> header.</p>
<p>Do not enable Managed OAuth for third-party MCP server code that already handles its own OAuth flow and cannot validate Access JWTs.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4831.md")
</div></div>
<p>To test, open an MCP client and connect to the protected MCP server. The client should open a browser window prompting you to log in to Access. Refer to the <a href="#authorization-flow">Authorization flow</a> section for more details.</p>
<h2 id="enable-managed-oauth-on-an-mcp-server-portal">Enable managed OAuth on an MCP server portal</h2>
<p>Managed OAuth is available on <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> and is the mechanism that allows MCP clients to authenticate users through the portal without a browser cookie flow.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4834.md")
</div></div>
<p>To test, open an MCP client and <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-to-a-portal">connect to the MCP portal</a>. The client should open a browser window prompting you to log in to Access. Refer to the <a href="#authorization-flow">Authorization flow</a> section for more details.</p>
<h2 id="managed-oauth-settings">Managed OAuth settings</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4837.md")
</div></div>
<h2 id="authorization-flow">Authorization flow</h2>
<p>When managed OAuth is enabled, Access returns a <code>401</code> response instead of a <code>302</code> redirect to non-browser clients. The <code>401</code> includes a <code>WWW-Authenticate</code> header that points the client to Access's OAuth discovery metadata.</p>
<p>The authorization flow proceeds as follows:</p>
<ol>
<li>The client fetches the OAuth authorization server metadata from the <code>/.well-known/</code> endpoint:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-app-domain&gt;/.well-known/oauth-authorization-server&#10;</code></pre>
<p>This endpoint conforms to <a href="https://datatracker.ietf.org/doc/html/rfc8414">RFC 8414</a> and <a href="https://datatracker.ietf.org/doc/html/rfc9728">RFC 9728</a> and returns the authorization and token endpoint URLs for the application.</p>
<ol start="2">
<li>
<p>The client initiates an authorization code flow. It opens the user's browser to the Access authorization endpoint, where the user logs in to their IdP as usual.</p>
</li>
<li>
<p>Access issues an OAuth access token to the client. The client uses this token in subsequent requests to the protected application.</p>
</li>
</ol>
<h3 id="token-format">Token format</h3>
<p>Managed OAuth issues <strong>opaque</strong> access tokens (for example, <code>oauth:CvNoo...</code>), not JSON Web Tokens (JWTs). This is by design — the OAuth flow gives clients the ability to make requests on a user's behalf without exposing identity information to the client.</p>
<p>When a client presents an opaque token to your application, Cloudflare resolves the token into the user's identity on the backend and forwards a signed assertion to your origin. From your origin's perspective, the request looks the same as a browser-authenticated request.</p>
<p>Because the token is opaque, the client cannot decode it or forward it directly as a JWT to other applications. To make authenticated requests to downstream Access applications, use the <a href="/cloudflare-one/access-controls/applications/linked-app-token/">Linked App Token</a> pattern — your origin reads the <code>Cf-Access-Jwt-Assertion</code> header and forwards it to downstream apps as <code>Cf-Access-Token</code>.</p>
<h3 id="multi-domain-applications">Multi-domain applications</h3>
<p>If your Access application is configured with <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#multi-domain-applications">multiple domains</a>, an OAuth token obtained through any one domain is valid for all domains in the same application. The user authenticates once and can use the same token to access all domains without additional prompts.</p>
<p>This is useful when you have multiple internal services that share a common trust boundary. Instead of configuring separate Access applications with <a href="/cloudflare-one/access-controls/applications/linked-app-token/">Linked App Token</a> policies, you can add all domains to a single application and authenticate once via Managed OAuth.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4823.md")
</aside>
<h2 id="managed-oauth-vs-service-tokens">Managed OAuth vs service tokens</h2>
<p>Both managed OAuth and <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service tokens</a> allow non-browser clients to authenticate with Access-protected applications, but they serve different use cases:</p>
<table>
<thead>
<tr>
<th></th>
<th>Managed OAuth</th>
<th>Service tokens</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Authentication model</strong></td>
<td>User-based — the end user logs in through their identity provider</td>
<td>Machine-based — a shared secret authenticates the service itself</td>
</tr>
<tr>
<td><strong>Best for</strong></td>
<td>Interactive CLI tools, AI agents, SDKs where a human initiates the request</td>
<td>Fully automated systems, cron jobs, CI/CD pipelines, server-to-server communication</td>
</tr>
<tr>
<td><strong>User identity</strong></td>
<td>Access knows which user made the request</td>
<td>No user identity — requests are attributed to the service token</td>
</tr>
<tr>
<td><strong>Policy enforcement</strong></td>
<td>Can use identity-based policies (for example, require specific groups or emails)</td>
<td>Requires a <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth</a> policy action</td>
</tr>
<tr>
<td><strong>Credential management</strong></td>
<td>No shared secrets to distribute — users authenticate with their own credentials</td>
<td>Requires distributing and rotating Client ID and Client Secret</td>
</tr>
</tbody>
</table>
<p>Use managed OAuth when you want non-browser clients to authenticate users the same way a browser would — the user logs in once, and the client receives an OAuth token to make requests on their behalf.</p>
<p>Use service tokens when no human is involved and you need a machine identity to access your application programmatically.</p>
