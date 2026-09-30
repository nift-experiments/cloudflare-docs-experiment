<h2 id="basic-uploads">Basic Uploads</h2>
<p>For files smaller than 200 MB, you can use simple form-based uploads.</p>
<h2 id="upload-through-the-cloudflare-dashboard">Upload through the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Stream</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Drag and drop your video into the <strong>Quick upload</strong> area. You can also click to browse for the file on your machine.</li>
</ol>
<p>After the video finishes uploading, the video appears in the list.</p>
<h2 id="upload-with-the-stream-api">Upload with the Stream API</h2>
<p>Make a <code>POST</code> request with the <code>content-type</code> header set to <code>multipart/form-data</code> and include the media as an input with the name set to <code>file</code>.</p>
<pre><code class="language-bash">curl --request POST \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-form file=@/Users/user_name/Desktop/my-video.mp4 \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14369.md")
</aside>
