---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/access/2/
  description: '2026-04-23'
  full_title: access changelog - page 2 | Cloudflare Docs
  head_html: <title>access changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-23"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/access/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="access changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-23"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/access/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/access/2/#page","headline":"access changelog - page 2 | Cloudflare Docs","description":"2026-04-23","url":"https://developers.cloudflare.com/changelog/product/access/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/access/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="aaguid-restrictions-and-amr-matching-for-access-independent-mfa"><a href="/changelog/post/2026-04-23-independent-mfa-aaguid-amr/">AAGUID restrictions and AMR matching for Access independent MFA</a></h2>
<p><em>2026-04-23</em></p>
<p><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a> in Cloudflare Access now supports two additional organization-level controls:</p>
<ul>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid">Restrict authenticators by AAGUID</a></strong> — Limit enrollment to a specific set of WebAuthn authenticators using their <a href="https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid">AAGUID</a>. This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new <a href="/cloudflare-one/reusable-components/lists/">List</a> type.</li>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa">AMR matching</a></strong> — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the <code>amr</code> claim defined in <a href="https://datatracker.ietf.org/doc/html/rfc8176">RFC 8176</a> and matches supported values such as <code>hwk</code>, <code>otp</code>, and <code>fpt</code> to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>


<h2 id="homepage-and-sign-out-for-mcp-server-portals"><a href="/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/">Homepage and sign-out for MCP server portals</a></h2>
<p><em>2026-04-17</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> display a homepage when users visit the portal domain in a browser.</p>
<p><img src="/assets/upstream/images/changelog/access/portals-homepage-disconnected.png" alt="MCP server portal homepage showing connection status and setup instructions" /></p>
<p>The homepage shows:</p>
<ul>
<li>The portal name and organization branding</li>
<li>The MCP endpoint URL with a copy button</li>
<li>Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients</li>
</ul>
<p>Authenticated users see their email address and a <strong>Sign out</strong> button. Selecting <strong>Sign out</strong> revokes all portal-level OAuth grants, deletes upstream server OAuth states, and redirects through Cloudflare Access logout. A confirmation page shows a summary of the revoked sessions.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#portal-homepage">MCP server portals</a>.</p>


<h2 id="independent-mfa-for-access-applications"><a href="/changelog/post/2026-04-15-independent-mfa/">Independent MFA for Access applications</a></h2>
<p><em>2026-04-15</em></p>
<p>Cloudflare Access now supports independent multi-factor authentication (MFA), allowing you to enforce MFA requirements without relying on your identity provider (IdP). With per-application and per-policy configuration, you can enforce stricter authentication methods like hardware security keys on sensitive applications without requiring them across your entire organization. This reduces the risk of MFA fatigue for your broader user population while adding additional security where it matters most.</p>
<p>This feature also addresses common gaps in IdP-based MFA, such as inconsistent MFA policies across different identity providers or the need for additional security layers beyond what the IdP provides.</p>
<p>Independent MFA supports the following authenticator types:</p>
<ul>
<li><strong>Authenticator application</strong> — Time-based one-time passwords (TOTP) using apps like Google Authenticator, Microsoft Authenticator, or Authy.</li>
<li><strong>Security key</strong> — Hardware security keys such as YubiKeys.</li>
<li><strong>Biometrics</strong> — Built-in device authenticators including Apple Touch ID, Apple Face ID, and Windows Hello.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17620.md")</aside>
<h4 id="2026-04-15-independent-mfa-configuration-levels">Configuration levels</h4>
<p>You can configure MFA requirements at three levels:</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Organization</strong></td>
<td>Enforce MFA by default for all applications in your account.</td>
</tr>
<tr>
<td><strong>Application</strong></td>
<td>Require or turn off MFA for a specific application.</td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>Require or turn off MFA for users who match a specific policy.</td>
</tr>
</tbody>
</table>
<p>Settings at lower levels (policy) override settings at higher levels (organization), giving you granular control over MFA enforcement.</p>
<h4 id="2026-04-15-independent-mfa-user-enrollment">User enrollment</h4>
<p>Users enroll their authenticators through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. To help with onboarding, administrators can share a direct enrollment link: <code>&lt;your-team-name&gt;.cloudflareaccess.com/AddMfaDevice</code>.</p>
<p>To get started with Independent MFA, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>


