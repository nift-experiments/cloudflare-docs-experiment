<p>Your <a href="https://www.cloudflare.com/learning/cdn/glossary/origin-server">origin server</a> is a physical or virtual machine that is not owned by Cloudflare and hosts your application content (data, webpages, etc.).</p>
<p>Receiving too many requests can be bad for your origin. These requests might increase latency for visitors, incur higher costs — particularly for cloud-based machines — and could knock your application offline.</p>
<h2 id="secure-origin-connections">Secure origin connections</h2>
<p>When you secure origin connections, it prevents attackers from discovering and overloading your origin server with requests.</p>
<ul>
<li><strong>DNS</strong>:
<ol>
<li><strong>Proxy records</strong> (when possible): Set up <a href="/dns/proxy-status/">proxied (orange-clouded) DNS records</a> to hide your origin IP addresses and provide DDoS protection. As part of this, you should <a href="/fundamentals/concepts/cloudflare-ip-addresses/">allow Cloudflare IP addresses</a> at your origin to prevent requests from being blocked.</li>
<li><strong>Review DNS-only records</strong>: Audit existing <strong>DNS-only</strong> records (<code>SPF</code>, <code>TXT</code>, and more) to make sure they do not contain origin IP information.</li>
<li><strong>Evaluate mail infrastructure</strong>: If possible, do not host a mail service on the same server as the web resource you want to protect, since emails sent to non-existent addresses get bounced back to the attacker and reveal the mail server IP.</li>
<li><strong>Rotate origin IPs</strong>: Once <a href="/dns/zone-setups/full-setup/setup/#35-verify-changes">onboarded</a>, rotate your origin IPs, as DNS records are in the public domain. Historical records are kept and would contain IP addresses prior to joining Cloudflare</li>
</ol>
</li>
</ul>
<h3 id="application-layer">Application layer</h3>
<details class="nb-details"><summary>Cloudflare Tunnel (HTTP / WebSockets)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8757.md")
</div></details>
<details class="nb-details"><summary>HTTP Header Validation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8758.md")
</div></details>
<details class="nb-details"><summary>JSON Web Tokens (JWT) Validation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8759.md")
</div></details>
<h3 id="transport-layer">Transport Layer</h3>
<details class="nb-details"><summary>Authenticated Origin Pulls</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8760.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Tunnel (SSH / RDP)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8761.md")
</div></details>
<h3 id="network-layer">Network Layer</h3>
<details class="nb-details"><summary>Allowlist Cloudflare IP addresses</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8762.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Magic Transit</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8763.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Network Interconnect</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8764.md")
</div></details>
<details class="nb-details"><summary>Dedicated CDN Egress IPs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8767.md")
</div></details>
<h2 id="monitor-origin-health">Monitor origin health</h2>
<p>For passive monitoring, <a href="/notifications/get-started/#create-a-notification">create notifications</a> for <strong>Origin Error Rate Alerts</strong> to receive alerts when your origin returns 5xx codes above a configurable threshold and <strong>Passive Origin Monitoring</strong> to see when Cloudflare is unable to reach your origin for a few minutes.</p>
<p>For more active monitoring, set up <a href="/health-checks/">standalone health checks</a> for your origin.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8756.md")
</aside>
<h3 id="zero-downtime-failover">Zero Downtime Failover</h3>
<p>If you have another <code>A</code> or <code>AAAA</code> record in your Cloudflare <strong>DNS</strong> or your Cloudflare <strong>Load Balancer</strong> provides another <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8768.md")
</div> in the same pool, **Zero-Downtime Failover** automatically retries requests to your origin even before a Load Balancing decision is made.
<p>Zero-downtime failover will trigger a single retry only if there is another healthy endpoint in the pool and a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/">521, 522, 523, 525 or 526 error code</a> is occurring. No other error codes will trigger a zero-downtime failover operation.</p>
<br />
<h2 id="reduce-origin-traffic">Reduce origin traffic</h2>
<h3 id="block-traffic">Block traffic</h3>
<p>For more details, refer to <a href="/learning-paths/application-security/account-security/">Secure your website</a>.</p>
<h3 id="increase-caching">Increase caching</h3>
<p>The <a href="/cache/">cache</a> stores data from your application (webpages, etc.) at Cloudflare data centers around the world, which reduces the number of requests sent to your origin server.</p>
<h3 id="distribute-traffic">Distribute traffic</h3>
<p>To randomly distribute traffic across multiple servers, <a href="/dns/manage-dns-records/how-to/round-robin-dns/">set up multiple DNS records</a>.</p>
<p>For more fine-grained control over traffic distribution — including automatic failover, intelligent routing, and more — set up our <a href="/load-balancing/">add-on load balancing service</a>.</p>
<p>To protect specific endpoints from being overwhelmed by traffic spikes, <a href="/waiting-room/">set up a waiting room</a>.</p>
