<h1 id="changelog">Changelog</h1>

<h2 id="shadowed-record-warnings-are-now-available-for-all-zones"><a href="/changelog/post/2026-09-14-shadowed-record-warnings/">Shadowed record warnings are now available for all zones</a></h2>
<p><em>2026-09-14</em></p>
<p>Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.</p>
<p>Shadow metadata is also available in DNS records API responses when you set <code>include_shadow_metadata=true</code>. The metadata identifies the delegating <code>NS</code> records and, when applicable, whether an <code>A</code> or <code>AAAA</code> record is glue. For more information, refer to <a href="/dns/manage-dns-records/reference/shadowed-records/">Shadowed records</a>.</p>


<h2 id="configure-origin-range-requests-with-the-rulesets-api"><a href="/changelog/post/2026-09-02-origin-range-requests-rulesets-api/">Configure Origin Range Requests with the Rulesets API</a></h2>
<p><em>2026-09-02</em></p>
<p>The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.</p>
<p>Set <code>origin_range_requests.mode</code> to <code>on</code>, <code>off</code>, or <code>default</code> for any traffic matched by a Cache Rule.</p>
<p>To override Cloudflare's default Origin Range Requests behavior, set the mode to <code>off</code>. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:</p>
<pre><code class="language-json">{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;set_cache_settings&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;origin_range_requests&quot;: {&#10;      &quot;mode&quot;: &quot;off&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores <code>Range</code> and returns a complete <code>200 OK</code>, Cloudflare can use the response but must download the complete file. Origins should honor <code>Accept-Encoding: identity</code> and return consistent, unencoded partial responses.</p>
<p>For configuration details and mode behavior, refer to <a href="/cache/how-to/cache-rules/settings/#origin-range-requests">Origin Range Requests in Cache Rules</a>. For client responses and the complete origin contract, refer to <a href="/cache/reference/range-requests/">Range request behavior</a>.</p>


<h2 id="load-balancing-now-supports-pool-sets"><a href="/changelog/post/2026-08-31-pool-sets/">Load Balancing now supports pool sets</a></h2>
<p><em>2026-08-31</em></p>
<p>Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.</p>
<p>Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.</p>
<p>For example, this pool set uses Dynamic Latency steering for traffic from Germany:</p>
<pre><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;germany-lowest-latency&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;DE&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;0930eec54a4c7ae6616985b79f678210&quot;,&#10;					&quot;c8b4f5a6d7e84910a2b3c4d5e6f70819&quot;&#10;				],&#10;				&quot;steering_policy&quot;: &quot;dynamic_latency&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.</p>
<p>For configuration details and more examples, refer to <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">Pool sets</a>.</p>


<h2 id="apo-caches-more-crawler-and-bot-traffic-again"><a href="/changelog/post/2026-08-27-accept-header-caching/">APO caches more crawler and bot traffic again</a></h2>
<p><em>2026-08-27</em></p>
<p>We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit <code>Accept: text/html</code> header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (<code>cf-cache-status: DYNAMIC</code>) instead of the cache.</p>
<p>APO now caches these requests again. No action is needed. If you added a Transform Rule to set <code>Accept: text/html</code> as a workaround, you can remove it.</p>
<p>For details on how APO decides what to cache, refer to <a href="/automatic-platform-optimization/about/">About APO</a>.</p>


<h2 id="web-analytics-improves-soft-navigation-measurement-for-single-page-applications-spas"><a href="/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/">Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. <strong>Update: this update is complete as of 2026-09-04.</strong></p>
<p><strong>This change may alter the volume of reported pageviews and visits in the dashboard and GraphQL API. The reported Largest Contentful Paint (LCP) metric may also fluctuate.</strong> The extent of these variances depend on your front-end architecture and visitor traffic patterns.</p>
<p>Single Page Applications (SPAs)—such as websites built with React, Angular, Vue, or Svelte—predominantly use soft navigations. Soft navigations avoid fully unloading the current page and rendering the next one from scratch as visitors navigate.</p>
<p>Any client-side navigation counts as a soft navigation, including navigations intercepted by <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or triggered by <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">the History API</a>. This means a non-SPA website can have soft navigation activity if its implementation uses these APIs.</p>
<p>The main improvement comes from <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">Google Chrome's new Soft Navigation API</a>. It natively measures <a href="/web-analytics/data-metrics/core-web-vitals/#core-web-vitals-metrics">Largest Contentful Paint (LCP)</a> on soft navigations, removing a blind spot in perceived loading speed across pageviews.</p>
<p>We've extended our <code>navigationType</code> values to segment these different types of navigations:</p>
<table>
<thead>
<tr>
<th><code>navigationType</code></th>
<th>New?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>navigate</code></td>
<td>❌</td>
<td>Hard navigations that traditional websites (or &quot;Multi Page Applications&quot;) perform when clicking links or submitting forms</td>
</tr>
<tr>
<td><code>soft-navigation</code></td>
<td>✅</td>
<td>Where <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">the new Soft Navigation API</a> is available and a visitor makes a client-side navigation, we record these events</td>
</tr>
<tr>
<td><code>routing-apis</code></td>
<td>✅</td>
<td>Where the native Soft Navigation API is unavailable (e.g. Safari, Firefox, older Chromium-based browsers), we fallback to measuring soft navigations using <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">History API</a>. We cannot collect LCP for these, but the other Core Web Vitals are present.</td>
</tr>
</tbody>
</table>
<p>Prior to this change, we only used History API and all navigations were bucketed into <code>navigate</code>.</p>
<p>For more information, refer to the <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a> and <a href="/web-analytics/get-started/web-analytics-spa/">Web Analytics SPA</a> documentation pages.</p>


<h2 id="load-balancing-analytics-now-filters-by-pool-name"><a href="/changelog/post/2026-08-17-pool-name-analytics-filter/">Load balancing analytics now filters by pool name</a></h2>
<p><em>2026-08-17</em></p>
<p>Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.</p>
<p>Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.</p>
<p>The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:</p>
<ul>
<li><strong>Requests over time</strong>, filtering the chart series to the selected pool.</li>
<li><strong>Pool distribution</strong>, showing only the selected pool segment.</li>
<li><strong>Top endpoints</strong>, displaying cards for origins in the selected pool.</li>
<li><strong>Latency</strong>, showing latency data for the selected pool.</li>
</ul>
<p>The <strong>Logs</strong> view and health event filtering are unchanged.</p>
<p>To use this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same pool filter appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>For more information about analytics filters and metrics, refer to <a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a>.</p>


<h2 id="oracle-cloud-infrastructure-object-storage-support-in-cloud-connector"><a href="/changelog/post/2026-08-13-oci-object-storage-cloud-connector/">Oracle Cloud Infrastructure Object Storage support in Cloud Connector</a></h2>
<p><em>2026-08-13</em></p>
<p>Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.</p>
<p>OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional <code>oraclecloud.com</code> and dedicated <code>customer-oci.com</code> path-style endpoints.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-08-13-oci-object-storage-cloud-connector-public-buckets-only">Public buckets only</h4>
@markup("md", "content/.markup/bodies/17751.md")</aside>
<h4 id="2026-08-13-oci-object-storage-cloud-connector-api-example">API example</h4>
<p>Set <code>provider</code> to <code>oci_storage</code> and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:</p>
<pre><code class="language-json">{&#10;	&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/assets/*\&quot;&quot;,&#10;	&quot;provider&quot;: &quot;oci_storage&quot;,&#10;	&quot;description&quot;: &quot;Route assets to OCI Object Storage&quot;,&#10;	&quot;enabled&quot;: true,&#10;	&quot;parameters&quot;: {&#10;		&quot;host&quot;: &quot;&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For endpoint formats and bucket requirements, refer to <a href="/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage">Supported cloud providers in Cloud Connector</a>.</p>


<h2 id="certificate-transparency-monitoring-is-now-generally-available"><a href="/changelog/post/2026-08-13-ct-monitoring-ga/">Certificate Transparency Monitoring is now Generally Available</a></h2>
<p><em>2026-08-13</em></p>
<p>Certificate Transparency Monitoring is now <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">generally available</a> across all Cloudflare plans.</p>
<p>Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.</p>
<p>Learn more in the <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">launch blog post</a> or the <a href="/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">CT Monitoring docs</a>.</p>


<h2 id="load-balancing-health-notifications-now-resolve-automatically"><a href="/changelog/post/2026-08-07-stateful-health-notifications/">Load Balancing health notifications now resolve automatically</a></h2>
<p><em>2026-08-07</em></p>
<p><a href="/load-balancing/">Load Balancing</a> health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.</p>
<p>As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.</p>
<p>This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by <a href="/health-checks/">Health Checks</a> notifications.</p>
<p>Two things to keep in mind:</p>
<ul>
<li>A recovery notification is matched to the earlier unhealthy notification for the <strong>same pool or endpoint</strong>. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.</li>
<li>If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.</li>
</ul>
<p>Refer to <a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a> to learn more about routing Load Balancing health notifications to an incident management tool.</p>


<h2 id="see-fallback-pool-traffic-separately-in-load-balancing-analytics"><a href="/changelog/post/2026-08-03-fallback-pool-analytics/">See fallback pool traffic separately in load balancing analytics</a></h2>
<p><em>2026-08-03</em></p>
<p>Load balancing analytics now shows traffic served by your <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pool</a> separately from traffic routed to the same pool by normal steering.</p>
<p>Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.</p>
<p>Fallback traffic is now labeled with the pool name followed by <code>(Fallback)</code>. A pool named <code>eu-west</code>, for example, is shown as <code>eu-west (Fallback)</code>. This label appears as its own entry in:</p>
<ul>
<li><strong>Requests over time</strong>, as a separate series in the chart.</li>
<li><strong>Pool distribution</strong>, as a separate segment.</li>
<li><strong>Top endpoints</strong>, as a separate card for the pool.</li>
</ul>
<p>The <strong>Latency</strong> view and the health event <strong>Logs</strong> are unchanged.</p>
<p>To see this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same breakdown appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>Refer to <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to learn more.</p>


<h2 id="faster-and-more-secure-tls-handshakes-to-your-origins-automatically"><a href="/changelog/post/2026-07-21-automatic-origin-key-exchange/">Faster and more secure TLS handshakes to your origins, automatically</a></h2>
<p><em>2026-07-21</em></p>
<p>Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first <code>ClientHello</code>, helping avoid a <code>HelloRetryRequest</code> and one extra network round trip.</p>
<p>Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum <code>X25519MLKEM768</code> hybrid key agreement.</p>
<p>To change this behavior, go to <strong>SSL/TLS</strong> &gt; <strong>Overview</strong> &gt; <strong>Origin connection &amp; post-quantum encryption</strong>. Turn off <strong>Automatic key exchange</strong> to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.</p>
<p><strong>Compliance requirements</strong> apply only to TLS 1.3 connections. The <strong>Post-quantum hybrid</strong> option requires hybrid post-quantum key agreements support on your origin server. The <strong>Federal Information Processing Standards (FIPS)</strong> option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.</p>
<p>For requirements, configuration options, and rollout details, refer to <a href="/ssl/origin-configuration/automatic-key-exchange/">Automatic key exchange to origins</a>.</p>


<h2 id="bot-management-fields-and-asn-support-in-cache-rules"><a href="/changelog/post/2026-07-16-cache-rules-bot-fields-asn/">Bot management fields and ASN support in Cache Rules</a></h2>
<p><em>2026-07-16</em></p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-bot-management-fields-and-asn-support-in-cache-rules">Bot management fields and ASN support in Cache Rules</h4>
<p>Cache Rules now supports bot management fields and the <code>ip.src.asnum</code> field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).</p>
<p>This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.</p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-new-fields">New fields</h4>
<p>The following fields are now available in Cache Rules expressions:</p>
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
<td><code>cf.bot_management.score</code></td>
<td>Number</td>
<td>Bot score from <code>1</code> to <code>99</code>, where a lower value indicates a higher likelihood that the request originates from a bot.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja3_hash</code></td>
<td>String</td>
<td>JA3 fingerprint of the request, which helps identify the client making the connection.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja4</code></td>
<td>String</td>
<td>JA4 fingerprint of the request, which provides a more detailed client identification than JA3.</td>
</tr>
<tr>
<td><code>cf.bot_management.verified_bot</code></td>
<td>Boolean</td>
<td>Whether the request originates from a verified bot, such as a search engine crawler.</td>
</tr>
<tr>
<td><code>cf.bot_management.static_resource</code></td>
<td>Boolean</td>
<td>Whether the request is for a static resource and therefore exempt from bot detection.</td>
</tr>
<tr>
<td><code>cf.bot_management.js_detection.passed</code></td>
<td>Boolean</td>
<td>Whether the browser passed JavaScript detection when the feature is enabled.</td>
</tr>
<tr>
<td><code>cf.bot_management.detection_ids</code></td>
<td>Array&lt;Number&gt;</td>
<td>List of IDs that correspond to Bot Management heuristic detections made on the request.</td>
</tr>
<tr>
<td><code>cf.bot_management.tags</code></td>
<td>Array&lt;String&gt;</td>
<td>List of tags associated with the bot traffic, such as <code>API</code>, <code>GOOGLE</code>, or <code>BING</code>. Match a tag with an expression such as <code>any(cf.bot_management.tags[*] eq &quot;API&quot;)</code>.</td>
</tr>
<tr>
<td><code>cf.bot_management.signed_agent</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known agent that identifies itself with Web Bot Auth.</td>
</tr>
<tr>
<td><code>cf.bot_management.corporate_proxy</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known corporate proxy.</td>
</tr>
<tr>
<td><code>ip.src.asnum</code></td>
<td>Number</td>
<td>The autonomous system number (ASN) of the incoming request's IP address.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17750.md")</aside>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-example">Example</h4>
<p>Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:</p>
<pre><code class="language-txt">(http.request.uri.path contains &quot;/api/&quot; and cf.bot_management.score lt 30)&#10;or&#10;(http.request.uri.path contains &quot;/api/&quot; and not ip.src.asnum in {12345 67890})&#10;</code></pre>
<p>To learn more, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a> and the <a href="/ruleset-engine/rules-language/fields/">Fields reference</a>.</p>


<h2 id="internal-dns-is-now-generally-available"><a href="/changelog/post/2026-07-15-internal-dns-ga/">Internal DNS is now generally available</a></h2>
<p><em>2026-07-15</em></p>
<p><a href="/dns/internal-dns/">Internal DNS</a> is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.</p>
<h4 id="2026-07-15-internal-dns-ga-why-it-matters">Why it matters</h4>
<ul>
<li><strong>Consolidate DNS operations.</strong> Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.</li>
<li><strong>Simplify split-horizon DNS.</strong> Internal and external resolution are defined as separate <a href="/dns/internal-dns/dns-views/">views</a> over shared zones, managed from a single control plane — so there is no drift to chase down.</li>
<li><strong>Extend Zero Trust to DNS.</strong> Resolver policies decide which users and devices resolve against which view, enforced by the same <a href="/cloudflare-one/traffic-policies/">Gateway</a> that already governs the rest of your traffic.</li>
</ul>
<p>Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.</p>
<pre><code class="language-json">POST /zones&#10;{&#10;  &quot;account&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  },&#10;  &quot;name&quot;: &quot;corp.internal&quot;,&#10;  &quot;type&quot;: &quot;internal&quot;&#10;}&#10;</code></pre>
<p>Internal DNS is included with <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for Enterprise customers. To get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="improved-reliability-for-account-wide-web-analytics-dashboards"><a href="/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/">Improved reliability for account-wide Web Analytics dashboards</a></h2>
<p><em>2026-07-14</em></p>
<p>Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.</p>
<p>For larger accounts (with &gt;100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.</p>
<p>Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.</p>
<p>If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.</p>


<h2 id="new-dns-firewall-ux-with-more-dashboard-settings"><a href="/changelog/post/2026-07-09-new-dns-firewall-ux/">New DNS Firewall UX with more dashboard settings</a></h2>
<p><em>2026-07-09</em></p>
<p>The DNS Firewall page in the Cloudflare dashboard has been refreshed, bringing several settings that were previously API-only into the UI and modernizing how you view and manage your DNS Firewall clusters.</p>
<p><img src="/assets/upstream/images/changelog/dns/dnsfw-new-ux.png" alt="New DNS Firewall UX" /></p>
<h4 id="2026-07-09-new-dns-firewall-ux-what-is-new">What is new</h4>
<ul>
<li><strong>More settings in the dashboard</strong>: cluster options that were previously only configurable through the API — such as attack mitigation, rate limiting, negative TTL, and resolver subnet — are now available directly in the dashboard.</li>
<li><strong>Better table experience</strong>: the DNS Firewall cluster table has been revised to surface cluster details at a glance, with resizable columns and the option to show or hide columns to tailor the view to your workflow.</li>
<li><strong>New create and edit UX</strong>: adding and editing clusters now uses a modernized form that groups related settings together, making configuration faster and clearer.</li>
</ul>
<h4 id="2026-07-09-new-dns-firewall-ux-availability">Availability</h4>
<p>Available to all DNS Firewall customers as part of their existing subscription.</p>
<h4 id="2026-07-09-new-dns-firewall-ux-where-to-find-it">Where to find it</h4>
<p>In the Cloudflare dashboard, go to the <strong>DNS Firewall</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/dns/dns-firewall/">DNS Firewall</a>.</p>


<h2 id="cache-multiple-versions-of-a-url-with-vary"><a href="/changelog/post/2026-07-02-vary-for-cache-rules/">Cache multiple versions of a URL with Vary</a></h2>
<p><em>2026-07-02</em></p>
<p>Your origin can serve different responses for the same URL — different languages based on <code>Accept-Language</code>, or different formats based on <code>Accept</code> — by returning a <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary"><code>Vary</code></a> response header. Cloudflare's cache now honors that header directly in <a href="/cache/how-to/cache-rules/">Cache Rules</a>, so the same URL can hold multiple cached versions and each request is matched to the right one. Content that previously had to bypass cache to stay correct can now be cached, following standard <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">HTTP caching behavior</a>.</p>
<h4 id="2026-07-02-vary-for-cache-rules-what-changed">What changed</h4>
<p>Your origin now decides which request headers matter by listing them in its <code>Vary</code> response, and you control how Cloudflare treats each one. When you have enabled Vary using a cache rule and a response includes a <code>Vary</code> header, the request headers listed become part of the cache key.</p>
<p>For each header your origin varies on, choose one of three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Behavior</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>normalize</code></td>
<td>Converts equivalent header values to the same cache key value before matching, collapsing redundant versions.</td>
<td>Most <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code> use cases.</td>
</tr>
<tr>
<td><code>passthrough</code></td>
<td>Uses the raw header value to select the cached version and forwards it to the origin unchanged.</td>
<td>When byte-for-byte differences in the header value should create versions.</td>
</tr>
<tr>
<td><code>bypass</code></td>
<td>Bypasses cache whenever this header name appears in the origin's <code>Vary</code> response.</td>
<td>Per-user values, or headers with too many possible values to cache safely.</td>
</tr>
</tbody>
</table>
<h4 id="2026-07-02-vary-for-cache-rules-benefits">Benefits</h4>
<ul>
<li><strong>Higher cache hit ratios</strong>: <code>normalize</code> treats semantically equivalent headers as one version. For example, <code>Accept-Language: en-US, fr;q=0.8</code> and <code>Accept-Language: fr;q=0.8, en-GB</code> both resolve to the same cache key, so you serve more requests from cache instead of the origin.</li>
<li><strong>Correct content negotiation</strong>: Requests always receive the cached version that matches their headers, so language and format variants stay accurate.</li>
<li><strong>No origin or Worker changes required</strong>: If your origin already sends <code>Vary</code>, you configure the behavior entirely in Cache Rules.</li>
<li><strong>Standards-aligned</strong>: Cache key calculation follows RFC 9111, and <code>Vary: *</code> continues to bypass cache as required by RFC 9110.</li>
</ul>
<h4 id="2026-07-02-vary-for-cache-rules-availability">Availability</h4>
<p>Vary in Cache Rules is available on all plans (Free, Pro, Business, and Enterprise). For per-request control in Workers subrequests, use the <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a> property.</p>
<h4 id="2026-07-02-vary-for-cache-rules-get-started">Get started</h4>
<p>Configure Vary in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or through the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. To learn how Vary affects cache keys and how each action works, refer to <a href="/cache/concepts/vary/">Vary</a> and the <a href="/cache/how-to/cache-rules/settings/#vary">Cache Rules Vary setting</a>.</p>


<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="cloudflare-amp-sxg-is-now-end-of-life"><a href="/changelog/post/2026-06-23-amp-sxg-end-of-life/">Cloudflare AMP/SXG is now end of life.</a></h2>
<p><em>2026-06-23</em></p>
<p>Cloudflare Accelerated Mobile Pages (AMP) and Signed Exchanges (SXG) support has reached end of life. The features have been disabled since October 2025, so customers who had them configured should see no change to their traffic.</p>
<p>Customers will no longer be able to configure AMP/SXG through API or rulesets. The Zone API will start throwing errors. Rulesets with the SXG configuration will fail to save until SXG has been removed.</p>


<h2 id="cloudflare-fonts-error-handling-and-security-improvements"><a href="/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/">Cloudflare Fonts error handling and security improvements</a></h2>
<p><em>2026-06-18</em></p>
<p>Cloudflare Fonts now forwards <code>/cf-fonts</code> requests to your origin server when it encounters invalid paths or unexpected runtime errors, instead of returning 4xx or 5xx responses directly. This update also adds additional input validation to enhance security.</p>


<h2 id="post-quantum-ml-dsa-certificates-for-authenticated-origin-pulls-and-custom-origin-trust-store"><a href="/changelog/post/2026-06-17-pqc-mldsa-aop-cots/">Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store</a></h2>
<p><em>2026-06-17</em></p>
<p>Cloudflare now accepts <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a> (FIPS 204) post-quantum certificates on the connection between Cloudflare's edge and your origin server. Combined with our existing <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> key agreement, this lets you establish end-to-end post-quantum authentication on the Cloudflare-to-origin connection.</p>
<p>ML-DSA is supported in two origin-facing features:</p>
<ul>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> (AOP) — upload an ML-DSA client certificate that Cloudflare will present during the mTLS handshake to your origin. Available at both zone-level and per-hostname scopes.</li>
<li><a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> (COTS) — upload an ML-DSA certificate authority that Cloudflare will trust when validating your origin server certificate under <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>.</li>
</ul>
<p>Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and setup guidance, and to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the current post-quantum deployment status across Cloudflare.</p>


<h2 id="account-level-dns-records-quota"><a href="/changelog/post/2026-06-10-account-level-record-quota/">Account-level DNS records quota</a></h2>
<p><em>2026-06-10</em></p>
<p>Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.</p>
<p>Accounts without an account-level quota are unaffected: existing per-zone quotas behave exactly as before.</p>
<p>For more details, refer to <a href="/dns/manage-dns-records/#dns-records-quota">DNS records quota</a>.</p>


<h2 id="bypass-status-now-returned-for-uncacheable-responses"><a href="/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/">BYPASS status now returned for uncacheable responses</a></h2>
<p><em>2026-05-26</em></p>
<p>Cloudflare now returns a <code>BYPASS</code> <a href="/cache/concepts/cache-responses/">cache status</a> whenever a response is not cacheable, instead of the previous mix of <code>BYPASS</code> and <code>MISS</code> that depended on why Cloudflare chose not to cache the response.</p>
<p>There are multiple reasons Cloudflare may refuse to cache a response — for example, the response exceeds the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">maximum cacheable file size</a> for your plan, the origin sends <code>Cache-Control: no-cache</code>, <code>private</code>, or <code>max-age=0</code>, the response includes a <code>Set-Cookie</code> header, or the request includes an <code>Authorization</code> header.</p>
<p>Previously, only some of these conditions returned <code>BYPASS</code>. Others — such as responses exceeding the maximum cacheable file size — returned <code>MISS</code> on every request, regardless of whether <a href="/cache/concepts/cache-control/#origin-cache-control-behavior">Origin Cache Control</a> was on or off. Because the response could never be cached, every subsequent request also returned <code>MISS</code>, which looked indistinguishable from a broken cache and made it hard to tell whether Cloudflare was trying and failing to cache the asset or had deliberately chosen not to cache it.</p>
<p><code>BYPASS</code> now consistently signals that Cloudflare refused to cache the response, regardless of the reason. <code>MISS</code> is reserved for cacheable responses that simply were not in the local cache at request time.</p>
<h4 id="2026-05-26-bypass-status-for-uncacheable-responses-what-to-expect-in-your-analytics">What to expect in your analytics</h4>
<p>After this change rolls out, you should see:</p>
<ul>
<li><strong>MISS rate decreases</strong>: Uncacheable responses no longer count as cache misses.</li>
<li><strong>BYPASS rate increases</strong>: These same responses are now reported as bypasses.</li>
<li><strong>Cache hit ratio increases</strong>: Hit ratio calculations no longer include uncacheable traffic that could never have been cached, giving you a more accurate view of cache effectiveness.</li>
</ul>
<p>Your total request volume and origin traffic are unchanged — only the cache status label is different.</p>
<h4 id="2026-05-26-bypass-status-for-uncacheable-responses-browser-cache-ttl-behavior-is-preserved">Browser cache TTL behavior is preserved</h4>
<p>The cache status label is the only thing changing — browser cache TTL handling for any given response is identical to what it was before:</p>
<ul>
<li>Responses that historically returned <code>MISS</code> because Cloudflare refused to cache them (for example, responses over the maximum cacheable file size) now return <code>BYPASS</code>, but continue to have browser cache TTL applied — exactly as they did when they were labeled <code>MISS</code>.</li>
<li>Responses that historically returned <code>BYPASS</code> and skipped browser cache TTL continue to skip browser cache TTL.</li>
</ul>
<p>In both cases, the decision to apply browser cache TTL depends on the underlying reason Cloudflare did not cache the response, not on the new <code>BYPASS</code> label.</p>


<h2 id="new-dns-records-ux-is-rolling-out"><a href="/changelog/post/2026-05-20-new-dns-records-ux/">New DNS records UX is rolling out</a></h2>
<p><em>2026-05-20</em></p>
<p>Starting today, everyone can opt in to a refreshed DNS records page in the Cloudflare dashboard. Over the coming weeks, the new experience will become the default for Free plan users first, followed by paid plans.</p>
<p><img src="/assets/upstream/images/changelog/dns/new-dns-ux.png" alt="New DNS records UX" /></p>
<h4 id="2026-05-20-new-dns-records-ux-what-is-new">What is new</h4>
<ul>
<li><strong>Better table experience</strong>: resizable and hideable columns, row pinning, advanced filters with logical operators (AND/OR), configurable pagination, and expanded input fields so long values are no longer cut off.</li>
<li><strong>First-class mobile experience</strong>: responsive layout with a touch-friendly, card-based UI and compact controls for small screens.</li>
<li><strong>DNS quick reference</strong>: bite-sized explainers for DNS, proxy status, and TTL, available directly in the product to help users configure records without leaving the page.</li>
<li><strong>Modern frontend</strong>: a refactor onto Cloudflare's new UI framework that improves performance and lays the foundation for future improvements.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/new-dns-ux.gif" alt="New DNS records UX" /></p>
<h4 id="2026-05-20-new-dns-records-ux-rollout-plan">Rollout plan</h4>
<p>Dates are subject to change based on feedback received during the rollout.</p>
<ul>
<li><strong>20 May - 05 June</strong>: ramped rollout to Free, then Pro and Business plans.</li>
<li><strong>08 June - 03 July</strong>: ramped rollout to Enterprise plans.</li>
</ul>
<h4 id="2026-05-20-new-dns-records-ux-share-your-feedback">Share your feedback</h4>
<p>Once the new experience is turned on for your account, look for the feedback link at the top of the DNS records page in the Cloudflare dashboard and let us know what you think. Your input helps us prioritize the next round of improvements.</p>


<h2 id="cdn-cgi-rum-endpoint-now-returns-405-for-non-post-requests"><a href="/changelog/post/2026-05-13-rum-405-method-not-allowed/">/cdn-cgi/rum endpoint now returns 405 for non-POST requests</a></h2>
<p><em>2026-05-13</em></p>
<p>The <code>/cdn-cgi/rum</code> beacon endpoint now returns <code>405 Method Not Allowed</code> for non-POST requests instead of <code>404 Not Found</code>. The response includes an <code>Allow: POST, OPTIONS</code> header per <a href="https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6">RFC 9110 §15.5.6</a>.</p>
<p>Previously, sending a <code>GET</code> or other non-POST request to this endpoint returned a <code>404</code>, which was misleading because it suggested the endpoint did not exist. The new <code>405</code> response clearly indicates that the endpoint exists but only accepts <code>POST</code> requests.</p>
<p>The Web Analytics beacon (<code>beacon.min.js</code>) already uses <code>POST</code> for all metric submissions, so this change does not affect normal beacon operation. <code>OPTIONS</code> requests for CORS preflight continue to work as before.</p>
<p>For more information, refer to the <a href="/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum">Web Analytics FAQ</a>.</p>


<h2 id="pingora-now-powers-cloudflare-s-cache"><a href="/changelog/post/2026-05-04-pingora-powers-cache/">Pingora now powers Cloudflare's cache</a></h2>
<p><em>2026-05-04</em></p>
<p>Cloudflare's cache now runs on a new proxy built on <a href="https://github.com/cloudflare/pingora">Pingora</a>, the Rust-based framework that already serves a significant portion of Cloudflare's network traffic. The new proxy is faster, more memory-safe, and designed to evolve our cache architecture. It delivers immediate performance improvements and enables new caching capabilities.</p>
<h4 id="2026-05-04-pingora-powers-cache-what-this-brings">What this brings</h4>
<ul>
<li><strong>Lower latency</strong>: The new proxy reduces per-request overhead through improved connection reuse.</li>
<li><strong>Reduced cache MISSes</strong>: Enhanced cache retention improves origin offload.</li>
<li><strong>Better RFC compliance</strong>: Caching behavior more closely follows HTTP caching standards.</li>
<li><strong>Foundation for future features</strong>: The new architecture enables upcoming improvements to cache functionality and efficiency.</li>
</ul>
<h4 id="2026-05-04-pingora-powers-cache-new-features">New features</h4>
<ul>
<li><strong>Asynchronous <code>stale-while-revalidate</code></strong>: Every request returns stale content immediately while revalidation happens in the background, instead of the first request after expiry blocking on the origin. Refer to the <a href="/changelog/post/2026-02-26-async-stale-while-revalidate/">asynchronous <code>stale-while-revalidate</code> changelog</a> for details.</li>
<li><strong>Unbuffered bypass by default</strong>: Responses that bypass cache are streamed directly to the client without buffering, reducing time-to-first-byte for uncacheable content.</li>
</ul>
<h4 id="2026-05-04-pingora-powers-cache-behavioral-changes">Behavioral changes</h4>
<p>The new architecture introduces the following behavioral changes to improve RFC compliance and correctness:</p>
<ul>
<li><strong><code>Vary: *</code> results in cache bypass</strong>: According to <a href="https://httpwg.org/specs/rfc9110.html#field.vary">RFC 9110 Section 12.5.5</a>, a <code>Vary</code> header value of <code>*</code> indicates the response varies on factors beyond request headers and must not be served from cache. Cloudflare now bypasses cache for these responses instead of storing them.</li>
<li><strong><code>Set-Cookie</code> stripped on MISS and EXPIRED</strong>: For cacheable assets, <code>Set-Cookie</code> is now stripped on MISS and EXPIRED responses, not only on HITs.</li>
<li><strong>Floating-point TTL values</strong>: Floating-point time-to-live values (for example, <code>max-age=1.5</code>) are rounded down to the nearest integer instead of being rejected as invalid.</li>
</ul>
<h4 id="2026-05-04-pingora-powers-cache-what-s-next">What's next</h4>
<p>A deeper look at the new cache proxy is coming soon to the <a href="https://blog.cloudflare.com/">Cloudflare blog</a>. For background on the underlying framework, read:</p>
<ul>
<li><a href="https://blog.cloudflare.com/pingora-open-source/">Open sourcing Pingora: our Rust framework for building programmable network services</a></li>
<li><a href="https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/">How we built Pingora, the proxy that connects Cloudflare to the Internet</a></li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 4</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-performance/2/">Next</a></nav>
