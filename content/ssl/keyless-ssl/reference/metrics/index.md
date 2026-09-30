<p>The gokeyless key server exposes a <a href="https://prometheus.io/">Prometheus</a> metrics endpoint that you can use to monitor signing performance, error rates, connection health, and certificate expiry. This endpoint can also be scraped by the OpenTelemetry Collector Prometheus receiver, making the metrics available to any OpenTelemetry-compatible backend.</p>
<h2 id="metrics-endpoint">Metrics endpoint</h2>
<p>By default, metrics are served at:</p>
<pre><code class="language-txt">http://&lt;host&gt;:2406/metrics&#10;</code></pre>
<p>The port is configurable via the <code>metrics_port</code> key in your configuration file, the <code>--metrics-port</code> flag, or the <code>KEYLESS_METRICS_PORT</code> environment variable.</p>
<p>The endpoint serves only <code>/metrics</code>. There are no additional HTTP endpoints such as <code>/health</code> or <code>/debug</code>.</p>
<hr />
<h2 id="histogram-buckets">Histogram buckets</h2>
<p>All histogram metrics share the same bucket configuration: 15 exponential buckets starting at 100 microseconds, doubling each step up to approximately 1.64 seconds, plus a final <code>+Inf</code> bucket.</p>
<table>
<thead>
<tr>
<th>Bucket</th>
<th>Upper bound</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>100 µs</td>
</tr>
<tr>
<td>2</td>
<td>200 µs</td>
</tr>
<tr>
<td>3</td>
<td>400 µs</td>
</tr>
<tr>
<td>4</td>
<td>800 µs</td>
</tr>
<tr>
<td>5</td>
<td>1.6 ms</td>
</tr>
<tr>
<td>6</td>
<td>3.2 ms</td>
</tr>
<tr>
<td>7</td>
<td>6.4 ms</td>
</tr>
<tr>
<td>8</td>
<td>12.8 ms</td>
</tr>
<tr>
<td>9</td>
<td>25.6 ms</td>
</tr>
<tr>
<td>10</td>
<td>51.2 ms</td>
</tr>
<tr>
<td>11</td>
<td>102 ms</td>
</tr>
<tr>
<td>12</td>
<td>205 ms</td>
</tr>
<tr>
<td>13</td>
<td>410 ms</td>
</tr>
<tr>
<td>14</td>
<td>819 ms</td>
</tr>
<tr>
<td>15</td>
<td>~1.64 s</td>
</tr>
<tr>
<td>+Inf</td>
<td>Anything above ~1.64 s</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14199.md")
</aside>
<hr />
<h2 id="metrics-reference">Metrics reference</h2>
<h3 id="keyless-requests"><code>keyless_requests</code></h3>
<p><strong>Type:</strong> Counter<br />
<strong>Labels:</strong> <code>opcode</code></p>
<p>Counts every incoming request received over an established connection, regardless of outcome. Incremented once per request before any processing begins.</p>
<p>The <code>opcode</code> label uses the full constant name from the gokeyless protocol.</p>
<h4 id="rsa-operations">RSA operations</h4>
<table>
<thead>
<tr>
<th><code>opcode</code> label</th>
<th>Wire value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>OpRSADecrypt</code></td>
<td><code>0x01</code></td>
<td>RSA raw decryption — used in TLS RSA key exchange (deprecated in TLS 1.3)</td>
</tr>
<tr>
<td><code>OpRSASignMD5SHA1</code></td>
<td><code>0x02</code></td>
<td>RSA PKCS#1 v1.5 signature over MD5+SHA1 combined hash — TLS 1.0/1.1 handshake</td>
</tr>
<tr>
<td><code>OpRSASignSHA1</code></td>
<td><code>0x03</code></td>
<td>RSA PKCS#1 v1.5 signature over SHA1</td>
</tr>
<tr>
<td><code>OpRSASignSHA224</code></td>
<td><code>0x04</code></td>
<td>RSA PKCS#1 v1.5 signature over SHA224</td>
</tr>
<tr>
<td><code>OpRSASignSHA256</code></td>
<td><code>0x05</code></td>
<td>RSA PKCS#1 v1.5 signature over SHA256</td>
</tr>
<tr>
<td><code>OpRSASignSHA384</code></td>
<td><code>0x06</code></td>
<td>RSA PKCS#1 v1.5 signature over SHA384</td>
</tr>
<tr>
<td><code>OpRSASignSHA512</code></td>
<td><code>0x07</code></td>
<td>RSA PKCS#1 v1.5 signature over SHA512</td>
</tr>
<tr>
<td><code>OpRSAPSSSignSHA256</code></td>
<td><code>0x35</code></td>
<td>RSASSA-PSS signature over SHA256 — primary RSA operation in TLS 1.3</td>
</tr>
<tr>
<td><code>OpRSAPSSSignSHA384</code></td>
<td><code>0x36</code></td>
<td>RSASSA-PSS signature over SHA384</td>
</tr>
<tr>
<td><code>OpRSAPSSSignSHA512</code></td>
<td><code>0x37</code></td>
<td>RSASSA-PSS signature over SHA512</td>
</tr>
</tbody>
</table>
<h4 id="ecdsa-operations">ECDSA operations</h4>
<table>
<thead>
<tr>
<th><code>opcode</code> label</th>
<th>Wire value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>OpECDSASignMD5SHA1</code></td>
<td><code>0x12</code></td>
<td>ECDSA signature over MD5+SHA1 combined hash</td>
</tr>
<tr>
<td><code>OpECDSASignSHA1</code></td>
<td><code>0x13</code></td>
<td>ECDSA signature over SHA1</td>
</tr>
<tr>
<td><code>OpECDSASignSHA224</code></td>
<td><code>0x14</code></td>
<td>ECDSA signature over SHA224</td>
</tr>
<tr>
<td><code>OpECDSASignSHA256</code></td>
<td><code>0x15</code></td>
<td>ECDSA signature over SHA256 — most common in TLS 1.2 and TLS 1.3</td>
</tr>
<tr>
<td><code>OpECDSASignSHA384</code></td>
<td><code>0x16</code></td>
<td>ECDSA signature over SHA384</td>
</tr>
<tr>
<td><code>OpECDSASignSHA512</code></td>
<td><code>0x17</code></td>
<td>ECDSA signature over SHA512</td>
</tr>
</tbody>
</table>
<h4 id="other-signing">Other signing</h4>
<table>
<thead>
<tr>
<th><code>opcode</code> label</th>
<th>Wire value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>OpEd25519Sign</code></td>
<td><code>0x18</code></td>
<td>Ed25519 signature over an arbitrary-length payload (not a pre-hashed digest)</td>
</tr>
</tbody>
</table>
<h4 id="sealing-and-infrastructure-operations">Sealing and infrastructure operations</h4>
<table>
<thead>
<tr>
<th><code>opcode</code> label</th>
<th>Wire value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>OpSeal</code></td>
<td><code>0x21</code></td>
<td>Encrypt a blob using the server's sealing key — used for TLS session tickets</td>
</tr>
<tr>
<td><code>OpUnseal</code></td>
<td><code>0x22</code></td>
<td>Decrypt a blob previously encrypted by <code>OpSeal</code>. Returns <code>ErrExpired</code> if the sealing key has rotated</td>
</tr>
<tr>
<td><code>OpRPC</code></td>
<td><code>0x23</code></td>
<td>Execute a named function registered on the server. Available to all connection types</td>
</tr>
<tr>
<td><code>OpCustom</code></td>
<td><code>0x24</code></td>
<td>Execute a custom function set in the server configuration. Available to unrestricted connections only</td>
</tr>
<tr>
<td><code>OpPing</code></td>
<td><code>0xF1</code></td>
<td>Health check — the server echoes the payload back as <code>OpPong</code> with no HSM or key lookup involved</td>
</tr>
</tbody>
</table>
<hr />
<h3 id="keyless-request-exec-duration-per-opcode"><code>keyless_request_exec_duration_per_opcode</code></h3>
<p><strong>Type:</strong> Histogram<br />
<strong>Labels:</strong> <code>type</code>, <code>error</code></p>
<p>Measures the time to execute a single operation, from when processing begins to when a response is produced. For operations backed by a PKCS#11 HSM, this includes the full time waiting for a session from the pool plus the HSM cryptographic operation time.</p>
<p>This metric does not include time a request spends waiting for a connection semaphore slot. That is captured by <a href="#keyless_request_total_duration_per_opcode"><code>keyless_request_total_duration_per_opcode</code></a>.</p>
<h4 id="type-label"><code>type</code> label</h4>
<p>Opcodes are grouped into coarser categories for this label:</p>
<table>
<thead>
<tr>
<th><code>type</code> label</th>
<th>Opcodes included</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rsa</code></td>
<td><code>OpRSADecrypt</code>, all <code>OpRSASign*</code>, all <code>OpRSAPSSSign*</code></td>
</tr>
<tr>
<td><code>ecdsa</code></td>
<td>All <code>OpECDSASign*</code></td>
</tr>
<tr>
<td><code>ed25519</code></td>
<td><code>OpEd25519Sign</code></td>
</tr>
<tr>
<td><code>rpc</code></td>
<td><code>OpRPC</code></td>
</tr>
<tr>
<td><code>custom</code></td>
<td><code>OpCustom</code></td>
</tr>
<tr>
<td><code>other</code></td>
<td><code>OpSeal</code>, <code>OpUnseal</code>, <code>OpPing</code>, <code>OpPong</code>, <code>OpResponse</code>, <code>OpError</code></td>
</tr>
<tr>
<td><code>unknown</code></td>
<td>Any unrecognised opcode byte</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14198.md")
</aside>
<h4 id="error-label"><code>error</code> label</h4>
<p>For successful requests the value is <code>no error</code>. All other values indicate a failed operation.</p>
<table>
<thead>
<tr>
<th><code>error</code> label</th>
<th>Description</th>
<th>Common cause</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>no error</code></td>
<td>Operation completed successfully</td>
<td>—</td>
</tr>
<tr>
<td><code>cryptography error</code></td>
<td>HSM or signing operation failed</td>
<td>PKCS#11 session pool exhaustion (<code>resource pool timed out</code>), HSM returned an error, key type mismatch</td>
</tr>
<tr>
<td><code>key not found due to no matching SKI/SNI/ServerIP</code></td>
<td>Key lookup returned no result</td>
<td>Key not loaded in keystore, incorrect SKI in request</td>
</tr>
<tr>
<td><code>read failure</code></td>
<td>I/O read error during the operation</td>
<td>Disk error reading key file</td>
</tr>
<tr>
<td><code>version mismatch</code></td>
<td>Protocol version not supported</td>
<td>Client and server version skew</td>
</tr>
<tr>
<td><code>bad opcode</code></td>
<td>Unknown opcode received</td>
<td><code>OpCustom</code> sent with no custom handler configured</td>
</tr>
<tr>
<td><code>unexpected opcode</code></td>
<td>A response opcode was used as a request</td>
<td>Client sent <code>OpPong</code>, <code>OpResponse</code>, or <code>OpError</code> as a request</td>
</tr>
<tr>
<td><code>malformed message</code></td>
<td>TLV parse failure</td>
<td>Corrupt or truncated packet</td>
</tr>
<tr>
<td><code>internal error</code></td>
<td>Non-cryptographic server-side failure</td>
<td>Sealer is nil, RPC dispatch error</td>
</tr>
<tr>
<td><code>certificate not found</code></td>
<td>Certificate lookup failed</td>
<td>Certificate not loaded</td>
</tr>
<tr>
<td><code>sealing key expired</code></td>
<td><code>OpUnseal</code> blob is too old to decrypt</td>
<td>TLS session ticket key rotation — blob sealed with a key that has since been retired</td>
</tr>
<tr>
<td><code>remote configuration error</code></td>
<td>Remote key server is misconfigured</td>
<td>Key points to an unreachable or misconfigured remote key server</td>
</tr>
</tbody>
</table>
<hr />
<h3 id="keyless-request-total-duration-per-opcode"><code>keyless_request_total_duration_per_opcode</code></h3>
<p><strong>Type:</strong> Histogram<br />
<strong>Labels:</strong> <code>type</code>, <code>error</code> (same values as <a href="#keyless_request_exec_duration_per_opcode"><code>keyless_request_exec_duration_per_opcode</code></a>)</p>
<p>Measures the total time to satisfy a request, from when the request packet is read off the wire to when the response bytes are written back to the client.</p>
<pre><code class="language-txt">total_duration = exec_duration + response_write_time&#10;</code></pre>
<p>Both timestamps are captured after the connection semaphore is already held, so semaphore queue wait time is not included in either histogram. Under normal load, total duration and exec duration are approximately equal. A growing gap between them indicates slow writes back to the client — for example, network backpressure between the key server and the Cloudflare edge.</p>
<hr />
<h3 id="keyless-key-load-duration"><code>keyless_key_load_duration</code></h3>
<p><strong>Type:</strong> Histogram<br />
<strong>Labels:</strong> None</p>
<p>Measures the time taken by the keystore to locate and return the private key for each request, keyed by SKI, SNI, and server IP.</p>
<ul>
<li>For file-backed keystores, this is a map lookup and is typically sub-millisecond.</li>
<li>For PKCS#11 or HSM keystores, this may include a network round-trip to the HSM if key references are not cached in memory.</li>
</ul>
<p>This metric is recorded for all signing and decryption operations: <code>OpRSADecrypt</code>, all <code>OpRSASign*</code>, all <code>OpRSAPSSSign*</code>, all <code>OpECDSASign*</code>, and <code>OpEd25519Sign</code>.</p>
<p>It is <strong>not</strong> recorded for <code>OpPing</code>, <code>OpSeal</code>, <code>OpUnseal</code>, <code>OpRPC</code>, or <code>OpCustom</code>, which do not require a private key lookup.</p>
<hr />
<h3 id="keyless-failed-connection"><code>keyless_failed_connection</code></h3>
<p><strong>Type:</strong> Counter<br />
<strong>Labels:</strong> None</p>
<p>Counts connection-level transport failures. This metric reflects problems at the network or TLS layer — it does not count signing errors or key lookup failures, which are reported in the <code>error</code> label of the duration histograms.</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Counted?</th>
</tr>
</thead>
<tbody>
<tr>
<td>TLS handshake failure</td>
<td>No</td>
</tr>
<tr>
<td>Client disconnected before TLS handshake (EOF)</td>
<td>No</td>
</tr>
<tr>
<td>Failure determining connection trust level after TLS</td>
<td>Yes</td>
</tr>
<tr>
<td>Non-EOF read error on an established connection</td>
<td>Yes</td>
</tr>
<tr>
<td>Write error when delivering a response</td>
<td>Yes</td>
</tr>
<tr>
<td>Read timeout — graceful connection drain</td>
<td>No</td>
</tr>
<tr>
<td>Signing error, including PKCS#11 pool timeout</td>
<td>No</td>
</tr>
<tr>
<td>Key not found</td>
<td>No</td>
</tr>
</tbody>
</table>
<hr />
<h3 id="certificate-expiration-timestamp-seconds"><code>certificate_expiration_timestamp_seconds</code></h3>
<p><strong>Type:</strong> Gauge<br />
<strong>Labels:</strong> <code>source</code>, <code>serial_no</code>, <code>cn</code>, <code>hostnames</code>, <code>ca</code>, <code>server</code>, <code>client</code></p>
<p>Reports the expiration time (<code>NotAfter</code>) of each certificate loaded by the key server as a Unix timestamp. One time series is emitted per certificate.</p>
<p>This metric is updated:</p>
<ul>
<li>At startup, for the server authentication certificate (<code>auth_cert</code>) and the Cloudflare CA certificate (<code>cloudflare_ca_cert</code>).</li>
<li>On each successful inbound TLS connection, for the peer certificates presented by the connecting client.</li>
</ul>
<table>
<thead>
<tr>
<th>Label</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>source</code></td>
<td>File path for startup certs; <code>listener: &lt;addr&gt;</code> for peer certs from incoming connections</td>
</tr>
<tr>
<td><code>serial_no</code></td>
<td>Certificate serial number</td>
</tr>
<tr>
<td><code>cn</code></td>
<td>Subject Common Name</td>
</tr>
<tr>
<td><code>hostnames</code></td>
<td>Sorted, comma-separated list of DNS Subject Alternative Names</td>
</tr>
<tr>
<td><code>ca</code></td>
<td><code>1</code> if the certificate is a CA certificate, <code>0</code> otherwise</td>
</tr>
<tr>
<td><code>server</code></td>
<td><code>1</code> if the certificate includes <code>ExtKeyUsageServerAuth</code>, <code>0</code> otherwise</td>
</tr>
<tr>
<td><code>client</code></td>
<td><code>1</code> if the certificate includes <code>ExtKeyUsageClientAuth</code>, <code>0</code> otherwise</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14197.md")
</aside>
<hr />
<h2 id="example-promql-queries">Example PromQL queries</h2>
<h3 id="signing-throughput-by-key-type">Signing throughput by key type</h3>
<pre><code class="language-txt">sum by (opcode) (rate(keyless_requests[1m]))&#10;</code></pre>
<h3 id="error-rate-by-error-type">Error rate by error type</h3>
<pre><code class="language-txt">sum by (error) (&#10;  rate(keyless_request_exec_duration_per_opcode_count{error!=&quot;no error&quot;}[5m])&#10;)&#10;</code></pre>
<h3 id="99th-percentile-signing-latency-for-rsa">99th percentile signing latency for RSA</h3>
<pre><code class="language-txt">histogram_quantile(&#10;  0.99,&#10;  rate(keyless_request_exec_duration_per_opcode_bucket{type=&quot;rsa&quot;}[5m])&#10;)&#10;</code></pre>
<p>A value approaching 10 seconds indicates PKCS#11 session pool exhaustion. Refer to <a href="/ssl/keyless-ssl/reference/scaling-and-benchmarking/">Scaling and benchmarking</a> and your HSM documentation for guidance on increasing the session pool size.</p>
<h3 id="99th-percentile-key-load-latency">99th percentile key load latency</h3>
<pre><code class="language-txt">histogram_quantile(0.99, rate(keyless_key_load_duration_bucket[5m]))&#10;</code></pre>
<p>A spike here without a corresponding spike in exec duration suggests the keystore lookup itself is slow — a possible disk I/O issue or PKCS#11 object enumeration delay.</p>
<h3 id="connection-failure-rate">Connection failure rate</h3>
<pre><code class="language-txt">rate(keyless_failed_connection_total[5m])&#10;</code></pre>
<p>A sustained non-zero rate indicates network or TLS problems between the Cloudflare network and your key server.</p>
<h3 id="alert-on-certificate-expiry-within-30-days">Alert on certificate expiry within 30 days</h3>
<pre><code class="language-txt">(certificate_expiration_timestamp_seconds - time()) / 86400 &lt; 30&#10;</code></pre>
