<h1 id="changelog">Changelog</h1>

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


<h2 id="account-level-dns-analytics-now-available-via-graphql-analytics-api"><a href="/changelog/post/2025-06-23-account-level-dns-analytics-api/">Account-level DNS analytics now available via GraphQL Analytics API</a></h2>
<p><em>2025-06-19</em></p>
<p>Authoritative DNS analytics are now available on the <strong>account level</strong> via the <a href="/analytics/graphql-api/">Cloudflare GraphQL Analytics API</a>.</p>
<p>This allows users to query DNS analytics across multiple zones in their account, by using the <code>accounts</code> filter.</p>
<p>Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an <code>NXDOMAIN</code> response over a given time frame. Please replace <code>a30f822fcd7c401984bf85d8f2a5111c</code> with your actual account ID.</p>
<pre><code class="language-graphql">query GetLatestNXDOMAINResponses {&#10;	viewer {&#10;		accounts(filter: { accountTag: &quot;a30f822fcd7c401984bf85d8f2a5111c&quot; }) {&#10;			dnsAnalyticsAdaptive(&#10;				filter: {&#10;					date_geq: &quot;2025-06-16&quot;&#10;					date_leq: &quot;2025-06-18&quot;&#10;					responseCode: &quot;NXDOMAIN&quot;&#10;				}&#10;				limit: 10000&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				zoneTag&#10;				queryName&#10;				responseCode&#10;				queryType&#10;				datetime&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To learn more and get started, refer to the <a href="/dns/additional-options/analytics/#analytics">DNS Analytics documentation</a>.</p>


<h2 id="internal-dns-beta-now-manageable-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-06-16-internal-dns-beta-ui/">Internal DNS (beta) now manageable in the Cloudflare dashboard</a></h2>
<p><em>2025-06-16</em></p>
<p>Participating beta testers can now fully configure <a href="/dns/internal-dns/">Internal DNS</a> directly in the <a href="https://dash.cloudflare.com/?to=/:account/internal-dns">Cloudflare dashboard</a>.</p>
<h4 id="2025-06-16-internal-dns-beta-ui-internal-dns-enables-customers-to">Internal DNS enables customers to:</h4>
<ul>
<li>
<p>Map internal hostnames to private IPs for services, devices, and applications not exposed to the public Internet</p>
</li>
<li>
<p>Resolve internal DNS queries securely through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a></p>
</li>
<li>
<p>Use split-horizon DNS to return different responses based on network context</p>
</li>
<li>
<p>Consolidate internal and public DNS zones within a single management platform</p>
</li>
</ul>
<h4 id="2025-06-16-internal-dns-beta-ui-what-s-new-in-this-release">What’s new in this release:</h4>
<ul>
<li>Beta participants can now create and manage internal zones and views in the Cloudflare dashboard</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/internal-dns-beta-ui.png" alt="Internal DNS UI" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17716.md")</aside>
<p>To learn more and get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="nsec3-support-for-dnssec"><a href="/changelog/post/2025-06-11-nsec3-support/">NSEC3 support for DNSSEC</a></h2>
<p><em>2025-06-11</em></p>
<p>Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>NSEC3 support for live-signed zones</strong> – For both primary and secondary zones that are configured to be live-signed (also known as &quot;on-the-fly signing&quot;), NSEC3 can now be selected as proof of non-existence.</p>
</li>
<li>
<p><strong>NSEC3 support for pre-signed zones</strong> – Secondary zones that are transferred to Cloudflare in a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">pre-signed setup</a> now also support NSEC3 as proof of non-existence.</p>
</li>
</ul>
<p>For more information and how to enable NSEC3, refer to the <a href="/dns/dnssec/enable-nsec3/">NSEC3 documentation</a>.</p>


<h2 id="more-flexible-fallback-handling-custom-errors-now-support-fetching-assets-returned-with-4xx-or-5xx-status-codes"><a href="/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/">More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</a></h2>
<p><em>2025-06-09</em></p>
<p><a href="/rules/custom-errors/">Custom Errors</a> can now fetch and store <a href="/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard">assets</a> and <a href="/rules/custom-errors/#error-pages">error pages</a> from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.</li>
<li>These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.</li>
</ul>
<p>This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.</p>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors</a> documentation.</p>


