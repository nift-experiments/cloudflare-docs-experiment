---
cp9:
  canonical: https://developers.cloudflare.com/changelog/43/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 43 | Cloudflare Docs
  head_html: <title>Changelog - page 43 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/43/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 43"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/43/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/43/#page","headline":"Changelog - page 43 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/43/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/43/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-05-08">May 8, 2025</time><div>
<h2 id="post-2025-05-08-finalization-registry"><a href="/changelog/post/2025-05-08-finalization-registry/">Improved memory efficiency for WebAssembly Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry">FinalizationRegistry</a> is now available in Workers. You can opt-in using the <a href="/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref"><code>enable_weak_ref</code></a> compatibility flag.</p>
<p>This can reduce memory leaks when using WebAssembly-based Workers, which includes <a href="/workers/languages/python/">Python Workers</a> and <a href="/workers/languages/rust/">Rust Workers</a>. The FinalizationRegistry works by enabling toolchains such as <a href="https://emscripten.org/">Emscripten</a> and <a href="https://wasm-bindgen.github.io/wasm-bindgen/">wasm-bindgen</a> to automatically free WebAssembly heap allocations. If you are using WASM and seeing Exceeded Memory errors and cannot determine a cause using <a href="/workers/observability/dev-tools/memory-usage/">memory profiling</a>, you may want to enable the FinalizationRegistry.</p>
<p>For more information refer to the <a href="/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref"><code>enable_weak_ref</code></a> compatibility flag documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-07">May 7, 2025</time><div>
<h2 id="post-2025-05-07-forensic-copy-update"><a href="/changelog/post/2025-05-07-forensic-copy-update/">Send forensic copies to storage without DLP profiles</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination">send DLP forensic copies</a> to third-party storage for any HTTP policy with an <code>Allow</code> or <code>Block</code> action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.</p>
<p>By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.</p>
<p><img src="/assets/upstream/images/changelog/dlp/forensic-copies-for-all.png" alt="DLP" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-06">May 6, 2025</time><div>
<h2 id="post-2025-05-06-private-health-monitoring-methods"><a href="/changelog/post/2025-05-06-private-health-monitoring-methods/">UDP and ICMP Monitor Support for Private Load Balancing Endpoints</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Cloudflare Load Balancing now supports <strong>UDP (Layer 4)</strong> and <strong>ICMP (Layer 3)</strong> health monitors for <strong>private endpoints</strong>. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.</p>
<h4 id="2025-05-06-private-health-monitoring-methods-what-you-can-do">What you can do:</h4>
<ul>
<li>Set up <strong>ICMP ping monitors</strong> to check if your private endpoints are reachable.</li>
<li>Use <strong>UDP monitors</strong> for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.</li>
<li>Gain better visibility and uptime guarantees for services running behind <strong>Private Network Load Balancing</strong>, without requiring public IP addresses.</li>
</ul>
<p>This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/"><strong>Cloudflare Tunnel</strong></a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/"><strong>WARP</strong></a>, and <a href="/cloudflare-wan/"><strong>Magic WAN</strong></a> to create a secure and observable private network.</p>
<p>Learn more about <a href="/load-balancing/private-network/">Private Network Load Balancing</a> or view the full list of <a href="/load-balancing/monitors/#supported-protocols">supported health monitor protocols</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-06">May 6, 2025</time><div>
<h2 id="post-2025-05-06-terraform-v5.4.0-provider"><a href="/changelog/post/2025-05-06-terraform-v5.4.0-provider/">Terraform v5.4.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-changes">Changes</h4>
<ul>
<li>
<p>Removes the <code>worker_platforms_script_secret</code> resource from the provider (see <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret">migration guide</a> for alternatives—applicable to both Workers and Workers for Platforms)</p>
</li>
<li>
<p>Removes duplicated fields in <code>cloudflare_cloud_connector_rules</code> resource</p>
</li>
<li>
<p>Fixes <code>cloudflare_workers_route</code> id issues <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134">#5134</a> <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501">#5501</a></p>
</li>
<li>
<p>Fixes issue around refreshing resources that have unsupported response types</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre tabindex="0"><code>  &lt;li&gt;`cloudflare_certificate_pack`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_registrar_domain`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_download`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_webhook`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_user`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_kv`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_script`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixes <code>cloudflare_workers_kv</code> state refresh issues</p>
</li>
<li>
<p>Fixes issues around configurability of nested properties without computed values for the following resources</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre tabindex="0"><code>  &lt;li&gt;`cloudflare_account`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_dns_settings`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_api_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_cloud_connector_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_custom_ssl`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_d1_database`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_dns_record`&lt;/li&gt;&#10;  &lt;li&gt;`email_security_trusted_domains`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_hyperdrive_config`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_keyless_certificate`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_list_item`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_load_balancer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_logpush_dataset_job`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_network_monitoring_configuration`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_lan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_wan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_wan_static_route`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_notification_policy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_pages_project`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue_consumer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_cors`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_event_notification`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lifecycle`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lock`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_sippy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_ruleset`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippet_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippets`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_spectrum_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_deployment`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_group`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixed defaults that made <code>cloudflare_workers_script</code> fail when using Assets</p>
</li>
<li>
<p>Fixed Workers Logpush setting in <code>cloudflare_workers_script</code> mistakenly being readonly</p>
</li>
<li>
<p>Fixed <code>cloudflare_pages_project</code> broken when using &quot;source&quot;</p>
</li>
</ul>
<p>The detailed <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0">changelog</a> is available on GitHub.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>, or by opening a <a href="https://www.support.cloudflare.com/s/?language=en_US">support ticket</a>.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-05">May 5, 2025</time><div>
<h2 id="post-2025-05-05-waf-release"><a href="/changelog/post/2025-05-05-waf-release/">WAF Release - 2025-05-05</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's analysis covers five CVEs with varying impact levels. Four are rated critical, while one is rated high severity. Remote Code Execution vulnerabilities dominate this set.</p>
<p><strong>Key Findings</strong></p>
<p>GFI KerioControl (CVE-2024-52875) contains an unauthenticated Remote Code Execution (RCE) vulnerability that targets firewall appliances. This vulnerability can let attackers gain root level system access, making this CVE particularly attractive for threat actors.</p>
<p>The SonicWall SMA vulnerabilities remain concerning due to their continued exploitation since 2021. These critical vulnerabilities in remote access solutions create dangerous entry points to networks.</p>
<p><strong>Impact</strong></p>
<p>Customers using the Managed Ruleset will receive rule coverage following this week's release. Below is a breakdown of the recommended prioritization based on current exploitation trends:</p>
<ul>
<li>GFI KerioControl (CVE-2024-52875) - Highest priority; unauthenticated RCE</li>
<li>SonicWall SMA (Multiple vulnerabilities) - Critical for network appliances</li>
<li>XWiki (CVE-2025-24893) - High priority for development environments</li>
<li>Langflow (CVE-2025-3248) - Important for AI workflow platforms</li>
<li>MinIO (CVE-2025-31489) - Important for object storage implementations</li>
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
				<code class="nb-rule-id" title="921660147baa48eaa9151077d0b7a392">d0b7a392</code>
</td>
<td>100724</td>
<td>GFI KerioControl - Remote Code Execution - CVE:CVE-2024-52875</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3900934273b4a488111f810717a9e42">717a9e42</code>
</td>
<td>100748</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="616ad0e03892473191ca1df4e9cf745d">e9cf745d</code>
</td>
<td>100750</td>
<td>
				SonicWall SMA - Dangerous File Upload - CVE:CVE-2021-20040,
				CVE:CVE-2021-20041, CVE:CVE-2021-20042
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1a11fbe84b49451193ee1ee6d29da333">d29da333</code>
</td>
<td>100751</td>
<td>Langflow - Remote Code Execution - CVE:CVE-2025-3248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100752</td>
<td>MinIO - Auth Bypass - CVE:CVE-2025-31489</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-01">May 1, 2025</time><div>
<h2 id="post-2025-05-01-browser-isolation-overview-page"><a href="/changelog/post/2025-05-01-browser-isolation-overview-page/">Browser Isolation Overview page for Zero Trust</a></h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>A new <strong>Browser Isolation Overview</strong> page is now available in the Cloudflare Zero Trust dashboard. This centralized view simplifies the management of <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> deployments, providing:</p>
<ul>
<li><strong>Streamlined Onboarding:</strong> Easily set up and manage isolation policies from one location.</li>
<li><strong>Quick Testing:</strong> Validate <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">clientless web application isolation</a> with ease.</li>
<li><strong>Simplified Configuration:</strong> Configure <a href="/cloudflare-one/access-controls/policies/isolate-application/">isolated access applications</a> and policies efficiently.</li>
<li><strong>Centralized Monitoring:</strong> Track aggregate usage and blocked actions.</li>
</ul>
<p>This update consolidates previously disparate settings, accelerating deployment, improving visibility into isolation activity, and making it easier to ensure your protections are working effectively.</p>
<p><img src="/assets/upstream/images/changelog/browser-isolation/browser-isolation-overview.png" alt="Browser Isolation Overview" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and find Browser Isolation in the side navigation bar.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-01">May 1, 2025</time><div>
<h2 id="post-2025-05-01-r2-dashboard-updates"><a href="/changelog/post/2025-05-01-r2-dashboard-updates/">R2 Dashboard experience gets new updates</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>We're excited to announce several improvements to the <a href="/r2/">Cloudflare R2</a> dashboard experience that make managing your object storage easier and more intuitive:</p>
<p><img src="/assets/upstream/images/r2/r2-dashboard-updates.png" alt="Cloudflare R2 Dashboard" /></p>
<h4 id="2025-05-01-r2-dashboard-updates-all-new-settings-page">All-new settings page</h4>
<p>We've redesigned the bucket settings page, giving you a centralized location to manage all your bucket configurations in one place.</p>
<h4 id="2025-05-01-r2-dashboard-updates-improved-navigation-and-sharing">Improved navigation and sharing</h4>
<ul>
<li>Deeplink support for prefix directories: Navigate through your bucket hierarchy without losing your state. Your browser's back button now works as expected, and you can share direct links to specific prefix directories with teammates.</li>
<li>Objects as clickable links: Objects are now proper links that you can copy or <code>CMD + Click</code> to open in a new tab.</li>
</ul>
<h4 id="2025-05-01-r2-dashboard-updates-clearer-public-access-controls">Clearer public access controls</h4>
<ul>
<li>Renamed &quot;r2.dev domain&quot; to &quot;Public Development URL&quot; for better clarity when exposing bucket contents for non-production workloads.</li>
<li>Public Access status now clearly displays &quot;Enabled&quot; when your bucket is exposed to the internet (via Public Development URL or Custom Domains).</li>
</ul>
<p>We've also made numerous other usability improvements across the board to make your R2 experience smoother and more productive.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-30">Apr 30, 2025</time><div>
<h2 id="post-2025-04-30-zero-trust-dashboard-dark-mode"><a href="/changelog/post/2025-04-30-zero-trust-dashboard-dark-mode/">Dark Mode for Zero Trust Dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>The <a href="https://one.dash.cloudflare.com/">Cloudflare Zero Trust dashboard</a> now supports Cloudflare's native dark mode for all accounts and plan types.</p>
<p>Zero Trust Dashboard will automatically accept your user-level preferences for system settings, so if your Dashboard appearance is set to 'system' or 'dark', the Zero Trust dashboard will enter dark mode whenever the rest of your Cloudflare account does.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/dark-mode.png" alt="Zero Trust dashboard supports dark mode" /></p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17706.md")
</div></div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-30">Apr 30, 2025</time><div>
<h2 id="post-2025-04-30-appliance-multiple-dns-servers"><a href="/changelog/post/2025-04-30-appliance-multiple-dns-servers/">Cloudflare One Appliance supports multiple DNS server IPs</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.</p>
<p>Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-28">Apr 28, 2025</time><div>
<h2 id="post-2025-04-28-FDQN-Filtering-Egress-Policies"><a href="/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/">FQDN Filtering For Gateway Egress Policies</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.</p>
<ul>
<li>Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.</li>
<li>During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
<ul>
<li>For WARP client support, additional configuration is required. For more information, refer to the <a href="/cloudflare-one/traffic-policies/egress-policies/#limitations">WARP client configuration documentation</a>.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/gateway/Gateway-Egress-FQDN-Policy-preview.png" alt="Egress by FQDN and Hostname" /></p>
<p>This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-26">Apr 26, 2025</time><div>
<h2 id="post-2025-04-26-emergency-waf-release"><a href="/changelog/post/2025-04-26-emergency-waf-release/">WAF Release - 2025-04-26 - Emergency</a></h2>
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
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="54ea354d7f2d43c69b238d1419fcc883">19fcc883</code>
</td>
<td>100755</td>
<td>
				React.js - Router and Remix Vulnerability - CVE:CVE-2025-43864,
				CVE:CVE-2025-43865
