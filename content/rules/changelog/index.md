<h2 id="2026-08-13">2026-08-13</h2>

<strong>Oracle Cloud Infrastructure Object Storage support in Cloud Connector</strong>

<p>Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.</p>
<p>OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional <code>oraclecloud.com</code> and dedicated <code>customer-oci.com</code> path-style endpoints.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-08-13-oci-object-storage-cloud-connector-public-buckets-only">Public buckets only</h4>
@markup("md", "content/.markup/bodies/17751.md")</aside>
<h4 id="2026-08-13-oci-object-storage-cloud-connector-api-example">API example</h4>
<p>Set <code>provider</code> to <code>oci_storage</code> and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:</p>
<pre><code class="language-json">{&#10;	&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/assets/*\&quot;&quot;,&#10;	&quot;provider&quot;: &quot;oci_storage&quot;,&#10;	&quot;description&quot;: &quot;Route assets to OCI Object Storage&quot;,&#10;	&quot;enabled&quot;: true,&#10;	&quot;parameters&quot;: {&#10;		&quot;host&quot;: &quot;&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For endpoint formats and bucket requirements, refer to <a href="/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage">Supported cloud providers in Cloud Connector</a>.</p>


<h2 id="2026-07-16">2026-07-16</h2>

<strong>Bot management fields and ASN support in Cache Rules</strong>

<h4 id="2026-07-16-cache-rules-bot-fields-asn-bot-management-fields-and-asn-support-in-cache-rules">Bot management fields and ASN support in Cache Rules</h4>
<p>Cache Rules now supports bot management fields and the <code>ip.src.asnum</code> field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).</p>
<p>This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.</p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-new-fields">New fields</h4>
<p>The following fields are now available in Cache Rules expressions:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.bot_management.score</code></td>
<td>Number</td>
<td>Bot score from <code>1</code> to <code>99</code>, where a lower value indicates a higher likelihood that the request originates from a bot.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja3_hash</code></td>
<td>String</td>
<td>JA3 fingerprint of the request, which helps identify the client making the connection.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja4</code></td>
<td>String</td>
<td>JA4 fingerprint of the request, which provides a more detailed client identification than JA3.</td>
</tr>
<tr>
<td><code>cf.bot_management.verified_bot</code></td>
<td>Boolean</td>
<td>Whether the request originates from a verified bot, such as a search engine crawler.</td>
</tr>
<tr>
<td><code>cf.bot_management.static_resource</code></td>
<td>Boolean</td>
<td>Whether the request is for a static resource and therefore exempt from bot detection.</td>
</tr>
<tr>
<td><code>cf.bot_management.js_detection.passed</code></td>
<td>Boolean</td>
<td>Whether the browser passed JavaScript detection when the feature is enabled.</td>
</tr>
<tr>
<td><code>cf.bot_management.detection_ids</code></td>
<td>Array&lt;Number&gt;</td>
<td>List of IDs that correspond to Bot Management heuristic detections made on the request.</td>
</tr>
<tr>
<td><code>cf.bot_management.tags</code></td>
<td>Array&lt;String&gt;</td>
<td>List of tags associated with the bot traffic, such as <code>API</code>, <code>GOOGLE</code>, or <code>BING</code>. Match a tag with an expression such as <code>any(cf.bot_management.tags[*] eq &quot;API&quot;)</code>.</td>
</tr>
<tr>
<td><code>cf.bot_management.signed_agent</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known agent that identifies itself with Web Bot Auth.</td>
</tr>
<tr>
<td><code>cf.bot_management.corporate_proxy</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known corporate proxy.</td>
</tr>
<tr>
<td><code>ip.src.asnum</code></td>
<td>Number</td>
<td>The autonomous system number (ASN) of the incoming request's IP address.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17750.md")</aside>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-example">Example</h4>
<p>Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:</p>
<pre><code class="language-txt">(http.request.uri.path contains &quot;/api/&quot; and cf.bot_management.score lt 30)&#10;or&#10;(http.request.uri.path contains &quot;/api/&quot; and not ip.src.asnum in {12345 67890})&#10;</code></pre>
<p>To learn more, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a> and the <a href="/ruleset-engine/rules-language/fields/">Fields reference</a>.</p>