<h2 id="match-workers-subrequests-by-upstream-zone-cf-worker-upstream-zone-now-supported-in-transform-rules"><a href="/changelog/post/2025-06-09-transform-rule-subrequest-matching/">Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules</a></h2>
<p><em>2025-06-09</em></p>
<p>You can now use the <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field in <a href="/rules/transform/">Transform Rules</a> to control rule execution based on whether a request originates from <a href="/workers/">Workers</a>, including subrequests issued by Workers in other zones.</p>
<p><img src="/assets/upstream/images/changelog/rules/transform-rule-subrequest-matching.png" alt="Match Workers subrequests by upstream zone in Transform Rules" /></p>
<p><strong>What's new:</strong></p>
<ul>
<li><code>cf.worker.upstream_zone</code> is now supported in Transform Rules expressions.</li>
<li>Skip or apply logic conditionally when handling <a href="/workers/platform/limits/#subrequests">Workers subrequests</a>.</li>
</ul>
<p>For example, to add a header when the subrequest comes from another zone:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-06-09-transform-rule-subrequest-matching-example">Example</h3>
@markup("md", "content/.markup/bodies/17746.md")</div>
<p>This gives you more granular control in how you handle incoming requests for your zone.</p>
<p>Learn more in the <a href="/rules/transform/">Transform Rules</a> documentation and <a href="/ruleset-engine/rules-language/fields/reference/">Rules language fields</a> reference.</p>


<h2 id="new-account-level-load-balancing-ui-and-private-load-balancers"><a href="/changelog/post/2025-06-04-account-load-balancing-ui/">New Account-Level Load Balancing UI and Private Load Balancers</a></h2>
<p><em>2025-06-04</em></p>
<p>We've made two large changes to load balancing:</p>
<ul>
<li>Redesigned the user interface, now centralized at the <strong>account level</strong>.</li>
<li>Introduced <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.</li>
</ul>
<p>This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/account-load-balancing-ui.png" alt="Load Balancing UI" /></p>
<p><strong>Key Enhancements:</strong></p>
<ul>
<li>
<p><strong>Account-Level UI Consolidation:</strong></p>
<ul>
<li>
<p><strong>Unified Management:</strong> Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.</p>
</li>
<li>
<p><strong>Improved Efficiency:</strong> This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.</p>
</li>
</ul>
</li>
<li>
<p><strong>Private Network Load Balancing:</strong></p>
<ul>
<li>
<p><strong>Secure Internal Application Access:</strong> Create <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.</p>
</li>
<li>
<p><strong>WARP &amp; Magic WAN Integration:</strong> Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.</p>
</li>
<li>
<p><strong>Enhanced Security for Internal Resources:</strong> Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.</p>
</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/load-balancing/private-load-balancer.png" alt="Private Load Balancers" /></p>


<h2 id="improved-onboarding-for-shopify-merchants"><a href="/changelog/post/2025-06-03-shopify-o2o-improvements/">Improved onboarding for Shopify merchants</a></h2>
<p><em>2025-06-03</em></p>
<p>Shopify merchants can now onboard to <strong>O2O</strong> automatically, without needing to contact support or community members.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>Automatic enablement</strong> – O2O is available for all mutual Cloudflare and Shopify customers.</p>
</li>
<li>
<p><strong>Branded record display</strong> – Merchants see a Shopify logo in DNS records, complete with helpful tooltips.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/shop-dns-icon-o2o.png" alt="Shopify O2O logo" /></p>
<ul>
<li><strong>Checkout protection</strong> – Workers and Snippets are blocked from running on the checkout path to reduce risk and improve security.</li>
</ul>
<p>For more information, refer to the <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/">provider guide</a>.</p>


<h2 id="fine-tune-image-optimization-webp-now-supported-in-configuration-rules"><a href="/changelog/post/2025-05-30-configuration-rules-webp/">Fine-tune image optimization — WebP now supported in Configuration Rules</a></h2>
<p><em>2025-05-30</em></p>
<p>You can now enable <a href="/images/polish/activate-polish/">Polish</a> with the <code>webp</code> format directly in <a href="/rules/configuration-rules/">Configuration Rules</a>, allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/images/polish/compression/#webp">WebP</a> is now a supported <a href="/rules/configuration-rules/settings/#polish">value</a> in the <strong>Polish</strong> setting for Configuration Rules.</li>
</ul>
<p>This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.</p>
<p>Learn more in the <a href="/images/polish/">Polish</a> and <a href="/rules/configuration-rules/">Configuration Rules</a> documentation.</p>


