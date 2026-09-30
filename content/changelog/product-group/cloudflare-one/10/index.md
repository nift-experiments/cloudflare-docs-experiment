---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/
  description: '2025-09-16'
  full_title: Cloudflare One changelog - page 10 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 10 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-09-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 10"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-09-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/#page","headline":"Cloudflare One changelog - page 10 | Cloudflare Docs","description":"2025-09-16","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/10/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-ai-enabled-search-for-zero-trust-dashboard"><a href="/changelog/post/2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard/">New AI-Enabled Search for Zero Trust Dashboard</a></h2>
<p><em>2025-09-16</em></p>
<p>Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/searchexample.png" alt="Example search results in the Zero Trust dashboard" /></p>
<p><strong>Ask Cloudy</strong> — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.</p>
<p>Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.</p>
<p><strong>Find Recents</strong> — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.</p>


<h2 id="regional-email-processing-for-germany-india-or-australia"><a href="/changelog/post/2025-09-11-regional-email-processing-gia/">Regional Email Processing for Germany, India, or Australia</a></h2>
<p><em>2025-09-11T23:15:00+00:00</em></p>
<p>We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: <strong>MX</strong>, <strong>BCC</strong>, and <strong>Journaling</strong>.</p>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-new">What’s new</h4>
<p>Customers can now select where their email is processed. The following regions are supported:</p>
<ul>
<li><strong>Germany</strong></li>
<li><strong>India</strong></li>
<li><strong>Australia</strong></li>
</ul>
<p>Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.</p>
<h4 id="2025-09-11-regional-email-processing-gia-how-to-use-it">How to use it</h4>
<p>When onboarding a domain with MX, BCC, or Journaling:</p>
<ol>
<li>Select the desired processing location (Germany, India, or Australia).</li>
<li>The UI will display updated processing addresses specific to that region.</li>
<li>For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.</li>
</ol>
<h4 id="2025-09-11-regional-email-processing-gia-availability">Availability</h4>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-next">What’s next</h4>
<p>We’re expanding the list of processing locations to match our <a href="/data-localization/">Data Localization Suite (DLS)</a> footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.</p>


<h2 id="dns-filtering-for-private-network-onramps"><a href="/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/">DNS filtering for private network onramps</a></h2>
<p><em>2025-09-11</em></p>
<p><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering">Magic WAN</a> and <a href="/mesh/features/routes/#dns-filtering">WARP Connector</a> users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.</p>
<p>Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">Internal DNS</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">hostname-based policies</a>.</p>
<p>To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, <code>172.64.36.1</code> and <code>172.64.36.2</code>. Once you configure DNS resolution and filtering, you can use <em>Source Internal IP</em> as a traffic selector in your <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for routing private DNS traffic to your <a href="/dns/internal-dns/">Internal DNS</a>.</p>


<h2 id="custom-ike-id-for-ipsec-tunnels"><a href="/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/">Custom IKE ID for IPsec Tunnels</a></h2>
<p><em>2025-09-08</em></p>
<p>Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.</p>
<p>This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the <a href="/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/">Custom IKE ID feature and the API call to configure it</a>.</p>


<h2 id="bidirectional-tunnel-health-checks-are-compatible-with-all-magic-on-ramps"><a href="/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/">Bidirectional tunnel health checks are compatible with all Magic on-ramps</a></h2>
<p><em>2025-09-05</em></p>
<p>All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.</p>
<p>Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.</p>
<p>There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.</p>
<p>Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.</p>