<h2 id="2026-04-01">2026-04-01</h2>

<strong>New QUIC RTT and delivery rate fields</strong>

<p>Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing <a href="/ruleset-engine/rules-language/fields/reference/"><code>cf.timings.client_tcp_rtt_msec</code></a> field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.</p>
<p>Previously, QUIC RTT and delivery rate data was only available via the <code>Server-Timing: cfL4</code> response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.</p>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.client_quic_rtt_msec</code></td>
<td>Integer</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns <code>0</code> for TCP connections.</td>
</tr>
<tr>
<td><code>cf.edge.l4.delivery_rate</code></td>
<td>Integer</td>
<td>The most recent data delivery rate estimate for the client connection, in bytes per second. Returns <code>0</code> when L4 statistics are not available for the request.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-route-slow-connections-to-a-lightweight-origin">Example: Route slow connections to a lightweight origin</h4>
<p>Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:</p>
<p><strong>Rule expression:</strong></p>
<pre><code class="language-txt">cf.timings.client_tcp_rtt_msec &gt; 200 or cf.timings.client_quic_rtt_msec &gt; 200&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>X-High-Latency</code></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-match-low-bandwidth-connections">Example: Match low-bandwidth connections</h4>
<pre><code class="language-txt">cf.edge.l4.delivery_rate &gt; 0 and cf.edge.l4.delivery_rate &lt; 100000&#10;</code></pre>
<p>For more information, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a> and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="2026-03-25">2026-03-25</h2>

<strong>New mTLS certificate fields for Transform Rules</strong>