<h2 id="increased-limits-for-cloudflare-for-saas-and-secrets-store-free-and-pay-as-you-go-plans"><a href="/changelog/post/2025-05-19-paygo-updates/">Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</a></h2>
<p><em>2025-05-27T11:00:00+00:00</em></p>
<p>With upgraded limits to <a href="https://www.cloudflare.com/plans/">all free and paid plans</a>, you can now scale more easily with <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> and <a href="https://developers.cloudflare.com/secrets-store/">Secrets Store</a>.</p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/">limit for custom hostnames</a> on a Cloudflare for SaaS Pay-as-you-go plan has been <strong>raised from 5,000 custom hostnames to 50,000 custom hostnames.</strong></p>
<p>With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">Custom origin server</a> is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.</p>
<p>You can enable custom origin server on a per-custom hostname basis <a href="https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/">via the API</a> or the UI:</p>
<p><img src="/assets/upstream/images/ssl/custom-origin-server.png" alt="Import repo or choose template" /></p>
<p>Currently <a href="https://blog.cloudflare.com/secrets-store-beta/">in beta with a Workers integration</a>, <a href="https://developers.cloudflare.com/secrets-store/">Cloudflare Secrets Store</a> allows you to store, manage, and deploy account level secrets from a secure, centralized platform your <a href="https://developers.cloudflare.com/workers/">Cloudflare Workers</a>. Now, you can create and deploy <strong>100 secrets per account</strong>. Try it out <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a>, with <a href="https://developers.cloudflare.com/secrets-store/integrations/workers/">Wrangler</a>, or <a href="https://developers.cloudflare.com/api/resources/secrets_store/">via the API</a> today.</p>


<h2 id="more-ways-to-match-snippets-now-support-custom-lists-bot-score-and-waf-attack-score"><a href="/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/">More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</a></h2>
<p><em>2025-05-09</em></p>
<p>You can now use IP, Autonomous System (AS), and Hostname <a href="/waf/tools/lists/custom-lists/">custom lists</a> to route traffic to <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a>, giving you greater precision and control over how you match and process requests at the edge.</p>
<p>In Snippets, you can now also match on <a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a>, unlocking smarter edge logic for everything from request filtering and mitigation to <a href="/rules/snippets/examples/slow-suspicious-requests/">tarpitting</a> and logging.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a> matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or <a href="/api/resources/rules/subresources/lists/methods/list/">Lists API</a>. Great for shared logic across zones.</li>
<li><a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a> – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-lists-scores.png" alt="New fields in Snippets" /></p>
<p>These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.</p>
<p>Learn more in the <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="udp-and-icmp-monitor-support-for-private-load-balancing-endpoints"><a href="/changelog/post/2025-05-06-private-health-monitoring-methods/">UDP and ICMP Monitor Support for Private Load Balancing Endpoints</a></h2>
<p><em>2025-05-06</em></p>
<p>Cloudflare Load Balancing now supports <strong>UDP (Layer 4)</strong> and <strong>ICMP (Layer 3)</strong> health monitors for <strong>private endpoints</strong>. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.</p>
<h4 id="2025-05-06-private-health-monitoring-methods-what-you-can-do">What you can do:</h4>
<ul>
<li>Set up <strong>ICMP ping monitors</strong> to check if your private endpoints are reachable.</li>
<li>Use <strong>UDP monitors</strong> for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.</li>
<li>Gain better visibility and uptime guarantees for services running behind <strong>Private Network Load Balancing</strong>, without requiring public IP addresses.</li>
</ul>
<p>This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/"><strong>Cloudflare Tunnel</strong></a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/"><strong>WARP</strong></a>, and <a href="/cloudflare-wan/"><strong>Magic WAN</strong></a> to create a secure and observable private network.</p>
<p>Learn more about <a href="/load-balancing/private-network/">Private Network Load Balancing</a> or view the full list of <a href="/load-balancing/monitors/#supported-protocols">supported health monitor protocols</a>.</p>


<h2 id="custom-errors-are-now-generally-available"><a href="/changelog/post/2025-04-24-custom-errors-ga/">Custom Errors are now Generally Available</a></h2>
<p><em>2025-04-24</em></p>
<p><a href="/rules/custom-errors/">Custom Errors</a> are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.</p>
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


