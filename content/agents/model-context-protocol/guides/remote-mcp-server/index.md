---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/
  description: Deploy a remote MCP server on Cloudflare with optional authentication using Streamable HTTP transport.
  full_title: Build a Remote MCP server · Cloudflare Agents docs
  head_html: <title>Build a Remote MCP server · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a remote MCP server on Cloudflare with optional authentication using Streamable HTTP transport."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/index.md"><meta property="og:title" content="Build a Remote MCP server · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a remote MCP server on Cloudflare with optional authentication using Streamable HTTP transport."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#page","headline":"Build a Remote MCP server \u00b7 Cloudflare Agents docs","description":"Deploy a remote MCP server on Cloudflare with optional authentication using Streamable HTTP transport.","url":"https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/guides/remote-mcp-server/
  schema: 1
---
<p>This guide shows how to deploy a remote MCP server on Cloudflare using <a href="/agents/model-context-protocol/protocol/transport/">Streamable HTTP transport</a>. You have two options:</p>
<ul>
<li><strong>Without authentication</strong> — anyone can connect and use the server (no login required).</li>
<li><strong>With <a href="/agents/model-context-protocol/guides/remote-mcp-server/#add-authentication">authentication and authorization</a></strong> — users sign in before accessing tools, and you can control which tools an agent can call based on the user's permissions.</li>
</ul>
<h2 id="choosing-an-approach">Choosing an approach</h2>
<p>The Agents SDK provides multiple ways to create MCP servers. Choose the approach that fits your use case:</p>
<table>
<thead>
<tr>
<th>Approach</th>
<th>Stateful?</th>
<th>Protocol path</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/agents/model-context-protocol/apis/handler-api/"><code>createMcpHandler()</code></a></td>
<td>No</td>
<td>stateless with legacy compatibility</td>
<td>New stateless tools</td>
</tr>
<tr>
<td><a href="/agents/model-context-protocol/apis/handler-api/#createlegacymcphandler"><code>createLegacyMcpHandler()</code></a></td>
<td>Optional</td>
<td>legacy</td>
<td>Temporary existing <code>WorkerTransport</code> routes</td>
</tr>
<tr>
<td><a href="/agents/model-context-protocol/apis/agent-api/"><code>McpAgent</code></a></td>
<td>Yes</td>
<td>legacy</td>
<td>Deprecated Durable Object and RPC servers</td>
</tr>
<tr>
<td>Raw SDK transport</td>
<td>Depends on transport</td>
<td>Depends on SDK package</td>
<td>Custom transport ownership</td>
</tr>
</tbody>
</table>
<p>Use <code>createMcpHandler</code> for a new stateless server. An existing <code>McpAgent</code> without legacy stateful dependencies can migrate directly. If it uses MCP session state, RPC, pushed requests, streams, or replay, plan the stateless equivalents and serve stateless and legacy lanes during the transition. Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for the staged rollout.</p>
<h2 id="deploy-your-first-mcp-server">Deploy your first MCP server</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="template-protocol-path">Template protocol path</h3>
@markup("md", "content/.markup/bodies/2214.md")
</aside>
<p>You can start by deploying a <a href="https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless">public MCP server</a> without authentication, then add user authentication and scoped authorization later. If you already know your server will require authentication, you can skip ahead to the <a href="/agents/model-context-protocol/guides/remote-mcp-server/#add-authentication">next section</a>.</p>
<h3 id="via-the-dashboard">Via the dashboard</h3>
<p>The button below will guide you through everything you need to do to deploy an <a href="https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless">example MCP server</a> to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Once deployed, this server will be live at your <code>workers.dev</code> subdomain (for example, <code>remote-mcp-server-authless.your-account.workers.dev/mcp</code>). You can connect to it immediately using the <a href="https://playground.ai.cloudflare.com/">AI Playground</a> (a remote MCP client), <a href="https://github.com/modelcontextprotocol/inspector">MCP inspector</a> or <a href="/agents/model-context-protocol/guides/remote-mcp-server/#connect-from-an-mcp-client-via-a-local-proxy">other MCP clients</a>.</p>
<p>A new git repository will be set up on your GitHub or GitLab account for your MCP server, configured to automatically deploy to Cloudflare each time you push a change or merge a pull request to the main branch of the repository. You can clone this repository, <a href="/agents/model-context-protocol/guides/remote-mcp-server/#via-the-cli">develop locally</a>, and start customizing the MCP server with your own <a href="/agents/model-context-protocol/protocol/tools/">tools</a>.</p>
<h3 id="via-the-cli">Via the CLI</h3>
<p>You can use the <a href="/workers/wrangler">Wrangler CLI</a> to create a new MCP Server on your local machine and deploy it to Cloudflare.</p>
<ol>
<li>Open a terminal and run the following command:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless" aria-label="Copy to clipboard">Copy</button></div></div>
<p>During setup, select the following options: - For <em>Do you want to add an AGENTS.md file to help AI coding tools understand
Cloudflare APIs?</em>, choose <code>No</code>. - For <em>Do you want to use git for version control?</em>, choose <code>No</code>. - For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be testing the server before deploying).</p>
<p>Now, you have the MCP server setup, with dependencies installed.</p>
<ol start="2">
<li>Move into the project folder:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cd remote-mcp-server-authless&#10;</code></pre>
<ol start="3">
<li>In the directory of your new project, run the following command to start the development server:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npm start&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">⎔ Starting local server...&#10;[wrangler:info] Ready on http://localhost:8788&#10;</code></pre>
<p>Check the command output for the local port. In this example, the MCP server runs on port <code>8788</code>, and the MCP endpoint URL is <code>http://localhost:8788/mcp</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2213.md")
</aside>
<ol start="4">
<li>To test the server locally:
<ol>
<li>In a new terminal, run the <a href="https://github.com/modelcontextprotocol/inspector">MCP inspector</a>. The MCP inspector is an interactive MCP client that allows you to connect to your MCP server and invoke tools from a web browser.</li>
</ol>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx @modelcontextprotocol/inspector@latest&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">🚀 MCP Inspector is up and running at:&#10;	http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3&#10;&#10;🌐 Opening browser...&#10;</code></pre>
<pre tabindex="0"><code>  The MCP Inspector will launch in your web browser. You can also launch it manually by opening a browser and going to `http://localhost:&lt;PORT&gt;`. Check the command output for the local port where MCP Inspector is running. In this example, MCP Inspector is served on port `5173`.&#10;</code></pre>
<ol start="2">
<li>
<p>In the MCP inspector, enter the URL of your MCP server (<code>http://localhost:8788/mcp</code>), and select <strong>Connect</strong>. Select <strong>List Tools</strong> to show the tools that your MCP server exposes.</p>
</li>
<li>
<p>You can now deploy your MCP server to Cloudflare. From your project directory, run:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler@latest deploy&#10;</code></pre>
<p>If you have already <a href="/workers/ci-cd/builds/">connected a git repository</a> to the Worker with your MCP server, you can deploy your MCP server by pushing a change or merging a pull request to the main branch of the repository.</p>
<p>The MCP server will be deployed to your <code>*.workers.dev</code> subdomain at <code>https://remote-mcp-server-authless.your-account.workers.dev/mcp</code>.</p>
<ol start="6">
<li>To test the remote MCP server, take the URL of your deployed MCP server (<code>https://remote-mcp-server-authless.your-account.workers.dev/mcp</code>) and enter it in the MCP inspector running on <code>http://localhost:5173</code>.</li>
</ol>
<p>You now have a remote MCP server that MCP clients can connect to.</p>
<h2 id="connect-from-an-mcp-client-via-a-local-proxy">Connect from an MCP client via a local proxy</h2>
<p>Now that your remote MCP server is running, you can use the <a href="https://www.npmjs.com/package/mcp-remote"><code>mcp-remote</code> local proxy</a> to connect Claude Desktop or other MCP clients to it — even if your MCP client does not support remote transport or authorization on the client side. This lets you test what an interaction with your remote MCP server will be like with a real MCP client.</p>
<p>For example, to connect from Claude Desktop:</p>
<ol>
<li>Update your Claude Desktop configuration to point to the URL of your MCP server:</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;math&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;mcp-remote&quot;,&#10;				&quot;https://remote-mcp-server-authless.your-account.workers.dev/mcp&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<ol start="2">
<li>
<p>Restart Claude Desktop to load the MCP Server. Once this is done, Claude will be able to make calls to your remote MCP server.</p>
</li>
<li>
<p>To test, ask Claude to use one of your tools. For example:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">Could you use the math tool to add 23 and 19?&#10;</code></pre>
<p>Claude should invoke the tool and show the result generated by the remote MCP server.</p>
<p>To learn how to use remote MCP servers with other MCP clients, refer to <a href="/agents/model-context-protocol/guides/test-remote-mcp-server/">Test a Remote MCP Server</a>.</p>
<h2 id="add-authentication">Add Authentication</h2>
<p>The public MCP server example you deployed earlier allows any client to connect and invoke tools without logging in. To add user authentication to your MCP server, you can integrate Cloudflare Access or a third-party service as the OAuth provider. Your MCP server handles secure login flows and issues access tokens that MCP clients can use to make authenticated tool calls. Users sign in with the OAuth provider and grant their AI agent permission to interact with the tools exposed by your MCP server, using scoped permissions.</p>
<h3 id="cloudflare-access-oauth">Cloudflare Access OAuth</h3>
<p>You can configure your MCP server to require user authentication through Cloudflare Access. Cloudflare Access acts as an identity aggregator and verifies user emails, signals from your existing <a href="/cloudflare-one/integrations/identity-providers/">identity providers</a> (such as GitHub or Google), and other attributes such as IP address or device certificates. When users connect to the MCP server, they will be prompted to log in to the configured identity provider and are only granted access if they pass your <a href="/cloudflare-one/access-controls/policies/#selectors">Access policies</a>.</p>
<p>For a step-by-step deployment guide, refer to <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/">Secure MCP servers with Access for SaaS</a>.</p>
<h3 id="third-party-oauth">Third-party OAuth</h3>
<p>You can connect your MCP server with any <a href="/agents/model-context-protocol/protocol/authorization/#2-third-party-oauth-provider">OAuth provider</a> that supports the OAuth 2.0 specification, including GitHub, Google, Slack, <a href="/agents/model-context-protocol/protocol/authorization/#stytch">Stytch</a>, <a href="/agents/model-context-protocol/protocol/authorization/#auth0">Auth0</a>, <a href="/agents/model-context-protocol/protocol/authorization/#workos">WorkOS</a>, and more.</p>
<p>The following example demonstrates how to use GitHub as an OAuth provider.</p>
<h4 id="step-1-create-a-new-mcp-server">Step 1 — Create a new MCP server</h4>
<p>Run the following command to create a new MCP server with GitHub OAuth:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Now, you have the MCP server setup, with dependencies installed. Move into that project folder:</p>
<pre tabindex="0"><code class="language-sh">cd my-mcp-server-github-auth&#10;</code></pre>
<p>You'll notice that in the example MCP server, if you open <code>src/index.ts</code>, the primary difference is that the <code>defaultHandler</code> is set to the <code>GitHubHandler</code>:</p>
<pre tabindex="0"><code class="language-ts">import GitHubHandler from &quot;./github-handler&quot;;&#10;&#10;export default new OAuthProvider({&#10;	apiRoute: &quot;/mcp&quot;,&#10;	apiHandler: MyMCP.serve(&quot;/mcp&quot;),&#10;	defaultHandler: GitHubHandler,&#10;	authorizeEndpoint: &quot;/authorize&quot;,&#10;	tokenEndpoint: &quot;/token&quot;,&#10;	clientRegistrationEndpoint: &quot;/register&quot;,&#10;});&#10;</code></pre>
<p>This ensures that your users are redirected to GitHub to authenticate. To get this working though, you need to create OAuth client apps in the steps below.</p>
<h4 id="step-2-create-an-oauth-app">Step 2 — Create an OAuth App</h4>
<p>You'll need to create two <a href="https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app">GitHub OAuth Apps</a> to use GitHub as an authentication provider for your MCP server — one for local development, and one for production.</p>
<h4 id="step-2-1-create-a-new-oauth-app-for-local-development">Step 2.1 — Create a new OAuth App for local development</h4>
<ol>
<li>
<p>Navigate to <a href="https://github.com/settings/developers">github.com/settings/developers</a> to create a new OAuth App with the following settings:</p>
<ul>
<li><strong>Application name</strong>: <code>My MCP Server (local)</code></li>
<li><strong>Homepage URL</strong>: <code>http://localhost:8788</code></li>
<li><strong>Authorization callback URL</strong>: <code>http://localhost:8788/callback</code></li>
</ul>
</li>
<li>
<p>For the OAuth app you just created, add the client ID of the OAuth app as <code>GITHUB_CLIENT_ID</code> and generate a client secret, adding it as <code>GITHUB_CLIENT_SECRET</code> to a <code>.env</code> file in the root of your project, which <a href="/workers/configuration/secrets/">will be used to set secrets in local development</a>.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch .env&#10;echo &#x27;GITHUB_CLIENT_ID=&quot;your-client-id&quot;&#x27; &gt;&gt; .env&#10;echo &#x27;GITHUB_CLIENT_SECRET=&quot;your-client-secret&quot;&#x27; &gt;&gt; .env&#10;cat .env&#10;</code></pre>
<ol start="3">
<li>Run the following command to start the development server:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npm start&#10;</code></pre>
<p>Your MCP server is now running on <code>http://localhost:8788/mcp</code>.</p>
<ol start="4">
<li>In a new terminal, run the <a href="https://github.com/modelcontextprotocol/inspector">MCP inspector</a>. The MCP inspector is an interactive MCP client that allows you to connect to your MCP server and invoke tools from a web browser.</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx @modelcontextprotocol/inspector@latest&#10;</code></pre>
<ol start="5">
<li>Open the MCP inspector in your web browser:</li>
</ol>
<pre tabindex="0"><code class="language-sh">open http://localhost:5173&#10;</code></pre>
<ol start="6">
<li>
<p>In the inspector, enter the URL of your MCP server, <code>http://localhost:8788/mcp</code></p>
</li>
<li>
<p>In the main panel on the right, click the <strong>OAuth Settings</strong> button and then click <strong>Quick OAuth Flow</strong>.</p>
<p>You should be redirected to a GitHub login or authorization page. After authorizing the MCP Client (the inspector) access to your GitHub account, you will be redirected back to the inspector.</p>
</li>
<li>
<p>Click <strong>Connect</strong> in the sidebar and you should see the &quot;List Tools&quot; button, which will list the tools that your MCP server exposes.</p>
</li>
</ol>
<h4 id="step-2-2-create-a-new-oauth-app-for-production">Step 2.2 — Create a new OAuth App for production</h4>
<p>You'll need to repeat <a href="#step-21--create-a-new-oauth-app-for-local-development">Step 2.1</a> to create a new OAuth App for production.</p>
<ol>
<li>Navigate to <a href="https://github.com/settings/developers">github.com/settings/developers</a> to create a new OAuth App with the following settings:</li>
</ol>
<ul>
<li><strong>Application name</strong>: <code>My MCP Server (production)</code></li>
<li><strong>Homepage URL</strong>: Enter the workers.dev URL of your deployed MCP server (ex: <code>worker-name.account-name.workers.dev</code>)</li>
<li><strong>Authorization callback URL</strong>: Enter the <code>/callback</code> path of the workers.dev URL of your deployed MCP server (ex: <code>worker-name.account-name.workers.dev/callback</code>)</li>
</ul>
<ol start="2">
<li>For the OAuth app you just created, add the client ID and client secret, using Wrangler CLI:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put GITHUB_CLIENT_ID&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put GITHUB_CLIENT_SECRET&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put COOKIE_ENCRYPTION_KEY&#10;</code></pre>
<p>Use any random string for <code>COOKIE_ENCRYPTION_KEY</code>, for example the output of <code>openssl rand -hex 32</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2212.md")
</aside>
<ol start="3">
<li>
<p>Set up a KV namespace</p>
<pre tabindex="0"><code>a. Create the KV namespace:&#10;</code></pre>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">npx wrangler kv namespace create &quot;OAUTH_KV&quot;&#10;</code></pre>
<pre tabindex="0"><code>    b. Update the `wrangler.jsonc` file with the resulting KV ID:&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;kvNamespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;OAUTH_KV&quot;,&#10;			&quot;id&quot;: &quot;&lt;YOUR_KV_NAMESPACE_ID&gt;&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="4">
<li>Deploy the MCP server to your Cloudflare <code>workers.dev</code> domain:</li>
</ol>
<pre tabindex="0"><code class="language-bash">npm run deploy&#10;</code></pre>
<ol start="5">
<li>Connect to your server running at <code>worker-name.account-name.workers.dev/mcp</code> using the <a href="https://playground.ai.cloudflare.com/">AI Playground</a>, MCP Inspector, or <a href="/agents/model-context-protocol/guides/test-remote-mcp-server/">other MCP clients</a>, and authenticate with GitHub.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-mcp-tools-agents-model-context-protocol-protocol-tools"><a href="/agents/model-context-protocol/protocol/tools/">MCP Tools</a></h3><p>Add tools to your MCP server.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-authorization-agents-model-context-protocol-protocol-authorization"><a href="/agents/model-context-protocol/protocol/authorization/">Authorization</a></h3><p>Customize authentication and authorization.</p></div>
