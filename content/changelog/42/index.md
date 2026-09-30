<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-05-29">May 29, 2025</time><div>
<h2 id="post-2025-05-30-d1-rest-api-latency"><a href="/changelog/post/2025-05-30-d1-rest-api-latency/">50-500ms Faster D1 REST API Requests</a></h2>
<div class="changelog-badges"><span>d1</span><span>workers</span></div><div class="changelog-body"><p>Users using Cloudflare's <a href="/api/resources/d1/">REST API</a> to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.</p>
<p>Latency improvements range from 50-500 ms depending on request location and <a href="/d1/configuration/data-location/">database location</a> and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.</p>
<p>D1 query endpoints like <code>/query</code> and <code>/raw</code> have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-28">May 28, 2025</time><div>
<h2 id="post-2025-05-28-playwright-mcp"><a href="/changelog/post/2025-05-28-playwright-mcp/">Playwright MCP server is now compatible with Browser Rendering</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We're excited to share that you can now use the <a href="https://github.com/cloudflare/playwright-mcp">Playwright MCP</a> server with Browser Rendering.</p>
<p>Once you <a href="/browser-run/playwright/playwright-mcp/#deploying">deploy the server</a>, you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.</p>
<p><img src="/assets/upstream/images/browser-run/playground-ai-screenshot.png" alt="Access Analytics" /></p>
<p>Playwright MCP is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright-mcp"><code>@cloudflare/playwright-mcp</code></a>. To install it, type:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Deploying the server is then as easy as:</p>
<pre><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createMcpAgent } from &quot;@cloudflare/playwright-mcp&quot;;&#10;&#10;export const PlaywrightMCP = createMcpAgent(env.BROWSER);&#10;export default PlaywrightMCP.mount(&quot;/sse&quot;);&#10;</code></pre>
<p>Check out the full code at <a href="https://github.com/cloudflare/playwright-mcp">GitHub</a>.</p>
<p>Learn more about Playwright MCP in our <a href="/browser-run/playwright/playwright-mcp/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-28">May 28, 2025</time><div>
<h2 id="post-2025-05-28-updated-attack-score-model"><a href="/changelog/post/2025-05-28-updated-attack-score-model/">Updated attack score model</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>We have deployed an updated attack score model focused on enhancing the detection of multiple false positives (FPs).</p>
<p>As a result of this improvement, some changes in observed attack scores are expected.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-27">May 27, 2025</time><div>
<h2 id="post-2025-05-19-paygo-updates"><a href="/changelog/post/2025-05-19-paygo-updates/">Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</a></h2>
<div class="changelog-badges"><span>ssl</span><span>cloudflare-for-saas</span><span>secrets-store</span></div><div class="changelog-body"><p>With upgraded limits to <a href="https://www.cloudflare.com/plans/">all free and paid plans</a>, you can now scale more easily with <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> and <a href="https://developers.cloudflare.com/secrets-store/">Secrets Store</a>.</p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/">limit for custom hostnames</a> on a Cloudflare for SaaS Pay-as-you-go plan has been <strong>raised from 5,000 custom hostnames to 50,000 custom hostnames.</strong></p>
<p>With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">Custom origin server</a> is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.</p>
<p>You can enable custom origin server on a per-custom hostname basis <a href="https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/">via the API</a> or the UI:</p>
<p><img src="/assets/upstream/images/ssl/custom-origin-server.png" alt="Import repo or choose template" /></p>
<p>Currently <a href="https://blog.cloudflare.com/secrets-store-beta/">in beta with a Workers integration</a>, <a href="https://developers.cloudflare.com/secrets-store/">Cloudflare Secrets Store</a> allows you to store, manage, and deploy account level secrets from a secure, centralized platform your <a href="https://developers.cloudflare.com/workers/">Cloudflare Workers</a>. Now, you can create and deploy <strong>100 secrets per account</strong>. Try it out <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a>, with <a href="https://developers.cloudflare.com/secrets-store/integrations/workers/">Wrangler</a>, or <a href="https://developers.cloudflare.com/api/resources/secrets_store/">via the API</a> today.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-27">May 27, 2025</time><div>
<h2 id="post-2025-05-27-Protocol-Detection-availability"><a href="/changelog/post/2025-05-27-Protocol-Detection-availability/">Gateway Protocol Detection Now Available for Pay-as-you-go and Free Plans</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>All Cloudflare One Gateway users can now use Protocol detection logging and filtering, including those on Pay-as-you-go and Free plans.</p>
<p>With Protocol Detection, admins can identify and enforce policies on traffic proxied through Gateway based on the underlying network protocol (for example, HTTP, TLS, or SSH), enabling more granular traffic control and security visibility no matter your plan tier.</p>
<p>This feature is available to enable in your account network settings for all accounts. For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-27">May 27, 2025</time><div>
<h2 id="post-2025-05-27-waf-release"><a href="/changelog/post/2025-05-27-waf-release/">WAF Release - 2025-05-27</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup covers nine vulnerabilities, including six critical RCEs and one dangerous file upload. Affected platforms span cloud services, CI/CD pipelines, CMSs, and enterprise backup systems. Several are now addressed by updated WAF managed rulesets.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Ingress-Nginx (CVE-2025-1098): Unauthenticated RCE via unsafe annotation handling. Impacts Kubernetes clusters.</li>
<li>GitHub Actions (CVE-2025-30066): RCE through malicious workflow inputs. Targets CI/CD pipelines.</li>
<li>Craft CMS (CVE-2025-32432): Template injection enables unauthenticated RCE. High risk to content-heavy sites.</li>
<li>F5 BIG-IP (CVE-2025-31644): RCE via TMUI exploit, allowing full system compromise.</li>
<li>AJ-Report (CVE-2024-15077): RCE through untrusted template execution. Affects reporting dashboards.</li>
<li>NAKIVO Backup (CVE-2024-48248): RCE via insecure script injection. High-value target for ransomware.</li>
<li>SAP NetWeaver (CVE-2025-31324): Dangerous file upload flaw enables remote shell deployment.</li>
<li>Ivanti EPMM (CVE-2025-4428, 4427): Auth bypass allows full access to mobile device management.</li>
<li>Vercel (CVE-2025-32421): Information leak via misconfigured APIs. Useful for attacker recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical components across Kubernetes, CI/CD pipelines, and enterprise systems to severe threats including unauthenticated remote code execution, authentication bypass, and information leaks. High-impact flaws in Ingress-Nginx, Craft CMS, F5 BIG-IP, and NAKIVO Backup enable full system compromise, while SAP NetWeaver and AJ-Report allow remote shell deployment and template-based attacks. Ivanti EPMM’s auth bypass further risks unauthorized control over mobile device fleets.</p>
<p>GitHub Actions and Vercel introduce supply chain and reconnaissance risks, allowing malicious workflow inputs and data exposure that aid in targeted exploitation. Organizations should prioritize immediate patching, enhance monitoring, and deploy updated WAF and IDS signatures to defend against likely active exploitation.</p>
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
				<code class="nb-rule-id" title="6a61a14f44af4232a44e45aad127592a">d127592a</code>
