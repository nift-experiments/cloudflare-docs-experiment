---
cp9:
  canonical: https://developers.cloudflare.com/changelog/5/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 5 | Cloudflare Docs
  head_html: <title>Changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/5/#page","headline":"Changelog - page 5 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/5/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-08-14">Aug 14, 2026</time><div>
<h2 id="post-2026-08-14-deepseek-v4-workers-ai"><a href="/changelog/post/2026-08-14-deepseek-v4-workers-ai/">DeepSeek V4 Flash and Pro now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/deepseek-v4-pro-0813/"><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></a> and <a href="/workers-ai/models/deepseek-v4-flash-0731/"><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></a> are now available on Workers AI.</p>
<p>DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full <strong>one million (1,048,576) token context window</strong>. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.</p>
<p>DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Reasoning</strong>: Both models support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>Long context</strong>: Both models support a full 1,048,576 token context window.</li>
</ul>
<p>Both models require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use these models through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/deepseek-v4-pro-0813/">DeepSeek V4 Pro model page</a>, the <a href="/workers-ai/models/deepseek-v4-flash-0731/">DeepSeek V4 Flash model page</a>, and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-13">Aug 13, 2026</time><div>
<h2 id="post-2026-08-13-artifacts-jurisdictions"><a href="/changelog/post/2026-08-13-artifacts-jurisdictions/">Data localization support for Artifacts</a></h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p>Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.</p>
<p>Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.</p>
<p>For supported jurisdictions and usage details, refer to <a href="/artifacts/guides/data-localization/">Data localization</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-13">Aug 13, 2026</time><div>
<h2 id="post-2026-08-13-package-protection"><a href="/changelog/post/2026-08-13-package-protection/">Detect and control software package downloads with package registry security</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> using <code>pkg.*</code> selectors to allow or block package downloads.</p>
<h4 id="2026-08-13-package-protection-supported-ecosystems">Supported ecosystems</h4>
<p>Gateway detects package downloads for the following ecosystems:</p>
<table>
<thead>
<tr>
<th>Ecosystem</th>
<th>Namespace</th>
</tr>
</thead>
<tbody>
<tr>
<td>npm</td>
<td>Scope (for example, <code>@babel</code>)</td>
</tr>
<tr>
<td>PyPI</td>
<td>--</td>
</tr>
<tr>
<td>RubyGems</td>
<td>--</td>
</tr>
<tr>
<td>Cargo</td>
<td>--</td>
</tr>
<tr>
<td>Go</td>
<td>Module path</td>
</tr>
<tr>
<td>Maven</td>
<td>Group ID</td>
</tr>
<tr>
<td>NuGet</td>
<td>--</td>
</tr>
</tbody>
</table>
<h4 id="2026-08-13-package-protection-selectors">Selectors</h4>
<p>In the dashboard, select <strong>Package Ecosystem</strong> to access the package registry selectors. After selecting a single ecosystem, nested fields for package name, version, and namespace become available. Five <code>pkg.*</code> selectors are available for HTTP policies with the Allow and Block actions:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pkg.ecosystem</code></td>
<td>The package ecosystem detected from the request URL.</td>
</tr>
<tr>
<td><code>pkg.name</code></td>
<td>The package name extracted from the download URL.</td>
</tr>
<tr>
<td><code>pkg.version</code></td>
<td>The package version, with support for ecosystem-aware comparison operators.</td>
</tr>
<tr>
<td><code>pkg.namespace</code></td>
<td>The package namespace, when the ecosystem supports one.</td>
</tr>
<tr>
<td><code>pkg.purl</code></td>
<td>The <a href="https://github.com/package-url/purl-spec">Package URL (PURL)</a> derived from the detected coordinates. Available in the API only.</td>
</tr>
</tbody>
</table>
<p>Detection is based on the registry protocol rather than the hostname, so it works the same way whether traffic goes to a public registry, a corporate proxy such as Artifactory or Nexus, or a self-hosted mirror.</p>
<p>Package registry security requires <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> to be turned on.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/package-registry-security/">Package registry security</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-13">Aug 13, 2026</time><div>
<h2 id="post-2026-08-13-datachannels-reliability-ordering"><a href="/changelog/post/2026-08-13-datachannels-reliability-ordering/">Control Realtime SFU DataChannel delivery</a></h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC selective forwarding unit</a> that runs on Cloudflare's global network. It forwards audio, video, and application data between WebRTC clients without requiring you to manage SFU infrastructure or regions.</p>
<p><a href="/realtime/sfu/datachannels/">DataChannels</a> are WebRTC channels for application messages. A client publishes a named DataChannel to Realtime SFU, and the SFU forwards its messages to every client that subscribes to that channel. Use DataChannels for low-latency payloads such as chat messages, game state, sensor updates, and control events.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-what-changed">What changed</h4>
<p>Realtime SFU DataChannels now support unordered and partially reliable delivery. DataChannels remain reliable and ordered by default, so existing channels keep their current behavior.</p>
<p>With ordered delivery, a delayed message can block later messages. For game state or sensor updates, recent data may be more useful than recovering an older message. Unordered delivery lets later messages proceed, while partial reliability limits retransmission attempts or delivery time.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-choose-delivery-behavior">Choose delivery behavior</h4>
<p>Delivery settings answer two questions: whether newer messages can bypass a delayed message, and when the transport should stop retrying delivery.</p>
<p>Choose the policy that matches how long your payload remains useful:</p>
<table>
<thead>
<tr>
<th>Goal</th>
<th>Settings</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reliable, ordered delivery (default)</td>
<td>Omit <code>ordered</code>, <code>maxRetransmits</code>, and <code>maxPacketLifeTime</code></td>
<td>Messages remain useful and must arrive in order</td>
</tr>
<tr>
<td>Reliable, unordered delivery</td>
<td>Set <code>ordered: false</code>; omit both retry fields</td>
<td>Messages remain useful, but later messages should not wait for earlier messages</td>
</tr>
<tr>
<td>No retries or ordering</td>
<td>Set <code>ordered: false</code> and <code>maxRetransmits: 0</code></td>
<td>The application tolerates message loss and discards out-of-date updates</td>
</tr>
<tr>
<td>Limited retries</td>
<td>Set <code>maxRetransmits: &lt;COUNT&gt;</code></td>
<td>Brief recovery is useful, but repeated retries are not</td>
</tr>
<tr>
<td>Time-bounded delivery</td>
<td>Set <code>maxPacketLifeTime: &lt;MILLISECONDS&gt;</code></td>
<td>A message loses value after a known time window</td>
</tr>
</tbody>
</table>
<p><code>ordered</code> controls ordering independently from retries. <code>maxRetransmits</code> and <code>maxPacketLifeTime</code> are alternative retry budgets, so set at most one for each channel. Omit both for reliable delivery, whether ordered or unordered.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-apply-the-policy-end-to-end">Apply the policy end to end</h4>
<p>Realtime DataChannels use negotiated IDs, so browsers do not receive delivery settings from the remote peer. Apply the same settings when the publisher creates the local channel, each subscriber pulls the remote channel, and each client calls <code>createDataChannel()</code>.</p>
<p>The following example configures unordered delivery with no retransmissions. It begins after you <a href="/realtime/sfu/datachannels/#set-up-a-datachannel">establish a DataChannel transport on both sessions and complete any required SDP exchange</a>. Run the API requests from your backend with <code>APP_ID</code>, <code>APP_TOKEN</code>, <code>PUBLISHER_SESSION_ID</code>, and <code>SUBSCRIBER_SESSION_ID</code> set in your environment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17744.md")</div>
<h4 id="2026-08-13-datachannels-reliability-ordering-related-documentation">Related documentation</h4>
<ul>
<li><a href="/realtime/sfu/">Realtime SFU overview</a></li>
<li><a href="/realtime/sfu/datachannels/">DataChannels</a></li>
<li><a href="/realtime/sfu/https-api/">Connection API</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-13">Aug 13, 2026</time><div>
<h2 id="post-2026-08-13-oci-object-storage-cloud-connector"><a href="/changelog/post/2026-08-13-oci-object-storage-cloud-connector/">Oracle Cloud Infrastructure Object Storage support in Cloud Connector</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.</p>
<p>OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional <code>oraclecloud.com</code> and dedicated <code>customer-oci.com</code> path-style endpoints.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-08-13-oci-object-storage-cloud-connector-public-buckets-only">Public buckets only</h4>
@markup("md", "content/.markup/bodies/17751.md")</aside>
<h4 id="2026-08-13-oci-object-storage-cloud-connector-api-example">API example</h4>
<p>Set <code>provider</code> to <code>oci_storage</code> and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/assets/*\&quot;&quot;,&#10;	&quot;provider&quot;: &quot;oci_storage&quot;,&#10;	&quot;description&quot;: &quot;Route assets to OCI Object Storage&quot;,&#10;	&quot;enabled&quot;: true,&#10;	&quot;parameters&quot;: {&#10;		&quot;host&quot;: &quot;&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For endpoint formats and bucket requirements, refer to <a href="/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage">Supported cloud providers in Cloud Connector</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-13">Aug 13, 2026</time><div>
<h2 id="post-2026-08-13-ct-monitoring-ga"><a href="/changelog/post/2026-08-13-ct-monitoring-ga/">Certificate Transparency Monitoring is now Generally Available</a></h2>
<div class="changelog-badges"><span>ssl</span></div><div class="changelog-body"><p>Certificate Transparency Monitoring is now <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">generally available</a> across all Cloudflare plans.</p>
<p>Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.</p>
<p>Learn more in the <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">launch blog post</a> or the <a href="/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">CT Monitoring docs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-12">Aug 12, 2026</time><div>
<h2 id="post-2026-08-12-blocked-content-rules"><a href="/changelog/post/2026-08-12-blocked-content-rules/">Block emails by content with blocked content rules</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email security now lets administrators write their own content-based blocking rules. A new <strong>Blocked content</strong> area under <strong>Policies &amp; rules</strong> lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.</p>
<ul>
<li>Create rules using either <strong>plaintext</strong> matches or <strong>regular expressions</strong> — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.</li>
<li>Choose the <strong>search location</strong> for each rule: <strong>subject</strong>, <strong>body</strong>, or <strong>subject and body</strong>.</li>
<li>Use the built-in <strong>regular expression checker</strong> to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.</li>
<li>Matching messages are marked with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> and prevented from reaching users' inboxes.</li>
</ul>
<p>Blocked content rules currently only support the block action.</p>
<p>This feature is available for the following Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-content/">Blocked content</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-12">Aug 12, 2026</time><div>
<h2 id="post-2026-08-12-fido2-keys-infrastructure-ssh"><a href="/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/">Independent MFA supports FIDO2 for infrastructure applications</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Infrastructure</a> applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow <code>ssh_fido2_key</code>, <code>piv_key</code>, or both in application-level and policy-level MFA settings.</p>
<p>Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps">Enroll a FIDO2 key for infrastructure apps</a> and <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Configure MFA for infrastructure applications</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-12">Aug 12, 2026</time><div>
<h2 id="post-2026-08-12-mcp-detection-and-dashboard"><a href="/changelog/post/2026-08-12-mcp-detection-and-dashboard/">MCP protocol detection and AI Security dashboard</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Cloudflare Gateway now automatically detects <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP)</a> traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.</p>
<h4 id="2026-08-12-mcp-detection-and-dashboard-mcp-policy-selector">MCP policy selector</h4>
<p>A new <strong>Is MCP</strong> selector (<code>experimental.is_mcp</code>) is available in <a href="/cloudflare-one/traffic-policies/http-policies/#is-mcp">HTTP policies</a>. Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.</p>
<p>This selector is currently in beta and may change before general availability.</p>
<p>For example, the following policy blocks MCP traffic that does not arrive through an approved <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a>:</p>
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
<td>Is MCP</td>
<td>is</td>
<td><em>True</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Traffic Source</td>
<td>is not</td>
<td><em>MCP portal</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-block-unknown-mcp.png" alt="Example Gateway policy that blocks MCP traffic not arriving through an MCP portal" /></p>
<h4 id="2026-08-12-mcp-detection-and-dashboard-ai-security-report">AI security report</h4>
<p>A new <strong>AI security report</strong> dashboard under <strong>Insights &amp; Logs &gt; Dashboards</strong> provides visibility into MCP usage across your organization. The dashboard includes:</p>
<ul>
<li>Total MCP request volume, unique users, and unique MCP servers</li>
<li>A timeseries chart of unique MCP servers observed over time</li>
<li>A summary of Gateway policies that target MCP traffic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-mcp-dashboard.png" alt="AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-12">Aug 12, 2026</time><div>
<h2 id="post-2026-08-12-traffic-source-selector"><a href="/changelog/post/2026-08-12-traffic-source-selector/">Traffic Source selector in Gateway policies</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Gateway <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> policies now include a <strong>Traffic Source</strong> selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.</p>
<h4 id="2026-08-12-traffic-source-selector-available-traffic-source-values">Available traffic source values</h4>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Device client</td>
<td><code>device_client</code></td>
<td>Traffic from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client (WARP)</a></td>
</tr>
<tr>
<td>Mesh</td>
<td><code>mesh</code></td>
<td>Traffic from a <a href="/mesh/">Cloudflare Mesh</a> connector</td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td><code>cloudflare_wan</code></td>
<td>Traffic from <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a> (Magic WAN)</td>
</tr>
<tr>
<td>Clientless RDP</td>
<td><code>clientless_rdp</code></td>
<td>Traffic from a clientless RDP session</td>
</tr>
<tr>
<td>Proxy endpoint</td>
<td><code>proxy_endpoint</code></td>
<td>Traffic from a <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoint</a> (PAC file)</td>
</tr>
<tr>
<td>Clientless Browser Isolation</td>
<td><code>agentless_biso</code></td>
<td>Traffic from <a href="/cloudflare-one/remote-browser-isolation/">clientless Browser Isolation</a></td>
</tr>
<tr>
<td>MCP portal</td>
<td><code>mcp_portal</code></td>
<td>Traffic from an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a></td>
</tr>
</tbody>
</table>
<p>The selector uses the <code>net.onramp.type</code> API field in both HTTP and Network policies.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Traffic Source</td>
<td><code>net.onramp.type == &quot;device_client&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-08-12-traffic-source-selector-browser-isolation-selector">Browser Isolation selector</h4>
<p>A <strong>Browser Isolation</strong> selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, allowing administrators to apply different policy behavior to isolated traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser Isolation</td>
<td><code>net.is_isolated == true</code></td>
</tr>
</tbody>
</table>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-11">Aug 11, 2026</time><div>
<h2 id="post-2026-08-11-skip-superseded-builds"><a href="/changelog/post/2026-08-11-skip-superseded-builds/">Pages now skips superseded queued builds</a></h2>
<div class="changelog-badges"><span>pages</span></div><div class="changelog-body"><p>Pages now automatically skips a queued build when a newer build for the same project, branch, and deployment target is also queued.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-11">Aug 11, 2026</time><div>
<h2 id="post-2026-08-11-new-status-page"><a href="/changelog/post/2026-08-11-new-status-page/">New Cloudflare Status page</a></h2>
<div class="changelog-badges"><span>support</span></div><div class="changelog-body"><p>The Cloudflare Status page at <a href="https://www.cloudflarestatus.com/">www.cloudflarestatus.com</a> has been rebuilt. It is available at the same address, and every previously documented <a href="https://www.cloudflarestatus.com/api">Status API</a> endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.</p>
<h4 id="2026-08-11-new-status-page-notifications-that-fire-even-when-cloudflare-is-down">Notifications that fire even when Cloudflare is down</h4>
<p>The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.</p>
<p>The <strong>Maintenance Notification</strong> and <strong>Incident Alerts</strong> in <a href="/notifications/">Cloudflare Notifications</a> remain supported, and deliver to the destinations already configured on your account.</p>
<h4 id="2026-08-11-new-status-page-markdown-for-ai-agents">Markdown for AI agents</h4>
<p>Every page on the status page returns Markdown when requested with an <code>Accept: text/markdown</code> header, so agents can read the current status without parsing HTML:</p>
<pre tabindex="0"><code class="language-sh">curl -H &quot;Accept: text/markdown&quot; https://www.cloudflarestatus.com/locations&#10;</code></pre>
<h4 id="2026-08-11-new-status-page-separate-feeds-for-incidents-and-maintenance">Separate feeds for incidents and maintenance</h4>
<p>Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:</p>
<pre tabindex="0"><code class="language-txt">https://www.cloudflarestatus.com/api/v3/incidents.rss&#10;https://www.cloudflarestatus.com/api/v3/incidents.atom&#10;https://www.cloudflarestatus.com/api/v3/maintenance.rss&#10;https://www.cloudflarestatus.com/api/v3/maintenance.atom&#10;</code></pre>
<p>For more information, refer to <a href="/support/cloudflare-status/">Cloudflare Status</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-11">Aug 11, 2026</time><div>
<h2 id="post-2026-08-11-hostname-routing-ga-public-initial-resolved-ips"><a href="/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/">Hostname routing is now generally available, with a new public IP range for initial resolved IPs</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span><span>mesh</span><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="https://blog.cloudflare.com/tunnel-hostname-routing/">Hostname routing</a> is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong>: route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> (for example, <code>wiki.internal.local</code>) to a private application behind your tunnel, or a <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> (for example, <code>bank.example.com</code>) to egress through a specific tunnel and anchor traffic to a dedicated exit node.</li>
<li><strong>Cloudflare Mesh</strong>: attract a <a href="/mesh/features/routes/#hostname-routes">private or public hostname's traffic</a> to a Mesh node.</li>
</ul>
<p>Alongside GA, the default IPv4 range used for <span class="nb-glossary-tooltip" title="initial resolved IP">initial resolved IPs</span> (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:</p>
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p><strong>Why this is changing:</strong> Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restrictions block background requests to CGNAT addresses (<code>100.64.0.0/10</code>), which included the previous initial resolved IP default (<code>100.80.0.0/16</code>). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.</p>
<p><strong>What is affected:</strong> Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public</a> hostname routing for Cloudflare Tunnel</li>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a> for Cloudflare Mesh</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> on non-HTTPS ports</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> (Domain, Host, Application, and Content Categories)</li>
</ul>
<p>You can check your account's current range, or configure a custom range, at any time from <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>, or using the <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip">Initial Resolved IP Subnet API</a>.</p>
<div class="nb-dash-button"></div>
<p>For full instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>. The IPv6 range (<code>2606:4700:0cf1:4000::/64</code>) is unchanged and is not affected by this restriction.</p>
<p>The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details.</p>
<p>If you were relying on a Chrome Enterprise policy workaround (such as <code>LocalNetworkAccessRestrictionsTemporaryOptOut</code>) while your account was still on the legacy CGNAT-based range, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</a> for next steps.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-11">Aug 11, 2026</time><div>
<h2 id="post-2026-08-11-waf-release"><a href="/changelog/post/2026-08-11-waf-release/">WAF Release - 2026-08-11</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>A new detection provides protection against vBulletin CVE-2026-61511.</li>
<li>Two existing detections have been improved to strengthen coverage.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.</p>
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
				<code class="nb-rule-id" title="1b0775f0f092483387cfb23f94f3006b">94f3006b</code>
</td>
<td>N/A</td>
<td>vBulletin - Remote Code Execution - CVE:CVE-2026-61511</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="784d3824b6cf419db6af0b64098b749e">098b749e</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID: <code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a561c9138b46470ca6db96edd56225d8">d56225d8</code>
</td>
<td>N/A</td>
<td>vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: <code class="nb-rule-id" title="5137834eb8634842852273a08fe9f1c7">8fe9f1c7</code>)</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-11">Aug 11, 2026</time><div>
<h2 id="post-2026-08-10-warp-windows-ga"><a href="/changelog/post/2026-08-10-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.905.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-10">Aug 10, 2026</time><div>
<h2 id="post-2026-08-10-tunnel-live-logs-core-dashboard"><a href="/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/">Stream live logs from Cloudflare Tunnel in the dashboard</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Real-time Tunnel log streaming is now available in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-live-logs-core-dashboard.gif" alt="Stream live logs from a tunnel in the Cloudflare dashboard" /></p>
<p>In the tunnel detail view, a new <strong>Live logs</strong> tab lets you:</p>
<ul>
<li><strong>Stream logs from single or multiple connectors</strong> — In <a href="/tunnel/configuration/#replicas-and-high-availability">highly available</a> deployments with multiple <code>cloudflared</code> replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.</li>
<li><strong>Filter by log level, event type, and HTTP method</strong> — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or <code>cloudflared</code> internal), at any log level.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/tunnel/observability/#remote-log-streaming">Tunnel observability</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-10">Aug 10, 2026</time><div>
<h2 id="post-2026-08-10-turnstile-spin-ga"><a href="/changelog/post/2026-08-10-turnstile-spin-ga/">Turnstile Spin is now generally available</a></h2>
<div class="changelog-badges"><span>turnstile</span></div><div class="changelog-body"><p><a href="/turnstile/spin/">Turnstile Spin</a> is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.</p>
<h4 id="2026-08-10-turnstile-spin-ga-server-side-verification">Server-side verification</h4>
<p>Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.</p>
<ul>
<li>The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.</li>
<li>The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select <strong>Fix with Spin</strong> to copy a prompt that guides your agent through wiring siteverify into your backend.</li>
<li>Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.</li>
</ul>
<h4 id="2026-08-10-turnstile-spin-ga-run-spin">Run Spin</h4>
<p>You can run Spin three ways:</p>
<ul>
<li>In the <strong>Turnstile dashboard</strong>, select <strong>Set up with Spin</strong>, enter your domains, then select <strong>Set up</strong>. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.</li>
<li>From the <code>Wrangler CLI</code>, run <a href="/turnstile/spin/#set-up-from-the-wrangler-cli"><code>wrangler turnstile widget create</code></a>. Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.</li>
<li>From your <strong>AI coding agent</strong>, paste the <a href="/turnstile/spin/#set-up-from-an-ai-coding-agent">Spin prompt</a> into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.</li>
</ul>
<p>To get started, refer to the <a href="/turnstile/spin/">Turnstile Spin documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-workers-ai-unified-billing"><a href="/changelog/post/2026-08-07-workers-ai-unified-billing/">Workers AI and AI Gateway unify model access and billing</a></h2>
<div class="changelog-badges"><span>ai-gateway</span><span>workers-ai</span></div><div class="changelog-body"><p>Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-entrypoints-and-observability">Unified entrypoints and observability</h4>
<p>The <a href="/ai-gateway/usage/worker-binding-methods/">AI binding</a> supports both Workers AI and third-party models through <code>env.AI.run()</code>. The <a href="/ai-gateway/usage/rest-api/">REST API</a> provides shared <code>/ai/</code> endpoints with Cloudflare authentication across providers.</p>
<p>Route a Workers AI request through AI Gateway by specifying a gateway ID. Use <code>default</code> to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17687.md")</div>
<p>Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-billing-and-higher-rate-limits">Unified billing and higher rate limits</h4>
<p>You can now use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a> to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. Workers AI requests routed through that gateway deduct from your credit balance in real time.</p>
<p>Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.</p>
<p>For details, refer to <a href="/workers-ai/platform/limits/">Workers AI limits</a>, <a href="/workers-ai/platform/pricing/">Workers AI pricing</a>, <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, and the <a href="/ai/models/">AI Gateway model catalog</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-hyperdrive-mysql-ga"><a href="/changelog/post/2026-08-07-hyperdrive-mysql-ga/">MySQL support in Hyperdrive is now generally available</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same <a href="/hyperdrive/platform/pricing/">pricing</a> as Postgres.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17733.md")</div>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-hyperdrive-restart-configuration-dashboard"><a href="/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/">Restart a Hyperdrive configuration from the dashboard</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.</p>
<p>Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.</p>
<p>To restart, select your Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to the <strong>Settings</strong> tab, and select <strong>Restart</strong> under <strong>Danger zone</strong>. Restarting requires the <a href="/fundamentals/manage-members/roles/"><strong>Hyperdrive Admin</strong> role</a>. After a restart, the <strong>Settings</strong> tab shows when the configuration was last manually restarted.</p>
<p><img src="/assets/upstream/images/hyperdrive/dashboard-restart-danger-zone.png" alt="The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions." /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17734.md")</aside>
<p>For more information, refer to <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-stateful-health-notifications"><a href="/changelog/post/2026-08-07-stateful-health-notifications/">Load Balancing health notifications now resolve automatically</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p><a href="/load-balancing/">Load Balancing</a> health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.</p>
<p>As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.</p>
<p>This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by <a href="/health-checks/">Health Checks</a> notifications.</p>
<p>Two things to keep in mind:</p>
<ul>
<li>A recovery notification is matched to the earlier unhealthy notification for the <strong>same pool or endpoint</strong>. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.</li>
<li>If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.</li>
</ul>
<p>Refer to <a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a> to learn more about routing Load Balancing health notifications to an incident management tool.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-mesh-container-image"><a href="/changelog/post/2026-08-07-mesh-container-image/">Container image for Cloudflare Mesh</a></h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/mesh/">Cloudflare Mesh</a> nodes can now run as Docker containers. The <a href="https://hub.docker.com/r/cloudflare/mesh"><code>cloudflare/mesh</code></a> image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.</p>
<p>The image supports <code>amd64</code> and <code>arm64</code> architectures and includes built-in <a href="/mesh/guides/run-mesh-in-containers/#source-nat">source NAT</a> so return traffic routes correctly without VPC route table changes.</p>
<h4 id="2026-08-07-mesh-container-image-deployment-patterns">Deployment patterns</h4>
<ul>
<li><strong>Docker Compose</strong> — add a <code>cloudflare-mesh</code> service to your <code>compose.yaml</code> and connect your entire stack to a private network.</li>
<li><strong>Kubernetes StatefulSet</strong> — deploy a standalone Mesh node with persistent registration state.</li>
<li><strong>Kubernetes sidecar</strong> — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.</li>
<li><strong>CI/CD</strong> — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.</li>
</ul>
<p>For <a href="/mesh/features/high-availability/">high availability</a>, run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, runtime configuration, and deployment examples, refer to <a href="/mesh/guides/run-mesh-in-containers/">Run Mesh in Docker / Kubernetes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-radar-as-connectivity-upstreams"><a href="/changelog/post/2026-08-07-radar-as-connectivity-upstreams/">AS-level connectivity and upstream providers on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> expands its <a href="https://radar.cloudflare.com/routing">Routing section</a> with two widgets on AS pages, such as <a href="https://radar.cloudflare.com/routing/as13335">AS13335</a>, that describe how a network reaches the rest of the Internet: the paths it takes toward the <a href="https://en.wikipedia.org/wiki/Tier_1_network">Tier-1</a> networks, and the mix of direct upstreams carrying its routes. Both are derived from <a href="https://www.routeviews.org/">RouteViews</a> RIB snapshots, unioned across selected collectors.</p>
<h4 id="2026-08-07-radar-as-connectivity-upstreams-as-level-connectivity">AS-level connectivity</h4>
<p>The <strong>AS-level connectivity</strong> graph aggregates the BGP paths an AS uses to reach the Tier-1 networks, unioned across all the prefixes it announces, as observed by selected RouteViews collectors. It reads from left to right, starting at the queried AS and ending at the Tier-1 networks, and each node is labeled with its AS number, country, and organization name. Tier-1 nodes are marked so they stand apart from the intermediate networks that lead to them.</p>
<p>By default, the graph shows the network's direct connections to Tier-1 networks plus the indirect paths, which keeps the view readable. A <strong>Show full paths</strong> toggle expands it to every observed path, including transit through Tier-1 networks the AS already connects to. An IP version selector switches between IPv4 and IPv6, because the paths reaching Tier-1 networks may differ between the two address families.</p>
<p><img src="/assets/upstream/images/radar/as-level-connectivity-graph.png" alt="AS-level connectivity graph for AS13335, showing Tier-1 networks it reaches directly alongside paths that reach others through intermediate networks" /></p>
<p>This is the AS-level counterpart to the <strong>Real-time connectivity</strong> graph on prefix pages, such as the one for <a href="https://radar.cloudflare.com/routing/prefix/1.1.1.0/24">1.1.1.0/24</a>. Instead of covering a single prefix, it covers the union of paths for all prefixes an AS announces, which makes it a fast way to read a network's transit hierarchy: which providers it depends on, how many hops separate it from the core, and whether its paths to the core are diverse or concentrated. For more information on the prefix-level graph, refer to <a href="/radar/glossary/#bgp-real-time-routes">BGP real-time routes</a>.</p>
<h4 id="2026-08-07-radar-as-connectivity-upstreams-upstream-providers">Upstream providers</h4>
<p>The <strong>Upstream providers</strong> widget tracks the share of an AS's observed paths carried by each of its direct upstream networks over time, drawn as a stacked area chart. Up to 10 upstreams appear as their own series and the remaining ones are grouped into <strong>Other</strong>. Transit changes such as adding a provider, dropping one, or moving traffic between them appear as movement between bands rather than as a single aggregate number. As with the connectivity graph, an IP version selector switches between IPv4 and IPv6.</p>
<p><img src="/assets/upstream/images/radar/as-upstream-providers-timeseries.png" alt="Stacked area chart of the share of AS13335's observed paths carried by each of its top 10 direct upstreams, with the remainder grouped into Other" /></p>
<h4 id="2026-08-07-radar-as-connectivity-upstreams-api-endpoints">API endpoints</h4>
<p>The data behind both widgets is also available through two new endpoints on the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list/"><code>/bgp/routes/paths/{asn}</code></a> — Returns the ordered AS path segments an AS uses to reach the Tier-1 networks, each with its observed path count, peer count, and contributing collectors, alongside the name and country of every ASN in the response. Pass <code>collector</code> to scope the result to a single RouteViews collector.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries/"><code>/bgp/routes/upstreams/{asn}/timeseries</code></a> — Returns the share of an AS's observed paths carried by each direct upstream over time. Use <code>limit</code> to control how many upstreams come back as separate series before the rest are grouped into an <code>OTHER</code> series, and <code>ipVersion</code> to select the address family.</li>
</ul>
<p>Visit the <a href="https://radar.cloudflare.com/routing/as13335">AS13335 routing page</a> to explore both widgets, or swap in any other AS number.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-radar-researcher-and-webmcp"><a href="/changelog/post/2026-08-07-radar-researcher-and-webmcp/">Radar Researcher beta and WebMCP support now available</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Cloudflare Radar</strong></a> now includes <a href="https://radar.cloudflare.com/?prompt=">Radar Researcher</a>, a beta AI-powered assistant for exploring Internet trends and traffic data in plain language. Open Researcher from the header on any Radar page to ask questions by voice or text, receive explanations, and view interactive charts based on Radar API data.</p>
<p><img src="/assets/upstream/images/radar/radar-researcher-panel.webp" alt="Screenshot of the Radar Researcher panel alongside the Radar overview page" /></p>
<p>To ask about a specific chart, select <strong>Explain with AI</strong> to start a conversation with its underlying data and context.</p>
<p><img src="/assets/upstream/images/radar/radar-explain-with-ai.webp" alt="Screenshot of the Explain with AI option in a Radar chart menu" /></p>
<p>You can explore further with suggested follow-up questions, find earlier conversations through searchable history, and share conversations through shareable links.</p>
<p>Alongside the user-facing Researcher experience, Radar now supports <a href="/browser-run/features/webmcp/">WebMCP</a>, allowing browser-based AI agents to navigate Radar, search data, and use tools such as URL scanning and domain lookup.</p>
<p>To get started, visit <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-sandbox-sdk-1-0-preview"><a href="/changelog/post/2026-08-07-sandbox-sdk-1-0-preview/">Sandbox SDK 1.0 preview on @next</a></h2>
<div class="changelog-badges"><span>sandbox</span></div><div class="changelog-body"><p><strong>Sandbox SDK 1.0</strong> is available to preview under the npm <code>@next</code> tag. For existing applications, the current stable package remains published on the 0.12.x line.</p>
<p>Sandbox SDK first shipped to provide a rich library for running untrusted and agent-driven work on <a href="/containers/">Cloudflare Containers</a>. Since then, both Sandbox and Containers have matured. This preview is a thinner SDK built on a richer Cloudflare Containers foundation.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-what-this-preview-is">What this preview is</h4>
<ul>
<li><strong>A single execution interface</strong> — <code>sandbox.exec()</code> takes an argument list, returns when the process <strong>starts</strong>, and gives you a handle for output, logs, waits, and signals. Both short commands and long-running services use the same API.</li>
<li><strong>Removed session execution</strong> — the SDK no longer maintains shell state between executions. Each launch is independent. Pass <code>cwd</code> and <code>env</code> when you need them, or put multi-step shell syntax in one explicit shell command.</li>
<li><strong>RPC as the only transport</strong> — the SDK talks to the container exclusively over RPC. Remove <code>SANDBOX_TRANSPORT</code>, <code>transport</code> on <code>getSandbox()</code>, and <code>setTransport()</code>.</li>
<li><strong>Improved PTY and terminal interface</strong> — interactive PTYs use <code>createTerminal</code> / <code>connect</code>, not the older session-shaped helpers.</li>
<li><strong>Code interpreter as an extension</strong> — configure the code interpreter on your <code>Sandbox</code> subclass so you only ship what you need.</li>
</ul>
<p>Start new projects on <code>@next</code>. Migrate existing apps when you can so you are ready when 1.0 becomes stable. Deploy the Worker package and container image from the <strong>same</strong> <code>@next</code> line.</p>
<p>Coding agents: install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> (<a href="/agent-setup/">Agent setup</a>). Use <strong><code>sandbox-next</code></strong> for <code>@next</code> (recommended for new projects), <strong><code>sandbox-stable</code></strong> for the current stable package, and <strong><code>sandbox-migrate-to-next</code></strong> when you are ready to port. Stable-package deprecated-API cleanup is in the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation guide</a>.</p>
<p>The main <a href="/sandbox/">Sandbox documentation</a> still describes today's stable package. Preview docs:</p>
<ul>
<li><a href="/sandbox/1-0-preview/">1.0 preview</a></li>
<li><a href="/sandbox/1-0-preview/get-started/">Get started</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Processes</a> · <a href="/sandbox/1-0-preview/terminals/">Terminals</a> · <a href="/sandbox/1-0-preview/errors/">Errors</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
</ul>
<p>The self-deployed Sandbox bridge is not currently part of this preview. We are working on bringing it in line with the latest code. Until then, use the <a href="/sandbox/bridge/">stable bridge</a> with the matching stable package and container image.</p>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-timeline-for-1-0">Timeline for 1.0</h4>
<p>Further Cloudflare Containers features will let us keep reducing the size of the Sandbox SDK. We aim to ship Sandbox SDK 1.0 once those are in. In the meantime we continue to support and maintain the 1.0 preview (<code>@next</code>) alongside the current stable release.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/4/">Previous</a><span>Page 5 of 50</span><a class="pagination-next" rel="next" href="/changelog/6/">Next</a></nav>
</div>
