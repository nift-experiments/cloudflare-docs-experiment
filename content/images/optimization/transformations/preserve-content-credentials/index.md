<p><a href="https://contentcredentials.org/">Content Credentials</a> (or C2PA metadata) are a type of metadata that includes the full provenance chain of a digital asset. This provides information about an image's creation, authorship, and editing flow. This data is cryptographically authenticated and can be verified using an <a href="https://contentcredentials.org/verify">open-source verification service</a>.</p>
<p>You can preserve Content Credentials when optimizing images stored in remote sources.</p>
<h2 id="enable">Enable</h2>
<p>You can configure how Content Credentials are handled for each zone where transformations are served.</p>
<p>In the Cloudflare dashboard under <strong>Images</strong> &gt; <strong>Transformations</strong>, navigate to a specific zone and enable the toggle to preserve Content Credentials:</p>
<p><img src="/assets/upstream/images/images/preserve-content-credentials.png" alt="Enable Preserving Content Credentials in the dashboard" /></p>
<p>The behavior of this setting is determined by the <a href="/images/optimization/features/#metadata"><code>metadata</code></a> parameter for each transformation.</p>
<p>For example, if a transformation specifies <code>metadata=copyright</code>, then the EXIF copyright tag and all Content Credentials will be preserved in the resulting image and all other metadata will be discarded.</p>
<p>When Content Credentials are preserved in a transformation, Cloudflare will keep any existing Content Credentials embedded in the source image and automatically append and cryptographically sign additional actions.</p>
<p>When this setting is disabled, any existing Content Credentials will always be discarded.</p>
