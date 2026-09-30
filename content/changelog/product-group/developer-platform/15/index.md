<h1 id="changelog">Changelog</h1>

<h2 id="new-cpu-pricing-for-containers-and-sandboxes"><a href="/changelog/post/2025-11-21-new-cpu-pricing/">New CPU Pricing for Containers and Sandboxes</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> pricing for CPU time is now based on active usage only, instead of provisioned resources.</p>
<p>This means that you now pay less for Containers and Sandboxes.</p>
<h4 id="2025-11-21-new-cpu-pricing-an-example-before-and-after">An Example Before and After</h4>
<p>Imagine running the <code>standard-2</code> instance type for one hour, which can use up to 1 vCPU,
but on average you use only 20% of your CPU capacity.</p>
<p>CPU-time is priced at <em>$0.00002 per vCPU-second</em>.</p>
<p>Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.</p>
<p>CPU cost would have been: <strong>$0.072</strong> — 1 vCPU * 3600 seconds * $0.00002</p>
<p>Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.</p>
<p>CPU cost is now: <strong>$0.0144</strong> — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization</p>
<p>This can significantly reduce costs for Containers and Sandboxes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17708.md")</aside>
<p>See the documentation to learn more about <a href="/containers/get-started/">Containers</a>, <a href="/sandbox/">Sandboxes</a>,
and <a href="/containers/platform/pricing">associated pricing</a>.</p>


<h2 id="environment-variable-limits-increase-for-workers-builds"><a href="/changelog/post/2025-11-21-builds-env-var-increase/">Environment variable limits increase for Workers Builds</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports up to 64 environment variables, and each environment variable can be up to 5 KB in size. The previous limit was 5 KB total across all environment variables.</p>
<p>This change enables better support for complex build configurations, larger application settings, and more flexible CI/CD workflows.</p>
<p>For more details, refer to the <a href="/workers/ci-cd/builds/limits-and-pricing/#definitions">build limits documentation</a>.</p>


<h2 id="better-local-deployment-flow-for-cloudflare-workers"><a href="/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/">Better local deployment flow for Cloudflare Workers</a></h2>
<p><em>2025-11-21</em></p>
<p>Until now, if a Worker had been previously deployed via the <a href="https://dash.cloudflare.com">Cloudflare Dashboard</a>, a subsequent deployment done via the Cloudflare Workers CLI, <a href="/workers/wrangler/"><strong>Wrangler</strong></a>
(through the <a href="/workers/wrangler/commands/general/#deploy"><code>deploy</code> command</a>), would allow the user to override the Worker's dashboard settings without providing details on
what dashboard settings would be lost.</p>
<p>Now instead, <code>wrangler deploy</code> presents a helpful representation of the differences between the <a href="/workers/wrangler/configuration/">local configuration</a>
and the remote dashboard settings, and offers to update your local configuration file for you.</p>
<p>See example below showing a before and after for <code>wrangler deploy</code> when a local configuration is expected to override a Worker's dashboard settings:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-11-21-wrangler-deploy-remote-config-management-before">Before</h3>
@markup("md", "content/.markup/bodies/17791.md")</div>
<div class="nb-example"><h3 class="nb-component-title" id="2025-11-21-wrangler-deploy-remote-config-management-after">After</h3>
@markup("md", "content/.markup/bodies/17792.md")</div>
<p>Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.</p>
<p>Update to <a href="/workers/wrangler/">Wrangler</a> v4.50.0 or greater to take advantage of this improved deploy flow.</p>


