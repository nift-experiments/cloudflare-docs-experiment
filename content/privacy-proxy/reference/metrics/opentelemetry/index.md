<p>Privacy Proxy exports telemetry data using the <a href="https://opentelemetry.io/docs/specs/otlp/">OpenTelemetry Protocol (OTLP)</a>. You can configure an endpoint to receive this data and forward it to your observability platform.</p>
<hr />
<h2 id="configure-telemetry-export">Configure telemetry export</h2>
<p>During onboarding, provide Cloudflare with your OpenTelemetry collector endpoint:</p>
<ul>
<li><strong>Endpoint URL</strong>: The HTTPS endpoint where telemetry data should be sent.</li>
<li><strong>Authentication</strong>: Headers or credentials required to authenticate with your collector. Supported authentication types include bearer token headers, custom header-based authentication, and mutual TLS (mTLS).</li>
</ul>
<p>Cloudflare configures your Privacy Proxy instance to export telemetry to this endpoint.</p>
<hr />
<h2 id="supported-signals">Supported signals</h2>
<p>Privacy Proxy exports the following telemetry signals:</p>
<table>
<thead>
<tr>
<th>Signal</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Metrics</td>
<td>Connection counts, request rates, latency histograms, error rates</td>
</tr>
<tr>
<td>Traces</td>
<td>Per-request traces showing proxy processing time. Traces are sampled at approximately 1% of requests.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="metrics">Metrics</h2>
<p>Privacy Proxy exports metrics that help you understand usage patterns and performance.</p>
<h3 id="connection-metrics">Connection metrics</h3>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>privacy_proxy_connections_total</code></td>
<td>Total number of proxy connections</td>
</tr>
<tr>
<td><code>privacy_proxy_connections_active</code></td>
<td>Currently active connections</td>
</tr>
<tr>
<td><code>privacy_proxy_connections_duration_seconds</code></td>
<td>Connection duration histogram</td>
</tr>
</tbody>
</table>
<h3 id="request-metrics">Request metrics</h3>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>privacy_proxy_requests_total</code></td>
<td>Total CONNECT requests processed</td>
</tr>
<tr>
<td><code>privacy_proxy_requests_by_status</code></td>
<td>Requests grouped by response status code</td>
</tr>
<tr>
<td><code>privacy_proxy_bytes_sent_total</code></td>
<td>Total bytes sent to destinations</td>
</tr>
<tr>
<td><code>privacy_proxy_bytes_received_total</code></td>
<td>Total bytes received from destinations</td>
</tr>
</tbody>
</table>
<h3 id="latency-metrics">Latency metrics</h3>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>privacy_proxy_connect_latency_seconds</code></td>
<td>Time to establish connection to destination</td>
</tr>
<tr>
<td><code>privacy_proxy_first_byte_latency_seconds</code></td>
<td>Time to first byte from destination</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="server-timing-header"><code>Server-Timing</code> header</h2>
<p>Privacy Proxy includes a <code>Server-Timing</code> header in responses to help measure processing latency from the client side. For full header format details, refer to <a href="/privacy-proxy/reference/http-headers/#server-timing">HTTP headers</a>.</p>
<pre><code class="language-http">Server-Timing: proxy;dur=12.5&#10;</code></pre>
<p>The <code>dur</code> value is the processing time in milliseconds introduced by the proxy. Use this header as a client-side SLI (Service Level Indicator) to monitor proxy performance.</p>
<h3 id="example-prometheus-and-grafana">Example: Prometheus and Grafana</h3>
<p>To visualize Privacy Proxy metrics in Grafana:</p>
<ol>
<li>Configure an OpenTelemetry collector to receive data from Privacy Proxy.</li>
<li>Export metrics from the collector to Prometheus.</li>
<li>Create Grafana dashboards using Prometheus as a data source.</li>
</ol>
<pre><code class="language-txt">&#35; Request rate over time&#10;rate(privacy_proxy_requests_total[5m])&#10;&#10;&#35; 95th percentile connection latency&#10;histogram_quantile(0.95, rate(privacy_proxy_connect_latency_seconds_bucket[5m]))&#10;&#10;&#35; Error rate&#10;sum(rate(privacy_proxy_requests_by_status{status=~&quot;5..&quot;}[5m])) / sum(rate(privacy_proxy_requests_total[5m]))&#10;</code></pre>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://opentelemetry.io/docs/">OpenTelemetry documentation</a> — Learn more about OpenTelemetry concepts and configuration.</li>
<li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a> — Query metrics programmatically via Cloudflare's GraphQL API.</li>
</ul>