<h2 id="cloudflare-snippets-are-now-generally-available"><a href="/changelog/post/2025-04-09-snippets-ga/">Cloudflare Snippets are now Generally Available</a></h2>
<p><em>2025-04-09</em></p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga.png" alt="Cloudflare Snippets are now GA" /></p>
<p><a href="/rules/snippets/">Cloudflare Snippets</a> are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.</p>
<p>You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.</p>
<p>What's new:</p>
<ul>
<li><strong>Snippets are now GA</strong> – Available at no extra cost on all Pro, Business, and Enterprise plans.</li>
<li><strong>Ready for production</strong> – Snippets deliver a production-grade experience built for scale.</li>
<li><strong>Part of the Cloudflare Rules platform</strong> – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.</li>
<li><strong>Trace integration</strong> – Use <a href="/rules/trace-request/">Cloudflare Trace</a> to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga-trace.gif" alt="Snippets shown in Cloudflare Trace results" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/snippets/">launch blog post</a>.</p>


<h2 id="cloudflare-secrets-store-now-available-in-beta"><a href="/changelog/post/2025-04-09-secrets-store-beta/">Cloudflare Secrets Store now available in Beta</a></h2>
<p><em>2025-04-09</em></p>
<p>Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.</p>
<p><img src="/assets/upstream/images/ssl/secrets-store-landing-page.png" alt="Import repo or choose template" /></p>
<p>To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a> or use this Wrangler command:</p>
<pre><code class="language-sh">wrangler secrets-store store create &lt;name&gt; --remote&#10;</code></pre>
<p>The following are supported in the Secrets Store beta:</p>
<ul>
<li>Secrets Store UI &amp; API: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Workers UI: bind a new or existing account level secret to a Worker and deploy in code</li>
<li>Wrangler: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Account Management UI &amp; API: assign Secrets Store permissions roles &amp; view audit logs for actions taken in Secrets Store core platform</li>
</ul>
<p>For instructions on how to get started, visit our <a href="/secrets-store/">developer documentation</a>.</p>


<h2 id="workers-fetch-api-can-override-cache-rules"><a href="/changelog/post/2025-04-04-workers-fetch-api-override-cache-rules/">Workers Fetch API can override Cache Rules</a></h2>
<p><em>2025-04-04</em></p>
<p>You can now programmatically override Cache Rules using the <code>cf</code> object in the <code>fetch()</code> command. This feature gives you fine-grained control over caching behavior on a per-request basis, allowing Workers to customize cache settings dynamically based on request properties, user context, or business logic.</p>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-how-it-works">How it works</h4>
<p>Using the <code>cf</code> object in <code>fetch()</code>, you can override specific Cache Rules settings by:</p>
<ol>
<li><strong>Setting custom cache options</strong>: Pass cache properties in the <code>cf</code> object as the second argument to <code>fetch()</code> to override default Cache Rules.</li>
<li><strong>Dynamic cache control</strong>: Apply different caching strategies based on request headers, cookies, or other runtime conditions.</li>
<li><strong>Per-request customization</strong>: Bypass or modify Cache Rules for individual requests while maintaining default behavior for others.</li>
<li><strong>Programmatic cache management</strong>: Implement complex caching logic that adapts to your application's needs.</li>
</ol>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-what-can-be-configured">What can be configured</h4>
<p>Workers can override the following Cache Rules settings through the <code>cf</code> object:</p>
<ul>
<li><strong><code>cacheEverything</code></strong>: Treat all content as static and cache all file types beyond the default cached content.</li>
<li><strong><code>cacheTtl</code></strong>: Set custom time-to-live values in seconds for cached content at the edge, regardless of origin headers.</li>
<li><strong><code>cacheTtlByStatus</code></strong>: Set different TTLs based on the response status code (for example, <code>{ &quot;200-299&quot;: 86400, 404: 1, &quot;500-599&quot;: 0 }</code>).</li>
<li><strong><code>cacheKey</code></strong>: Customize cache keys to control which requests are treated as the same for caching purposes (Enterprise only).</li>
<li><strong><code>cacheTags</code></strong>: Append additional cache tags for targeted cache purging operations.</li>
</ul>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-benefits">Benefits</h4>
<ul>
<li><strong>Enhanced flexibility</strong>: Customize cache behavior without modifying zone-level Cache Rules.</li>
<li><strong>Dynamic optimization</strong>: Adjust caching strategies in real-time based on request context.</li>
<li><strong>Simplified configuration</strong>: Reduce the number of Cache Rules needed by handling edge cases programmatically.</li>
<li><strong>Improved performance</strong>: Fine-tune cache behavior for specific use cases to maximize hit rates.</li>
</ul>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-get-started">Get started</h4>
<p>To get started, refer to the <a href="/workers/runtime-apis/fetch/">Workers Fetch API documentation</a> and the <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties">cf object properties documentation</a>.</p>


