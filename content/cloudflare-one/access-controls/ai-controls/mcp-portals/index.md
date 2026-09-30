<p>An MCP server portal centralizes multiple <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP) servers</a> onto a single HTTP endpoint.</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/mcp-portal.png" alt="MCP clients connect through an MCP portal to access internal MCP servers and SaaS MCP servers." /></p>
<p>This guide explains how to add MCP servers to Cloudflare Access, create an MCP portal with customized tools and policies, and connect users to the portal using an MCP client.</p>
<h2 id="key-features">Key features</h2>
<p>MCP server portals provide the following capabilities:</p>
<ul>
<li><strong>Streamlined access to multiple MCP servers</strong>: MCP server portals support both unauthenticated MCP servers and MCP servers secured using OAuth (for example, via <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/">Access for SaaS</a> or a <a href="/agents/model-context-protocol/protocol/authorization/">third-party OAuth provider</a>). Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.</li>
<li><strong>MCP protocol compatibility</strong>: The portal supports stateless MCP <code>2026-07-28</code> and earlier 2025 Streamable HTTP clients and servers. The portal selects the supported protocol for each connection without requiring protocol settings.</li>
<li><strong>Customized tools per portal</strong>: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.</li>
<li><strong>Tool and prompt aliases</strong>: Admins can <a href="#rename-tools-and-prompts-with-aliases">rename tools and prompts</a> and edit their descriptions at the portal or server level without modifying the upstream MCP server. Aliases help end users find the right tool and help AI agents select the correct one.</li>
<li><strong>Context optimization</strong>: Portals support query parameter options that reduce context window usage by minimizing or hiding tool definitions. Refer to <a href="#optimize-context">Optimize context</a> for details.</li>
<li><strong>Non-browser client support</strong>: MCP clients authenticate to the portal using a standard OAuth 2.0 authorization code flow via <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">managed OAuth</a>. This managed OAuth configuration applies to the portal's Access application. It is separate from upstream OAuth used by individual MCP servers in the portal. Non-browser clients receive a <code>401</code> response with a <code>WWW-Authenticate</code> header pointing to Access's OAuth discovery endpoints, rather than a browser redirect. You can also connect using <a href="#connect-with-a-service-token">Access service tokens</a> for machine-to-machine access.</li>
<li><strong>Code Mode</strong>: Code Mode collapses all upstream tools into two tools for search and code execution. The AI agent writes JavaScript that calls typed methods for each tool. The code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. Admins can control whether Code Mode is unavailable, optional, on by default, or required. Refer to <a href="#code-mode">Code Mode</a> for configuration and connection instructions.</li>
<li><strong>Observability</strong>: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal. You can optionally route portal traffic through <a href="#route-portal-traffic-through-gateway">Cloudflare Gateway</a> for richer HTTP logging and data loss prevention (DLP) scanning.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>The following diagram shows how requests flow through an MCP server portal.</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/mcp-portal-request-flow.svg" alt="Request flow diagram showing how an MCP client connects through Cloudflare Access and the MCP server portal to reach upstream MCP servers, with an optional Gateway path for DLP inspection." /></p>
<ol>
<li>An MCP client connects to the portal URL and receives a <code>401</code> response with OAuth discovery metadata.</li>
<li>The user authenticates through Cloudflare Access via their identity provider or uses <a href="#connect-with-a-service-token">service token</a> headers.</li>
<li>Access validates the user's identity, and the portal returns the tools available from enabled upstream servers.</li>
<li>When the user calls a tool, the portal identifies the target server from the <a href="#tool-namespacing">tool namespace</a>, attaches the appropriate credentials, and proxies the request. If <a href="#route-portal-traffic-through-gateway">Gateway routing</a> is turned on, the request passes through Cloudflare Gateway for HTTP logging and DLP inspection.</li>
<li>The upstream server processes the request and returns a response through the same path.</li>
</ol>
<p>For servers that use automatic OAuth registration, background synchronization of tools and prompts runs approximately every two hours using admin credentials. This sync connects directly to upstream servers and does not route through Gateway.</p>
<h3 id="transport">Transport</h3>
<p>The portal accepts stateless <a href="https://modelcontextprotocol.io/specification/2026-07-28">MCP <code>2026-07-28</code></a> and earlier 2025 Streamable HTTP clients at its <code>/mcp</code> endpoint. The portal selects the protocol from each request. You do not need to configure a protocol version.</p>
<p>The portal connects to upstream MCP servers using <a href="https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http">Streamable HTTP</a> or <a href="https://spec.modelcontextprotocol.io/specification/2024-11-05/basic/transports/#server-sent-events-sse-deprecated">SSE</a> transport. For Streamable HTTP servers, the portal checks for MCP <code>2026-07-28</code> support and uses the stateless protocol when available. If the upstream server does not support it, the portal falls back to the 2025 handshake on the same connection. SSE connections always use the legacy protocol.</p>
<p>Client and upstream protocol selection are independent. For example, a 2025 client can connect through a portal to a stateless upstream server. A stateless client can also connect to a legacy upstream server.</p>
<p>You do not need to specify which transport your upstream server uses. The portal automatically detects the correct transport by trying multiple connection strategies in order:</p>
<table>
<thead>
<tr>
<th>Upstream URL pattern</th>
<th>Connection strategies (in order)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ends in <code>/mcp</code></td>
<td>Streamable HTTP only</td>
</tr>
<tr>
<td>Ends in <code>/sse</code></td>
<td>SSE (or Streamable HTTP if Gateway routing is turned on)</td>
</tr>
<tr>
<td>All other URLs</td>
<td>Streamable HTTP on original URL, then SSE on original URL, then Streamable HTTP on <code>{url}/mcp</code>, then SSE on <code>{url}/sse</code></td>
</tr>
</tbody>
</table>
<p>If a connection attempt returns a <code>404</code>, <code>405</code>, or <code>406</code> error, the portal falls back to the next strategy. All other errors stop the connection attempt.</p>
<h3 id="built-in-portal-tools">Built-in portal tools</h3>
<p>Every portal exposes the following built-in tools to MCP clients, in addition to the upstream server tools:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>portal_list_servers</code></td>
<td>Lists all available upstream servers with their ID, name, and whether they are currently turned on.</td>
</tr>
<tr>
<td><code>portal_toggle_servers</code></td>
<td>Opens a URL-based server selection page where you can turn servers on or off.</td>
</tr>
<tr>
<td><code>portal_toggle_single_server</code></td>
<td>Turns a single server on or off by server ID, without leaving the MCP client.</td>
</tr>
</tbody>
</table>
<p>When <a href="#optimize-context">context optimization</a> is turned on, additional tools are exposed depending on the mode:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Additional tools</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>minimize_tools</code></td>
<td><code>portal_query_tools</code> — Search tools by regex pattern and return full definitions.</td>
</tr>
<tr>
<td><code>search_and_execute</code></td>
<td><code>portal_query_tools</code> and <code>portal_execute</code> — Search tools and execute them via proxy.</td>
</tr>
</tbody>
</table>
<h3 id="session-lifecycle">Session lifecycle</h3>
<p>MCP <code>2026-07-28</code> requests are stateless and do not create an MCP protocol session. The portal retains authentication, server selection, and upstream OAuth state for the user's portal authorization grant.</p>
<p>Earlier 2025 clients create a session that persists until the user disconnects or the session expires after 24 hours of inactivity.</p>
<p>Users can turn individual servers on or off without disconnecting. For stateless requests, server toggles apply to every request that uses the same portal authorization grant. For legacy clients, toggles are scoped to the MCP session. Toggles do not affect other users.</p>
<h3 id="naming">Naming</h3>
<p>MCP server portals were previously referred to as <strong>Agents Gateway</strong> in some contexts. The API paths, Terraform resources, and internal codebases may still use <code>agents_gateway</code> or <code>agw</code> prefixes. The product name is <strong>MCP server portals</strong> and the dashboard navigation is <strong>MCP Portals</strong>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A domain for the portal URL. You can use one of the following:
<ul>
<li>An <a href="/fundamentals/manage-domains/add-site/">active domain on Cloudflare</a> that uses either a <a href="/dns/zone-setups/full-setup/">full setup</a> or a <a href="/dns/zone-setups/partial-setup/">partial (<code>CNAME</code>) setup</a></li>
<li>Your account's <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a></li>
<li>A <code>pages.dev</code> domain associated with a Cloudflare Pages project</li>
</ul>
</li>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured on Cloudflare Zero Trust</li>
</ul>
<h2 id="add-an-mcp-server">Add an MCP server</h2>
<p>Add individual MCP servers to Cloudflare Access to bring them under centralized management.</p>
<p>To add an MCP server:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Go to the <strong>MCP servers</strong> tab.</li>
<li>Select <strong>Add an MCP server</strong>.</li>
<li>Enter any name for the server.</li>
<li>(Optional) Enter a custom string for the <strong>Server ID</strong>.</li>
<li>In <strong>HTTP URL</strong>, enter the full URL of your MCP server. For example, if you want to add the <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/docs-ai-search">Cloudflare Documentation MCP server</a>, enter <code>https://docs.mcp.cloudflare.com/mcp</code>.</li>
<li>Add <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to show or hide the server in an <a href="#create-a-portal">MCP server portal</a>. The MCP server link will only appear in the portal for users who match an Allow policy. Users who do not pass an Allow policy will not see this server through any portals.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4719.md")
</aside>
<ol start="8">
<li>Select <strong>Save and connect server</strong>.</li>
<li>If the MCP server supports OAuth, you will be redirected to log in to your OAuth provider. You can log in to any account on the MCP server. The account used to authenticate will serve as the admin credential for that MCP server. You can <a href="#create-a-portal">configure an MCP portal</a> to use this admin credential to make requests.</li>
</ol>
<p>Cloudflare Access will validate the server connection and retrieve a list of prompts and tools. Once the server is successfully connected, the <a href="#server-status">server status</a> will change to <strong>Ready</strong>. You can now add the MCP server to an <a href="#create-a-portal">MCP server portal</a>.</p>
<h3 id="configure-manual-oauth-credentials">Configure manual OAuth credentials</h3>
<p>Use manual OAuth credentials when the upstream provider does not support <a href="https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#dynamic-client-registration">OAuth Dynamic Client Registration</a>. This flow uses an OAuth application that you register with the upstream provider.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4720.md")
</div>
<p>The dashboard uses the <a href="#shared-cloudflare-callback-url-opt-in">shared Cloudflare callback URL</a> when you switch a server from automatic to manual credentials:</p>
<pre><code class="language-txt">https://oauth-callbacks.cloudflareaccess.com/cdn-cgi/access/outbound-oauth-callback&#10;</code></pre>
<p>Always register the redirect URI displayed in the dashboard. OAuth providers typically require an exact URI match.</p>
<p>Cloudflare stores the client secret encrypted and does not return it through the dashboard or API. When editing the server, leave <strong>Client secret</strong> blank to keep the existing value. To rotate the secret, create or activate the replacement at the upstream provider, enter the new value, and save the server.</p>
<p>Manual credentials require per-user authentication. Leave <strong>Require user auth</strong> enabled when you add the server to a portal. The server remains in <strong>Waiting</strong> status until the first user completes upstream OAuth. Cloudflare then retrieves the server's tools and prompts and changes its status to <strong>Ready</strong>.</p>
<h3 id="mcp-apps">MCP Apps</h3>
<p><a href="https://modelcontextprotocol.io/extensions/apps/overview">MCP Apps</a> — tools that declare a UI resource in their description — will also be available after successfully connecting to an MCP server. A list of MCP clients that support MCP Apps is available in the <a href="https://modelcontextprotocol.io/extensions/client-matrix">Extension Support Matrix</a>.</p>
<h3 id="server-status">Server status</h3>
<p>The MCP server status indicates the server's connection and tool and prompt synchronization status in Cloudflare Access.</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error</td>
<td>The server could not be reached or returned an error. Refer to <a href="#error-details">error details</a> to identify and fix the cause.</td>
</tr>
<tr>
<td>Sync Required</td>
<td>The server's OAuth credentials can no longer be refreshed and the server needs to be reauthenticated. To fix the issue, <a href="#reauthenticate-the-mcp-server">reauthenticate the server</a>.</td>
</tr>
<tr>
<td>Waiting</td>
<td>The server's tools and prompts are being synchronized. A server with manual OAuth credentials remains in this state until its first user completes upstream OAuth.</td>
</tr>
<tr>
<td>Ready</td>
<td>The server connected successfully and its tools and prompts were synchronized. This status does not guarantee that the server will connect or return resources when queried.</td>
</tr>
</tbody>
</table>
<h4 id="error-details">Error details</h4>
<p>When an MCP server is in the <strong>Error</strong> or <strong>Sync Required</strong> state, hover over its status in the dashboard to view available diagnostic information. The API returns these details in the <code>error_details</code> object:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>status_code</code></td>
<td>The HTTP status code returned by the MCP server, if available.</td>
</tr>
<tr>
<td><code>mcp_code</code></td>
<td>The MCP protocol error code, if the server returned an MCP error.</td>
</tr>
<tr>
<td><code>retryable</code></td>
<td>Whether the error is likely to be temporary and the connection is worth retrying.</td>
</tr>
<tr>
<td><code>is_upstream</code></td>
<td><code>true</code> if the MCP server returned the error; <code>false</code> if the connection to the MCP server failed.</td>
</tr>
<tr>
<td><code>cause</code></td>
<td>The underlying error message.</td>
</tr>
</tbody>
</table>
<p>If <code>is_upstream</code> is <code>true</code>, use <code>status_code</code>, <code>mcp_code</code>, and <code>cause</code> to troubleshoot the MCP server. If it is <code>false</code>, verify that the server URL is correct and reachable. Retry the sync when <code>retryable</code> is <code>true</code>; otherwise, correct the reported cause before trying again. Reauthenticate the server only when the error points to expired or invalid credentials.</p>
<h3 id="reauthenticate-the-mcp-server">Reauthenticate the MCP server</h3>
<p>To reauthenticate an MCP server in Cloudflare Access:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Go to the <strong>MCP servers</strong> tab.</li>
<li>Select the server that you want to reauthenticate, then select <strong>Edit</strong>.</li>
<li>Select <strong>Authenticate server</strong>.</li>
</ol>
<p>You will be redirected to log in to your OAuth provider. The account used to authenticate will serve as the new admin credential for this MCP server.</p>
<h3 id="synchronize-the-mcp-server">Synchronize the MCP server</h3>
<p>For servers that use automatic OAuth registration, Cloudflare Access synchronizes tools and prompts approximately every two hours. During synchronization, Cloudflare connects to your MCP server using the <a href="#reauthenticate-the-mcp-server">admin credential</a> and fetches the current list of tools and prompts. If the admin credential's OAuth access token has expired, Cloudflare refreshes it automatically using the stored refresh token before connecting.</p>
<p>Resources are not synchronized or stored. When an MCP client sends a <code>resources/list</code> request, the portal fetches resources live from the upstream servers. Servers that cannot connect or respond are omitted from the result.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4718.md")
</aside>
<p>To manually refresh the MCP server in Zero Trust:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Go to the <strong>MCP servers</strong> tab and find the server that you want to refresh.</li>
<li>Select the three dots &gt; <strong>Sync capabilities</strong>.</li>
</ol>
<p>The MCP server page will show the updated list of tools and prompts. New tools and prompts are automatically enabled in the MCP server portal.</p>
<p>You can also trigger a sync via the API. The sync endpoint returns the current server state after synchronization, including the updated <a href="#server-status">server status</a>, tool count, and <a href="#error-details">error details</a> if the sync failed.</p>
<h3 id="upstream-oauth-callback-url">Upstream OAuth callback URL</h3>
<p>When a user authorizes an upstream MCP server that requires per-user OAuth, the portal performs an OAuth authorization code flow with the upstream server on the user's behalf. As part of this flow, the portal registers a callback URL (<code>redirect_uri</code>) with the upstream server. The upstream server redirects to this URL after the user authorizes access.</p>
<p>By default, the portal uses a callback URL on your portal domain:</p>
<pre><code class="language-txt">https://&lt;your-portal-hostname&gt;/servers-callback&#10;</code></pre>
<p>Allowlist this URL as a redirect URI at the upstream OAuth provider. OAuth providers typically exact-match the full URI including path.</p>
<h4 id="shared-cloudflare-callback-url-opt-in">Shared Cloudflare callback URL (opt-in)</h4>
<p>If you turn on the shared callback URL for an MCP server, every portal that uses that server uses this Cloudflare-owned URL instead:</p>
<pre><code class="language-txt">https://oauth-callbacks.cloudflareaccess.com/cdn-cgi/access/outbound-oauth-callback&#10;</code></pre>
<p>Use the shared callback URL when an upstream vendor only allows a small number of redirect URIs, or when you want one callback URL for a server across multiple portals. This setting is off by default and configured separately for each OAuth server. To turn it on, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong> &gt; <strong>MCP servers</strong>, add or edit an OAuth server, and turn on <strong>Use the Cloudflare-hosted OAuth callback</strong> under <strong>Basic information</strong> &gt; <strong>Advanced settings</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4717.md")
</aside>
<h2 id="create-a-portal">Create a portal</h2>
<p>To create an MCP server portal:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Select <strong>Add MCP server portal</strong>.</li>
<li>Enter any name for the portal.</li>
<li>Under <strong>Custom domain</strong>, select a domain for the portal URL. You can choose a domain from an active zone in your account, your account's <code>workers.dev</code> subdomain, or a <code>pages.dev</code> domain associated with a Pages project. You can optionally specify a subdomain.</li>
<li><a href="#add-an-mcp-server">Add MCP servers</a> to the portal.</li>
<li>(Optional) Under <strong>MCP servers</strong>, <a href="#manage-tools-and-prompts">configure the tools and prompts</a> available through the portal.</li>
<li>(Optional) Configure <strong>Require user auth</strong> for servers that support OAuth: - <code>Enabled</code>: (default) User will be prompted to utilize their own login credentials to establish a connection with the MCP server. - <code>Disabled</code>: Users who are connected to the portal will automatically have access to the MCP server via its <a href="#reauthenticate-the-mcp-server">admin credential</a>.</li>
<li>Add <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to define the users who can connect to the portal URL.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4716.md")
</aside>
<ol start="9">
<li>Select <strong>Add an MCP server portal</strong>.</li>
<li>(Optional) <a href="#customize-login-settings">Customize the login experience</a> for the portal.</li>
</ol>
<p>Users can now <a href="#connect-to-a-portal">connect to the portal</a> at <code>https://&lt;subdomain&gt;.&lt;domain&gt;/mcp</code> using an MCP client.</p>
<h3 id="customize-login-settings">Customize login settings</h3>
<p>Cloudflare Access automatically creates an Access application for each MCP server portal. You can customize the portal login experience by updating Access application settings:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Find the portal that you want to configure, then select the three dots &gt; <strong>Edit</strong>.</li>
<li>To configure identity providers for the portal:
<ol>
<li>Go to <strong>Authentication</strong>.</li>
<li>Select the <a href="/cloudflare-one/integrations/identity-providers/">identity providers</a> that you want to enable for your application.</li>
<li>(Recommended) If you plan to only allow access via a single identity provider, turn on <strong>Apply instant authentication</strong>. End users will not be shown the <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">Cloudflare Access login page</a>. Instead, Cloudflare will redirect users directly to your SSO login event.</li>
</ol>
</li>
<li>To customize the block page:
<ol>
<li>Go to <strong>Additional settings</strong>.</li>
<li></li>
</ol>
</li>
</ol>
<p><strong>Custom block pages</strong>: Choose what users will see when they are denied access to the application.</p>
<ul>
<li><strong>Cloudflare default</strong>: Reload the <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">login page</a> and display a block message below the Cloudflare Access logo. The default message is <code>That account does not have access</code>, or you can enter a custom message.</li>
<li><strong>Redirect URL</strong>: Redirect to the specified website.</li>
<li><strong>Custom page template</strong>: Display a <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/">custom block page</a> hosted in Cloudflare One.</li>
</ul>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="manage-tools-and-prompts">Manage tools and prompts</h2>
<p>When you add an MCP server to a portal, all of its tools and prompts are available to portal users by default. You can customize which tools and prompts are exposed, rename them with aliases, and override their descriptions.</p>
<h3 id="turn-off-individual-tools-or-prompts">Turn off individual tools or prompts</h3>
<p>To hide specific tools or prompts from portal users:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Find the portal you want to configure, then select the three dots &gt; <strong>Edit</strong>.</li>
<li>Under <strong>Servers</strong>, select the server name to open its tools panel.</li>
<li>Scroll down to the <strong>Tools</strong> section, then turn off the toggle next to any tool or prompt that you want to hide from users.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/applications/mcp-portal-manage-tools.png" alt="The tools panel for an MCP server shows a list of tools with a toggle next to each one." /></p>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Turned-off tools will not appear in the portal's tool list. Users will not be able to call them.</p>
<h3 id="use-an-allowlist-pattern">Use an allowlist pattern</h3>
<p>By default, all tools and prompts from an MCP server are available in the portal. You can invert this behavior so that all tools are hidden by default and only explicitly turned-on tools are exposed. This is useful when an MCP server has many tools but you only want to expose a curated subset.</p>
<p>To configure an allowlist via the API, set <code>default_disabled</code> to <code>true</code> on the server-to-portal mapping, then explicitly list the tools you want to expose in <code>updated_tools</code>:</p>
<pre><code class="language-json">{&#10;	&quot;servers&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;example-server&quot;,&#10;			&quot;default_disabled&quot;: true,&#10;			&quot;updated_tools&quot;: [&#10;				{&#10;					&quot;name&quot;: &quot;search_documents&quot;,&#10;					&quot;enabled&quot;: true&#10;				},&#10;				{&#10;					&quot;name&quot;: &quot;list_projects&quot;,&#10;					&quot;enabled&quot;: true&#10;				}&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>With <code>default_disabled</code> set to <code>true</code>, only <code>search_documents</code> and <code>list_projects</code> will be available to portal users. All other tools from this server will be hidden.</p>
<h3 id="rename-tools-and-prompts-with-aliases">Rename tools and prompts with aliases</h3>
<p>Aliases let you give tools and prompts clearer names in the portal. Use aliases to:</p>
<ul>
<li>Replace unclear tool names with names that match your organization's terminology.</li>
<li>Add or improve descriptions so AI agents select the correct tool.</li>
<li>Standardize naming across multiple MCP servers in a portal.</li>
</ul>
<p>Alias names must be 1-40 characters and can only contain letters, numbers, hyphens, and underscores. Names must start and end with an alphanumeric character. The value must match <code>^[a-zA-Z0-9]+([_-][a-zA-Z0-9]+)*$</code>. For example, <code>search_customer_records</code> or <code>get-user-profile</code>. No two tools or prompts on the same server can share the same name, whether that name is an alias or the original upstream name.</p>
<h4 id="alias-precedence">Alias precedence</h4>
<p>You can set aliases at two levels. Portal-level aliases take precedence over server-level aliases.</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Field</th>
<th>Scope</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Server-level</strong></td>
<td><code>alias</code></td>
<td>Applies across all portals that include this server</td>
</tr>
<tr>
<td><strong>Portal-level</strong></td>
<td><code>portal_alias</code></td>
<td>Applies only within a specific portal; overrides server-level</td>
</tr>
</tbody>
</table>
<p>When multiple names exist, the portal resolves them in this order: <code>portal_alias</code> &gt; <code>server_alias</code> &gt; <code>alias</code> &gt; original tool name.</p>
<p>If no alias is set, the portal uses the original name and description from the upstream server.</p>
<p>Custom descriptions follow the same precedence. Set a description by including the <code>description</code> field on an entry in <code>updated_tools</code> or <code>updated_prompts</code>. In API responses, server-level descriptions are returned as <code>server_description</code> and portal-level descriptions are returned as <code>portal_description</code>. Portal-level descriptions take precedence over server-level descriptions when both are set.</p>
<h4 id="set-aliases-in-the-dashboard">Set aliases in the dashboard</h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="aliasLevel"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4723.md")
</div></div>
<p>Tools and prompts that have been modified display a <strong>Modified</strong> label in the dashboard.</p>
<h4 id="set-aliases-with-the-api">Set aliases with the API</h4>
<p>Send a <code>PUT</code> request to the <a href="/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/portals/methods/update/">update a MCP portal</a> endpoint. Include the <code>alias</code> field for each tool or prompt you want to rename.</p>
<pre><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/portals/{id}</code></pre>
<p>To set server-level aliases that apply across all portals, send a <code>PUT</code> request to the <a href="/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/update/">update a MCP server</a> endpoint with the same <code>updated_tools</code> and <code>updated_prompts</code> fields.</p>
<h4 id="reset-an-alias">Reset an alias</h4>
<p>To reset a tool or prompt to its original upstream name, open the edit modal for the tool or prompt in the dashboard and select &quot;Reset to server definition.&quot; When using the API, omit the <code>alias</code> field from the corresponding entry in <code>updated_tools</code> or <code>updated_prompts</code>.</p>
<h4 id="how-aliases-affect-end-users">How aliases affect end users</h4>
<p>MCP clients receive the aliased name and description instead of the original. End users do not see the original name.</p>
<p>If you change an alias while a user has an active session, the user must reauthenticate to see the update. Refer to <a href="#manage-portal-sessions">Manage portal sessions</a> for reauthentication options.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4715.md")
</aside>
<h3 id="tool-and-prompt-namespacing">Tool and prompt namespacing</h3>
<p>All tools and prompts exposed through a portal are automatically namespaced with the server ID as a prefix. The format is <code>{server_id}_{original_name}</code>. For example, a tool named <code>list_issues</code> on a server with ID <code>github</code> appears as <code>github_list_issues</code> in the portal. This prevents name collisions when multiple MCP servers expose tools with the same name.</p>
<p>Prompts follow the same pattern. A prompt named <code>summarize</code> on a server with ID <code>github</code> appears as <code>github_summarize</code>.</p>
<h4 id="how-the-server-id-is-determined">How the server ID is determined</h4>
<p>The server ID used for namespacing comes from the <strong>Server ID</strong> field you set when <a href="#add-an-mcp-server">adding an MCP server</a>. You can enter a custom server ID in step 5 of the setup process, or let Cloudflare generate one automatically.</p>
<p>Choose short, descriptive server IDs when you plan to expose the server through a portal. The server ID becomes part of every tool name that MCP clients and AI agents see.</p>
<h4 id="parsing-namespaced-names">Parsing namespaced names</h4>
<p>The portal splits namespaced names on the <strong>first</strong> underscore only. Everything before the first underscore is the server ID, and everything after it is the tool or prompt name. This means tool names can contain underscores without ambiguity.</p>
<table>
<thead>
<tr>
<th>Namespaced name</th>
<th>Server ID</th>
<th>Tool name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>github_list_issues</code></td>
<td><code>github</code></td>
<td><code>list_issues</code></td>
</tr>
<tr>
<td><code>github_create_pull_request</code></td>
<td><code>github</code></td>
<td><code>create_pull_request</code></td>
</tr>
<tr>
<td><code>sentry_get_issue_details</code></td>
<td><code>sentry</code></td>
<td><code>get_issue_details</code></td>
</tr>
</tbody>
</table>
<p>Because the split happens on the first underscore, server IDs themselves cannot contain underscores. Use hyphens instead when you need a multi-word server ID (for example, <code>my-server</code>).</p>
<h4 id="namespacing-with-aliases">Namespacing with aliases</h4>
<p>If you <a href="#rename-tools-and-prompts-with-aliases">rename a tool with an alias</a>, the alias replaces the original tool name in the namespaced format. The server ID prefix still applies.</p>
<p>For example, if you alias the tool <code>list_issues</code> to <code>issues</code> on a server with ID <code>github</code>, the namespaced name becomes <code>github_issues</code>.</p>
<h4 id="namespacing-in-code-mode">Namespacing in Code Mode</h4>
<p>When <a href="#code-mode">Code Mode</a> is active, the portal applies an additional transformation to make namespaced tool names safe for use as JavaScript identifiers. Hyphens and dots in the namespaced name are replaced with underscores, names that start with a digit get a <code>_</code> prefix, and JavaScript reserved words get a <code>_</code> suffix. For example, a server with ID <code>my-server</code> and a tool named <code>get-data</code> would appear as <code>my_server_get_data</code> in the Code Mode sandbox.</p>
<p>This sanitization happens automatically. You do not need to call any helper functions when using Code Mode as an end user.</p>
<h4 id="helper-functions-in-the-agents-sdk">Helper functions in the Agents SDK</h4>
<p>If you are building an MCP client with the <a href="/agents/model-context-protocol/apis/client-api/">Agents SDK</a>, the SDK provides helper functions for working with server IDs and tool names:</p>
<ul>
<li><strong><code>normalizeServerId</code></strong> (exported from <code>agents/mcp/client</code>) normalizes a caller-supplied server ID into a safe string. For example, <code>&quot;GitHub MCP!&quot;</code> becomes <code>&quot;github-mcp&quot;</code>. The SDK calls this automatically when you pass an <code>id</code> option to <code>addMcpServer()</code>.</li>
<li><strong><code>sanitizeToolName</code></strong> (exported from <code>@cloudflare/codemode</code>) converts a tool name into a valid JavaScript identifier by replacing hyphens and dots with underscores. This is called automatically in Code Mode contexts. Refer to the <a href="/agents/tools/codemode/api-reference/#code-and-output-utilities">Code Mode SDK reference</a> for details.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4714.md")
</aside>
<h3 id="portal-native-tools">Portal-native tools</h3>
<p>In addition to upstream MCP server tools, the portal exposes its own built-in tools that let AI agents manage server connections and discover tools during a session. These tools use the <code>portal_</code> prefix and are not associated with any upstream server.</p>
<h4 id="always-available">Always available</h4>
<p>The following tools are available in every portal session, regardless of the connection mode:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>portal_list_servers</code></td>
<td>Lists all upstream MCP servers with their IDs, names, and whether they are currently enabled in the session.</td>
</tr>
<tr>
<td><code>portal_toggle_servers</code></td>
<td>Opens a server selection flow. Returns a URL that the user visits in a browser to enable or disable servers and manage OAuth credentials.</td>
</tr>
<tr>
<td><code>portal_toggle_single_server</code></td>
<td>Toggles a single server on or off without requiring a browser visit. Accepts a <code>server_id</code> and an <code>action</code> (<code>toggle</code> or <code>untoggle</code>). If the server requires OAuth and the user has not authenticated yet, the portal falls back to the browser-based <code>portal_toggle_servers</code> flow.</td>
</tr>
</tbody>
</table>
<p>These tools power the <a href="#manage-portal-sessions">session management</a> features described later in this guide. AI agents call them automatically when you ask to enable a server, disable a server, or return to the server selection page.</p>
<h4 id="context-optimization-tools">Context optimization tools</h4>
<p>When you connect with the <a href="#optimize-context"><code>optimize_context</code></a> query parameter, the portal exposes additional tools for discovering and calling upstream tools:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Available in</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>portal_query_tools</code></td>
<td><code>minimize_tools</code>, <code>search_and_execute</code></td>
<td>Searches upstream tools by name, description, or schema using a regex pattern. Returns full tool definitions so the agent can call them. Required in <code>minimize_tools</code> mode because upstream tool schemas are stripped to reduce context size.</td>
</tr>
<tr>
<td><code>portal_execute</code></td>
<td><code>search_and_execute</code></td>
<td>Calls an upstream tool by name with the provided arguments. In <code>search_and_execute</code> mode, upstream tools are hidden from the tool list entirely, so agents must use <code>portal_query_tools</code> to discover them and <code>portal_execute</code> to call them.</td>
</tr>
</tbody>
</table>
<h4 id="code-mode-tools">Code Mode tools</h4>
<p>When you connect with <a href="#code-mode">Code Mode</a> enabled, the portal replaces all upstream tools with two code execution tools:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>portal_codemode_search</code></td>
<td>Searches available tools by running JavaScript in a sandboxed Worker. The sandbox provides a <code>codemode.tools()</code> function that returns all upstream tool definitions with sanitized names.</td>
</tr>
<tr>
<td><code>portal_codemode_execute</code></td>
<td>Calls upstream tools by running JavaScript in a sandboxed Worker. The sandbox provides a <code>codemode</code> proxy object where each property maps to an upstream tool. Supports <code>Promise.all()</code> for parallel tool calls.</td>
</tr>
</tbody>
</table>
<p>Refer to the <a href="/agents/tools/codemode/api-reference/">Code Mode SDK reference</a> for details on writing code for these tools.</p>
<h2 id="manage-portals-via-api">Manage portals via API</h2>
<p>In addition to the dashboard, you can manage MCP server portals programmatically using the Cloudflare API. The following examples show common operations.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4713.md")
</aside>
<h3 id="list-portals">List portals</h3>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/portals</code></pre>
<h3 id="create-a-portal-1">Create a portal</h3>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/portals</code></pre>
<h3 id="list-mcp-servers">List MCP servers</h3>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/servers</code></pre>
<h3 id="create-an-mcp-server">Create an MCP server</h3>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/servers</code></pre>
<p>The <code>auth_type</code> field accepts the following values:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>oauth</code></td>
<td>The server requires OAuth authentication. You can use automatic OAuth registration or provide manual OAuth credentials.</td>
</tr>
<tr>
<td><code>bearer</code></td>
<td>The server uses a static bearer token or custom authentication headers. Provide the credentials in <code>auth_credentials</code> (refer to <a href="#bearer-authentication-credentials">Bearer authentication credentials</a>).</td>
</tr>
<tr>
<td><code>unauthenticated</code></td>
<td>The server does not require authentication.</td>
</tr>
</tbody>
</table>
<h4 id="manual-oauth-credentials">Manual OAuth credentials</h4>
<p>To create an MCP server with a pre-registered OAuth client, set <code>auth_type</code> to <code>oauth</code> and provide both <code>auth_credentials</code> and <code>client_secret</code>. The <code>auth_credentials</code> value is required and must be a JSON-encoded string:</p>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/servers</code></pre>
<p>The decoded <code>auth_credentials</code> object must contain:</p>
<ul>
<li><code>auth_mode</code>: Must be <code>manual</code>.</li>
<li><code>config.authorization_endpoint</code> and <code>config.token_endpoint</code>: The upstream provider's OAuth endpoints. <code>issuer</code> and <code>revocation_endpoint</code> are optional.</li>
<li><code>registration_info.client_id</code>: The client ID issued by the upstream provider.</li>
<li><code>registration_info.redirect_uris</code>: At least one registered redirect URI. This can be omitted when <code>is_shared_oauth_callback_enabled</code> is <code>true</code>; Cloudflare then adds the shared callback URL.</li>
<li><code>registration_info.token_endpoint_auth_method</code>: Optional. Accepted values are <code>none</code>, <code>client_secret_post</code>, and <code>client_secret_basic</code>.</li>
<li><code>registration_info.scope</code>: Optional space-delimited scope string.</li>
</ul>
<p>Do not include <code>client_secret</code> or OAuth tokens inside <code>auth_credentials</code>. Send <code>client_secret</code> as the separate sibling field shown above.</p>
<p>To change the OAuth metadata, send <code>auth_credentials</code> in a <code>PUT</code> request to the <a href="/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/update/">update an MCP server</a> endpoint. An existing manual OAuth server can be updated without <code>client_secret</code>; the stored secret remains unchanged. Send a new <code>client_secret</code> to rotate it. A new manual OAuth server, or a server being changed to manual OAuth, requires a non-empty <code>client_secret</code>.</p>
<p>The client secret is write-only. Cloudflare encrypts it before storage and never returns it from read, create, or update requests. Responses also omit the raw <code>auth_credentials</code> value. Use <code>auth_config_summary.has_client_secret</code> and <code>auth_config_summary.client_secret_version</code> to confirm that a secret is configured and identify its current version.</p>
<h4 id="bearer-authentication-credentials">Bearer authentication credentials</h4>
<p>The <code>auth_credentials</code> field accepts two forms:</p>
<ul>
<li><strong>A raw bearer token</strong> — the portal sends the value as the <code>Authorization: Bearer &lt;token&gt;</code> header on requests to the upstream MCP server:</li>
</ul>
<pre><code class="language-json">{&#10;  &quot;auth_type&quot;: &quot;bearer&quot;,&#10;  &quot;auth_credentials&quot;: &quot;your-bearer-token&quot;&#10;}&#10;</code></pre>
<ul>
<li><strong>A JSON-encoded object of custom headers</strong> — for upstream MCP servers that require multiple headers or a non-standard header name:</li>
</ul>
<pre><code class="language-json">{&#10;  &quot;auth_type&quot;: &quot;bearer&quot;,&#10;  &quot;auth_credentials&quot;: &quot;{\&quot;headers\&quot;:{\&quot;X-Api-Key\&quot;:\&quot;&lt;api-key&gt;\&quot;,\&quot;X-Client-Id\&quot;:\&quot;&lt;client-id&gt;\&quot;}}&quot;&#10;}&#10;</code></pre>
<p>The value of <code>auth_credentials</code> must be a JSON string. The parsed object must have a <code>headers</code> field mapping header names to string values. The portal forwards all headers verbatim to the upstream MCP server.</p>
<h3 id="view-tool-call-analytics">View tool-call analytics</h3>
<p>Use the account endpoint to retrieve daily or monthly MCP tool-call counts across the account:</p>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/analytics/tool-calls/timeseries?granularity=daily&amp;aggregate=false&amp;tz=utc&amp;days=30</code></pre>
<p>The same query parameters apply to each endpoint:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Values and behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>granularity</code></td>
<td><code>daily</code> or <code>monthly</code>. Defaults to <code>daily</code>.</td>
</tr>
<tr>
<td><code>aggregate</code></td>
<td><code>true</code> or <code>false</code>. Defaults to <code>false</code>. Set to <code>true</code> to request aggregated counts.</td>
</tr>
<tr>
<td><code>tz</code></td>
<td><code>utc</code>, <code>Z</code>, or a fixed <code>+HH:MM</code> or <code>-HH:MM</code> offset. Defaults to <code>utc</code>. Offsets range from <code>-12:00</code> through <code>+14:00</code>; <code>+14:00</code> and <code>-12:00</code> are the limits. The offset is used for local-day bucketing and does not account for daylight saving time changes within the window.</td>
</tr>
<tr>
<td><code>days</code></td>
<td>An integer from <code>1</code> to <code>179</code>. For daily results, this sets the trailing window and defaults to <code>7</code>. It is ignored when <code>granularity=monthly</code>.</td>
</tr>
</tbody>
</table>
<p>The response <code>result</code> includes the selected <code>granularity</code>, <code>aggregate</code>, and <code>tz</code>, the <code>start</code> and <code>end</code> of the window as epoch milliseconds, a <code>series</code> of <code>day</code> and <code>count</code> values, and the <code>total</code> count. The window includes <code>start</code> and excludes <code>end</code>. Daily <code>day</code> values use <code>YYYY-MM-DD</code> in the requested timezone offset.</p>
<p>Use a scoped endpoint to limit the counts:</p>
<ul>
<li>Server: <code>GET /accounts/{account_id}/access/ai-controls/mcp/analytics/servers/{server_id}/tool-calls/timeseries</code></li>
<li>Portal: <code>GET /accounts/{account_id}/access/ai-controls/mcp/analytics/portals/{portal_id}/tool-calls/timeseries</code></li>
</ul>
<h3 id="force-sync-an-mcp-server">Force sync an MCP server</h3>
<p>To manually trigger a synchronization of tools and prompts from an upstream MCP server:</p>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/servers/{server_id}/sync</code></pre>
<h3 id="delete-a-portal">Delete a portal</h3>
<pre><code class="language-bash">curl --request DELETE --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/ai-controls/mcp/portals/{id}</code></pre>
<h2 id="configure-via-terraform">Configure via Terraform</h2>
<p>You can manage MCP server portals using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>. Use the <code>cloudflare_zero_trust_access_mcp_server_portal</code> resource to create and configure portals programmatically.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4712.md")
</aside>
<p>The following example creates an MCP server portal with a CNAME record:</p>
<pre><code class="language-hcl">&#35; Create the MCP server portal&#10;resource &quot;cloudflare_zero_trust_access_mcp_server_portal&quot; &quot;example&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;Engineering Portal&quot;&#10;  hostname   = &quot;mcp.example.com&quot;&#10;}&#10;&#10;&#35; Required: Create the CNAME record for the portal hostname&#10;resource &quot;cloudflare_dns_record&quot; &quot;mcp_portal&quot; {&#10;  zone_id = var.cloudflare_zone_id&#10;  name    = &quot;mcp&quot;&#10;  content = &quot;gateway.agents.cloudflare.com&quot;&#10;  type    = &quot;CNAME&quot;&#10;  proxied = true&#10;}&#10;</code></pre>
<p>For the full list of supported resource arguments, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider documentation</a>.</p>
<h2 id="code-mode">Code Mode</h2>
<p><a href="/agents/tools/codemode/">Code Mode</a> reduces context window usage by replacing upstream tool definitions with two tools for search and code execution. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. Authentication credentials and environment variables remain outside the model context.</p>
<p>Code Mode is useful for portals with many MCP servers or tools. Context window usage stays fixed as the portal adds tools.</p>
<h3 id="code-mode-policies">Code Mode policies</h3>
<p>Each portal has a Code Mode policy. The default policy is <em>Opt-in</em>.</p>
<table>
<thead>
<tr>
<th>Policy</th>
<th>API value</th>
<th>Default behavior</th>
<th>Client override</th>
</tr>
</thead>
<tbody>
<tr>
<td>Off</td>
<td><code>off</code></td>
<td>Code Mode is unavailable</td>
<td>Query parameters are ignored</td>
</tr>
<tr>
<td>Opt-in</td>
<td><code>opt_in</code></td>
<td>Code Mode is off</td>
<td>Add <code>?codemode=search_and_execute</code> to turn it on</td>
</tr>
<tr>
<td>On by default</td>
<td><code>default_on</code></td>
<td>Code Mode is on</td>
<td>Add <code>?codemode=off</code> to turn it off</td>
</tr>
<tr>
<td>Enforced</td>
<td><code>enforced</code></td>
<td>Code Mode is on</td>
<td>Query parameters are ignored</td>
</tr>
</tbody>
</table>
<p>Use <em>Opt-in</em> or <em>On by default</em> if some clients run their own Code Mode implementation. These policies let clients avoid nested code execution.</p>
<h3 id="upstream-servers-with-code-mode-turned-on">Upstream servers with Code Mode turned on</h3>
<p>MCP portals do not support upstream MCP servers that have their own Code Mode turned on. When adding a server to your portal, connect to a version of the server that returns its full tool list. If the upstream server runs its own Code Mode, use the server's opt-out mechanism if available. Alternatively, consider turning off Code Mode on your MCP portal.</p>
<h3 id="configure-a-code-mode-policy">Configure a Code Mode policy</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4724.md")
</div>
<p>The <code>allow_code_mode</code> API field is deprecated. Use <code>code_mode</code> for new integrations.</p>
<h3 id="connect-with-code-mode">Connect with Code Mode</h3>
<p>The portal policy determines whether the MCP client needs a query parameter. For <em>Opt-in</em>, append <code>?codemode=search_and_execute</code> to the portal URL. For <em>On by default</em>, clients can append <code>?codemode=off</code> instead.</p>
<p>For example, an <em>Opt-in</em> portal at <code>https://&lt;subdomain&gt;.&lt;domain&gt;/mcp</code> uses this URL:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For MCP clients with server configuration files, use the portal URL with the query string parameter:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;example-portal&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;mcp-remote@latest&quot;,&#10;				&quot;https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>When Code Mode is active, the portal advertises <code>portal_codemode_search</code> and <code>portal_codemode_execute</code>. The AI agent can discover tools and compose multiple tool calls in one execution.</p>
<p>For more information on building with Code Mode, refer to the <a href="/agents/tools/codemode/api-reference/">Code Mode SDK reference</a>.</p>
<h2 id="route-portal-traffic-through-gateway">Route portal traffic through Gateway</h2>
<p>When Gateway routing is turned on, calls to MCP servers protected by your MCP server portal are routed through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This makes portal traffic appear in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a> alongside the rest of your organization's HTTP traffic. You can then create <a href="#example-gateway-policy">Data Loss Prevention (DLP) policies</a> to detect and block sensitive data from being sent to your upstream MCP servers.</p>
<h3 id="how-gateway-routing-works">How Gateway routing works</h3>
<p>When a user calls a tool through the portal, the portal proxies the request to the upstream MCP server. With Gateway routing turned on, this outbound request passes through Cloudflare Gateway before reaching the upstream server. Gateway inspects the traffic and applies any matching HTTP policies, including DLP scanning.</p>
<p>Because portal traffic routes through Gateway, it also respects <a href="/cloudflare-one/traffic-policies/egress-policies/">Gateway egress policies</a>. This means outbound requests to upstream MCP servers will originate from your dedicated egress IPs or Gateway IP ranges rather than generic Cloudflare IPs. If your upstream MCP servers restrict inbound traffic by source IP (for example, to a VPN or corporate IP range), you can use egress policies to ensure portal traffic comes from a predictable set of IPs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4711.md")
</aside>
<h3 id="tls-decryption">TLS decryption</h3>
<p>DLP inspection requires Gateway to decrypt TLS traffic. For portal traffic, Gateway decrypts and inspects the payload automatically — you do not need to turn on the account-level <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> setting. Because the portal terminates the connection from the MCP client and re-originates the request through Gateway, Gateway decrypts portal traffic regardless of whether the global TLS decryption setting is on.</p>
<p>This automatic decryption applies only to traffic that flows through the portal. To inspect MCP traffic that does not pass through the portal — for example, an agent on a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">device running the WARP client</a> connecting directly to an upstream MCP server — you must turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> as you would for any other <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4710.md")
</aside>
<h3 id="supported-transports">Supported transports</h3>
<p>Gateway routing supports <a href="https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http">Streamable HTTP</a> connections only. If an upstream MCP server is configured with a Server-Sent Events (SSE) endpoint (a URL ending in <code>/sse</code>), the portal will automatically attempt to connect using Streamable HTTP instead. If the upstream server does not support Streamable HTTP, the connection will fail when Gateway routing is turned on.</p>
<h3 id="enable-gateway-routing">Enable Gateway routing</h3>
<p>You can route every server in a portal through Gateway or turn on routing for individual servers. If Gateway routing is enabled on the portal, it applies to every server in that portal regardless of the server-level setting.</p>
<h4 id="route-every-server-in-a-portal">Route every server in a portal</h4>
<p>To route traffic from every MCP server in a portal through Gateway:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Find the portal you want to configure, then select the three dots &gt; <strong>Edit</strong>.</li>
<li>Under <strong>Basic information</strong>, turn on <strong>Route traffic through Cloudflare Gateway</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h4 id="route-an-individual-server">Route an individual server</h4>
<p>To route traffic from one MCP server through Gateway without enabling Gateway routing for the entire portal:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>AI controls</strong>.</li>
<li>Go to the <strong>MCP servers</strong> tab.</li>
<li>Find the server you want to configure, then select the three dots &gt; <strong>Edit</strong>.</li>
<li>Under <strong>Basic information</strong>, turn on <strong>Route traffic through Cloudflare Gateway</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The API field for the server-level setting is <code>secure_web_gateway</code>. It defaults to <code>false</code>.</p>
<p>Portal traffic will now appear in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a>. To apply DLP scanning, <a href="#example-gateway-policy">create a Gateway HTTP policy</a>.</p>
<h3 id="example-gateway-policy">Example Gateway policy</h3>
<p>To scan traffic for sensitive data, <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">create a Gateway HTTP policy</a> that matches both the MCP server and a predefined or custom <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profile</a>.</p>
<p>Gateway HTTP policies for MCP portal traffic must explicitly target the upstream MCP server. Ensure that your policy matches the upstream MCP server hostname (for example, <code>example-mcp-server.example.workers.dev</code>) rather than the portal URL (<code>&lt;subdomain&gt;.&lt;domain&gt;</code>).</p>
<p>For example, the following policy blocks traffic that contains <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#credentials-and-secrets">credentials and secrets</a> or <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#financial-information">financial information</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>in</td>
<td><code>example-mcp-server.example.workers.dev</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Credentials and Secrets</em>, <em>Financial Information</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="what-happens-when-a-request-is-blocked">What happens when a request is blocked</h3>
<p>When a tool call matches a Block DLP policy, Gateway blocks it and the portal surfaces the block to the MCP client as an error rather than completing the tool call. This applies in both directions:</p>
<ul>
<li><strong>Tool call requests</strong>: If the data the agent sends to a tool matches a DLP profile, Gateway blocks the outbound request and the agent receives an error indicating the request was blocked.</li>
<li><strong>Tool call responses</strong>: If the data the upstream server returns matches a DLP profile, Gateway blocks the response and the portal returns an error instead of the matched content.</li>
</ul>
<p>The agent can retry the request, but it will continue to be blocked until the content no longer matches the policy.</p>
<h3 id="limitations">Limitations</h3>
<ul>
<li>DLP <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#ai-prompt">AI prompt profiles</a> do not apply to MCP server portal traffic. AI prompt profiles are designed for specific web client API paths and do not match the MCP protocol format. Use standard DLP profiles instead.</li>
<li>SSE transport is not supported through Gateway. If your upstream MCP server only supports SSE, Gateway routing will not work for that server.</li>
<li>Background synchronization of tools and prompts does not route through Gateway. Only real-time user requests are inspected.</li>
</ul>
<h2 id="connect-to-a-portal">Connect to a portal</h2>
<p>Users can connect to your MCP server running at <code>https://&lt;subdomain&gt;.&lt;domain&gt;/mcp</code> using <a href="https://playground.ai.cloudflare.com/">Workers AI Playground</a>, <a href="https://github.com/modelcontextprotocol/inspector">MCP inspector</a>, or <a href="/agents/model-context-protocol/guides/remote-mcp-server/#connect-your-mcp-server-to-claude-and-other-mcp-clients">other MCP clients</a> that support remote MCP servers.</p>
<p>To test in Workers AI Playground:</p>
<ol>
<li>Go to <a href="https://playground.ai.cloudflare.com/">Workers AI Playground</a>.</li>
<li>Under <strong>MCP Servers</strong>, enter <code>https://&lt;subdomain&gt;.&lt;domain&gt;/mcp</code> for the portal URL.</li>
<li>Select <strong>Connect</strong>.</li>
<li>In the popup window, log in to your Cloudflare Access identity provider.</li>
<li>The popup window will list the MCP servers in the portal that require authentication. For each of these MCP servers, select <strong>Connect</strong> and follow the login prompts.</li>
<li>Select <strong>Done</strong> to complete the portal authentication process.</li>
</ol>
<p>Workers AI Playground will show a <strong>Connected</strong> status and list the available tools. You can now ask the AI model to complete a task using an available tool. Requests made to an MCP server will appear in your <a href="#view-portal-logs">portal logs</a>.</p>
<p>For MCP clients with server configuration files, we recommend using the <code>npx</code> command with the <code>mcp-remote@latest</code> argument:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;example-mcp-server&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;mcp-remote@latest&quot;,&#10;				&quot;https://&lt;subdomain&gt;.&lt;domain&gt;.com/mcp&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>We do not recommend using the <code>serverURL</code> parameter since it may cause issues with portal session creation and management.</p>
<h3 id="portal-homepage">Portal homepage</h3>
<p>When users visit the portal domain (<code>https://&lt;subdomain&gt;.&lt;domain&gt;/</code>) in a browser, the portal displays a homepage with connection details and setup instructions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4709.md")
</aside>
<p>The homepage shows:</p>
<ul>
<li>The portal name and your organization branding (if configured in Cloudflare Access)</li>
<li>The MCP endpoint URL with a copy button</li>
<li>Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients with OS-specific file paths</li>
</ul>
<p>Authenticated users see their email address and a <strong>Sign out</strong> button in the session bar. Users who are not authenticated can still view the homepage and connection instructions.</p>
<h3 id="sign-out-of-a-portal">Sign out of a portal</h3>
<p>To end a portal session, select <strong>Sign out</strong> from the <a href="#portal-homepage">portal homepage</a> (<code>https://&lt;subdomain&gt;.&lt;domain&gt;/</code>). The sign-out flow:</p>
<ol>
<li>Revokes all portal-level OAuth grants for your user.</li>
<li>Deletes all upstream MCP server OAuth states associated with your session.</li>
<li>Redirects through Cloudflare Access logout.</li>
</ol>
<p>After sign-out, the portal displays a confirmation page with a summary of the revoked sessions. To reconnect, visit the portal homepage and authenticate again.</p>
<h3 id="connect-with-a-service-token">Connect with a service token</h3>
<p>You can connect to an MCP portal using an <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a> for machine-to-machine access. Service tokens bypass the browser-based OAuth flow and authenticate using the <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers.</p>
<p>A service token session is authorized twice: once at the portal URL, and once for each upstream MCP server it tries to reach through the portal. Both checks need a matching <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth policy</a>.</p>
<h4 id="required-configuration">Required configuration</h4>
<table>
<thead>
<tr>
<th>Where</th>
<th>Policy action</th>
<th>Include rule</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>Portal Access application</td>
<td>Service Auth</td>
<td>Your service token</td>
<td>Lets the bot connect to the portal URL.</td>
</tr>
<tr>
<td>Each linked MCP server Access app</td>
<td>Service Auth</td>
<td>Your service token</td>
<td>Lets the bot see and call that server's tools through the portal.</td>
</tr>
<tr>
<td>Server's portal mapping</td>
<td>n/a</td>
<td>n/a</td>
<td><strong>Require user auth</strong> must be <strong>off</strong> so the portal uses the admin credential.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4708.md")
</aside>
<p>If a linked MCP server does not have a Service Auth policy matching the token, that server is hidden from the bot's tool list.</p>
<h4 id="set-up-a-service-token-connection">Set up a service token connection</h4>
<ol>
<li><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#create-a-service-token">Create a service token</a> in your Zero Trust account.</li>
<li>Open the portal's Access application and add a Service Auth policy that includes the service token.</li>
<li>For each upstream MCP server you want the bot to reach:
<ol>
<li>Open the server's Access application and add a Service Auth policy that includes the same service token.</li>
<li>Open the portal and edit the server. Turn <strong>Require user auth</strong> off so the portal uses the <a href="#reauthenticate-the-mcp-server">admin credential</a> for that server.</li>
</ol>
</li>
<li>Connect from your MCP client with the service token headers.</li>
</ol>
<p>For a CLI client, set the headers directly:</p>
<pre><code class="language-sh">curl https://&lt;subdomain&gt;.&lt;domain&gt;/mcp \&#10;  &#45;H &quot;CF-Access-Client-Id: &lt;CLIENT_ID&gt;&quot; \&#10;  &#45;H &quot;CF-Access-Client-Secret: &lt;CLIENT_SECRET&gt;&quot;&#10;</code></pre>
<p>For <code>mcp-remote</code>, pass the headers with <code>--header</code>:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;example-portal&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;mcp-remote@latest&quot;,&#10;				&quot;https://&lt;subdomain&gt;.&lt;domain&gt;/mcp&quot;,&#10;				&quot;--header&quot;,&#10;				&quot;CF-Access-Client-Id: &lt;CLIENT_ID&gt;&quot;,&#10;				&quot;--header&quot;,&#10;				&quot;CF-Access-Client-Secret: &lt;CLIENT_SECRET&gt;&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4707.md")
</aside>
<h3 id="device-authentication">Device authentication</h3>
<p>MCP server portals require a browser-based authentication flow. <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Device authentication</a> (picking up identity from the Cloudflare One Client without a browser redirect) is not currently supported for MCP portals. Users must complete the Access login flow in a browser when first connecting.</p>
<h2 id="optimize-context">Optimize context</h2>
<p>MCP server portals support context optimization options that reduce how many tokens tool definitions consume in the model's context window. These options are useful when a portal aggregates many MCP servers or servers that expose a large number of tools.</p>
<p>To use context optimization, append the <code>optimize_context</code> query parameter to your portal URL when connecting from an MCP client.</p>
<h3 id="minimize-tools">Minimize tools</h3>
<p>The <code>minimize_tools</code> option strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special <code>query</code> tool that agents use to search and retrieve full tool definitions on demand. Agents can discover tools without loading all definitions upfront.</p>
<p>This option provides up to 5x savings in token usage, though querying tool definitions before use adds a small amount of overhead.</p>
<p>To connect with <code>minimize_tools</code>, use the following portal URL:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&#10;</code></pre>
<p>For MCP clients with server configuration files:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;example-portal&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;mcp-remote@latest&quot;,&#10;				&quot;https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="search-and-execute">Search and execute</h3>
<p>The <code>search_and_execute</code> option hides all upstream tools and exposes only two tools to the agent: <code>query</code> and <code>execute</code>. The <code>query</code> tool searches and retrieves tool definitions. The <code>execute</code> tool runs the upstream tools. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, which keeps authentication credentials and environment variables out of the model context.</p>
<p>This option reduces the initial token cost of portal tools to a small constant, regardless of how many tools are available. However, the agent becomes fully reliant on <code>query</code> to discover tools before it can call them.</p>
<p>To connect with <code>search_and_execute</code>, use the following portal URL:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&#10;</code></pre>
<p>For MCP clients with server configuration files:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;example-portal&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;mcp-remote@latest&quot;,&#10;				&quot;https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For more information on the Code Mode pattern behind <code>search_and_execute</code>, refer to <a href="/agents/tools/codemode/">Code Mode</a>.</p>
<h2 id="manage-portal-sessions">Manage portal sessions</h2>
<p>Once connected to a portal, users can manage their upstream MCP server sessions without leaving their MCP client. The portal uses <a href="https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation">MCP elicitations</a> to provide a server selection page where you can enable or disable servers, log out of individual servers, and reauthenticate.</p>
<h3 id="return-to-the-server-selection-page">Return to the server selection page</h3>
<p>To manage your server connections during an active session, ask your AI agent to take you back to the server selection page. For example, prompt your agent with:</p>
<blockquote>
<p>Take me back to the server selection page.</p>
</blockquote>
<p>The portal returns an authorization URL. Open this URL in your web browser to access the server selection page:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/authorize?elicitationId=&lt;ELICITATION_ID&gt;&#10;</code></pre>
<p>From this page you can:</p>
<ul>
<li><strong>Enable or disable servers</strong> — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.</li>
<li><strong>Log out and reauthenticate</strong> — Log out of a server and log back in if you need to change which data the server has access to. For example, you may need to reauthenticate with different permissions.</li>
</ul>
<h3 id="enable-or-disable-a-server-inline">Enable or disable a server inline</h3>
<p>You can also enable or disable a specific server directly from your MCP client without visiting the server selection page. For example:</p>
<blockquote>
<p>Enable the wiki server.</p>
</blockquote>
<blockquote>
<p>Disable my Jira server.</p>
</blockquote>
<p>The portal toggles the server and updates the active tool list immediately. Disabling a server removes its tools from the session, which reduces context window usage.</p>
<h3 id="reauthenticate-a-server">Reauthenticate a server</h3>
<p>When an upstream MCP server token expires, the portal prompts you to reauthenticate from within your MCP client. Open the provided URL in your browser and complete the login to restore the session.</p>
<p>If your MCP client does not display the reauthentication prompt, you can manually clear cached credentials:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4706.md")
</aside>
<pre><code class="language-sh">rm -rf ~/.mcp-auth&#10;</code></pre>
<p>After clearing credentials, reconnect to the portal from your MCP client.</p>
<h3 id="authorize-new-servers">Authorize new servers</h3>
<p>When an admin adds a new upstream MCP server to a portal, the portal automatically prompts connected users to authorize the new server. The portal batches admin changes and redirects you to the authorization flow once, rather than interrupting for each individual server update.</p>
<h2 id="view-portal-logs">View portal logs</h2>
<p>Portal logs allow you to monitor user activity through an MCP server portal. You can view logs on a per-portal or per-server basis.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>MCP Portals</strong>.</li>
<li>Find the portal or server that you want to view logs for, then select the three dots &gt; <strong>Edit</strong>.</li>
<li>Select <strong>Logs</strong>.</li>
</ol>
<h3 id="log-fields">Log fields</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Time</td>
<td>Date and time of the request</td>
</tr>
<tr>
<td>Status</td>
<td>Whether the server successfully returned a response</td>
</tr>
<tr>
<td>Server</td>
<td>Name of the MCP server that handled the request</td>
</tr>
<tr>
<td>Capability</td>
<td>The tool used to process the request</td>
</tr>
<tr>
<td>Duration</td>
<td>Processing time for the request in milliseconds</td>
</tr>
</tbody>
</table>
<h3 id="export-logs-with-logpush">Export logs with Logpush</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4705.md")
</aside>
<p>You can automatically export MCP portal logs to third-party storage destinations or security information and event management (SIEM) tools using <a href="/logs/logpush/">Logpush</a>. This allows you to integrate with your existing security workflows and retain logs for as long as your business requires.</p>
<p>To set up a Logpush job for MCP portal logs, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>. For a list of available log fields, refer to <a href="/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/">MCP portal logs</a>.</p>
<h2 id="known-limitations">Known limitations</h2>
<p>MCP server portals have the following known limitations:</p>
<ul>
<li><strong>Only remote HTTP MCP servers are supported.</strong> MCP servers that use <a href="https://modelcontextprotocol.io/specification/2025-11-25/basic/transports">stdio transport only</a> (for example, <code>github/github-mcp-server</code>) do not expose a remote HTTP endpoint and cannot be added to an MCP server portal. To use a stdio-only server, you must self-host it behind an HTTP endpoint and authenticate with a <a href="#create-an-mcp-server">bearer token or custom headers</a>.</li>
<li><strong>Some MCP servers block proxy-based clients.</strong> Certain MCP servers reject requests from proxy-based clients like MCP server portals, returning a <code>403</code> error on the registration endpoint. These servers are not compatible with MCP server portals until those providers add Cloudflare as a supported MCP client.</li>
<li><strong>Manual OAuth capabilities are captured during the first user authorization.</strong> Servers configured with <a href="#configure-manual-oauth-credentials">manual OAuth credentials</a> remain in <strong>Waiting</strong> status until a user completes upstream OAuth. Cloudflare stores the tools and prompts returned during that connection. Background and manual capability synchronization do not refresh them.</li>
<li><strong>Admin OAuth tokens can expire silently.</strong> The admin credential used to <a href="#reauthenticate-the-mcp-server">authenticate an MCP server</a> is subject to the upstream provider's token expiration policy. When the token expires, the server status changes to <strong>Error</strong> or <strong>Sync Required</strong> and the server will not appear in the portal for end users. Admins are not notified when this happens. Periodically check the <a href="#server-status">server status</a> and <a href="#reauthenticate-the-mcp-server">reauthenticate</a> servers that show an error.</li>
<li><strong>Each portal supports up to 80 MCP servers.</strong></li>
</ul>
<h2 id="policy-limitations">Policy limitations</h2>
<p>MCP servers use a dedicated Access application type (<em>mcp</em>) that does not support the following Access policy features when the server is authorized through a portal.</p>
<ul>
<li><strong><a href="/cloudflare-one/access-controls/policies/mfa-requirements/#independent-mfa">Independent MFA</a></strong> — Users will not be prompted to perform MFA through Cloudflare Access when authorizing a server, regardless of whether MFA global enforcement is enabled or whether an MFA policy is assigned to the server.</li>
<li><strong><a href="/cloudflare-one/access-controls/policies/require-purpose-justification/">Purpose justification</a></strong> — Users will not be prompted to provide a purpose justification when authorizing a server.</li>
<li><strong><a href="/cloudflare-one/access-controls/policies/temporary-auth/">Temporary authentication</a></strong> — Users will not be prompted to request access and approvers will not receive approval requests when a user authorizes a server.</li>
</ul>
<p>These limitations only apply to servers that are being authorized through a portal. Access policy selectors such as Emails, Groups, Country, and Device Posture Checks will be enforced.</p>
<p>Independent MFA, purpose justification, and temporary authentication will be enforced for servers that are not authorized through a portal.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="after-authenticating-to-the-portal-my-user-receives-the-error-no-allowed-servers-available-check-your-zero-trust-policies">After authenticating to the portal, my user receives the error <code>No allowed servers available, check your Zero Trust Policies</code>.</h3>
<ol>
<li>An MCP portal and server must both have an attached Access policy. Ensure that all MCP servers assigned to the portal have their own associated policy.</li>
<li>The server's admin authentication may be expired. Check that the <a href="#server-status">server's status</a> is <strong>Ready</strong>. If the status shows <strong>Error</strong> or <strong>Sync Required</strong>, <a href="#reauthenticate-the-mcp-server">reauthenticate the server</a>.</li>
</ol>
<h3 id="the-portal-url-does-not-prompt-for-authentication-when-it-is-added-to-an-mcp-client">The portal URL does not prompt for authentication when it is added to an MCP client.</h3>
<ol>
<li>Verify that the portal has an assigned Access policy.</li>
<li>Verify that the portal URL does not have any applied <a href="/workers/configuration/routing/custom-domains/">Workers</a>, <a href="/rules/page-rules/manage/">Page Rules</a>, <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostname</a> definitions, or any other configuration that may interfere with its ability to connect to the MCP client.</li>
</ol>
<h3 id="the-portal-returns-a-522-error">The portal returns a <code>522</code> error.</h3>
<p>A <code>522</code> error indicates that Cloudflare cannot reach the portal's origin. This typically means the DNS record for the portal hostname is missing or misconfigured.</p>
<ol>
<li>Verify that a CNAME record exists for your portal subdomain pointing to <code>gateway.agents.cloudflare.com</code>.</li>
<li>Ensure the CNAME record has <strong>Proxy status</strong> turned on in Cloudflare DNS.</li>
<li>If you created the portal using the <a href="#manage-portals-via-api">API</a> or the <a href="#configure-via-terraform">Terraform provider</a>, you must create the DNS record separately. Unlike the dashboard, the API and Terraform provider do not auto-create DNS records.</li>
</ol>
<h3 id="an-mcp-server-is-stuck-in-waiting-status">An MCP server is stuck in <code>Waiting</code> status.</h3>
<p>The <code>Waiting</code> status means Cloudflare is attempting to connect to the upstream MCP server and fetch its tools and prompts. If the server stays in this status:</p>
<ol>
<li>Verify that the upstream MCP server URL is correct and the server is reachable.</li>
<li>Check that the upstream server supports <a href="https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http">Streamable HTTP</a> or SSE transport. The portal will attempt multiple connection strategies automatically.</li>
<li>If the server requires authentication, verify that the admin credentials are valid by <a href="#reauthenticate-the-mcp-server">reauthenticating the server</a>.</li>
<li>Select the three dots &gt; <strong>Sync capabilities</strong> to manually retry the connection.</li>
</ol>
<h3 id="an-mcp-server-shows-stale-status">An MCP server shows <code>Stale</code> status.</h3>
<p>A <code>Stale</code> status means the admin credential for the server could not be refreshed during the last synchronization attempt. The server's tools may still work for users who have their own OAuth tokens (servers with <strong>Require user auth</strong> turned on), but the admin credential needs to be refreshed.</p>
<p>To resolve this, <a href="#reauthenticate-the-mcp-server">reauthenticate the server</a> with valid admin credentials.</p>
<h3 id="tool-calls-fail-with-an-unauthorized-error">Tool calls fail with an <code>unauthorized</code> error.</h3>
<ol>
<li>If the server uses per-user OAuth (<strong>Require user auth</strong> is turned on), the user's OAuth token may have expired. Ask the user to <a href="#reauthenticate-a-server">reauthenticate the server</a> from their MCP client.</li>
<li>If the server uses admin credentials, check the <a href="#server-status">server status</a>. A status of <strong>Error</strong> or <strong>Sync Required</strong> indicates the admin credential needs to be refreshed.</li>
<li>If the user recently changed permissions on the upstream service (for example, revoked OAuth scopes), they will need to reauthenticate.</li>
</ol>
<h3 id="oauth-authentication-fails-with-a-redirect-uri-error-when-connecting-to-an-upstream-mcp-server">OAuth authentication fails with a redirect URI error when connecting to an upstream MCP server.</h3>
<p>Errors such as <code>invalid_redirect_uri</code>, <code>invalid_client_metadata</code>, or <code>Redirect URI not allowed</code> indicate that the upstream MCP server rejected the callback URL that the portal registered during the OAuth flow. Refer to <a href="#upstream-oauth-callback-url">Upstream OAuth callback URL</a> for background on how the callback URL is determined.</p>
<ol>
<li>By default, the upstream provider must allowlist <code>https://&lt;your-portal-hostname&gt;/servers-callback</code> as a redirect URI (for example, <code>https://my-portal.example.com/servers-callback</code>). OAuth providers typically exact-match the full URI including path. Contact the upstream MCP server vendor if you do not control the allowlist.</li>
<li>If the portal is configured to use the <a href="#shared-cloudflare-callback-url-opt-in">shared Cloudflare callback URL</a>, the upstream provider must instead allowlist <code>https://oauth-callbacks.cloudflareaccess.com/cdn-cgi/access/outbound-oauth-callback</code>.</li>
</ol>
<h3 id="tool-calls-fail-when-gateway-routing-is-turned-on">Tool calls fail when Gateway routing is turned on.</h3>
<ol>
<li>Verify that the upstream MCP server supports Streamable HTTP transport. SSE transport is not supported through Gateway.</li>
<li>If the upstream server URL ends in <code>/sse</code>, the portal automatically attempts to connect using Streamable HTTP on a <code>/mcp</code> path instead. If the server does not support this, the connection will fail.</li>
<li>Check <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a> for DLP block events. If a DLP policy is blocking the traffic, the portal returns an error to the MCP client with the DLP rule ID.</li>
</ol>
<h3 id="users-cannot-connect-with-mcp-remote-or-similar-tools">Users cannot connect with <code>mcp-remote</code> or similar tools.</h3>
<ol>
<li>Ensure you are using the latest version of <code>mcp-remote</code>. Run <code>npx -y mcp-remote@latest</code> to update.</li>
<li>Use the <code>command</code> and <code>args</code> format in your MCP client configuration, not the <code>serverURL</code> parameter. The <code>serverURL</code> parameter may cause issues with portal session creation.</li>
<li>If authentication fails repeatedly, clear cached credentials by running <code>rm -rf ~/.mcp-auth</code> and reconnecting.</li>
</ol>
<h3 id="the-portal-homepage-shows-the-wrong-name-or-domain">The portal homepage shows the wrong name or domain.</h3>
<p>The portal homepage displays your Access organization name and branding. If the displayed name is incorrect:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Settings</strong> &gt; <strong>General</strong> &gt; <strong>Team name</strong>.</li>
<li>Update your team name. The change will take effect the next time a user visits the portal homepage.</li>
</ol>
