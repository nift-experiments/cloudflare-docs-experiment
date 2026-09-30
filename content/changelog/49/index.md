---
cp9:
  canonical: https://developers.cloudflare.com/changelog/49/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 49 | Cloudflare Docs
  head_html: <title>Changelog - page 49 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/49/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 49"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/49/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/49/#page","headline":"Changelog - page 49 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/49/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/49/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-01-07">Jan 7, 2025</time><div>
<h2 id="post-2025-01-07-d1-faster-query"><a href="/changelog/post/2025-01-07-d1-faster-query/">40-60% Faster D1 Worker API Requests</a></h2>
<div class="changelog-badges"><span>d1</span></div><div class="changelog-body"><p>Users making <a href="/d1/">D1</a> requests via the <a href="/d1/worker-api/">Workers API</a> can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.</p>
<p><img src="/images/d1/faster-d1-worker-api.png" alt="D1 Worker API latency" /></p>
<p><em>p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement.</em></p>
<p>This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 <a href="/d1/configuration/data-location/#provide-a-location-hint">location hints</a> can be used to influence the geographic location of a database.</p>
<p>For more details on how D1 removed redundant round trips, see the D1 specific release note <a href="/d1/platform/release-notes/#2025-01-07">entry</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-06">Jan 6, 2025</time><div>
<h2 id="post-2025-01-06-waf-release"><a href="/changelog/post/2025-01-06-waf-release/">WAF Release - 2025-01-06</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="3a321b10270b42549ac201009da08beb">9da08beb</code>
</td>
<td>100678</td>
<td>Pandora FMS - Remote Code Execution - CVE:CVE-2024-11320</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="1fe510368b4a47dda90363c2ecdf3d02">ecdf3d02</code>
</td>
<td>100679</td>
<td>
				Palo Alto Networks - Remote Code Execution - CVE:CVE-2024-0012,
				CVE:CVE-2024-9474
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="b7ba636927b44ee288b9a697a40f2a35">a40f2a35</code>
</td>
<td>100680</td>
<td>Ivanti - Command Injection - CVE:CVE-2024-37397</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="6bd9b07c8acc4beeb17c8bee58ae3c89">58ae3c89</code>
</td>
<td>100681</td>
<td>Really Simple Security - Auth Bypass - CVE:CVE-2024-10924</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="c86e79e15a4a4307870f6f77e37f2da6">e37f2da6</code>
</td>
<td>100682</td>
<td>Magento - XXE - CVE:CVE-2024-34102</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="945f41b48be9485f953116015054c752">5054c752</code>
</td>
<td>100683</td>
<td>CyberPanel - Remote Code Execution - CVE:CVE-2024-51567</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="aec9a2e554a34a8fa547d069dfe93d7b">dfe93d7b</code>
</td>
<td>100684</td>
<td>
				Microsoft SharePoint - Remote Code Execution - CVE:CVE-2024-38094,
				CVE:CVE-2024-38024, CVE:CVE-2024-38023
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="e614dd46c1ce404da1909e841454c856">1454c856</code>
</td>
<td>100685</td>
<td>CyberPanel - Remote Code Execution - CVE:CVE-2024-51568</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="685a4edf68f740b4a2c80d45e92362e5">e92362e5</code>
</td>
<td>100686</td>
<td>Seeyon - Remote Code Execution</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="204f9d948a124829acb86555b9f1c9f8">b9f1c9f8</code>
</td>
<td>100687</td>
<td>
				WordPress - Remote Code Execution - CVE:CVE-2024-10781,
				CVE:CVE-2024-10542
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="19587024724e49329d5b482d0d7ca374">0d7ca374</code>
</td>
<td>100688</td>
<td>ProjectSend - Remote Code Execution - CVE:CVE-2024-11680</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="fa49213e55484f6c824e0682a5260b70">a5260b70</code>
</td>
<td>100689</td>
<td>
				Palo Alto GlobalProtect - Remote Code Execution - CVE:CVE-2024-5921
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="11b5fc23e85b41ca90316bddd007118b">d007118b</code>
</td>
<td>100690</td>
<td>Ivanti - Remote Code Execution - CVE:CVE-2024-37404</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="aaeada52bcc840598515de6cc3e49f64">c3e49f64</code>
</td>
<td>100691</td>
<td>Array Networks - Remote Code Execution - CVE:CVE-2023-28461</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="e2c7ce1ecd6847219f8d9aedfcc6f5bb">fcc6f5bb</code>
</td>
<td>100692</td>
<td>CyberPanel - Remote Code Execution - CVE:CVE-2024-51378</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="84d481b1f49c4735afa2fb2bb615335e">b615335e</code>
</td>
<td>100693</td>
<td>Symfony Profiler - Auth Bypass - CVE:CVE-2024-50340</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="9f258f463f9f4b26ad07e3c209d08c8a">09d08c8a</code>
</td>
<td>100694</td>
<td>Citrix Virtual Apps - Remote Code Execution - CVE:CVE-2024-8069</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="b490d6edcfec4028aef45cf08aafb2f5">8aafb2f5</code>
</td>
<td>100695</td>
<td>MSMQ Service - Remote Code Execution - CVE:CVE-2023-21554</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="c8f65bc9eeef4665820ecfe411b7a8c7">11b7a8c7</code>
</td>
<td>100696</td>
<td>Nginxui - Remote Code Execution - CVE:CVE-2024-49368</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="d5f2e133e34640198d06d7b345954c7e">45954c7e</code>
</td>
<td>100697</td>
<td>
				Apache ShardingSphere - Remote Code Execution - CVE:CVE-2022-22733
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="c34432e257074cffa9fa15f3f5311209">f5311209</code>
</td>
<td>100698</td>
<td>Mitel MiCollab - Auth Bypass - CVE:CVE-2024-41713</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="3bda15acd73a4b55a5f60cd2b3e5e46e">b3e5e46e</code>
</td>
<td>100699</td>
<td>Apache Solr - Auth Bypass - CVE:CVE-2024-45216</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-02">Jan 2, 2025</time><div>
<h2 id="post-2025-01-07-aig-provider-deepseek"><a href="/changelog/post/2025-01-07-aig-provider-deepseek/">AI Gateway adds DeepSeek as a Provider</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p><a href="/ai-gateway/"><strong>AI Gateway</strong></a> now supports <a href="/ai-gateway/usage/providers/deepseek/"><strong>DeepSeek</strong></a>, including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or <a href="/workers-ai/">Workers AI</a>, AI Gateway empowers you to:</p>
<ul>
<li><strong>Monitor</strong>: Gain actionable insights with analytics and logs.</li>
<li><strong>Control</strong>: Implement caching, rate limiting, and fallbacks.</li>
<li><strong>Optimize</strong>: Improve performance with feedback and evaluations.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/deepseek.png" alt="AI Gateway adds DeepSeek as a provider" /></p>
<p>To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>For detailed setup instructions, see our <a href="/ai-gateway/usage/providers/deepseek/">DeepSeek provider documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-29">Dec 29, 2024</time><div>
<h2 id="post-2024-12-29-faster-builds"><a href="/changelog/post/2024-12-29-faster-builds/">Faster Workers Builds with Build Caching and Watch Paths</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-caching.png" alt="Build caching settings" />
<img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-watch-paths.png" alt="Build watch path settings" /></p>
<p><a href="/workers/ci-cd/builds/"><strong>Workers Builds</strong></a>, the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.</p>
<ul>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-caching/">Build Caching</a></strong>: Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.</p>
</li>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-watch-paths/">Build Watch Paths</a></strong>: Define paths to include or exclude from the build process, ideal for <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepos</a> to target only the files that need to be rebuilt per Workers project.</p>
</li>
</ul>
<p>To get started, select your Worker on the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> then go to <strong>Settings</strong> &gt; <strong>Builds</strong>, and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-20">Dec 20, 2024</time><div>
<h2 id="post-2024-12-19-escalate-user-submissions"><a href="/changelog/post/2024-12-19-escalate-user-submissions/">Escalate user submissions</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>After you triage your users' submissions (that are machine reviewed), you can now escalate them to our team for reclassification (which are instead human reviewed). User submissions from the submission alias, PhishNet, and our API can all be escalated.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Escalate.png" alt="Escalate" /></p>
<p>From <strong>Reclassifications</strong>, go to <strong>User submissions</strong>. Select the three dots next to any of the user submissions, then select <strong>Escalate</strong> to create a team request for reclassification. The Cloudflare dashboard will then show you the submissions on the <strong>Team Submissions</strong> tab.</p>
<p>Refer to <a href="/cloudflare-one/email-security/submissions/user-submissions/">User submissions</a> to learn more about this feature.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-19">Dec 19, 2024</time><div>
<h2 id="post-2024-12-19-reclassification-tab"><a href="/changelog/post/2024-12-19-reclassification-tab/">Increased transparency for phishing email submissions</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You now have more transparency about team and user submissions for phishing emails through a <strong>Reclassification</strong> tab in the Zero Trust dashboard.</p>
<p>Reclassifications happen when users or admins <a href="/cloudflare-one/email-security/settings/phish-submissions/">submit a phish</a> to Email security. Cloudflare reviews and - in some cases - reclassifies these emails based on improvements to our machine learning models.</p>
<p>This new tab increases your visibility into this process, allowing you to view what submissions you have made and what the outcomes of those submissions are.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassifications-tab.png" alt="Use the Reclassification area to review submitted phishing emails" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-19">Dec 19, 2024</time><div>
<h2 id="post-2024-12-19-diagnostic-logs"><a href="/changelog/post/2024-12-19-diagnostic-logs/">Troubleshoot tunnels with diagnostic logs</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-17">Dec 17, 2024</time><div>
<h2 id="post-2024-12-17-bgp-support-cni"><a href="/changelog/post/2024-12-17-bgp-support-cni/">Establish BGP peering over Direct CNI circuits</a></h2>
<div class="changelog-badges"><span>magic-transit</span><span>cloudflare-wan</span><span>network-interconnect</span></div><div class="changelog-body"><p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Magic WAN BGP peering</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Magic Transit BGP peering</a> to learn more about this feature and how to set it up.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-11">Dec 11, 2024</time><div>
<h2 id="post-2024-12-11-hyperdrive-caching-at-edge"><a href="/changelog/post/2024-12-11-hyperdrive-caching-at-edge/">Up to 10x faster cached queries for Hyperdrive</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.</p>
<p>When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.</p>
<p>This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-edge-caching-metrics.png" alt="Hyperdrive edge caching improves average session duration for database queries" /></p>
<p><em>P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.</em></p>
<p>This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.</p>
<p>For more details on how Hyperdrive performs query caching, refer to the <a href="/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching">Hyperdrive documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-11">Dec 11, 2024</time><div>
<h2 id="post-2024-12-11-terraform-snippets"><a href="/changelog/post/2024-12-11-terraform-snippets/">Terraform Support for Snippets</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Now, you can manage <a href="/rules/snippets/">Cloudflare Snippets</a> with <a href="/terraform/">Terraform</a>. Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.</p>
<p>Example Terraform configuration:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>Learn more in the <a href="/rules/snippets/create-terraform/">Configure Snippets using Terraform</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-12-05">Dec 5, 2024</time><div>
<h2 id="post-2024-12-05-cloud-onramp-terraform"><a href="/changelog/post/2024-12-05-cloud-onramp-terraform/">Generate customized terraform files for building cloud network on-ramps</a></h2>
<div class="changelog-badges"><span>multi-cloud-networking</span></div><div class="changelog-body"><p>You can now generate customized terraform files for building cloud network on-ramps to <a href="/cloudflare-wan/">Magic WAN</a>.</p>
<p><a href="/multi-cloud-networking/">Magic Cloud</a> can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.</p>
<p>You might want to do this to:</p>
<ul>
<li>Review the proposed configuration for an on-ramp before deploying it with Cloudflare.</li>
<li>Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.</li>
</ul>
<p>For more details, refer to <a href="/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform">Set up with Terraform</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-22">Nov 22, 2024</time><div>
<h2 id="post-2024-11-22-cloud-data-extraction-aws"><a href="/changelog/post/2024-11-22-cloud-data-extraction-aws/">Find security misconfigurations in your AWS cloud environment</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p>You can now use CASB to find security misconfigurations in your AWS cloud environment using <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a>.</p>
<p>You can also <a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account">connect your AWS compute account</a> to extract and scan your S3 buckets for sensitive data while avoiding egress fees. CASB will scan any objects that exist in the bucket at the time of configuration.</p>
<p>To connect a compute account to your AWS integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find and select your AWS integration.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to connect a new compute account.</li>
<li>Select <strong>Refresh</strong>.</li>
</ol>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-22">Nov 22, 2024</time><div>
<h2 id="post-2024-11-22-cloud-connector-r2"><a href="/changelog/post/2024-11-22-cloud-connector-r2/">Cloud Connector Now Supports R2</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Now, you can use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to your <a href="/r2/">R2 buckets</a> based on URLs, headers, geolocation, and more.</p>
<p>Example setup:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<p>Get started using <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-21">Nov 21, 2024</time><div>
<h2 id="post-2024-11-21-non-english-keyboard"><a href="/changelog/post/2024-11-21-non-english-keyboard/">Improved non-English keyboard support</a></h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-20">Nov 20, 2024</time><div>
<h2 id="post-2024-11-20-smart-tiered-cache-for-r2"><a href="/changelog/post/2024-11-20-smart-tiered-cache-for-r2/">Smart Tiered Cache automatically optimizes R2 caching</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now reduce latency and lower R2 egress costs automatically when using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> with <a href="/r2/">R2</a>. Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.</p>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-how-it-works">How it works</h4>
<p>When you enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> for zones using <a href="/r2/">R2</a> as an origin, Cloudflare automatically:</p>
<ol>
<li><strong>Identifies your R2 bucket location</strong>: Determines the geographical region where your R2 bucket is stored.</li>
<li><strong>Selects an optimal Upper Tier</strong>: Chooses a data center close to your bucket as the common Upper Tier cache.</li>
<li><strong>Routes requests efficiently</strong>: All cache misses in edge locations route through this Upper Tier before reaching R2.</li>
</ol>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-benefits">Benefits</h4>
<ul>
<li><strong>Automatic optimization</strong>: No manual configuration required.</li>
<li><strong>Lower egress costs</strong>: Fewer requests to R2 reduce egress charges.</li>
<li><strong>Improved hit ratio</strong>: Common Upper Tier increases cache efficiency.</li>
<li><strong>Reduced latency</strong>: Upper Tier proximity to R2 minimizes fetch times.</li>
</ul>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone using R2 as an origin.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-11">Nov 11, 2024</time><div>
<h2 id="post-2024-11-11-cache-no-store"><a href="/changelog/post/2024-11-11-cache-no-store/">Bypass caching for subrequests made from Cloudflare Workers, with Request.cache</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now use the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface to bypass <a href="/workers/reference/how-the-cache-works/">Cloudflare's cache</a> when making subrequests from <a href="/workers">Cloudflare Workers</a>, by setting its value to <code>no-store</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17761.md")</div>
<p>When you set the value to <code>no-store</code> on a subrequest made from a Worker, the Cloudflare Workers runtime will not check whether a match exists in the cache, and not add the response to the cache, even if the response includes directives in the <code>Cache-Control</code> HTTP header that otherwise indicate that the response is cacheable.</p>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code> property on <code>Request</code>, the Workers runtime threw an exception.</p>
<p>If you've tried to use <code>@planetscale/database</code>, <code>redis-js</code>, <code>stytch-node</code>, <code>supabase</code>, <code>axiom-js</code> or have seen the error message <code>The cache field on RequestInitializerDict is not implemented in fetch</code> — you should try again, making sure that the <a href="/workers/configuration/compatibility-dates/">Compatibility Date</a> of your Worker is set to on or after <code>2024-11-11</code>, or the <a href="/workers/configuration/compatibility-flags/#enable-cache-no-store-http-standard-api"><code>cache_option_enabled</code> compatibility flag</a> is enabled for your Worker.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-08">Nov 8, 2024</time><div>
<h2 id="post-2024-11-07-logpush-user-actions"><a href="/changelog/post/2024-11-07-logpush-user-actions/">Use Logpush for Email security user actions</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.</p>
<p>When creating a new Logpush job, remember to select <strong>Audit logs</strong> as the dataset and filter by:</p>
<ul>
<li><strong>Field</strong>: <code>&quot;ResourceType&quot;</code></li>
<li><strong>Operator</strong>: <code>&quot;starts with&quot;</code></li>
<li><strong>Value</strong>: <code>&quot;email_security&quot;</code>.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-User-Actions.png" alt="Logpush-user-actions" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs">Enable user action logs</a>.</p>
<p>This feature is available across all Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-07">Nov 7, 2024</time><div>
<h2 id="post-2024-11-07-cache-versioning"><a href="/changelog/post/2024-11-07-cache-versioning/">Stage and test cache configurations safely</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.</p>
<h4 id="2024-11-07-cache-versioning-how-it-works">How it works</h4>
<p>With versioned environments, you can:</p>
<ol>
<li><strong>Create staging versions</strong> of your cache configuration.</li>
<li><strong>Test cache rules</strong> in a non-production environment.</li>
<li><strong>Purge staged content</strong> independently from production.</li>
<li><strong>Validate changes</strong> before promoting to production.</li>
</ol>
<p>This capability integrates with Cloudflare's broader <a href="/version-management/">versioning system</a>, allowing you to manage cache configurations alongside other zone settings.</p>
<h4 id="2024-11-07-cache-versioning-benefits">Benefits</h4>
<ul>
<li><strong>Risk-free testing</strong>: Validate configuration changes without impacting production.</li>
<li><strong>Independent purging</strong>: Clear staging cache without affecting live content.</li>
<li><strong>Deployment confidence</strong>: Catch issues before they reach end users.</li>
<li><strong>Team collaboration</strong>: Multiple team members can work on different versions.</li>
</ul>
<h4 id="2024-11-07-cache-versioning-get-started">Get started</h4>
<p>To get started, refer to the <a href="/version-management/">version management documentation</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2024-11-07-cache-versioning-important-limitation">Important limitation</h4>
@markup("md", "content/.markup/bodies/17701.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-11-07">Nov 7, 2024</time><div>
<h2 id="post-2024-11-07-shard-cache-by-cache-key"><a href="/changelog/post/2024-11-07-shard-cache-by-cache-key/">Shard cache using custom cache key values</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by <strong>sharding cache</strong> using up to ten values from previously restricted headers with <a href="/cache/how-to/cache-keys/">custom cache keys</a>.</p>
<h4 id="2024-11-07-shard-cache-by-cache-key-how-it-works">How it works</h4>
<p>When configuring <a href="/cache/how-to/cache-keys/">custom cache keys</a>, you can now include values from these headers to create distinct cache entries:</p>
<ul>
<li><strong><code>accept*</code> headers</strong> (for example, <code>accept</code>, <code>accept-encoding</code>, <code>accept-language</code>): Serve different cached versions based on content negotiation.</li>
<li><strong><code>referer</code> header</strong>: Cache content differently based on the referring page or site.</li>
<li><strong><code>user-agent</code> header</strong>: Maintain separate caches for different browsers, devices, or bots.</li>
</ul>
<h4 id="2024-11-07-shard-cache-by-cache-key-when-to-use-cache-sharding">When to use cache sharding</h4>
<ul>
<li>Content varies significantly by device type (mobile vs desktop).</li>
<li>Different language or encoding preferences require distinct responses.</li>
<li>Referrer-specific content optimization is needed.</li>
</ul>
<h4 id="2024-11-07-shard-cache-by-cache-key-example-configuration">Example configuration</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;cache_key&quot;: {&#10;    &quot;custom_key&quot;: {&#10;      &quot;header&quot;: {&#10;        &quot;include&quot;: [&quot;accept-language&quot;, &quot;user-agent&quot;],&#10;        &quot;check_presence&quot;: [&quot;referer&quot;]&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>This configuration creates separate cache entries based on the <code>accept-language</code> and <code>user-agent</code> headers, while also considering whether the <code>referer</code> header is present.</p>
<h4 id="2024-11-07-shard-cache-by-cache-key-get-started">Get started</h4>
<p>To get started, refer to the <a href="/cache/how-to/cache-keys/">custom cache keys documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17702.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-10-24">Oct 24, 2024</time><div>
<h2 id="post-2024-10-24-workflows-beta"><a href="/changelog/post/2024-10-24-workflows-beta/">Workflows is now in open beta</a></h2>
<div class="changelog-badges"><span>workers</span><span>workflows</span></div><div class="changelog-body"><p>Workflows is now in open beta, and available to any developer a free or paid Workers plan.</p>
<p>Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.</p>
<h4 id="2024-10-24-workflows-beta-get-started">Get started</h4>
<p>You can get started with Workflows by <a href="/workflows/get-started/guide/">following our get started guide</a> and/or using <code>npm create cloudflare</code> to pull down the starter project:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>You can open the <code>src/index.ts</code> file, extend it, and use <code>wrangler deploy</code> to deploy your first Workflow. From there, you can:</p>
<ul>
<li>Learn the <a href="/workflows/build/workers-api/">Workflows API</a></li>
<li><a href="/workflows/build/trigger-workflows/">Trigger Workflows</a> via your Workers apps.</li>
<li>Understand the <a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a> and how to adopt best practices</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-10-23">Oct 23, 2024</time><div>
<h2 id="post-2024-10-23-url-rewrites-wildcard"><a href="/changelog/post/2024-10-23-url-rewrites-wildcard/">Simplified UI for URL Rewrites</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>It’s now easy to create <strong>wildcard-based <a href="/rules/transform/url-rewrite/">URL Rewrites</a></strong>. No need for complex functions—just define your patterns and go.</p>
<p><img src="/assets/upstream/images/rules/transform/create-url-rewrite-rule.png" alt="Rules Overview Interface" /></p>
<p>What’s improved:</p>
<ul>
<li><strong>Full wildcard support</strong> – Create rewrite patterns using intuitive interface.</li>
<li><strong>Simplified rule creation</strong> – No need for complex functions.</li>
</ul>
<p>Try it via <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">creating a Rewrite URL rule in the dashboard</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-10-08">Oct 8, 2024</time><div>
<h2 id="post-2024-10-08-new-gateway-fields"><a href="/changelog/post/2024-10-08-new-gateway-fields/">New fields added to Gateway-related datasets in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has introduced new fields to two Gateway-related datasets in Cloudflare Logs:</p>
<ul>
<li>
<p><strong>Gateway HTTP</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>CategoryIDs</code>, <code>CategoryNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
<li>
<p><strong>Gateway Network</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>TransportProtocol</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-10-02">Oct 2, 2024</time><div>
<h2 id="post-2024-10-02-custom-rule-search"><a href="/changelog/post/2024-10-02-custom-rule-search/">Search for custom rules using rule name and/or ID</a></h2>
<div class="changelog-badges"><span>cloudflare-network-firewall</span></div><div class="changelog-body"><p>The Magic Firewall dashboard now allows you to search custom rules using the rule name and/or ID.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Network Analytics</strong>.</li>
<li>Select <strong>Magic Firewall</strong>.</li>
<li>Add a filter for <strong>Rule ID</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/search-with-rule-id.png" alt="Search for firewall rules with rule IDs" /></p>
<p>Additionally, the rule ID URL link has been added to Network Analytics.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-10-01">Oct 1, 2024</time><div>
<h2 id="post-2024-10-01-ssh-with-access-for-infrastructure"><a href="/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/">Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.</p>
<p>SSH with <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/">WARP-to-Tunnel</a>.</p>
<p>SSH with Access for Infrastructure enables you to:</p>
<ul>
<li><strong>Author fine-grained policy</strong> to control who may access your SSH servers, including specific ports, protocols, and SSH users.</li>
<li><strong>Monitor infrastructure access</strong> with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.</li>
<li><strong>Preserve your end users' workflows.</strong> SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/infrastructure-app.png" alt="Example of an infrastructure Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Access for Infrastructure</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-09-24">Sep 24, 2024</time><div>
<h2 id="post-2024-09-24-magic-network-monitoring"><a href="/changelog/post/2024-09-24-magic-network-monitoring/">Try out Magic Network Monitoring</a></h2>
<div class="changelog-badges"><span>network-flow</span></div><div class="changelog-body"><p>The free version of Magic Network Monitoring (MNM) is now available to everyone with a Cloudflare account by default.</p>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Magic Monitoring</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/network-flow/get-started.png" alt="Try out the free version of Magic Network Monitoring" /></p>
<p>For more details, refer to the <a href="/network-flow/get-started/">Get started guide</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/48/">Previous</a><span>Page 49 of 50</span><a class="pagination-next" rel="next" href="/changelog/50/">Next</a></nav>
</div>