</td>
<td>100746</td>
<td>Vercel - Information Disclosure</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100754</td>
<td>AJ-Report - Remote Code Execution - CVE:CVE-2024-15077</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6a13bd6e5fc94b1d9c97eb87dfee7ae4">dfee7ae4</code>
</td>
<td>100756</td>
<td>NAKIVO Backup - Remote Code Execution - CVE:CVE-2024-48248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a4af6f2f15c9483fa9eab01d1c52f6d0">1c52f6d0</code>
</td>
<td>100757</td>
<td>Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1098</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100759</td>
<td>SAP NetWeaver - Dangerous File Upload - CVE:CVE-2025-31324</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dab2df4f548349e3926fee845366ccc1">5366ccc1</code>
</td>
<td>100760</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2025-32432</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb23f172ed64ee08895e161eb40686b">eb40686b</code>
</td>
<td>100761</td>
<td>GitHub Action - Remote Code Execution - CVE:CVE-2025-30066</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="827037f2d5f941789efcba6260fc041c">60fc041c</code>
</td>
<td>100762</td>
<td>Ivanti EPMM - Auth Bypass - CVE:CVE-2025-4428, CVE:CVE-2025-4427</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ddee6d1c4f364768b324609cebafdfe6">ebafdfe6</code>
</td>
<td>100763</td>
<td>F5 Big IP - Remote Code Execution - CVE:CVE-2025-31644</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-23">May 23, 2025</time><div>
<h2 id="post-2025-05-23-graphql-api-explorer"><a href="/changelog/post/2025-05-23-graphql-api-explorer/">New GraphQL Analytics API Explorer and MCP Server</a></h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:</p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-api-explorer">GraphQL API Explorer</h4>
<p>The new <a href="https://graphql.cloudflare.com/explorer">GraphQL API Explorer</a> helps you build, test, and run queries directly in your browser. Features include:</p>
<ul>
<li>In-browser schema documentation to browse available datasets and fields</li>
<li>Interactive query editor with autocomplete and inline documentation</li>
<li>A &quot;Run in GraphQL API Explorer&quot; button to execute example queries from our docs</li>
<li>Seamless OAuth authentication — no manual setup required</li>
</ul>
<p><img src="/assets/upstream/images/changelog/analytics/graphql-api-explorer.png" alt="GraphQL API Explorer" /></p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-model-context-protocol-mcp-server">GraphQL Model Context Protocol (MCP) Server</h4>
<p>MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our <a href="https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/">blog post</a> for details on how they work and which servers are available. The new <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql">GraphQL MCP server</a> helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:</p>
<ul>
<li>Explore what data is available to query</li>
<li>Generate and refine queries using natural language, with one-click links to run them in the API Explorer</li>
<li>Build dashboards and visualizations from structured query outputs</li>
</ul>
<p>Example prompts include:</p>
<ul>
<li>“Show me HTTP traffic for the last 7 days for example.com”</li>
<li>“What GraphQL node returns firewall events?”</li>
<li>“Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”</li>
</ul>
<p>We’re continuing to expand these tools, and your feedback helps shape what’s next. <a href="/analytics/graphql-api/">Explore the documentation</a> to learn more and get started.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-22">May 22, 2025</time><div>
<h2 id="post-2025-05-22-handle-request-cancellation"><a href="/changelog/post/2025-05-22-handle-request-cancellation/">Handle incoming request cancellation in Workers with Request.signal</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>In Cloudflare Workers, you can now attach an event listener to <a href="/workers/runtime-apis/request/"><code>Request</code></a> objects, using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request/signal"><code>signal</code> property</a>. This allows you to perform tasks when the request to your Worker is canceled by the client. To use this feature, you must set the <a href="/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests"><code>enable_request_signal</code></a> compatibility flag.</p>
<p>You can use a listener to perform cleanup tasks or write to logs before your Worker's invocation ends. For example, if you run the Worker below, and then abort the request from the client, a log will be written:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17775.md")</div>
<p>For more information see the <a href="/workers/runtime-apis/request"><code>Request</code> documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-19">May 19, 2025</time><div>
<h2 id="post-2025-05-19-terraform-v5.5.0-provider"><a href="/changelog/post/2025-05-19-terraform-v5.5.0-provider/">Terraform v5.5.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_gateway_policy</code></li>
<li><code>cloudflare_zero_trust_access_application</code></li>
<li><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li><code>cloudflare_zone_setting</code></li>
<li><code>cloudflare_ruleset</code></li>
<li><code>cloudflare_page_rule</code></li>
</ul>
</li>
<li>Zone settings can be re-applied without client errors</li>
<li>Page rules conversion errors are fixed</li>
<li>Failure to apply changes to <code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0">changelog</a> in GitHub.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-issues-closed">Issues Closed</h4>
- [#5304: Importing cloudflare_zero_trust_gateway_policy invalid attribute filter value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare_page_rule import does not set values for all of the fields in terraform state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare_page_rule Page rule creation with redirect fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare_turnstile_wwidget not able to update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare_cloud_connector_rules: Provider returned invalid result object after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare_zone_setting: "Invalid value for zone setting always_use_https"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-19">May 19, 2025</time><div>
<h2 id="post-2025-05-19-waf-release"><a href="/changelog/post/2025-05-19-waf-release/">WAF Release - 2025-05-19</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in <em>Block</em> mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.</li>
<li>BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.</li>
<li>Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.</li>
<li>Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured
<code>mod_proxy</code> behavior. While not RCE, this is useful for pre-attack recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.</p>
<p>Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.</p>
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
				<code class="nb-rule-id" title="5c3559ad62994e5b932d7d0075129820">75129820</code>
</td>
<td>100745</td>
<td>Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28a22a685bba478d99bc904526a517f1">26a517f1</code>
</td>
<td>100747</td>
<td>
				Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6bb954d0634e368c49d7d1d7619ccb">d7619ccb</code>
</td>
<td>100749</td>
<td>BentoML - Remote Code Execution - CVE:CVE-2025-27520</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="91250eebec894705b62305b2f15bfda4">f15bfda4</code>
</td>
<td>100753</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2024-56145</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-18">May 18, 2025</time><div>
<h2 id="post-new-applications-71825"><a href="/changelog/post/new-applications-71825/">New Applications Added to Zero Trust</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>42 new applications have been added for Zero Trust support within the Application Library and Gateway policy enforcement, giving you the ability to investigate or apply inline policies to these applications.</p>
<p>33 of the 42 applications are Artificial Intelligence applications. The others are Human Resources (2 applications), Development (2 applications), Productivity (2 applications), Sales &amp; Marketing, Public Cloud, and Security.</p>
<p>To view all available applications, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, navigate to the <strong>App Library</strong> under <strong>My Team</strong>.</p>
<p>For more information on creating Gateway policies, see our <a href="/cloudflare-one/traffic-policies/">Gateway policy documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-16">May 16, 2025</time><div>
<h2 id="post-access-analytics-v2"><a href="/changelog/post/access-analytics-v2/">New Access Analytics in the Cloudflare One Dashboard</a></h2>
<div class="changelog-badges"><span>access</span><span>cloudflare-one</span></div><div class="changelog-body"><p>A new Access Analytics dashboard is now available to all Cloudflare One customers. Customers can apply and combine multiple filters to dive into specific slices of their Access metrics. These filters include:</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-16">May 16, 2025</time><div>
<h2 id="post-2025-05-14-python-worker-durable-object"><a href="/changelog/post/2025-05-14-python-worker-durable-object/">Durable Objects are now supported in Python Workers</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p>You can now create <a href="/durable-objects/">Durable Objects</a> using
<a href="/workers/languages/python/">Python Workers</a>. A Durable Object is a special kind of
Cloudflare Worker which uniquely combines compute with storage, enabling stateful
long-running applications which run close to your users. For more info see
<a href="/durable-objects/concepts/what-are-durable-objects/">here</a>.</p>
<p>You can define a Durable Object in Python in a similar way to JavaScript:</p>
<pre><code class="language-python">from workers import DurableObject, Response, WorkerEntrypoint&#10;&#10;from urllib.parse import urlparse&#10;&#10;class MyDurableObject(DurableObject):&#10;    def __init__(self, ctx, env):&#10;        self.ctx = ctx&#10;        self.env = env&#10;&#10;    def fetch(self, request):&#10;        result = self.ctx.storage.sql.exec(&quot;SELECT &#x27;Hello, World!&#x27; as greeting&quot;).one()&#10;        return Response(result.greeting)&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        url = urlparse(request.url)&#10;        id = env.MY_DURABLE_OBJECT.idFromName(url.path)&#10;        stub = env.MY_DURABLE_OBJECT.get(id)&#10;        greeting = await stub.fetch(request.url)&#10;        return greeting&#10;</code></pre>
<p>Define the Durable Object in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17773.md")</div>
<p>Then define the storage backend for your Durable Object:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17774.md")</div>
<p>Then test your new Durable Object locally by running <code>wrangler dev</code>:</p>
<pre><code class="language-bash">npx wrangler dev&#10;</code></pre>
<p>Consult the <a href="/durable-objects/">Durable Objects documentation</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-16">May 16, 2025</time><div>
<h2 id="post-2025-05-08-open-attachments-with-browser-isolation"><a href="/changelog/post/2025-05-08-open-attachments-with-browser-isolation/">Open email attachments with Browser Isolation</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now safely open email attachments to view and investigate them.</p>
<p>What this means is that messages now have a <strong>Attachments</strong> section. Here, you can view processed attachments and their classifications (for example, <em>Malicious</em>, <em>Suspicious</em>, <em>Encrypted</em>). Next to each attachment, a <strong>Browser Isolation</strong> icon allows your team to safely open the file in a <strong>clientless, isolated browser</strong> with no risk to the analyst or your environment.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Attachment-RBI.png" alt="Attachment-RBI" /></p>
<p>To use this feature, you must:</p>
<ul>
<li>Turn on <strong>Allow users to open a remote browser without the device client</strong> in your Zero Trust settings.</li>
<li>Have <strong>Browser Isolation (BISO)</strong> seats assigned.</li>
</ul>
<p>For more details, refer to our <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">setup guide</a>.</p>
<p>Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-14">May 14, 2025</time><div>
<h2 id="post-2025-05-14-domain-category-improvements"><a href="/changelog/post/2025-05-14-domain-category-improvements/">Domain Categories improvements</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p><strong>New categories added</strong></p>
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
<td>1</td>
<td>Ads</td>
<td>66</td>
<td>Advertisements</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>185</td>
<td>Personal Finance</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>186</td>
<td>Brokerage &amp; Investing</td>
</tr>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>187</td>
<td>Compromised Domain</td>
</tr>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>188</td>
<td>Potentially Unwanted Software</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>189</td>
<td>Reference</td>
</tr>
<tr>
<td>9</td>
<td>Government &amp; Politics</td>
<td>190</td>
<td>Charity and Non-profit</td>
</tr>
</tbody>
</table>
<p><strong>Changes to existing categories</strong></p>
<table>
<thead>
<tr>
<th>Original Name</th>
<th>New Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>Religion</td>
<td>Religion &amp; Spirituality</td>
</tr>
<tr>
<td>Government</td>
<td>Government/Legal</td>
</tr>
<tr>
<td>Redirect</td>
<td>URL Alias/Redirect</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-14">May 14, 2025</time><div>
<h2 id="post-2025-05-14-hyperdrive-fedramp"><a href="/changelog/post/2025-05-14-hyperdrive-fedramp/">Hyperdrive achieves FedRAMP Moderate-Impact Authorization</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive has been approved for FedRAMP Authorization and is now available in the <a href="https://marketplace.fedramp.gov/products/FR2000863987">FedRAMP Marketplace</a>.</p>
<p>FedRAMP is a U.S. government program that provides standardized assessment and authorization for cloud products and services. As a result of this product update,
Hyperdrive has been approved as an authorized service to be used by U.S. federal agencies at the Moderate Impact level.</p>
<p>For detailed information regarding FedRAMP and its implications, please refer to the <a href="https://marketplace.fedramp.gov/products/FR2000863987">official FedRAMP documentation for Cloudflare</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-14">May 14, 2025</time><div>
<h2 id="post-2025-05-14-media-transformations-origin-restrictions"><a href="/changelog/post/2025-05-14-media-transformations-origin-restrictions/">Introducing Origin Restrictions for Media Transformations</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>We are adding <a href="/stream/transform-videos/sources/">source origin restrictions</a> to
the Media Transformations beta. This allows customers to restrict what sources
can be used to fetch images and video for transformations. This feature is the
same as --- and uses the same settings as ---
<a href="/images/optimization/transformations/sources/">Image Transformations sources</a>.</p>
<p>When transformations is first enabled, the default setting only allows
transformations on images and media from the same website or domain being used to make
the transformation request. In other words, by default, requests to
<code>example.com/cdn-cgi/media</code> can only reference originals on <code>example.com</code>.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<p>Adding access to other sources, or allowing any source,
<a href="/images/optimization/transformations/sources/">is easy to do</a>
in the <strong>Transformations</strong> tab under <strong>Stream</strong>. Click each domain enabled for
Transformations and set its sources list to match the needs of your content. The
user making this change will need permission to edit zone settings.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-13">May 13, 2025</time><div>
<h2 id="post-2025-05-13-rbi-saml-post-support"><a href="/changelog/post/2025-05-13-rbi-saml-post-support/">SAML HTTP-POST bindings support for RBI</a></h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused <code>405</code> errors during login and improves compatibility with multi-factor authentication (MFA) flows.</p>
<p>With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to <a href="/cloudflare-one/remote-browser-isolation/setup/">set up Remote Browser Isolation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-13">May 13, 2025</time><div>
<h2 id="post-2025-05-13-new-applications-added"><a href="/changelog/post/2025-05-13-new-applications-added/">New Applications Added for DNS Filtering</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>You can now create DNS policies to manage outbound traffic for an expanded list of applications.
This update adds support for 273 new applications, giving you more control over your organization's outbound traffic.</p>
<p>With this update, you can:</p>
<ul>
<li>Create DNS policies for a wider range of applications</li>
<li>Manage outbound traffic more effectively</li>
<li>Improve your organization's security and compliance posture</li>
</ul>
<p>For more information on creating DNS policies, see our <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policy documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-12">May 12, 2025</time><div>
<h2 id="post-2025-05-12-case-sensitive-cwl"><a href="/changelog/post/2025-05-12-case-sensitive-cwl/">Case Sensitive Custom Word Lists</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now configure <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom word lists</a> to enforce case sensitivity. This setting supports flexibility where needed and aims to reduce false positives where letter casing is critical.</p>
<p><img src="/assets/upstream/images/changelog/dlp/case-sesitive-cwl.png" alt="dlp" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-09">May 9, 2025</time><div>
<h2 id="post-2025-05-09-publish-to-queues-via-http"><a href="/changelog/post/2025-05-09-publish-to-queues-via-http/">Publish messages to Queues directly via HTTP</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p>You can now publish messages to <a href="/queues/">Cloudflare Queues</a> directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within <a href="/workers/">Cloudflare Workers</a>. You can already consume from queues via Workers or <a href="/queues/configuration/pull-consumers/">HTTP pull consumers</a>, and now publishing is just as flexible.</p>
<p>Publishing via HTTP requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>Queues Edit</code> permissions for authentication. Here's a simple example:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/queues/&lt;queue_id&gt;/messages&quot; \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot;, &quot;timestamp&quot;:  &quot;2025-07-24T12:00:00Z&quot;} }&#x27;&#10;</code></pre>
<p>You can also use our <a href="/fundamentals/api/reference/sdks/">SDKs</a> for TypeScript, Python, and Go.</p>
<p>To get started with HTTP publishing, check out our <a href="/queues/examples/publish-to-a-queue-via-http/">step-by-step example</a> and the full API documentation in our <a href="/api/resources/queues/subresources/messages/methods/push/">API reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-09">May 9, 2025</time><div>
<h2 id="post-2025-05-09-snippets-cloud-connector-lists-waf-bot-scores"><a href="/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/">More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>You can now use IP, Autonomous System (AS), and Hostname <a href="/waf/tools/lists/custom-lists/">custom lists</a> to route traffic to <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a>, giving you greater precision and control over how you match and process requests at the edge.</p>
<p>In Snippets, you can now also match on <a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a>, unlocking smarter edge logic for everything from request filtering and mitigation to <a href="/rules/snippets/examples/slow-suspicious-requests/">tarpitting</a> and logging.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a> matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or <a href="/api/resources/rules/subresources/lists/methods/list/">Lists API</a>. Great for shared logic across zones.</li>
<li><a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a> – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-lists-scores.png" alt="New fields in Snippets" /></p>
<p>These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.</p>
<p>Learn more in the <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-09">May 9, 2025</time><div>
<h2 id="post-2025-05-15-open-links-browser-isolation"><a href="/changelog/post/2025-05-15-open-links-browser-isolation/">Open email links with Browser Isolation</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now safely open links in emails to view and investigate them.</p>
<p><img src="/assets/upstream/images/changelog/email-security/investigate-links.jpg" alt="Open links with Browser Isolation" /></p>
<p>From <strong>Investigation</strong>, go to <strong>View details</strong>, and look for the <strong>Links identified</strong> section. Next to each link, the Cloudflare dashboard will display an <strong>Open in Browser Isolation</strong> icon which allows your team to safely open the link in a clientless, isolated browser with no risk to the analyst or your environment. Refer to <a href="/cloudflare-one/email-security/investigation/search-email/#open-links">Open links</a> to learn more about this feature.</p>
<p>To use this feature, you must:</p>
<ul>
<li>Turn on <strong>Allow users to open a remote browser without the device client</strong> in your Zero Trust settings.</li>
<li>Have <strong>Browser Isolation (RBI)</strong> seats assigned.</li>
</ul>
<p>For more details, refer to our <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">setup guide</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-08">May 8, 2025</time><div>
<h2 id="post-2025-05-07-url-scanner-geoegress"><a href="/changelog/post/2025-05-07-url-scanner-geoegress/">URL Scanner now supports geo-specific scanning</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Enterprise customers can now choose the geographic location from which a URL scan is performed — either via <a href="/security-center/investigate/">Security Center</a> in the Cloudflare dashboard or via the <a href="/api/resources/url_scanner/subresources/scans/methods/create/">URL Scanner API</a>.</p>
<p>This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>Location Picker: Select a location for the scan via <strong>Security Center → Investigate</strong> in the dashboard or through the API.</li>
<li>Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.</li>
<li>Default behavior: If no location is set, scans default to the user’s current geographic region.</li>
</ul>
<p>Learn more in the <a href="/security-center/">Security Center documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-08">May 8, 2025</time><div>
<h2 id="post-2025-05-08-improved-payload-logging"><a href="/changelog/post/2025-05-08-improved-payload-logging/">Improved Payload Logging for WAF Managed Rules</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:</p>
<ul>
<li><strong>Targeted logging</strong>: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.</li>
<li><strong>Visual highlighting</strong>: Matched content is visually highlighted in the UI for faster identification.</li>
<li><strong>Enhanced context</strong>: Logs now include surrounding context to make diagnostics more effective.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/waf/2025-05-payload-logging-update.png" alt="Log entry showing payload logging details" /></p>
<p>Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can <a href="/waf/managed-rules/payload-logging/">get started</a>.</p>
<p><strong>Note:</strong> The structure of the <code>encrypted_matched_data</code> field in Logpush has changed from <code>Map&lt;Field, Value&gt;</code> to <code>Map&lt;Field, {Before: bytes, Content: Value, After: bytes}&gt;</code>. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/41/">Previous</a><span>Page 42 of 50</span><a class="pagination-next" rel="next" href="/changelog/43/">Next</a></nav>
</div>
