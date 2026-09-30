---
cp9:
  canonical: https://developers.cloudflare.com/changelog/21/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 21 | Cloudflare Docs
  head_html: <title>Changelog - page 21 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/21/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 21"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/21/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/21/#page","headline":"Changelog - page 21 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/21/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/21/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-logs-ui-refresh"><a href="/changelog/post/2026-04-01-logs-ui-refresh/">Logs UI refresh</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span><span>gateway</span></div><div class="changelog-body"><p>Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-new-logs-ui.png" alt="Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options" /></p>
<p>The updated UI includes:</p>
<ul>
<li><strong>Filter by field</strong> - Select any field value to add it as a filter and narrow down your results.</li>
<li><strong>Customizable fields</strong> - Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.</li>
<li><strong>View details</strong> - Select a timestamp to view the full details of a log entry.</li>
<li><strong>Switch to classic view</strong> - Return to the previous log viewer interface if needed.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-radar-routing-section"><a href="/changelog/post/2026-04-01-radar-routing-section/">Routing Section Expansion on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now features an expanded <a href="https://radar.cloudflare.com/routing">Routing section</a> with dedicated sub-pages, providing a more organized and in-depth view of the global routing ecosystem. This restructuring lays the groundwork for additional routing features and widgets coming in the near future.</p>
<h4 id="2026-04-01-radar-routing-section-dedicated-sub-pages">Dedicated sub-pages</h4>
<p>The single Routing page has been split into three focused sub-pages:</p>
<ul>
<li><a href="https://radar.cloudflare.com/routing"><strong>Overview</strong></a> — Routing statistics, IP address space trends, BGP announcements, and the new Top 100 ASes ranking.</li>
<li><a href="https://radar.cloudflare.com/routing/rpki"><strong>RPKI</strong></a> — RPKI validation status, ASPA deployment trends, and per-ASN ASPA provider details.</li>
<li><a href="https://radar.cloudflare.com/routing/anomalies"><strong>Anomalies</strong></a> — BGP route leaks, origin hijacks, and Multi-Origin AS (MOAS) conflicts.</li>
</ul>
<p><img src="/assets/upstream/images/radar/routing-section-menu.png" alt="Screenshot of the routing section menu" /></p>
<h4 id="2026-04-01-radar-routing-section-new-widgets">New widgets</h4>
<p>The routing overview now includes a <strong>Top 100 ASes</strong> table ranking autonomous systems by customer cone size, IPv4 address space, or IPv6 address space. Users can switch between rankings using a segmented control.</p>
<p><img src="/assets/upstream/images/radar/top-100-ases-table.png" alt="Screenshot of the top-100 ASes table" /></p>
<p>The RPKI sub-page introduces a <strong>RPKI validation</strong> view for per-ASN pages, showing prefixes grouped by RPKI validation status (Valid, Invalid, Unknown) with visibility scores.</p>
<p><img src="/assets/upstream/images/radar/rpki-validation-view.png" alt="Screenshot of the RPKI validation view" /></p>
<h4 id="2026-04-01-radar-routing-section-improved-ip-address-space-chart">Improved IP address space chart</h4>
<p>The <a href="https://radar.cloudflare.com/routing">IP address space</a> chart now displays both IPv4 and IPv6 trends stacked vertically and is available on global, country, and AS views.</p>
<p><img src="/assets/upstream/images/radar/combined-ipv4-ipv6-space.png" alt="Screenshot of the IPv4 and IPv6 combined IP space chart" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/routing">Radar routing section</a> to explore the data, and stay tuned for more routing insights coming soon.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-quic-rtt-delivery-rate-fields"><a href="/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/">New QUIC RTT and delivery rate fields</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing <a href="/ruleset-engine/rules-language/fields/reference/"><code>cf.timings.client_tcp_rtt_msec</code></a> field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.</p>
<p>Previously, QUIC RTT and delivery rate data was only available via the <code>Server-Timing: cfL4</code> response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.</p>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.client_quic_rtt_msec</code></td>
<td>Integer</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns <code>0</code> for TCP connections.</td>
</tr>
<tr>
<td><code>cf.edge.l4.delivery_rate</code></td>
<td>Integer</td>
<td>The most recent data delivery rate estimate for the client connection, in bytes per second. Returns <code>0</code> when L4 statistics are not available for the request.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-route-slow-connections-to-a-lightweight-origin">Example: Route slow connections to a lightweight origin</h4>
<p>Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.timings.client_tcp_rtt_msec &gt; 200 or cf.timings.client_quic_rtt_msec &gt; 200&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>X-High-Latency</code></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-match-low-bandwidth-connections">Example: Match low-bandwidth connections</h4>
<pre tabindex="0"><code class="language-txt">cf.edge.l4.delivery_rate &gt; 0 and cf.edge.l4.delivery_rate &lt; 100000&#10;</code></pre>
<p>For more information, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a> and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-deploy-hooks"><a href="/changelog/post/2026-04-01-deploy-hooks/">Deploy Hooks are now available for Workers Builds</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.</p>
<p>Each Deploy Hook is a unique URL tied to a specific branch. Send it a <code>POST</code> and your Worker builds and deploys.</p>
<pre tabindex="0"><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/&lt;DEPLOY_HOOK_ID&gt;&quot;&#10;</code></pre>
<p>To create one, go to <strong>Workers &amp; Pages</strong> &gt; your Worker &gt; <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Deploy Hooks</strong>.</p>
<p>Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> can rebuild your project on a schedule:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17803.md")</div>
<p>You can also use Deploy Hooks to <a href="/workers/ci-cd/builds/deploy-hooks/#cms-integration">rebuild when your CMS publishes new content</a> or <a href="/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command">deploy from a Slack slash command</a>.</p>
<h4 id="2026-04-01-deploy-hooks-built-in-optimizations">Built-in optimizations</h4>
<ul>
<li><strong>Automatic deduplication</strong>: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.</li>
<li><strong>Last triggered</strong>: The dashboard shows when each hook was last triggered.</li>
<li><strong>Build source</strong>: Your Worker's build history shows which Deploy Hook started each build by name.</li>
</ul>
<p>Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Limits &amp; pricing</a>.</p>
<p>To get started, read the <a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-l4-transport-telemetry-fields"><a href="/changelog/post/2026-04-01-l4-transport-telemetry-fields/">New L4 transport telemetry fields in Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Three new properties are now available on <code>request.cf</code> in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.</p>
<p>Previously, this telemetry was only available via the <code>Server-Timing: cfL4</code> response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.</p>
<h4 id="2026-04-01-l4-transport-telemetry-fields-new-properties">New properties</h4>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>clientTcpRtt</code></td>
<td>number | undefined</td>
<td>The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, <code>22</code>.</td>
</tr>
<tr>
<td><code>clientQuicRtt</code></td>
<td>number | undefined</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, <code>42</code>.</td>
</tr>
<tr>
<td><code>edgeL4</code></td>
<td>Object | undefined</td>
<td>Layer 4 transport statistics. Contains <code>deliveryRate</code> (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, <code>123456</code>.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-l4-transport-telemetry-fields-example-log-connection-quality-metrics">Example: Log connection quality metrics</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const cf = request.cf;&#10;&#10;    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;&#10;    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;&#10;    const transport = cf.clientTcpRtt ? &quot;TCP&quot; : &quot;QUIC&quot;;&#10;&#10;    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;X-Client-RTT&quot;, String(rtt));&#10;    headers.set(&quot;X-Delivery-Rate&quot;, String(deliveryRate));&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/request/">Workers Runtime APIs: Request</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-31">Mar 31, 2026</time><div>
<h2 id="post-2026-03-31-internal-dns-open-beta"><a href="/changelog/post/2026-03-31-internal-dns-open-beta/">Internal DNS - now in open beta</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Internal DNS is now in open beta.</p>
<h4 id="2026-03-31-internal-dns-open-beta-who-can-use-it">Who can use it?</h4>
Internal DNS is bundled as a part of Cloudflare Gateway and is now available to every Enterprise customer with one of the following subscriptions:
<ul>
<li>Cloudflare Zero Trust Enterprise</li>
<li>Cloudflare Gateway Enterprise</li>
</ul>
<p>To learn more and get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-30">Mar 30, 2026</time><div>
<h2 id="post-2026-03-30-waf-release"><a href="/changelog/post/2026-03-30-waf-release/">WAF Release - 2026-03-30</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new detections for a critical authentication bypass vulnerability in Fortinet products (CVE-2025-59718), alongside three new generic detection rules designed to identify and block HTTP Parameter Pollution attempts. Additionally, this release includes targeted protection for a high-impact unrestricted file upload vulnerability in Magento and Adobe Commerce.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2025-59718: An improper cryptographic signature verification vulnerability in Fortinet FortiOS, FortiProxy, and FortiSwitchManager. This may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication using a maliciously crafted SAML message, if that feature is enabled on the device.</p>
</li>
<li>
<p>Magento 2 - Unrestricted File Upload: A critical flaw in Magento and Adobe Commerce allows unauthenticated attackers to bypass security checks and upload malicious files to the server, potentially leading to Remote Code Execution (RCE).</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of the Fortinet and Magento vulnerabilities could allow unauthenticated attackers to gain administrative control or deploy webshells, leading to complete server compromise and data theft.</p>
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
        <code class="nb-rule-id" title="4f7d513cea424c2a853881982f7f95e9">2f7f95e9</code>
</td>
<td>N/A</td>
<td>Generic Rules - Parameter Pollution - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="60d023f3be414d379428add3319731a4">319731a4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Parameter Pollution - Header - Form</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2dde02d792ad41ec8fd65c2bdef262dd">def262dd</code>
</td>
<td>N/A</td>
<td>Generic Rules - Parameter Pollution - URI</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab8a96ed13034d56a81a79e570a36147">70a36147</code>
</td>
<td>N/A</td>
<td>Magento 2 - Unrestricted file upload</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0a13a38dd81c44688950444e2ffcca9f">2ffcca9f</code>
</td>
<td>N/A</td>
<td>Fortinet FortiCloud SSO - Authentication Bypass - CVE:CVE-2025-59718</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>    
</tbody>    
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-27">Mar 27, 2026</time><div>
<h2 id="post-2026-03-27-rfc9440-mtls-fields"><a href="/changelog/post/2026-03-27-rfc9440-mtls-fields/">New RFC 9440 mTLS certificate fields in Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Four new fields are now available on <code>request.cf.tlsClientAuth</code> in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format — the same standard format used by the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.</p>
<h4 id="2026-03-27-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>certRFC9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format (<code>:base64-DER:</code>). Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>certRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted from <code>certRFC9440</code>.</td>
</tr>
<tr>
<td><code>certChainRFC9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>certChainRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted from <code>certChainRFC9440</code>.</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-27-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin">Example: forwarding client certificate headers to your origin</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const tls = request.cf.tlsClientAuth;&#10;&#10;    // Only forward if cert was verified and chain is complete&#10;    if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {&#10;      return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;    }&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;Client-Cert&quot;, tls.certRFC9440);&#10;    headers.set(&quot;Client-Cert-Chain&quot;, tls.certChainRFC9440);&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/ssl/client-certificates/client-certificate-variables/#workers-variables">Client certificate variables</a> and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-26">Mar 26, 2026</time><div>
<h2 id="post-2026-03-26-mcp-portal-code-mode"><a href="/changelog/post/2026-03-26-mcp-portal-code-mode/">Code Mode for MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>, a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.</p>
<p>To turn it off, edit the portal in <strong>Access controls</strong> &gt; <strong>AI controls</strong> and turn off <strong>Code Mode</strong> under <strong>Basic information</strong>.</p>
<p>When Code Mode is active, the portal exposes a single <code>code</code> tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods for each upstream tool. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, keeping authentication credentials and environment variables out of the model context.</p>
<p>To use Code Mode, append <code>?codemode=search_and_execute</code> to your portal URL when connecting from an MCP client:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode">Code Mode</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-26">Mar 26, 2026</time><div>
<h2 id="post-2026-03-26-mcp-portal-context-optimization"><a href="/changelog/post/2026-03-26-mcp-portal-context-optimization/">Context optimization for MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the <code>optimize_context</code> query parameter to the portal URL.</p>
<h4 id="2026-03-26-mcp-portal-context-optimization-minimize-tools"><code>minimize_tools</code></h4>
<p>Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special <code>query</code> tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&#10;</code></pre>
<h4 id="2026-03-26-mcp-portal-context-optimization-search-and-execute"><code>search_and_execute</code></h4>
<p>Hides all upstream tools and exposes only two tools: <code>query</code> and <code>execute</code>. The <code>query</code> tool searches and retrieves tool definitions. The <code>execute</code> tool runs the upstream tools in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context">Optimize context</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-26">Mar 26, 2026</time><div>
<h2 id="post-2026-03-26-outbound-workers"><a href="/changelog/post/2026-03-26-outbound-workers/">Easily connect Containers and Sandboxes to Workers</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> now support connecting directly to Workers over HTTP. This allows you to call Workers
functions and <a href="/workers/runtime-apis/bindings/">bindings</a>, like <a href="/kv">KV</a> or <a href="/r2/">R2</a>, from within the container at specific hostnames.</p>
<h4 id="2026-03-26-outbound-workers-run-worker-code">Run Worker code</h4>
<p>Define an <code>outbound</code> handler to capture any HTTP request or use <code>outboundByHost</code> to capture requests to individual hostnames and IPs.</p>
<pre tabindex="0"><code class="language-js">export class MyApp extends Sandbox {}&#10;&#10;MyApp.outbound = async (request, env, ctx) =&gt; {&#10;	// you can run arbitrary functions defined in your Worker on any HTTP request&#10;	return await someWorkersFunction(request.body);&#10;};&#10;&#10;MyApp.outboundByHost = {&#10;	&quot;my.worker&quot;: async (request, env, ctx) =&gt; {&#10;		return await anotherFunction(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>In this example, requests from the container to <code>http://my.worker</code> will run the function defined within <code>outboundByHost</code>,
and any other HTTP requests will run the <code>outbound</code> handler. These handlers run entirely inside the Workers runtime,
outside of the container sandbox.</p>
<h4 id="2026-03-26-outbound-workers-access-workers-bindings">Access Workers bindings</h4>
<p>Each handler has access to <code>env</code>, so it can call any binding set in <a href="/workers/wrangler/configuration/#bindings">Wrangler config</a>.
Code inside the container makes a standard HTTP request to that hostname and the outbound Worker translates it into a binding call.</p>
<pre tabindex="0"><code class="language-js">export class MyApp extends Sandbox {}&#10;&#10;MyApp.outboundByHost = {&#10;	&quot;my.kv&quot;: async (request, env, ctx) =&gt; {&#10;		const key = new URL(request.url).pathname.slice(1);&#10;		const value = await env.KV.get(key);&#10;		return new Response(value ?? &quot;&quot;, { status: value ? 200 : 404 });&#10;	},&#10;	&quot;my.r2&quot;: async (request, env, ctx) =&gt; {&#10;		const key = new URL(request.url).pathname.slice(1);&#10;		const object = await env.BUCKET.get(key);&#10;		return new Response(object?.body ?? &quot;&quot;, { status: object ? 200 : 404 });&#10;	},&#10;};&#10;</code></pre>
<p>Now, from inside the container sandbox, <code>curl http://my.kv/some-key</code> will access <a href="/kv">Workers KV</a> and <code>curl http://my.r2/some-object</code> will access <a href="/r2/">R2</a>.</p>
<h4 id="2026-03-26-outbound-workers-access-durable-object-state">Access Durable Object state</h4>
<p>Use <code>ctx.containerId</code> to reference the container's automatically provisioned <a href="/durable-objects">Durable Object</a>.</p>
<pre tabindex="0"><code class="language-js">export class MyContainer extends Container {}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;get-state.do&quot;: async (request, env, ctx) =&gt; {&#10;		const id = env.MY_CONTAINER.idFromString(ctx.containerId);&#10;		const stub = env.MY_CONTAINER.get(id);&#10;		return stub.getStateForKey(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>This provides an easy way to associate state with any container instance, and includes a <a href="/durable-objects/get-started/#2-write-a-durable-object-class-using-sql-api">built-in SQLite database</a>.</p>
<h4 id="2026-03-26-outbound-workers-get-started-today">Get Started Today</h4>
<p>Upgrade to <code>@cloudflare/containers</code> version 0.2.0 or later, or <code>@cloudflare/sandbox</code> version 0.8.0 or later to use outbound Workers.</p>
<p>Refer to <a href="/containers/guides/outbound-traffic/">Containers outbound traffic</a> and <a href="/sandbox/guides/outbound-traffic/">Sandboxes outbound traffic</a> for more details and examples.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-26">Mar 26, 2026</time><div>
<h2 id="post-2026-03-26-streaming-zip-handler"><a href="/changelog/post/2026-03-26-streaming-zip-handler/">Streaming ZIP file scanning removes per-file size limits</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.</p>
<p>Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.</p>
<p>This improvement is automatic — no configuration changes are required.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-26">Mar 26, 2026</time><div>
<h2 id="post-2026-03-26-durable-object-id-jurisdiction"><a href="/changelog/post/2026-03-26-durable-object-id-jurisdiction/">Access Durable Object jurisdiction via `ctx.id.jurisdiction`</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p><code>ctx.id.jurisdiction</code> inside a Durable Object now reports the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the object was created in — for example <code>&quot;eu&quot;</code> when accessed through <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)</code> — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve <code>jurisdiction</code>, refer to the <a href="/durable-objects/api/id/#jurisdiction">Durable Object ID documentation</a>.</p>
<pre tabindex="0"><code class="language-js">export class RegionalRoom extends DurableObject {&#10;	async fetch(request) {&#10;		// &quot;eu&quot; when accessed through env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)&#10;		const region = this.ctx.id.jurisdiction;&#10;		return new Response(`Hello from ${region ?? &quot;the default region&quot;}!`);&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const stub = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have <code>jurisdiction</code> stored; to backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-26">Mar 26, 2026</time><div>
<h2 id="post-2026-03-26-url-scanner-improvements"><a href="/changelog/post/2026-03-26-url-scanner-improvements/">URL Scanner improvements on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> ships several improvements to the <a href="https://radar.cloudflare.com/scan">URL Scanner</a> that make scan reports more informative and easier to share:</p>
<ul>
<li><strong>Live screenshots</strong> — the summary card now includes an option to capture a live screenshot of the scanned URL on demand using the <a href="/browser-run/">Browser Rendering</a> API.</li>
<li><strong>Save as PDF</strong> — a new button generates a print-optimized document aggregating all tab contents (Summary, Security, Network, Behavior, and Indicators) into a single file.</li>
<li><strong>Download as JSON</strong> — raw scan data is available as a JSON download for programmatic use.</li>
<li><strong>Redesigned summary layout</strong> — page information and security details are now displayed side by side with the screenshot, with a layout that adapts to narrower viewports.</li>
<li><strong>File downloads</strong> — downloads are separated into a dedicated card with expandable rows showing each file's source URL and SHA256 hash.</li>
<li><strong>Detailed IP address data</strong> — the Network tab now includes additional detail per IP address observed during the scan.</li>
</ul>
<p><img src="/assets/upstream/images/radar/url-scanner-summary-redesign.png" alt="Screenshot of the redesigned URL Scanner summary on Radar" /></p>
<p>Explore these improvements on the <a href="https://radar.cloudflare.com/scan">Cloudflare Radar URL Scanner</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-25">Mar 25, 2026</time><div>
<h2 id="post-2026-03-25-har-file-detection-and-sanitization"><a href="/changelog/post/2026-03-25-har-file-detection-and-sanitization/">Detect and sanitize HAR files</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.</p>
<p>Gateway now includes a predefined DLP profile called <strong>Unsanitized HAR</strong> that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.</p>
<h4 id="2026-03-25-har-file-detection-and-sanitization-how-to-configure-a-har-file-policy">How to configure a HAR file policy</h4>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to  <strong>Zero Trust</strong> &gt;  <strong>Traffic policies</strong> &gt; <strong>Firewall Policies</strong> &gt; <strong>HTTP</strong> and create a new HTTP policy using the <strong>DLP Profile</strong> selector:</p>
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
<td><em>Unsanitized HAR</em></td>
<td></td>
</tr>
</tbody>
</table>
<p>Then choose one of the following actions:</p>
<ul>
<li><strong>Block</strong>: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.</li>
<li><strong>Block</strong> with <strong>Gateway Redirect</strong>: Intercepts the upload and redirects the user to <code>https://har-sanitizer.pages.dev/</code>, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.</li>
</ul>
<h4 id="2026-03-25-har-file-detection-and-sanitization-sanitized-har-recognition">Sanitized HAR recognition</h4>
<p>HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.</p>
<h4 id="2026-03-25-har-file-detection-and-sanitization-visibility-in-gateway-logs">Visibility in Gateway logs</h4>
<p>Gateway logs will reflect whether a detected HAR file was classified as <strong>Unsanitized</strong> or <strong>Sanitized</strong>, giving your security team full visibility into HAR file activity across your organization.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-25">Mar 25, 2026</time><div>
<h2 id="post-2026-03-25-logpush-granular-timestamps"><a href="/changelog/post/2026-03-25-logpush-granular-timestamps/">Logpush — More granular timestamps</a></h2>
<div class="changelog-badges"><span>logpush</span><span>logs</span></div><div class="changelog-body"><p>Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>To use the new formats, set <code>timestamp_format</code> in your Logpush job's <code>output_options</code>:</p>
<ul>
<li><code>rfc3339ms</code> — <code>2024-02-17T23:52:01.123Z</code></li>
<li><code>rfc3339ns</code> — <code>2024-02-17T23:52:01.123456789Z</code></li>
</ul>
<p>Default timestamp formats apply unless explicitly set. The dashboard defaults to <code>rfc3339</code> and the API defaults to <code>unixnano</code>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/log-output-options/">Log output options</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-25">Mar 25, 2026</time><div>
<h2 id="post-2026-03-25-rfc9440-mtls-fields"><a href="/changelog/post/2026-03-25-rfc9440-mtls-fields/">New mTLS certificate fields for Transform Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized <code>Client-Cert</code> and <code>Client-Cert-Chain</code> header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.</p>
<p>Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, <code>:MIIDsT...Vw==:</code>. A chain of intermediates is expressed as a comma-separated list of such values.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be <code>false</code>.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted.</td>
</tr>
</tbody>
</table>
<p>The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin-server">Example: Forwarding client certificate headers to your origin server</h4>
<p>Add a request header transform rule to set the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>Client-Cert</code></td>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
</tr>
<tr>
<td>Set</td>
<td><code>Client-Cert-Chain</code></td>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
</tr>
</tbody>
</table>
<p>To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates <code>cf.tls_client_auth.cert_verified</code> and <code>cf.tls_client_auth.cert_revoked</code>.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-03-25-rfc9440-mtls-fields-prevent-header-injection">Prevent header injection</h4>
@markup("md", "content/.markup/bodies/17749.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>, <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>, and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-25">Mar 25, 2026</time><div>
<h2 id="post-2026-03-24-secrets-config-property"><a href="/changelog/post/2026-03-24-secrets-config-property/">Declare required secrets in your Wrangler configuration</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The new <code>secrets</code> configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17802.md")</div>
<h4 id="2026-03-24-secrets-config-property-local-development">Local development</h4>
<p>When <code>secrets</code> is defined, <code>wrangler dev</code> and <code>vite dev</code> load only the keys listed in <code>secrets.required</code> from <code>.dev.vars</code> or <code>.env</code>/<code>process.env</code>. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.</p>
<h4 id="2026-03-24-secrets-config-property-type-generation">Type generation</h4>
<p><code>wrangler types</code> generates typed bindings from <code>secrets.required</code> instead of inferring names from <code>.dev.vars</code> or <code>.env</code>. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated <code>Env</code> type marks secrets that only appear in some environments as optional.</p>
<h4 id="2026-03-24-secrets-config-property-deploy">Deploy</h4>
<p><code>wrangler deploy</code> and <code>wrangler versions upload</code> validate that all secrets in <code>secrets.required</code> are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.</p>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#secrets-configuration-property"><code>secrets</code> configuration property</a> reference.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-24">Mar 24, 2026</time><div>
<h2 id="post-2026-03-24-waf-rule-preservation"><a href="/changelog/post/2026-03-24-waf-rule-preservation/">Advanced WAF customization for AI Crawl Control blocks</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.</p>
<p>If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the <strong>Crawlers</strong> page with a link to view the rule directly in WAF.</p>
<p>For more information, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management">WAF rule management</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-24">Mar 24, 2026</time><div>
<h2 id="post-2026-03-24-cache-response-rules"><a href="/changelog/post/2026-03-24-cache-response-rules/">Cache Response Rules</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now control how Cloudflare handles origin responses without changing your origin. Cache Response Rules let you modify <code>Cache-Control</code> directives, manage cache tags, and strip headers like <code>Set-Cookie</code> from origin responses <em>before</em> they reach Cloudflare's cache. Whether traffic is cached or passed through dynamically, these rules give you control over origin response behavior that was previously out of reach.</p>
<h4 id="2026-03-24-cache-response-rules-what-changed">What changed</h4>
<p>Cache Rules previously only operated on request attributes. Cache Response Rules introduce a new response phase that evaluates origin responses and lets you act on them before caching. You can now:</p>
<ul>
<li><strong>Modify <code>Cache-Control</code> directives</strong>: Set or remove individual directives like <code>no-store</code>, <code>no-cache</code>, <code>max-age</code>, <code>s-maxage</code>, <code>stale-while-revalidate</code>, <code>immutable</code>, and more. For example, remove a <code>no-cache</code> directive your origin sends so Cloudflare can cache the asset, or set an <code>s-maxage</code> to control how long Cloudflare stores it.</li>
<li><strong>Set a different browser <code>Cache-Control</code></strong>: Send a different <code>Cache-Control</code> header downstream to browsers and other clients than what Cloudflare uses internally, giving you independent control over edge and browser caching strategies.</li>
<li><strong>Manage cache tags</strong>: Add, set, or remove cache tags on responses, including converting tags from another CDN's header format into Cloudflare's <code>Cache-Tag</code> header. This is especially useful if you are migrating from a CDN that uses a different tag header or delimiter.</li>
<li><strong>Strip headers that block caching</strong>: Remove <code>Set-Cookie</code>, <code>ETag</code>, or <code>Last-Modified</code> headers from origin responses before caching, so responses that would otherwise be treated as uncacheable can be stored and served from cache.</li>
</ul>
<h4 id="2026-03-24-cache-response-rules-benefits">Benefits</h4>
<ul>
<li><strong>No origin changes required</strong>: Fix caching behavior entirely from Cloudflare, even when your origin configuration is locked down or managed by a different team.</li>
<li><strong>Simpler CDN migration</strong>: Match caching behavior from other CDN providers without rewriting your origin. Translate cache tag formats and override directives that do not align with Cloudflare's defaults.</li>
<li><strong>Native support, fewer workarounds</strong>: Functionality that previously required workarounds is now built into Cache Rules with full Tiered Cache compatibility.</li>
<li><strong>Fine-grained control</strong>: Use expressions to match on request and response attributes, then apply precise cache settings per rule. Rules are stackable and composable with existing Cache Rules.</li>
</ul>
<h4 id="2026-03-24-cache-response-rules-get-started">Get started</h4>
<p>Configure Cache Response Rules in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or via the <a href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/">Rulesets API</a>. For more details, refer to the <a href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/">Cache Rules documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-24">Mar 24, 2026</time><div>
<h2 id="post-2026-03-24-docker-hub-images"><a href="/changelog/post/2026-03-24-docker-hub-images/">Use Docker Hub images with Containers</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Containers now support <a href="https://hub.docker.com/">Docker Hub</a> images. You can use a fully qualified Docker Hub image reference in your <a href="https://developers.cloudflare.com/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17710.md")</div>
<p>Containers also support private Docker Hub images. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-docker-hub-images">Use private Docker Hub images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-24">Mar 24, 2026</time><div>
<h2 id="post-2026-03-24-oidc-claims-filtering-gateway-policies"><a href="/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/">OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare Gateway now supports <a href="/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims">OIDC Claims</a> as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.</p>
<p>With this update, you can:</p>
<ul>
<li>Filter traffic in <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies based on OIDC claim values.</li>
<li>Apply custom <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> to route DNS queries to specific resolvers depending on a user's OIDC claims.</li>
<li>Control <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a> to assign dedicated egress IPs based on OIDC claim attributes.</li>
</ul>
<p>For example, you can create a policy that routes traffic differently for users with <code>department=engineering</code> in their OIDC claims, or restrict access to certain destinations based on a user's role claim.</p>
<p>To get started, configure <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> on your identity provider and use the <strong>OIDC Claims</strong> selector in the Gateway policy builder.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-24">Mar 24, 2026</time><div>
<h2 id="post-2026-03-24-interconnects-navigation-update"><a href="/changelog/post/2026-03-24-interconnects-navigation-update/">Interconnects moved to Connectors</a></h2>
<div class="changelog-badges"><span>network-interconnect</span></div><div class="changelog-body"><p>The top-level <strong>Interconnects</strong> page in the Cloudflare dashboard has been removed. Interconnects are now located under <strong>Connectors</strong> &gt; <strong>Interconnects</strong>.</p>
<p>Your existing configurations and functionality remain the same.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-24">Mar 24, 2026</time><div>
<h2 id="post-2026-03-24-dynamic-workers-open-beta"><a href="/changelog/post/2026-03-24-dynamic-workers-open-beta/">Dynamic Workers, now in open beta</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/dynamic-workers/">Dynamic Workers</a> are now in <a href="https://blog.cloudflare.com/dynamic-workers/">open beta</a> for all paid Workers users. You can now have a Worker spin up other Workers, called Dynamic Workers, at runtime to execute code on-demand in a secure, sandboxed environment. Dynamic Workers start in milliseconds, making them well suited for fast, secure code execution at scale.</p>
<h4 id="2026-03-24-dynamic-workers-open-beta-use-dynamic-workers-for">Use Dynamic Workers for</h4>
<ul>
<li><strong><a href="/agents/tools/codemode/">Code Mode</a></strong>: LLMs are trained to write code. Run tool-calling logic written in code instead of stepping through many tool calls, which can save up to 80% in inference tokens and cost.</li>
<li><strong>AI agents executing code</strong>: Run code for tasks like data analysis, file transformation, API calls, and chained actions.</li>
<li><strong>Running AI-generated code</strong>: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.</li>
<li><strong>Fast development and previews</strong>: Load prototypes, previews, and playgrounds in milliseconds.</li>
<li><strong>Custom automations</strong>: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.</li>
</ul>
<h4 id="2026-03-24-dynamic-workers-open-beta-executing-dynamic-workers">Executing Dynamic Workers</h4>
<p>Dynamic Workers support two loading modes:</p>
<ul>
<li><code>load(code)</code> — for one-time code execution (equivalent to calling <code>get()</code> with a null ID).</li>
<li><code>get(id, callback)</code> — caches a Dynamic Worker by ID so it can stay warm across requests. Use this when the same code will receive subsequent requests.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17801.md")</div>
<h4 id="2026-03-24-dynamic-workers-open-beta-helper-libraries-for-dynamic-workers">Helper libraries for Dynamic Workers</h4>
<p>Here are 3 new libraries to help you build with Dynamic Workers:</p>
<ul>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a></strong>: Replace individual tool calls with a single <code>code()</code> tool, so LLMs write and execute TypeScript that orchestrates multiple API calls in one pass.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a></strong>: Resolve npm dependencies and bundle source files into ready-to-load modules for Dynamic Workers, all at runtime.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/shell"><code>@cloudflare/shell</code></a></strong>: Give your agent a virtual filesystem inside a Dynamic Worker with persistent storage backed by SQLite and R2.</p>
</li>
</ul>
<h4 id="2026-03-24-dynamic-workers-open-beta-try-it-out">Try it out</h4>
<p><strong>Dynamic Workers Starter</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Use this <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter</a> to deploy a Worker that can load and execute Dynamic Workers.</p>
<p><strong>Dynamic Workers Playground</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a> to write or import code, bundle it at runtime with <code>@cloudflare/worker-bundler</code>, execute it through a Dynamic Worker, and see real-time responses and execution logs.</p>
<p>For the full API reference and configuration options, refer to the <a href="/dynamic-workers/">Dynamic Workers documentation</a>.</p>
<h4 id="2026-03-24-dynamic-workers-open-beta-pricing">Pricing</h4>
<p>Dynamic Workers <a href="/dynamic-workers/pricing/">pricing</a> is based on three dimensions: Dynamic Workers created daily, requests, and CPU time.</p>
<table>
<thead>
<tr>
<th></th>
<th>Included</th>
<th>Additional usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dynamic Workers created daily</strong></td>
<td>1,000 unique Dynamic Workers per month</td>
<td>+$0.002 per Dynamic Worker per day</td>
</tr>
<tr>
<td><strong>Requests</strong> ¹</td>
<td>10 million per month</td>
<td>+$0.30 per million requests</td>
</tr>
<tr>
<td><strong>CPU time</strong> ¹</td>
<td>30 million CPU milliseconds per month</td>
<td>+$0.02 per million CPU milliseconds</td>
</tr>
</tbody>
</table>
<p>¹ Uses <a href="/workers/platform/pricing/#workers">Workers Standard rates</a> and will appear as part of your existing Workers bill, not as separate Dynamic Workers charges.</p>
<p>Note: Dynamic Workers requests and CPU time are already billed as part of your Workers plan and will count toward your Workers requests and CPU usage. The Dynamic Workers created daily charge is not yet active — you will not be billed for the number of Dynamic Workers created at this time. Pricing information is shared in advance so you can estimate future costs.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-local-dev-instance-methods"><a href="/changelog/post/2026-03-23-local-dev-instance-methods/">Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Workflow instance methods <code>pause()</code>, <code>resume()</code>, <code>restart()</code>, and <code>terminate()</code> are now available in local development when using <code>wrangler dev</code>.</p>
<p>You can now test the full Workflow instance lifecycle locally:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.MY_WORKFLOW.create({&#10;	id: &quot;my-instance-id&quot;,&#10;});&#10;&#10;await instance.pause(); // pauses a running workflow instance&#10;await instance.resume(); // resumes a paused instance&#10;await instance.restart(); // restarts the instance from the beginning&#10;await instance.terminate(); // terminates the instance immediately&#10;</code></pre>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/20/">Previous</a><span>Page 21 of 50</span><a class="pagination-next" rel="next" href="/changelog/22/">Next</a></nav>
</div>
