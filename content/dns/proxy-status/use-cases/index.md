<p>This page lists common scenarios where DNS records should be <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7575.md")
</div> or set to DNS only, and describes aspects to keep in mind depending on your configuration. For background on how proxy status works, refer to [Proxy status](/dns/proxy-status/).
<h2 id="proxied-records">Proxied records</h2>
<p>You should proxy all A, AAAA, and CNAME records that serve HTTP or HTTPS web traffic. This includes records for:</p>
<ul>
<li>Your website or web application (for example, <code>example.com</code>, <code>www.example.com</code>)</li>
<li>Subdomains that serve web content (for example, <code>blog.example.com</code>, <code>app.example.com</code>)</li>
<li>API endpoints that accept HTTP/HTTPS requests and do not require origin IP validation</li>
</ul>
<p>Proxied records benefit from <a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">DDoS protection</a>, <a href="/cache/">caching</a>, <a href="/waf/">WAF</a>, and other Cloudflare security and performance features.</p>
<p>When traffic is proxied through Cloudflare, the following behaviors apply. You may need to adjust your origin configuration, depending on your use case.</p>
<h3 id="source-ip-changes">Source IP changes</h3>
<p>Your origin server sees Cloudflare IP addresses as the source of all requests instead of the end-user's IP address. Applications that rely on the source IP for authentication, rate limiting, or geolocation will not function as expected without additional configuration.</p>
<p>Cloudflare includes the original visitor IP address in the <a href="/fundamentals/reference/http-headers/"><code>CF-Connecting-IP</code></a> and <code>X-Forwarded-For</code> request headers. Configure your origin server to read the visitor IP from these headers. For more information, refer to <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Restoring original visitor IPs</a>.</p>
<h3 id="client-certificate-mtls-validation">Client certificate (mTLS) validation</h3>
<p>When a record is proxied, TLS terminates at Cloudflare's global network. Cloudflare establishes a separate TLS connection to your origin server. This means the origin never receives the end-user's client certificate during the TLS handshake. You can achieve mTLS through the following:</p>
<ul>
<li><a href="/ssl/client-certificates/">Client certificates (mTLS)</a>: validate client certificates between your end-users and Cloudflare.</li>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a>: Verify that traffic reaching your origin comes from Cloudflare.</li>
<li><a href="/ssl/client-certificates/forward-a-client-certificate/">Forward a client certificate</a>: Forward client certificate details to your origin via HTTP headers.</li>
</ul>
<h3 id="header-modifications">Header modifications</h3>
<p>Cloudflare adds and modifies HTTP request headers when proxying traffic, including headers for <a href="/fundamentals/reference/http-headers/">visitor IP identification</a>, diagnostics, and connection management. Applications that expect a fixed number of headers or parse headers by position instead of by name may experience errors.</p>
<p>For a full list of headers that Cloudflare adds or modifies, refer to <a href="/fundamentals/reference/http-headers/">HTTP request headers</a>.</p>
<h2 id="dns-only">DNS only</h2>
<p>The following records should be set to DNS-only because the services they support are not compatible with Cloudflare's HTTP proxy. Proxying these records causes the associated service to break.</p>
<h3 id="email">Email</h3>
<p>MX records cannot be proxied. If an A or AAAA record is used exclusively for email (for example, <code>mail.example.com</code>), it should also be set to DNS-only.</p>
<p>Cloudflare does not proxy SMTP traffic on port <code>25</code> by default. Proxying a record that handles email traffic causes mail servers to connect to Cloudflare's IP addresses instead of your mail server. This prevents email delivery.</p>
<p>Use a dedicated hostname for email that is separate from your proxied web traffic hostname. If your MX record points to the same hostname as your website, Cloudflare <a href="/dns/manage-dns-records/troubleshooting/unexpected-dns-records/#_dc-mx-and-dc--subdomains">dynamically prepends</a> <code>_dc-mx</code> to the hostname in the response for the MX record. This ensures that mail or service traffic bypasses the Cloudflare proxy and reaches your server directly.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7574.md")
</aside>
<h3 id="domain-verification">Domain verification</h3>
<p>Third-party services often require CNAME or TXT records to verify domain ownership. Proxying a verification CNAME record returns Cloudflare IP addresses instead of the expected verification target. The third-party service cannot match the response and verification fails.</p>
<p>Common services that require DNS-only verification records:</p>
<ul>
<li>Google Workspace</li>
<li>AWS Certificate Manager (<code>acm-validations.aws</code>)</li>
<li>Squarespace (<code>verify.squarespace.com</code>)</li>
<li>Amazon Amplify</li>
</ul>
<p>Set domain verification records to <strong>DNS Only</strong> until verification completes. Some services require the record to be DNS-only permanently.</p>
<h3 id="saas-hosted-websites">SaaS-hosted websites</h3>
<p>If your site is hosted on a SaaS platform (for example, <a href="/dns/manage-dns-records/reference/vendor-specific-records/#wix">Wix</a>, Squarespace, Webflow), the platform serves your site from its own infrastructure. Proxying the DNS record pointing to a SaaS platform causes one or more of the following issues:</p>
<ul>
<li><strong>SSL errors</strong>: Both Cloudflare and the SaaS platform attempt to terminate SSL, which causes certificate mismatches or handshake failures.</li>
<li><strong>Redirect loops</strong>: Both services try to redirect HTTP to HTTPS, which creates an infinite loop.</li>
<li><strong>Broken pages or assets</strong>: The platform rejects requests that do not come directly from the expected DNS resolution.</li>
</ul>
<p>If your SaaS platform does not explicitly support Cloudflare's proxy, set the record to <strong>DNS-only</strong>. Refer to <a href="/dns/manage-dns-records/reference/vendor-specific-records/">vendor-specific DNS records</a> for platform-specific guidance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7573.md")
</aside>
<h3 id="non-http-services">Non-HTTP services</h3>
<p>Records used for FTP, SSH, RDP, game servers, or other non-HTTP protocols must be DNS-only. Cloudflare's proxy only handles HTTP and HTTPS traffic. Proxying these records routes the traffic to Cloudflare, which drops the non-HTTP connection.</p>
<p>To proxy non-HTTP protocols, use <a href="/spectrum/">Cloudflare Spectrum</a>.</p>
<h3 id="other-cdn-or-proxy-providers">Other CDN or proxy providers</h3>
<p>If a CNAME record points to another CDN or proxy provider (for example, AWS CloudFront, Akamai, Fastly), proxying it through Cloudflare can cause conflicts between the two proxies:</p>
<ul>
<li><strong>SSL negotiation failures</strong>: Both proxies attempt to terminate TLS, which creates certificate chain errors.</li>
<li><strong>Routing loops</strong>: Each proxy forwards requests back to the other.</li>
<li><strong>Connectivity errors</strong>: The upstream CDN rejects requests from Cloudflare's IP addresses.</li>
</ul>
<p>Cloudflare automatically <a href="/dns/proxy-status/limitations/#proxy-eligibility">prevents proxying</a> for some known targets. For targets that are not automatically blocked, set the record to <strong>DNS-only</strong> if you experience connectivity issues.</p>
<h3 id="api-and-webhook-origin-validation">API and webhook origin validation</h3>
<p>Some third-party services validate the origin IP address of incoming API calls or webhook deliveries. When you proxy the DNS record for an endpoint that sends outbound requests or receives webhooks, the remote service sees Cloudflare's IP addresses instead of your server's IP address. This causes the validation to fail.</p>
<p>If a third-party service requires IP-based validation and does not accept <a href="https://www.cloudflare.com/ips/">Cloudflare's IP ranges</a>, set the record for that service to <strong>DNS-only</strong>.</p>
