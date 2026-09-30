---
cp9:
  canonical: https://developers.cloudflare.com/changelog/18/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 18 | Cloudflare Docs
  head_html: <title>Changelog - page 18 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/18/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 18"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/18/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/18/#page","headline":"Changelog - page 18 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/18/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/18/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-04-22">Apr 22, 2026</time><div>
<h2 id="post-2026-04-22-snapshot-expiration-cleans-data-files"><a href="/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/">R2 Data Catalog snapshot expiration now removes unreferenced data files</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.</p>
<p>Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran <code>remove_orphan_files</code> or <code>expire_snapshots</code> through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.</p>
<p>Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>For more information, refer to the <a href="/r2-data-catalog/table-maintenance/">table maintenance documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-unified-routing-geoip-country-rules"><a href="/changelog/post/2026-04-21-unified-routing-geoip-country-rules/">Country rules supported in Unified Routing</a></h2>
<div class="changelog-badges"><span>cloudflare-network-firewall</span><span>magic-transit</span><span>cloudflare-wan</span></div><div class="changelog-body"><p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Country rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.</p>
<p>This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-network-overview-page"><a href="/changelog/post/2026-04-21-network-overview-page/">Network Overview page in the dashboard</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>A new <strong>Network Overview</strong> page in the Cloudflare dashboard gives you a single starting point for network security and connectivity products.</p>
<p>From the Network Overview page, you can:</p>
<ul>
<li><strong>Connect resources with <a href="/tunnel/">Cloudflare Tunnel</a></strong> - Create tunnels to connect your infrastructure to Cloudflare without exposing it to the public Internet.</li>
<li><strong>Monitor traffic with Network Flow</strong> - Get real-time visibility into traffic volume from your routers.</li>
<li><strong>Configure Address Maps</strong> - Map dedicated static IPs or BYOIP prefixes to specific hostnames.</li>
<li><strong>Explore Magic Transit and Cloudflare WAN</strong> - Set up DDoS protection for your networks and connectivity for your branch offices and data centers.</li>
</ul>
<p>To find it, go to <a href="https://dash.cloudflare.com/?to=/:account/magic-networks/overview"><strong>Networking</strong></a> in the dashboard sidebar.</p>
<p>If you already use <a href="/magic-transit/">Magic Transit</a>, <a href="/cloudflare-wan/">Cloudflare WAN</a>, or other Cloudflare network services products, your existing experience is unchanged.</p>
<p><img src="/assets/upstream/images/fundamentals/network-overview.png" alt="Network Overview page in the Cloudflare dashboard" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-step-context-and-readable-streams"><a href="/changelog/post/2026-04-21-step-context-and-readable-streams/">Additional step context and ReadableStream support now available in Workflows step.do()</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> now provides additional context inside <code>step.do()</code> callbacks and supports returning <code>ReadableStream</code> to handle larger step outputs.</p>
<h4 id="2026-04-21-step-context-and-readable-streams-step-context-properties">Step context properties</h4>
<p>The <code>step.do()</code> callback receives a context object with new properties <a href="/changelog/post/2026-03-06-step-context-available/">alongside</a> <code>attempt</code>:</p>
<ul>
<li><strong><code>step.name</code></strong> — The name passed to <code>step.do()</code></li>
<li><strong><code>step.count</code></strong> — How many times a step with that name has been invoked in this instance (1-indexed)
<ul>
<li>Useful when running the same step in a loop.</li>
</ul>
</li>
<li><strong><code>config</code></strong> — The resolved step configuration, including <code>timeout</code> and <code>retries</code> with defaults applied</li>
</ul>
<pre tabindex="0"><code class="language-ts">type ResolvedStepConfig = {&#10;	retries: {&#10;		limit: number;&#10;		delay: WorkflowDelayDuration | number;&#10;		backoff?: &quot;constant&quot; | &quot;linear&quot; | &quot;exponential&quot;;&#10;	};&#10;	timeout: WorkflowTimeoutDuration | number;&#10;};&#10;&#10;type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: ResolvedStepConfig;&#10;};&#10;</code></pre>
<h4 id="2026-04-21-step-context-and-readable-streams-readablestream-support-in-step-do">ReadableStream support in <code>step.do()</code></h4>
<p>Steps can now return a <code>ReadableStream</code> directly. Although non-stream step outputs are <a href="/workflows/reference/limits/">limited to 1 MiB</a>, streamed outputs support much larger payloads.</p>
<pre tabindex="0"><code class="language-ts">const largePayload = await step.do(&quot;fetch-large-file&quot;, async () =&gt; {&#10;	const object = await env.MY_BUCKET.get(&quot;large-file.bin&quot;);&#10;	return object.body;&#10;});&#10;</code></pre>
<p>Note that streamed outputs are still considered part of the Workflow instance storage limit.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-correlated-worker-durable-object-logs"><a href="/changelog/post/2026-04-21-correlated-worker-durable-object-logs/">Container logs page now includes relevant Worker and Durable Object logs</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>The Container logs page now displays related <a href="/workers/">Worker</a> and <a href="/durable-objects/">Durable Object</a> logs alongside container logs. This co-locates all relevant log events for a container application in one place, making it easier to trace requests and debug issues.</p>
<p><img src="/assets/upstream/images/containers/container-worker-logs.png" alt="Container logs page showing Worker and Durable Object logs alongside container logs" /></p>
<p>You can filter to a single source when you need to isolate Container, Worker, or Durable Object output.</p>
<p>For information on configuring container logging, refer to <a href="/containers/faq/#how-do-container-logs-work">How do Container logs work?</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-13-billable-usage-dashboard-and-budget-alerts"><a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Introducing Billable Usage dashboard and Budget alerts</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>workers</span></div><div class="changelog-body"><p>Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.</p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-billable-usage-dashboard">Billable Usage dashboard</h4>
<p>The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.</p>
<p>The dashboard displays:</p>
<ul>
<li>A bar chart showing daily usage charges for your billing period</li>
<li>A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs</li>
<li>Ability to view previous billing periods</li>
</ul>
<p>Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.</p>
<p>To access the dashboard, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-billable-usage-dashboard.png" alt="Screenshot of the Billable Usage dashboard in the Cloudflare dashboard" /></p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-budget-alerts">Budget alerts</h4>
<p>Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.</p>
<p>To configure a budget alert:</p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</li>
<li>Select <strong>Set Budget Alert</strong>.</li>
<li>Enter a budget threshold amount greater than $0.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>Alternatively, configure alerts via <strong>Notifications</strong> &gt; <strong>Add</strong> &gt; <strong>Budget Alert</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-budget-alert-modal.png" alt="Create Budget Alert modal in the Cloudflare dashboard" /></p>
<p>You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.</p>
<p>Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.</p>
<p>For more information, refer to the <a href="/billing/understand/usage-based-billing/">Usage based billing documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-logpush-subrequests-merging"><a href="/changelog/post/2026-04-21-logpush-subrequests-merging/">Logpush subrequest merging for HTTP requests</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.</p>
<h4 id="2026-04-21-logpush-subrequests-merging-what-s-new">What's new</h4>
- New subrequest_merging field on Logpush jobs — Set "merge_subrequests": true when creating or updating an http_requests Logpush job to enable the feature.
- New Subrequests log field — When subrequest merging is enabled, a Subrequests field (`array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http_requests fields for that subrequest.
<h4 id="2026-04-21-logpush-subrequests-merging-limitations">Limitations</h4>
- Applies to the http_requests (zone-scoped) dataset only.
- A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
- Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
- Subrequests that do not qualify appear as separate log entries — no data is lost.
- Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
- For more information, refer to [Subrequests](/logs/logpush/logpush-job/subrequests/).
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-waf-release"><a href="/changelog/post/2026-04-21-waf-release/">WAF Release - 2026-04-21</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces a new detection for a Remote Code Execution (RCE) vulnerability in Apache ActiveMQ (CVE-2026-34197) and an updated signature for Magento 2 - Unrestricted File Upload. Alongside these detections, we are continuing our work on rule refinements to provide deeper security insights for our customers.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Apache ActiveMQ (CVE-2026-34197): A vulnerability in Apache ActiveMQ allows an unauthenticated, remote attacker to execute arbitrary code. This flaw occurs during the processing of specially crafted network packets, leading to potential full system compromise.</p>
</li>
<li>
<p>Magento 2 - Unrestricted File Upload - 2: This is a follow-up enhancement to our existing protections for Magento and Adobe Commerce.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain full administrative control over affected servers. We strongly recommend applying official vendor patches for Apache ActiveMQ and Magento to address the underlying vulnerabilities.</p>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
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
				<code class="nb-rule-id" title="ff8df24181aa4573a81be531ee159e2e">ee159e2e</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 8 - uri</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. Previous description was "Command Injection - Generic 8 - uri - Beta"</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9429b63c137247faadeb8a29a15308cf">a15308cf</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 8 - body - Beta</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 8 - body" (ID:{" "}
				<code class="nb-rule-id" title="5b3ce84c099040c6a25cee2d413592e2">413592e2</code>). The rule previously known as "Command Injection - Generic 8" is now renamed to "Command Injection - Generic 8 - body".
</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="85aaf5db9e0c4237b87e837e958047ed">958047ed</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"MySQL - SQLi - Executable Comment - Body" (ID:{" "}
				<code class="nb-rule-id" title="8629bb58defe4193ab4d493c7bd2d8fa">7bd2d8fa</code>) The rule previously known as "MySQL - SQLi - Executable Comment" is now renamed to "MySQL - SQLi - Executable Comment - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d19cd574c4644952881a6f3a582cc559">582cc559</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="407f9ec8a17348dfba3b9450a16639d3">a16639d3</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d07e6dbf15664b99b37b0d2544f24211">44f24211</code>
</td>
<td>N/A</td>
<td>Magento 2 - Unrestricted file upload - 2</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>     
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="26ef21cb197b44fc8a98b7cebf170a17">bf170a17</code>
</td>
<td>N/A</td>
<td>Apache ActiveMQ - Remote Code Execution - CVE:CVE-2026-34197</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7f7bc3d28a8e43bf97bd15d68c2ac1a7">8c2ac1a7</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Sleep Function" (ID:{" "}
				<code class="nb-rule-id" title="2c333735f7b24566b17cb64ef77e8d54">f77e8d54</code>)
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3872e5638bdf4bf0943a80394dacaeb8">4dacaeb8</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>   
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bebce8fadfa94ccab09eb74fed4c9ece">ed4c9ece</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7a40eed5a8654a50a2598a821dfa64df">1dfa64df</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - uri</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="15c6b2ce033949b2a1a9f9454c62e2e7">4c62e2e7</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - header</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fc9d800b7a724181af8d5650aab28ea1">aab28ea1</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - body</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Probing" (ID: <code class="nb-rule-id" title="2c20b5e8684043f48620ff77b4026c88">b4026c88</code>)
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="945c5aa9f45141dd872d7ec920999be0">20999be0</code>
</td>
<td>N/A</td>
<td>SQLi - Probing 2 </td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule had duplicate detection logic and has been deprecated.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f1771273700342758e73cf16d7aa0008">d7aa0008</code>
</td>
<td>N/A</td>
<td>SQLi - UNION in MSSQL - Body</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule has been renamed to differentiate from "SQLi - UNION in MSSQL" (ID: <code class="nb-rule-id" title="ef7db598c7654c729d9db56fee5e35fd">ee5e35fd</code>) and contains updated rule logic.
</td>
</tr> 
<tr> 
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3ffd242b4ba242ca965022d3a67d8561">a67d8561</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 3</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule had duplicate detection logic and has been deprecated.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5e69d599ad634c81abe36a5f0af34bba">0af34bba</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag  - URI</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2635275641bf44d4bad6a2e170282f38">70282f38</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b3d033ea9f364574b0a2ec4223f4d718">23f4d718</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - IFrame Tag - Src and Srcdoc Attributes - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="76c37816ef5c4997ab2080a36978def1">6978def1</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7d6757e8a28f4853a72b4ce6ebd81645">ebd81645</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - URI</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>           
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-21">Apr 21, 2026</time><div>
<h2 id="post-2026-04-21-websocket-standard-binary-type"><a href="/changelog/post/2026-04-21-websocket-standard-binary-type/">WebSocket binary messages now delivered as Blob by default</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Binary frames received on a <code>WebSocket</code> are now delivered to the <code>message</code> event as <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob"><code>Blob</code></a> objects by default. This matches the <a href="https://websockets.spec.whatwg.org/">WebSocket specification</a> and standard browser behavior. Previously, binary frames were always delivered as <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a>. The <a href="/workers/runtime-apis/websockets/#binarytype"><code>binaryType</code></a> property on <code>WebSocket</code> controls the delivery type on a per-WebSocket basis.</p>
<p>This change has been active for Workers with compatibility dates on or after <code>2026-03-17</code>, via the <a href="/workers/configuration/compatibility-flags/#websocket-standard-binary-type"><code>websocket_standard_binary_type</code></a> compatibility flag. We should have documented this change when it shipped but didn't. We're sorry for the trouble that caused. If your Worker handles binary WebSocket messages and assumes <code>event.data</code> is an <code>ArrayBuffer</code>, the frames will arrive as <code>Blob</code> instead, and a naive <code>instanceof ArrayBuffer</code> check will silently drop every frame.</p>
<p>To opt back into <code>ArrayBuffer</code> delivery, assign <code>binaryType</code> before calling <code>accept()</code>. This works regardless of the compatibility flag:</p>
<pre tabindex="0"><code class="language-js">const resp = await fetch(&quot;https://example.com&quot;, {&#10;	headers: { Upgrade: &quot;websocket&quot; },&#10;});&#10;const ws = resp.webSocket;&#10;&#10;// Opt back into ArrayBuffer delivery for this WebSocket.&#10;ws.binaryType = &quot;arraybuffer&quot;;&#10;ws.accept();&#10;&#10;ws.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;	if (typeof event.data === &quot;string&quot;) {&#10;		// Text frame.&#10;	} else {&#10;		// event.data is an ArrayBuffer because we set binaryType above.&#10;	}&#10;});&#10;</code></pre>
<p>If you are not ready to migrate and want to keep <code>ArrayBuffer</code> as the default for all WebSockets in your Worker, add the <code>no_websocket_standard_binary_type</code> flag to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>This change has no effect on the Durable Object hibernatable WebSocket <a href="/durable-objects/best-practices/websockets/"><code>webSocketMessage</code></a> handler, which continues to receive binary data as <code>ArrayBuffer</code>.</p>
<p>For more information, refer to <a href="/workers/runtime-apis/websockets/#binary-messages">WebSockets binary messages</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-20">Apr 20, 2026</time><div>
<h2 id="post-2026-04-20-network-session-analytics"><a href="/changelog/post/2026-04-20-network-session-analytics/">Network session analytics dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>gateway</span></div><div class="changelog-body"><p>The new <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a> dashboard is now available in Cloudflare One. This dashboard provides visibility into your network traffic patterns, helping you understand how traffic flows through your Cloudflare One infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-network-session-analytics.png" alt="Cloudflare One Network Session Analytics" /></p>
<h4 id="2026-04-20-network-session-analytics-what-you-can-do-with-network-session-analytics">What you can do with Network session analytics</h4>
<ul>
<li><strong>Analyze geographic distribution</strong>: View a world map showing where your network traffic originates, with a list of top locations by session count.</li>
<li><strong>Monitor key metrics</strong>: Track session count, total bytes transferred, and unique users.</li>
<li><strong>Identify connection issues</strong>: Analyze connection close reasons to troubleshoot network problems.</li>
<li><strong>Review protocol usage</strong>: See which network protocols (TCP, UDP, ICMP) are most used.</li>
</ul>
<h4 id="2026-04-20-network-session-analytics-dashboard-features">Dashboard features</h4>
<ul>
<li><strong>Summary metrics</strong>: Session count, bytes total, and unique users</li>
<li><strong>Traffic by location</strong>: World map visualization and location list with top traffic sources</li>
<li><strong>Top protocols</strong>: Breakdown of TCP, UDP, ICMP, and ICMPv6 traffic</li>
<li><strong>Connection close reasons</strong>: Insights into why sessions terminated (client closed, origin closed, timeouts, errors)</li>
</ul>
<h4 id="2026-04-20-network-session-analytics-how-to-access">How to access</h4>
<ol>
<li>Log in to <a href="https://dash.cloudflare.com">Cloudflare One</a>.</li>
<li>Go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Dashboards</strong>.</li>
<li>Select <strong>Network session analytics</strong>.</li>
</ol>
<p>For more information, refer to the <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-20">Apr 20, 2026</time><div>
<h2 id="post-2026-04-20-pipelines-logpush-destination"><a href="/changelog/post/2026-04-20-pipelines-logpush-destination/">Cloudflare Pipelines as a Logpush destination</a></h2>
<div class="changelog-badges"><span>logs</span><span>pipelines</span></div><div class="changelog-body"><p>Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.</p>
<p>With this release, you can now send your logs directly to <a href="/pipelines/">Pipelines</a> to ingest, transform, and store your logs in <a href="/r2/">R2</a> as Parquet files or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This makes the data footprint more compact and more efficient at querying your logs instantly with <a href="/r2-sql/">R2 SQL</a> or any other query engine that supports Apache Iceberg or Parquet.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-transform-logs-before-storage">Transform logs before storage</h4>
<p>Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-20">Apr 20, 2026</time><div>
<h2 id="post-2026-04-20-r2-sql-json-functions-explain-format"><a href="/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/">R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL now supports functions for querying JSON data stored in Apache Iceberg tables, an easier way to parse query plans with <code>EXPLAIN FORMAT JSON</code>, and querying tables without partition keys stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>JSON functions extract and manipulate JSON values directly in SQL without client-side processing:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;  json_get_str(doc, &#x27;name&#x27;) AS name,&#10;  json_get_int(doc, &#x27;user&#x27;, &#x27;profile&#x27;, &#x27;level&#x27;) AS level,&#10;  json_get_bool(doc, &#x27;active&#x27;) AS is_active&#10;FROM my_namespace.sales_data&#10;WHERE json_contains(doc, &#x27;email&#x27;)&#10;</code></pre>
<p>For a full list of available functions, refer to <a href="/r2-sql/sql-reference/scalar-functions/#json-functions">JSON functions</a>.</p>
<p><code>EXPLAIN FORMAT JSON</code> returns query execution plans as structured JSON for programmatic analysis and observability integrations:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &quot;${WAREHOUSE}&quot; &quot;EXPLAIN FORMAT JSON SELECT * FROM logpush.requests LIMIT 10;&quot;&#10;&#10;┌──────────────────────────────────────┐&#10;│ plan                                 │&#10;├──────────────────────────────────────┤&#10;│ {                                    │&#10;│   &quot;name&quot;: &quot;CoalescePartitionsExec&quot;,  │&#10;│   &quot;output_partitions&quot;: 1,            │&#10;│   &quot;rows&quot;: 10,                        │&#10;│   &quot;size_approx&quot;: &quot;310B&quot;,             │&#10;│   &quot;children&quot;: [                      │&#10;│     {                                │&#10;│       &quot;name&quot;: &quot;DataSourceExec&quot;,      │&#10;│       &quot;output_partitions&quot;: 4,        │&#10;│       &quot;rows&quot;: 28951,                 │&#10;│       &quot;size_approx&quot;: &quot;900.0KB&quot;,      │&#10;│       &quot;table&quot;: &quot;logpush.requests&quot;,   │&#10;│       &quot;files&quot;: 7,                    │&#10;│       &quot;bytes&quot;: 900019,               │&#10;│       &quot;projection&quot;: [                │&#10;│         &quot;__ingest_ts&quot;,               │&#10;│         &quot;CPUTimeMs&quot;,                 │&#10;│         &quot;DispatchNamespace&quot;,         │&#10;│         &quot;Entrypoint&quot;,                │&#10;│         &quot;Event&quot;,                     │&#10;│         &quot;EventTimestampMs&quot;,          │&#10;│         &quot;EventType&quot;,                 │&#10;│         &quot;Exceptions&quot;,                │&#10;│         &quot;Logs&quot;,                      │&#10;│         &quot;Outcome&quot;,                   │&#10;│         &quot;ScriptName&quot;,                │&#10;│         &quot;ScriptTags&quot;,                │&#10;│         &quot;ScriptVersion&quot;,             │&#10;│         &quot;WallTimeMs&quot;                 │&#10;│       ],                             │&#10;│       &quot;limit&quot;: 10                    │&#10;│     }                                │&#10;│   ]                                  │&#10;│ }                                    │&#10;└──────────────────────────────────────┘&#10;</code></pre>
<p>For more details, refer to <a href="/r2-sql/sql-reference/#explain">EXPLAIN</a>.</p>
<p>Unpartitioned Iceberg tables can now be queried directly, which is useful for smaller datasets or data without natural time dimensions. For tables with more than 1000 files, partitioning is still recommended for better performance.</p>
<p>Refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a> for the latest guidance on using R2 SQL.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-20">Apr 20, 2026</time><div>
<h2 id="post-2026-04-27-archive-and-audit-security-action-items"><a href="/changelog/post/2026-04-27-archive-and-audit-security-action-items/">Archive and audit security action items</a></h2>
<div class="changelog-badges"><span>security-overview</span></div><div class="changelog-body"><h4 id="2026-04-27-archive-and-audit-security-action-items-archive-and-audit-security-action-items">Archive and audit security action items</h4>
<p>Introducing enhanced archiving capabilities for security action items within the Security Overview dashboard. This update allows security teams to maintain a cleaner workspace by removing resolved, accepted, or irrelevant items from their active list while maintaining a clear paper trail for compliance.</p>
<hr />
<h4 id="2026-04-27-archive-and-audit-security-action-items-why-this-matters">Why this matters</h4>
<p>Managing a high volume of security insights can be overwhelming. Previously, users lacked a structured way to dismiss items without losing the context of why they were ignored.</p>
<p>With these new archiving options—<strong>False Positive</strong>, <strong>Accept Risk</strong>, and <strong>Other</strong>—you can now suppress items indefinitely with required rationale text for risk-based decisions. This ensures that your team remains focused on critical, actionable vulnerabilities while preserving institutional knowledge for audits.</p>
<h4 id="2026-04-27-archive-and-audit-security-action-items-key-features">Key features</h4>
<ul>
<li><strong>Structured Archiving:</strong> Choose from specific categories to define why an action item is being moved.</li>
<li><strong>Required Rationale:</strong> For &quot;Accept Risk&quot; and &quot;Other&quot; categories, users must provide documentation, ensuring accountability for security decisions.</li>
<li><strong>Audit Log Transparency:</strong> New API endpoints allow you to programmatically retrieve the history of status changes and rationale for any insight at the account or zone level.</li>
<li><strong>Reversible Actions:</strong> Any archived item can be moved back to the active list at any time if the security context changes.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17753.md")</aside>
<hr />
<h4 id="2026-04-27-archive-and-audit-security-action-items-example-retrieve-audit-logs-via-api">Example: Retrieve audit logs via API</h4>
<p>To review the history and rationale of a specific archived issue at the account level, you can use the following API command:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){account_id}/insights/{insight_id}/audit-log&quot; \&#10;     &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-20">Apr 20, 2026</time><div>
<h2 id="post-2026-04-20-kimi-k2-6-workers-ai"><a href="/changelog/post/2026-04-20-kimi-k2-6-workers-ai/">Moonshot AI Kimi K2.6 now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.</p>
<p>Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).</p>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python</li>
<li><strong>Coding-driven design</strong> that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows</li>
<li><strong>Agent swarm orchestration</strong> scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-differences-from-kimi-k2-5">Differences from Kimi K2.5</h4>
<p>If you are migrating from Kimi K2.5, note the following API changes:</p>
<ul>
<li>K2.6 uses <code>chat_template_kwargs.thinking</code> to control reasoning, replacing <code>chat_template_kwargs.enable_thinking</code></li>
<li>K2.6 returns reasoning content in the <code>reasoning</code> field, replacing <code>reasoning_content</code></li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.6 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.6/">Kimi K2.6 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-17">Apr 17, 2026</time><div>
<h2 id="post-2026-04-17-mcp-portal-homepage-and-sign-out"><a href="/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/">Homepage and sign-out for MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> display a homepage when users visit the portal domain in a browser.</p>
<p><img src="/assets/upstream/images/changelog/access/portals-homepage-disconnected.png" alt="MCP server portal homepage showing connection status and setup instructions" /></p>
<p>The homepage shows:</p>
<ul>
<li>The portal name and organization branding</li>
<li>The MCP endpoint URL with a copy button</li>
<li>Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients</li>
</ul>
<p>Authenticated users see their email address and a <strong>Sign out</strong> button. Selecting <strong>Sign out</strong> revokes all portal-level OAuth grants, deletes upstream server OAuth states, and redirects through Cloudflare Access logout. A confirmation page shows a summary of the revoked sessions.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#portal-homepage">MCP server portals</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-17">Apr 17, 2026</time><div>
<h2 id="post-2026-04-17-redirects-for-ai-training"><a href="/changelog/post/2026-04-17-redirects-for-ai-training/">Introducing Redirects for AI Training</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via <strong>AI Crawl Control</strong> &gt; <strong>Quick Actions</strong>, AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.</p>
<p>This feature leverages your existing <code>&lt;link rel=&quot;canonical&quot;&gt;</code> tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.</p>
<p>Refer to the <a href="/ai-crawl-control/reference/redirects-for-ai-training/">Redirects for AI Training documentation</a> for details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-17">Apr 17, 2026</time><div>
<h2 id="post-2026-04-17-tools-for-agentic-internet"><a href="/changelog/post/2026-04-17-tools-for-agentic-internet/">Tools to prepare your site for the agentic Internet</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now includes new tools to help you prepare your site for the agentic Internet—a web where AI agents are first-class citizens that discover and interact with content differently than human visitors.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-content-format-insights">Content Format insights</h4>
<p>The <strong>Metrics</strong> tab now includes a <strong>Content Format</strong> chart showing what content types AI systems request versus what your origin serves. Understanding these patterns helps you optimize content delivery for both human and agent consumption.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-directives-tab-formerly-robots-txt">Directives tab (formerly Robots.txt)</h4>
<p>The <strong>Robots.txt</strong> tab has been renamed to <strong>Directives</strong> and now includes a link to check your site's <a href="https://isitagentready.com">Agent Readiness</a> score.</p>
<p>Refer to our <a href="https://blog.cloudflare.com/agent-readiness/">blog post on preparing for the agentic Internet</a> for more on why these capabilities matter.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-17">Apr 17, 2026</time><div>
<h2 id="post-2026-04-17-smart-tiered-cache-for-public-cloud"><a href="/changelog/post/2026-04-17-smart-tiered-cache-for-public-cloud/">Smart Tiered Cache optimizes public cloud origins</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache HIT rates and reduce origin load for origins hosted on public cloud providers with <a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a>. By setting a cloud region hint for your origin, Cloudflare selects the optimal upper-tier data center for that cloud region, funneling all cache MISSes through a single location close to your origin.</p>
<p>Previously, Smart Tiered Cache could not reliably select an optimal upper tier for origins behind anycast or regional unicast networks commonly used by cloud providers. Origins on AWS, GCP, Azure, and Oracle Cloud would fall back to a multi-upper-tier topology, resulting in lower cache HIT rates and more requests reaching your origin.</p>
<h4 id="2026-04-17-smart-tiered-cache-for-public-cloud-how-it-works">How it works</h4>
<p>Set a cloud region hint (for example, <code>aws/us-east-1</code> or <code>gcp/europe-west1</code>) for your origin IP or hostname. Smart Tiered Cache uses this hint along with real-time latency data to select a primary upper tier close to your cloud region, plus a fallback in a different location for resilience.</p>
<ul>
<li><strong>Supported providers</strong>: AWS, GCP, Azure, and Oracle Cloud.</li>
<li><strong>All plans</strong>: Available on Free, Pro, Business, and Enterprise plans at no additional cost.</li>
<li><strong>Dashboard and API</strong>: Configure from <strong>Caching</strong> &gt; <strong>Tiered Cache</strong> &gt; <strong>Origin Configuration</strong>, or use the API and Terraform.</li>
</ul>
<h4 id="2026-04-17-smart-tiered-cache-for-public-cloud-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> and set a cloud region hint for your origin in the <a href="/cache/how-to/tiered-cache/#public-cloud-origins">Tiered Cache settings</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-17">Apr 17, 2026</time><div>
<h2 id="post-2026-04-17-radar-ai-insights-updates"><a href="/changelog/post/2026-04-17-radar-ai-insights-updates/">AI Insights updates on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> adds three new features to the <a href="https://radar.cloudflare.com/ai-insights">AI Insights</a> page, expanding visibility into how AI bots, crawlers, and agents interact with the web.</p>
<h4 id="2026-04-17-radar-ai-insights-updates-adoption-of-ai-agent-standards">Adoption of AI agent standards</h4>
<p>The AI Insights page now includes an <a href="https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards">adoption of AI agent standards</a> widget that tracks how websites adopt agent-facing standards. The data is filterable by domain category and updated weekly on Mondays.
This data is also available through the <a href="/api/resources/radar/subresources/agent_readiness/methods/summary/">Agent Readiness API reference</a>.</p>
<p><img src="/assets/upstream/images/radar/agent-readiness-adoption-chart.png" alt="Screenshot of the adoption of AI agent standards chart" /></p>
<p><a href="https://radar.cloudflare.com/scan">URL Scanner</a> reports now include an <strong>Agent readiness</strong> tab that evaluates a scanned URL against the criteria used by the <a href="https://isitagentready.com/">Agent Readiness score tool</a>.</p>
<p><img src="/assets/upstream/images/radar/agent-readiness-url-scanner.png" alt="Screenshot of the URL Scanner agent readiness tab" /></p>
<p>For more details, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">Agent Readiness blog post</a>.</p>
<h4 id="2026-04-17-radar-ai-insights-updates-markdown-for-agents-savings">Markdown for Agents savings</h4>
<p>A new <a href="https://radar.cloudflare.com/ai-insights#markdown-for-agents-savings">savings gauge</a> shows the median response-size reduction when serving Markdown instead of HTML to AI bots and crawlers. This highlights the bandwidth and token savings that <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> provides.</p>
<div style="max-width: 300px;">
<p><img src="/assets/upstream/images/radar/markdown-for-agents-savings.png" alt="Screenshot of the Markdown for Agents savings gauge" /></p>
</div>
<p>For more details, refer to the <a href="/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary">Markdown for Agents API reference</a>.</p>
<h4 id="2026-04-17-radar-ai-insights-updates-response-status">Response status</h4>
<p>The new <a href="https://radar.cloudflare.com/ai-insights#response-status">response status widget</a> displays the distribution of HTTP response status codes returned to AI bots and crawlers. Results are groupable by individual status code (200, 403, 404) or by category (2xx, 3xx, 4xx, 5xx).</p>
<p>The same widget is available on each verified bot's detail page (only available for AI bots), for example <a href="https://radar.cloudflare.com/bots/directory/google#response-status">Google</a>.</p>
<p><img src="/assets/upstream/images/radar/ai-response-status.png" alt="Screenshot of the response status distribution widget" /></p>
<p>Explore all three features on the <a href="https://radar.cloudflare.com/ai-insights">Cloudflare Radar AI Insights</a> page.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-16">Apr 16, 2026</time><div>
<h2 id="post-2026-04-16-ai-search-namespace-binding"><a href="/changelog/post/2026-04-16-ai-search-namespace-binding/">AI Search instances now include built-in storage and namespace Workers Bindings</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>New <a href="/ai-search/">AI Search</a> instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.</p>
<p>Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-built-in-storage-and-vector-index">Built-in storage and vector index</h4>
<p>All new instances now comes with built-in storage which allows you to upload files directly to it using the <a href="/ai-search/api/items/workers-binding/">Items API</a> or the dashboard. No R2 buckets to set up, no external data sources to connect first.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;// upload and wait for indexing to complete&#10;const item = await instance.items.uploadAndPoll(&quot;faq.md&quot;, content);&#10;&#10;// search immediately after indexing&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;onboarding guide&quot; }],&#10;});&#10;</code></pre>
<h4 id="2026-04-16-ai-search-namespace-binding-namespace-binding">Namespace binding</h4>
<p>The new <code>ai_search_namespaces</code> binding replaces the previous <code>env.AI.autorag()</code> API provided through the <code>AI</code> binding. It gives your Worker access to all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a> and lets you create, update, and delete instances at runtime without redeploying.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search_namespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;AI_SEARCH&quot;,&#10;			&quot;namespace&quot;: &quot;default&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">// create an instance at runtime&#10;const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;});&#10;</code></pre>
<p>For migration details, refer to <a href="/ai-search/api/migration/workers-binding/">Workers binding migration</a>. For more on namespaces, refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-cross-instance-search">Cross-instance search</h4>
<p>Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/api/search/workers-binding/#namespace-level">Namespace-level search</a> for details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-16">Apr 16, 2026</time><div>
<h2 id="post-2026-04-16-hybrid-search-and-relevance-boosting"><a href="/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/">AI Search now has hybrid search and relevance boosting</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-hybrid-search">Hybrid search</h4>
<p>Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.</p>
<p>You can configure the tokenizer (<code>porter</code> for natural language, <code>trigram</code> for code), keyword match mode (<code>and</code> for precision, <code>or</code> for recall), and fusion method (<code>rrf</code> or <code>max</code>) per instance:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: { vector: true, keyword: true },&#10;	fusion_method: &quot;rrf&quot;,&#10;	indexing_options: { keyword_tokenizer: &quot;porter&quot; },&#10;	retrieval_options: { keyword_match_mode: &quot;and&quot; },&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/concepts/search-modes/">Search modes</a> for an overview and <a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a> for configuration details.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-relevance-boosting">Relevance boosting</h4>
<p>Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on <code>timestamp</code>, or surface high-priority content by boosting on a custom metadata field like <code>priority</code>.</p>
<p>Configure up to 3 boost fields per instance or override them per request:</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.get(&quot;my-instance&quot;).search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;deployment guide&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [&#10;				{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; },&#10;				{ field: &quot;priority&quot;, direction: &quot;desc&quot; },&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a> for configuration details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-16">Apr 16, 2026</time><div>
<h2 id="post-2026-04-16-artifacts-now-in-beta"><a href="/changelog/post/2026-04-16-artifacts-now-in-beta/">Artifacts now in beta: versioned filesystem with Git access</a></h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p><a href="/artifacts/">Artifacts</a> is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.</p>
<p>You can <a href="https://blog.cloudflare.com/artifacts-git-for-agents-beta/">read the announcement blog</a> to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.</p>
<p>Artifacts has three API surfaces:</p>
<ul>
<li>Workers bindings (for creating and managing repositories)</li>
<li>REST API (for creating and managing repos from any other compute platform)</li>
<li>Git protocol (for interacting with repos)</li>
</ul>
<p>As an example: you can use the Workers binding to create a repo and read back its remote URL:</p>
<pre tabindex="0"><code class="language-ts">&#35; Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.&#10;const created = await env.PROD_ARTIFACTS.create(&quot;agent-007&quot;);&#10;const remote = (await created.repo.info())?.remote;&#10;</code></pre>
<p>Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos&quot; --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; --header &quot;Content-Type: application/json&quot; --data &#x27;{&quot;name&quot;:&quot;agent-007&quot;}&#x27;&#10;</code></pre>
<p>Any Git client that speaks smart HTTP can use the returned remote URL:</p>
<pre tabindex="0"><code class="language-bash">&#35; Agents know git.&#10;&#35; Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.&#10;git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git&#10;</code></pre>
<p>To learn more, refer to <a href="/artifacts/get-started/">Get started</a>, <a href="/artifacts/api/workers-binding/">Workers binding</a>, and <a href="/artifacts/api/git-protocol/">Git protocol</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-16">Apr 16, 2026</time><div>
<h2 id="post-2026-04-16-email-sending-public-beta"><a href="/changelog/post/2026-04-16-email-sending-public-beta/">Email Sending now in public beta</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p><strong><a href="/email-service/api/send-emails/">Email Sending</a></strong> is now in public beta. Send transactional emails directly from Workers (<code>env.EMAIL.send()</code>) or the REST API, with support for HTML, plain text, attachments, inline images, and custom headers. Email Sending joins <a href="https://blog.cloudflare.com/introducing-email-routing/">Email Routing</a> under the new <strong>Cloudflare Email Service</strong> — a single service for sending and receiving email on the Cloudflare developer platform.</p>
<p>Send an email from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17722.md")</div>
<p>Email Service also integrates with the <a href="/agents/">Agents SDK</a>, giving your agents a native <code>onEmail</code> hook to receive, process, and reply to emails. Combined with the new <a href="https://github.com/cloudflare/mcp-server-cloudflare">Email MCP server</a> and Wrangler CLI email commands, any agent can send email regardless of where it runs.</p>
<p>Start sending and receiving emails from Workers and agents today. Email Sending is available on the Workers paid plan. Refer to the <a href="/email-service/">Email Service documentation</a> to get started.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-br-rename"><a href="/changelog/post/2026-04-15-br-rename/">Browser Rendering is now Browser Run</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We are renaming Browser Rendering to <strong><a href="/browser-run/">Browser Run</a></strong>. The name Browser Rendering never fully captured what the product does. Browser Run lets you run full browser sessions on Cloudflare's global network, drive them with code or AI, record and replay sessions, crawl pages for content, debug in real time, and let humans intervene when your agent needs help.</p>
<p>Along with the rename, we have increased limits for Workers Paid plans and redesigned the Browser Run dashboard.</p>
<p>We have 4x-ed concurrency limits for Workers Paid plan users:</p>
<ul>
<li><strong>Concurrent browsers per account</strong>: 30 → <strong>120 per account</strong></li>
<li><strong>New browser instances</strong>: 30 per minute → <strong>1 per second</strong></li>
<li><strong>REST API rate limits</strong>: recently increased from <a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">3 to 10 requests per second</a></li>
</ul>
<p>Rate limits across the <a href="/browser-run/limits/">limits page</a> are now expressed in per-second terms, matching how they are enforced. No action is needed to benefit from the higher limits.</p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">redesigned dashboard</a> now shows every request in a single Runs tab, not just browser sessions but also quick actions like screenshots, PDFs, markdown, and crawls. Filter by endpoint, view target URLs, status, and duration, and expand any row for more detail.</p>
<p><img src="/images/browser-run/BRdashboardredesign.png" alt="Browser Run dashboard Runs tab with browser sessions and quick actions visible in one list, and an expanded crawl job showing its progress" /></p>
<p>We are also shipping several new features:</p>
<ul>
<li><strong><a href="/changelog/post/2026-04-15-br-observability/">Live View, Human in the Loop, and Session Recordings</a></strong> - See what your agent is doing in real time, let humans step in when automation hits a wall, and replay any session after it ends.</li>
<li><strong><a href="/changelog/post/2026-04-15-br-webmcp/">WebMCP</a></strong> - Websites can expose structured tools for AI agents to discover and call directly, replacing slow screenshot-analyze-click loops.</li>
</ul>
<p>For the full story, read our Agents Week blog <a href="https://blog.cloudflare.com/browser-run-for-ai-agents">Browser Run: Give your agents a browser</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-15">Apr 15, 2026</time><div>
<h2 id="post-2026-04-15-br-observability"><a href="/changelog/post/2026-04-15-br-observability/">Browser Run adds Live View, Human in the Loop, and Session Recordings</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>When browser automation fails or behaves unexpectedly, it can be hard to understand what happened. We are shipping three new features in <a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) to help:</p>
<ul>
<li><strong><a href="/browser-run/features/live-view/">Live View</a></strong> for real-time visibility</li>
<li><strong><a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a></strong> for human intervention</li>
<li><strong><a href="/browser-run/features/session-recording/">Session Recordings</a></strong> for replaying sessions after they end</li>
</ul>
<h4 id="2026-04-15-br-observability-live-view">Live View</h4>
<p><a href="/browser-run/features/live-view/">Live View</a> lets you see what your agent is doing in real time. The page, DOM, console, and network requests are all visible for any active browser session. Access Live View from the Cloudflare dashboard, via the hosted UI at <code>live.browser.run</code>, or using native Chrome DevTools.</p>
<h4 id="2026-04-15-br-observability-human-in-the-loop">Human in the Loop</h4>
<p>When your agent hits a snag like a login page or unexpected edge case, it can hand off to a human instead of failing. With <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, a human steps into the live browser session through Live View, resolves the issue, and hands control back to the script.</p>
<p>Today, you can step in by opening the Live View URL for any active session. Next, we are adding a handoff flow where the agent can signal that it needs help, notify a human to step in, then hand control back to the agent once the issue is resolved.</p>
<p><img src="/images/browser-run/liveview.gif" alt="Browser Run Human in the Loop demo where an AI agent searches Amazon, selects a product, and requests human help when authentication is needed to buy" /></p>
<h4 id="2026-04-15-br-observability-session-recordings">Session Recordings</h4>
<p><a href="/browser-run/features/session-recording/">Session Recordings</a> records DOM state so you can replay any session after it ends. Enable recordings by passing <code>recording: true</code> when launching a browser. After the session closes, view the recording in the Cloudflare dashboard under <strong>Browser Run</strong> &gt; <strong>Runs</strong>, or retrieve via API using the session ID. Next, we are adding the ability to inspect DOM state and console output at any point during the recording.</p>
<p><img src="/images/browser-run/sessionrecording.gif" alt="Browser Run session recording showing an automated browser navigating the Sentry Shop and adding a bomber jacket to the cart" /></p>
<p>To get started, refer to the documentation for <a href="/browser-run/features/live-view/">Live View</a>, <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, and <a href="/browser-run/features/session-recording/">Session Recording</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/17/">Previous</a><span>Page 18 of 50</span><a class="pagination-next" rel="next" href="/changelog/19/">Next</a></nav>
</div>