</td>
<td>Block</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-24">Apr 24, 2025</time><div>
<h2 id="post-2025-04-24-custom-errors-ga"><a href="/changelog/post/2025-04-24-custom-errors-ga/">Custom Errors are now Generally Available</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p><a href="/rules/custom-errors/">Custom Errors</a> are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.</p>
<p>You can now manage <strong>Custom Error Rules</strong>, <strong>Custom Error Assets</strong>, and redesigned <strong>Error Pages</strong> directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.</p>
<p>What's new:</p>
<ul>
<li><strong>Custom Errors are now GA</strong> – Available on all paid plans and ready for production traffic.</li>
<li><strong>UI for Custom Error Rules and Assets</strong> – Manage your zone-level rules from the Rules &gt; Overview and your zone-level assets from the Rules &gt; Settings tabs.</li>
<li><strong>Define inline content or upload assets</strong> – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.</li>
<li><strong>Refreshed UI and new name for Error Pages</strong> – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.</li>
<li><strong>Powered by Ruleset Engine</strong> – Custom Error Rules support <a href="/ruleset-engine/rules-language/">conditional logic</a> and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or <a href="/ruleset-engine/reference/phases-list/">other Cloudflare products</a>. You can also configure <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> to add, change, or remove HTTP headers from responses returned by Custom Error Rules.</li>
</ul>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-24">Apr 24, 2025</time><div>
<h2 id="post-2025-04-22-python-worker-cron-triggers"><a href="/changelog/post/2025-04-22-python-worker-cron-triggers/">Cron triggers are now supported in Python Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create Python Workers which are executed via a cron trigger.</p>
<p>This is similar to how it's done in JavaScript Workers, simply define a scheduled event
listener in your Worker:</p>
<pre tabindex="0"><code class="language-python">from workers import handler&#10;&#10;@handler&#10;async def on_scheduled(event, env, ctx):&#10;  print(&quot;cron processed&quot;)&#10;</code></pre>
<p>Define a cron trigger configuration in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17772.md")</div>
<p>Then test your new handler by using Wrangler with the <code>--test-scheduled</code> flag and
making a request to <code>/cdn-cgi/local/scheduled?cron=*+*+*+*+*</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<p>Consult the <a href="/workers/configuration/cron-triggers/">Workers Cron Triggers page</a> for full details on cron triggers in Workers.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-23">Apr 23, 2025</time><div>
<h2 id="post-2025-04-23-autorag-metadata-filtering"><a href="/changelog/post/2025-04-23-autorag-metadata-filtering/">Metadata filtering and multitenancy support in AutoRAG</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now filter <a href="/ai-search/">AutoRAG</a> search results by <code>folder</code> and <code>timestamp</code> using <a href="/ai-search/configuration/indexing/metadata/">metadata filtering</a> to narrow down the scope of your query.</p>
<p>This makes it easy to build <a href="/ai-search/how-to/per-tenant-search/">multitenant experiences</a> where each user can only access their own data. By organizing your content into per-tenant folders and applying a <code>folder</code> filter at query time, you ensure that each tenant retrieves only their own documents.</p>
<p><strong>Example folder structure:</strong></p>
<pre tabindex="0"><code class="language-bash">customer-a/logs/&#10;customer-a/contracts/&#10;customer-b/contracts/&#10;</code></pre>
<p><strong>Example query:</strong></p>
<pre tabindex="0"><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;When did I sign my agreement contract?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;folder&quot;,&#10;		value: &quot;customer-a/contracts/&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select <strong>Sync index</strong>. Metadata filtering is available for all data indexed on or after <strong>April 21, 2025</strong>.</p>
<p>If you are new to AutoRAG, get started with the <a href="/ai-search/get-started/">Get started AutoRAG guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-22">Apr 22, 2025</time><div>
<h2 id="post-2025-04-22-waf-release"><a href="/changelog/post/2025-04-22-waf-release/">WAF Release - 2025-04-22</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>Each of this week's rule releases covers a distinct CVE, with half of the rules targeting Remote Code Execution (RCE) attacks. Of the 6 CVEs covered, four were scored as critical, with the other two scored as high.</p>
<p>When deciding which exploits to tackle, Cloudflare tunes into the attackers' areas of focus. Cloudflare's network intelligence provides a unique lens into attacker activity – for instance, through the volume of blocked requests related with CVE exploits after updating WAF Managed Rules with new detections.</p>
<p>From this week's releases, one indicator that RCE is a &quot;hot topic&quot; attack type is the fact that the Oracle PeopleSoft RCE rule accounts for half of all of the new rule matches. This rule patches CVE-2023-22047, a high-severity vulnerability in the Oracle PeopleSoft suite that allows unauthenticated attackers to access PeopleSoft Enterprise PeopleTools data through remote code execution. This is particularly concerning because of the nature of the data managed by PeopleSoft – this can include payroll records or student profile information. This CVE, along with five others, are addressed with the latest detection update to WAF Managed Rules.</p>
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
				<code class="nb-rule-id" title="faa032d9825e4844a1188f3ba5be3327">a5be3327</code>