<h2 id="cloudflare-tunnel-and-networks-api-will-no-longer-return-deleted-resources-by-default-starting-december-1-2025"><a href="/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/">Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</a></h2>
<p><em>2025-09-02</em></p>
<p>Starting <strong>December 1, 2025</strong>, list endpoints for the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.</p>
<p>No action is required if you already explicitly set <code>is_deleted=false</code> or if you only need to list active resources.</p>
<p>This change affects the following API endpoints:</p>
<ul>
<li>List all tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/methods/list/"><code>GET /accounts/{account_id}/tunnels</code></a></li>
<li>List <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a></li>
<li>List <a href="/mesh/">WARP Connector</a> tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a></li>
<li>List tunnel routes: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/"><code>GET /accounts/{account_id}/teamnet/routes</code></a></li>
<li>List subnets: <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/"><code>GET /accounts/{account_id}/zerotrust/subnets</code></a></li>
<li>List virtual networks: <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/"><code>GET /accounts/{account_id}/teamnet/virtual_networks</code></a></li>
</ul>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-what-is-changing">What is changing?</h4>
<p>The default behavior of the <code>is_deleted</code> query parameter will be updated.</p>
<table>
<thead>
<tr>
<th align="left">Scenario</th>
<th align="left">Previous behavior (before December 1, 2025)</th>
<th align="left">New behavior (from December 1, 2025)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>is_deleted</code> parameter is omitted</td>
<td align="left">Returns <strong>active &amp; deleted</strong> tunnels, routes, subnets and virtual networks</td>
<td align="left">Returns <strong>only active</strong> tunnels, routes, subnets and virtual networks</td>
</tr>
</tbody>
</table>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-action-required">Action required</h4>
<p>If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the <code>is_deleted</code> parameter before <strong>December 1, 2025</strong>.</p>
<p>To get a list of only deleted resources, you must now explicitly add the <code>is_deleted=true</code> query parameter to your request:</p>
<pre tabindex="0"><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>


<h2 id="updated-email-security-roles"><a href="/changelog/post/2025-09-01-updated-new-roles/">Updated Email security roles</a></h2>
<p><em>2025-09-01T23:25:49+00:00</em></p>
<p>To provide more granular controls, we refined the <a href="/cloudflare-one/roles-permissions/#email-security-roles">existing roles</a> for Email security and launched a new Email security role as well.</p>
<p>All Email security roles no longer have read or write access to any of the other Zero Trust products:</p>
<ul>
<li><strong>Email Configuration Admin</strong></li>
<li><strong>Email Integration Admin</strong></li>
<li><strong>Email security Read Only</strong></li>
<li><strong>Email security Analyst</strong></li>
<li><strong>Email security Policy Admin</strong></li>
<li><strong>Email security Reporting</strong></li>
</ul>
<p>To configure <a href="/cloudflare-one/email-security/outbound-dlp/">Data Loss Prevention (DLP)</a> or <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation">Remote Browser Isolation (RBI)</a>, you now need to be an admin for the Zero Trust dashboard with the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>Also through customer feedback, we have created a new additive role to allow <strong>Email security Analyst</strong> to create, edit, and delete Email security policies, without needing to provide access via the <strong>Email Configuration Admin</strong> role. This role is called <strong>Email security Policy Admin</strong>, which can read all settings, but has write access to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="cloudflare-one-warp-diagnostic-ai-analyzer"><a href="/changelog/post/2025-08-29-warp-AI-diag-analyzer/">Cloudflare One WARP Diagnostic AI Analyzer</a></h2>
<p><em>2025-08-29</em></p>
<p>We're excited to share a new AI feature, the <a href="https://blog.cloudflare.com/ai-troubleshoot-warp-and-network-connectivity-issues/">WARP diagnostic analyzer</a>, to help you troubleshoot and resolve WARP connectivity issues faster. This beta feature is now available in the <a href="https://dash.cloudflare.com/one/">Cloudflare One dashboard</a> to all users. The AI analyzer makes it easier for you to identify the root cause of client connectivity issues by parsing <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture">remote captures</a> of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">WARP diagnostic logs</a>. The WARP diagnostic analyzer provides a summary of impact that may be experienced on the device, lists notable events that may contribute to performance issues, and recommended troubleshooting steps and articles to help you resolve these issues. Refer to <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta">WARP diagnostics analyzer (beta)</a> to learn more about how to maximize using the WARP diagnostic analyzer to troubleshoot the WARP client.</p>