<h2 id="all-cache-purge-methods-now-available-for-all-plans"><a href="/changelog/post/2025-04-01-purge-for-all/">All cache purge methods now available for all plans</a></h2>
<p><em>2025-04-03</em></p>
<p>You can now access all Cloudflare cache purge methods — no matter which plan you’re on. Whether you need to update a single asset or instantly invalidate large portions of your site’s content, you now have the same powerful tools previously reserved for Enterprise customers.</p>
<p><strong>Anyone on Cloudflare can now:</strong></p>
<ol>
<li><a href="/cache/how-to/purge-cache/purge-everything/">Purge Everything</a>: Clears all cached content associated with a website.</li>
<li><a href="/cache/how-to/purge-cache/purge_by_prefix/">Purge by Prefix</a>: Targets URLs sharing a common prefix.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-hostname/">Purge by Hostname</a>: Invalidates content by specific hostnames.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-single-file/">Purge by URL (single-file purge)</a>: Precisely targets individual URLs.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-tags/">Purge by Tag</a>: Uses Cache-Tag response headers to invalidate grouped assets, offering flexibility for complex cache management scenarios.</li>
</ol>
<p>Want to learn how each purge method works, when to use them, or what limits apply to your plan? Dive into our <a href="/cache/how-to/purge-cache/">purge cache documentation</a> and <a href="https://developers.cloudflare.com/api/resources/cache/methods/purge/">API reference</a> for all the details.</p>


<h2 id="zaraz-moves-to-the-tag-management-category-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-02-24-zaraz-dash-placement/">Zaraz moves to the “Tag Management” category in the Cloudflare dashboard</a></h2>
<p><em>2025-02-24</em></p>
<p><img src="/assets/upstream/images/zaraz/zaraz-account-level.jpg" alt="Zaraz at zone level to Tag management at account level" /></p>
<p>Previously, you could only configure Zaraz by going to each individual zone under your Cloudflare account. Now, if you’d like to get started with Zaraz or manage your existing configuration, you can navigate to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Management</a> section on the Cloudflare dashboard – this will make it easier to compare and configure the same settings across multiple zones.</p>
<p>These changes will not alter any existing configuration or entitlements for zones you already have Zaraz enabled on. If you’d like to edit existing configurations, you can go to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Setup</a> section of the dashboard, and select the zone you'd like to edit.</p>


<h2 id="upload-a-certificate-bundle-with-an-rsa-and-ecdsa-certificate-per-custom-hostname"><a href="/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/">Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname</a></h2>
<p><em>2025-02-14</em></p>
<p>Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.</p>
<p>Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.</p>
<pre><code>curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;d &#x27;{&#10;    &quot;hostname&quot;: &quot;hostname&quot;,&#10;    &quot;ssl&quot;: {&#10;        &quot;custom_cert_bundle&quot;: [&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;RSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;RSA Key&quot;&#10;            },&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;ECDSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;ECDSA Key&quot;&#10;            }&#10;        ],&#10;        &quot;bundle_method&quot;: &quot;force&quot;,&#10;        &quot;wildcard&quot;: false,&#10;        &quot;settings&quot;: {&#10;            &quot;min_tls_version&quot;: &quot;1.0&quot;&#10;        }&#10;    }&#10;}’&#10;</code></pre>
<p>You can also:</p>
<ul>
<li>
<p><a href="/api/resources/custom_hostnames/methods/create/">Upload</a> an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/">Replace</a> the RSA or ECDSA certificate with a certificate of its same type.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/">Delete</a> the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).</p>
</li>
</ul>
<p>This feature is available for Business and Enterprise customers who have purchased custom certificates.</p>


