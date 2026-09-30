<p>There are some caveats and limitations when deploying Data Localization Suite features.</p>
<p>Cloudflare is working hard to improve this offering and fill the gaps. If you have a specific feature request, please contact your <a href="/support/contacting-cloudflare-support/">Account Team</a>.</p>
<h2 id="key-management">Key Management</h2>
<p>When using Geo Key Manager or Keyless SSL (a service where your private key stays on your own infrastructure), some caveats may apply.</p>
<p>When a visitor first connects to your site, Cloudflare must complete a TLS handshake (the initial negotiation that establishes an encrypted connection). If the data center handling the connection does not hold your private key, it must contact a key server in an authorized region. This extra step adds latency corresponding to the round-trip time between the two locations, which can be as much as a second if the key server is on the other side of the world. Once the handshake is complete, the key server is not involved. Furthermore, if the visitor reconnects within the TLS Session Resumption window (a mechanism that reuses previous connection parameters), the private key is not required. Hence, latency is only added for the initial connection establishment.</p>
<p>Learn more about how it works in our <a href="https://blog.cloudflare.com/geo-key-manager-how-it-works/">blog post</a>.</p>
<h2 id="regional-services">Regional Services</h2>
<p>When using Regional Services, some caveats and limitations may apply.</p>
<p>For product-specific caveats, refer to <a href="/data-localization/compatibility/">Cloudflare product compatibility</a> page.</p>
<p>The following features and protocols are not supported by Regional Services and will not work on regionalized hostnames:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/">ICMP</a> — Internet Control Message Protocol, used for network diagnostics like <code>ping</code></li>
<li><a href="/ssl/edge-certificates/ech/">Encrypted Client Hello (ECH)</a> — a privacy feature that encrypts the initial part of a TLS connection</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a> — origin-to-origin, a Cloudflare for SaaS setup</li>
<li><a href="/network/onion-routing/">Onion Routing (Tor)</a></li>
</ul>
<p>Since Regional Services leverages Spectrum (Cloudflare's Layer 4 proxy service) in the background, <a href="/spectrum/reference/limitations/">Spectrum limitations</a> apply.</p>
<h3 id="regional-hostnames-and-spectrum-applications">Regional hostnames and Spectrum applications</h3>
<p>Regional hostnames configured through the dashboard or the Regional Hostnames API only apply to hostnames <a href="/dns/proxy-status/">proxied</a> through Cloudflare. They do not regionalize <a href="/spectrum/">Spectrum</a> applications.</p>
<p>If a hostname has both a regional hostname configuration and an active Spectrum application, these are independent systems. The Spectrum application may override the regional hostname's IP steering with its own IP assignment. As a result, traffic may not be processed in the region configured via the Regional Hostnames API. If you need to regionalize a Spectrum application, contact your <a href="/support/contacting-cloudflare-support/">Account Team</a> about Spectrum-specific regionalization options. Spectrum-specific regionalization only applies to HTTP and HTTPS <a href="/spectrum/reference/configuration-options/#application-type">application types</a>.</p>
<p>Regional Services does not apply to <a href="/workers/platform/limits/#subrequests">subrequests</a> (secondary HTTP requests that your Cloudflare Workers make to other services). Regional Services operates on your hostname's IPs. We recommend using <a href="/learning-paths/application-security/default-traffic-security/dnssec/">DNSSEC</a> (which cryptographically signs DNS records to prevent tampering) and/or <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> (which encrypts DNS queries) to ensure that DNS responses are secure and correct.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>There are certain limitations and caveats when using Customer Metadata Boundary.</p>
<p>When you configure Customer Metadata Boundary to EU, most of the analytics and logging sections in the Cloudflare dashboard will show no data. To view your data, use <a href="/waf/analytics/security-analytics/">Security Analytics</a> (which respects CMB) or set up <a href="/logs/logpush/">Logpush</a> to export <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP request</a> logs to a storage destination you control.</p>
<p>To configure Customer Metadata Boundary to EU, you must disable Log Retention for all zones within your account. Log Retention is a legacy feature of <a href="/logs/logpull/">Logpull</a> (an older API for downloading logs, now superseded by Logpush).</p>
<p>For product-specific caveats, refer to <a href="/data-localization/compatibility/">Cloudflare product compatibility</a> page.</p>
<h3 id="data-unavailability">Data unavailability</h3>
<p>If you encounter a message on the dashboard indicating that your data is unavailable due to your account's Metadata Boundary configuration, this is because you are trying to access data that is not stored in your region (that is, you are in the US and trying to access data that is only stored in the EU, or vice versa). If you receive this error message while being in the region where your data is stored, there are two potential reasons why you might get this message:</p>
<ul>
<li>
<p>Your account has Customer Metadata Boundary (CMB) enabled, and your request is being directed to an incorrect region. For example, if you are in the EU and CMB is configured to store your data in the US.</p>
</li>
<li>
<p>If you are trying to access your data from the correct region, such as being in the EU with CMB configured to save your data in the EU, the issue may be caused by network congestion. Typically, this problem resolves within a few minutes.</p>
</li>
</ul>
<h3 id="dashboard-ui-analytics">Dashboard UI Analytics</h3>
<p>In some cases, when using Customer Metadata Boundary set to the EU, some Dashboard UI Analytics might show up empty.</p>
