<p>The following products and features are available on the Cloudflare China Network operated by JD Cloud:</p>
<h2 id="application-services">Application Services</h2>
<table>
<thead>
<tr>
<th>Product/Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/china-network/concepts/china-dns/">Authoritative DNS</a></td>
<td>Authoritative DNS resolution inside Mainland China.</td>
</tr>
<tr>
<td><a href="/cache/">CDN/Cache</a></td>
<td>Core cache features. Static cache only. Does not support Cache Reserve or Tiered Cache.</td>
</tr>
<tr>
<td><a href="/images/">Image Transformations</a></td>
<td>Optimize image format at the edge to fit a domain's layout.</td>
</tr>
<tr>
<td><a href="/ddos-protection/">DDoS Protection</a></td>
<td>Layer 7 (application layer) protection against DDoS attacks such as HTTP flood attacks, WordPress Pingback attacks, HULK attacks, and LOIC attacks.</td>
</tr>
<tr>
<td><a href="/waf/managed-rules/">Managed rules</a></td>
<td>Pre-configured OWASP rulesets and Cloudflare managed rulesets.</td>
</tr>
<tr>
<td><a href="/waf/custom-rules/">Custom rules</a></td>
<td>Custom WAF rules. Supports uploaded content scanning and managed challenges.</td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></td>
<td>Define rate limits for incoming requests matching an expression, and the action to take when those rate limits are reached.</td>
</tr>
<tr>
<td><a href="/waf/detections/malicious-uploads/">Content scanning</a></td>
<td>Attempts to detect content objects, such as uploaded files, and scans them for malicious signatures like malware.</td>
</tr>
<tr>
<td><a href="/client-side-security/">Client-side security</a> (formerly Page Shield)</td>
<td>Simplifies external script management by tracking loaded resources like scripts and providing alerts when it detects new resources or malicious scripts.</td>
</tr>
<tr>
<td><a href="/bots/">Bot Management</a><sup><a href="#footnote-1">1</a></sup></td>
<td>Provides bot identification and protection for a domain. Only supports certain Machine Learning (ML) models.</td>
</tr>
<tr>
<td><a href="/argo-smart-routing/">Argo Smart Routing</a></td>
<td>Layer 7 (application layer) traffic smart-routed more efficiently to origin.</td>
</tr>
<tr>
<td><a href="/rules/">Rules</a><sup><a href="#footnote-2">2</a></sup></td>
<td>Make adjustments to requests and responses, configure Cloudflare settings, and trigger specific actions for matching requests.</td>
</tr>
<tr>
<td><a href="/load-balancing/additional-options/load-balancing-china/">Load Balancing</a></td>
<td>Maximize application performance and availability.</td>
</tr>
</tbody>
</table>
<h2 id="developer-services">Developer Services</h2>
<table>
<thead>
<tr>
<th>Product/Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/">Workers</a></td>
<td>A serverless execution environment running on the Cloudflare global network.</td>
</tr>
<tr>
<td><a href="/kv/">Workers KV</a></td>
<td>Configuration data, service routing metadata, personalization (A/B testing).</td>
</tr>
<tr>
<td><a href="/r2/">R2</a><sup><a href="#footnote-3">3</a></sup></td>
<td>Object storage for all your data.</td>
</tr>
<tr>
<td><a href="/workers/static-assets/">Assets</a></td>
<td>Upload static assets (HTML, CSS, images and other files) as part of your Worker — Cloudflare will handle caching and serving them to web browsers.</td>
</tr>
<tr>
<td><a href="/workers/configuration/environment-variables/">Environment variables</a></td>
<td>Attach text strings or JSON values to your Worker.</td>
</tr>
<tr>
<td><a href="/images/optimization/binding/">Images</a><sup><a href="#footnote-4">4</a></sup></td>
<td>Store, transform, optimize, and deliver images at scale.</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/mtls/">mTLS</a></td>
<td>Securely connect to backend servers over <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">mTLS</a>.</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting</a></td>
<td>Define rate limits and write code around them in your Worker.</td>
</tr>
<tr>
<td><a href="/workers/configuration/secrets/">Secrets</a></td>
<td>Attach encrypted text values to your Worker.</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a></td>
<td>Service bindings allow one Worker to call into another, without going through a publicly-accessible URL.</td>
</tr>
<tr>
<td><a href="/workers/observability/logs/tail-workers/">Tail Workers</a></td>
<td>Receives information about the execution of other Workers.</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/version-metadata/">Version metadata</a></td>
<td>Access metadata associated with a version from inside the Workers runtime.</td>
</tr>
<tr>
<td><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></td>
<td>Deploy custom code on behalf of your users or let your users directly deploy their own code to your platform, managing infrastructure.</td>
</tr>
</tbody>
</table>
<h2 id="network-services">Network Services</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/network/ipv6-compatibility/">IPv6</a></td>
<td>All data centers have IPv6 support by default.</td>
</tr>
<tr>
<td><a href="/ssl/">SSL/TLS</a></td>
<td>Customer Certificate, Dedicated Certificate, Universal Certificate, Custom, ACM (Dedicated), Universal SSL.</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/learning/performance/what-is-http3/">HTTP/3 (QUIC)</a></td>
<td>The latest version of the HTTP protocol to optimize page loading performance.</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/websockets/">WebSockets</a></td>
<td>Real-time communication with Cloudflare Workers serverless functions.</td>
</tr>
</tbody>
</table>
<h2 id="zero-trust-services">Zero Trust Services</h2>
<p>Refer to <a href="/china-network/concepts/global-acceleration/">Global Acceleration</a> for more information.</p>
<h2 id="other-services">Other Services</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/logs/instant-logs/">Instant Logs</a></td>
<td>Live Tail your Cloudflare HTTP logs in the Cloudflare dashboard.</td>
</tr>
<tr>
<td><a href="/logs/logpush/">Logpush</a></td>
<td>Push your Cloudflare HTTP logs to a storage service.</td>
</tr>
</tbody>
</table>
<p>For more details or specific product features, refer to the <a href="/china-network/faq/#products-and-features">FAQ</a> page or contact your account team.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">[Turnstile](/turnstile/) is not available within Mainland China.</li>
<li id="footnote-2">[Origin Rules](/rules/origin-rules/) require that China Network is enabled on both the original zone (the one visitors are accessing) and the target zone. Otherwise, visitors will receive a [1016 error](/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1016/) along with an [HTTP 530 status code](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-530/).</li>
<li id="footnote-3">R2 buckets cannot be created within Mainland China and [custom domains](/r2/buckets/public-buckets/#add-your-domain-to-cloudflare) are not supported within Mainland China. However, R2 can be extended into Mainland China through [Global Acceleration](/china-network/concepts/global-acceleration/).</li>
<li id="footnote-4">Image Resizing works [within Workers](/images/optimization/transformations/transform-via-workers/), but may not be available [through URL format](/images/optimization/features/).</li></ol></section>