<h2 id="dex-mcp-server"><a href="/changelog/post/2025-08-29-dex-mcp-server/">DEX MCP Server</a></h2>
<p><em>2025-08-29</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device connectivity and performance across your Cloudflare SASE deployment.</p>
<p>We've released an MCP server <a href="https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">(Model Context Protocol)</a> for DEX.</p>
<p>The DEX MCP server is an AI tool that allows customers to ask a question like, &quot;Show me the connectivity and performance metrics for the device used by carly‌@acme.com&quot;, and receive an answer that contains data from the DEX API.</p>
<p>Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.</p>
<p>Customers can test the new DEX MCP server in less than one minute. To learn more, read the <a href="/cloudflare-one/insights/dex/dex-mcp-server/">DEX MCP server documentation</a>.</p>


<h2 id="shadow-it-saas-analytics-dashboard"><a href="/changelog/post/2025-08-27-shadow-it-analytics/">Shadow IT - SaaS analytics dashboard</a></h2>
<p><em>2025-08-27</em></p>
<p>Zero Trust has significantly upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including <strong>Unreviewed</strong>, <strong>In Review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong> designating how they can be used in your organization.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-analytics.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="new-casb-integrations-for-chatgpt-claude-and-gemini"><a href="/changelog/post/2025-08-26-casb-ai-integrations/">New CASB integrations for ChatGPT, Claude, and Gemini</a></h2>
<p><em>2025-08-26 16:00:00 UTC</em></p>
<p><a href="https://www.cloudflare.com/zero-trust/products/casb/">Cloudflare CASB</a> now supports three of the most widely used GenAI platforms — <strong>OpenAI ChatGPT</strong>, <strong>Anthropic Claude</strong>, and <strong>Google Gemini</strong>. These API-based integrations give security teams agentless visibility into posture, data, and compliance risks across their organization’s use of generative AI.</p>
<p><img src="/assets/upstream/images/casb/changelog/casb-ai-integrations-preview.png" alt="Cloudflare CASB showing selection of new findings for ChatGPT, Claude, and Gemini integrations." /></p>
<h4 id="2025-08-26-casb-ai-integrations-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Agentless connections</strong> — connect ChatGPT, Claude, and Gemini tenants via API; no endpoint software required</li>
<li><strong>Posture management</strong> — detect insecure settings and misconfigurations that could lead to data exposure</li>
<li><strong>DLP detection</strong> — identify sensitive data in uploaded chat attachments or files</li>
<li><strong>GenAI-specific insights</strong> — surface risks unique to each provider’s capabilities</li>
</ul>
<h4 id="2025-08-26-casb-ai-integrations-learn-more">Learn more</h4>
<ul>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/openai/">ChatGPT integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/">Claude integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/">Gemini integration docs</a></li>
</ul>
<p>These integrations are available to all Cloudflare One customers today.</p>


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


