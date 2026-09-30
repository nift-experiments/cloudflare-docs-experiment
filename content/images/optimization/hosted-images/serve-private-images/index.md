<p>You can serve private images by using signed URL tokens. When an image requires a signed URL, the image cannot be accessed without a token unless it is being requested for a variant set to always allow public access.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Keys</strong>.</li>
<li>Copy your key and use it to generate an expiring tokenized URL.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9467.md")
</aside>
<h2 id="generate-signed-urls-from-your-backend">Generate signed URLs from your backend</h2>
<p>Signed URLs are generated server-side to protect your signing key. The example below uses a Cloudflare Worker, but the same signing logic can be implemented in any backend environment (Node.js, Python, PHP, Go, etc.).</p>
<p>The Worker accepts a regular Images URL and returns a signed URL that expires after one day. Adjust the <code>EXPIRATION</code> value to set a different expiry period.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9466.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9468.md")
</div>
