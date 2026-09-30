<p>Cloudflare offers a DNS over HTTPS resolver at:</p>
<pre><code class="language-txt">https://cloudflare-dns.com/dns-query&#10;</code></pre>
<h2 id="http-method">HTTP method</h2>
<p>Cloudflare's DNS over HTTPS (DoH) endpoint supports <code>POST</code> and <code>GET</code> for DNS wireformat, and <code>GET</code> for JSON format.</p>
<p>When making requests using <code>POST</code>, the DNS query is included as the message body of the HTTP request, and the MIME type (<code>application/dns-message</code>) is sent in the <code>Content-Type</code> request header. Cloudflare will use the message body of the HTTP request as sent by the client, so the message body should not be encoded.</p>
<p>When making requests using <code>GET</code>, the DNS query is encoded into the URL.</p>
<h2 id="valid-mime-types">Valid MIME types</h2>
<p>If you use JSON format, set <code>application/dns-json</code>, and if you use DNS wireformat, use <code>application/dns-message</code>.</p>
<p>Refer to <a href="/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-wireformat/">DNS wireformat</a> and <a href="/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/">JSON</a> for cURL examples.</p>
<h2 id="send-multiple-questions-in-a-query">Send multiple questions in a query</h2>
<p>Each DNS query maps to exactly one HTTP request. To send multiple queries concurrently, use HTTP/2 or HTTP/3, which supports multiplexing multiple requests over a single connection.</p>
<p>HTTP/2 is the minimum recommended version of HTTP for use with DoH. This is not specific to 1.1.1.1, but rather how DoH operates per <a href="https://datatracker.ietf.org/doc/html/rfc8484#section-5.2">RFC 8484</a>.</p>
<p>Example request:</p>
<pre><code class="language-sh">curl --http2 --header &quot;accept: application/dns-json&quot; &quot;https://one.one.one.one/dns-query?name=cloudflare.com&quot; --next --http2 --header &quot;accept: application/dns-json&quot; &quot;https://one.one.one.one/dns-query?name=example.com&quot;&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<p>No authentication is required to send requests to this API.</p>
<h2 id="supported-tls-versions">Supported TLS versions</h2>
<p>Cloudflare's DNS over HTTPS resolver supports TLS 1.2 and TLS 1.3.</p>
<h2 id="return-codes">Return codes</h2>
<table>
<thead>
<tr>
<th>HTTP Status</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>400</code></td>
<td>DNS query not specified or too small.</td>
</tr>
<tr>
<td><code>413</code></td>
<td>DNS query is larger than maximum allowed DNS message size.</td>
</tr>
<tr>
<td><code>415</code></td>
<td>Unsupported content type.</td>
</tr>
<tr>
<td><code>504</code></td>
<td>Resolver timeout while waiting for the query response.</td>
</tr>
</tbody>
</table>