<h2 id="session-management-for-mcp-server-portals"><a href="/changelog/post/2026-04-02-mcp-portal-session-management/">Session management for MCP server portals</a></h2>
<p><em>2026-04-02</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.</p>
<p>To return to the server selection page, ask your AI agent with a prompt like &quot;take me back to the server selection page.&quot; The portal responds with an authorization URL via <a href="https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation">MCP elicitation</a> that you open in your browser:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/authorize?elicitationId=&lt;ELICITATION_ID&gt;&#10;</code></pre>
<p>From the server selection page you can:</p>
<ul>
<li><strong>Enable or disable servers</strong> — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.</li>
<li><strong>Log out and reauthenticate</strong> — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.</li>
</ul>
<p>Users can also enable or disable a server inline by asking their AI agent directly, for example &quot;enable the wiki server&quot; or &quot;disable my Jira server.&quot;</p>
<p>The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal">managed OAuth</a>.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions">Manage portal sessions</a>.</p>


<h2 id="logs-ui-refresh"><a href="/changelog/post/2026-04-01-logs-ui-refresh/">Logs UI refresh</a></h2>
<p><em>2026-04-01</em></p>
<p>Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-new-logs-ui.png" alt="Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options" /></p>
<p>The updated UI includes:</p>
<ul>
<li><strong>Filter by field</strong> - Select any field value to add it as a filter and narrow down your results.</li>
<li><strong>Customizable fields</strong> - Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.</li>
<li><strong>View details</strong> - Select a timestamp to view the full details of a log entry.</li>
<li><strong>Switch to classic view</strong> - Return to the previous log viewer interface if needed.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</p>


<h2 id="code-mode-for-mcp-server-portals"><a href="/changelog/post/2026-03-26-mcp-portal-code-mode/">Code Mode for MCP server portals</a></h2>
<p><em>2026-03-26</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>, a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.</p>
<p>To turn it off, edit the portal in <strong>Access controls</strong> &gt; <strong>AI controls</strong> and turn off <strong>Code Mode</strong> under <strong>Basic information</strong>.</p>
<p>When Code Mode is active, the portal exposes a single <code>code</code> tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods for each upstream tool. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, keeping authentication credentials and environment variables out of the model context.</p>
<p>To use Code Mode, append <code>?codemode=search_and_execute</code> to your portal URL when connecting from an MCP client:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode">Code Mode</a>.</p>


<h2 id="context-optimization-for-mcp-server-portals"><a href="/changelog/post/2026-03-26-mcp-portal-context-optimization/">Context optimization for MCP server portals</a></h2>
<p><em>2026-03-26</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the <code>optimize_context</code> query parameter to the portal URL.</p>
<h4 id="2026-03-26-mcp-portal-context-optimization-minimize-tools"><code>minimize_tools</code></h4>
<p>Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special <code>query</code> tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&#10;</code></pre>
<h4 id="2026-03-26-mcp-portal-context-optimization-search-and-execute"><code>search_and_execute</code></h4>
<p>Hides all upstream tools and exposes only two tools: <code>query</code> and <code>execute</code>. The <code>query</code> tool searches and retrieves tool definitions. The <code>execute</code> tool runs the upstream tools in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context">Optimize context</a>.</p>


