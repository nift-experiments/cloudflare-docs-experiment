<h2 id="get-an-epoch">Get an epoch</h2>
<pre><code class="language-sh">curl &#x27;https://plexi.key-transparency.cloudflare.com/namespaces/{namespace}/audits/1&#x27;&#10;{&#10;  &quot;namespace&quot;: &quot;your.new.log.com&quot;,&#10;  &quot;timestamp&quot;: 1717084639921,&#10;  &quot;epoch&quot;: 1,&#10;  &quot;digest&quot;: &quot;1111111111111111111111111111111111111111111111111111111111111111&quot;,&#10;  &quot;signature&quot;: &quot;f6a51443bb6703813b330959d9d97471bc06464142165e59733fa102a18b052782a5307d59c31b8b13c1af7dfff6f6e7bf44e880d44e26e96c50a72f72a30c07&quot;&#10;}&#10;</code></pre>
<h2 id="publish-a-new-epoch">Publish a new epoch</h2>
<p>Refer to the example below to publish a new epoch by requesting its signature.</p>
<p>This API is authenticated via <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">mTLS</a>, so that only a Log owner can publish new epochs.</p>
<pre><code class="language-sh">curl &#x27;https://plexi.key-transparency.cloudflare.com/namespaces/{namespace}/audits&#x27; \&#10;      &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;      &#45;-data &#x27;{&quot;epoch&quot;: 1, &quot;digest&quot;: &quot;1111111111111111111111111111111111111111111111111111111111111111&quot;}&#x27;&#10;{&#10;  &quot;namespace&quot;: &quot;your.new.log.com&quot;,&#10;  &quot;timestamp&quot;: 1717084639921,&#10;  &quot;epoch&quot;: 1,&#10;  &quot;digest&quot;: &quot;1111111111111111111111111111111111111111111111111111111111111111&quot;,&#10;  &quot;signature&quot;: &quot;f6a51443bb6703813b330959d9d97471bc06464142165e59733fa102a18b052782a5307d59c31b8b13c1af7dfff6f6e7bf44e880d44e26e96c50a72f72a30c07&quot;,&#10;  &quot;key_id&quot;: 74,&#10;}&#10;</code></pre>
<h3 id="constraints">Constraints</h3>
<ul>
<li>If <code>root</code> is defined for the namespace, the first epoch must match it (number and digest).</li>
<li>Epochs must be increasing. Second epoch is 2, third is 3, etc.</li>
<li>Epochs must have a unique digest or it will be rejected.</li>
<li>Epochs cannot be republished.</li>
<li>Digest must be a 32 byte string hex encoded (length 64).</li>
</ul>
<p>If a namespace is disabled, you receive the following error:</p>
<pre><code class="language-txt">HTTP 400 Bad Request&#10;Namespace is disabled and read-only.&#10;</code></pre>
