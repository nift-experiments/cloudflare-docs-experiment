<p>A protocol is a set of rules governing the exchange or transmission of data between devices. One of the most important protocols that run on the human-computer interaction layer, where applications can access the network services, is HTTP (Hypertext Transfer Protocol).</p>
<p>HTTP is a well established protocol that has several versions, and each version adds features that improve performance over the older one. HTTP/1.1 and HTTP/2 are widely deployed on the Internet today. HTTP/1.1 has been around for more than a decade, but in 2015 the IETF (Internet Engineering Task Force) introduced HTTP/2, which introduces several features to reduce page load times. To know more about the differences between HTTP/1.1 and HTTP/2, please refer to <a href="https://www.cloudflare.com/learning/performance/http2-vs-http1.1/">HTTP/2 versus HTTP/1.1</a>.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="disable-http-2-to-origin">Disable HTTP/2 to Origin</h2>
<p>At Cloudflare, HTTP/2 connection to the origin is enabled by default.</p>
<p>If you wish to disable HTTP/2 to Origin, you can follow these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Speed</strong> &gt; <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Protocol Optimization</strong> tab and under <strong>HTTP/2 to Origin</strong> set the toggle to <strong>Off</strong>.</li>
</ol>
<h2 id="connection-multiplexing">Connection multiplexing</h2>
<p>Cloudflare supports HTTP/2 multiplexing from its global edge network to your origin servers. Instead of opening a new TCP connection for every incoming request, multiple HTTP/2 streams share a single long-lived TCP connection. This significantly reduces the cost of connection setup and teardown, improving efficiency and performance between Cloudflare and your origin.</p>
<p>By pooling many requests into fewer TCP connections, Cloudflare lowers the number of active connections your origin must maintain — particularly valuable for backends sensitive to connection overhead or resource limits.</p>
<h3 id="how-it-works">How it works</h3>
<p>When a new request arrives, Cloudflare attempts to reuse an existing HTTP/2 connection to the origin:</p>
<ul>
<li>If the connection has not reached its concurrent stream limit, Cloudflare multiplexes the request over that same connection.</li>
<li>If the stream limit has been reached, Cloudflare opens a new TCP connection as needed.</li>
</ul>
<p>Connections are kept alive and reused until they become idle or hit their concurrency limit.</p>
<h4 id="connection-lifecycle">Connection lifecycle</h4>
<ul>
<li>
<p><strong>Connection reuse</strong>: Cloudflare maintains persistent (keep-alive) TCP connections to your origin. Reuse continues until the HTTP/2 stream limit is reached or the connection goes idle.</p>
</li>
<li>
<p><strong>Idle timeout (900s)</strong>: If a connection remains idle (no active streams) for 900 seconds, Cloudflare closes it. Attempting to reuse a closed connection may result in a <code>520</code> error.</p>
</li>
<li>
<p><strong>Keep-alives</strong>: Cloudflare sends periodic TCP keep-alives to detect unresponsive origins. After two unanswered probes, the connection is reset.</p>
<ul>
<li>First probe after ~30 seconds of inactivity</li>
<li>Second probe after 15 seconds</li>
</ul>
</li>
<li>
<p><strong>Connection tear-down</strong>: Connections may also close due to:</p>
<ul>
<li>Load balancing decisions</li>
<li>Data center or node maintenance</li>
<li>Reaching the maximum concurrency limit</li>
<li>Origin or intermediary network closing idle connections</li>
</ul>
</li>
</ul>
<h3 id="benefits">Benefits</h3>
<table>
<thead>
<tr>
<th>Advantage</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fewer TCP handshakes</td>
<td>Multiple requests share a single long-lived TCP connection, minimizing connection churn.</td>
</tr>
<tr>
<td>Lower latency</td>
<td>Eliminates repeated TCP/TLS handshakes, reducing round-trip delays for new requests.</td>
</tr>
<tr>
<td>Reduced origin load</td>
<td>Fewer concurrent connections for the origin to manage, easing load on resource-constrained systems.</td>
</tr>
<tr>
<td>Adaptive scaling</td>
<td>During surges (for example, failovers), Cloudflare reuses available streams first, then opens new connections as needed.</td>
</tr>
</tbody>
</table>
<h3 id="default-behavior-by-plan">Default behavior by plan</h3>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Default State</th>
<th>Max concurrent streams per connection</th>
<th>Configurable?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free / Pro / Business</td>
<td>Enabled by default</td>
<td>200</td>
<td>No</td>
</tr>
<tr>
<td>Enterprise</td>
<td>Disabled by default (1 stream per connection)</td>
<td>1–200+</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<ul>
<li><strong>Free/Pro/Business</strong>: Multiplexing is automatically enabled. Each connection supports up to 200 concurrent streams.</li>
<li><strong>Enterprise</strong>: Multiplexing starts effectively disabled (1 stream). You can enable and configure concurrency per zone (up to 200+ concurrent streams).</li>
</ul>
<h3 id="configuration">Configuration</h3>
<p>Connection multiplexing is enabled by default on Free, Pro and Business zones and uses up to 100 concurrent streams by default. Enterprise plans can explicitly configure the maximum number of concurrent streams (often called the “multiplexing ratio”) for a zone in the dashboard or via API.</p>
<details class="nb-details"><summary>Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13915.md")
</div></details>
<details class="nb-details"><summary>API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13916.md")
</div></details>
<details class="nb-details"><summary>Terraform</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13917.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13914.md")
</aside>
<h3 id="timeouts-and-error-codes">Timeouts and error codes</h3>
<table>
<thead>
<tr>
<th>Condition</th>
<th>Default / Range</th>
<th>Error code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Proxy Read Timeout</td>
<td>125s (up to 6000s for Enterprise)</td>
<td><code>524</code></td>
<td>Origin took too long to respond.</td>
</tr>
<tr>
<td>Proxy Idle Timeout</td>
<td>900s (fixed)</td>
<td><code>520</code></td>
<td>Connection closed due to idleness.</td>
</tr>
<tr>
<td>TCP Keep-Alive Interval</td>
<td>30s initial, 15s between probes</td>
<td><code>520</code></td>
<td>After two missed probes, Cloudflare resets the connection.</td>
</tr>
<tr>
<td>TCP Handshake Timeout</td>
<td>19s</td>
<td><code>522</code></td>
<td>Origin did not complete the SYN handshake.</td>
</tr>
<tr>
<td>TCP ACK Timeout</td>
<td>90s</td>
<td><code>522</code></td>
<td>Origin stopped acknowledging data.</td>
</tr>
</tbody>
</table>
<h3 id="common-scenarios">Common scenarios</h3>
<p><strong>Failover events</strong></p>
<p>When traffic shifts suddenly (for example, during origin failover), Cloudflare reuses active connections where possible. If concurrency limits are reached, it opens new ones. Active connection counts may spike temporarily, but overall total connections remain lower than without multiplexing.</p>
<p><strong>Long-Lived or idle requests</strong></p>
<pre><code>- If your requests exceed 125 seconds (for example, streaming), increase the Proxy Read Timeout (Enterprise only).&#10;- Origins that close connections faster than 900 seconds may experience connection churn, but Cloudflare automatically reestablishes new connections as needed.&#10;</code></pre>
<p><strong>Potential 5xx errors</strong></p>
<p>Some 5xx errors, like <code>520</code> or <code>522</code>, may be related to idle timeouts or unreachable origins. If concurrency is set too high for an underpowered origin, bursts of simultaneous requests can overwhelm it and lead to stream resets or short spikes of 5xx errors. Enterprise customers who encounter this can ask their Cloudflare account team or support to lower the concurrency limit, which reduces how many requests are sent to the origin at the same time and helps prevent overload.</p>
<h3 id="faq">FAQ</h3>
<h4 id="does-cloudflare-use-a-fixed-multiplexing-ratio">Does Cloudflare use a fixed multiplexing ratio?</h4>
<p>Free, Pro, and Business plans use 200 concurrent streams per connection. Enterprise users can configure between 1–200+ streams.</p>
<h4 id="how-does-cloudflare-scale-connections-during-spikes-or-failovers">How does Cloudflare scale connections during spikes or failovers?</h4>
<p>Cloudflare first reuses existing keep-alive connections. If they reach concurrency limits, new connections are opened as needed. Even during surges, total connection count is typically lower than without multiplexing.</p>
<h4 id="what-if-my-backend-is-sensitive-to-parallel-requests">What if my backend is sensitive to parallel requests?</h4>
<p>Enterprise users can lower the concurrency limit. Cloudflare also honors your origin's <code>SETTINGS_MAX_CONCURRENT_STREAMS</code>, allowing your server to enforce stricter limits. Cloudflare's CDN also provides Cache Locking, which helps avoid multiple parallel requests to your origin during revalidation. Refer to <a href="/cache/concepts/revalidation/">Revalidation</a> for more information.</p>
<h4 id="can-i-gradually-roll-out-higher-concurrency">Can I gradually roll out higher concurrency?</h4>
<p>Yes. You can adjust your origin's HTTP/2 settings or Cloudflare's zone setting incrementally to increase concurrency safely.</p>
<h4 id="from-where-does-cloudflare-connect-to-my-origin">From where does Cloudflare connect to my origin?</h4>
<p>Cloudflare operates a flat anycast network. Any data center may connect directly to your origin — there is no L1/L2 hierarchy. Origin connections may come from multiple data centers worldwide.</p>
<h4 id="does-cloudflare-prewarm-connections-to-origins">Does Cloudflare prewarm connections to origins?</h4>
<p>No. Connections are created on demand and reused where possible. There is no persistent idle pool.</p>
<h4 id="how-are-idle-connections-managed">How are idle connections managed?</h4>
<p>Idle connections are closed after 900 seconds of inactivity. They are not reopened proactively; new connections are created as traffic resumes.</p>
<h4 id="can-cloudflare-close-active-tcp-connections">Can Cloudflare close active TCP connections?</h4>
<p>Only if the origin closes them, a network error occurs, or Cloudflare performs maintenance or load redistribution. There is no hard maximum lifetime for active connections.</p>
<h2 id="protocol-compatibility">Protocol compatibility</h2>
<p>Note that if the origin does not support HTTP/2, Cloudflare will initiate an HTTP/1.1 connection.
We connect to servers who announce support of HTTP/2 connections via <a href="https://blog.cloudflare.com/introducing-http2">ALPN</a>.</p>
<p>If you are unsure if your server supports HTTP/2, we suggest checking your origin server's documentation or using a testing tool for HTTP/2 implementation (for example, <a href="https://github.com/summerwind/h2spec">h2spec</a>).</p>
