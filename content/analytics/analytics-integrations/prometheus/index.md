<p>This tutorial explains how to export Cloudflare metrics to <a href="https://prometheus.io/">Prometheus</a> using the <a href="https://github.com/cloudflare/cloudflare-prometheus-exporter">Cloudflare Prometheus Exporter</a>, an open-source tool built on Cloudflare Workers with Durable Objects.</p>
<h2 id="overview">Overview</h2>
<p>Before setting up the Cloudflare Prometheus Exporter, note that this integration:</p>
<ul>
<li>Is available to all Cloudflare customer plans (Free, Pro, Business, and Enterprise). Zones on the Free plan have limited metrics availability.</li>
<li>Is based on the Cloudflare GraphQL Analytics API and REST API.</li>
<li>Exports 90+ Prometheus metrics covering requests, bandwidth, threats, Workers, load balancers, SSL certificates, firewall events, health checks, Magic Transit, Stream, and more.</li>
<li>Runs as a Cloudflare Worker with Durable Objects for stateful counter accumulation and background refresh.</li>
<li>Supports multi-account setups, automatically discovering all accessible accounts and zones.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before deploying the exporter, make sure that you:</p>
<ul>
<li>Have a Cloudflare account.</li>
<li>Have a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with the required permissions (see <a href="#task-2---create-an-api-token">Create an API token</a> below).</li>
<li>Have a Prometheus instance to scrape the exporter.</li>
</ul>
<h2 id="task-1-deploy-the-exporter">Task 1 - Deploy the exporter</h2>
<p>You can deploy the exporter using one-click deploy or manually.</p>
<h3 id="one-click-deploy">One-click deploy</h3>
<p>Select the button below to deploy the exporter to your Cloudflare Workers account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/cloudflare-prometheus-exporter"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare Workers" /></a></p>
<p>After deployment, configure <code>CLOUDFLARE_API_TOKEN</code> as a secret. Optionally configure <code>BASIC_AUTH_USER</code> and <code>BASIC_AUTH_PASSWORD</code> to protect the exporter with HTTP Basic Auth.</p>
<h3 id="manual-deployment">Manual deployment</h3>
<pre><code class="language-bash">git clone https://github.com/cloudflare/cloudflare-prometheus-exporter.git&#10;cd cloudflare-prometheus-exporter&#10;bun install&#10;wrangler secret put CLOUDFLARE_API_TOKEN&#10;bun run deploy&#10;</code></pre>
<h2 id="task-2-create-an-api-token">Task 2 - Create an API token</h2>
<p>Create a Cloudflare API token with the following permissions:</p>
<p><a href="https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22analytics%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22account_analytics%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22ssl_and_certificates%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22firewall_services%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22load_balancers%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22account_logs%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22magic_transit%22%2C%22type%22%3A%22read%22%7D%5D&amp;name=Cloudflare%20Prometheus%20Exporter">Create token with pre-filled permissions</a></p>
<table>
<thead>
<tr>
<th>Permission</th>
<th>Access</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zone &gt; Analytics</td>
<td>Read</td>
<td>Yes</td>
</tr>
<tr>
<td>Account &gt; Account Analytics</td>
<td>Read</td>
<td>Yes</td>
</tr>
<tr>
<td>Account &gt; Workers Scripts</td>
<td>Read</td>
<td>Yes</td>
</tr>
<tr>
<td>Zone &gt; SSL and Certificates</td>
<td>Read</td>
<td>Optional</td>
</tr>
<tr>
<td>Zone &gt; Firewall Services</td>
<td>Read</td>
<td>Optional</td>
</tr>
<tr>
<td>Zone &gt; Load Balancers</td>
<td>Read</td>
<td>Optional</td>
</tr>
<tr>
<td>Account &gt; Logs</td>
<td>Read</td>
<td>Optional</td>
</tr>
<tr>
<td>Account &gt; Magic Transit</td>
<td>Read</td>
<td>Optional</td>
</tr>
</tbody>
</table>
<h2 id="task-3-configure-prometheus">Task 3 - Configure Prometheus</h2>
<p>Add the exporter as a scrape target in your Prometheus configuration:</p>
<pre><code class="language-yaml">scrape_configs:&#10;  &#45; job_name: &#x27;cloudflare&#x27;&#10;    scrape_interval: 60s&#10;    scrape_timeout: 30s&#10;    static_configs:&#10;      &#45; targets: [&#x27;your-worker.your-subdomain.workers.dev&#x27;]&#10;</code></pre>
<h3 id="with-basic-auth">With Basic Auth</h3>
<p>If you configured Basic Auth on the exporter, update your Prometheus configuration:</p>
<pre><code class="language-yaml">scrape_configs:&#10;  &#45; job_name: &#x27;cloudflare&#x27;&#10;    scrape_interval: 60s&#10;    scrape_timeout: 30s&#10;    basic_auth:&#10;      username: &#x27;your-username&#x27;&#10;      password: &#x27;your-password&#x27;&#10;    static_configs:&#10;      &#45; targets: [&#x27;your-worker.your-subdomain.workers.dev&#x27;]&#10;</code></pre>
<h2 id="configuration">Configuration</h2>
<p>Configuration is resolved in order: <strong>KV overrides</strong> &gt; <strong>environment variables</strong> &gt; <strong>defaults</strong>. You can use the runtime config API for dynamic changes without redeployment.</p>
<p>Set environment variables in <code>wrangler.jsonc</code> or via <code>wrangler secret put</code>:</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CLOUDFLARE_API_TOKEN</code></td>
<td>-</td>
<td>Cloudflare API token (secret)</td>
</tr>
<tr>
<td><code>SCRAPE_DELAY_SECONDS</code></td>
<td><code>300</code></td>
<td>Delay before fetching metrics (data propagation)</td>
</tr>
<tr>
<td><code>TIME_WINDOW_SECONDS</code></td>
<td><code>60</code></td>
<td>Query time window</td>
</tr>
<tr>
<td><code>METRIC_REFRESH_INTERVAL_SECONDS</code></td>
<td><code>60</code></td>
<td>Background refresh interval</td>
</tr>
<tr>
<td><code>CF_ACCOUNTS</code></td>
<td>-</td>
<td>Comma-separated account IDs to include (default: all)</td>
</tr>
<tr>
<td><code>CF_ZONES</code></td>
<td>-</td>
<td>Comma-separated zone IDs to include (default: all)</td>
</tr>
<tr>
<td><code>METRICS_DENYLIST</code></td>
<td>-</td>
<td>Comma-separated list of metrics to exclude</td>
</tr>
<tr>
<td><code>EXCLUDE_HOST</code></td>
<td><code>false</code></td>
<td>Exclude host labels from metrics</td>
</tr>
<tr>
<td><code>METRICS_PATH</code></td>
<td><code>/metrics</code></td>
<td>Custom path for metrics endpoint</td>
</tr>
<tr>
<td><code>BASIC_AUTH_USER</code></td>
<td>-</td>
<td>Username for Basic Auth (secret)</td>
</tr>
<tr>
<td><code>BASIC_AUTH_PASSWORD</code></td>
<td>-</td>
<td>Password for Basic Auth (secret)</td>
</tr>
</tbody>
</table>
<p>For a full list of configuration options, refer to the <a href="https://github.com/cloudflare/cloudflare-prometheus-exporter#configuration">exporter README</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<table>
<thead>
<tr>
<th>Path</th>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td>GET</td>
<td>Landing page</td>
</tr>
<tr>
<td><code>/metrics</code></td>
<td>GET</td>
<td>Prometheus metrics</td>
</tr>
<tr>
<td><code>/health</code></td>
<td>GET</td>
<td>Health check</td>
</tr>
<tr>
<td><code>/config</code></td>
<td>GET</td>
<td>Get all runtime config</td>
</tr>
<tr>
<td><code>/config/:key</code></td>
<td>PUT</td>
<td>Set a config override (persisted in KV)</td>
</tr>
<tr>
<td><code>/config/:key</code></td>
<td>DELETE</td>
<td>Reset a config key to its default</td>
</tr>
</tbody>
</table>
<h2 id="available-metrics">Available metrics</h2>
<p>The exporter provides 90+ metrics across the following categories:</p>
<ul>
<li><strong>Zone requests</strong> - Total requests, cached requests, requests by status code, country, content type, HTTP version, and more.</li>
<li><strong>Zone bandwidth</strong> - Total bandwidth, cached bandwidth, bandwidth by content type and country.</li>
<li><strong>Zone threats</strong> - Threat counts by country and type.</li>
<li><strong>Firewall</strong> - Firewall events by action, source, and rule. Bot detection metrics.</li>
<li><strong>Workers</strong> - Request counts, error counts, CPU time, and duration by script.</li>
<li><strong>Load balancers</strong> - Pool health status, request counts, RTT, steering policy, and origin weights.</li>
<li><strong>Health checks</strong> - Health check events, RTT, TTFB, TCP connection time, and TLS handshake time.</li>
<li><strong>SSL certificates</strong> - Certificate validation status by type and issuer.</li>
<li><strong>Cache</strong> - Cache hit ratio and cache miss origin duration.</li>
<li><strong>Error rates</strong> - 4xx/5xx error counts, edge and origin error rates, origin response duration.</li>
<li><strong>Logpush</strong> - Failed job counts at account and zone level.</li>
<li><strong>Magic Transit</strong> - Tunnel health, SLO status, and per-tunnel traffic (bits and packets).</li>
<li><strong>Magic Firewall</strong> - Per-rule sampled traffic (bits and packets).</li>
<li><strong>Network Analytics</strong> - Traffic volume across Magic Transit, DDoS defense, IDPS, TCP protection, and DNS protection.</li>
<li><strong>Stream</strong> - Video playback counts, time viewed, live input metrics.</li>
<li><strong>Hostname metrics</strong> - Per-hostname request counts, latency averages, and percentiles (requires <code>HOST_METRICS_ALLOWLIST</code>).</li>
</ul>
<p>For a complete list of metrics with types and labels, refer to the <a href="https://github.com/cloudflare/cloudflare-prometheus-exporter#available-metrics">exporter README</a>.</p>
<h2 id="free-tier-zone-limitations">Free tier zone limitations</h2>
<p>Zones on Cloudflare's Free plan do not have access to the GraphQL Analytics API. The exporter automatically detects and skips free tier zones for metrics that require this API.</p>
<p>Free tier zones still export:</p>
<ul>
<li><code>cloudflare_zone_certificate_validation_status</code> (SSL certificates)</li>
<li><code>cloudflare_zone_lb_origin_weight</code> (Load balancer weights, if configured)</li>
</ul>
<p>You can monitor skipped zones with the <code>cloudflare_zones_skipped_free_tier</code> metric.</p>
