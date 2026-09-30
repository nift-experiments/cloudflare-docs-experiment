<p>You can delete an image from the Cloudflare Images storage using the dashboard, the API, or from a Worker via the <a href="/images/storage/binding/#imageimageiddelete">Images binding</a>.</p>
<h2 id="delete-images-via-the-cloudflare-dashboard">Delete images via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the image you want to remove and select <strong>Delete</strong>.</li>
<li>(Optional) To delete more than one image, select the checkbox next to the images you want to delete and then <strong>Delete selected</strong>.</li>
</ol>
<p>Your image will be deleted from your account.</p>
<h2 id="delete-images-via-the-api">Delete images via the API</h2>
<p>Make a <code>DELETE</code> request to the <a href="/api/resources/images/subresources/v1/methods/delete/">delete image endpoint</a>. <code>{image_id}</code> must be fully URL encoded in the API call URL.</p>
<pre><code class="language-bash">curl --request DELETE https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/{image_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>After the image has been deleted, the response returns <code>&quot;success&quot;: true</code>.</p>
