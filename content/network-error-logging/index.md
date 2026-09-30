<p>Network Error Logging (NEL) is a browser-based reporting system that allows users to report their own failures to an external endpoint. You can use Network Error Logging to gain insight into connectivity issues on the Internet to learn when and where an incident is happening, who is impacted, and how they are being impacted.</p>
<h2 id="the-last-mile">The last mile</h2>
<p>The last mile is the path from a user to the first point of ingress to the resource, whether that be a network like Cloudflare or directly to the origin server. The last mile is important because it is in the critical path of the request for a resource: if the last mile has issues, users cannot connect to their resources. When Network Error Logging is enabled, you can receive alerts about issues in the last mile — which are typically difficult to detect — to learn what the problem is and how to fix it.</p>
<p><img src="/assets/upstream/images/network-error-logging/last-mile.png" alt="The last mile diagram, showing the steps involved in delivering data to a customer" /></p>
<h2 id="how-nel-affects-requests">How NEL affects requests</h2>
<p>The Report-To header is present in all requests to Cloudflare zones that have NEL enabled:  </p>
<pre><code class="language-txt">report-to: {&quot;group&quot;:&quot;cf-nel&quot;,&quot;max_age&quot;:31536000,&quot;endpoints&quot;:[{&quot;url&quot;:&quot;`[`https://a.nel.cloudflare.com/report?lkg-colo=lhr&amp;lkg-time=1600338181`](https://gcp.nel.cloudflare.com/report?lkg-colo=lhr&amp;lkg-time=1600338181&amp;lkg-ip=1.1.1.1)`&quot;}]}&#10;</code></pre>
<p>A sample Network Error Report payload appears as follows:</p>
<pre><code class="language-json">{&#10;  &quot;age&quot;: 20,&#10;  &quot;type&quot;: &quot;network-error&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/previous-page&quot;,&#10;  &quot;body&quot;: {&#10;    &quot;elapsed_time&quot;: 18,&#10;    &quot;method&quot;: &quot;POST&quot;,&#10;    &quot;phase&quot;: &quot;dns&quot;,&#10;    &quot;protocol&quot;: &quot;http/1.1&quot;,&#10;    &quot;referrer&quot;: &quot;https://example.com/previous-page&quot;,&#10;    &quot;sampling_fraction&quot;: 1,&#10;    &quot;server_ip&quot;: &quot;&quot;,&#10;    &quot;status_code&quot;: 0,&#10;    &quot;type&quot;: &quot;dns.name_not_resolved&quot;,&#10;    &quot;url&quot;: &quot;https://example-host.com/&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="privacy">Privacy</h2>
<p>Cloudflare uses geolocation lookups to extract the following information from every client IP in a NEL report:</p>
<ul>
<li>Client ASN</li>
<li>Client country</li>
<li>Client metro area</li>
</ul>
<p>Cloudflare uses internal lookups to associate the above data with a customer domain and customer account.</p>
<p>Cloudflare does not store any PII or user-specific data, and any IP data is only kept for the duration of the request as it is processed. After the report is processed through the NEL pipeline, all PII data is purged from the system.</p>
<p>The client IP address is only stored in volatile memory for the lifetime of the request to Cloudflare’s NEL endpoint (order of milliseconds) and is dropped immediately after the request completes. Cloudflare does not log the client IP address anywhere in the Network Error Logging pipeline.</p>
<p>NEL reports contain information about the end user's network conditions, which could be considered sensitive. Cloudflare takes privacy seriously and has implemented the following safeguards:</p>
<ul>
<li>Reports are sent to Cloudflare's infrastructure and are not shared with third parties.</li>
<li>Reports do not contain personally identifiable information (PII).</li>
<li>Customers can opt out of having their end users consume the NEL headers using one of the following methods:
<ol>
<li><strong>Self-service (Zone setting)</strong> — Use the dashboard toggle or API (<code>PATCH /zones/{zone_id}/settings/nel</code>) to disable NEL for your zone. This can be re-enabled by any zone administrator at any time.</li>
<li><strong>Permanent opt-out via Support</strong> — Contact Cloudflare support to have the <code>nel___enable</code> feature flag disabled at the product level. This prevents NEL from being enabled on your zone entirely and cannot be reversed by zone administrators.
For Free and Pro plans, the dashboard toggle is typically sufficient. Enterprise customers with strict privacy requirements may prefer the permanent support-level opt-out.</li>
</ol>
</li>
</ul>