<h2 id="new-dlp-topic-based-detection-entries-for-ai-prompt-protection"><a href="/changelog/post/2025-08-25-ai-prompt-protection/">New DLP topic based detection entries for AI prompt protection</a></h2>
<p><em>2025-08-25</em></p>
<p>You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.</p>
<ol>
<li><strong>Prompt Detection for AI Applications</strong></li>
</ol>
<p>DLP can now natively detect and inspect user prompts submitted to popular AI applications, including <strong>Google Gemini</strong>, <strong>ChatGPT</strong>, <strong>Claude</strong>, and <strong>Perplexity</strong>.</p>
<ol start="2">
<li><strong>Prompt Analysis and Topic Classification</strong></li>
</ol>
<p>Our DLP engine performs deep analysis on each prompt, applying <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">topic classification</a>. These topics are grouped into two evaluation categories:</p>
<pre tabindex="0"><code>    - **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.&#10;&#10;    - **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.&#10;</code></pre>
<p>To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.</p>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-detection-entry.png" alt="DLP" /></p>
<ol start="3">
<li>
<p><strong>Granular Guardrails</strong></p>
<p>You can now build guardrails using Gateway HTTP policies with <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a>. Apply a DLP profile containing an <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topic detection</a> to individual AI applications (for example, <code>ChatGPT</code>) and specific user actions (for example, <code>SendPrompt</code>) to block sensitive prompts.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-policy.png" alt="DLP" /></p>
<ol start="4">
<li>
<p><strong>Full Prompt Logging</strong></p>
<p>To aid in incident investigation, an optional setting in your Gateway policy allows you to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content">capture prompt logs</a> to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by <code>conversation_id</code>, allowing you to reconstruct the full context of an interaction that led to a policy violation.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-log.png" alt="DLP" /></p>
<p>AI prompt protection is now available in open beta. To learn more about it, read the <a href="https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging">blog</a> or refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>


<h2 id="gateway-byoip-dedicated-egress-ips-now-available"><a href="/changelog/post/2025-08-21-byoip-dedicated-egress-ip/">Gateway BYOIP Dedicated Egress IPs now available.</a></h2>
<p><em>2025-08-21</em></p>
<p>Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.</p>
<p>Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.</p>
<p>Get started by following the <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP onboarding process</a>. Once your IPs are onboarded, go to <strong>Gateway</strong> &gt; <strong>Egress policies</strong> and select or create an egress policy. In <strong>Select an egress IP</strong>, choose <em>Use dedicated egress IPs (Cloudflare or BYOIP)</em>, then select your BYOIP address from the dropdown menu.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-byoip-dedicated-egress-ips.png" alt="Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP for dedicated egress IPs</a>.</p>


<h2 id="sftp-support-for-ssh-with-cloudflare-access-for-infrastructure"><a href="/changelog/post/2025-08-15-sftp/">SFTP support for SSH with Cloudflare Access for Infrastructure</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Cloudflare Access for Infrastructure</a> now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.</p>


<h2 id="steer-traffic-by-as-number-in-load-balancing-custom-rules"><a href="/changelog/post/2025-08-15-asnum-support-in-custom-rules/">Steer Traffic by AS Number in Load Balancing Custom Rules</a></h2>
<p><em>2025-08-15</em></p>
<p>You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.</p>
<p>This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/asnum-custom-rule.png" alt="Create a Load Balancing Custom Rule using AS Num" /></p>
<p>To get started, create a <a href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/">Custom Rule</a> in your Load Balancer and select <strong>AS Num</strong> from the <strong>Field</strong> dropdown.</p>


<h2 id="cloudflare-access-logging-supports-the-customer-metadata-boundary-cmb"><a href="/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/">Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</a></h2>
<p><em>2025-08-14</em></p>
<p>Cloudflare Access logs now support the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a>. If you have configured the CMB for your account, all Access logging will respect that configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17615.md")</aside>


<h2 id="expanded-email-link-isolation"><a href="/changelog/post/2025-08-07-expanded-link-isolation/">Expanded Email Link Isolation</a></h2>
<p><em>2025-08-07T23:22:49+00:00</em></p>
<p>When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.</p>
<p>For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.</p>
<p><img src="/assets/upstream/images/changelog/email-security/expanded-link-actions.jpg" alt="Expanded Email Link Isolation Configuration" /></p>
<p>To isolate all links within a message based on the disposition, select <strong>Settings</strong> &gt; <strong>Link Actions</strong> &gt; <strong>View</strong> and select <strong>Configure</strong>. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on <a href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">Configure link actions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="improvements-to-monitoring-using-zone-settings"><a href="/changelog/post/2025-08-06-zone-monitoring-improvements/">Improvements to Monitoring Using Zone Settings</a></h2>
<p><em>2025-08-06</em></p>
<p>Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.</p>
<p>All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.</p>
<h4 id="2025-08-06-zone-monitoring-improvements-what-you-can-expect">What you can expect:</h4>
<ul>
<li>More reliable application of zone settings to monitoring requests, including
<ul>
<li>Authenticated Origin Pulls</li>
<li>Aegis Egress IP Pools</li>
<li>Argo Smart Routing</li>
<li>HTTP/2 to Origin</li>
</ul>
</li>
<li>Improved support and bug fixes for retries, redirects, and proxied origin resolution</li>
<li>Improved performance and reliability of monitoring requests within the Cloudflare network</li>
<li>Unrelated CDN or WAF configuration changes should have no risk of impact to pool health</li>
</ul>