<h2 id="configurable-multiplexing-http-2-to-origin"><a href="/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/">Configurable multiplexing HTTP/2 to Origin</a></h2>
<p><em>2025-02-12</em></p>
<p>You can now configure HTTP/2 multiplexing settings for origin connections on Enterprise plans. This feature allows you to optimize how Cloudflare manages concurrent requests over HTTP/2 connections to your origin servers, improving cache efficiency and reducing connection overhead.</p>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-how-it-works">How it works</h4>
<p>HTTP/2 multiplexing allows multiple requests to be sent over a single TCP connection. With this configuration option, you can:</p>
<ol>
<li><strong>Control concurrent streams</strong>: Adjust the maximum number of concurrent streams per connection.</li>
<li><strong>Optimize connection reuse</strong>: Fine-tune connection pooling behavior for your origin infrastructure.</li>
<li><strong>Reduce connection overhead</strong>: Minimize the number of TCP connections required between Cloudflare and your origin.</li>
<li><strong>Improve cache performance</strong>: Better connection management can enhance cache fetch efficiency.</li>
</ol>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-benefits">Benefits</h4>
<ul>
<li><strong>Customizable performance</strong>: Tailor multiplexing settings to your origin's capabilities.</li>
<li><strong>Reduced latency</strong>: Fewer connection handshakes improve response times.</li>
<li><strong>Lower origin load</strong>: More efficient connection usage reduces server resource consumption.</li>
<li><strong>Enhanced scalability</strong>: Better connection management supports higher traffic volumes.</li>
</ul>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-get-started">Get started</h4>
<p>Enterprise customers can configure HTTP/2 multiplexing settings in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> or through our <a href="/api/">API</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-configurable-multiplexing-http2-to-origin-important-consideration">Important consideration</h4>
@markup("md", "content/.markup/bodies/17703.md")</aside>


<h2 id="increased-cloudflare-rules-limits"><a href="/changelog/post/2025-02-12-rules-upgraded-limits/">Increased Cloudflare Rules limits</a></h2>
<p><em>2025-02-12</em></p>
<p>We have upgraded and streamlined <a href="/rules/">Cloudflare Rules</a> limits across all plans, simplifying rule management and improving scalability for everyone.</p>
<p><strong>New limits by product:</strong></p>
<ul>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>
<ul>
<li>Free: <strong>20</strong> → <strong>10,000</strong> URL redirects across lists</li>
<li>Pro: <strong>500</strong> → <strong>25,000</strong> URL redirects across lists</li>
<li>Business: <strong>500</strong> → <strong>50,000</strong> URL redirects across lists</li>
<li>Enterprise: <strong>10,000</strong> → <strong>1,000,000</strong> URL redirects across lists</li>
</ul>
</li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a>
<ul>
<li>Free: <strong>5</strong> → <strong>10</strong> connectors</li>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> connectors</li>
</ul>
</li>
<li><a href="/rules/custom-errors/">Custom Errors</a>
<ul>
<li>Pro: <strong>5</strong> → <strong>25</strong> error assets and rules</li>
<li>Business: <strong>20</strong> → <strong>50</strong> error assets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> error assets and rules</li>
</ul>
</li>
<li><a href="/rules/snippets/">Snippets</a>
<ul>
<li>Pro: <strong>10</strong> → <strong>25</strong> code snippets and rules</li>
<li>Business: <strong>25</strong> → <strong>50</strong> code snippets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> code snippets and rules</li>
</ul>
</li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a>, <a href="/rules/configuration-rules/">Configuration Rules</a>, <a href="/rules/compression-rules/">Compression Rules</a>, <a href="/rules/origin-rules/">Origin Rules</a>, <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, and <a href="/rules/transform/">Transform Rules</a>
<ul>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> rules</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-rules-upgraded-limits-gradual-rollout">Gradual rollout</h4>
@markup("md", "content/.markup/bodies/17745.md")</aside>


