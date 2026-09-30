---
cp9:
  canonical: https://developers.cloudflare.com/changelog/25/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 25 | Cloudflare Docs
  head_html: <title>Changelog - page 25 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/25/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 25"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/25/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/25/#page","headline":"Changelog - page 25 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/25/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/25/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-02-23">Feb 23, 2026</time><div>
<h2 id="post-2026-02-23-Saved-views-in-threat-events"><a href="/changelog/post/2026-02-23-Saved-views-in-threat-events/">Saved views for Threat Events</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p><strong>TL;DR:</strong> You can now create and save custom configurations of the Threat Events dashboard, allowing you to instantly return to specific filtered views — such as industry-specific attacks or regional Sankey flows — without manual reconfiguration.</p>
<h4 id="2026-02-23-Saved-views-in-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is personalized. Previously, analysts had to manually re-apply complex filters (like combining specific industry datasets with geographic origins) every time they logged in. This update provides material value by:</p>
<ul>
<li>Analysts can now jump straight into &quot;Known Ransomware Infrastructure&quot; or &quot;Retail Sector Targets&quot; views with a single click, eliminating repetitive setup tasks</li>
<li>Teams can ensure everyone is looking at the same data subsets by using standardized saved views, reducing the risk of missing critical patterns due to inconsistent filtering.</li>
</ul>
<p>Cloudforce One subscribers can start saving their custom views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-20">Feb 20, 2026</time><div>
<h2 id="post-2026-02-20-codemode-sdk-rewrite"><a href="/changelog/post/2026-02-20-codemode-sdk-rewrite/">@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> package has been rewritten into a modular, runtime-agnostic SDK.</p>
<p><a href="https://blog.cloudflare.com/code-mode/">Code Mode</a> enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.</p>
<p>The new <code>Executor</code> interface is runtime agnostic and comes with a prebuilt <code>DynamicWorkerExecutor</code> to run generated code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a>.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-breaking-changes">Breaking changes</h4>
<ul>
<li>Removed <code>experimental_codemode()</code> and <code>CodeModeProxy</code> — the package no longer owns an LLM call or model choice</li>
<li>New import path: <code>createCodeTool()</code> is now exported from <code>@cloudflare/codemode/ai</code></li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-new-features">New features</h4>
<ul>
<li><strong><code>createCodeTool()</code></strong> — Returns a standard AI SDK <code>Tool</code> to use in your AI agents.</li>
<li><strong><code>Executor</code> interface</strong> — Minimal <code>execute(code, fns)</code> contract. Implement for any code sandboxing primitive or runtime.</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<p>Runs code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a>. It comes with the following features:</p>
<ul>
<li><strong>Network isolation</strong> — <code>fetch()</code> and <code>connect()</code> blocked by default (<code>globalOutbound: null</code>) when using <code>DynamicWorkerExecutor</code></li>
<li><strong>Console capture</strong> — <code>console.log/warn/error</code> captured and returned in <code>ExecuteResult.logs</code></li>
<li><strong>Execution timeout</strong> — Configurable via <code>timeout</code> option (default 30s)</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-usage">Usage</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17638.md")</div>
<h4 id="2026-02-20-codemode-sdk-rewrite-wrangler-configuration">Wrangler configuration</h4>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17639.md")</div>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for full API reference and examples.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-20">Feb 20, 2026</time><div>
<h2 id="post-2026-02-20-cloudy-in-casb"><a href="/changelog/post/2026-02-20-cloudy-in-casb/">Understand CASB findings instantly with Cloudy Summaries</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p>You can now easily understand your SaaS security posture findings and why they were detected with <strong>Cloudy Summaries in CASB</strong>. This feature integrates Cloudflare's Cloudy AI directly into your CASB Posture Findings to automatically generate clear, plain-language summaries of complex security misconfigurations, third-party app risks, and data exposures.</p>
<p>This allows security teams and IT administrators to drastically reduce triage time by immediately understanding the context, potential impact, and necessary remediation steps for any given finding—without needing to be an expert in every connected SaaS application.</p>
<p>To view a summary, simply navigate to your Posture Findings in the Cloudflare One dashboard (under <strong>Cloud and SaaS findings</strong>) and open the finding details of a specific instance of a Finding.</p>
<p>Cloudy Summaries are supported on all available integrations, including Microsoft 365, Google Workspace, Salesforce, GitHub, AWS, Slack, and Dropbox. See the full list of supported integrations <a href="/cloudflare-one/integrations/cloud-and-saas/">here</a>.</p>
<h4 id="2026-02-20-cloudy-in-casb-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Contextual explanations</strong> — Quickly understand the specifics of a finding with plain-language summaries detailing exactly what was detected, from publicly shared sensitive files to risky third-party app scopes.</li>
<li><strong>Clear risk assessment</strong> — Instantly grasp the potential security impact of the finding, such as data breach risks, unauthorized account access, or email spoofing vulnerabilities.</li>
<li><strong>Actionable guidance</strong> — Get clear recommendations and next steps on how to effectively remediate the issue and secure your environment.</li>
<li><strong>Built-in feedback</strong> — Help improve future AI summarization accuracy by submitting feedback directly using the thumbs-up and thumbs-down buttons.</li>
</ul>
<h4 id="2026-02-20-cloudy-in-casb-learn-more">Learn more</h4>
<ul>
<li>Learn more about managing <a href="/cloudflare-one/cloud-and-saas-findings/">CASB Posture Findings</a> in Cloudflare.</li>
</ul>
<p>Cloudy Summaries in CASB are available to all Cloudflare CASB users today.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-20">Feb 20, 2026</time><div>
<h2 id="post-2026-02-20-tunnel-core-dashboard"><a href="/changelog/post/2026-02-20-tunnel-core-dashboard/">Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is now available in the main Cloudflare Dashboard at <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a>, bringing first-class Tunnel management to developers using Tunnel for securing origin servers.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-core-dashboard.gif" alt="Manage Tunnels in the Core Dashboard" /></p>
<p>This new experience provides everything you need to manage Tunnels for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, including:</p>
<ul>
<li><strong>Full Tunnel lifecycle management</strong>: Create, configure, delete, and monitor all your Tunnels in one place.</li>
<li><strong>Native integrations</strong>: View Tunnels by name when configuring <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> and <a href="/workers-vpc/">Workers VPC</a> — no more copy-pasting UUIDs.</li>
<li><strong>Real-time visibility</strong>: Monitor <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> and Tunnel <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">health status</a> directly in the dashboard.</li>
<li><strong>Routing map</strong>: Manage all ingress routes for your Tunnel, including <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostnames</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">private CIDRs</a>, and <a href="/workers-vpc/">Workers VPC services</a>, from a single interactive interface.</li>
</ul>
<h4 id="2026-02-20-tunnel-core-dashboard-choose-the-right-dashboard-for-your-use-case">Choose the right dashboard for your use case</h4>
<p><strong>Core Dashboard</strong>: Navigate to <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a> to manage Tunnels for:</p>
<ul>
<li>Securing origin servers and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a> with CDN, WAF, Load Balancing, and DDoS protection</li>
<li>Connecting <a href="/workers-vpc/">Workers to private services</a> via Workers VPC</li>
</ul>
<p><strong>Cloudflare One Dashboard</strong>: Navigate to <a href="https://one.dash.cloudflare.com/?to=/:account/networks/connectors">Zero Trust &gt; Networks &gt; Connectors</a> to manage Tunnels for:</p>
<ul>
<li>Securing your public applications with <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Zero Trust access policies</a></li>
<li>Connecting users to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a></li>
<li>Building a <a href="/reference-architecture/architectures/sase/#connecting-networks">private mesh network</a></li>
</ul>
<p>Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.</p>
<h4 id="2026-02-20-tunnel-core-dashboard-get-started">Get started</h4>
<p>New to Tunnel? Learn how to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">get started with Cloudflare Tunnel</a> or explore advanced use cases like <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">securing SSH servers</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running Tunnels in Kubernetes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-19">Feb 19, 2026</time><div>
<h2 id="post-2026-02-19-ai-dashboard-experience-improvements"><a href="/changelog/post/2026-02-19-ai-dashboard-experience-improvements/">AI dashboard experience improvements</a></h2>
<div class="changelog-badges"><span>ai-gateway</span><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/">Workers AI</a> and <a href="/ai-gateway/">AI Gateway</a> have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.</p>
<p><strong>Navigation and discoverability</strong></p>
<p>AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.</p>
<p><img src="/assets/upstream/images/ai-gateway/sidebar-navigation.png" alt="AI sidebar navigation in the Cloudflare dashboard" />
<em>The new top-level AI section in the dashboard sidebar.</em></p>
<p><strong>Onboarding and getting started</strong></p>
<p><a href="/ai-gateway/get-started/">Getting started</a> with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.</p>
<p><img src="/assets/upstream/images/ai-gateway/onboarding-flow.png" alt="AI Gateway onboarding flow" />
<em>The first-run setup experience for new gateways.</em></p>
<p>We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.</p>
<p><strong>Dynamic Routing</strong></p>
<ul>
<li>The <a href="/ai-gateway/features/dynamic-routing/">route builder</a> is now more performant and responsive.</li>
<li>You can now copy route names to your clipboard with a single click.</li>
<li>Code examples use the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> format, making it easier to integrate routes into your application.</li>
</ul>
<p><strong>Observability and analytics</strong></p>
<ul>
<li>Small monetary values now display correctly in <a href="/ai-gateway/observability/costs/">cost analytics</a> charts, so you can accurately track spending at any scale.</li>
</ul>
<p><strong>Accessibility</strong></p>
<ul>
<li>Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by <a href="/ai-gateway/usage/providers/">provider</a>.</li>
<li>Improvements to sorting and filtering components on the <a href="/workers-ai/models/">Workers AI</a> models page.</li>
</ul>
<p>For more information, refer to the <a href="/ai-gateway/">AI Gateway documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-19">Feb 19, 2026</time><div>
<h2 id="post-2026-02-19-dex-supports-cmb-eu"><a href="/changelog/post/2026-02-19-dex-supports-cmb-eu/">DEX Supports EU Customer Metadata Boundary</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into <a href="/warp-client/">WARP</a> device connectivity and performance to any internal or external application.</p>
<p>Now, all DEX logs are fully compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.</p>
<p>If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via <a href="/logs/logpush/">LogPush</a>, and build their own analytics and dashboards.</p>
<p>If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: &quot;DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets.&quot;</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_supports_cmb.png" alt="Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-19">Feb 19, 2026</time><div>
<h2 id="post-2026-02-19-threat-events-graphs"><a href="/changelog/post/2026-02-19-threat-events-graphs/">Cloudforce One Threat events graphs are now visible in the dashboard</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We have introduced dynamic visualizations to the Threat Events dashboard to help you better understand the threat landscape and identify emerging patterns at a glance.</p>
<p>What's new:</p>
<ul>
<li><strong>Sankey Diagrams</strong>: Trace the flow of attacks from country of origin to target country to identify which regions are being hit hardest and where the threat infrastructure resides.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-sankey-diagram.png" alt="Sankey Diagram" /></p>
<ul>
<li><strong>Dataset Distribution over time</strong>: Instantly pivot your view to understand if a specific campaign is targeting your sector or if it is a broad-spectrum commodity attack.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-events-over-time.png" alt="Events over time" /></p>
<ul>
<li><strong>Enhanced Filtering</strong>: Use these visual tools to filter and drill down into specific attack vectors directly from the charts.</li>
</ul>
<p>Cloudforce One subscribers can explore these new views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-18">Feb 18, 2026</time><div>
<h2 id="post-2026-02-18-cfworker-server-timing"><a href="/changelog/post/2026-02-18-cfworker-server-timing/">New cfWorker metric in Server-Timing header</a></h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The Server-Timing header now includes a new <code>cfWorker</code> metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.</p>
<p>Previously, Worker execution time was included in the <code>edge</code> metric, making it harder to identify true edge performance. The new <code>cfWorker</code> metric provides this visibility:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>edge</code></td>
<td>Total time spent on the Cloudflare edge, including Worker execution</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>Time spent fetching from the origin server</td>
</tr>
<tr>
<td><code>cfWorker</code></td>
<td>Time spent in Worker execution, including subrequests but excluding origin fetch time</td>
</tr>
</tbody>
</table>
<h4 id="2026-02-18-cfworker-server-timing-example-response">Example response</h4>
<pre tabindex="0"><code class="language-txt">Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7&#10;</code></pre>
<p>In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.</p>
<h4 id="2026-02-18-cfworker-server-timing-availability">Availability</h4>
<p>The <code>cfWorker</code> metric is enabled by default if you have <a href="/web-analytics/">Real User Monitoring (RUM)</a> enabled. Otherwise, you can enable it using <a href="/rules/">Rules</a>.</p>
<p>This metric is particularly useful for:</p>
<ul>
<li><strong>Performance debugging</strong>: Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.</li>
<li><strong>Optimization targeting</strong>: Identify which component of your request path needs optimization.</li>
<li><strong>Real User Monitoring (RUM)</strong>: Access detailed timing breakdowns directly from response headers for client-side analytics.</li>
</ul>
<p>For more information about Server-Timing headers, refer to the <a href="https://www.w3.org/TR/server-timing/">W3C Server Timing specification</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-17">Feb 17, 2026</time><div>
<h2 id="post-2026-02-17-clientless-access-for-private-apps"><a href="/changelog/post/2026-02-17-clientless-access-for-private-apps/">Streamlined clientless browser isolation for private applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>A new <strong>Allow clientless access</strong> setting makes it easier to connect users without a device client to internal applications, without using public DNS.</p>
<p><img src="/assets/upstream/images/changelog/access/allow-clientless-access.png" alt="Allow clientless access setting in the Cloudflare One dashboard" /></p>
<p>Previously, to provide clientless access to a private hostname or IP without a <a href="/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route">published application</a>, you had to create a separate <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark application</a> pointing to a prefixed <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> URL (for example, <code>https://&lt;your-teamname&gt;.cloudflareaccess.com/browser/https://10.0.0.1/</code>). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.</p>
<p>Now, you can manage clientless access directly within your <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private self-hosted application</a>. When  <strong>Allow clientless access</strong> is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">remote browser permissions</a> to open the link.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-17">Feb 17, 2026</time><div>
<h2 id="post-2026-02-17-policies-for-bookmarks"><a href="/changelog/post/2026-02-17-policies-for-bookmarks/">Policies for bookmark applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>You can now assign <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark applications</a>. This lets you control which users see a bookmark in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> based on identity, device posture, and other policy rules.</p>
<p>Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:</p>
<ul>
<li><strong>Tailor the App Launcher to each user</strong> — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.</li>
<li><strong>Restrict visibility of sensitive bookmarks</strong> — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.</li>
</ul>
<p>Bookmarks support all <a href="/cloudflare-one/access-controls/policies/">Access policy configurations</a> except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/bookmarks/">Add bookmarks</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-17">Feb 17, 2026</time><div>
<h2 id="post-2026-02-17-agents-sdk-v0.5.0"><a href="/changelog/post/2026-02-17-agents-sdk-v0.5.0/">Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds built-in retry utilities, per-connection protocol message control, and a fully rewritten <code>@cloudflare/ai-chat</code> with data parts, tool approval persistence, and zero breaking changes.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-retry-utilities">Retry utilities</h4>
<p>A new <code>this.retry()</code> method lets you retry any async operation with exponential backoff and jitter. You can pass an optional <code>shouldRetry</code> predicate to bail early on non-retryable errors.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17635.md")</div>
<p>Retry options are also available per-task on <code>queue()</code>, <code>schedule()</code>, <code>scheduleEvery()</code>, and <code>addMcpServer()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17636.md")</div>
<p>Retry options are validated eagerly at enqueue/schedule time, and invalid values throw immediately. Internal retries have also been added for workflow operations (<code>terminateWorkflow</code>, <code>pauseWorkflow</code>, and others) with Durable Object-aware error detection.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-per-connection-protocol-message-control">Per-connection protocol message control</h4>
<p>Agents automatically send JSON text frames (identity, state, MCP server lists) to every WebSocket connection. You can now suppress these per-connection for clients that cannot handle them — binary-only devices, MQTT clients, or lightweight embedded systems.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17637.md")</div>
<p>Connections with protocol messages disabled still fully participate in RPC and regular messaging. Use <code>isConnectionProtocolEnabled(connection)</code> to check a connection's status at any time. The flag persists across Durable Object hibernation.</p>
<p>See <a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a> for full documentation.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-cloudflare-ai-chat-v0-1-0"><code>@cloudflare/ai-chat</code> v0.1.0</h4>
<p>The first stable release of <code>@cloudflare/ai-chat</code> ships alongside this release with a major refactor of <code>AIChatAgent</code> internals — new <code>ResumableStream</code> class, WebSocket <code>ChatTransport</code>, and simplified SSE parsing — with zero breaking changes. Existing code using <code>AIChatAgent</code> and <code>useAgentChat</code> works as-is.</p>
<p>Key new features:</p>
<ul>
<li><strong>Data parts</strong> — Attach typed JSON blobs (<code>data-*</code>) to messages alongside text. Supports reconciliation (type+id updates in-place), append, and transient parts (ephemeral via <code>onData</code> callback). See <a href="/agents/communication-channels/chat/chat-agents/#data-parts">Data parts</a>.</li>
<li><strong>Tool approval persistence</strong> — The <code>needsApproval</code> approval UI now survives page refresh and DO hibernation. The streaming message is persisted to SQLite when a tool enters <code>approval-requested</code> state.</li>
<li><strong><code>maxPersistedMessages</code></strong> — Cap SQLite message storage with automatic oldest-message deletion.</li>
<li><strong><code>body</code> option on <code>useAgentChat</code></strong> — Send custom data with every request (static or dynamic).</li>
<li><strong>Incremental persistence</strong> — Hash-based cache to skip redundant SQL writes.</li>
<li><strong>Row size guard</strong> — Automatic two-pass compaction when messages approach the SQLite 2 MB limit.</li>
<li><strong><code>autoContinueAfterToolResult</code> defaults to <code>true</code></strong> — Client-side tool results and tool approvals now automatically trigger a server continuation, matching server-executed tool behavior. Set <code>autoContinueAfterToolResult: false</code> in <code>useAgentChat</code> to restore the previous behavior.</li>
</ul>
<p>Notable bug fixes:</p>
<ul>
<li>Resolved stream resumption race conditions</li>
<li>Resolved an issue where <code>setMessages</code> functional updater sent empty arrays</li>
<li>Resolved an issue where client tool schemas were lost after DO hibernation</li>
<li>Resolved <code>InvalidPromptError</code> after tool approval (<code>approval.id</code> was dropped)</li>
<li>Resolved an issue where message metadata was not propagated on broadcast/resume paths</li>
<li>Resolved an issue where <code>clearAll()</code> did not clear in-memory chunk buffers</li>
<li>Resolved an issue where <code>reasoning-delta</code> silently dropped data when <code>reasoning-start</code> was missed during stream resumption</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-synchronous-queue-and-schedule-getters">Synchronous queue and schedule getters</h4>
<p><code>getQueue()</code>, <code>getQueues()</code>, <code>getSchedule()</code>, <code>dequeue()</code>, <code>dequeueAll()</code>, and <code>dequeueAllByCallback()</code> were unnecessarily <code>async</code> despite only performing synchronous SQL operations. They now return values directly instead of wrapping them in Promises. This is backward compatible — existing code using <code>await</code> on these methods will continue to work.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Fix TypeScript &quot;excessively deep&quot; error</strong> — A depth counter on <code>CanSerialize</code> and <code>IsSerializableParam</code> types bails out to <code>true</code> after 10 levels of recursion, preventing the &quot;Type instantiation is excessively deep&quot; error with deeply nested types like AI SDK <code>CoreMessage[]</code>.</li>
<li><strong>POST SSE keepalive</strong> — The POST SSE handler now sends <code>event: ping</code> every 30 seconds to keep the connection alive, matching the existing GET SSE handler behavior. This prevents POST response streams from being silently dropped by proxies during long-running tool calls.</li>
<li><strong>Widened peer dependency ranges</strong> — Peer dependency ranges across packages have been widened to prevent cascading major bumps during 0.x minor releases. <code>@cloudflare/ai-chat</code> and <code>@cloudflare/codemode</code> are now marked as optional peer dependencies.</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-17">Feb 17, 2026</time><div>
<h2 id="post-2026-02-17-product-name-updates"><a href="/changelog/post/2026-02-17-product-name-updates/">Cloudflare One Product Name Updates</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span><span>cloudflare-network-firewall</span><span>network-flow</span></div><div class="changelog-body"><p>We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.</p>
<p>We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.</p>
<h4 id="2026-02-17-product-name-updates-what-s-changing">What's changing</h4>
<ul>
<li><strong>Magic WAN</strong> → <strong>Cloudflare WAN</strong></li>
<li><strong>Magic WAN IPsec</strong> → <strong>Cloudflare IPsec</strong></li>
<li><strong>Magic WAN GRE</strong> → <strong>Cloudflare GRE</strong></li>
<li><strong>Magic WAN Connector</strong> → <strong>Cloudflare One Appliance</strong></li>
<li><strong>Magic Firewall</strong> → <strong>Cloudflare Network Firewall</strong></li>
<li><strong>Magic Network Monitoring</strong> → <strong>Network Flow</strong></li>
<li><strong>Magic Cloud Networking</strong> → <strong>Cloudflare One Multi-cloud Networking</strong></li>
</ul>
<p><strong>No action is required by you</strong> — all functionality, existing configurations, and billing will remain exactly the same.</p>
<p>For more information, visit the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-17">Feb 17, 2026</time><div>
<h2 id="post-2026-02-17-docker-in-docker"><a href="/changelog/post/2026-02-17-docker-in-docker/">Docker-in-Docker support added to Containers and Sandboxes</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support running Docker for &quot;Docker-in-Docker&quot; setups. This is particularly useful when your end users or <a href="/agents">agents</a> want to run a full sandboxed development environment.</p>
<p>This allows you to:</p>
<ul>
<li>Develop containerized applications with your Sandbox</li>
<li>Run isolated test environments for images</li>
<li>Build container images as part of CI/CD workflows</li>
<li>Deploy arbitrary images supplied at runtime within a container</li>
</ul>
<p>For <a href="/sandbox/">Sandbox SDK</a> users, see the <a href="/sandbox/guides/docker-in-docker/">Docker-in-Docker guide</a> for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the <a href="/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker">Containers FAQ</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-16">Feb 16, 2026</time><div>
<h2 id="post-2026-02-16-markdown-for-agents-improvements"><a href="/changelog/post/2026-02-16-markdown-for-agents-improvements/">Content encoding support for Markdown for Agents and other improvements</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>When AI systems request pages from any website that uses Cloudflare and has <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> enabled, they can express the preference for <code>text/markdown</code> in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.</p>
<p>This release adds the following improvements:</p>
<ul>
<li>The origin response limit was raised from 1 MB to 2 MB (2,097,152 bytes).</li>
<li>We no longer require the origin to send the <code>content-length</code> header.</li>
<li>We now support content encoded responses from the origin.</li>
</ul>
<p>If you haven’t enabled automatic Markdown conversion yet, visit the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ai">AI Crawl Control</a> section of the Cloudflare dashboard and enable <strong>Markdown for Agents</strong>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-16">Feb 16, 2026</time><div>
<h2 id="post-2026-02-16-waf-release"><a href="/changelog/post/2026-02-16-waf-release/">WAF Release - 2026-02-16</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for CVE-2025-68645 and CVE-2025-31125.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-68645: A Local File Inclusion (LFI) vulnerability in the Webmail Classic UI of Zimbra Collaboration Suite (ZCS) 10.0 and 10.1 allows unauthenticated remote attackers to craft requests to the <code>/h/rest</code> endpoint, improperly influence internal dispatching, and include arbitrary files from the WebRoot directory.</li>
<li>CVE-2025-31125: Vite, the JavaScript frontend tooling framework, exposes content of non-allowed files via <code>?inline&amp;import</code> when its development server is network-exposed, enabling unauthorized attackers to read arbitrary files and potentially leak sensitive information.</li>
</ul>
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
				<code class="nb-rule-id" title="695d76ff756844d384cab548833761f7">833761f7</code>
</td>
<td>N/A</td>
<td>Zimbra - Local File Inclusion - CVE:CVE-2025-68645</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="38fff9f3deba46a2abc10a8f950ed8c8">950ed8c8</code>
</td>
<td>N/A</td>
<td>Vite - WASM Import Path Traversal - CVE:CVE-2025-31125</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-16">Feb 16, 2026</time><div>
<h2 id="post-2026-02-12-quick-editor-dev-tools-deprecation"><a href="/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/">Quick Editor devtools replaced with log viewer</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Cloudflare has deprecated the Workers Quick Editor dev tools inspector and replaced it with a lightweight log viewer.</p>
<p>This aligns our logging with <code>wrangler tail</code> and gives us the opportunity to focus our efforts on bringing benefits from the work we have invested in observability, which would not be possible otherwise.</p>
<p>We have made improvements to this logging viewer based on your feedback such that you can log object and array types, and easily clear the list of logs. This does not include class instances. Limitations are documented in the <a href="/workers/playground/">Workers Playground docs</a>.</p>
<p>If you do need to develop your Worker with a remote inspector, you can still do this using Wrangler locally. Cloning a project from your quick editor to your computer for local development can be done with the <code>wrangler init --from-dash</code> command. For more information, refer to <a href="/workers/wrangler/commands/general/#init">Wrangler commands</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-15">Feb 15, 2026</time><div>
<h2 id="post-2026-02-15-workers-best-practices"><a href="/changelog/post/2026-02-15-workers-best-practices/">New Best Practices guide for Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>A new <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a> guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Keep your compatibility date current and enable <code>nodejs_compat</code></strong> — Ensure you have access to the latest runtime features and Node.js built-in modules.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17799.md")</div>
- **Generate binding types with `wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
- **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
- **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
- **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
- **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
- **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
- **Always `await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
- **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.
<p>To learn more, refer to <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-13">Feb 13, 2026</time><div>
<h2 id="post-2026-02-13-access-policy-service-token-permissions"><a href="/changelog/post/2026-02-13-access-policy-service-token-permissions/">Fine-grained permissions for Access policies and service tokens</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>access</span></div><div class="changelog-body"><p>Fine-grained permissions for <strong>Access policies</strong> and <strong>Access service tokens</strong> are available. These new resource-scoped roles expand the existing RBAC model, enabling administrators to grant permissions scoped to individual resources.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-13">Feb 13, 2026</time><div>
<h2 id="post-2026-02-13-cloudflare-python-v5.0.0-beta.1"><a href="/changelog/post/2026-02-13-cloudflare-python-v5.0.0-beta.1/">Cloudflare Python SDK v5.0.0-beta.1 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>sdk</span></div><div class="changelog-body"><blockquote>
<p><strong>Disclaimer:</strong> Please note that v5.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0-beta.1">v4.3.1...v5.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions,
which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce
our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>There may be changes that are not captured in this changelog. Feel free to open an issue to report any inaccuracies, and we will make sure it gets into the changelog before the v5.0.0 release.</p>
<p>Most of the breaking changes below are caused by improvements to the accuracy of the base OpenAPI schemas, which
sometimes translates to breaking changes in downstream clients that depend on those schemas.</p>
<p>Please ensure you read through the list of changes below and the migration guide before moving to this version - this
will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-breaking-changes">Breaking Changes</h4>
<p><strong>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/v5-migration-guide.md">v5 Migration Guide</a> for detailed migration instructions.</strong></p>
<ul>
<li><code>abusereports</code></li>
<li><code>acm.totaltls</code></li>
<li><code>apigateway.configurations</code></li>
<li><code>cloudforceone.threatevents</code></li>
<li><code>d1.database</code></li>
<li><code>intel.indicatorfeeds</code></li>
<li><code>logpush.edge</code></li>
<li><code>origintlsclientauth.hostnames</code></li>
<li><code>queues.consumers</code></li>
<li><code>radar.bgp</code></li>
<li><code>rulesets.rules</code></li>
<li><code>schemavalidation.schemas</code></li>
<li><code>snippets</code></li>
<li><code>zerotrust.dlp</code></li>
<li><code>zerotrust.networks</code></li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-features">Features</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-new-api-resources">New API Resources</h4>
<ul>
<li><code>abusereports</code> - Abuse report management</li>
<li><code>abusereports.mitigations</code> - Abuse report mitigation actions</li>
<li><code>ai.tomarkdown</code> - AI-powered markdown conversion</li>
<li><code>aigateway.dynamicrouting</code> - AI Gateway dynamic routing configuration</li>
<li><code>aigateway.providerconfigs</code> - AI Gateway provider configurations</li>
<li><code>aisearch</code> - AI-powered search functionality</li>
<li><code>aisearch.instances</code> - AI Search instance management</li>
<li><code>aisearch.tokens</code> - AI Search authentication tokens</li>
<li><code>alerting.silences</code> - Alert silence management</li>
<li><code>brandprotection.logomatches</code> - Brand protection logo match detection</li>
<li><code>brandprotection.logos</code> - Brand protection logo management</li>
<li><code>brandprotection.matches</code> - Brand protection match results</li>
<li><code>brandprotection.queries</code> - Brand protection query management</li>
<li><code>cloudforceone.binarystorage</code> - CloudForce One binary storage</li>
<li><code>connectivity.directory</code> - Connectivity directory services</li>
<li><code>d1.database</code> - D1 database management</li>
<li><code>diagnostics.endpointhealthchecks</code> - Endpoint health check diagnostics</li>
<li><code>fraud</code> - Fraud detection and prevention</li>
<li><code>iam.sso</code> - IAM Single Sign-On configuration</li>
<li><code>loadbalancers.monitorgroups</code> - Load balancer monitor groups</li>
<li><code>organizations</code> - Organization management</li>
<li><code>organizations.organizationprofile</code> - Organization profile settings</li>
<li><code>origintlsclientauth.hostnamecertificates</code> - Origin TLS client auth hostname certificates</li>
<li><code>origintlsclientauth.hostnames</code> - Origin TLS client auth hostnames</li>
<li><code>origintlsclientauth.zonecertificates</code> - Origin TLS client auth zone certificates</li>
<li><code>pipelines</code> - Data pipeline management</li>
<li><code>pipelines.sinks</code> - Pipeline sink configurations</li>
<li><code>pipelines.streams</code> - Pipeline stream configurations</li>
<li><code>queues.subscriptions</code> - Queue subscription management</li>
<li><code>r2datacatalog</code> - R2 Data Catalog integration</li>
<li><code>r2datacatalog.credentials</code> - R2 Data Catalog credentials</li>
<li><code>r2datacatalog.maintenanceconfigs</code> - R2 Data Catalog maintenance configurations</li>
<li><code>r2datacatalog.namespaces</code> - R2 Data Catalog namespaces</li>
<li><code>radar.bots</code> - Radar bot analytics</li>
<li><code>radar.ct</code> - Radar certificate transparency data</li>
<li><code>radar.geolocations</code> - Radar geolocation data</li>
<li><code>realtimekit.activesession</code> - Real-time Kit active session management</li>
<li><code>realtimekit.analytics</code> - Real-time Kit analytics</li>
<li><code>realtimekit.apps</code> - Real-time Kit application management</li>
<li><code>realtimekit.livestreams</code> - Real-time Kit live streaming</li>
<li><code>realtimekit.meetings</code> - Real-time Kit meeting management</li>
<li><code>realtimekit.presets</code> - Real-time Kit preset configurations</li>
<li><code>realtimekit.recordings</code> - Real-time Kit recording management</li>
<li><code>realtimekit.sessions</code> - Real-time Kit session management</li>
<li><code>realtimekit.webhooks</code> - Real-time Kit webhook configurations</li>
<li><code>tokenvalidation.configuration</code> - Token validation configuration</li>
<li><code>tokenvalidation.rules</code> - Token validation rules</li>
<li><code>workers.beta</code> - Workers beta features</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-new-endpoints-existing-resources">New Endpoints (Existing Resources)</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-acm-totaltls"><code>acm.totaltls</code></h4>
- `edit()`
- `update()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-cloudforceone-threatevents"><code>cloudforceone.threatevents</code></h4>
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-contentscanning"><code>contentscanning</code></h4>
- `create()`
- `get()`
- `update()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-dns-records"><code>dns.records</code></h4>
- `scan_list()`
- `scan_review()`
- `scan_trigger()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-intel-indicatorfeeds"><code>intel.indicatorfeeds</code></h4>
- `create()`
- `delete()`
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-leakedcredentialchecks-detections"><code>leakedcredentialchecks.detections</code></h4>
- `get()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-queues-consumers"><code>queues.consumers</code></h4>
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-radar-ai"><code>radar.ai</code></h4>
- `summary()`
- `timeseries()`
- `timeseries_groups()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-radar-bgp"><code>radar.bgp</code></h4>
- `changes()`
- `snapshot()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-workers-subdomains"><code>workers.subdomains</code></h4>
- `delete()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-zerotrust-networks"><code>zerotrust.networks</code></h4>
- `create()`
- `delete()`
- `edit()`
- `get()`
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-general-fixes-and-improvements">General Fixes and Improvements</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-type-system-compatibility">Type System &amp; Compatibility</h4>
<ul>
<li><strong>Type inference improvements</strong>: Allow Pyright to properly infer TypedDict types within SequenceNotStr</li>
<li><strong>Type completeness</strong>: Add missing types to method arguments and response models</li>
<li><strong>Pydantic compatibility</strong>: Ensure compatibility with Pydantic versions prior to 2.8.0 when using additional fields</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-request-response-handling">Request/Response Handling</h4>
<ul>
<li><strong>Multipart form data</strong>: Correctly handle sending multipart/form-data requests with JSON data</li>
<li><strong>Header handling</strong>: Do not send headers with default values set to omit</li>
<li><strong>GET request headers</strong>: Don't send Content-Type header on GET requests</li>
<li><strong>Response body model accuracy</strong>: Broad improvements to the correctness of models</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-parsing-data-processing">Parsing &amp; Data Processing</h4>
<ul>
<li><strong>Discriminated unions</strong>: Correctly handle nested discriminated unions in response parsing</li>
<li><strong>Extra field types</strong>: Parse extra field types correctly</li>
<li><strong>Empty metadata</strong>: Ignore empty metadata fields during parsing</li>
<li><strong>Singularization rules</strong>: Update resource name singularization rules for better consistency</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-13">Feb 13, 2026</time><div>
<h2 id="post-2026-02-13-glm-4.7-flash-workers-ai"><a href="/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/">Introducing GLM-4.7-Flash on Workers AI, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1</a></h2>
<div class="changelog-badges"><span>workers</span><span>agents</span><span>workers-ai</span></div><div class="changelog-body"><p>We're excited to announce <strong>GLM-4.7-Flash</strong> on Workers AI, a fast and efficient text generation model optimized for multilingual dialogue and instruction-following tasks, along with the brand-new <a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai"><strong>@cloudflare/tanstack-ai</strong></a> package and <a href="https://www.npmjs.com/package/workers-ai-provider"><strong>workers-ai-provider v3.1.1</strong></a>.</p>
<p>You can now run AI agents entirely on Cloudflare. With GLM-4.7-Flash's multi-turn tool calling support, plus full compatibility with TanStack AI and the Vercel AI SDK, you have everything you need to build agentic applications that run completely at the edge.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-glm-4-7-flash-multilingual-text-generation-model">GLM-4.7-Flash — Multilingual Text Generation Model</h4>
<p><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> is a multilingual model with a 131,072 token context window, making it ideal for long-form content generation, complex reasoning tasks, and multilingual applications.</p>
<p><strong>Key Features and Use Cases:</strong></p>
<ul>
<li><strong>Multi-turn Tool Calling for Agents</strong>: Build AI agents that can call functions and tools across multiple conversation turns</li>
<li><strong>Multilingual Support</strong>: Built to handle content generation in multiple languages effectively</li>
<li><strong>Large Context Window</strong>: 131,072 tokens for long-form writing, complex reasoning, and processing long documents</li>
<li><strong>Fast Inference</strong>: Optimized for low-latency responses in chatbots and virtual assistants</li>
<li><strong>Instruction Following</strong>: Excellent at following complex instructions for code generation and structured tasks</li>
</ul>
<p>Use GLM-4.7-Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via <a href="/workers-ai/configuration/ai-sdk/">workers-ai-provider</a> for the Vercel AI SDK.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-4.7-flash/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-cloudflare-tanstack-ai-v0-1-1-tanstack-ai-adapters-for-workers-ai-and-ai-gateway">@cloudflare/tanstack-ai v0.1.1 — TanStack AI adapters for Workers AI and AI Gateway</h4>
<p>We've released <code>@cloudflare/tanstack-ai</code>, a new package that brings Workers AI and AI Gateway support to <a href="https://tanstack.com/ai">TanStack AI</a>. This provides a framework-agnostic alternative for developers who prefer TanStack's approach to building AI applications.</p>
<p><strong>Workers AI adapters</strong> support four configuration modes — plain binding (<code>env.AI</code>), plain REST, AI Gateway binding (<code>env.AI.gateway(id)</code>), and AI Gateway REST — across all capabilities:</p>
<ul>
<li><strong>Chat</strong> (<code>createWorkersAiChat</code>) — Streaming chat completions with tool calling, structured output, and reasoning text streaming.</li>
<li><strong>Image generation</strong> (<code>createWorkersAiImage</code>) — Text-to-image models.</li>
<li><strong>Transcription</strong> (<code>createWorkersAiTranscription</code>) — Speech-to-text.</li>
<li><strong>Text-to-speech</strong> (<code>createWorkersAiTts</code>) — Audio generation.</li>
<li><strong>Summarization</strong> (<code>createWorkersAiSummarize</code>) — Text summarization.</li>
</ul>
<p><strong>AI Gateway adapters</strong> route requests from third-party providers — OpenAI, Anthropic, Gemini, Grok, and OpenRouter — through Cloudflare AI Gateway for caching, rate limiting, and unified billing.</p>
<p>To get started:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/tanstack-ai @tanstack/ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-workers-ai-provider-v3-1-1-transcription-speech-reranking-and-reliability">workers-ai-provider v3.1.1 — transcription, speech, reranking, and reliability</h4>
<p>The Workers AI provider for the <a href="https://ai-sdk.dev">Vercel AI SDK</a> now supports three new capabilities beyond chat and image generation:</p>
<ul>
<li><strong>Transcription</strong> (<code>provider.transcription(model)</code>) — Speech-to-text with automatic handling of model-specific input formats across binding and REST paths.</li>
<li><strong>Text-to-speech</strong> (<code>provider.speech(model)</code>) — Audio generation with support for voice and speed options.</li>
<li><strong>Reranking</strong> (<code>provider.reranking(model)</code>) — Document reranking for RAG pipelines and search result ordering.</li>
</ul>
<pre tabindex="0"><code class="language-typescript">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import {&#10;	experimental_transcribe,&#10;	experimental_generateSpeech,&#10;	rerank,&#10;} from &quot;ai&quot;;&#10;&#10;const workersai = createWorkersAI({ binding: env.AI });&#10;&#10;const transcript = await experimental_transcribe({&#10;	model: workersai.transcription(&quot;@cf/openai/whisper-large-v3-turbo&quot;),&#10;	audio: audioData,&#10;	mediaType: &quot;audio/wav&quot;,&#10;});&#10;&#10;const speech = await experimental_generateSpeech({&#10;	model: workersai.speech(&quot;@cf/deepgram/aura-1&quot;),&#10;	text: &quot;Hello world&quot;,&#10;	voice: &quot;asteria&quot;,&#10;});&#10;&#10;const ranked = await rerank({&#10;	model: workersai.reranking(&quot;@cf/baai/bge-reranker-base&quot;),&#10;	query: &quot;What is machine learning?&quot;,&#10;	documents: [&quot;ML is a branch of AI.&quot;, &quot;The weather is sunny.&quot;],&#10;});&#10;</code></pre>
<p>This release also includes a comprehensive reliability overhaul (v3.0.5):</p>
<ul>
<li><strong>Fixed streaming</strong> — Responses now stream token-by-token instead of buffering all chunks, using a proper <code>TransformStream</code> pipeline with backpressure.</li>
<li><strong>Fixed tool calling</strong> — Resolved issues with tool call ID sanitization, conversation history preservation, and a heuristic that silently fell back to non-streaming mode when tools were defined.</li>
<li><strong>Premature stream termination detection</strong> — Streams that end unexpectedly now report <code>finishReason: &quot;error&quot;</code> instead of silently reporting <code>&quot;stop&quot;</code>.</li>
<li><strong>AI Search support</strong> — Added <code>createAISearch</code> as the canonical export (renamed from AutoRAG). <code>createAutoRAG</code> still works with a deprecation warning.</li>
</ul>
<p>To upgrade:</p>
<pre tabindex="0"><code class="language-sh">npm install workers-ai-provider@latest ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-resources">Resources</h4>
<ul>
<li><a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai">@cloudflare/tanstack-ai on npm</a></li>
<li><a href="https://www.npmjs.com/package/workers-ai-provider">workers-ai-provider on npm</a></li>
<li><a href="https://github.com/cloudflare/ai">GitHub repository</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-13">Feb 13, 2026</time><div>
<h2 id="post-2026-02-13-origin-ca-certificate-support"><a href="/changelog/post/2026-02-13-origin-ca-certificate-support/">Origin CA certificate support for Workers VPC</a></h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>Workers VPC now supports <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificates</a> when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).</p>
<p>With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the <code>https</code> scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.</p>
<p>For more information, refer to <a href="/workers-vpc/configuration/vpc-services/#supported-tls-certificates">Supported TLS certificates</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-12">Feb 12, 2026</time><div>
<h2 id="post-2026-02-12-anycast-ips-on-dashboard"><a href="/changelog/post/2026-02-12-anycast-ips-on-dashboard/">Anycast IPs displayed on the dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.</p>
<p>Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.</p>
<p>No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-12">Feb 12, 2026</time><div>
<h2 id="post-2026-02-12-markdown-for-agents"><a href="/changelog/post/2026-02-12-markdown-for-agents/">Introducing Markdown for Agents</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare's network now supports real-time content conversion at the source, for enabled zones using <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation">content negotiation</a> headers. When AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for <code>text/markdown</code> in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.</p>
<p>Here is a curl example with the <code>Accept</code> negotiation header requesting this page from our developer documentation:</p>
<pre tabindex="0"><code class="language-bash">curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \&#10;  &#45;H &quot;Accept: text/markdown&quot;&#10;</code></pre>
<p>The response to this request is now formatted in markdown:</p>
<pre tabindex="0"><code class="language-http">HTTP/2 200&#10;date: Wed, 11 Feb 2026 11:44:48 GMT&#10;content-type: text/markdown; charset=utf-8&#10;content-length: 2899&#10;vary: accept&#10;x-markdown-tokens: 725&#10;content-signal: ai-train=yes, search=yes, ai-input=yes&#10;&#10;&#45;--&#10;title: Markdown for Agents · Cloudflare Agents docs&#10;&#45;--&#10;&#10;&#35;# What is Markdown for Agents&#10;&#10;Markdown has quickly become the lingua franca for agents and AI systems&#10;as a whole. The format’s explicit structure makes it ideal for AI processing,&#10;ultimately resulting in better results while minimizing token waste.&#10;...&#10;</code></pre>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> and our <a href="https://blog.cloudflare.com/markdown-for-agents/">blog announcement</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-12">Feb 12, 2026</time><div>
<h2 id="post-2026-02-12-radar-ai-bots-content-type"><a href="/changelog/post/2026-02-12-radar-ai-bots-content-type/">Content Type Dimension for AI Bots in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes content type insights for AI bot and crawler traffic. The new <code>content_type</code> dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.</p>
<p>The content type dimension and filter are available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/"><code>/ai/bots/summary/content_type</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/"><code>/ai/bots/timeseries_groups/content_type</code></a></li>
</ul>
<p>Content type categories:</p>
<ul>
<li><strong>HTML</strong> - Web pages (<code>text/html</code>)</li>
<li><strong>Images</strong> - All image formats (<code>image/*</code>)</li>
<li><strong>JSON</strong> - JSON data and API responses (<code>application/json</code>, <code>*+json</code>)</li>
<li><strong>JavaScript</strong> - Scripts (<code>application/javascript</code>, <code>text/javascript</code>)</li>
<li><strong>CSS</strong> - Stylesheets (<code>text/css</code>)</li>
<li><strong>Plain Text</strong> - Unformatted text (<code>text/plain</code>)</li>
<li><strong>Fonts</strong> - Web fonts (<code>font/*</code>, <code>application/font-*</code>)</li>
<li><strong>XML</strong> - XML documents and feeds (<code>text/xml</code>, <code>application/xml</code>, <code>application/rss+xml</code>, <code>application/atom+xml</code>)</li>
<li><strong>YAML</strong> - Configuration files (<code>text/yaml</code>, <code>application/yaml</code>)</li>
<li><strong>Video</strong> - Video content and streaming (<code>video/*</code>, <code>application/ogg</code>, <code>*mpegurl</code>)</li>
<li><strong>Audio</strong> - Audio content (<code>audio/*</code>)</li>
<li><strong>Markdown</strong> - Markdown documents (<code>text/markdown</code>)</li>
<li><strong>Documents</strong> - PDFs, Office documents, ePub, CSV (<code>application/pdf</code>, <code>application/msword</code>, <code>text/csv</code>)</li>
<li><strong>Binary</strong> - Executables, archives, WebAssembly (<code>application/octet-stream</code>, <code>application/zip</code>, <code>application/wasm</code>)</li>
<li><strong>Serialization</strong> - Binary API formats (<code>application/protobuf</code>, <code>application/grpc</code>, <code>application/msgpack</code>)</li>
<li><strong>Other</strong> - All other content types</li>
</ul>
<p>Additionally, individual <a href="https://radar.cloudflare.com/bots/directory/gptbot">bot information pages</a> now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.</p>
<p><img src="/assets/upstream/images/radar/ai-bots-content-type.png" alt="Screenshot of the Content Type Distribution chart on the AI Insights page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/ai-insights#content-type">AI Insights page</a> to explore the data.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-12">Feb 12, 2026</time><div>
<h2 id="post-2026-02-12-brand-protection-logo-matching-percentage-selector"><a href="/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/">Enhanced Logo Matching for Brand Protection</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We have significantly upgraded our Logo Matching capabilities within Brand Protection. While previously limited to approximately 100% matches, users can now detect a wider range of brand assets through a redesigned matching model and UI.</p>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-what-s-new">What's new</h4>
<ul>
<li><strong>Configurable match thresholds</strong>: Users can set a minimum match score (starting at 75%) when creating a logo query to capture subtle variations or high-quality impersonations.</li>
<li><strong>Visual match scores</strong>: Allow users to see the exact percentage of the match directly in the results table, highlighted with color-coded lozenges to indicate severity.</li>
<li><strong>Direct logo previews</strong>: Available in the Cloudflare dashboard — similar to string matches — to verify infringements at a glance.</li>
</ul>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-key-benefits">Key benefits</h4>
<ul>
<li><strong>Expose sophisticated impersonators</strong> who use slightly altered logos to bypass basic detection filters.</li>
<li><strong>Faster triage</strong> of the most relevant threats immediately using visual indicators, reducing the time spent manually reviewing matches.</li>
</ul>
<p>Ready to protect your visual identity? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/24/">Previous</a><span>Page 25 of 50</span><a class="pagination-next" rel="next" href="/changelog/26/">Next</a></nav>
</div>
