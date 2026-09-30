<p>While your <a href="/dns/manage-dns-records/">DNS records</a> contain information about your domain, the proxy status controls whether HTTP/HTTPS traffic for that record routes through Cloudflare's network or goes directly to your origin server.</p>
<p>When a record is <strong>Proxied</strong>, Cloudflare sits between your visitors and your server — optimizing, caching, and protecting traffic along the way. When a record is <strong>DNS-only</strong>, Cloudflare responds with your server's actual IP address and does not route HTTP/HTTPS traffic through its network.</p>
<p>Only <a href="/dns/manage-dns-records/reference/dns-record-types/#ip-address-resolution">records used for IP address resolution</a> — A, AAAA, and CNAME records — can be proxied. Other record types (such as MX or TXT) are always DNS-only.</p>
<p>Cloudflare recommends proxying all A, AAAA, and CNAME records that serve web traffic. Records used for other purposes, such as <a href="/dns/manage-dns-records/troubleshooting/cname-domain-verification/">CNAME records that prove your domain ownership</a>, should not be proxied.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7584.md")
</aside>
<h3 id="benefits">Benefits</h3>
<p>When you set a DNS record to <strong>Proxied</strong> — shown as an orange cloud icon in the dashboard, also known as &quot;orange-clouded&quot; — Cloudflare can:</p>
<ul>
<li>Protect your origin server (the server hosting your website or application) from <a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">DDoS attacks</a>.</li>
<li><a href="/fundamentals/manage-domains/add-site/">Optimize, cache, and protect</a> all requests to your application.</li>
<li>Apply your Cloudflare product configurations (such as <a href="/waf/">WAF</a> rules, <a href="/cache/">caching</a>, and <a href="/rules/url-forwarding/">redirect rules</a>) to incoming traffic.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7583.md")
</aside>
<h3 id="example">Example</h3>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/7585.md")
</div>
<p>In the example DNS table above, there are two DNS records. The record with the name <code>blog</code> has proxy on, while the record named <code>shop</code> has the proxy off (that is, <strong>DNS only</strong>).</p>
<p>This means that:</p>
<ul>
<li>A DNS query to the proxied record <code>blog.example.com</code> will be answered with Cloudflare <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP addresses</a> — shared IP addresses used to route traffic through a nearby data center — instead of <code>192.0.2.1</code>. This ensures that HTTP/HTTPS requests for this name will be sent to Cloudflare's network and can be proxied, which allows the <a href="#benefits">benefits listed above</a>.</li>
<li>A DNS query to the DNS-only record <code>shop.example.com</code> will be answered with the actual origin IP address, <code>192.0.2.2</code>. This exposes your origin IP address to anyone who queries the record, which removes a layer of protection against targeted attacks. Cloudflare also cannot provide HTTP/HTTPS analytics on those requests (only DNS analytics).</li>
</ul>
<p>For further context, refer to <a href="/fundamentals/concepts/how-cloudflare-works/">How Cloudflare works</a>.</p>
<hr />
<h2 id="proxied-records">Proxied records</h2>
<p>The sections below describe specific behaviors and expected outcomes when you have DNS records set to <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7586.md")
</div>. There may also be some [limitations](/dns/proxy-status/limitations/) in specific scenarios.
<h3 id="predefined-time-to-live">Predefined time to live</h3>
<p>By default, all proxied records have a time to live (TTL) of <strong>Auto</strong>, which is set to 300 seconds. This value cannot be edited.</p>
<p>This short TTL ensures that if Cloudflare changes the <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP address</a> assigned to your record, the change takes effect quickly. Recursive resolvers — the DNS servers that look up records on behalf of end users — will not cache the old address for longer than 300 seconds (five minutes).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7582.md")
</aside>
<h3 id="mix-proxied-and-unproxied">Mix proxied and unproxied</h3>
<p>If you have multiple A or AAAA records on the same name and at least one of them is proxied, Cloudflare will treat all A or AAAA records on this name as being proxied.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7588.md")
</div></details>
<p>Cloudflare will also proxy a request if a hostname on a CNAME chain — where one CNAME record points to another — is proxied.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7591.md")
</div></details>
<h3 id="cname-records">CNAME records</h3>
<p>With <a href="/dns/cname-flattening/">CNAME flattening</a>, Cloudflare follows the CNAME chain to find the final IP address, helping DNS queries resolve faster. Proxied <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">CNAME records</a> are flattened by default, as they return Cloudflare anycast IPs.</p>
<p>In some cases, Cloudflare will show a warning message or <a href="/dns/proxy-status/limitations/#proxy-eligibility">prevent</a> you from proxying a CNAME record. This happens to avoid misconfigurations and is generally related to other CDN providers or to specific records used for <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DKIM</a> (email authentication) validation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7580.md")
</aside>
<h3 id="protocol-optimization">Protocol optimization</h3>
<p>For proxied records, if your domain has <a href="/speed/optimization/protocol/">HTTP/2 or HTTP/3 enabled</a> and is also using <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a>, Cloudflare automatically generates <a href="/dns/manage-dns-records/reference/dns-record-types/#svcb-and-https">HTTPS Service (HTTPS) records</a> on the fly. These DNS records provide clients with information about how to connect to your server upfront, without the need for an initial plaintext HTTP connection to discover supported protocols.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7579.md")
</aside>
<h3 id="request-and-response-size-limits">Request and response size limits</h3>
<p>Cloudflare enforces size limits on proxied requests. These limits vary by plan and cannot be bypassed while traffic is proxied. For the full list of connection and request limits, refer to <a href="/fundamentals/reference/connection-limits/">Connection limits</a>.</p>
<h3 id="connection-timeouts">Connection timeouts</h3>
<p>Cloudflare enforces a default <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a> between Cloudflare and your origin server. If your origin does not send an HTTP response within the defined time limit, Cloudflare returns a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/"><code>524</code> error</a>. Enterprise customers can <a href="/cache/how-to/cache-rules/settings/#proxy-read-timeout-enterprise-only">increase the timeout value</a>.</p>
<hr />
<h2 id="dns-only-records">DNS-only records</h2>
<p>When an A, AAAA, or CNAME record is <strong>DNS-only</strong> — shown as a gray cloud icon in the dashboard, also known as &quot;gray-clouded&quot; — DNS queries for these will resolve to the record's actual origin IP address, as described in the <a href="#example">example</a>.</p>
<p><strong>DNS-only</strong> is only recommended for records that do not serve web traffic, such as records used for email routing or third-party domain verification. For records that serve web traffic, <strong>DNS-only</strong> means your origin IP addresses are visible to anyone who queries the record, potentially exposing your server to bad actors and <a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">DDoS attacks</a>. Cloudflare also cannot <a href="/fundamentals/concepts/how-cloudflare-works/">optimize, cache, and protect</a> those requests or provide HTTP/HTTPS analytics on them.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7578.md")
</aside>
<h3 id="when-to-use-dns-only">When to use DNS-only</h3>
<p>Certain DNS records should be DNS-only because the services they support are not compatible with Cloudflare's HTTP proxy. Common examples include email records, domain verification records, SaaS-hosted websites, and non-HTTP services.</p>
<p>For a detailed list of scenarios, refer to <a href="/dns/proxy-status/use-cases/">Use cases</a>. For hard constraints on proxying, refer to <a href="/dns/proxy-status/limitations/">Proxying limitations</a>.</p>
