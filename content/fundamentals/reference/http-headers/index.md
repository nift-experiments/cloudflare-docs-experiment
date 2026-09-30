<h2 id="request-headers">Request headers</h2>
<p>Cloudflare passes all HTTP request headers to your origin web server and adds additional headers as specified below.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8792.md")
</aside>
<h3 id="accept-encoding">Accept-Encoding</h3>
<p>For incoming requests, the value of this header will always be set to <code>accept-encoding: br, gzip</code>. If the client set a different value, such as <code>accept-encoding: deflate</code>, it will be overwritten and the original value will be available in <code>request.cf.clientAcceptEncoding</code>.</p>
<h3 id="cf-connecting-ip">CF-Connecting-IP</h3>
<p><code>CF-Connecting-IP</code> provides the client IP address connecting to Cloudflare to the origin web server.
This header will only be sent on the traffic from Cloudflare's edge to your origin web server.</p>
<p>For guidance on logging your visitor's original IP address, refer to <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Restoring original visitor IPs</a>.</p>
<p>Alternatively, if you do not wish to receive the <code>CF-Connecting-IP</code> header or any HTTP header that may contain the visitor's IP address, <a href="/rules/transform/managed-transforms/configure/">enable the <strong>Remove visitor IP headers</strong> Managed Transform</a>.</p>
<h4 id="cf-connecting-ip-in-worker-subrequests">CF-Connecting-IP in Worker subrequests</h4>
<p>In same-zone Worker subrequests, the value of <code>CF-Connecting-IP</code> reflects the value of <code>x-real-ip</code> (the client's IP). <code>x-real-ip</code> can be altered by the user in their Worker script.</p>
<p>In cross-zone subrequests from one Cloudflare zone to another Cloudflare zone, the <code>CF-Connecting-IP</code> value will be set to the Worker client IP address <code>'2a06:98c0:3600::103'</code> for security reasons.</p>
<p>For Worker subrequests destined for a non-Cloudflare customer zone, the <code>CF-Connecting-IP</code> and <code>x-real-ip</code> headers will both reflect the client's IP address, with only the <code>x-real-ip</code> header able to be altered.</p>
<p>When no Worker subrequest is triggered, <code>cf-connecting-ip</code> reflects the client's IP address and the <code>x-real-ip</code> header is stripped.</p>
<h3 id="cf-connecting-ipv6">CF-Connecting-IPv6</h3>
<p>Cloudflare provides <a href="/network/ipv6-compatibility/">free IPv6 support</a> to all domains without requiring additional configuration or hardware. To support migrating to IPv6, Cloudflare's <a href="/network/pseudo-ipv4/">Pseudo IPv4</a> provides an IPv6 to IPv4 translation service for all Cloudflare domains.</p>
<p>If <strong>Pseudo IPv4</strong> is set to <code>Overwrite Headers</code> - Cloudflare overwrites the existing <code>Cf-Connecting-IP</code> and <code>X-Forwarded-For</code> headers with a pseudo IPv4 address while preserving the real IPv6 address in <code>CF-Connecting-IPv6</code> header.
<br /></p>
<h3 id="cf-ew-via">CF-EW-Via</h3>
<p>This header is used for loop detection, similar to the <code>CDN-Loop</code> <a href="https://blog.cloudflare.com/preventing-request-loops-using-cdn-loop/">header</a>.</p>
<h3 id="cf-pseudo-ipv4">CF-Pseudo-IPv4</h3>
<p>If <a href="/network/pseudo-ipv4/">Pseudo IPv4</a> is set to <code>Add Header</code> - Cloudflare automatically adds the <code>CF-Pseudo-IPv4</code> header with a Class E IPv4 address hashed from the original IPv6 address.</p>
<h3 id="true-client-ip-enterprise-plan-only">True-Client-IP (Enterprise plan only)</h3>
<p><code>True-Client-IP</code> provides the original client IP address to the origin web server. <code>True-Client-IP</code> is only available on an Enterprise plan. In the example below, <code>203.0.113.1</code> is the original visitor IP address. For example: <code>True-Client-IP: 203.0.113.1</code></p>
<p>There is no difference between the <code>True-Client-IP</code> and <code>CF-Connecting-IP</code> headers besides the name of the header. Some Enterprise customers with legacy devices need <code>True-Client-IP</code> to avoid updating firewalls or load-balancers to read a custom header name.</p>
<p>To add a <code>True-Client-IP</code> HTTP header to requests, <a href="/rules/transform/managed-transforms/configure/">enable the <strong>Add &quot;True-Client-IP&quot; header</strong> Managed Transform</a>.</p>
<p>Alternatively, if you do not wish to receive the <code>True-Client-IP</code> header or any HTTP header that may contain the visitor's IP address, <a href="/rules/transform/managed-transforms/configure/">enable the <strong>Remove visitor IP headers</strong> Managed Transform</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8791.md")
</aside>
<h3 id="x-forwarded-for">X-Forwarded-For</h3>
<p><code>X-Forwarded-For</code> maintains proxy server and original visitor IP addresses. If there was no existing <code>X-Forwarded-For</code>header in the request sent to Cloudflare, <code>X-Forwarded-For</code> has an identical value to the <code>CF-Connecting-IP</code> header.</p>
<p>For example, if the original visitor IP address is <code>203.0.113.1</code> and the request sent to Cloudflare does not contain an <code>X-Forwarded-For</code> header, then Cloudflare will send <code>X-Forwarded-For: 203.0.113.1</code> to the origin.</p>
<p>If, on the other hand, an <code>X-Forwarded-For</code> header was already present in the request to Cloudflare, Cloudflare will append the IP address of the HTTP proxy connecting to Cloudflare to the header. For example, if the original visitor IP address is <code>203.0.113.1</code> and a request is proxied through two proxies: proxy A with an IP address of <code>198.51.100.101</code> and proxy B with an IP address of <code>198.51.100.102</code> before being proxied to Cloudflare, then Cloudflare will send <code>X-Forwarded-For: 203.0.113.1,198.51.100.101,198.51.100.102</code> to the origin. Proxy A will append the original visitor's IP address (<code>203.0.113.1</code>) to <code>X-Forwarded-For</code> before proxying the request to proxy B which, in turn, will append Proxy A's IP address (<code>198.51.100.101</code>) to <code>X-Forwarded-For</code> before proxying the request to Cloudflare. And finally, Cloudflare will append proxy B's IP address (<code>198.51.100.102</code>) to <code>X-Forwarded-For</code> before proxying the request to the origin.</p>
<p>If you do not wish to receive the visitor's IP address (and other intermediate proxy IP addresses) in the <code>X-Forwarded-For</code> header, or any HTTP header that may contain the visitor's IP address, <a href="/rules/transform/managed-transforms/configure/">enable the <strong>Remove visitor IP headers</strong> Managed Transform</a>. For the <code>X-Forwarded-For</code> header specifically, this Managed Transform will only remove the visitor IP from the header value when Cloudflare receives a request proxied by at least another CDN. In this case, Cloudflare will only keep the IP address of the last proxy.</p>
<p>Using the previous example where a request was proxied twice (proxies A and B) before being proxied through Cloudflare, with <strong>Remove visitor IP headers</strong> enabled, Cloudflare would send <code>X-Forwarded-For: 198.51.100.102</code> to the origin, keeping only proxy B's IP address (the last proxy before Cloudflare). Refer to <a href="/rules/transform/managed-transforms/reference/#visitor-ip-address-in-the-x-forwarded-for-http-header">Visitor IP address in the <code>x-forwarded-for</code> HTTP header</a> for more details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8790.md")
</aside>
<h3 id="x-forwarded-proto">X-Forwarded-Proto</h3>
<p><code>X-Forwarded-Proto</code> is used to identify the protocol (HTTP or HTTPS) that a visitor used to connect to Cloudflare. By default, the protocol used is <code>https</code>, unless the visitor selected a different <a href="/ssl/origin-configuration/ssl-modes/#custom-ssltls">encryption mode</a>.</p>
<p>For incoming requests, the value of this header will be set to the protocol the client used (<code>http</code> or <code>https</code>). If the client set a different value, it will be overwritten.</p>
<h3 id="cf-ray">Cf-Ray</h3>
<p>The <code>Cf-Ray</code> header (otherwise known as a <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a>) is a hashed value that encodes information about the data center and the visitor's request. For example: <code>Cf-Ray: 230b030023ae2822-SJC</code>.</p>
<p>The Cf-Ray header identifies the data center processing the request when displayed as a response header. This is represented by a three-letter code corresponding to the data center's location.</p>
<p>The Cf-Ray header is also sent to upstream origins and may be modified to reflect the connecting data center. This occurs when a request is routed through <a href="/argo-smart-routing/">Argo Smart Routing</a> or <a href="/cache/how-to/tiered-cache/">Argo Tiered Caching</a>. In such cases, the three-letter code in the Cf-Ray header will indicate the data center connecting to the origin, not the ingress data center.</p>
<p>Add the <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#add-the-cf-ray-header-to-your-logs"><code>Cf-Ray</code> header to your origin web server logs</a> to match requests proxied to Cloudflare to requests in your server logs.</p>
<p>Enterprise customers can see all requests via <a href="/logs/">Cloudflare Logs</a>, including data related to the ingress data center.</p>
<h3 id="cf-ipcountry">CF-IPCountry</h3>
<p>The <code>CF-IPCountry</code> header contains a two-character country code of the originating visitor's country.</p>
<p>Besides the <a href="https://www.iso.org/iso-3166-country-codes.html">ISO-3166-1 alpha-2 codes</a>, Cloudflare uses the following special country codes:</p>
<ul>
<li><code>XX</code> - Used for clients without country code data.</li>
<li><code>T1</code> - Used for clients using the Tor network.</li>
</ul>
<p>To add this header to requests, along with other HTTP headers with location information for the visitor's IP address, <a href="/rules/transform/managed-transforms/configure/">enable the <strong>Add visitor location headers</strong> Managed Transform</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8789.md")
</aside>
<h3 id="cf-visitor">CF-Visitor</h3>
<p>Currently, this header is a JSON object, containing only one key called <code>scheme</code>. The header will be either HTTP or HTTPS, and it is only relevant if you need to enable Flexible SSL in your Cloudflare settings. For example: <code>CF-Visitor: { \&quot;scheme\&quot;:\&quot;https\&quot;}</code>.</p>
<h3 id="cdn-loop">CDN-Loop</h3>
<p><code>CDN-Loop</code> allows Cloudflare to specify how many times a request can enter Cloudflare's network before it is blocked as a looping request. For example: <code>CDN-Loop: cloudflare</code>.</p>
<h3 id="cf-connecting-o2o">CF-Connecting-O2O</h3>
<p>If <a href="/cloudflare-for-platforms/cloudflare-for-saas/">SSL for SaaS</a> is used for <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">the SaaS provider-owned zone</a>, a HTTP header will be set to <code>cf-connecting-o2o: 1</code>.</p>
<h3 id="cf-worker">CF-Worker</h3>
<p>The <code>CF-Worker</code> request header is added to an edge Worker subrequest that identifies the host that spawned the subrequest. For example: <code>CF-Worker: example.com</code>.</p>
<p>You can add <code>CF-Worker</code> header on server logs similar to the way you add the <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#add-the-cf-ray-header-to-your-logs"><code>CF-RAY</code></a> header. To do that, add <code>$http_cf_worker</code> in the log format file: <code>log_format cf_custom &quot;CF-Worker:$http_cf_worker&quot;'</code></p>
<p><code>CF-Worker</code> is added to all Worker subrequests sent via <code>fetch()</code>. It is set to the name of the zone which owns the Worker making the subrequest. For example, a Worker script on route for <code>foo.example.com/*</code> from <code>example.com</code> will have all subrequests with the header:</p>
<pre><code class="language-txt">CF-Worker: example.com&#10;</code></pre>
<p>The intended purpose of this header is to provide a means for recipients (for example, origins, load balancers, other Workers) to recognize, filter, and route traffic generated by Workers on specific zones.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8788.md")
</aside>
<h3 id="connection">Connection</h3>
<p>For incoming requests, the value of this header will always be set to <code>Keep-Alive</code>. If the client set a different value, such as <code>close</code>, it will be overwritten. Note that is also the case when the client uses HTTP/2 or HTTP/3 to connect.</p>
<h3 id="considerations-for-spectrum">Considerations for Spectrum</h3>
<p>When using Spectrum with a TCP application, these headers are not visible at the origin as they are HTTP headers. If you wish to utilize these in your application, there are two options:</p>
<ul>
<li>Use an HTTP or HTTPS Spectrum app instead of TCP</li>
<li>Use the <a href="/spectrum/how-to/enable-proxy-protocol/">Proxy Protocol feature</a></li>
</ul>
<h2 id="response-headers">Response headers</h2>
<p>Cloudflare will remove some HTTP headers from the response sent back to the visitor and add some Cloudflare-specific HTTP headers.</p>
<h3 id="removed-response-headers">Removed response headers</h3>
<p>Cloudflare passes all HTTP headers in the response from the origin server back to the visitor with the exception of the following headers:</p>
<ul>
<li><code>X-Accel-Buffering</code></li>
<li><code>X-Accel-Charset</code></li>
<li><code>X-Accel-Limit-Rate</code></li>
<li><code>X-Accel-Redirect</code></li>
<li><code>Alt-Svc</code></li>
</ul>
<h3 id="added-response-headers">Added response headers</h3>
<p>Cloudflare adds the HTTP headers specified below to the response sent to the visitor.</p>
<h4 id="cf-ray-1">Cf-Ray</h4>
<p>The <code>Cf-Ray</code> value returned to the visitor will be the same <code>Cf-Ray</code> value that was sent to the origin server.</p>
<h4 id="cf-cache-status">Cf-Cache-Status</h4>
<p>A list of all possible <code>Cf-Cache-Status</code> values is contained in <a href="/cache/concepts/cache-responses/">Cloudflare cache responses</a>.</p>
