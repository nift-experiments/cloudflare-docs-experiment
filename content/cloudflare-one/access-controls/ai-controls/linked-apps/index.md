<p>MCP servers often need to call internal applications on behalf of authenticated users. For example, an MCP server that helps employees interact with internal tools needs to forward the user's identity to those downstream services (the internal applications the MCP server connects to) so that each request is authorized with the correct permissions.</p>
<p>The <a href="/cloudflare-one/access-controls/applications/linked-app-token/">Linked App Token</a> policy selector enables this by allowing an Access policy on one application to accept tokens issued for another. There are two ways to set this up depending on how your MCP server is deployed.</p>
<h2 id="self-hosted-mcp-server-recommended">Self-hosted MCP server (recommended)</h2>
<p>If your MCP server is a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access application</a>, Cloudflare Access handles authentication automatically. The MCP server receives the user's JWT from Access in the <code>Cf-Access-Jwt-Assertion</code> header and should forward it to downstream applications in the <code>Cf-Access-Token</code> header. No OAuth implementation is needed in your MCP server code.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Self-hosted MCP server accessing internal applications&#10;    User --&gt; client[&quot;MCP client&quot;]&#10;    client --&gt; mcp[&quot;MCP server &lt;br&gt; (self-hosted app)&quot;]&#10;    mcp -- &quot;Cf-Access-Token: &amp;lt;JWT&amp;gt;&quot; --&gt; app1[&quot;Internal API &lt;br&gt; (self-hosted app)&quot;]&#10;    mcp -- &quot;Cf-Access-Token: &amp;lt;JWT&amp;gt;&quot; --&gt; app2[&quot;Company wiki &lt;br&gt; (self-hosted app)&quot;]&#10;    idp[Identity provider] &lt;--&gt; mcp&#10;</code></pre>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Add your downstream applications (for example, your <code>Internal API</code> and <code>Company wiki</code>) as <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access applications</a>.</li>
<li>Add your MCP server as a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access application</a>.</li>
</ul>
<h3 id="1-configure-downstream-applications"><ol>
<li>Configure downstream applications</li>
</ol></h3>
<p>On each self-hosted application that the MCP server needs to access (for example, the <code>Internal API</code> and <code>Company wiki</code> apps), create a Linked App Token policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4731.md")
</div></div>
<h3 id="2-configure-your-mcp-server"><ol start="2">
<li>Configure your MCP server</li>
</ol></h3>
<p>In your MCP server code, forward the <code>Cf-Access-Jwt-Assertion</code> header from incoming requests as the <code>Cf-Access-Token</code> header on outgoing requests to the downstream application:</p>
<pre><code class="language-txt">Cf-Access-Token: &lt;JWT from Cf-Access-Jwt-Assertion&gt;&#10;</code></pre>
<p>Access will now validate the JWT token against the Linked App Token rule and propagate the user's identity to the downstream application.</p>
<h2 id="saas-mcp-server-access-for-saas-with-oauth">SaaS MCP server (Access for SaaS with OAuth)</h2>
<p>If your MCP server is registered as an <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/">Access for SaaS OIDC application</a> and implements <a href="https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization">MCP OAuth</a>, it receives an OAuth <code>access_token</code> from Cloudflare Access. The MCP server forwards this token to downstream self-hosted applications in the <code>Authorization: Bearer</code> header.</p>
<p>This approach requires your MCP server to implement the OAuth authorization code flow. Use the <a href="#self-hosted-mcp-server-recommended">self-hosted MCP server approach</a> if you want Cloudflare to handle authentication for you.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: SaaS MCP server accessing internal applications&#10;    User --&gt; client[&quot;MCP client&quot;]&#10;    client --&gt; mcp[&quot;MCP server &lt;br&gt; (Access for SaaS app)&quot;]&#10;    mcp -- &quot;Authorization: Bearer &amp;lt;token&amp;gt;&quot; --&gt; app1[&quot;Internal API &lt;br&gt; (self-hosted app)&quot;]&#10;    mcp -- &quot;Authorization: Bearer &amp;lt;token&amp;gt;&quot; --&gt; app2[&quot;Company wiki &lt;br&gt; (self-hosted app)&quot;]&#10;    idp[Identity provider] &lt;--&gt; mcp&#10;</code></pre>
<h3 id="prerequisites-1">Prerequisites</h3>
<ul>
<li>Add your downstream applications (for example, your <code>Internal API</code> and <code>Company wiki</code>) as <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access applications</a>.</li>
<li>Add your MCP server as an <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/#saas-managed-third-party-mcp-server">Access for SaaS OIDC application</a>.</li>
</ul>
<h3 id="1-configure-downstream-applications-1"><ol>
<li>Configure downstream applications</li>
</ol></h3>
<p>On each self-hosted application that the MCP server needs to access (for example, the <code>Internal API</code> and <code>Company wiki</code> apps), create a Linked App Token policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4734.md")
</div></div>
<h3 id="2-configure-your-mcp-server-1"><ol start="2">
<li>Configure your MCP server</li>
</ol></h3>
<p>Configure the MCP server to forward the <code>access_token</code> in outgoing requests:</p>
<pre><code class="language-txt">Authorization: Bearer ACCESS_TOKEN&#10;</code></pre>
<h2 id="known-limitations">Known limitations</h2>
<ul>
<li>The Linked App Token policy can only be added to <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted applications</a>. It cannot be added to <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">SaaS applications</a> or other application types.</li>
<li>This feature works best with applications that rely on the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">Cloudflare Access JWT</a> for authentication and identity. If the downstream application implements its own authentication layer after Cloudflare Access, requests that pass Access validation may still be rejected by the application itself.</li>
<li>When the upstream application uses <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">Managed OAuth</a>, the client receives an <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#token-format">opaque access token</a>, not a JWT. The client cannot forward this token directly to downstream applications as a <code>Cf-Access-Token</code> header. Instead, the upstream application's origin must read the <code>Cf-Access-Jwt-Assertion</code> header (which contains the resolved JWT) and forward it as <code>Cf-Access-Token</code> to the downstream application. If you want clients to access multiple endpoints without a proxy, consider using a <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#multi-domain-applications">multi-domain Access application</a> instead.</li>
</ul>