<h2 id="managed-oauth-for-cloudflare-access"><a href="/changelog/post/2026-03-20-managed-oauth/">Managed OAuth for Cloudflare Access</a></h2>
<p><em>2026-03-20</em></p>
<p>Cloudflare Access supports managed OAuth, which allows non-browser clients — such as CLIs, AI agents, SDKs, and scripts — to authenticate with Access-protected applications using a standard OAuth 2.0 authorization code flow.</p>
<p>Previously, non-browser clients that attempted to access a protected application received a <code>302</code> redirect to a login page they could not complete. The established workaround was <code>cloudflared access curl</code>, which required installing additional tooling.</p>
<p>With managed OAuth, clients instead receive a <code>401</code> response with a <code>WWW-Authenticate</code> header that points to Access's OAuth discovery endpoints (<a href="https://datatracker.ietf.org/doc/html/rfc8414">RFC 8414</a> and <a href="https://datatracker.ietf.org/doc/html/rfc9728">RFC 9728</a>). The client opens the end user's browser to the Access login page. The end user authenticates with their identity provider, and the client receives an OAuth access token for subsequent requests.</p>
<p>Access enforces the same policies as a browser login; the OAuth layer is a new transport mechanism, not a separate authentication path.</p>
<p>Managed OAuth can be enabled on any self-hosted Access application or <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a>. It is opt-in for existing applications to avoid interfering with those that run their own OAuth servers and rely on their own <code>WWW-Authenticate</code> headers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17618.md")</aside>
<p>To enable managed OAuth, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>, edit the application, and turn on <strong>Managed OAuth</strong> under <strong>Advanced settings</strong>.</p>
<p>You can also enable it via the API by setting <code>oauth_configuration.enabled</code> to <code>true</code> on the <a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/">Access applications endpoint</a>.</p>
<p><img src="/assets/upstream/images/changelog/access/managed-oauth.png" alt="Managed OAuth settings in the Cloudflare dashboard" /></p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">Enable managed OAuth</a>.</p>


<h2 id="route-mcp-server-portal-traffic-through-cloudflare-gateway"><a href="/changelog/post/2026-03-20-mcp-portal-gateway-routing/">Route MCP server portal traffic through Cloudflare Gateway</a></h2>
<p><em>2026-03-20</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now route traffic through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for richer HTTP request logging and data loss prevention (DLP) scanning.</p>
<p>When Gateway routing is turned on, portal traffic appears in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a>. You can create <a href="/cloudflare-one/traffic-policies/">Gateway HTTP policies</a> with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to detect and block sensitive data sent to upstream MCP servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17619.md")</aside>
<p>To enable Gateway routing, go to <strong>Access controls</strong> &gt; <strong>AI controls</strong>, edit the portal, and turn on <strong>Route traffic through Cloudflare Gateway</strong> under <strong>Basic information</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-route-through-gateway.png" alt="Route MCP server portal traffic through Cloudflare Gateway" /></p>
<p>For more details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway">Route traffic through Gateway</a>.</p>


<h2 id="user-risk-score-selector-in-access-policies"><a href="/changelog/post/2026-03-04-user-risk-score-access-policies/">User risk score selector in Access policies</a></h2>
<p><em>2026-03-04</em></p>
<p>You can now use <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. The new <strong>User Risk Score</strong> selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.</p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies">Use risk scores in Access policies</a>.</p>


<h2 id="clipboard-controls-for-browser-based-rdp"><a href="/changelog/post/2026-03-01-rdp-clipboard-controls/">Clipboard controls for browser-based RDP</a></h2>
<p><em>2026-03-01</em></p>
<p>You can now configure clipboard controls for browser-based RDP with Cloudflare Access. Clipboard controls allow administrators to restrict whether users can copy or paste text between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-clipboard-controls.png" alt="Enable users to copy and paste content from their local machine to remote RDP sessions in the Cloudflare One dashboard" /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting clipboard access, you can prevent sensitive data from being transferred out of the remote session to a user's personal device.</p>
<h4 id="2026-03-01-rdp-clipboard-controls-configuration-options">Configuration options</h4>
<p>Clipboard controls are configured per policy within your Access application. For each policy, you can independently allow or deny:</p>
<ul>
<li><strong>Copy from local client to remote RDP session</strong> — Users can copy/paste text from their local machine into the browser-based RDP session.</li>
<li><strong>Copy from remote RDP session to local client</strong> — Users can copy/paste text from the browser-based RDP session to their local machine.</li>
</ul>
<p>By default, both directions are denied for new policies. For existing Access applications created before this feature was available, clipboard access remains enabled to preserve backwards compatibility.</p>
<p>When a user attempts a restricted clipboard action, the clipboard content is replaced with an error message informing them that the action is not allowed.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#clipboard-controls">Clipboard controls for browser-based RDP</a>.</p>


