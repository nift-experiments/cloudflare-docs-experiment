<p>Gateway supports the detection, logging, and filtering of network protocols using packet attributes.</p>
<p>Protocol detection only applies to devices connected to Cloudflare One via the Cloudflare One Client in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default">Traffic and DNS mode</a> mode.</p>
<h2 id="turn-on-protocol-detection">Turn on protocol detection</h2>
<p>To turn on protocol detection:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong> &gt; <strong>Proxy and inspection settings</strong>.</li>
<li>Turn on <strong>Allow protocol detection</strong>.</li>
</ol>
<p>You can now use <em>Detected Protocol</em> as a selector in a <a href="/cloudflare-one/traffic-policies/network-policies/#detected-protocol">Network policy</a>.</p>
<h3 id="inspect-on-all-ports">Inspect on all ports</h3>
<p>By default, Gateway will only inspect HTTP traffic through port <code>80</code>. Additionally, if you <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption">turn on TLS decryption</a>, Gateway will inspect HTTPS traffic through port <code>443</code>.</p>
<p>To detect and inspect HTTP and HTTPS traffic on ports in addition to <code>80</code> and <code>443</code>, <p>under <strong>Manage HTTP inspection by port</strong>, choose <em>Inspect on all ports</em></p>
.</p>
<h4 id="important-considerations">Important considerations</h4>
<p><strong>TLS interception on all ports</strong>: When you turn on this setting, Gateway will attempt to intercept TLS traffic on every port, not just port <code>443</code>. This means all applications using TLS on non-standard ports will have their traffic intercepted by the Gateway proxy. If you only want to turn on SNI detection for Network policy filtering without full TLS interception, you will need to create <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#do-not-inspect">Do Not Inspect policies</a> for the specific applications or domains that use TLS on non-standard ports.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="non-http-protocols-inside-tls-bypass-network-policy-filtering">Non-HTTP protocols inside TLS bypass network policy filtering</h3>
@markup("md", "content/.markup/bodies/6421.md")
</aside>
<p>To use HTTP policies to filter all HTTPS traffic on all ports when using a default Block Network policy, <a href="/cloudflare-one/traffic-policies/network-policies/common-policies/#filter-https-traffic-when-inspecting-on-all-ports">create a Network policy to explicitly allow HTTP and TLS traffic</a>.</p>
<h2 id="supported-protocols">Supported protocols</h2>
<p>Gateway supports detection and filtering of the following protocols:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP</td>
<td>Hypertext Transfer Protocol (HTTP/1.1).</td>
</tr>
<tr>
<td>HTTP2</td>
<td>Hypertext Transfer Protocol Version 2.</td>
</tr>
<tr>
<td>SSH</td>
<td>Secure Shell Protocol — remote login and command execution.</td>
</tr>
<tr>
<td>TLS</td>
<td>Transport Layer Security. Gateway detects TLS versions 1.1 through 1.3 with the <em>TLS</em> value.</td>
</tr>
<tr>
<td>DCERPC</td>
<td>Distributed Computing Environment / Remote Procedure Call.</td>
</tr>
<tr>
<td>MQTT</td>
<td>Message Queuing Telemetry Transport — lightweight IoT messaging protocol.</td>
</tr>
<tr>
<td>TPKT</td>
<td>TPKT commonly initiates RDP sessions, so you can use it to identify and filter RDP traffic.</td>
</tr>
<tr>
<td>IMAP</td>
<td>Internet Message Access Protocol — email retrieval.</td>
</tr>
<tr>
<td>POP3</td>
<td>Post Office Protocol v3 — email retrieval.</td>
</tr>
<tr>
<td>SMTP</td>
<td>Simple Mail Transfer Protocol — email sending.</td>
</tr>
<tr>
<td>MYSQL</td>
<td>MySQL database wire protocol.</td>
</tr>
<tr>
<td>RSYNC-DAEMON</td>
<td>rsync daemon protocol.</td>
</tr>
<tr>
<td>LDAP</td>
<td>Lightweight Directory Access Protocol.</td>
</tr>
<tr>
<td>NTP</td>
<td>Network Time Protocol.</td>
</tr>
</tbody>
</table>
<h2 id="example-network-policy">Example network policy</h2>
<p>You can create network policies that filter traffic based on protocol detections rather than common ports. For example, you can block all SSH traffic on your network without blocking port 22 or any other non-default ports:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Detected Protocol</td>
<td>in</td>
<td><em>SSH</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