<p>Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized <code>Client-Cert</code> and <code>Client-Cert-Chain</code> header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.</p>
<p>Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, <code>:MIIDsT...Vw==:</code>. A chain of intermediates is expressed as a comma-separated list of such values.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be <code>false</code>.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted.</td>
</tr>
</tbody>
</table>
<p>The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin-server">Example: Forwarding client certificate headers to your origin server</h4>
<p>Add a request header transform rule to set the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:</p>
<p><strong>Rule expression:</strong></p>
<pre><code class="language-txt">cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>Client-Cert</code></td>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
</tr>
<tr>
<td>Set</td>
<td><code>Client-Cert-Chain</code></td>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
</tr>
</tbody>
</table>
<p>To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates <code>cf.tls_client_auth.cert_verified</code> and <code>cf.tls_client_auth.cert_revoked</code>.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-03-25-rfc9440-mtls-fields-prevent-header-injection">Prevent header injection</h4>
@markup("md", "content/.markup/bodies/17749.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>, <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>, and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="2026-03-18">2026-03-18</h2>

<strong>Worker execution timing field now available in Rules</strong>

<p>The <code>cf.timings.worker_msec</code> field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.</p>
<p>You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.</p>
<h4 id="2026-03-18-worker-timing-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.worker_msec</code></td>
<td>Integer</td>
<td>The time spent executing a Cloudflare Worker in milliseconds. Returns <code>0</code> if no Worker was invoked.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>cf.timings.worker_msec &gt; 500&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/">Fields reference</a>.</p>


<h2 id="2026-01-27">2026-01-27</h2>

<strong>Control request and response body buffering in Configuration Rules</strong>

<p>You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>
<h4 id="2026-01-27-body-buffering-settings-request-body-buffering">Request body buffering</h4>
<p>Controls how Cloudflare buffers HTTP request bodies before forwarding them to your origin server:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the request body for enabled functionality such as WAF and Bot Management.</td>
</tr>
<tr>
<td><strong>Full</strong></td>
<td>Buffers the entire request body before sending to origin.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the request body streams directly to origin without inspection.</td>
</tr>
</tbody>
</table>
<h4 id="2026-01-27-body-buffering-settings-response-body-buffering">Response body buffering</h4>
<p>Controls how Cloudflare buffers HTTP response bodies before forwarding them to the client:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the response body for enabled functionality.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the response body streams directly to the client without inspection.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17748.md")</aside>
<h4 id="2026-01-27-body-buffering-settings-api-example">API example</h4>
<pre><code class="language-json">{&#10;  &quot;action&quot;: &quot;set_config&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;request_body_buffering&quot;: &quot;standard&quot;,&#10;    &quot;response_body_buffering&quot;: &quot;none&quot;&#10;  }&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>


<h2 id="2026-01-22">2026-01-22</h2>

<strong>New cryptographic functions — encode_base64() and sha256()</strong>

<p>Cloudflare Rulesets now includes <code>encode_base64()</code> and <code>sha256()</code> functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.</p>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>encode_base64(input, flags)</code></td>
<td>Encodes a string to Base64 format. Optional <code>flags</code> parameter: <code>u</code> for URL-safe encoding, <code>p</code> for padding (adds <code>=</code> characters to make the output length a multiple of 4, as required by some systems). By default, output is standard Base64 without padding.</td>
<td>All plans (in header transform rules)</td>
</tr>
<tr>
<td><code>sha256(input)</code></td>
<td>Computes a SHA256 hash of the input string.</td>
<td>Requires enablement</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17747.md")</aside>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-examples">Examples</h4>
<p><strong>Encode a string to Base64 format:</strong></p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Encode a string to Base64 format with padding:</strong></p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;p&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ=</code></p>
<p><strong>Perform a URL-safe Base64 encoding of a string:</strong></p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;u&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Compute the SHA256 hash of a secret token:</strong></p>
<pre><code class="language-txt">sha256(&quot;my-token&quot;)&#10;</code></pre>
<p>Returns a hash that your origin can validate to authenticate requests.</p>
<p><strong>Compute the SHA256 hash of a string and encode the result to Base64 format:</strong></p>
<pre><code class="language-txt">encode_base64(sha256(&quot;my-token&quot;))&#10;</code></pre>
<p>Combines hashing and encoding for systems that expect Base64-encoded signatures.</p>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="2026-01-20">2026-01-20</h2>

<strong>New functions for array and map operations</strong>

<h4 id="2026-01-20-array-map-functions-new-functions-for-array-and-map-operations">New functions for array and map operations</h4>
<p>Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.</p>
<hr />
<h4 id="2026-01-20-array-map-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>split(source, delimiter)</code></td>
<td>Splits a string into an array of strings using the specified delimiter.</td>
</tr>
<tr>
<td><code>join(array, delimiter)</code></td>
<td>Joins an array of strings into a single string using the specified delimiter.</td>
</tr>
<tr>
<td><code>has_key(map, key)</code></td>
<td>Returns <code>true</code> if the specified key exists in the map.</td>
</tr>
<tr>
<td><code>has_value(map, value)</code></td>
<td>Returns <code>true</code> if the specified value exists in the map.</td>
</tr>
</tbody>
</table>
<hr />
<h4 id="2026-01-20-array-map-functions-example-use-cases">Example use cases</h4>
<p><strong>Check if a country code exists in a header list:</strong></p>
<pre><code class="language-txt">has_value(split(http.response.headers[&quot;x-allow-country&quot;][0], &quot;,&quot;), ip.src.country)&#10;</code></pre>
<p><strong>Check if a specific header key exists:</strong></p>
<pre><code class="language-txt">has_key(http.request.headers, &quot;x-custom-header&quot;)&#10;</code></pre>
<p><strong>Join array values for logging or comparison:</strong></p>
<pre><code class="language-txt">join(http.request.headers.names, &quot;, &quot;)&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="2026-01-12">2026-01-12</h2>

<strong>Metro code field now available in Rules</strong>

<p>The <code>ip.src.metro_code</code> field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.</p>
<p>You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.</p>
<h4 id="2026-01-12-dma-metro-code-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ip.src.metro_code</code></td>
<td>String | null</td>
<td>The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>ip.src.metro_code eq &quot;501&quot;&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/">Fields reference</a>.</p>


<h2 id="2025-10-30">2025-10-30</h2>

<strong>New TCP-based fields available in Rulesets</strong>

<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-build-rules-based-on-tcp-transport-and-latency">Build rules based on TCP transport and latency</h4>
<p>Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.</p>
<hr />
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.edge.client_tcp</code></td>
<td>Boolean</td>
<td>Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.</td>
</tr>
<tr>
<td><code>cf.timings.client_tcp_rtt_msec</code></td>
<td>Number</td>
<td>Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>cf.edge.client_tcp &amp;&amp; cf.timings.client_tcp_rtt_msec &lt; 100&#10;</code></pre>
<p>More information can be found in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="2025-06-09">2025-06-09</h2>

<strong>More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</strong>

<p><a href="/rules/custom-errors/">Custom Errors</a> can now fetch and store <a href="/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard">assets</a> and <a href="/rules/custom-errors/#error-pages">error pages</a> from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.</li>
<li>These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.</li>
</ul>
<p>This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.</p>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors</a> documentation.</p>


<h2 id="2025-06-09-1">2025-06-09</h2>

<strong>Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules</strong>

<p>You can now use the <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field in <a href="/rules/transform/">Transform Rules</a> to control rule execution based on whether a request originates from <a href="/workers/">Workers</a>, including subrequests issued by Workers in other zones.</p>
<p><img src="/assets/upstream/images/changelog/rules/transform-rule-subrequest-matching.png" alt="Match Workers subrequests by upstream zone in Transform Rules" /></p>
<p><strong>What's new:</strong></p>
<ul>
<li><code>cf.worker.upstream_zone</code> is now supported in Transform Rules expressions.</li>
<li>Skip or apply logic conditionally when handling <a href="/workers/platform/limits/#subrequests">Workers subrequests</a>.</li>
</ul>
<p>For example, to add a header when the subrequest comes from another zone:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-06-09-transform-rule-subrequest-matching-example">Example</h3>
@markup("md", "content/.markup/bodies/17746.md")</div>
<p>This gives you more granular control in how you handle incoming requests for your zone.</p>
<p>Learn more in the <a href="/rules/transform/">Transform Rules</a> documentation and <a href="/ruleset-engine/rules-language/fields/reference/">Rules language fields</a> reference.</p>


<h2 id="2025-05-30">2025-05-30</h2>

<strong>Fine-tune image optimization — WebP now supported in Configuration Rules</strong>

<p>You can now enable <a href="/images/polish/activate-polish/">Polish</a> with the <code>webp</code> format directly in <a href="/rules/configuration-rules/">Configuration Rules</a>, allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/images/polish/compression/#webp">WebP</a> is now a supported <a href="/rules/configuration-rules/settings/#polish">value</a> in the <strong>Polish</strong> setting for Configuration Rules.</li>
</ul>
<p>This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.</p>
<p>Learn more in the <a href="/images/polish/">Polish</a> and <a href="/rules/configuration-rules/">Configuration Rules</a> documentation.</p>


<h2 id="2025-05-09">2025-05-09</h2>

<strong>More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</strong>

<p>You can now use IP, Autonomous System (AS), and Hostname <a href="/waf/tools/lists/custom-lists/">custom lists</a> to route traffic to <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a>, giving you greater precision and control over how you match and process requests at the edge.</p>
<p>In Snippets, you can now also match on <a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a>, unlocking smarter edge logic for everything from request filtering and mitigation to <a href="/rules/snippets/examples/slow-suspicious-requests/">tarpitting</a> and logging.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a> matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or <a href="/api/resources/rules/subresources/lists/methods/list/">Lists API</a>. Great for shared logic across zones.</li>
<li><a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a> – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-lists-scores.png" alt="New fields in Snippets" /></p>
<p>These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.</p>
<p>Learn more in the <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="2025-04-24">2025-04-24</h2>

<strong>Custom Errors are now Generally Available</strong>

<p><a href="/rules/custom-errors/">Custom Errors</a> are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.</p>
<p>You can now manage <strong>Custom Error Rules</strong>, <strong>Custom Error Assets</strong>, and redesigned <strong>Error Pages</strong> directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.</p>
<p>What's new:</p>
<ul>
<li><strong>Custom Errors are now GA</strong> – Available on all paid plans and ready for production traffic.</li>
<li><strong>UI for Custom Error Rules and Assets</strong> – Manage your zone-level rules from the Rules &gt; Overview and your zone-level assets from the Rules &gt; Settings tabs.</li>
<li><strong>Define inline content or upload assets</strong> – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.</li>
<li><strong>Refreshed UI and new name for Error Pages</strong> – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.</li>
<li><strong>Powered by Ruleset Engine</strong> – Custom Error Rules support <a href="/ruleset-engine/rules-language/">conditional logic</a> and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or <a href="/ruleset-engine/reference/phases-list/">other Cloudflare products</a>. You can also configure <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> to add, change, or remove HTTP headers from responses returned by Custom Error Rules.</li>
</ul>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors documentation</a>.</p>


<h2 id="2025-04-09">2025-04-09</h2>

<strong>Cloudflare Snippets are now Generally Available</strong>

<p><img src="/assets/upstream/images/changelog/rules/snippets-ga.png" alt="Cloudflare Snippets are now GA" /></p>
<p><a href="/rules/snippets/">Cloudflare Snippets</a> are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.</p>
<p>You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.</p>
<p>What's new:</p>
<ul>
<li><strong>Snippets are now GA</strong> – Available at no extra cost on all Pro, Business, and Enterprise plans.</li>
<li><strong>Ready for production</strong> – Snippets deliver a production-grade experience built for scale.</li>
<li><strong>Part of the Cloudflare Rules platform</strong> – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.</li>
<li><strong>Trace integration</strong> – Use <a href="/rules/trace-request/">Cloudflare Trace</a> to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga-trace.gif" alt="Snippets shown in Cloudflare Trace results" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/snippets/">launch blog post</a>.</p>


<h2 id="2025-02-12">2025-02-12</h2>

<strong>Increased Cloudflare Rules limits</strong>

<p>We have upgraded and streamlined <a href="/rules/">Cloudflare Rules</a> limits across all plans, simplifying rule management and improving scalability for everyone.</p>
<p><strong>New limits by product:</strong></p>
<ul>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>
<ul>
<li>Free: <strong>20</strong> → <strong>10,000</strong> URL redirects across lists</li>
<li>Pro: <strong>500</strong> → <strong>25,000</strong> URL redirects across lists</li>
<li>Business: <strong>500</strong> → <strong>50,000</strong> URL redirects across lists</li>
<li>Enterprise: <strong>10,000</strong> → <strong>1,000,000</strong> URL redirects across lists</li>
</ul>
</li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a>
<ul>
<li>Free: <strong>5</strong> → <strong>10</strong> connectors</li>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> connectors</li>
</ul>
</li>
<li><a href="/rules/custom-errors/">Custom Errors</a>
<ul>
<li>Pro: <strong>5</strong> → <strong>25</strong> error assets and rules</li>
<li>Business: <strong>20</strong> → <strong>50</strong> error assets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> error assets and rules</li>
</ul>
</li>
<li><a href="/rules/snippets/">Snippets</a>
<ul>
<li>Pro: <strong>10</strong> → <strong>25</strong> code snippets and rules</li>
<li>Business: <strong>25</strong> → <strong>50</strong> code snippets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> code snippets and rules</li>
</ul>
</li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a>, <a href="/rules/configuration-rules/">Configuration Rules</a>, <a href="/rules/compression-rules/">Compression Rules</a>, <a href="/rules/origin-rules/">Origin Rules</a>, <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, and <a href="/rules/transform/">Transform Rules</a>
<ul>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> rules</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-rules-upgraded-limits-gradual-rollout">Gradual rollout</h4>
@markup("md", "content/.markup/bodies/17745.md")</aside>


<h2 id="2025-02-11">2025-02-11</h2>

<strong>Custom Errors (beta): Stored Assets &amp; Account-level Rules</strong>

<p>We're introducing <a href="/rules/custom-errors/">Custom Errors</a> (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.</p>
<p>This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.</p>
<p>This brings the following new capabilities:</p>
<ul>
<li><strong>Custom error assets</strong> – Fetch and store external error pages at the edge for use in error responses.</li>
<li><strong>Account-Level custom errors</strong> – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.</li>
</ul>
<p>You can use Cloudflare API to upload your existing assets for use with Custom Errors:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;maintenance&quot;,&#10;  &quot;description&quot;: &quot;Maintenance template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<p>You can then reference the stored asset in a Custom Error rule:</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;		{&#10;			&quot;action&quot;: &quot;serve_error&quot;,&#10;			&quot;action_parameters&quot;: {&#10;				&quot;asset_name&quot;: &quot;maintenance&quot;,&#10;				&quot;content_type&quot;: &quot;text/html&quot;,&#10;				&quot;status_code&quot;: 503&#10;			},&#10;			&quot;enabled&quot;: true,&#10;			&quot;expression&quot;: &quot;http.request.uri.path contains \&quot;error\&quot;&quot;&#10;		}&#10;	]&#10;}&#x27;&#10;</code></pre>


<h2 id="2025-01-29">2025-01-29</h2>

<strong>New Snippets Code Editor</strong>

<p>The new <a href="/rules/snippets/">Snippets</a> code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.</p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-new-editor.png" alt="New Snippets code editor" /></p>
<p>What’s new:</p>
<ul>
<li><strong>Single-page editing for code and rule</strong> – No need to jump between screens.</li>
<li><strong>Auto-complete &amp; syntax highlighting</strong> – Get suggestions and avoid mistakes.</li>
<li><strong>Code formatting &amp; refactoring</strong> – Write cleaner, more readable code.</li>
</ul>
<p>Try it now in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets">Rules &gt; Snippets</a>.</p>


<h2 id="2025-01-09">2025-01-09</h2>

<strong>New Rules Overview Interface</strong>

<p><strong>Rules Overview</strong> gives you a single page to manage all your <a href="/rules/">Cloudflare Rules</a>.</p>
<p>What you can do:</p>
<ul>
<li><strong>See all your rules in one place</strong> – No more clicking around.</li>
<li><strong>Find rules faster</strong> – Search by name.</li>
<li><strong>Understand execution order</strong> – See how rules run in sequence.</li>
<li><strong>Debug easily</strong> – Use <a href="/rules/trace-request/">Trace</a> without switching tabs.</li>
</ul>
<p>Check it out in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview">Rules &gt; Overview</a>.</p>


<h2 id="2024-12-11">2024-12-11</h2>

<strong>Terraform Support for Snippets</strong>

<p>Now, you can manage <a href="/rules/snippets/">Cloudflare Snippets</a> with <a href="/terraform/">Terraform</a>. Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.</p>
<p>Example Terraform configuration:</p>
<pre><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>Learn more in the <a href="/rules/snippets/create-terraform/">Configure Snippets using Terraform</a> documentation.</p>


<h2 id="2024-11-22">2024-11-22</h2>

<strong>Cloud Connector Now Supports R2</strong>

<p>Now, you can use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to your <a href="/r2/">R2 buckets</a> based on URLs, headers, geolocation, and more.</p>
<p>Example setup:</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<p>Get started using <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="2024-10-23">2024-10-23</h2>

<strong>Simplified UI for URL Rewrites</strong>

<p>It’s now easy to create <strong>wildcard-based <a href="/rules/transform/url-rewrite/">URL Rewrites</a></strong>. No need for complex functions—just define your patterns and go.</p>
<p><img src="/assets/upstream/images/rules/transform/create-url-rewrite-rule.png" alt="Rules Overview Interface" /></p>
<p>What’s improved:</p>
<ul>
<li><strong>Full wildcard support</strong> – Create rewrite patterns using intuitive interface.</li>
<li><strong>Simplified rule creation</strong> – No need for complex functions.</li>
</ul>
<p>Try it via <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">creating a Rewrite URL rule in the dashboard</a>.</p>


<h2 id="2024-09-20">2024-09-20</h2>
<p><strong>Automatic DNS Validation for Cloudflare Rules</strong></p>
<p>The Cloudflare dashboard now automatically validates <a href="https://developers.cloudflare.com/dns/proxy-status/">DNS records</a> and <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">Cloudflare for SaaS custom hostnames</a> for rules targeting specific hostnames or URLs. To prevent misconfigured rules and ensure smoother deployments, you will get proactive warnings for missing or misconfigured DNS records and custom hostnames.</p>
<h2 id="2024-09-17">2024-09-17</h2>
<p><strong>Compression Rules available to all plans with Zstandard support</strong></p>
<p><a href="https://developers.cloudflare.com/rules/compression-rules/">Compression Rules</a> now support Zstandard compression and are available in all Cloudflare plans. Users in the Free plan will gradually get access throughout 2024.</p>
<h2 id="2024-09-13">2024-09-13</h2>
<p><strong>Snippets now available in beta</strong></p>
<p><a href="https://developers.cloudflare.com/rules/snippets/">Cloudflare Snippets</a> have transitioned from alpha to beta.</p>
<h2 id="2024-09-10">2024-09-10</h2>
<p><strong>wildcard_replace() function now supported in URL rewrites</strong></p>
<p>You can now use the <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#wildcard_replace"><code>wildcard_replace()</code></a> function in rewrite expressions of <a href="https://developers.cloudflare.com/rules/transform/url-rewrite/">URL rewrites</a>.</p>
<h2 id="2024-09-05">2024-09-05</h2>
<p><strong>New Rules Templates for one-click rule creation</strong></p>
<p>The new <strong>Rules</strong> &gt; <strong>Templates</strong> page in the Cloudflare dashboard allows you to create common rules with a single click, featuring dozens of pre-built templates. You can also access these templates directly from each product's rule builder. Also, explore the <a href="https://developers.cloudflare.com/rules/examples/">Examples gallery</a> in the developer docs for real-world use cases and inspiration.</p>
<h2 id="2024-08-22">2024-08-22</h2>
<p><strong>Simplified UI for Single Redirects with wildcard support</strong></p>
<p>The simplified UI for <a href="https://developers.cloudflare.com/rules/url-forwarding/single-redirects/">Single Redirects</a> is now available to all users, making URL redirects easier and more intuitive. This update builds on the recent <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard support</a> in Ruleset Engine products. Access the new UI under <strong>Rules &gt; Redirect Rules</strong>. Learn more about wildcard support and our open-source Rust crate in the <a href="https://blog.cloudflare.com/wildcard-rules">blog post</a>.</p>
<h2 id="2024-08-20">2024-08-20</h2>
<p><strong>Cloud Connector now available to all customers</strong></p>
<p>Cloud Connector (beta) is now available to all customers. For setup details, refer to the <a href="https://developers.cloudflare.com/rules/cloud-connector/">documentation</a>, explore <a href="https://developers.cloudflare.com/rules/cloud-connector/examples/">examples</a>, and check out the <a href="https://blog.cloudflare.com/cloud-connector">blog post</a>.</p>
<h2 id="2024-08-16">2024-08-16</h2>
<p><strong>Cloud Connector now available to all free customers</strong></p>
<p>Cloud Connector (beta) is now available to all free and a subset of paid customers. This rollout will be <a href="https://developers.cloudflare.com/rules/cloud-connector/#availability">gradually extended</a> to all Cloudflare users, simplifying multi-cloud management and enhancing integration with Cloudflare's Connectivity Cloud. For more information, refer to the <a href="https://blog.cloudflare.com/cloud-connector">blog post</a>.</p>
<h2 id="2024-08-12">2024-08-12</h2>
<p><strong>Cloudflare Snippets limits have been upgraded</strong></p>
<p>Cloudflare Snippets (alpha) now allow multiple subrequests depending on your plan. For more information, refer to the <a href="https://developers.cloudflare.com/rules/snippets/#availability">Availability</a>.</p>
<h2 id="2024-07-31">2024-07-31</h2>
<p><strong>Wildcard support added to Ruleset Engine products</strong></p>
<p>Wildcards are now supported across our Ruleset Engine-based products, including Single Redirects, Cache Rules, Transform Rules, WAF, Waiting Room, and more:</p>
<ul>
<li>You can now use the <code>wildcard</code> and <code>strict wildcard</code> operators with any string field in the Ruleset Engine, such as full URI, host, headers, cookies, user-agent, and country. For more details, refer to <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/operators/">Operators</a> and <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#wildcard-matching">Wildcard matching</a>.</li>
<li>In <a href="https://developers.cloudflare.com/rules/url-forwarding/single-redirects/">Single Redirects</a>, the <code>wildcard_replace()</code> function allows you to use segments matched by the <code>wildcard</code> and <code>strict wildcard</code> operators in redirect URL targets. For more information, refer to <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#wildcard_replace">Functions</a>.</li>
</ul>
<h2 id="2024-07-01">2024-07-01</h2>
<p><strong>Cloudflare Snippets now available to all paid customers</strong></p>
<p>Cloudflare Snippets (alpha) are now available to all paid customers.</p>
<h2 id="2024-06-03">2024-06-03</h2>
<p><strong>Cloudflare Snippets now available to all Enterprise customers</strong></p>
<p>Cloudflare Snippets (alpha) are now available to all Enterprise customers. Customers in other paid plans will gradually get access throughout 2024.</p>
<h2 id="2024-05-14">2024-05-14</h2>
<p><strong>Page Rules migration</strong></p>
<p>The <a href="https://developers.cloudflare.com/rules/reference/page-rules-migration/">Page Rules migration guide</a> is now available for users interested in transitioning to modern Rules features instead of Page Rules. Explore the guide for detailed instructions on migrating your configurations.</p>
<h2 id="2024-05-13">2024-05-13</h2>
<p><strong>New Configuration Rules setting for Web Analytics (RUM)</strong></p>
<p>You can now turn off Cloudflare Web Analytics, also known as Real User Monitoring (RUM), for specific requests using a configuration rule.</p>
<h2 id="2024-04-29">2024-04-29</h2>
<p><strong>New Configuration Rules setting for Cloudflare Fonts</strong></p>
<p>You can now turn on or off Cloudflare Fonts for specific requests using a configuration rule.</p>
<h2 id="2024-03-22">2024-03-22</h2>
<p><strong>New TLS fields in rule expressions</strong></p>
<p>Customers can now use new fields <code>cf.tls_client_hello_length</code> (the length of the client hello message sent in a TLS handshake), <code>cf.tls_client_random</code> (the value of the 32-byte random value provided by the client in a TLS handshake), and <code>cf.tls_client_extensions_sha1</code> (the SHA-1 fingerprint of TLS client extensions) in various products built on Ruleset Engine.</p>
<h2 id="2024-03-20">2024-03-20</h2>
<p><strong>Origin Rules now allow port numbers in Host Header Override</strong></p>
<p>Customers can now use arbitrary port numbers in Host Header Override in Origin Rules. Previously, only hostname was allowed as a value (for example, <code>example.com</code>). Now, you can set the value to <code>hostname:port</code> (for example, <code>example.com:1234</code>) as well.</p>


