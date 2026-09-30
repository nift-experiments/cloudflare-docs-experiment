---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/changelog/access/
  description: Review recent changes to Cloudflare Access.
  full_title: Access Changelog · Cloudflare One docs
  head_html: <title>Access Changelog · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/changelog/access/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/changelog/access/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/cloudflare-one/changelog/access/index.xml"><meta property="og:title" content="Access Changelog · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/changelog/access/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/cloudflare-one/changelog/access/#page","headline":"Access Changelog \u00b7 Cloudflare One docs","description":"Review recent changes to Cloudflare Access.","url":"https://developers.cloudflare.com/cloudflare-one/changelog/access/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/changelog/access/
  schema: 1
---
<h2 id="2026-09-15">2026-09-15</h2>

<strong>Access for Infrastructure now supports tagged targets and tag-based target criteria</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now integrates with <a href="/resource-tagging/">Resource Tagging</a>. You can attach key-value tags to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target">infrastructure targets</a> and use them in access policies.</p>
<p>You can manage tags on targets inline when you create or edit a target or through the central <a href="/resource-tagging/how-to/manage-tags/">Resource Tagging API</a>. Cloudflare keeps tags in sync across both methods.</p>
<p>Infrastructure applications also support a target criteria model with <code>include</code>, <code>require</code>, and <code>exclude</code> operators. Each operator can match targets by hostname, tag, or both.</p>
<ul>
<li><strong>Include</strong> matches targets that have any of the specified values.</li>
<li><strong>Require</strong> matches targets that have all of the specified values.</li>
<li><strong>Exclude</strong> rejects targets that have any of the specified values.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/access/tags-in-infra-app.png" alt="Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Add an infrastructure application</a>.</p>


<h2 id="2026-09-14">2026-09-14</h2>

<strong>Require fresh authentication for SAML identity providers</strong>

<p>Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on <strong>Require reauthentication</strong> in the Cloudflare dashboard, or set <code>force_authn</code> to <code>true</code> through the API. Access will then set <code>ForceAuthn</code> to <code>true</code> in signed and unsigned SAML authentication requests.</p>
<p>This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is <code>false</code>.</p>
<p>For configuration details, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider">Require fresh authentication at the identity provider</a>.</p>


<h2 id="2026-08-26">2026-08-26</h2>

<strong>Access service token secrets use a scannable format</strong>

<p>Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format <code>cfast_[40 alphanumeric characters][8-character checksum]</code>. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.</p>
<p>Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> authentication headers.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a>.</p>


<h2 id="2026-08-25">2026-08-25</h2>

<strong>Grace periods for service token rotation</strong>

<p>Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.</p>
<p>The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets">Rotate service token secrets</a>.</p>


<h2 id="2026-08-25-1">2026-08-25</h2>

<strong>Temporarily turn off Access service tokens</strong>

<p>Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.</p>
<p>Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off">Turn a service token on or off</a>.</p>


<h2 id="2026-08-25-2">2026-08-25</h2>

<strong>MCP server portals support MCP 2026-07-28 specification</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support the stateless MCP <code>2026-07-28</code> specification for client and upstream server connections.</p>
<p>The portal's <code>/mcp</code> endpoint automatically accepts stateless MCP <code>2026-07-28</code> requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP <code>2026-07-28</code> support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.</p>
<p>SSE connections continue to use the legacy protocol. For details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport">MCP server portal transport and protocol compatibility</a>.</p>


<h2 id="2026-08-19">2026-08-19</h2>

<strong>Access resource lists now support resource-scoped roles</strong>

<p>Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.</p>
<p>The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned <code>403</code> responses.</p>
<p>For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.</p>
<p>For role definitions and assignment details, refer to <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a> and <a href="/fundamentals/manage-members/scope/">Role scopes</a>.</p>


<h2 id="2026-08-14">2026-08-14</h2>

<strong>You can now enable Access on a Worker or all Workers at once</strong>

