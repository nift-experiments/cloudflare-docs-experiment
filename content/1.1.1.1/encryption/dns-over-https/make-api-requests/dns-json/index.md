<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1822.md")
</aside>
<p>Cloudflare's DNS over HTTPS endpoint also supports JSON format for querying DNS data. There is no agreed-upon JSON schema for DNS over HTTPS in the Internet Engineering Task Force (IETF), so Cloudflare has chosen to follow the same schema as Google's DNS over HTTPS resolver.</p>
<p>JSON formatted queries are sent using a <code>GET</code> request. When making requests using <code>GET</code>, the DNS query is encoded into the URL. Include an HTTP <code>Accept</code> request header with a MIME type of <code>application/dns-json</code> to indicate that the client can accept a JSON response.</p>
<h2 id="supported-parameters">Supported parameters</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Required?</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>Yes</td>
<td>Query name.</td>
<td>-</td>
</tr>
<tr>
<td><code>type</code></td>
<td>No</td>
<td>Query type (either a <a href="https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4">numeric value or text</a>).</td>
<td><code>A</code></td>
</tr>
<tr>
<td><code>do</code></td>
<td>No</td>
<td><code>DO</code> bit - whether the client wants DNSSEC data (either empty or one of <code>0</code>, <code>false</code>, <code>1</code>, or <code>true</code>).</td>
<td><code>false</code></td>
</tr>
<tr>
<td><code>cd</code></td>
<td>No</td>
<td><code>CD</code> bit - disable validation (either empty or one of <code>0</code>, <code>false</code>, <code>1</code>, or <code>true</code>).</td>
<td><code>false</code></td>
</tr>
</tbody>
</table>
<h2 id="examples">Examples</h2>
<p>Example request and response:</p>
<pre><code class="language-sh">curl --header &quot;accept: application/dns-json&quot; &quot;https://cloudflare-dns.com/dns-query?name=example.com&amp;type=AAAA&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;Status&quot;: 0,&#10;	&quot;TC&quot;: false,&#10;	&quot;RD&quot;: true,&#10;	&quot;RA&quot;: true,&#10;	&quot;AD&quot;: true,&#10;	&quot;CD&quot;: false,&#10;	&quot;Question&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;example.com.&quot;,&#10;			&quot;type&quot;: 28&#10;		}&#10;	],&#10;	&quot;Answer&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;example.com.&quot;,&#10;			&quot;type&quot;: 28,&#10;			&quot;TTL&quot;: 1726,&#10;			&quot;data&quot;: &quot;2606:2800:220:1:248:1893:25c8:1946&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>In the case of an invalid request a <code>400 Bad Request</code> error is returned:</p>
<pre><code class="language-sh">curl --header &quot;accept: application/dns-json&quot; &quot;https://cloudflare-dns.com/dns-query?name=example.com&amp;cd=2&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;error&quot;: &quot;Invalid CD flag `2`. Expected to be empty or one of `0`, `false`, `1`, or `true`.&quot;&#10;}&#10;</code></pre>
<h2 id="response-fields">Response fields</h2>
<p>The following tables have more information on each response field.</p>
<h3 id="successful-response">Successful response</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Status</code></td>
<td>The Response Code of the DNS Query. The codes are defined here: <a href="https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6">https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6</a>.</td>
</tr>
<tr>
<td><code>TC</code></td>
<td>If the <code>TC</code> field is true, the truncated bit was set. This occurs when the DNS answer exceeds the size of a single UDP or TCP packet. With Cloudflare DNS over HTTPS, the <code>TC</code> field is almost always false because Cloudflare supports the maximum response size.</td>
</tr>
<tr>
<td><code>RD</code></td>
<td>If true, it means the Recursive Desired bit was set. This is always set to true for Cloudflare DNS over HTTPS.</td>
</tr>
<tr>
<td><code>RA</code></td>
<td>If true, it means the Recursion Available bit was set. This is always set to true for Cloudflare DNS over HTTPS.</td>
</tr>
<tr>
<td><code>AD</code></td>
<td>If true, it means that every record in the answer was verified with DNSSEC.</td>
</tr>
<tr>
<td><code>CD</code></td>
<td>If true, the client asked to disable DNSSEC validation. In this case, Cloudflare will still fetch the DNSSEC-related records, but it will not attempt to validate the records.</td>
</tr>
<tr>
<td><code>Question: name</code></td>
<td>The record name requested.</td>
</tr>
<tr>
<td><code>Question: type</code></td>
<td>The type of DNS record requested. These are defined here: <a href="https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4">https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4</a>.</td>
</tr>
<tr>
<td><code>Answer: name</code></td>
<td>The record owner.</td>
</tr>
<tr>
<td><code>Answer: type</code></td>
<td>The type of DNS record. These are defined here: <a href="https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4">https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4</a>.</td>
</tr>
<tr>
<td><code>Answer: TTL</code></td>
<td>The number of seconds the answer can be stored in cache before it is considered stale.</td>
</tr>
<tr>
<td><code>Answer: data</code></td>
<td>The value of the DNS record for the given name and type. The data will be in text for standardized record types and in hex for unknown types.</td>
</tr>
<tr>
<td><code>Authority: name</code></td>
<td>The record owner.</td>
</tr>
<tr>
<td><code>Authority: type</code></td>
<td>The type of DNS record. These are defined here: <a href="https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4">https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4</a>.</td>
</tr>
<tr>
<td><code>Authority: TTL</code></td>
<td>The number of seconds the answer can be stored in cache before it is considered stale.</td>
</tr>
<tr>
<td><code>Authority: data</code></td>
<td>The value of the DNS record for the given name and type. The data will be in text for standardized record types and in hex for unknown types.</td>
</tr>
<tr>
<td><code>Additional: name</code></td>
<td>The record owner.</td>
</tr>
<tr>
<td><code>Additional: type</code></td>
<td>The type of DNS record. These are defined here: <a href="https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4">https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4</a>.</td>
</tr>
<tr>
<td><code>Additional: TTL</code></td>
<td>The number of seconds the answer can be stored in cache before it is considered stale.</td>
</tr>
<tr>
<td><code>Additional: data</code></td>
<td>The value of the DNS record for the given name and type. The data will be in text for standardized record types and in hex for unknown types.</td>
</tr>
<tr>
<td><code>Comment</code></td>
<td>List of EDE messages. Refer to <a href="/1.1.1.1/infrastructure/extended-dns-error-codes/">Extended DNS error codes</a> for more information.</td>
</tr>
</tbody>
</table>
<h3 id="error-response">Error response</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>error</code></td>
<td>An explanation of the error that occurred.</td>
</tr>
</tbody>
</table>