<h2 id="custom-errors-beta-stored-assets-account-level-rules"><a href="/changelog/post/2025-02-11-custom-errors-beta/">Custom Errors (beta): Stored Assets & Account-level Rules</a></h2>
<p><em>2025-02-11</em></p>
<p>We're introducing <a href="/rules/custom-errors/">Custom Errors</a> (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.</p>
<p>This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.</p>
<p>This brings the following new capabilities:</p>
<ul>
<li><strong>Custom error assets</strong> – Fetch and store external error pages at the edge for use in error responses.</li>
<li><strong>Account-Level custom errors</strong> – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.</li>
</ul>
<p>You can use Cloudflare API to upload your existing assets for use with Custom Errors:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;maintenance&quot;,&#10;  &quot;description&quot;: &quot;Maintenance template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<p>You can then reference the stored asset in a Custom Error rule:</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;		{&#10;			&quot;action&quot;: &quot;serve_error&quot;,&#10;			&quot;action_parameters&quot;: {&#10;				&quot;asset_name&quot;: &quot;maintenance&quot;,&#10;				&quot;content_type&quot;: &quot;text/html&quot;,&#10;				&quot;status_code&quot;: 503&#10;			},&#10;			&quot;enabled&quot;: true,&#10;			&quot;expression&quot;: &quot;http.request.uri.path contains \&quot;error\&quot;&quot;&#10;		}&#10;	]&#10;}&#x27;&#10;</code></pre>


<h2 id="fight-csam-more-easily-than-ever"><a href="/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/">Fight CSAM More Easily Than Ever</a></h2>
<p><em>2025-02-04</em></p>
<p>You can now implement our <strong>child safety tooling</strong>, the <strong><a href="/cache/reference/csam-scanning/">CSAM Scanning Tool</a></strong>, more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.</p>
<p><strong>How It Works</strong></p>
<p>When enabled, the tool automatically <a href="https://blog.cloudflare.com/the-csam-scanning-tool/">hashes images for enabled websites as they enter the Cloudflare cache</a>. These hashes are then checked against a database of <strong>known abusive images</strong>.</p>
<ul>
<li><strong>Potential match detected?</strong>
<ul>
<li>The <strong>content URL is blocked</strong>, and</li>
<li><strong>Cloudflare will notify you</strong> about the found matches via the provided email address.</li>
</ul>
</li>
</ul>
<p><strong>Updated Service-Specific Terms</strong></p>
<p>We have also made updates to our <strong><a href="https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms">Service-Specific Terms</a></strong> to reflect these changes.</p>


<h2 id="removed-unused-meta-fields-from-dns-records"><a href="/changelog/post/2025-02-02-removed-meta-fields/">Removed unused meta fields from DNS records</a></h2>
<p><em>2025-02-02</em></p>
<p>Cloudflare is removing five fields from the <code>meta</code> object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.</p>
<p>The affected fields are:</p>
<ul>
<li>the <code>auto_added</code> boolean</li>
<li>the <code>managed_by_apps</code> boolean and corresponding <code>apps_install_id</code></li>
<li>the <code>managed_by_argo_tunnel</code> boolean and corresponding <code>argo_tunnel_id</code></li>
</ul>
<p>An example record returned from the API would now look like the following:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;www.example.com&quot;,&#10;		&quot;type&quot;: &quot;A&quot;,&#10;		&quot;content&quot;: &quot;192.0.2.1&quot;,&#10;		&quot;proxiable&quot;: true,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;meta&quot;: {&#10;			&quot;auto_added&quot;: false,&#10;			&quot;managed_by_apps&quot;: false,&#10;			&quot;managed_by_argo_tunnel&quot;: false,&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>For more guidance, refer to <a href="/dns/manage-dns-records/">Manage DNS records</a>.</p>


<h2 id="new-snippets-code-editor"><a href="/changelog/post/2025-01-29-snippets-code-editor/">New Snippets Code Editor</a></h2>
<p><em>2025-01-29</em></p>
<p>The new <a href="/rules/snippets/">Snippets</a> code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.</p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-new-editor.png" alt="New Snippets code editor" /></p>
<p>What’s new:</p>
<ul>
<li><strong>Single-page editing for code and rule</strong> – No need to jump between screens.</li>
<li><strong>Auto-complete &amp; syntax highlighting</strong> – Get suggestions and avoid mistakes.</li>
<li><strong>Code formatting &amp; refactoring</strong> – Write cleaner, more readable code.</li>
</ul>
<p>Try it now in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets">Rules &gt; Snippets</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-performance/2/">Previous</a><span>Page 3 of 4</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-performance/4/">Next</a></nav>