<h2 id="terraform-v5-13-0-now-available"><a href="/changelog/post/2025-11-20-terraform-v5.13.0-provider/">Terraform v5.13.0 now available</a></h2>
<p><em>2025-11-20</em></p>
<p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.</p>
<h4 id="2025-11-20-terraform-v5.13.0-provider-breaking-change">Breaking Change</h4>
Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.
<p>For more specific information about the changes or the actions required, please see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0">detailed Repository changelog</a>.</p>
<h4 id="2025-11-20-terraform-v5.13.0-provider-features">Features</h4>
<ul>
<li><strong>New resources and data sources added</strong>
<ul>
<li>cloudflare_connectivity_directory</li>
<li>cloudflare_sso_connector</li>
<li>cloudflare_universal_ssl_setting</li>
</ul>
</li>
<li><strong>api_token+account_tokens:</strong> state upgrader and schema bump (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6472">#6472</a>)</li>
<li><strong>docs:</strong> make docs explicit when a resource does not have import support</li>
<li><strong>magic_transit_connector:</strong> support self-serve license key (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6398">#6398</a>)</li>
<li><strong>worker_version:</strong> add content_base64 support</li>
<li><strong>worker_version:</strong> boolean support for run_worker_first (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6407">#6407</a>)</li>
<li><strong>workers_script_subdomains:</strong> add import support  (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6375">#6375</a>)</li>
<li><strong>zero_trust_access_application:</strong> add proxy_endpoint for ZT Access Application (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6453">#6453</a>)</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> Switch DLP Predefined Profile endpoints, introduce enabled_entries attribute</li>
</ul>
<h4 id="2025-11-20-terraform-v5.13.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_token:</strong> token policy order and nested resources (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6440">#6440</a>)</li>
<li>allow r2_bucket_event_notification to be applied twice without failing (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6419">#6419</a>)</li>
<li><strong>cloudflare_worker+cloudflare_worker_version:</strong> import for the resources (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6357">#6357</a>)</li>
<li><strong>dns_record:</strong> inconsistent apply error (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6452">#6452</a>)</li>
<li><strong>pages_domain:</strong> resource tests (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6338">#6338</a>)</li>
<li><strong>pages_project:</strong> unintended resource state drift (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6377">#6377</a>)</li>
<li><strong>queue_consumer:</strong> id population (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6181">#6181</a>)</li>
<li><strong>workers_kv:</strong> multipart request  (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6367">#6367</a>)</li>
<li><strong>workers_kv:</strong> updating workers metadata attribute to be read from endpoint (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6386">#6386</a>)</li>
<li><strong>workers_script_subdomain:</strong> add note to cloudflare_workers_script_subdomain about redundancy with cloudflare_worker (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6383">#6383</a>)</li>
<li><strong>workers_script:</strong> allow config.run_worker_first to accept list input</li>
<li><strong>zero_trust_device_custom_profile_local_domain_fallback:</strong> drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6365">#6365</a>)</li>
<li><strong>zero_trust_device_custom_profile:</strong> resolve drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6364">#6364</a>)</li>
<li><strong>zero_trust_dex_test:</strong> correct configurability for 'targeted' attribute to fix drift</li>
<li><strong>zero_trust_tunnel_cloudflared_config:</strong> remove warp_routing from cloudflared_config (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6471">#6471</a>)</li>
</ul>
<h4 id="2025-11-20-terraform-v5.13.0-provider-upgrading">Upgrading</h4>
We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-11-20-terraform-v5.13.0-provider-for-more-info">For more info</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)


<h2 id="ai-search-support-for-crawling-login-protected-website-content"><a href="/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/">AI Search support for crawling login protected website content</a></h2>
<p><em>2025-11-19</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/authentication-headers/">custom HTTP headers</a> for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.</p>
<p>Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.</p>
<p>This is particularly useful for indexing content like:</p>
<ul>
<li><strong>Internal documentation</strong> behind corporate login systems</li>
<li><strong>Premium content</strong> that requires users to provide access to unlock</li>
<li><strong>Sites protected by Cloudflare Access</strong> using service tokens</li>
</ul>
<p>To add custom headers when creating an AI Search instance, select <strong>Parse options</strong>. In the <strong>Extra headers</strong> section, you can add up to five custom headers per Website data source.</p>
<p><img src="/assets/upstream/images/ai-search/ai-search-extra-headers.png" alt="Custom headers configuration in AI Search" /></p>
<p>For example, to crawl a site protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>, you can add service token credentials as custom headers:</p>
<pre><code>CF-Access-Client-Id: your-token-id.access&#10;CF-Access-Client-Secret: your-token-secret&#10;</code></pre>
<p>The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.</p>
<p>Learn more about <a href="/ai-search/configuration/data-source/website/authentication-headers/">configuring custom headers for website crawling</a> in AI Search.</p>


<h2 id="more-sql-aggregate-date-and-time-functions-available-in-workers-analytics-engine"><a href="/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/">More SQL aggregate, date and time functions available in Workers Analytics Engine</a></h2>
<p><em>2025-11-12</em></p>
<p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>countIf()</code> - count the number of rows which satisfy a provided condition</li>
<li><code>sumIf()</code> - calculate a sum from rows which satisfy a provided condition</li>
<li><code>avgIf()</code> - calculate an average from rows which satisfy a provided condition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/"><strong>New date and time functions:</strong></a></p>
<ul>
<li><code>toYear()</code></li>
<li><code>toMonth()</code></li>
<li><code>toDayOfMonth()</code></li>
<li><code>toDayOfWeek()</code></li>
<li><code>toHour()</code></li>
<li><code>toMinute()</code></li>
<li><code>toSecond()</code></li>
<li><code>toStartOfYear()</code></li>
<li><code>toStartOfMonth()</code></li>
<li><code>toStartOfWeek()</code></li>
<li><code>toStartOfDay()</code></li>
<li><code>toStartOfHour()</code></li>
<li><code>toStartOfFifteenMinutes()</code></li>
<li><code>toStartOfTenMinutes()</code></li>
<li><code>toStartOfFiveMinutes()</code></li>
<li><code>toStartOfMinute()</code></li>
<li><code>today()</code></li>
<li><code>toYYYYMM()</code></li>
</ul>
<h4 id="2025-11-12-analytics-engine-further-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).


<h2 id="cloudflared-proxy-dns-command-will-be-removed-starting-february-2-2026"><a href="/changelog/post/2025-11-11-cloudflared-proxy-dns/">cloudflared proxy-dns command will be removed starting February 2, 2026</a></h2>
<p><em>2025-11-11</em></p>
<p>Starting February 2, 2026, the <code>cloudflared proxy-dns</code> command will be removed from all new <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">releases</a>.</p>
<p>This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the <code>proxy-dns</code> command and does not affect any other <code>cloudflared</code> features, such as the core <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> service.</p>
<p>The <code>proxy-dns</code> command, which runs a client-side <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS (DoH)</a> proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.</p>
<p>Versions of <code>cloudflared</code> released before this date will not be affected and will continue to operate. However, note that our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases">official support policy</a> for any <code>cloudflared</code> release is one year from its release date.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-migration-paths">Migration paths</h4>
<p>We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-end-user-devices">End-user devices</h4>
<p>The preferred method for enabling DNS-over-HTTPS on user devices is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare WARP client</a>. The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's <a href="/cloudflare-one/traffic-policies/">Zero Trust policies</a> and <a href="/cloudflare-one/reusable-components/posture-checks/">posture checks</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-servers-routers-and-iot-devices">Servers, routers, and IoT devices</h4>
<p>For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the <a href="/mesh/">WARP Connector</a>.</p>
<p>Instead of running <code>cloudflared proxy-dns</code> on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your <a href="/mesh/features/routes/">entire subnet</a> to Cloudflare for <a href="/cloudflare-one/traffic-policies/">filtering and logging</a>.</p>


<h2 id="select-wrangler-environments-using-the-cloudflare-env-environment-variable"><a href="/changelog/post/2025-11-09-cloudflare-env-variable/">Select Wrangler environments using the CLOUDFLARE_ENV environment variable</a></h2>
<p><em>2025-11-09</em></p>
<p>Wrangler now supports using the <code>CLOUDFLARE_ENV</code> <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables">environment variable</a> to select the active <a href="/workers/wrangler/environments/">environment</a> for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.</p>
<h4 id="2025-11-09-cloudflare-env-variable-what-s-new">What's new</h4>
<p><strong>Environment selection via environment variable:</strong></p>
<ul>
<li>Set <code>CLOUDFLARE_ENV</code> to specify which environment to use for Wrangler commands</li>
<li>Works with all Wrangler commands that support the <code>--env</code> flag</li>
<li>The <code>--env</code> command line argument takes precedence over the <code>CLOUDFLARE_ENV</code> environment variable</li>
</ul>
<h4 id="2025-11-09-cloudflare-env-variable-example-usage">Example usage</h4>
<pre><code class="language-bash">&#35; Deploy to the production environment using CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=production wrangler deploy&#10;&#10;&#35; Upload a version to the staging environment&#10;CLOUDFLARE_ENV=staging wrangler versions upload&#10;&#10;&#35; The --env flag takes precedence over CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=dev wrangler deploy --env production&#10;&#35; This will deploy to production, not dev&#10;</code></pre>
<h4 id="2025-11-09-cloudflare-env-variable-use-with-build-tools">Use with build tools</h4>
<p>The <code>CLOUDFLARE_ENV</code> environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:</p>
<pre><code class="language-bash">&#35; Set the environment for both build and deploy&#10;CLOUDFLARE_ENV=production npm run build &amp; wrangler deploy&#10;</code></pre>
<p>When using <code>@cloudflare/vite-plugin</code>, the build process generates a <a href="/workers/wrangler/configuration/#generated-wrangler-configuration">&quot;redirected deploy config&quot;</a> that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.</p>
<h4 id="2025-11-09-cloudflare-env-variable-learn-more">Learn more</h4>
<ul>
<li><a href="/workers/wrangler/system-environment-variables/">System environment variables</a></li>
<li><a href="/workers/wrangler/environments/">Environments</a></li>
</ul>


<h2 id="workers-automatic-tracing-now-in-open-beta"><a href="/changelog/post/2025-11-07-automatic-tracing/">Workers automatic tracing, now in open beta</a></h2>
<p><em>2025-11-07</em></p>
<p>Enable automatic tracing on your Workers, giving you detailed metadata and timing information for every operation your Worker performs.</p>
<p><img src="/assets/upstream/images/workers-observability/R2_Screenshot.png" alt="Tracing example" /></p>
<p>Tracing helps you identify performance bottlenecks, resolve errors, and understand how your Worker interacts with other services on the Workers platform. You can now answer questions like:</p>
<ul>
<li>Which calls are slowing down my application?</li>
<li>Which queries to my database take the longest?</li>
<li>What happened within a request that resulted in an error?</li>
</ul>
<p><strong>You can now:</strong></p>
<ul>
<li>View traces alongside your logs in the Workers Observability dashboard</li>
<li>Export traces (and correlated logs) to any <a href="https://opentelemetry.io/docs/specs/otel/protocol/">OTLP-compatible destination</a>, such as <a href="/workers/observability/exporting-opentelemetry-data/honeycomb/">Honeycomb</a>, <a href="/workers/observability/exporting-opentelemetry-data/sentry/">Sentry</a> or <a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/">Grafana</a>, by configuring a tracing destination in the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/destinations">Cloudflare dashboard</a></li>
<li>Analyze and query across span attributes (operation type, status, duration, errors)</li>
</ul>
<h4 id="2025-11-07-automatic-tracing-to-get-started-set">To get started, set:</h4>
<pre><code class="language-jsonc">{&#10;	&quot;observability&quot;: {&#10;		&quot;traces&quot;: {&#10;			&quot;enabled&quot;: true,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17790.md")</aside>
<h4 id="2025-11-07-automatic-tracing-want-to-learn-more">Want to learn more?</h4>
<ul>
<li><a href="https://blog.cloudflare.com/workers-tracing-now-in-open-beta/">Read the announcement</a></li>
<li><a href="/workers/observability/traces/">Check out the documentation</a></li>
</ul>


<h2 id="d1-can-restrict-data-localization-with-jurisdictions"><a href="/changelog/post/2025-11-05-d1-jurisdiction/">D1 can restrict data localization with jurisdictions</a></h2>
<p><em>2025-11-05</em></p>
<p>You can now set a <a href="/d1/configuration/data-location/">jurisdiction</a> when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include <code>eu</code> and <code>fedramp</code>.</p>
<p>A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.</p>
<pre><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu&#10;</code></pre>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<p>To learn more, visit D1's data location <a href="/d1/configuration/data-location/">documentation</a>.</p>


<h2 id="announcing-workers-vpc-services-beta"><a href="/changelog/post/2025-09-25-workers-vpc/">Announcing Workers VPC Services (Beta)</a></h2>
<p><em>2025-11-05</em></p>
<p><strong>Workers VPC Services</strong> is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.</p>
<h4 id="2025-09-25-workers-vpc-what-s-new">What's new</h4>
<ul>
<li><strong>VPC Services</strong>: Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax</li>
<li><strong>Multi-cloud Support</strong>: Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels</li>
</ul>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Perform application logic in Workers here&#10;&#10;		// Sample call to an internal API running on ECS in AWS using the binding&#10;		const response = await env.AWS_VPC_ECS_API.fetch(&quot;https://internal-host.example.com&quot;);&#10;&#10;		// Additional application logic in Workers&#10;		return new Response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-25-workers-vpc-getting-started">Getting started</h4>
<p>Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. <a href="/workers-vpc/">Refer to the documentation</a> to get started.</p>


<h2 id="capture-wrangler-command-output-in-structured-format"><a href="/changelog/post/2025-11-03-wrangler-output-file/">Capture Wrangler command output in structured format</a></h2>
<p><em>2025-11-03</em></p>
<p>You can now capture Wrangler command output in a structured <a href="https://github.com/ndjson/ndjson-spec">ND-JSON</a> format by setting the <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_OUTPUT_FILE_PATH</code></a> or <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_OUTPUT_FILE_DIRECTORY</code></a> environment variables. This feature is particularly useful for CI/CD pipelines and automation tools that need programmatic access to deployment information such as worker names, version IDs, deployment URLs, and error details. Commands that support this feature include <a href="/workers/wrangler/commands/#deploy"><code>wrangler deploy</code></a>, <a href="/workers/wrangler/commands/#versions"><code>wrangler versions upload</code></a>, <a href="/workers/wrangler/commands/#versions"><code>wrangler versions deploy</code></a>, and <a href="/workers/wrangler/commands/#deploy-1"><code>wrangler pages deploy</code></a>.</p>


<h2 id="workers-websocket-message-size-limit-increased-from-1-mib-to-32-mib"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<p><em>2025-10-31</em></p>
<p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>


<h2 id="increased-workflows-instance-and-concurrency-limits"><a href="/changelog/post/2025-10-28-raising-limits/">Increased Workflows instance and concurrency limits</a></h2>
<p><em>2025-10-31</em></p>
<p>We've raised the <a href="/workflows/">Cloudflare Workflows</a> account-level limits for all accounts on the <a href="/workers/platform/pricing/">Workers paid plan</a>:</p>
<ul>
<li><strong>Instance creation rate</strong> increased from 100 workflow instances per 10 seconds to 100 instances per second</li>
<li><strong>Concurrency limit</strong> increased from 4,500 to 10,000 workflow instances per account</li>
</ul>
<p>These increases mean you can create new instances up to 10x faster, and have more workflow instances concurrently executing. To learn more and get started with Workflows, refer to <a href="/workflows/get-started/guide/">the getting started guide</a>.</p>
<p>If your application requires a higher limit, fill out the <a href="/workers/platform/limits/">Limit Increase Request Form</a> or contact your account team. Please refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> for more information.</p>


<h2 id="access-workers-preview-urls-from-the-build-details-page"><a href="/changelog/post/2025-10-30-builds-preview/">Access Workers preview URLs from the Build details page</a></h2>
<p><em>2025-10-30</em></p>
<p>You can now access <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> directly from the build details page, making it easier to test your changes when reviewing builds in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/builds-preview-button.png" alt="preview button" /></p>
<p><strong>What's new</strong></p>
<ul>
<li>A <strong>Preview</strong> button now appears in the top-right corner of the build details page for successful builds</li>
<li>Click it to instantly open the latest preview URL</li>
<li>Matches the same experience you're familiar with from Pages</li>
</ul>


<h2 id="reranking-and-api-based-system-prompt-configuration-in-ai-search"><a href="/changelog/post/2025-10-27-ai-search-reranking-system-prompt/">Reranking and API-based system prompt configuration in AI Search</a></h2>
<p><em>2025-10-28</em></p>
<p><a href="/ai-search/">AI Search</a> now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.</p>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-rerank-for-more-relevant-results">Rerank for more relevant results</h4>
<p>You can now enable <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.</p>
<p>You can enable and configure reranking in the dashboard or directly in your API requests:</p>
<pre><code class="language-javascript">const answer = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-set-system-prompts-in-api">Set system prompts in API</h4>
<p>Previously, <a href="/ai-search/configuration/retrieval/system-prompt/">system prompts</a> could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:</p>
<pre><code class="language-javascript">// Dynamically set query and system prompt in AI Search&#10;async function getAnswer(query, tone) {&#10;	const systemPrompt = `You are a ${tone} assistant.`;&#10;&#10;	const response = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;		query: query,&#10;		system_prompt: systemPrompt,&#10;	});&#10;&#10;	return response;&#10;}&#10;&#10;// Example usage&#10;const query = &quot;What is Cloudflare?&quot;;&#10;const tone = &quot;friendly&quot;;&#10;&#10;const answer = await getAnswer(query, tone);&#10;console.log(answer);&#10;</code></pre>
<p>Learn more about <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> and <a href="/ai-search/configuration/retrieval/system-prompt/">System Prompt</a> in AI Search.</p>


<h2 id="automatic-resource-provisioning-for-kv-r2-and-d1"><a href="/changelog/post/2025-10-24-automatic-resource-provisioning/">Automatic resource provisioning for KV, R2, and D1</a></h2>
<p><em>2025-10-24</em></p>
<p>Previously, if you wanted to develop or deploy a worker with attached resources, you'd have to first manually create the desired resources. Now, if your Wrangler configuration file includes a KV namespace, D1 database, or R2 bucket that does not yet exist on your account, you can develop locally and deploy your application seamlessly, without having to run additional commands.</p>
<p>Automatic provisioning is launching as an open beta, and we'd love to hear your feedback to help us make improvements! It currently works for KV, R2, and D1 bindings. You can disable the feature using the <code>--no-x-provision</code> flag.</p>
<p>To use this feature, update to wrangler@4.45.0 and add bindings to your config file <em>without</em> resource IDs e.g.:</p>
<pre><code class="language-jsonc">{&#10;	&quot;kv_namespaces&quot;: [{ &quot;binding&quot;: &quot;MY_KV&quot; }],&#10;	&quot;d1_databases&quot;: [{ &quot;binding&quot;: &quot;MY_DB&quot; }],&#10;	&quot;r2_buckets&quot;: [{ &quot;binding&quot;: &quot;MY_R2&quot; }],&#10;}&#10;</code></pre>
<p><code>wrangler dev</code> will then automatically create these resources for you locally, and on your next run of <code>wrangler deploy</code>, Wrangler will call the Cloudflare API to create the requested resources and link them to your Worker.</p>
<p>Though resource IDs will be automatically written back to your Wrangler config file after resource creation, resources will stay linked across future deploys even without adding the resource IDs to the config file. This is especially useful for shared templates, which now no longer need to include account-specific resource IDs when adding a binding.</p>


<h2 id="build-tanstack-start-apps-with-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-10-24-tanstack-start/">Build TanStack Start apps with the Cloudflare Vite plugin</a></h2>
<p><em>2025-10-24</em></p>
<p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> now supports <a href="https://tanstack.com/start/">TanStack Start</a> apps.
Get started with new or existing projects.</p>
<h4 id="2025-10-24-tanstack-start-new-projects">New projects</h4>
<p>Create a new TanStack Start project that uses the Cloudflare Vite plugin via the <code>create-cloudflare</code> CLI:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2025-10-24-tanstack-start-existing-projects">Existing projects</h4>
<p>Migrate an existing TanStack Start project to use the Cloudflare Vite plugin:</p>
<ol>
<li>Install <code>@cloudflare/vite-plugin</code> and <code>wrangler</code></li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Add the Cloudflare plugin to your Vite config</li>
</ol>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import viteReact from &quot;@vitejs/plugin-react&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;		tanstackStart(),&#10;		viteReact(),&#10;	],&#10;});&#10;</code></pre>
<ol start="3">
<li>Add your Worker config file</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17789.md")</div>
<ol start="4">
<li>Modify the scripts in your <code>package.json</code></li>
</ol>
<pre><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;vite dev&quot;,&#10;		&quot;build&quot;: &quot;vite build &amp;&amp; tsc --noEmit&quot;,&#10;		&quot;start&quot;: &quot;node .output/server/index.mjs&quot;,&#10;		&quot;preview&quot;: &quot;vite preview&quot;,&#10;		&quot;deploy&quot;: &quot;npm run build &amp;&amp; wrangler deploy&quot;,&#10;		&quot;cf-typegen&quot;: &quot;wrangler types&quot;&#10;	}&#10;}&#10;</code></pre>
<p>See the <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start framework guide</a> for more info.</p>


<h2 id="workers-preview-url-default-behavior-now-matches-your-workers-dev-setting"><a href="/changelog/post/2025-10-23-preview-url-default-behavior/">Workers Preview URL default behavior now matches your workers.dev setting</a></h2>
<p><em>2025-10-23</em></p>
<p>We have updated the default behavior for Cloudflare Workers <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>. <strong>Going forward, if a preview URL setting is not <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">explicitly configured</a> during deployment, its default behavior will automatically match the setting of your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a>.</strong></p>
<p>This change is intended to provide a more intuitive and secure experience by aligning your preview URL's default state with your <code>workers.dev</code> configuration to prevent cases where a preview URL might remain public even after you disabled your <code>workers.dev</code> route.</p>
<p><strong>What this means for you:</strong></p>
<ul>
<li><strong>If neither setting is configured:</strong> both the workers.dev route and the preview URL will default to enabled</li>
<li><strong>If your workers.dev route is enabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to enabled</li>
<li><strong>If your workers.dev route is disabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to disabled</li>
</ul>
<p>You can override the default setting by explicitly enabling or disabling the preview URL in your Worker's configuration through the <a href="/api/resources/workers/subresources/scripts/subresources/subdomain/">API</a>, <a href="/workers/versions-and-deployments/preview-urls/#from-the-dashboard">Dashboard</a>, or <a href="/workers/versions-and-deployments/preview-urls/#from-the-wrangler-configuration-file">Wrangler</a>.</p>
<p><strong>Wrangler Version Behavior</strong></p>
<p>The default behavior depends on the version of Wrangler you are using. This new logic applies to the latest version. Here is a summary of the behavior across different versions:</p>
<ul>
<li><strong>Before v4.34.0:</strong> Preview URLs defaulted to enabled, regardless of the workers.dev setting.</li>
<li><strong>v4.34.0 up to (but not including) v4.44.0:</strong> Preview URLs defaulted to disabled, regardless of the workers.dev setting.</li>
<li><strong>v4.44.0 or later:</strong> Preview URLs now default to matching your workers.dev setting.</li>
</ul>
<p><strong>Why we’re making this change</strong></p>
<p>In July, <a href="/changelog/2025-07-23-workers-preview-urls/">we introduced preview URLs to Workers</a>, which let you preview code changes before deploying to production. This made disabling your Worker’s workers.dev URL an ambiguous action — the preview URL, served as a subdomain of <code>workers.dev</code> (ex: <code>preview-id-worker-name.account-name.workers.dev</code>) would still be live even if you had disabled your Worker’s <code>workers.dev</code> route. If you misinterpreted what it meant to disable your <code>workers.dev</code> route, you might unintentionally leave preview URLs enabled when you didn’t mean to, and expose them to the public Internet.</p>
<p>To address this, we made a <a href="/changelog/2025-09-17-update-preview-url-setting/">one-time update</a> to disable preview URLs on existing Workers that had their workers.dev route disabled and changed the default behavior to be disabled for all new deployments where a preview URL setting was not explicitly configured.</p>
<p>While this change helped secure many customers, it was disruptive for customers who keep their <code>workers.dev</code> route enabled and actively use the preview functionality, as it now required them to explicitly enable preview URLs on every redeployment.This new, more intuitive behavior ensures that your preview URL settings align with your <code>workers.dev</code> configuration by default, providing a more secure and predictable experience.</p>
<p><strong>Securing access to <code>workers.dev</code> and preview URL endpoints</strong></p>
<p>To further secure your <code>workers.dev</code> subdomain and preview URL, you can <a href="/changelog/2025-10-03-one-click-access-for-workers/">enable Cloudflare Access with a single click</a> in your Worker's settings to limit access to specific users or groups.</p>


<h2 id="workers-ai-markdown-conversion-new-endpoint-to-list-supported-formats"><a href="/changelog/post/2025-10-23-new-markdown-conversion-endpoint/">Workers AI Markdown Conversion: New endpoint to list supported formats</a></h2>
<p><em>2025-10-23</em></p>
<p>Developers can now programmatically retrieve a list of all file formats supported by the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a> in Workers AI.</p>
<p>You can use the <a href="/workers-ai/configuration/bindings/"><code>env.AI</code></a> binding:</p>
<pre><code class="language-typescript">await env.AI.toMarkdown().supported()&#10;</code></pre>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<p>Both return a list of file formats that users can convert into Markdown:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;extension&quot;: &quot;.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;	},&#10;	{&#10;		&quot;extension&quot;: &quot;.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;	},&#10;	...&#10;]&#10;</code></pre>
<p>Learn more about our <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a>.</p>


<h2 id="view-and-edit-durable-object-data-in-ui-with-data-studio-beta"><a href="/changelog/post/2025-10-16-durable-objects-data-studio/">View and edit Durable Object data in UI with Data Studio (Beta)</a></h2>
<p><em>2025-10-16</em></p>
<p><img src="/assets/upstream/images/workers/changelog/do-data-studio.png" alt="Screenshot of Durable Objects Data Studio" /></p>
<p>You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage</a> can use Data Studio.</p>
<div class="nb-dash-button"></div>
<p>Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.</p>
<p>To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the <code>Workers Platform Admin</code> role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.</p>
<p>To learn more, visit the Data Studio <a href="/durable-objects/observability/data-studio/">documentation</a>. If you have feedback or suggestions for the new Data Studio, please share your experience on <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord</a></p>


<h2 id="worker-startup-time-limit-increased-to-1-second"><a href="/changelog/post/2025-10-10-increased-startup-time/">Worker startup time limit increased to 1 second</a></h2>
<p><em>2025-10-10</em></p>
<p>You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.</p>
<p>This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.</p>
<p>For more information, see the documentation on <a href="/workers/platform/limits/#worker-startup-time">Workers startup limits</a>.</p>


<h2 id="you-can-now-deploy-full-stack-apps-on-workers-using-terraform"><a href="/changelog/post/2025-10-09-assets-terraform/">You can now deploy full-stack apps on Workers using Terraform</a></h2>
<p><em>2025-10-09</em></p>
<p>You can now upload Workers with <a href="/workers/static-assets/">static assets</a> (like HTML, CSS, JavaScript, images) with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs">Cloudflare Terraform provider v5.11.0</a>, making it even easier to deploy and manage full-stack apps with IaC.</p>
<p><strong>Previously</strong>, you couldn't use Terraform to upload static assets without writing custom scripts to handle generating an <a href="/workers/static-assets/direct-upload/#upload-manifest">asset manifest</a>, calling the <a href="/workers/static-assets/direct-upload/#upload-static-assets">Cloudflare API to upload assets in chunks</a>, and handling change detection.</p>
<p><strong>Now</strong>, you simply define the directory where your assets are built, and we handle the rest. Check out the <a href="/changelog/#examples">examples</a> for what this looks like in Terraform configuration.</p>
<p>You can get started today with <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs">the Cloudflare Terraform provider (v5.11.0)</a>, using either the existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code> resource</a>, or the beta <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version"><code>cloudflare_worker_version</code> resource</a>.</p>
<h4 id="2025-10-09-assets-terraform-examples">Examples</h4>
<h4 id="2025-10-09-assets-terraform-with-cloudflare-workers-script">With <code>cloudflare_workers_script</code></h4>
<p>Here's how you can use the existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource to upload your Worker code and assets in one shot.</p>
<pre><code class="language-hcl">resource &quot;cloudflare_workers_script&quot; &quot;my_app&quot; {&#10;  account_id  = var.account_id&#10;  script_name = &quot;my-app&quot;&#10;&#10;  content_file   = &quot;./dist/worker/index.js&quot;&#10;  content_sha256 = filesha256(&quot;./dist/worker/index.js&quot;)&#10;  main_module    = &quot;index.js&quot;&#10;&#10;  &#35; Just point to your assets directory - that&#x27;s it!&#10;  assets = {&#10;    directory = &quot;./dist/static&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-10-09-assets-terraform-with-cloudflare-worker-cloudflare-worker-version-and-cloudflare-workers-deployment">With <code>cloudflare_worker</code>, <code>cloudflare_worker_version</code>, and <code>cloudflare_workers_deployment</code></h4>
<p>And here's an example using the beta <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version"><code>cloudflare_worker_version</code></a> resource, alongside the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker"><code>cloudflare_worker</code></a> and <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment"><code>cloudflare_workers_deployment</code></a> resources:</p>
<pre><code class="language-hcl">&#10;&#35; This tracks the existence of your Worker, so that you&#10;&#35; can upload code and assets separately from tracking Worker state.&#10;&#10;resource &quot;cloudflare_worker&quot; &quot;my_app&quot; {&#10;  account_id = var.account_id&#10;  name       = &quot;my-app&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;my_app_version&quot; {&#10;  account_id = var.account_id&#10;  worker_id  = cloudflare_worker.my_app.id&#10;&#10;  &#35; Just point to your assets directory - that&#x27;s it!&#10;  assets = {&#10;    directory = &quot;./dist/static&quot;&#10;  }&#10;&#10;  modules = [{&#10;    name         = &quot;index.js&quot;&#10;    content_file = &quot;./dist/worker/index.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;my_app_deployment&quot; {&#10;  account_id  = var.account_id&#10;  script_name = cloudflare_worker.my_app.name&#10;&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    version_id = cloudflare_worker_version.my_app_version.id&#10;    percentage = 100&#10;  }]&#10;}&#10;</code></pre>
<h4 id="2025-10-09-assets-terraform-what-s-changed">What's changed</h4>
Under the hood, the Cloudflare Terraform provider now handles the same logic that Wrangler uses for static asset uploads. This includes scanning your assets directory, computing hashes for each file, generating a manifest with file metadata, and calling the Cloudflare API to upload any missing files in chunks. We support large directories with parallel uploads and chunking, and when the asset manifest hash changes, we detect what's changed and trigger an upload for *only* those changed files.
<h4 id="2025-10-09-assets-terraform-try-it-out">Try it out</h4>
-  Get started with [the Cloudflare Terraform provider (v5.11.0)](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs)
- You can use either the existing [`cloudflare_workers_script` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) to upload your Worker code and assets in one resource.
- Or you can use the new beta [`cloudflare_worker_version` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version) (along with the [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment)) resources to more granularly control the lifecycle of each Worker resource.


<h2 id="you-can-now-deploy-and-manage-workflows-in-terraform"><a href="/changelog/post/2025-10-09-workflows-terraform/">You can now deploy and manage Workflows in Terraform</a></h2>
<p><em>2025-10-09</em></p>
<p>You can now create and manage <a href="/workflows/">Workflows</a> using Terraform, now supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow">Cloudflare Terraform provider v5.11.0</a>. Workflows allow you to build durable, multi-step applications -- without needing to worry about retrying failed tasks or managing infrastructure.</p>
<p>Now, you can deploy and manage Workflows through Terraform using the new <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow"><code>cloudflare_workflow</code> resource</a>:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_workflow&quot; &quot;my_workflow&quot; {&#10;  account_id    = var.account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = &quot;my-worker&quot;&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-examples">Examples</h4>
Here are full examples of how to configure `cloudflare_workflow` in Terraform, using the existing [`cloudflare_workers_script` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), and the beta [`cloudflare_worker_version` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).
<h4 id="2025-10-09-workflows-terraform-with-cloudflare-workflow-and-cloudflare-workers-script">With <code>cloudflare_workflow</code> and <code>cloudflare_workers_script</code></h4>
<pre><code class="language-hcl">resource &quot;cloudflare_workers_script&quot; &quot;workflow_worker&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  script_name = &quot;my-workflow-worker&quot;&#10;&#10;  content_file   = &quot;${path.module}/../dist/worker/index.js&quot;&#10;  content_sha256 = filesha256(&quot;${path.module}/../dist/worker/index.js&quot;)&#10;  main_module    = &quot;index.js&quot;&#10;}&#10;&#10;resource &quot;cloudflare_workflow&quot; &quot;workflow&quot; {&#10;  account_id    = var.cloudflare_account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = cloudflare_workers_script.workflow_worker.script_name&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-with-cloudflare-workflow-and-the-new-beta-resources">With <code>cloudflare_workflow</code>, and the new beta resources</h4>
You can more granularly control the lifecycle of each Worker resource using the beta [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources.
<pre><code class="language-hcl">&#10;resource &quot;cloudflare_worker&quot; &quot;workflow_worker&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my-workflow-worker&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;workflow_worker_version&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  worker_id  = cloudflare_worker.workflow_worker.id&#10;&#10;  main_module         = &quot;index.js&quot;&#10;&#10;  modules = [{&#10;    name         = &quot;index.js&quot;&#10;    content_file = &quot;${path.module}/../dist/worker/index.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;workflow_deployment&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  script_name = cloudflare_worker.workflow_worker.name&#10;&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    version_id = cloudflare_worker_version.workflow_worker_version.id&#10;    percentage = 100&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workflow&quot; &quot;my_workflow&quot; {&#10;  account_id    = var.cloudflare_account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = cloudflare_worker.workflow_worker.name&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-try-it-out">Try it out</h4>
-  Get started with [the Cloudflare Terraform provider (v5.11.0)](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs) and the new [`cloudflare_workflow` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow).


<h2 id="new-overview-page-for-cloudflare-workers"><a href="/changelog/post/2025-10-06-new-worker-overview-page/">New Overview Page for Cloudflare Workers</a></h2>
<p><em>2025-10-07</em></p>
<p><img src="/assets/upstream/images/workers/changelog/workers-overview.png" alt="Screenshot of the Workers overview page in the Cloudflare dashboard" /></p>
<p>Each of your Workers now has a new overview page in the Cloudflare dashboard.</p>
<p>The goal is to make it easier to understand your Worker without digging through multiple tabs. Think of it as a new home base, a place to get a high-level overview on what's going on.</p>
<p>It's the first place you land when you open a Worker in the dashboard, and it gives you an immediate view of what’s going on. You can see requests, errors, and CPU time at a glance. You can view and add bindings, and see recent versions of your app, including who published them.</p>
<p>Navigation is also simpler, with visually distinct tabs at the top of the page. At the bottom right you'll find guided steps for what to do next that are based on the state of your Worker, such as adding a <a href="/workers/runtime-apis/bindings/">binding</a> or connecting a custom domain.</p>
<p>We plan to add more here over time. Better insights, more controls, and ways to manage your Worker from one page.</p>
<p>If you have feedback or suggestions for the new Overview page or your Cloudflare Workers experience in general, we'd love to hear from you. Join the Cloudflare developer community on <a href="https://discord.com/channels/595317990191398933/1064502845061210152">Discord</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/14/">Previous</a><span>Page 15 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/16/">Next</a></nav>
