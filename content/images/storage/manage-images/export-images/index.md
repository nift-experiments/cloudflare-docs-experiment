<p>Cloudflare Images supports image exports via the Cloudflare dashboard and API which allows you to get the original version of your image.</p>
<h2 id="export-images-via-the-cloudflare-dashboard">Export images via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the image or images you want to export.</li>
<li>To export a single image, select <strong>Export</strong> from its menu. To export several images, select the checkbox next to each image and then select <strong>Export selected</strong>.</li>
</ol>
<p>Your images are downloaded to your machine.</p>
<h2 id="export-images-via-the-api">Export images via the API</h2>
<p>Make a <code>GET</code> request as shown in the example below. <code>&lt;IMAGE_ID&gt;</code> must be fully URL encoded in the API call URL.</p>
<p><code>GET accounts/&lt;ACCOUNT_ID&gt;/images/v1/&lt;IMAGE_ID&gt;/blob</code></p>
