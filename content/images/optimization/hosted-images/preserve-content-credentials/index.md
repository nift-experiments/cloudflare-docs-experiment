<p><a href="https://contentcredentials.org/">Content Credentials</a> (or C2PA metadata) are a type of metadata that includes the full provenance chain of a digital asset. This provides information about an image's creation, authorship, and editing flow. This data is cryptographically authenticated and can be verified using an <a href="https://contentcredentials.org/verify">open-source verification service</a>.</p>
<p>You can preserve Content Credentials on images uploaded to and delivered from Cloudflare Images.</p>
<h2 id="enable">Enable</h2>
<p>Content Credentials preservation is an account-wide setting that applies to every image delivered from <code>imagedelivery.net</code> (and any custom domains configured for your Images account).</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Delivery</strong> tab.</p>
</li>
<li>
<p>Enable <strong>Preserve Content Credentials</strong>.</p>
</li>
</ol>
<p>You can also enable it via the API by making a <code>PATCH</code> request to the <a href="/api/resources/images/subresources/v1/subresources/variants/methods/edit/">images config endpoint</a>:</p>
<pre><code class="language-bash">curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;preserve_content_credentials&quot;: true}&#x27;&#10;</code></pre>
<p>The behavior of this setting is determined by the <a href="/images/optimization/features/#metadata"><code>metadata</code></a> parameter applied to each delivered image or variant.</p>
<p>For example, if a variant specifies <code>metadata=copyright</code> (the default), then the EXIF copyright tag and all Content Credentials will be preserved in the resulting image and all other metadata will be discarded.</p>
<p>When Content Credentials are preserved during delivery, Cloudflare will keep any existing Content Credentials embedded in the source image and automatically append and cryptographically sign additional actions describing the transformations it applied (such as resizing or format conversion).</p>