<h2 id="export-mcp-server-portal-logs-with-logpush"><a href="/changelog/post/2026-02-27-mcp-portal-logpush/">Export MCP server portal logs with Logpush</a></h2>
<p><em>2026-02-27</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-02-27-mcp-portal-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17617.md")</aside>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now supports <a href="/logs/logpush/">Logpush</a> integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.</p>
<h4 id="2026-02-27-mcp-portal-logpush-available-log-fields">Available log fields</h4>
<p>The MCP server portal logs dataset includes fields such as:</p>
<ul>
<li><code>Datetime</code> — Timestamp of the request</li>
<li><code>PortalID</code> / <code>PortalAUD</code> — Portal identifiers</li>
<li><code>ServerID</code> / <code>ServerURL</code> — Upstream MCP server details</li>
<li><code>Method</code> — JSON-RPC method (for example, <code>tools/call</code>, <code>prompts/get</code>, <code>resources/read</code>)</li>
<li><code>ToolCallName</code> / <code>PromptGetName</code> / <code>ResourceReadURI</code> — Method-specific identifiers</li>
<li><code>UserID</code> / <code>UserEmail</code> — Authenticated user information</li>
<li><code>Success</code> / <code>Error</code> — Request outcome</li>
<li><code>ServerResponseDurationMs</code> — Response time from upstream server</li>
</ul>
<p>For the complete field reference, refer to <a href="/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/">MCP portal logs</a>.</p>
<h4 id="2026-02-27-mcp-portal-logpush-set-up-logpush">Set up Logpush</h4>
<p>To configure Logpush for MCP server portal logs, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17616.md")</aside>


