<p>Variants let you specify how images should be resized for different use cases. By default, images are served with a <code>public</code> variant, but you can create up to 100 variants to fit your needs. Follow these steps to create a variant.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9472.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Delivery</strong> tab.</li>
<li>Select <strong>Create variant</strong>.</li>
<li>Name your variant and select <strong>Create</strong>.</li>
<li>Define variables for your new variant, such as resizing options, type of fit, and specific metadata options.</li>
</ol>
<h2 id="resize-via-the-api">Resize via the API</h2>
<p>Make a <code>POST</code> request to <a href="/api/resources/images/subresources/v1/subresources/variants/methods/create/">create a variant</a>.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/variants&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;id&quot;:&quot;&lt;NAME_OF_THE_VARIANT&gt;&quot;,&quot;options&quot;:{&quot;fit&quot;:&quot;scale-down&quot;,&quot;metadata&quot;:&quot;none&quot;,&quot;width&quot;:1366,&quot;height&quot;:768},&quot;neverRequireSignedURLs&quot;:true}&#10;</code></pre>
<h2 id="fit-options">Fit options</h2>
<p>The <code>Fit</code> property describes how the width and height dimensions should be interpreted. The chart below describes each of the options.</p>
<table>
<thead>
<tr>
<th>Fit Options</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Scale down</td>
<td>The image is shrunk in size to fully fit within the given width or height, but will not be enlarged.</td>
</tr>
<tr>
<td>Contain</td>
<td>The image is resized (shrunk or enlarged) to be as large as possible within the given width or height while preserving the aspect ratio.</td>
</tr>
<tr>
<td>Cover</td>
<td>The image is resized to exactly fill the entire area specified by width and height and will be cropped if necessary.</td>
</tr>
<tr>
<td>Crop</td>
<td>The image is shrunk and cropped to fit within the area specified by the width and height. The image will not be enlarged. For images smaller than the given dimensions, it is the same as <code>scale-down</code>. For images larger than the given dimensions, it is the same as <code>cover</code>.</td>
</tr>
<tr>
<td>Pad</td>
<td>The image is resized (shrunk or enlarged) to be as large as possible within the given width or height while preserving the aspect ratio. The extra area is filled with a background color (white by default).</td>
</tr>
</tbody>
</table>
<h2 id="metadata-options">Metadata options</h2>
<p>Variants allow you to choose what to do with your image’s metadata information. From the <strong>Metadata</strong> dropdown, choose:</p>
<ul>
<li>Strip all metadata</li>
<li>Strip all metadata except copyright</li>
<li>Keep all metadata</li>
</ul>
<h2 id="public-access">Public access</h2>
<p>When the <strong>Always allow public access</strong> option is selected, particular variants will always be publicly accessible, even when images are made private through the use of <a href="/images/optimization/hosted-images/serve-private-images/">signed URLs</a>.</p>