</td>
<td>100738</td>
<td>GitLab - Auth Bypass - CVE:CVE-2023-7028</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e96b6d5cdd94f7782b90e266c9531fa">6c9531fa</code>
</td>
<td>100740</td>
<td>Splunk Enterprise - Remote Code Execution - CVE:CVE-2025-20229</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5c9c095bc1e5411195edb893f40bbc2b">f40bbc2b</code>
</td>
<td>100741</td>
<td>Oracle PeopleSoft - Remote Code Execution - CVE:CVE-2023-22047</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1d7a3932296c42fd827055335462167c">5462167c</code>
</td>
<td>100742</td>
<td>CrushFTP - Auth Bypass - CVE:CVE-2025-31161</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100743</td>
<td>Ivanti - Buffer Error - CVE:CVE-2025-22457</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="410317f1e32b41859fa3214dd52139a8">d52139a8</code>
</td>
<td>100744</td>
<td>
				Oracle Access Manager - Remote Code Execution - CVE:CVE-2021-35587
</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-21">Apr 21, 2025</time><div>
<h2 id="post-2025-04-21-Access-Bulk-Policy-Tester"><a href="/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/">Access bulk policy tester</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>The <a href="/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application">Access bulk policy tester</a> is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).</p>
<p><img src="/assets/upstream/images/changelog/access/example-policy-tester.png" alt="Example policy tester" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-18">Apr 18, 2025</time><div>
<h2 id="post-2025-04-18-custom-fields-raw-transformed-values"><a href="/changelog/post/2025-04-18-custom-fields-raw-transformed-values/">Custom fields raw and transformed values support</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Custom Fields now support logging both <strong>raw and transformed values</strong> for request and response headers in the HTTP requests dataset.</p>
<p>These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.</p>
<p>By default:</p>
<ul>
<li>Request headers are logged as raw values</li>
<li>Response headers are logged as transformed values</li>
</ul>
<p>These defaults can be overridden to suit your logging needs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17737.md")</aside>
<p>For more information refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> documentation</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-17">Apr 17, 2025</time><div>
<h2 id="post-2025-04-17-pull-consumer-limits"><a href="/changelog/post/2025-04-17-pull-consumer-limits/">Increased limits for Queues pull consumers</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues/configuration/pull-consumers/">Queues pull consumers</a> can now pull and acknowledge up to <strong>5,000 messages / second per queue</strong>. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.</p>
<p>Pull consumers allow you to consume messages over HTTP from any environment—including outside of <a href="/workers">Cloudflare Workers</a>. They’re also useful when you need fine-grained control over how quickly messages are consumed.</p>
<p>To setup a new queue with a pull based consumer using <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler queues create my-queue&#10;npx wrangler queues consumer http add my-queue&#10;</code></pre>
<p>You can also configure a pull consumer using the <a href="/api/resources/queues/subresources/consumers/methods/create/">REST API</a> or the Queues dashboard.</p>
<p>Once configured, you can pull messages from the queue using any HTTP client. You'll need a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API Token</a> with <code>queues_read</code> and <code>queues_write</code> permissions. For example:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull&quot; \&#10;&#45;-header &quot;Authorization: Bearer ${API_TOKEN}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;visibility_timeout&quot;: 10000, &quot;batch_size&quot;: 2 }&#x27;&#10;</code></pre>
<p>To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the <a href="/queues/configuration/pull-consumers">pull consumer documentation</a>.</p>
<p>As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the <a href="/queues/platform/pricing">existing rate</a>, of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-17">Apr 17, 2025</time><div>
<h2 id="post-2025-04-10-kv-bulk-reads"><a href="/changelog/post/2025-04-10-kv-bulk-reads/">Read multiple keys from Workers KV with bulk reads</a></h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.</p>
<p>This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by <a href="/workers/platform/limits/#simultaneous-open-connections">Workers simultaneous connection limits</a>.</p>
<pre tabindex="0"><code class="language-js">// Read single key&#10;const key = &quot;key-a&quot;;&#10;const value = await env.NAMESPACE.get(key);&#10;&#10;// Read multiple keys&#10;const keys = [&quot;key-a&quot;, &quot;key-b&quot;, &quot;key-c&quot;, ...] // up to 100 keys&#10;const values : Map&lt;string, string?&gt; = await env.NAMESPACE.get(keys);&#10;&#10;// Print the value of &quot;key-a&quot; to the console.&#10;console.log(`The first key is ${values.get(&quot;key-a&quot;)}.`)&#10;</code></pre>
<p>Consult the <a href="/kv/api/read-key-value-pairs/">Workers KV Read key-value pairs API</a> for full details on Workers KV's new bulk reads support.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-15">Apr 15, 2025</time><div>
<h2 id="post-2026-04-15-registrar-api-beta"><a href="/changelog/post/2026-04-15-registrar-api-beta/">Cloudflare Registrar API is now in beta</a></h2>
<div class="changelog-badges"><span>registrar</span></div><div class="changelog-body"><p>Cloudflare Registrar API is now in beta.</p>
<p>You can now use the Cloudflare API to:</p>
<ul>
<li>Search for domain names.</li>
<li>Check real-time availability and pricing.</li>
<li>Register supported domains programmatically.</li>
</ul>
<p>This beta supports a subset of popular extensions available through Cloudflare Registrar. Search returns suggestions across API-supported extensions, check confirms current availability and pricing, and registration starts a workflow that can complete immediately or be polled if it takes longer.</p>
<p>Because the Registrar API is part of the Cloudflare API, it can also be used in <a href="https://github.com/cloudflare/mcp">Cloudflare MCP</a> and other agent-driven workflows.</p>
<p>If you are using Cloudflare MCP or other agent-driven workflows, prompts can be as simple as:</p>
<ul>
<li><code>Search for domain ideas for a coffee shop based in Evergreen, Colorado.</code></li>
<li><code>Check whether example.com is available and show me the current price.</code></li>
<li><code>Register example.com</code></li>
</ul>
<p>For supported operations, extension availability, and workflow details, refer to:</p>
<ul>
<li><a href="https://developers.cloudflare.com/registrar/registrar-api/">Registrar API guide</a></li>
<li><a href="https://developers.cloudflare.com/api/resources/registrar">Registrar API reference</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-15">Apr 15, 2025</time><div>
<h2 id="post-2025-04-15-workers-api-fixes"><a href="/changelog/post/2025-04-15-workers-api-fixes/">Fixed and documented Workers Routes and Secrets API</a></h2>
<div class="changelog-badges"><span>workers</span><span>workers-for-platforms</span></div><div class="changelog-body"><h4 id="2025-04-15-workers-api-fixes-workers-routes-api">Workers Routes API</h4>
<p>Previously, a request to the Workers <a href="/api/resources/workers/subresources/routes/methods/create/">Create Route API</a> always returned <code>null</code> for &quot;script&quot; and an empty string for &quot;pattern&quot; even if the request was successful.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \&#10;&#45;X PUT \&#10;&#45;H &quot;Authorization: Bearer $CF_API_TOKEN&quot; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{ &quot;pattern&quot;: &quot;example.com/*&quot;, &quot;script&quot;: &quot;hello-world-script&quot; }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;&quot;,&#10;		&quot;script&quot;: null,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Now, it properly returns all values!</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;example.com/*&quot;,&#10;		&quot;script&quot;: &quot;hello-world-script&quot;,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="2025-04-15-workers-api-fixes-workers-secrets-api">Workers Secrets API</h4>
<p>The <a href="/api/resources/workers/subresources/scripts/subresources/secrets/">Workers</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/">Workers for Platforms</a> secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (&gt;4.2.0) and <a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (&gt;4.1.0).</p>
<p>Note the <code>cloudflare_workers_secret</code> and <code>cloudflare_workers_for_platforms_script_secret</code> <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform resources</a> are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:</p>
<ul>
<li><a href="/api/resources/secrets_store/">Secrets Store</a> with the &quot;Secrets Store Secret&quot; binding on Workers and Workers for Platforms Script Upload</li>
<li>&quot;Secret Text&quot; Binding on <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Workers for Platforms Script Upload</a></li>
<li>Workers (and WFP) Secrets API</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-14">Apr 14, 2025</time><div>
<h2 id="post-2025-04-14-icd11-support"><a href="/changelog/post/2025-04-14-icd11-support/">New predefined detection entry for ICD-11</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You now have access to the World Health Organization (WHO) 2025 edition of the <a href="https://www.who.int/news/item/14-02-2025-who-releases-2025-update-to-the-international-classification-of-diseases-%28icd-11%29">International Classification of Diseases 11th Revision (ICD-11)</a> as a predefined detection entry. The new dataset can be found in the <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#health-information">Health Information</a> predefined profile.</p>
<p>ICD-10 dataset remains available for use.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-14">Apr 14, 2025</time><div>
<h2 id="post-2025-04-14-waf-release"><a href="/changelog/post/2025-04-14-waf-release/">WAF Release - 2025-04-14</a></h2>
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
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9209bb65527f4c088bca5ffad6b2d36c">d6b2d36c</code>
</td>
<td>100739A</td>
<td>Next.js - Auth Bypass - CVE:CVE-2025-29927 - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-11">Apr 11, 2025</time><div>
<h2 id="post-2025-04-11-http-redirect-custom-block-page-redirect"><a href="/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/">HTTP redirect and custom block page redirect</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>You can now use more flexible redirect capabilities in Cloudflare One with Gateway.</p>
<ul>
<li>A new <strong>Redirect</strong> action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.</li>
<li>For <strong>Block</strong> actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.</li>
</ul>
<p>Learn more in our documentation for <a href="/cloudflare-one/traffic-policies/http-policies/#redirect">HTTP Redirect</a> and <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">Block page redirect</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-11">Apr 11, 2025</time><div>
<h2 id="post-2025-04-14-webrtc-beta-signed-urls"><a href="/changelog/post/2025-04-14-webrtc-beta-signed-urls/">Signed URLs and Infrastructure Improvements on Stream Live WebRTC Beta</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>Cloudflare <a href="/stream/">Stream</a> has completed an infrastructure upgrade for our <a href="/stream/webrtc-beta/">Live WebRTC beta</a> support which brings increased scalability and improved playback performance to all customers. WebRTC allows broadcasting directly from a browser (or supported WHIP client) with ultra-low latency to tens of thousands of concurrent viewers across the globe.</p>
<p>Additionally, as part of this upgrade, the WebRTC beta now supports Signed URLs to protect playback, just like our standard live stream options (HLS/DASH).</p>
<p>For more information, learn about the <a href="/stream/webrtc-beta/">Stream Live WebRTC beta</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/42/">Previous</a><span>Page 43 of 50</span><a class="pagination-next" rel="next" href="/changelog/44/">Next</a></nav>
</div>