<h2 id="streamlined-clientless-browser-isolation-for-private-applications"><a href="/changelog/post/2026-02-17-clientless-access-for-private-apps/">Streamlined clientless browser isolation for private applications</a></h2>
<p><em>2026-02-17</em></p>
<p>A new <strong>Allow clientless access</strong> setting makes it easier to connect users without a device client to internal applications, without using public DNS.</p>
<p><img src="/assets/upstream/images/changelog/access/allow-clientless-access.png" alt="Allow clientless access setting in the Cloudflare One dashboard" /></p>
<p>Previously, to provide clientless access to a private hostname or IP without a <a href="/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route">published application</a>, you had to create a separate <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark application</a> pointing to a prefixed <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> URL (for example, <code>https://&lt;your-teamname&gt;.cloudflareaccess.com/browser/https://10.0.0.1/</code>). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.</p>
<p>Now, you can manage clientless access directly within your <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private self-hosted application</a>. When  <strong>Allow clientless access</strong> is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">remote browser permissions</a> to open the link.</p>


<h2 id="policies-for-bookmark-applications"><a href="/changelog/post/2026-02-17-policies-for-bookmarks/">Policies for bookmark applications</a></h2>
<p><em>2026-02-17</em></p>
<p>You can now assign <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark applications</a>. This lets you control which users see a bookmark in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> based on identity, device posture, and other policy rules.</p>
<p>Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:</p>
<ul>
<li><strong>Tailor the App Launcher to each user</strong> — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.</li>
<li><strong>Restrict visibility of sensitive bookmarks</strong> — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.</li>
</ul>
<p>Bookmarks support all <a href="/cloudflare-one/access-controls/policies/">Access policy configurations</a> except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/bookmarks/">Add bookmarks</a>.</p>


<h2 id="fine-grained-permissions-for-access-policies-and-service-tokens"><a href="/changelog/post/2026-02-13-access-policy-service-token-permissions/">Fine-grained permissions for Access policies and service tokens</a></h2>
<p><em>2026-02-13</em></p>
<p>Fine-grained permissions for <strong>Access policies</strong> and <strong>Access service tokens</strong> are available. These new resource-scoped roles expand the existing RBAC model, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2026-02-13-access-policy-service-token-permissions-new-roles">New roles</h4>
<ul>
<li><strong>Cloudflare Access policy admin</strong>: Can edit a specific <a href="/cloudflare-one/access-controls/policies/">Access policy</a> in an account.</li>
<li><strong>Cloudflare Access service token admin</strong>: Can edit a specific <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a> in an account.</li>
</ul>
<p>These roles complement the existing resource-scoped roles for Access applications, identity providers, and infrastructure targets.</p>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a></li>
<li><a href="/fundamentals/manage-members/scope/">Role scopes</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17729.md")</aside>


<h2 id="require-access-protection-for-zones"><a href="/changelog/post/2026-01-22-deny-by-default-for-zones/">Require Access protection for zones</a></h2>
<p><em>2026-01-22</em></p>
<p>You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.</p>
<p><img src="/assets/upstream/images/changelog/access/require-cloudflare-access-protection.png" alt="Require Cloudflare Access protection in the dashboard" /></p>
<h4 id="2026-01-22-deny-by-default-for-zones-how-it-works">How it works</h4>
<ul>
<li><strong>Blocked by default</strong>: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.</li>
<li><strong>Explicit access required</strong>: To allow traffic, create an Access application with an Allow or Bypass policy.</li>
<li><strong>Hostname exemptions</strong>: You can exempt specific hostnames from this requirement.</li>
</ul>
<p>To turn on this feature, refer to <a href="/cloudflare-one/access-controls/access-settings/require-access-protection/">Require Access protection</a>.</p>


<h2 id="new-granular-api-token-permissions-for-cloudflare-access"><a href="/changelog/post/2026-01-22-granular-api-token-permissions/">New granular API token permissions for Cloudflare Access</a></h2>
<p><em>2026-01-22</em></p>
<p>Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:</p>
<ul>
<li><strong>Access: Organizations Revoke</strong> — Grants the ability to <a href="/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions">revoke user sessions</a> in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.</li>
<li><strong>Access: Population Read</strong> — Grants read access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.</li>
<li><strong>Access: Population Write</strong> — Grants write access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.</li>
</ul>
<p>These permissions are scoped at the account level and can be combined with existing Access permissions.</p>
<p>For a full list of available permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>


<h2 id="cloudflare-admin-activity-logs-capture-creation-of-dns-over-http-doh-users"><a href="/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/">Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users</a></h2>
<p><em>2026-01-08</em></p>
<p>Cloudflare <a href="/cloudflare-one/insights/logs/">admin activity logs</a> now capture each time a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTP (DoH) user</a> is created.</p>
<p>These logs can be viewed from the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, pulled via the <a href="/api/">Cloudflare API</a>, and exported through <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>


<h2 id="generate-cloudflare-access-ssh-certificate-authority-ca-directly-from-the-cloudflare-dashboard"><a href="/changelog/post/2025-11-14-SSH-CA-enhancements/">Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard</a></h2>
<p><em>2025-11-14</em></p>
<p>SSH with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Cloudflare Access for Infrastructure</a> allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.</p>
<p>Previously, users had to generate this certificate by using the <a href="https://developers.cloudflare.com/api/">Cloudflare API</a> directly. With this update, you can now create and manage this certificate in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a> from the <strong>Access controls</strong> &gt; <strong>Service credentials</strong> page.</p>
<p><img src="/assets/upstream/images/changelog/access/SSH-CA-generation.png" alt="Navigate to Access controls and then Service credentials to see where you can generate an SSH CA" /></p>
<p>For more details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca">Generate a Cloudflare SSH CA</a>.</p>


<h2 id="access-private-hostname-applications-support-all-ports-protocols"><a href="/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/">Access private hostname applications support all ports/protocols</a></h2>
<p><em>2025-10-28</em></p>
<p><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Cloudflare Access for private hostname applications</a> can now secure traffic on all ports and protocols.</p>
<p>Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port <code>443</code> and support Server Name Indicator (SNI).</p>
<p>This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.</p>
<p><img src="/assets/upstream/images/changelog/access/internal_private_app_any_port.png" alt="Example private application on non-443 port" /></p>
<p>For example, you can now create a self-hosted application in Access for <code>ssh.testapp.local</code> running on port <code>22</code>. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.</p>
<p>This feature is generally available across all plans.</p>


<h2 id="fine-grained-permissioning-for-access-for-apps-idps-targets-now-in-public-beta"><a href="/changelog/post/2025-10-01-fine-grained-permissioning-beta/">Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta</a></h2>
<p><em>2025-10-02</em></p>
<p>Fine-grained permissions for <strong>Access Applications, Identity Providers (IdPs), and Targets</strong> is now available in Public Beta. This expands our RBAC model beyond account &amp; zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2025-10-01-fine-grained-permissioning-beta-what-s-new">What's New</h4>
- **[Access Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
- **[Identity Providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
- **[Targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-01-fine-grained-permissioning-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17728.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/">Get started with Cloudflare Permissioning</a></li>
<li><a href="/fundamentals/manage-members/manage">Manage Member Permissioning via the UI &amp; API</a></li>
</ul>


<h2 id="access-remote-desktop-protocol-rdp-destinations-securely-from-your-browser-now-generally-available"><a href="/changelog/post/2025-09-22-browser-based-rdp-ga/">Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</a></h2>
<p><em>2025-09-22</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>Since we announced our <a href="/changelog/access/#2025-06-30">open beta</a>, we've made a few improvements:</p>
<ul>
<li>Support for targets with IPv6.</li>
<li>Support for <a href="/cloudflare-wan/">Magic WAN</a> and <a href="/mesh/">WARP Connector</a> as on-ramps.</li>
<li>More robust error messaging on the login page to help you if you encounter an issue.</li>
<li>Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.</li>
<li>Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.</li>
</ul>
<p>As a refresher, here are some benefits browser-based RDP provides:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browser-based RDP Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>


<h2 id="manage-and-restrict-access-to-internal-mcp-servers-with-cloudflare-access"><a href="/changelog/post/2025-08-26-access-mcp-oauth/">Manage and restrict access to internal MCP servers with Cloudflare Access</a></h2>
<p><em>2025-08-26</em></p>
<p>You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<p><a href="/cloudflare-one/access-controls/ai-controls/linked-apps/">Self-hosted applications</a> in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.</p>
<p>For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog post</a> on the Cloudflare Blog.</p>


<h2 id="mcp-server-portals"><a href="/changelog/post/2025-08-26-mcp-server-portals/">MCP server portals</a></h2>
<p><em>2025-08-26</em></p>
<p><img src="/assets/upstream/images/changelog/access/mcp-server-portal.png" alt="MCP server portal" /></p>
<p>An <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:</p>
<ul>
<li><strong>Streamlined access to multiple MCP servers</strong>: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.</li>
<li><strong>Customized tools per portal</strong>: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.</li>
<li><strong>Observability</strong>: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.</li>
</ul>
<p>This is available in an open beta for all customers across all plans! For more information check out our <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog</a> for this release.</p>


<h2 id="sftp-support-for-ssh-with-cloudflare-access-for-infrastructure"><a href="/changelog/post/2025-08-15-sftp/">SFTP support for SSH with Cloudflare Access for Infrastructure</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Cloudflare Access for Infrastructure</a> now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/access/">Previous</a><span>Page 2 of 3</span><a class="pagination-next" rel="next" href="/changelog/product/access/3/">Next</a></nav>