<h2 id="terraform-v5-support-for-tunnels-and-routes"><a href="/changelog/post/2025-07-31-terraform-v5-tunnels-routes/">Terraform V5 support for tunnels and routes</a></h2>
<p><em>2025-07-31</em></p>
<p>The Cloudflare Terraform provider resources for Cloudflare WAN tunnels and routes now support Terraform provider version 5. Customers using infrastructure-as-code workflows can manage their tunnel and route configuration with the latest provider version.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider documentation</a>.</p>


<h2 id="magic-transit-and-magic-wan-health-check-data-is-fully-compatible-with-the-cmb-eu-setting"><a href="/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/">Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</a></h2>
<p><em>2025-07-30</em></p>
<p>Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU (<a href="/data-localization/metadata-boundary/">Customer Metadata Boundary - Europe</a>) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.</p>
<p>This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.</p>
<p>Specifically, these two GraphQL endpoints are now compatible with CMB EU:</p>
<ul>
<li><code>magicTransitTunnelHealthChecksAdaptiveGroups</code></li>
<li><code>magicTransitTunnelTrafficAdaptiveGroups</code></li>
</ul>


<h2 id="scam-domain-category-introduced-under-security-threats"><a href="/changelog/post/2025-07-28-Spam-domain-category-introduced/">Scam domain category introduced under Security Threats</a></h2>
<p><em>2025-07-28</em></p>
<p>We have introduced a new Security Threat category called <strong>Scam</strong>. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.</p>
<p><strong>New category added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>191</td>
<td>Scam</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="gateway-http-filtering-on-all-ports-available-in-open-beta"><a href="/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/">Gateway HTTP Filtering on all ports available in open BETA</a></h2>
<p><em>2025-07-24</em></p>
<p><a href="/cloudflare-one/traffic-policies/">Gateway</a> can now apply <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP filtering</a> to all proxied HTTP requests, not just traffic on standard HTTP (<code>80</code>) and HTTPS (<code>443</code>) ports. This means all requests can now be filtered by <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">A/V scanning</a>, <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a>, <a href="/cloudflare-one/data-loss-prevention/#data-in-transit">Data Loss Prevention (DLP)</a>, and more.</p>
<p>You can turn this <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">setting</a> on by going to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Firewall</strong> and choosing  <em>Inspect on all ports</em>.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-Inspection-all-ports.png" alt="HTTP Inspection on all ports setting" /></p>
<p>To learn more, refer to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">Inspect on all ports (Beta)</a>.</p>


<h2 id="google-bard-application-replaced-by-gemini"><a href="/changelog/post/2025-08-15-gemini-application-replaces-bard/">Google Bard Application replaced by Gemini</a></h2>
<p><em>2025-07-22</em></p>
<p>The <strong>Google Bard</strong> application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the <strong>Gemini</strong> application (ID: 1340).
Any existing Gateway policies that reference the old Google Bard application will no longer function.
To ensure your policies continue to work as intended, you should update them to use the new Gemini application.
We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies.
For more information about application policies, please see the <a href="/cloudflare-one/traffic-policies/application-app-types/">Cloudflare Gateway documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/9/">Previous</a><span>Page 10 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/11/">Next</a></nav>
