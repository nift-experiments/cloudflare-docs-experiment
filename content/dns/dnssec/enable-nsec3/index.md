<p>As explained in <a href="https://blog.cloudflare.com/black-lies/">our blog</a>, Cloudflare's implementation of negative answers with NSEC is protected against zone walking<sup><a href="#footnote-1">1</a></sup>. This implementation, also referred to as Compact Denial of Existence (<a href="https://www.rfc-editor.org/rfc/rfc9824.html">RFC 9824</a>), removes the need for NSEC3 and is significantly more efficient.</p>
<p>However, if you must use NSEC3 for compliance reasons, you can enable it as explained below.</p>
<h2 id="enable-nsec3">Enable NSEC3</h2>
<p>Use the <a href="/api/resources/dns/subresources/dnssec/methods/edit/">Edit DNSSEC Status endpoint</a>, setting <code>status</code> to <code>active</code> and <code>dnssec_use_nsec3</code> to <code>true</code>. You should replace the values started by <code>$</code> with your zone ID and authentication credentials. To learn more about using the Cloudflare API, refer to <a href="/fundamentals/api/get-started/">Fundamentals</a>.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;dnssec_use_nsec3&quot;: true,&#10;  &quot;status&quot;: &quot;active&quot;&#10;}&#x27;</code></pre>
<h3 id="pre-signed-dnssec">Pre-signed DNSSEC</h3>
<p>If you use Cloudflare as a secondary DNS provider with <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">pre-signed DNSSEC</a>, setting <code>dnssec_use_nsec3</code> to <code>true</code> means that Cloudflare will use NSEC3 records as transferred in from your primary DNS provider.</p>
<p>Otherwise, NSEC3 records will be generated and signed at request time.</p>
<h2 id="verify-nsec3-is-in-use">Verify NSEC3 is in use</h2>
<p>To validate that NSEC3 is being used, consider the following scenarios:</p>
<h3 id="non-existent-zone-name">Non-existent zone name</h3>
<p>A command like the following would trigger a signed negative response using NSEC3 for proof of non-existence. Look for NSEC3 records under the <code>Authority Section</code> of the response.</p>
<pre><code class="language-sh">dig +dnssec doesnotexist.example.com&#10;</code></pre>
<h3 id="non-existent-record-type-at-an-existing-name">Non-existent record type at an existing name</h3>
<p>If the name <code>www</code> exists but the type TXT does not, the example below would trigger a signed NODATA response using NSEC3. Look for NSEC3 records under the <code>Authority Section</code> of the response.</p>
<pre><code class="language-sh">dig +dnssec www.example.com TXT&#10;</code></pre>
<h2 id="availability">Availability</h2>
<p>NSEC3 is only available for zones on the Enterprise plan.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A method where an attacker exploits NSEC negative answers to obtain all names in a given zone. This is possible when such negative answers provide information on the previous and next names in a chain.</li></ol></section>
