---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/
  description: Secure MCP servers with Cloudflare Access.
  full_title: Secure MCP servers · Cloudflare One docs
  head_html: <title>Secure MCP servers · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Secure MCP servers with Cloudflare Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/index.md"><meta property="og:title" content="Secure MCP servers · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Secure MCP servers with Cloudflare Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One,Access"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/#page","headline":"Secure MCP servers \u00b7 Cloudflare One docs","description":"Secure MCP servers with Cloudflare Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/ai-controls/secure-mcp-servers/
  schema: 1
---
<p>You can secure <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP) servers</a> with Cloudflare Access. Choose an approach based on who manages the MCP server code and hostname:</p>
<table>
<thead>
<tr>
<th>Approach</th>
<th>Best for</th>
<th>Auth handled by</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#customer-managed-third-party-mcp-server">Customer-managed third-party MCP server</a></td>
<td>Third-party MCP server code running on a hostname you control in Cloudflare</td>
<td>The third-party MCP server</td>
</tr>
<tr>
<td><a href="#saas-managed-third-party-mcp-server">SaaS-managed third-party MCP server</a></td>
<td>Third-party MCP servers hosted by the provider that support customer-provided OAuth or OIDC identity settings</td>
<td>Third-party MCP server, with Access as the OIDC provider</td>
</tr>
</tbody>
</table>
<h2 id="customer-managed-third-party-mcp-server">Customer-managed third-party MCP server</h2>
<p>Use this setup when the MCP server runs on a hostname you control in Cloudflare, but the server code is managed by a third party and already handles its own OAuth flow. In this setup, do not enable Access Managed OAuth. You also do not need to add the MCP server hostname as a public hostname on the generated Access application.</p>
<ol>
<li>Ensure the MCP server hostname has <strong>Proxy status</strong> turned on in Cloudflare DNS.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>AI controls</strong>.</li>
<li>Go to the <strong>MCP servers</strong> tab.</li>
<li>Select <strong>Add an MCP server</strong>.</li>
<li>Enter a name for the server.</li>
<li>In <strong>HTTP URL</strong>, enter the MCP server URL, including the MCP path. For example, <code>https://mcp.example.com/mcp</code>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to define the users who can use the MCP server.</li>
<li></li>
</ol>
<p>Configure how users will authenticate:</p>
<ol>
<li>
Select the [identity providers](/cloudflare-one/integrations/identity-providers/) you want to enable for your application.
</li>
<li>
(Recommended) If you plan to only allow access via a single IdP, turn on **Apply instant authentication**. End users will not be shown the [Cloudflare Access login page](/cloudflare-one/reusable-components/custom-pages/access-login-page/). Instead, Cloudflare will redirect users directly to your SSO login event.
</li>
<li> (Optional) Turn on  <b>Authenticate with Cloudflare One Client</b> to allow users to authenticate to the application using their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/"> Cloudflare One Client session identity</a>. </li>
</ol>
<ol start="9">
<li>Select <strong>Save and connect server</strong>.</li>
<li>If the MCP server prompts you to authenticate, complete the third-party OAuth flow.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4692.md")
</aside>
<h2 id="saas-managed-third-party-mcp-server">SaaS-managed third-party MCP server</h2>
<p>Use this setup when a third-party provider hosts the MCP server and lets you configure a custom OAuth or OIDC identity provider. In this setup, the MCP server implements the OAuth authorization code flow against Cloudflare Access and receives an <code>access_token</code> that it can use to call downstream services.</p>
<p>The following guide uses a remote <span class="nb-glossary-tooltip" title="MCP server">MCP server</span> on <a href="/workers/">Cloudflare Workers</a> to show the Access for SaaS setup. For a SaaS-managed server, follow your provider's setup instructions and use the Access for SaaS values created in <a href="#2-create-an-access-for-saas-app">Step 2</a>. When users connect to the MCP server using an <span class="nb-glossary-tooltip" title="MCP client">MCP client</span>, they will be prompted to log in to your <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> and are only granted access if they pass your <a href="/cloudflare-one/access-controls/policies/#selectors">Access policies</a>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Create a <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a>.</li>
<li>Configure <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">One-time PIN</a> or connect a third-party <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a>.</li>
</ul>
<h3 id="1-deploy-an-example-mcp-server"><ol>
<li>Deploy an example MCP server</li>
</ol></h3>
<p>To deploy our <a href="https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-cf-access">example MCP server</a> to your Cloudflare account:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4697.md")
</div></div>
<h3 id="2-create-an-access-for-saas-app"><ol start="2">
<li>Create an Access for SaaS app</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4701.md")
</div></div>
<h3 id="3-configure-your-mcp-server"><ol start="3">
<li>Configure your MCP server</li>
</ol></h3>
<p>Your MCP server needs to perform an OAuth 2.0 authorization flow to get an <code>access_token</code> from the SaaS app created in <a href="#2-create-an-access-for-saas-app">Step 2</a>. When setting up the OAuth client on your MCP server, you will need to paste in the OAuth endpoints and credentials from the Access for SaaS app.</p>
<p>To add OAuth endpoints and credentials to our <a href="#1-deploy-an-example-mcp-server">example MCP server</a>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4704.md")
</div></div>
<h3 id="4-test-the-connection"><ol start="4">
<li>Test the connection</li>
</ol></h3>
<p>You can now connect to your MCP server at <code>https://mcp-server-cf-access.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/mcp</code> using <a href="https://playground.ai.cloudflare.com/">Workers AI Playground</a>, <a href="https://github.com/modelcontextprotocol/inspector">MCP inspector</a>, or <a href="/agents/model-context-protocol/guides/remote-mcp-server/#connect-your-mcp-server-to-claude-and-other-mcp-clients">other MCP clients</a> that support remote MCP servers.</p>
<p>To test in Workers AI Playground:</p>
<ol>
<li>
<p>Go to <a href="https://playground.ai.cloudflare.com/">Workers AI Playground</a>.</p>
</li>
<li>
<p>Under <strong>MCP Servers</strong>, enter <code>https://mcp-server-cf-access.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/mcp</code> for the MCP server URL.</p>
</li>
<li>
<p>Select <strong>Connect</strong>.</p>
</li>
<li>
<p>A popup window will appear requesting access to the MCP server. Select <strong>Approve</strong>.</p>
</li>
<li>
<p>Follow the prompts to log in to your identity provider.</p>
</li>
</ol>
<p>Workers AI Playground will show a <strong>Connected</strong> status. The MCP server should successfully obtain an <code>access_token</code> from Cloudflare Access.</p>
<h2 id="next-steps">Next steps</h2>
<p>To allow the MCP server to make authenticated requests to other self-hosted applications on behalf of the user, create a <a href="/cloudflare-one/access-controls/ai-controls/linked-apps/">Linked App Token</a> policy on the downstream application. The MCP server forwards the <code>Cf-Access-Jwt-Assertion</code> header it receives from Access as a <code>Cf-Access-Token</code> header to the downstream application.</p>
