<p>This guide covers common HTTP/2 and HTTP/3 issues, including origin incompatibility, multiplexing errors, and browser errors, with steps to diagnose and resolve them.</p>
<h2 id="h2-to-origin-origin-incompatibility">H2 to Origin - Origin incompatibility</h2>
<ul>
<li>The origin's <code>max_concurrent_streams</code> is negotiated during the handshake process.</li>
<li>If a <code>GOAWAY(0)</code> is received, it is likely due to a server restart or another reason causing the server to refuse new streams.</li>
<li>For more information, refer to <a href="https://datatracker.ietf.org/doc/html/rfc9113">RFC 9113 - SETTINGS_MAX_CONCURRENT_STREAMS</a>.</li>
</ul>
<h2 id="h2-multiplexing-origin-incompatibility-issues">H2 Multiplexing - Origin incompatibility/issues</h2>
<ul>
<li>Multiplexing issues can arise due to incorrect server configurations.</li>
<li>Use <a href="https://www.chromium.org/developers/design-documents/network-stack/netlog/">netlogs</a> to identify <code>SETTINGS_MAX_CONCURRENT_STREAMS</code> violations or unexpected <code>GOAWAY</code> frames.</li>
<li>For more information, refer to <a href="https://datatracker.ietf.org/doc/html/rfc9113#name-stream-concurrency">Stream Concurrency Issues</a>.</li>
</ul>
<h2 id="generic-browser-errors">Generic browser errors</h2>
<p>Common browser errors include:</p>
<ul>
<li><code>ERR_HTTP2_PROTOCOL_ERROR</code></li>
<li><code>ERR_HTTP3_PROTOCOL_ERROR</code></li>
<li><code>ERR_QUIC_PROTOCOL_ERROR</code></li>
</ul>
<p>These errors do not necessarily indicate a protocol-level issue. Follow these steps:</p>
<ol>
<li>Attempt reproduction using HTTP/1.1.</li>
<li>If the issue persists in HTTP/1.1, address the underlying error before testing HTTP/2 or HTTP/3.</li>
<li>If the issue does not persist, analyze netlogs for HTTP/2 or HTTP/3-specific issues.</li>
</ol>
<p>For more information, refer to <a href="https://chromium.googlesource.com/chromium/src/+/HEAD/net/url_request/url_request.h">Chromium URL Request Header</a>.</p>
<h2 id="chrome-stalls-or-fails-only-on-http-3">Chrome stalls or fails only on HTTP/3</h2>
<p>If the issue reproduces only in Chrome over HTTP/3 and disappears when HTTP/3 is disabled, the problem may be related to a browser-side QUIC handling issue rather than your origin server. This is a known Chrome issue (<a href="https://issues.chromium.org/issues/41161335">crbug.com/41161335</a>) — Cloudflare's QUIC implementation is not the cause.</p>
<p>Symptoms can include:</p>
<ul>
<li>Large downloads stall unexpectedly.</li>
<li>Pages with many concurrent requests hang for one to three minutes and then fail.</li>
<li>Chrome reports <code>ERR_QUIC_PROTOCOL_ERROR</code> or <code>ERR_HTTP3_PROTOCOL_ERROR</code> after the connection stops making progress.</li>
<li>Issue does not reproduce in Firefox or Safari.</li>
<li>Issue resolves after disabling QUIC in <code>chrome://flags</code>.</li>
</ul>
<h3 id="how-to-isolate-the-issue">How to isolate the issue</h3>
<ol>
<li>Temporarily disable HTTP/3 for the zone.</li>
<li>Test the same request again over HTTP/2.</li>
<li>If the issue disappears over HTTP/2, capture a NetLog for Chrome and compare the behavior.</li>
</ol>
<p><strong>Test immediately:</strong> In Chrome, go to <code>chrome://flags</code>, search for &quot;QUIC&quot;, set it to <strong>Disabled</strong>, then relaunch Chrome.</p>
<h3 id="resolution">Resolution</h3>
<p>If the issue is limited to specific hostnames, you can apply a more targeted workaround: create a Response Header Modification Transform Rule to remove the <code>Alt-Svc</code> header for the affected hostname.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
<li>Select <strong>Create rule</strong> &gt; <strong>Response Header Transform Rule</strong>.</li>
<li>Set the matching expression to your hostname: <code>(http.host eq &quot;example.com&quot;)</code>.</li>
<li>Under <strong>Modify response header</strong>, select <strong>Remove</strong> and enter <code>Alt-Svc</code> as the header name.</li>
</ol>
<p>This forces Chrome to use HTTP/2 for that hostname without disabling HTTP/3 globally. However, proxied hostnames can also advertise HTTP/3 through generated HTTPS records, so disabling HTTP/3 for the zone is the most reliable way to force HTTP/2 while you troubleshoot.</p>
<p>After changing <code>Alt-Svc</code>, remember that browsers may cache the advertised alternative service for up to 24 hours.</p>