<p>You now have two new ways to protect your <a href="/workers/">Workers</a> with <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p><strong>Protect an application across all its domains at once</strong></p>
<p>Until now, if a Worker was reachable on a route, a Custom Domain, and a <code>workers.dev</code> URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.</p>
<p>Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-one-worker.png" alt="Access setting for protecting a single Worker" /></p>
<p><strong>Protect all new and existing Workers by default</strong></p>
<p>Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-all-workers.png" alt="Account-wide Access setting that protects all Workers" /></p>
<p>If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.</p>
<p><img src="/assets/upstream/images/changelog/workers/make-worker-public.png" alt="Make a Worker public when all Workers are protected" /></p>
<p>Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.</p>
<p>For more advanced policy options, edit the policy in <a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Zero Trust</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/choose-who-can-sign-in.png" alt="Access policy configuration for controlling who can sign in" /></p>
<p><strong>View all of your Worker Access policies</strong></p>
<p>You can view and manage all of your Access policies in the <strong>Access</strong> tab of the Workers &amp; Pages section in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/access-policies.png" alt="Access tab showing all configured Access policies" /></p>
<p><strong>See who is accessing your Worker</strong></p>
<p>When Access is enabled on your Worker, every authenticated request includes <code>ctx.access</code>. Call <a href="/workers/runtime-apis/context/#access"><code>ctx.access.getIdentity()</code></a> to get the user's email, name, and groups — no manual JWT validation required.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    if (!ctx.access) {&#10;      return new Response(&quot;Access did not run&quot;, { status: 401 });&#10;    }&#10;&#10;    const identity = await ctx.access.getIdentity();&#10;    return Response.json({ aud: ctx.access.aud, email: identity?.email });&#10;  },&#10;};&#10;</code></pre>
<p><strong>Test Access locally</strong></p>
<p>You can now test Cloudflare Access locally with <code>wrangler dev</code>. Add a <code>dev</code> block to your <code>wrangler.jsonc</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;access&quot;: {&#10;    &quot;dev&quot;: {&#10;      &quot;aud&quot;: &quot;my-app&quot;,&#10;      &quot;identity&quot;: { &quot;email&quot;: &quot;admin@example.com&quot; }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Your Worker will receive this identity through <code>ctx.access</code> and <code>ctx.access.getIdentity()</code>, letting you test authenticated and unauthenticated flows without deploying. Remove the <code>dev</code> block to simulate unauthenticated requests.</p>
<p><strong>API and programmatic access</strong></p>
<p>You can also set up these policies through the <a href="/workers/configuration/cloudflare-access/">Workers API</a> instead of the dashboard.</p>


<h2 id="2026-08-12">2026-08-12</h2>

<strong>Independent MFA supports FIDO2 for infrastructure applications</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Infrastructure</a> applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow <code>ssh_fido2_key</code>, <code>piv_key</code>, or both in application-level and policy-level MFA settings.</p>
<p>Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps">Enroll a FIDO2 key for infrastructure apps</a> and <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Configure MFA for infrastructure applications</a>.</p>


<h2 id="2026-08-05">2026-08-05</h2>

<strong>Identity-aware controls are now available in AI Gateway</strong>

<p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>


<h2 id="2026-08-03">2026-08-03</h2>

<strong>Control authorization cookies for multi-domain Access applications</strong>

<p>Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.</p>
<p>Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.</p>
<p>The new <strong>Eager redirect cookie</strong> setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a <code>CF_Authorization</code> cookie. This supports applications that need to make requests across hostnames before the user visits each one.</p>
<p>For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.</p>
<p>To configure the setting, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie">Authorization cookie</a>.</p>


<h2 id="2026-07-31">2026-07-31</h2>

<strong>Static OAuth client credentials for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.</p>
<p>When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the <code>client_secret_post</code> and <code>client_secret_basic</code> token endpoint authentication methods.</p>
<p>Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials">Configure manual OAuth credentials</a>.</p>


<h2 id="2026-07-30">2026-07-30</h2>

<strong>Admins can turn on Code Mode by default for MCP portal users</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now support four Code Mode policies: <em>Off</em>, <em>Opt-in</em>, <em>On by default</em>, and <em>Enforced</em>. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.</p>
<p>Existing portals retain their current behavior. Portals that previously allowed Code Mode use <em>Opt-in</em>, while portals that did not allow Code Mode use <em>Off</em>. New portals also use <em>Opt-in</em> by default.</p>
<p>Clients turn on Code Mode for an <em>Opt-in</em> portal with <code>?codemode=search_and_execute</code>. The <em>On by default</em> policy lets clients opt out with <code>?codemode=off</code>, which avoids nested code execution when a client runs its own Code Mode implementation. The <em>Off</em> and <em>Enforced</em> policies ignore client overrides.</p>
<p>The Cloudflare API exposes these policies through the <code>code_mode</code> field:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;code_mode&quot;: &quot;default_on&quot;&#10;}&#10;</code></pre>
<p>The supported values are <code>off</code>, <code>opt_in</code>, <code>default_on</code>, and <code>enforced</code>. The previous <code>allow_code_mode</code> boolean is deprecated.</p>
<p>For configuration details and client behavior, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies">Code Mode policies</a>.</p>


<h2 id="2026-07-20">2026-07-20</h2>

<strong>Browser-based login for plaintext HTTP private applications</strong>

<p>Cloudflare Access now uses the standard browser-based login flow for <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a> served over plaintext HTTP on port <code>80</code>.</p>
<p>Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an <code>Authentication required</code> pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> on success.</p>
<p>This brings the HTTP experience in line with HTTPS apps (with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">Gateway TLS decryption</a> turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.</p>
<p>Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.</p>


<h2 id="2026-07-16">2026-07-16</h2>

<strong>Bulk print PDFs for browser-based RDP</strong>

<p>Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select <strong>Print all PDFs</strong> in the clipboard panel. The files are combined into one PDF and sent to your local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-bulk-print.png" alt="The clipboard panel showing the Print all PDFs option for multiple selected PDF files." /></p>
<p>Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs">Print PDFs for browser-based RDP</a>.</p>


<h2 id="2026-07-07">2026-07-07</h2>

<strong>File transfer controls for browser-based RDP (beta)</strong>

<p>You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/file-transfer-policy-control.png" alt="File transfer connection settings in the Access policy configuration." /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-configuration-options">Configuration options</h4>
<p>File transfer controls are configured per policy within your Access application, alongside existing <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings">text clipboard controls</a>. For each policy, you can select one of the following options:</p>
<ul>
<li><strong>Client to remote RDP session allowed</strong> — Users can upload files from their local machine into the browser-based RDP session.</li>
<li><strong>Remote RDP session to client allowed</strong> — Users can download files from the browser-based RDP session to their local machine.</li>
<li><strong>Both directions allowed</strong> — Users can upload and download files between their local machine and the browser-based RDP session.</li>
<li><strong>Disable copying/pasting</strong> — Users are not allowed to transfer files between their local machine and the browser-based RDP session.</li>
</ul>
<p>By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-how-it-works">How it works</h4>
<p>To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/clipboard-side-panel.png" alt="The clipboard side panel showing files available for transfer." /></p>
<p><img src="/assets/upstream/images/changelog/access/remote-doc-ready-for-download-or-print-local.png" alt="A remote document ready for download or local printing." /></p>
<p>This feature is in beta and available on all Zero Trust plans. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files">File transfer for browser-based RDP</a>.</p>


<h2 id="2026-07-01">2026-07-01</h2>

<strong>Fix redirect URL fragment encoding for single-page applications</strong>

<p>Access now correctly preserves URL fragment characters (<code>/</code>, <code>?</code>, <code>=</code>, <code>&amp;</code>, <code>;</code>) when redirecting users back to an application after login. Previously, these characters were encoded with <code>encodeURIComponent</code>, which mangled fragment-based routes used by single-page applications (SPAs).</p>
<p>For example, an SPA URL like <code>https://app.example.com/#/dashboard?tab=settings&amp;view=advanced</code> would previously redirect to a broken URL after login. This is now handled correctly.</p>
<p>If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.</p>


<h2 id="2026-07-01-1">2026-07-01</h2>

<strong>Independent MFA for infrastructure applications</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.</p>
<p>With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, <code>root</code>) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-enrollment">Enrollment</h4>
<p>Users enroll their YubiKey PIV key through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. For enrollment instructions and SSH client setup, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps">Enroll a PIV key for infrastructure apps</a>.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-configuration">Configuration</h4>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Enforce MFA for infrastructure applications</a>.</p>


<h2 id="2026-06-26">2026-06-26</h2>

<strong>Service token support for MCP server portals</strong>

<p>You can now connect autonomous agents and bots to an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> using an <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a>. Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.</p>
<p>To set this up:</p>
<ul>
<li>Add a <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth policy</a> that matches your service token to the portal's Access application.</li>
<li>Add a Service Auth policy that matches the same token to each linked MCP server's Access application.</li>
<li>Turn <strong>Require user auth</strong> off (<code>on_behalf: false</code>) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.</li>
</ul>
<p>The bot connects with <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.</p>
<p>For step-by-step setup, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token">Connect with a service token</a>.</p>


<h2 id="2026-06-18">2026-06-18</h2>

<strong>Cloudflare identity provider is now the default for new accounts</strong>

<p>When you create a new Zero Trust organization, Cloudflare now adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method. Previously, new organizations started with <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a>.</p>
<p>With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> whenever you need to.</p>
<p>This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.</p>


<h2 id="2026-06-04">2026-06-04</h2>

<strong>Share identity providers across accounts with IdP federation</strong>

<p>Cloudflare Access now supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which allows organizations to share a single identity provider across multiple Cloudflare accounts.</p>
<p>Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>One IdP, many accounts</strong> — Configure your IdP once and share it with all accounts in your organization.</li>
<li><strong>Lifecycle management</strong> — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.</li>
<li><strong>Immutable recipient connections</strong> — IdP connections in recipient accounts cannot be accidentally modified or deleted.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>.</p>


<h2 id="2026-06-03">2026-06-03</h2>

<strong>SAML assertion encryption for identity providers</strong>

<p>Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.</p>
<p>Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-encryption.png" alt="SAML encryption toggle in the identity provider configuration" /></p>
<p>SAML encryption includes built-in certificate lifecycle management:</p>
<ul>
<li><strong>Automatic certificate generation</strong>: Access generates an encryption certificate when you turn on SAML encryption for an identity provider.</li>
<li><strong>Certificate rotation</strong>: Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.</li>
<li><strong>PEM export</strong>: Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions">Encrypt SAML assertions</a>.</p>


<h2 id="2026-05-28">2026-05-28</h2>

<strong>Tool and prompt aliases for MCP server portals</strong>

<p>When you connect third-party MCP servers through <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a>, you have no control over how the server author named tools or wrote descriptions. Unclear names make it harder for AI agents to select the right tool and harder for users to understand what is available.</p>
<p>You can now <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">rename tools and prompts</a> and rewrite their descriptions directly on the portal, without modifying the upstream server. For example, a tool named <code>super_cool_tool</code> can become <code>search_customer_records</code> with a description tailored to your organization.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-edit-tool-modal.png" alt="Edit tool modal showing name and description fields for an MCP server tool" /></p>
<p>Modified tools display a <strong>Modified</strong> label in the tools list so administrators can see which tools have been customized at a glance.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-tools-authorized-modified.png" alt="Tools authorized list showing a modified label on a renamed tool" /></p>
<p>Aliases override the metadata that MCP clients receive. You can set them at two levels:</p>
<ul>
<li><strong>Per portal</strong>: Applies only within a specific portal. Takes precedence over server-level aliases.</li>
<li><strong>Per server</strong>: Applies across all portals that use the server.</li>
</ul>
<p>You can reset an alias at any time to restore the original upstream name.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">Tool and prompt aliases</a>.</p>


<h2 id="2026-05-19">2026-05-19</h2>

<strong>Cloudflare as identity provider and account membership selector</strong>

<p>Cloudflare Access now supports using Cloudflare itself as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a>. If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.</p>
<p>Cloudflare is now the <strong>default identity provider for all newly created Zero Trust accounts</strong>, replacing One-time PIN.</p>
<p>This also enables two new capabilities:</p>
<ul>
<li><strong>Cloudflare Account Member selector</strong> — A new <a href="/cloudflare-one/access-controls/policies/#cloudflare-access-selectors">policy selector</a> that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.</li>
<li><strong>Restrict to account members</strong> — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.</li>
</ul>
<p>To get started, add Cloudflare as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a> in your Zero Trust settings.</p>


<h2 id="2026-05-12">2026-05-12</h2>

<strong>Refreshed Access login page</strong>

<p>The <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">Access login page</a> and <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time password (OTP)</a> page now feature a refreshed design that improves visual consistency, user trust, and mobile responsiveness.</p>
<p><strong>Before:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-old.png" alt="Screenshot of the previous Access login page" /></p>
<p><strong>After:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-new.png" alt="Screenshot of the updated Access login page" /></p>
<p>The updated login experience includes:</p>
<ul>
<li><strong>Unified authentication card</strong> - All sign-in options (identity provider buttons, email input, OTP) now appear in a single card with consistent styling, replacing the previous multi-section layout.</li>
<li><strong>Consistent button styling</strong> - Identity provider buttons use a uniform size and layout for easier scanning and selection.</li>
<li><strong>Better mobile experience</strong> - Responsive layout improvements ensure the login page renders correctly on phones and tablets.</li>
<li><strong>Dark mode support</strong> - The login page now supports dark mode.</li>
</ul>


<h2 id="2026-04-23">2026-04-23</h2>

<strong>AAGUID restrictions and AMR matching for Access independent MFA</strong>

<p><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a> in Cloudflare Access now supports two additional organization-level controls:</p>
<ul>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid">Restrict authenticators by AAGUID</a></strong> — Limit enrollment to a specific set of WebAuthn authenticators using their <a href="https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid">AAGUID</a>. This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new <a href="/cloudflare-one/reusable-components/lists/">List</a> type.</li>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa">AMR matching</a></strong> — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the <code>amr</code> claim defined in <a href="https://datatracker.ietf.org/doc/html/rfc8176">RFC 8176</a> and matches supported values such as <code>hwk</code>, <code>otp</code>, and <code>fpt</code> to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>


<h2 id="2026-04-17">2026-04-17</h2>

<strong>Homepage and sign-out for MCP server portals</strong>

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


<h2 id="2026-04-15">2026-04-15</h2>

<strong>Independent MFA for Access applications</strong>

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


<h2 id="2026-04-02">2026-04-02</h2>

<strong>Session management for MCP server portals</strong>

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


<h2 id="2026-04-01">2026-04-01</h2>

<strong>Logs UI refresh</strong>

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


<h2 id="2026-03-26">2026-03-26</h2>

<strong>Code Mode for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>, a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.</p>
<p>To turn it off, edit the portal in <strong>Access controls</strong> &gt; <strong>AI controls</strong> and turn off <strong>Code Mode</strong> under <strong>Basic information</strong>.</p>
<p>When Code Mode is active, the portal exposes a single <code>code</code> tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods for each upstream tool. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, keeping authentication credentials and environment variables out of the model context.</p>
<p>To use Code Mode, append <code>?codemode=search_and_execute</code> to your portal URL when connecting from an MCP client:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode">Code Mode</a>.</p>


<h2 id="2026-03-26-1">2026-03-26</h2>

<strong>Context optimization for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the <code>optimize_context</code> query parameter to the portal URL.</p>
<h4 id="2026-03-26-mcp-portal-context-optimization-minimize-tools"><code>minimize_tools</code></h4>
<p>Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special <code>query</code> tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&#10;</code></pre>
<h4 id="2026-03-26-mcp-portal-context-optimization-search-and-execute"><code>search_and_execute</code></h4>
<p>Hides all upstream tools and exposes only two tools: <code>query</code> and <code>execute</code>. The <code>query</code> tool searches and retrieves tool definitions. The <code>execute</code> tool runs the upstream tools in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context">Optimize context</a>.</p>


<h2 id="2026-03-20">2026-03-20</h2>

<strong>Managed OAuth for Cloudflare Access</strong>

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


<h2 id="2026-03-20-1">2026-03-20</h2>

<strong>Route MCP server portal traffic through Cloudflare Gateway</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now route traffic through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for richer HTTP request logging and data loss prevention (DLP) scanning.</p>
<p>When Gateway routing is turned on, portal traffic appears in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a>. You can create <a href="/cloudflare-one/traffic-policies/">Gateway HTTP policies</a> with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to detect and block sensitive data sent to upstream MCP servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17619.md")</aside>
<p>To enable Gateway routing, go to <strong>Access controls</strong> &gt; <strong>AI controls</strong>, edit the portal, and turn on <strong>Route traffic through Cloudflare Gateway</strong> under <strong>Basic information</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-route-through-gateway.png" alt="Route MCP server portal traffic through Cloudflare Gateway" /></p>
<p>For more details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway">Route traffic through Gateway</a>.</p>


<h2 id="2026-03-04">2026-03-04</h2>

<strong>User risk score selector in Access policies</strong>

<p>You can now use <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. The new <strong>User Risk Score</strong> selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.</p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies">Use risk scores in Access policies</a>.</p>


<h2 id="2026-03-01">2026-03-01</h2>

<strong>Clipboard controls for browser-based RDP</strong>

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


<h2 id="2026-02-27">2026-02-27</h2>

<strong>Export MCP server portal logs with Logpush</strong>

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


<h2 id="2026-02-17">2026-02-17</h2>

<strong>Streamlined clientless browser isolation for private applications</strong>

<p>A new <strong>Allow clientless access</strong> setting makes it easier to connect users without a device client to internal applications, without using public DNS.</p>
<p><img src="/assets/upstream/images/changelog/access/allow-clientless-access.png" alt="Allow clientless access setting in the Cloudflare One dashboard" /></p>
<p>Previously, to provide clientless access to a private hostname or IP without a <a href="/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route">published application</a>, you had to create a separate <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark application</a> pointing to a prefixed <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> URL (for example, <code>https://&lt;your-teamname&gt;.cloudflareaccess.com/browser/https://10.0.0.1/</code>). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.</p>
<p>Now, you can manage clientless access directly within your <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private self-hosted application</a>. When  <strong>Allow clientless access</strong> is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">remote browser permissions</a> to open the link.</p>


<h2 id="2026-02-17-1">2026-02-17</h2>

<strong>Policies for bookmark applications</strong>

<p>You can now assign <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark applications</a>. This lets you control which users see a bookmark in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> based on identity, device posture, and other policy rules.</p>
<p>Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:</p>
<ul>
<li><strong>Tailor the App Launcher to each user</strong> — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.</li>
<li><strong>Restrict visibility of sensitive bookmarks</strong> — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.</li>
</ul>
<p>Bookmarks support all <a href="/cloudflare-one/access-controls/policies/">Access policy configurations</a> except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/bookmarks/">Add bookmarks</a>.</p>


<h2 id="2026-02-13">2026-02-13</h2>

<strong>Fine-grained permissions for Access policies and service tokens</strong>

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


<h2 id="2026-01-22">2026-01-22</h2>

<strong>Require Access protection for zones</strong>

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


<h2 id="2026-01-22-1">2026-01-22</h2>

<strong>New granular API token permissions for Cloudflare Access</strong>

<p>Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:</p>
<ul>
<li><strong>Access: Organizations Revoke</strong> — Grants the ability to <a href="/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions">revoke user sessions</a> in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.</li>
<li><strong>Access: Population Read</strong> — Grants read access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.</li>
<li><strong>Access: Population Write</strong> — Grants write access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.</li>
</ul>
<p>These permissions are scoped at the account level and can be combined with existing Access permissions.</p>
<p>For a full list of available permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>


<h2 id="2026-01-08">2026-01-08</h2>

<strong>Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users</strong>

<p>Cloudflare <a href="/cloudflare-one/insights/logs/">admin activity logs</a> now capture each time a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTP (DoH) user</a> is created.</p>
<p>These logs can be viewed from the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, pulled via the <a href="/api/">Cloudflare API</a>, and exported through <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>


<h2 id="2025-11-14">2025-11-14</h2>

<strong>Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard</strong>

<p>SSH with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Cloudflare Access for Infrastructure</a> allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.</p>
<p>Previously, users had to generate this certificate by using the <a href="https://developers.cloudflare.com/api/">Cloudflare API</a> directly. With this update, you can now create and manage this certificate in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a> from the <strong>Access controls</strong> &gt; <strong>Service credentials</strong> page.</p>
<p><img src="/assets/upstream/images/changelog/access/SSH-CA-generation.png" alt="Navigate to Access controls and then Service credentials to see where you can generate an SSH CA" /></p>
<p>For more details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca">Generate a Cloudflare SSH CA</a>.</p>


<h2 id="2025-10-28">2025-10-28</h2>

<strong>Access private hostname applications support all ports/protocols</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Cloudflare Access for private hostname applications</a> can now secure traffic on all ports and protocols.</p>
<p>Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port <code>443</code> and support Server Name Indicator (SNI).</p>
<p>This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.</p>
<p><img src="/assets/upstream/images/changelog/access/internal_private_app_any_port.png" alt="Example private application on non-443 port" /></p>
<p>For example, you can now create a self-hosted application in Access for <code>ssh.testapp.local</code> running on port <code>22</code>. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.</p>
<p>This feature is generally available across all plans.</p>


<h2 id="2025-10-02">2025-10-02</h2>

<strong>Fine-grained Permissioning for Access for Apps, IdPs, &amp; Targets now in Public Beta</strong>

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


<h2 id="2025-09-22">2025-09-22</h2>

<strong>Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</strong>

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


<h2 id="2025-08-26">2025-08-26</h2>

<strong>Manage and restrict access to internal MCP servers with Cloudflare Access</strong>

<p>You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<p><a href="/cloudflare-one/access-controls/ai-controls/linked-apps/">Self-hosted applications</a> in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.</p>
<p>For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog post</a> on the Cloudflare Blog.</p>


<h2 id="2025-08-26-1">2025-08-26</h2>

<strong>MCP server portals</strong>

<p><img src="/assets/upstream/images/changelog/access/mcp-server-portal.png" alt="MCP server portal" /></p>
<p>An <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:</p>
<ul>
<li><strong>Streamlined access to multiple MCP servers</strong>: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.</li>
<li><strong>Customized tools per portal</strong>: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.</li>
<li><strong>Observability</strong>: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.</li>
</ul>
<p>This is available in an open beta for all customers across all plans! For more information check out our <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog</a> for this release.</p>


<h2 id="2025-08-15">2025-08-15</h2>

<strong>SFTP support for SSH with Cloudflare Access for Infrastructure</strong>

<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Cloudflare Access for Infrastructure</a> now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.</p>


<h2 id="2025-08-14">2025-08-14</h2>

<strong>Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</strong>

<p>Cloudflare Access logs now support the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a>. If you have configured the CMB for your account, all Access logging will respect that configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17615.md")</aside>


<h2 id="2025-07-01">2025-07-01</h2>

<strong>Access RDP securely from your browser — now in open beta</strong>

<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now available in open beta for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>With browser-based RDP, you can:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browsed-based RDP Access application" /></p>
<p>To get started, see <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>


<h2 id="2025-06-05">2025-06-05</h2>

<strong>Cloudflare One Analytics Dashboards and Exportable Access Report</strong>

<p>Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/Analytics Dashboards.png" alt="Cloudflare One Analytics Dashboards"></p>
<p>Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A <strong>preview</strong> of the report is shown below, with more to be found in the report:</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-report.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>Both features are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="2025-05-16">2025-05-16</h2>

<strong>New Access Analytics in the Cloudflare One Dashboard</strong>

<p>A new Access Analytics dashboard is now available to all Cloudflare One customers. Customers can apply and combine multiple filters to dive into specific slices of their Access metrics. These filters include:</p>
<ul>
<li>Logins granted and denied</li>
<li>Access events by type (SSO, Login, Logout)</li>
<li>Application name (Salesforce, Jira, Slack, etc.)</li>
<li>Identity provider (Okta, Google, Microsoft, onetimepin, etc.)</li>
<li>Users (<code>chris@cloudflare.com</code>, <code>sally@cloudflare.com</code>, <code>rachel@cloudflare.com</code>, etc.)</li>
<li>Countries (US, CA, UK, FR, BR, CN, etc.)</li>
<li>Source IP address</li>
<li>App type (self-hosted, Infrastructure, RDP, etc.)</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/accessanalytics.png" alt="Access Analytics" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and find Analytics in the side navigation bar.</p>


<h2 id="2025-04-21">2025-04-21</h2>

<strong>Access bulk policy tester</strong>

<p>The <a href="/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application">Access bulk policy tester</a> is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).</p>
<p><img src="/assets/upstream/images/changelog/access/example-policy-tester.png" alt="Example policy tester" /></p>


<h2 id="2025-04-09">2025-04-09</h2>

<strong>Cloudflare Zero Trust SCIM User and Group Provisioning Logs</strong>

<p><a href="/cloudflare-one/team-and-resources/users/scim">Cloudflare Zero Trust SCIM provisioning</a> now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM logs</a> support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.</p>
<p>SCIM logs can be found on the Zero Trust Dashboard under <strong>Logs</strong> -&gt; <strong>SCIM provisioning</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/example-scim-log.png" alt="Example SCIM Logs" /></p>


<h2 id="2025-03-03">2025-03-03</h2>

<strong>New SAML and OIDC Fields and SAML transforms for Access for SaaS</strong>

<p><a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS applications</a> now include more configuration options to support a wider array of SaaS applications.</p>
<p><strong>SAML and OIDC Field Additions</strong></p>
<p>OIDC apps now include:</p>
<ul>
<li>Group Filtering via RegEx</li>
<li>OIDC Claim mapping from an IdP</li>
<li>OIDC token lifetime control</li>
<li>Advanced OIDC auth flows including hybrid and implicit flows</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/oidc-claims.png" alt="OIDC field additions" /></p>
<p>SAML apps now include improved SAML attribute mapping from an IdP.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-attribute-statements.png" alt="SAML field additions" /></p>
<p><strong>SAML transformations</strong></p>
<p>SAML identities sent to Access applications can be fully customized using JSONata expressions. This allows admins to configure the precise identity SAML statement sent to a SaaS application.</p>
<p><img src="/assets/upstream/images/changelog/access/transformation-box.png" alt="Configured SAML statement sent to application" /></p>


<h2 id="2025-01-15-1">2025-01-15</h2>

<strong>Export SSH command logs with Access for Infrastructure using Logpush</strong>

<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-01-15-ssh-logs-and-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17614.md")</aside>
<p>Cloudflare now allows you to send SSH command logs to storage destinations configured in <a href="/logs/logpush/">Logpush</a>, including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH logs dataset</a>.</p>
<p>To set up a Logpush job, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>


<h2 id="2024-10-01">2024-10-01</h2>

<strong>Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure</strong>

<p>Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.</p>
<p>SSH with <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/">WARP-to-Tunnel</a>.</p>
<p>SSH with Access for Infrastructure enables you to:</p>
<ul>
<li><strong>Author fine-grained policy</strong> to control who may access your SSH servers, including specific ports, protocols, and SSH users.</li>
<li><strong>Monitor infrastructure access</strong> with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.</li>
<li><strong>Preserve your end users' workflows.</strong> SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/infrastructure-app.png" alt="Example of an infrastructure Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Access for Infrastructure</a>.</p>


<h2 id="2025-02-12">2025-02-12</h2>
<p><strong>Access policies support filtering</strong></p>
<p>You can now filter Access policies by their action, selectors, rule groups, and assigned applications.</p>
<h2 id="2025-02-11">2025-02-11</h2>
<p><strong>Private self-hosted applications and reusable policies GA</strong></p>
<p><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Private self-hosted applications</a> and <a href="/cloudflare-one/access-controls/policies/policy-management/">reusable Access policies</a> are now generally available (GA) for all customers.</p>
<h2 id="2025-01-21">2025-01-21</h2>
<p><strong>Access Applications support private hostnames/IPs and reusable Access policies.</strong></p>
<p>Cloudflare Access self-hosted applications can now be defined by <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private IPs</a>, <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private hostnames</a> (on port 443) and <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">public hostnames</a>. Additionally, we made Access policies into their own object which can be reused across multiple applications. These updates involved significant updates to the overall Access dashboard experience. The updates will be slowly rolled out to different customer cohorts. If you are an Enterprise customer and would like early access, reach out to your account team.</p>
<h2 id="2025-01-15">2025-01-15</h2>
<p><strong>Logpush for SSH command logs</strong></p>
<p>Enterprise customers can now use Logpush to export SSH command logs for Access for Infrastructure targets.</p>
<h2 id="2024-12-04">2024-12-04</h2>
<p><strong>SCIM GA for Okta and Microsoft Entra ID</strong></p>
<p>Cloudflare's SCIM integrations with <a href="/cloudflare-one/integrations/identity-providers/okta/#synchronize-users-and-groups">Okta</a> and <a href="/cloudflare-one/integrations/identity-providers/entra-id/#synchronize-users-and-groups">Microsoft Entra ID</a> (formerly AzureAD) are now out of beta and generally available (GA) for all customers. These integrations can be used for Access and Gateway policies and Zero Trust user management. Note: This GA release does not include <a href="/fundamentals/account/account-security/scim-setup/">Dashboard SSO SCIM</a> support.</p>
<h2 id="2024-10-23">2024-10-23</h2>
<p><strong>SSH with Access for Infrastructure</strong></p>
<p>Admins can now use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a> to manage privileged access to SSH servers. Access for Infrastructure provides improved control and visibility over who accessed what service and what they did during their SSH session. Access for Infrastructure also eliminates the risk and overhead associated with managing SSH keys by using short-lived SSH certificates to access SSH servers.</p>
<h2 id="2024-08-26">2024-08-26</h2>
<p><strong>Reduce automatic seat deprovisioning minimum to 1 month, down from 2 months.</strong></p>
<p>Admins can now configure Zero Trust seats to <a href="/cloudflare-one/team-and-resources/users/seat-management/#enable-seat-expiration">automatically expire</a> after 1 month of user inactivity. The previous minimum was 2 months.</p>
<h2 id="2024-06-06">2024-06-06</h2>
<p><strong>Scalability improvements to the App Launcher</strong></p>
<p>Applications now load more quickly for customers with a large number of applications or complex policies.</p>
<h2 id="2024-04-28">2024-04-28</h2>
<p><strong>Add option to bypass CORS to origin server</strong></p>
<p>Access admins can <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/#bypass-options-requests-to-origin">defer all CORS enforcement to their origin server</a> for specific Access applications.</p>
<h2 id="2024-04-15">2024-04-15</h2>
<p><strong>Zero Trust User identity audit logs</strong></p>
<p>All user identity changes via SCIM or Authentication events are logged against a user's registry identity.</p>
<h2 id="2024-02-22">2024-02-22</h2>
<p><strong>Access for SaaS OIDC Support</strong></p>
<p>Access for SaaS applications can be setup with OIDC as an authentication method. OIDC and SAML 2.0 are now both fully supported.</p>
<h2 id="2024-02-22-1">2024-02-22</h2>
<p><strong>WARP as an identity source for Access</strong></p>
<p>Allow users to log in to Access applications with their WARP session identity. Users need to reauthenticate based on default session durations. WARP authentication identity must be turned on in your device enrollment permissions and can be enabled on a per application basis.</p>
<h2 id="2023-12-20">2023-12-20</h2>
<p><strong>Unique Entity IDs in Access for SaaS</strong></p>
<p>All new Access for SaaS applications have unique Entity IDs. This allows for multiple integrations with the same SaaS provider if required. The unique Entity ID has the application audience tag appended. Existing apps are unchanged.</p>
<h2 id="2023-12-15">2023-12-15</h2>
<p><strong>Default relay state support in Access for SaaS</strong></p>
<p>Allows Access admins to set a default relay state on Access for SaaS apps.</p>
<h2 id="2023-09-15">2023-09-15</h2>
<p><strong>App launcher supports tags and filters</strong></p>
<p>Access admins can now tag applications and allow users to filter by those tags in the App Launcher.</p>
<h2 id="2023-09-15-1">2023-09-15</h2>
<p><strong>App launcher customization</strong></p>
<p>Allow Access admins to configure the App Launcher page within Zero Trust.</p>
<h2 id="2023-09-15-2">2023-09-15</h2>
<p><strong>View active Access user identities in the dashboard and API</strong></p>
<p>Access admins can now view the full contents of a user's identity and device information for all active application sessions.</p>
<h2 id="2023-09-08">2023-09-08</h2>
<p><strong>Custom OIDC claims for named IdPs</strong></p>
<p>Access admins can now add custom claims to the existing named IdP providers. Previously this was locked to the generic OIDC provider.</p>
<h2 id="2023-08-02">2023-08-02</h2>
<p><strong>Azure AD authentication contexts</strong></p>
<p>Support Azure AD authentication contexts directly in Access policies.</p>
<h2 id="2023-06-23">2023-06-23</h2>
<p><strong>Custom block pages for Access applications</strong></p>
<p>Allow Access admins to customize the block pages presented by Access to end users.</p>


