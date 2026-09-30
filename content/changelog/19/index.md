---
cp9:
  canonical: https://developers.cloudflare.com/changelog/19/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 19 | Cloudflare Docs
  head_html: <title>Changelog - page 19 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/19/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 19"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/19/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/19/#page","headline":"Changelog - page 19 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/19/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/19/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-br-webmcp"><a href="/changelog/post/2026-04-15-br-webmcp/">Browser Run adds WebMCP support</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) now supports <a href="https://webmachinelearning.github.io/webmcp/">WebMCP</a> (Web Model Context Protocol), a new browser API from the Google Chrome team.</p>
<p>The Internet was built for humans, so navigating as an AI agent today is unreliable. WebMCP lets websites expose structured tools for AI agents to discover and call directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like <code>searchFlights()</code> or <code>bookTicket()</code> with typed parameters, making browser automation faster, more reliable, and less fragile.</p>
<p><img src="/images/browser-run/webMCP.gif" alt="Browser Run lab session showing WebMCP tools being discovered and executed in the Chrome DevTools console to book a hotel" /></p>
<p>With WebMCP, you can:</p>
<ul>
<li><strong>Discover website tools</strong> - Use <code>navigator.modelContextTesting.listTools()</code> to see available actions on any WebMCP-enabled site</li>
<li><strong>Execute tools directly</strong> - Call <code>navigator.modelContextTesting.executeTool()</code> with typed parameters</li>
<li><strong>Handle human-in-the-loop interactions</strong> - Some tools pause for user confirmation before completing sensitive actions</li>
</ul>
<p>WebMCP requires Chrome beta features. We have an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. To start a WebMCP session, add <code>lab=true</code> to your <code>/devtools/browser</code> request:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser?lab=true&amp;keep_alive=300000&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot;&#10;</code></pre>
<p>Combined with the recently launched <a href="/browser-run/cdp/">CDP endpoint</a>, AI agents can also use WebMCP. Connect an <a href="/browser-run/cdp/mcp-clients/">MCP client</a> to Browser Run via CDP, and your agent can discover and call website tools directly. Here's the same hotel booking demo, this time driven by an AI agent through OpenCode:</p>
<p><img src="/images/browser-run/webMCPagent.gif" alt="Browser Run Live View showing an AI agent navigating a hotel booking site in real time" /></p>
<p>For a step-by-step guide, refer to the <a href="/browser-run/features/webmcp/">WebMCP documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-workflows-limits-raised"><a href="/changelog/post/2026-04-15-workflows-limits-raised/">Increased concurrency, creation rate, and queued instance limits for Workflows instances</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> limits have been raised to the following:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent instances (running in parallel)</td>
<td>10,000</td>
<td>50,000</td>
</tr>
<tr>
<td>Instance creation rate (per account)</td>
<td>100/second per account</td>
<td>300/second per account, 100/second per workflow</td>
</tr>
<tr>
<td>Queued instances per Workflow <sup><a href="#2026-04-15-workflows-limits-raised-footnote-1">1</a></sup></td>
<td>1 million</td>
<td>2 million</td>
</tr>
</tbody>
</table>
<p>These increases apply to all users on the <a href="/workers/platform/pricing/">Workers Paid plan</a>. Refer to the <a href="/workflows/reference/limits/">Workflows limits documentation</a> for more details.</p>
<section class="footnotes"><h4 id="2026-04-15-workflows-limits-raised-footnotes">Footnotes</h4><ol><li id="2026-04-15-workflows-limits-raised-footnote-1">Queued instances are instances that have been created or awoken and are waiting for a concurrency slot.</li></ol></section>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-independent-mfa"><a href="/changelog/post/2026-04-15-independent-mfa/">Independent MFA for Access applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports independent multi-factor authentication (MFA), allowing you to enforce MFA requirements without relying on your identity provider (IdP). With per-application and per-policy configuration, you can enforce stricter authentication methods like hardware security keys on sensitive applications without requiring them across your entire organization. This reduces the risk of MFA fatigue for your broader user population while adding additional security where it matters most.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-agentlee-writeops-genui"><a href="/changelog/post/2026-04-15-agentlee-writeops-genui/">Agent Lee adds Write Operations and Generative UI</a></h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><h4 id="2026-04-15-agentlee-writeops-genui-agent-lee-adds-write-operations-and-generative-ui">Agent Lee adds Write Operations and Generative UI</h4>
<p>We are excited to announce two major capability upgrades for <strong>Agent Lee</strong>, the AI co-pilot built directly into the Cloudflare dashboard. Agent Lee is designed to understand your specific account configuration, and with this release, it moves from a passive advisor to an active assistant that can help you manage your infrastructure and visualize your data through natural language.</p>
<h4 id="2026-04-15-agentlee-writeops-genui-take-action-with-write-operations">Take action with Write Operations</h4>
<p>Agent Lee can now perform changes on your behalf across your Cloudflare account. Whether you need to update DNS records, modify SSL/TLS settings, or configure Workers routes, you can simply ask.</p>
<p>To ensure security and accuracy, every write operation requires <strong>explicit user approval</strong>. Before any change is committed, Agent Lee will present a summary of the proposed action in plain language. No action is taken until you select <strong>Confirm</strong>, and this approval requirement is enforced at the infrastructure level to prevent unauthorized changes.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Add an A record for blog.example.com pointing to 192.0.2.10.&quot;</em></li>
<li><em>&quot;Enable Always Use HTTPS on my zone.&quot;</em></li>
<li><em>&quot;Set the SSL mode for example.com to Full (strict).&quot;</em></li>
</ul>
<h4 id="2026-04-15-agentlee-writeops-genui-visualize-data-with-generative-ui">Visualize data with Generative UI</h4>
<p>Understanding your traffic and security trends is now as easy as asking a question. Agent Lee now features <strong>Generative UI</strong>, allowing it to render inline charts and structured data visualizations directly within the chat interface using your actual account telemetry.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Show me a chart of my traffic over the last 7 days.&quot;</em></li>
<li><em>&quot;What does my error rate look like for the past 24 hours?&quot;</em></li>
<li><em>&quot;Graph my cache hit rate for example.com this week.&quot;</em></li>
</ul>
<hr />
<h4 id="2026-04-15-agentlee-writeops-genui-availability">Availability</h4>
<p>These features are currently available in <strong>Beta</strong> for all users on the <strong>Free plan</strong>. To get started, log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select <strong>Ask AI</strong> in the upper right corner.</p>
<p>To learn more about how to interact with your account using AI, refer to the <a href="/agent-lee/">Agent Lee documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-new-rule-and-application-builders"><a href="/changelog/post/2026-04-15-new-rule-and-application-builders/">New, streamlined creation experience for Access Applications and Gateway Policies</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>The Cloudflare One dashboard now features redesigned builders for two core workflows: creating Gateway policies and configuring self-hosted Access applications.</p>
<h4 id="2026-04-15-new-rule-and-application-builders-gateway-rule-builder">Gateway rule builder</h4>
<p>The Gateway rule builder now features a redesigned user experience, bringing it in line with the Access policy builder experience. Improvements include:</p>
<ul>
<li><strong>Streamlined UX</strong> with clearer states and improved user interactions</li>
<li><strong>Wirefilter editing</strong> for viewing and editing Gateway rules directly from wirefilter expressions</li>
<li><strong>Preview state</strong> to review the impact of your policy in a simple graphic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-rule-builder.png" alt="New Gateway rule builder" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Traffic policies</a>.</p>
<h4 id="2026-04-15-new-rule-and-application-builders-access-application-builder-for-self-hosted-apps">Access application builder for self-hosted apps</h4>
<p>The self-hosted Access application builder now offers a simplified creation workflow with fewer steps from setup to save. Improvements include:</p>
<ul>
<li><strong>New application selection experience</strong> that makes choosing the right application type before you begin easier.</li>
<li><strong>Streamlined creation flow</strong> with fewer clicks to build and save an application</li>
<li><strong>Inline policy creation</strong> for building Access policies directly within the application creation flow</li>
<li><strong>Preview state</strong> to understand how your policies enforce user access before saving</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-application-builder.png" alt="New Access application builder" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/">self-hosted applications</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-dex-consistent-last-seen-timestamps"><a href="/changelog/post/2026-04-15-dex-consistent-last-seen-timestamps/">Last seen timestamp for Cloudflare One Client devices is more consistent</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p>The last seen timestamp for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-logpush-new-fields"><a href="/changelog/post/2026-04-15-logpush-new-fields/">New TenantID and Firewall for AI fields in Logpush datasets</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has added new fields to multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-04-15-logpush-new-fields-tenantid-field">TenantID field</h4>
<p>The following Gateway and Zero Trust datasets now include a <code>TenantID</code> field:</p>
<ul>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid">Gateway DNS</a></strong>: Identifies the tenant ID of the DNS request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid">Gateway HTTP</a></strong>: Identifies the tenant ID of the HTTP request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid">Gateway Network</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid">Zero Trust Network Sessions</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
</ul>
<h4 id="2026-04-15-logpush-new-fields-firewall-for-ai-fields">Firewall for AI fields</h4>
<p>The following datasets now include <a href="/api-shield/security/volumetric-abuse-detection/#firewall-for-ai">Firewall for AI</a> fields:</p>
<ul>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-graphql-analytics-api"><a href="/changelog/post/2026-04-15-graphql-analytics-api/">Privacy Proxy metrics now available via GraphQL Analytics API</a></h2>
<div class="changelog-badges"><span>privacy-proxy</span></div><div class="changelog-body"><p>Privacy Proxy metrics are now queryable through Cloudflare's <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>, the new default method for accessing Privacy Proxy observability data. All metrics are available through a single endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;{ viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-04-15-graphql-analytics-api-available-nodes">Available nodes</h4>
<p>Four GraphQL nodes are now live, providing aggregate metrics across all key dimensions of your Privacy Proxy deployment:</p>
<ul>
<li><strong><code>privacyProxyRequestMetricsAdaptiveGroups</code></strong> — Request volume, error rates, status codes, and proxy status breakdowns.</li>
<li><strong><code>privacyProxyIngressConnMetricsAdaptiveGroups</code></strong> — Client-to-proxy connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyEgressConnMetricsAdaptiveGroups</code></strong> — Proxy-to-origin connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyAuthMetricsAdaptiveGroups</code></strong> — Authentication attempt counts by method and result.</li>
</ul>
<p>All nodes support filtering by time, data center (<code>coloCode</code>), and endpoint, with additional node-specific dimensions such as transport protocol and authentication method.</p>
<h4 id="2026-04-15-graphql-analytics-api-what-this-means-for-existing-opentelemetry-users">What this means for existing OpenTelemetry users</h4>
<p>OpenTelemetry-based metrics export remains available. The GraphQL Analytics API is now the recommended default method — a plug-and-play method that requires no collector infrastructure, saving engineering overhead.</p>
<h4 id="2026-04-15-graphql-analytics-api-learn-more">Learn more</h4>
<ul>
<li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API for Privacy Proxy</a></li>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-waf-release"><a href="/changelog/post/2026-04-15-waf-release/">WAF Release - 2026-04-15</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces a new detection for a critical Remote Code Execution (RCE) vulnerability in Mesop (CVE-2026-33057), alongside protections for high-impact vulnerabilities in Cisco Secure Firewall Management Center (CVE-2026-20079) and FortiClient EMS (CVE-2026-21643). Additionally, this release includes an update to our existing React Server DoS coverage to address recently identified resource exhaustion vectors (CVE-2026-23869).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Cisco Secure FMC (CVE-2026-20079): A vulnerability in the web-based management interface of Cisco Secure Firewall Management Center (FMC) that allows an unauthenticated, remote attacker to execute arbitrary commands or bypass security filters.</p>
</li>
<li>
<p>FortiClient EMS (CVE-2026-21643): A critical vulnerability in the FortiClient EMS permitting unauthorized access or administrative configuration manipulation via crafted HTTP requests.</p>
</li>
<li>
<p>Mesop (CVE-2026-33057): A vulnerability in the Mesop Python-based UI framework where unauthenticated attackers can execute arbitrary code by sending specially crafted, Base64-encoded payloads in the request body.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, gain administrative control over network management infrastructure, or trigger server-side resource exhaustion. Administrators are strongly encouraged to apply official vendor updates.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7767165cda1841b8b6e5abb7aef9415b">aef9415b</code>
</td>
<td>N/A</td>
<td>Cisco Secure FMC - RCE via upgradeReadinessCall - CVE:CVE-2026-20079</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3dd0b2b6f45c4bc08e49bf27ee7be621">ee7be621</code>
</td>
<td>N/A</td>
<td>FortiClient EMS - Pre-Auth SQL Injection - CVE:CVE-2026-21643</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>   
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0e3a6828906c4b24bad318a9c953a72b">c953a72b</code>
</td>
<td>N/A</td>
<td>Mesop - Remote Code Execution - Base64 Payload - CVE:CVE-2026-33057</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d95aa5410d1b4e98bf7a59d150c08f6f">50c08f6f</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 1 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule "React Server - DOS - CVE:CVE-2026-23864 - 1" (ID: <code class="nb-rule-id" title="aaede80b4d414dc89c443cea61680354">61680354</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7d6757e8a28f4853a72b4ce6ebd81645">ebd81645</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - URI (beta)</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5e69d599ad634c81abe36a5f0af34bba">0af34bba</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag  - URI (beta)</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2025-04-14-account-level-dlp-settings"><a href="/changelog/post/2025-04-14-account-level-dlp-settings/">DLP account-level settings</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p><strong>Account-level DLP settings are now available</strong> in Cloudflare One. You can now configure advanced DLP settings at the account level, including OCR, AI context analysis, and payload masking. This provides consistent enforcement across all DLP profiles and simplifies configuration management.</p>
<p>Key changes:</p>
<ul>
<li><strong>Consistent enforcement</strong>: Settings configured at the account level apply to all DLP profiles</li>
<li><strong>Simplified migration</strong>: Settings enabled on any profile are automatically migrated to account level</li>
<li><strong>Deprecation notice</strong>: Profile-level advanced settings will be deprecated in a future release</li>
</ul>
<p><strong>Migration details:</strong></p>
<p>During the migration period, if a setting is enabled on any profile, it will automatically be enabled at the account level. This means profiles that previously had a setting disabled may now have it enabled if another profile in the account had it enabled.</p>
<p>Settings are evaluated using OR logic - a setting is enabled if it is turned on at either the account level or the profile level. However, profile-level settings cannot be enabled when the account-level setting is off.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/dlp-settings/">DLP settings documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-browser-wrangler-commands"><a href="/changelog/post/2026-04-14-browser-wrangler-commands/">Manage Browser Rendering sessions with Wrangler CLI</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Rendering</a> now supports <code>wrangler browser</code> commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler browser create</code></td>
<td>Create a new browser session</td>
</tr>
<tr>
<td><code>wrangler browser close</code></td>
<td>Close a session</td>
</tr>
<tr>
<td><code>wrangler browser list</code></td>
<td>List active sessions</td>
</tr>
<tr>
<td><code>wrangler browser view</code></td>
<td>View a live browser session</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any <a href="/browser-run/cdp/">CDP</a>-compatible client like <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, or <a href="/browser-run/cdp/mcp-clients/">MCP clients</a> to automate browsing, scrape content, or debug remotely.</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create&#10;</code></pre>
<p>Use <code>--keepAlive</code> to set the session keep-alive duration (60-600 seconds):</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create --keepAlive 300&#10;</code></pre>
<p>The <code>view</code> command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.</p>
<p>All commands support <code>--json</code> for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.</p>
<p>For full usage details, refer to the <a href="/browser-run/reference/wrangler-commands/">Wrangler commands documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-cloudflare-mesh"><a href="/changelog/post/2026-04-14-cloudflare-mesh/">Introducing Cloudflare Mesh</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/mesh/">Cloudflare Mesh</a> is now available (<a href="https://blog.cloudflare.com/mesh/">blog post</a>). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="Cloudflare Mesh network map showing nodes and devices connected through Cloudflare" /></p>
<h4 id="2026-04-14-cloudflare-mesh-what-cloudflare-mesh-does">What Cloudflare Mesh does</h4>
<ul>
<li>Assigns a private <a href="/mesh/concepts/#mesh-ips">Mesh IP</a> to every enrolled device and node.</li>
<li>Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.</li>
<li>Supports <a href="/mesh/features/routes/">CIDR routes</a> for subnet routing through Mesh nodes.</li>
<li>Supports <a href="/mesh/features/high-availability/">high availability</a> with active-passive replicas for nodes with routes.</li>
<li>All traffic flows through Cloudflare, so <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>, <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>, and access rules apply to every connection.</li>
</ul>
<h4 id="2026-04-14-cloudflare-mesh-what-changed">What changed</h4>
<ul>
<li><strong>WARP Connector</strong> is now <strong>Cloudflare Mesh</strong>. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.</li>
<li><strong>Peer-to-peer connectivity</strong> is now called <strong>Mesh connectivity</strong> and is part of the Cloudflare Mesh documentation.</li>
<li><strong>Mesh node limit</strong> increased from 10 to <strong>50 per account</strong>.</li>
<li>New <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard experience</a> at <strong>Networking</strong> &gt; <strong>Mesh</strong> with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.</li>
</ul>
<h4 id="2026-04-14-cloudflare-mesh-get-started">Get started</h4>
<p>Refer to the <a href="/mesh/">Cloudflare Mesh documentation</a> to set up your first Mesh network.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-cloudflare-api-token-detections"><a href="/changelog/post/2026-04-14-cloudflare-api-token-detections/">Detect Cloudflare API tokens with DLP</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>The <strong>Credentials and Secrets</strong> DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:</p>
<table>
<thead>
<tr>
<th>Entry name</th>
<th>Token prefix</th>
<th>Detects</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare User API Key</td>
<td><code>cfk_</code></td>
<td>User-scoped API keys</td>
</tr>
<tr>
<td>Cloudflare User API Token</td>
<td><code>cfut_</code></td>
<td>User-scoped API tokens</td>
</tr>
<tr>
<td>Cloudflare Account Owned API Token</td>
<td><code>cfat_</code></td>
<td>Account-scoped API tokens</td>
</tr>
</tbody>
</table>
<p>These detections target the new <a href="/fundamentals/api/get-started/token-formats/">Cloudflare API credential format</a>, which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as <code>Authorization: Bearer</code> headers is required.</p>
<p>Credentials generated before this format change will not be matched by these entries.</p>
<h4 id="2026-04-14-cloudflare-api-token-detections-how-to-enable-cloudflare-api-token-detections">How to enable Cloudflare API token detections</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>DLP</strong> &gt; <strong>DLP Profiles</strong>.</li>
<li>Select the <strong>Credentials and Secrets</strong> profile.</li>
<li>Turn on one or more of the new Cloudflare API token entries.</li>
<li>Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.</li>
</ol>
<p>Example policy:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Credentials and Secrets</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>You can also enable individual entries to scope detection to specific credential types — for example, enabling <strong>Account Owned API Token</strong> detection without enabling <strong>User API Key</strong> detection.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-configurable-payload-log-masking"><a href="/changelog/post/2026-04-14-configurable-payload-log-masking/">Configure how sensitive data appears in DLP payload logs</a></h2>
<div class="changelog-badges"><span>gateway</span><span>dlp</span></div><div class="changelog-body"><p>You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong> and find the <strong>Payload log masking</strong> card.</p>
<p>Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:</p>
<ul>
<li><strong>Full Mask (default):</strong> Masks the match while preserving character count and visual formatting (for example, <code>***-**-****</code> for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.</li>
<li><strong>Partial Mask:</strong> Reveals 25% of the matched content while masking the remainder (for example, <code>***-**-6789</code>).</li>
<li><strong>Clear Text:</strong> Stores the full, unmasked violation for deep investigation (for example, <code>123-45-6789</code>).</li>
</ul>
<p><strong>Important:</strong> The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.</p>
<p><strong>Applies to all enabled detections:</strong> When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">DLP logging options</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-oauth-consent-and-revoke"><a href="/changelog/post/2026-04-14-oauth-consent-and-revoke/">Improved OAuth experience for consent and management</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have <strong>granular control</strong> over which accounts these applications can access, plus the ability to revoke access anytime.</p>
<h4 id="2026-04-14-oauth-consent-and-revoke-what-s-new">What's new</h4>
<h4 id="2026-04-14-oauth-consent-and-revoke-choose-which-accounts-to-authorize">Choose which accounts to authorize</h4>
When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:
- **Account-by-account selection** — Choose exactly which accounts the application can access
- **"All accounts" option** — Still available for trusted tools like Wrangler
This gives you precise control who can access your data.
<h4 id="2026-04-14-oauth-consent-and-revoke-clear-consent-screens">Clear consent screens</h4>
The OAuth consent screen now shows:
- **What the application can access** — Explicit list of permissions being requested
- **Who created the application** — Application owner and contact information  
- **Which accounts you're authorizing** — Checkboxes for account selection
<h4 id="2026-04-14-oauth-consent-and-revoke-revoke-access-anytime">Revoke access anytime</h4>
Manage authorized OAuth applications from your profile:
- **See all connected apps** — View every OAuth application with access to your accounts
- **Review permissions and scope** — Check what each application can do and which accounts it can access
- **Revoke instantly** — Remove access with one click when you no longer need it
To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications](https://dash.cloudflare.com/profile/access-management/authorization)**.
<h4 id="2026-04-14-oauth-consent-and-revoke-why-this-matters">Why this matters</h4>
These updates give you:
- **Granular control** — Authorize apps per-account instead of all-or-nothing
- **Transparency** — Know exactly what you're authorizing before you consent
- **Security** — Limit blast radius by restricting access to only necessary accounts
- **Easy cleanup** — Revoke access when applications are no longer needed
<h4 id="2026-04-14-oauth-consent-and-revoke-learn-more">Learn more</h4>
Read more about these improvements in our blog post: [Improving the OAuth consent experience](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-bigquery-dashboard-support"><a href="/changelog/post/2026-04-14-bigquery-dashboard-support/">Logpush to BigQuery — Cloudflare dashboard support</a></h2>
<div class="changelog-badges"><span>logpush</span><span>logs</span></div><div class="changelog-body"><p>You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.</p>
<p>Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the <strong>Logpush</strong> page in the Cloudflare dashboard by selecting <strong>Google BigQuery</strong> as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Enable Logpush to Google BigQuery</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-radar-citations"><a href="/changelog/post/2026-04-14-radar-citations/">Generate citations on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> shareable widgets now include a <strong>generate citation</strong> action, making it easier to reference <a href="https://radar.cloudflare.com">Cloudflare Radar</a> data in research papers and other publications.</p>
<p><img src="/assets/upstream/images/radar/citation-action-icon.png" alt="Screenshot of the generate citation icon in the widget action bar" /></p>
<p>Select the citation icon to open a modal with five supported citation styles:</p>
<ul>
<li><strong>BibTeX</strong></li>
<li><strong>APA</strong></li>
<li><strong>MLA</strong></li>
<li><strong>Chicago</strong></li>
<li><strong>RIS</strong></li>
</ul>
<p><img src="/assets/upstream/images/radar/citation-modal.png" alt="Screenshot of the citation modal with format options" /></p>
<p>Explore the feature on any shareable widget at <a href="https://radar.cloudflare.com">Cloudflare Radar</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-email-obfuscation-defer"><a href="/changelog/post/2026-04-14-email-obfuscation-defer/">Email obfuscation decode script is now non-render-blocking</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>The decode script injected by <a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a> now loads with the <code>defer</code> attribute. This means the script no longer blocks page rendering. It downloads in parallel with HTML parsing and executes after the document is fully parsed, before the <code>DOMContentLoaded</code> event.</p>
<p>This improves page loading performance, contributing to better Core Web Vitals, for all zones with Email Address Obfuscation on. No action is required.</p>
<p>If you have custom JavaScript that depends on email addresses being decoded at a specific point during page load, note that the decode script now executes after HTML parsing completes rather than inline during parsing.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-14">Apr 14, 2026</time><div>
<h2 id="post-2026-04-14-vpc-networks"><a href="/changelog/post/2026-04-14-vpc-networks/">VPC Networks and Cloudflare Mesh support now in public beta</a></h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> bindings, which scope each binding to a specific host and port.</p>
<p>You can bind to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> by <code>tunnel_id</code> to reach any service on the network where that tunnel is running, or bind to your <a href="/mesh/">Cloudflare Mesh</a> network using <code>cf1:network</code> to reach any Mesh node, client device, or subnet route in your account:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17822.md")</div>
<p>At runtime, <code>fetch()</code> routes through the network to reach the service at the IP and port you specify:</p>
<pre tabindex="0"><code class="language-js">const response = await env.MESH.fetch(&quot;http://10.0.1.50:8080/api/data&quot;);&#10;</code></pre>
<p>For configuration options and examples, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and <a href="/workers-vpc/examples/connect-to-cloudflare-mesh/">Connect Workers to Cloudflare Mesh</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-13">Apr 13, 2026</time><div>
<h2 id="post-2026-04-13-containers-sandbox-ga"><a href="/changelog/post/2026-04-13-containers-sandbox-ga/">Containers and Sandboxes are now generally available</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Cloudflare <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> are now generally available.</p>
<p>Containers let you run more workloads on the Workers platform, including resource-intensive applications, different languages, and CLI tools that need full Linux environments.</p>
<p>Since the initial launch of Containers, there have been significant improvements to Containers' performance, stability, and feature set. Some highlights include:</p>
<ul>
<li><a href="/changelog/post/2026-02-25-higher-container-resource-limits/">Higher limits</a> allow you to run thousands of containers concurrently.</li>
<li><a href="/changelog/post/2025-11-21-new-cpu-pricing/">Active-CPU pricing</a> means that you only pay for used CPU cycles.</li>
<li><a href="/changelog/post/2026-03-26-outbound-workers/">Easy connections to Workers and other bindings</a> via hostnames help you extend your Containers with additional functionality.</li>
<li><a href="/changelog/post/2026-03-24-docker-hub-images/">Docker Hub support</a> makes it easy to use your existing images and registries.</li>
<li><a href="/changelog/post/2026-03-12-ssh-support/">SSH support</a> helps you access and debug issues in live containers.</li>
</ul>
<p>The <a href="/sandbox/">Sandbox SDK</a> provides isolated environments for running untrusted code securely, with a simple TypeScript API for executing commands, managing files, and exposing services. This makes it easier to secure and manage your agents at scale. Some additions since launch include:</p>
<ul>
<li><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Live preview URLs</a> so agents can run long-lived services and verify in-flight changes.</li>
<li><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Persistent code interpreters</a> for Python, JavaScript, and TypeScript, with rich structured outputs.</li>
<li><a href="/changelog/post/2026-02-09-pty-terminal-support/">Interactive PTY terminals</a> for real browser-based terminal access with multiple isolated shells per sandbox.</li>
<li><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore APIs</a> to snapshot a workspace and quickly restore an agent's coding session without repeating expensive setup steps.</li>
<li><a href="/changelog/post/2026-03-03-sandbox-watch-file-events/">Real-time filesystem watching</a> so apps and agents can react immediately to file changes inside a sandbox.</li>
</ul>
<p>For more information, refer to <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandbox SDK</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-13">Apr 13, 2026</time><div>
<h2 id="post-2026-04-13-sandbox-outbound-workers-tls-auth"><a href="/changelog/post/2026-04-13-sandbox-outbound-workers-tls-auth/">Secure credential injection and dynamic egress policies for Sandboxes</a></h2>
<div class="changelog-badges"><span>containers</span><span>agents</span></div><div class="changelog-body"><p>Outbound Workers for <a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support zero-trust credential injection, TLS interception, allow/deny lists, and dynamic per-instance egress policies. These features give platforms running agentic workloads full control over what leaves the sandbox, without exposing secrets to untrusted workloads, like user-generated code or coding agents.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-credential-injection">Credential injection</h4>
<p>Because outbound handlers run in the Workers runtime, outside the sandbox, they can hold secrets the sandbox never sees. A sandboxed workload can make a plain request, and credentials are transparently attached before a request is forwarded upstream.</p>
<p>For instance, you could run an agent in a sandbox and ensure that any requests it makes to Github are authenticated.
But it will never be able to access the credentials:</p>
<pre tabindex="0"><code class="language-ts">export class MySandbox extends Sandbox {}&#10;&#10;MySandbox.outboundByHost = {&#10;	&quot;github.com&quot;: (request: Request, env: Env, ctx: OutboundHandlerContext) =&gt; {&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, env.SECRET);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>You can easily inject unique credentials for different instances
by using <code>ctx.containerId</code>:</p>
<pre tabindex="0"><code class="language-ts">MySandbox.outboundByHost = {&#10;	&quot;my-internal-vcs.dev&quot;: async (&#10;		request: Request,&#10;		env: Env,&#10;		ctx: OutboundHandlerContext,&#10;	) =&gt; {&#10;		const authKey = await env.KEYS.get(ctx.containerId);&#10;&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, authKey);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>No token is ever passed into the sandbox. You can rotate secrets in the Worker environment
and every request will pick them up immediately.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-tls-interception">TLS interception</h4>
<p>Outbound Workers now intercept HTTPS traffic. A unique ephemeral certificate authority (CA) and private key are created for each sandbox instance. The CA is placed into the sandbox and trusted by default. The ephemeral private key never leaves the container runtime sidecar process and is never shared across instances.</p>
<p>With TLS interception active, outbound Workers can act as a transparent proxy for both HTTP and HTTPS traffic.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-allow-and-deny-hosts">Allow and deny hosts</h4>
<p>Easily filter outbound traffic with <code>allowedHosts</code> and <code>deniedHosts</code>. When <code>allowedHosts</code> is set, it becomes a deny-by-default allowlist. Both properties support glob patterns.</p>
<pre tabindex="0"><code class="language-ts">export class MySandbox extends Sandbox {&#10;	allowedHosts = [&quot;github.com&quot;, &quot;npmjs.org&quot;];&#10;}&#10;</code></pre>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-dynamic-outbound-handlers">Dynamic outbound handlers</h4>
<p>Define named outbound handlers then apply or remove them at runtime using <code>setOutboundHandler()</code> or <code>setOutboundByHost()</code>. This lets you change egress policy for a running sandbox without restarting it.</p>
<pre tabindex="0"><code class="language-ts">export class MySandbox extends Sandbox {}&#10;&#10;MySandbox.outboundHandlers = {&#10;	allowHosts: async (req: Request, env: Env, ctx: OutboundHandlerContext ) =&gt; {&#10;		const url = new URL(req.url);&#10;		if (ctx.params.allowedHostnames.includes(url.hostname)) {&#10;			return fetch(req);&#10;		}&#10;		return new Response(null, { status: 403 });&#10;	},&#10;&#10;	noHttp: async () =&gt; {&#10;		return new Response(null, { status: 403 });&#10;	},&#10;};&#10;</code></pre>
<p>Apply handlers programmatically from your Worker:</p>
<pre tabindex="0"><code class="language-ts">const sandbox = getSandbox(env.Sandbox, userId);&#10;&#10;// Open network for setup&#10;await sandbox.setOutboundHandler(&quot;allowHosts&quot;, {&#10;	allowedHostnames: [&quot;github.com&quot;, &quot;npmjs.org&quot;],&#10;});&#10;await sandbox.exec(&quot;npm install&quot;);&#10;&#10;// Lock down after setup&#10;await sandbox.setOutboundHandler(&quot;noHttp&quot;);&#10;</code></pre>
<p>Handlers accept <code>params</code>, so you can customize behavior per instance without defining separate handler functions.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-get-started">Get started</h4>
<p>Upgrade to <code>@cloudflare/containers@0.3.0</code> or <code>@cloudflare/sandbox@0.8.9</code> to use these features.</p>
<p>For more details, refer to <a href="/sandbox/guides/outbound-traffic/">Sandbox outbound traffic</a> and <a href="/containers/guides/outbound-traffic/">Container outbound traffic</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-13">Apr 13, 2026</time><div>
<h2 id="post-2026-04-13-local-explorer"><a href="/changelog/post/2026-04-13-local-explorer/">Local Explorer for local resource data</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Local Explorer is a browser-based interface and REST API for viewing and editing local resource data during development. It removes the need to write throwaway scripts or dig through <code>.wrangler/state</code> to understand what data your Worker has stored locally.</p>
<p>Local Explorer is available in Wrangler 4.82.1+ and the Cloudflare Vite plugin 1.32.0+. Start a local development session and press <code>e</code> in your terminal, or navigate to <code>/cdn-cgi/local/explorer</code> on your local dev server.</p>
<h4 id="2026-04-13-local-explorer-supported-resources">Supported resources</h4>
<p>Local Explorer supports five resource types and works across multiple workers running locally:</p>
<ul>
<li><strong><a href="/kv/">KV</a></strong> — Browse keys, view values and metadata, create, update, and delete key-value pairs.</li>
<li><strong><a href="/r2/">R2</a></strong> — List objects, view metadata, upload files, and delete objects. Supports directory views and multi-select.</li>
<li><strong><a href="/d1/">D1</a></strong> — Browse tables and rows, run arbitrary SQL queries, and edit schemas in a full data studio.</li>
<li><strong><a href="/durable-objects/">Durable Objects</a></strong> (SQLite storage) — Browse individual object SQLite tables, run SQL queries, and edit schemas.</li>
<li><strong><a href="/workflows/">Workflows</a></strong> — List instances, view status and step history, trigger new runs, and pause, resume, restart, or terminate instances.</li>
</ul>
<h4 id="2026-04-13-local-explorer-openapi-powered-rest-api">OpenAPI-powered REST API</h4>
<p>Local Explorer exposes a REST API at <code>/cdn-cgi/local/explorer/api</code> that provides programmatic access to the same operations available in the browser. The root endpoint returns an <a href="https://www.openapis.org/">OpenAPI specification</a> describing all available endpoints, parameters, and response formats.</p>
<pre tabindex="0"><code class="language-sh">curl http://localhost:8787/cdn-cgi/local/explorer/api&#10;</code></pre>
<p>Point an AI coding agent at <code>/cdn-cgi/local/explorer/api</code> and it can discover and interact with your local resources without manual setup. This enables iterative development loops where an agent can populate test data in KV or D1, inspect Durable Object state, trigger Workflow runs, or upload files to R2.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-10">Apr 10, 2026</time><div>
<h2 id="post-2026-04-10-canvas-remoting-performance"><a href="/changelog/post/2026-04-10-canvas-remoting-performance/">Canvas Remoting optimizes performance for productivity applications</a></h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>Remote Browser Isolation now supports <strong>Canvas Remoting</strong>, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.</p>
<h4 id="2026-04-10-canvas-remoting-performance-key-improvements">Key improvements</h4>
<ul>
<li><strong>10x bandwidth reduction:</strong> Microsoft Word and other Office apps use 90% less bandwidth</li>
<li><strong>Smooth performance:</strong> Google Sheets maintains consistent 30fps rendering</li>
<li><strong>Responsive terminals:</strong> Web-based development environments and AI notebooks work in real-time</li>
<li><strong>Zero configuration:</strong> Enabled by default for all Browser Isolation customers</li>
</ul>
<h4 id="2026-04-10-canvas-remoting-performance-how-it-works">How it works</h4>
<p>Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:</p>
<ol>
<li>Captures Canvas draw commands at the source</li>
<li>Converts them to lightweight vector instructions</li>
<li>Renders Canvas content on the client</li>
</ol>
<p>This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.</p>
<h4 id="2026-04-10-canvas-remoting-performance-managing-canvas-remoting">Managing Canvas Remoting</h4>
<p>To temporarily disable for troubleshooting:</p>
<ul>
<li>Right-click the isolated webpage background</li>
<li>Select <strong>Disable Canvas Remoting</strong></li>
<li>Re-enable the same way by selecting <strong>Enable Canvas Remoting</strong></li>
</ul>
<h4 id="2026-04-10-canvas-remoting-performance-limitations">Limitations</h4>
<p>Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to <a href="/cloudflare-one/remote-browser-isolation/canvas-remoting/">Canvas Remoting</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-10">Apr 10, 2026</time><div>
<h2 id="post-2026-04-10-browser-rendering-cdp-endpoint"><a href="/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/">Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Rendering</a> now exposes the <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a>, the low-level protocol that powers browser automation. The growing ecosystem of CDP-based agent tools, along with existing CDP automation scripts, can now use Browser Rendering directly.</p>
<p>Any CDP-compatible client, including <a href="/browser-run/cdp/puppeteer/">Puppeteer</a> and <a href="/browser-run/cdp/playwright/">Playwright</a>, can connect from any environment, whether that is <a href="/workers/">Cloudflare Workers</a>, your local machine, or a cloud environment. All you need is your Cloudflare API key.</p>
<p>For any existing CDP script, switching to Browser Rendering is a one-line change:</p>
<pre tabindex="0"><code class="language-js">const puppeteer = require(&quot;puppeteer-core&quot;);&#10;&#10;const browser = await puppeteer.connect({&#10;	browserWSEndpoint: `wss://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/browser-rendering/devtools/browser?keep_alive=600000`,&#10;	headers: { Authorization: `Bearer ${API_TOKEN}` },&#10;});&#10;&#10;const page = await browser.newPage();&#10;await page.goto(&quot;https://example.com&quot;);&#10;console.log(await page.title());&#10;await browser.close();&#10;</code></pre>
<p>Additionally, MCP clients like Claude Desktop, Claude Code, Cursor, and OpenCode can now use Browser Rendering as their remote browser via the <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">chrome-devtools-mcp</a> package.</p>
<p>Here is an example of how to configure Browser Rendering for Claude Desktop:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To get started, refer to the <a href="/browser-run/cdp/">CDP documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-10">Apr 10, 2026</time><div>
<h2 id="post-2026-04-10-secret-scanning-support"><a href="/changelog/post/2026-04-10-secret-scanning-support/">API tokens now detectable by secret scanning tools</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare API tokens now include <strong>identifiable patterns</strong> that enable secret scanning tools to automatically detect them when leaked in code repositories, configuration files, or other public locations.</p>
<h4 id="2026-04-10-secret-scanning-support-what-changed">What changed</h4>
<p>API tokens generated by Cloudflare now follow a standardized format that secret scanning tools can recognize. When a Cloudflare token is accidentally committed to GitHub, GitLab, or another platform with secret scanning enabled, the tool will flag it and alert you.</p>
<h4 id="2026-04-10-secret-scanning-support-why-this-matters">Why this matters</h4>
<p>Leaked credentials are a common security risk. By making Cloudflare tokens detectable by scanning tools, you can:</p>
<ul>
<li><strong>Detect leaks faster</strong> — Get notified immediately when a token is exposed.</li>
<li><strong>Reduce risk window</strong> — Exposed tokens are deactivated immediately, before they can be exploited.</li>
<li><strong>Automate security</strong> — Leverage existing secret scanning infrastructure without additional configuration.</li>
</ul>
<h4 id="2026-04-10-secret-scanning-support-what-happens-when-a-leak-is-detected">What happens when a leak is detected</h4>
<p>When a third-party secret scanning tool detects a leaked Cloudflare API token:</p>
<ol>
<li><strong>Cloudflare immediately deactivates the token</strong> to prevent unauthorized access.</li>
<li><strong>The token creator receives an email notification</strong> alerting them to the leak.</li>
<li><strong>The token is marked as &quot;Exposed&quot;</strong> in the Cloudflare dashboard.</li>
<li><strong>You can then roll or delete the token</strong> from the token management pages.</li>
</ol>
<h4 id="2026-04-10-secret-scanning-support-supported-platforms">Supported platforms</h4>
<ul>
<li><strong>GitHub Secret Scanning</strong> — Automatically enabled for public repositories</li>
</ul>
<p>For more information on token formats and secret scanning, refer to <a href="/fundamentals/api/get-started/token-formats/">API token formats</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/18/">Previous</a><span>Page 19 of 50</span><a class="pagination-next" rel="next" href="/changelog/20/">Next</a></nav>
</div>
