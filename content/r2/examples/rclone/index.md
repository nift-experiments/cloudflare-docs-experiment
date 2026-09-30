<p>You must <a href="/r2/api/tokens/">generate an Access Key</a> before getting started. All examples will utilize <code>access_key_id</code> and <code>access_key_secret</code> variables which represent the <strong>Access Key ID</strong> and <strong>Secret Access Key</strong> values you generated.</p>
<br />
<p>Rclone is a command-line tool which manages files on cloud storage. You can use rclone to upload objects to R2 concurrently.</p>
<h2 id="configure-rclone">Configure rclone</h2>
<p>With <a href="https://rclone.org/install/"><code>rclone</code></a> installed, you may run <a href="https://rclone.org/s3/"><code>rclone config</code></a> to configure a new S3 storage provider. You will be prompted with a series of questions for the new provider details.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommendation">Recommendation</h3>
@markup("md", "content/.markup/bodies/11457.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11458.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11456.md")
</aside>
<h3 id="edit-an-existing-rclone-configuration">Edit an existing rclone configuration</h3>
<p>If you have already configured <code>rclone</code> in the past, you may run <code>rclone config file</code> to print the location of your <code>rclone</code> configuration file:</p>
<pre><code class="language-sh">rclone config file&#10;&#35; Configuration file is stored at:&#10;&#35; ~/.config/rclone/rclone.conf&#10;</code></pre>
<p>Then use an editor (<code>nano</code> or <code>vim</code>, for example) to add or edit the new provider. This example assumes you are adding a new <code>r2</code> provider:</p>
<pre><code class="language-toml">[r2]&#10;type = s3&#10;provider = Cloudflare&#10;access_key_id = abc123&#10;secret_access_key = xyz456&#10;endpoint = https://&lt;accountid&gt;.r2.cloudflarestorage.com&#10;acl = private&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11455.md")
</aside>
<p>You may then use the new <code>rclone</code> provider for any of your normal workflows.</p>
<h2 id="list-buckets-objects">List buckets &amp; objects</h2>
<p>The <a href="https://rclone.org/commands/rclone_tree/">rclone tree</a> command can be used to list the contents of the remote, in this case Cloudflare R2.</p>
<pre><code class="language-sh">rclone tree r2:&#10;&#35; /&#10;&#35; ├── user-uploads&#10;&#35; │   └── foobar.png&#10;&#35; └── my-bucket-name&#10;&#35;     ├── cat.png&#10;&#35;     └── todos.txt&#10;&#10;rclone tree r2:my-bucket-name&#10;&#35; /&#10;&#35; ├── cat.png&#10;&#35; └── todos.txt&#10;</code></pre>
<h2 id="upload-and-retrieve-objects">Upload and retrieve objects</h2>
<p>The <a href="https://rclone.org/commands/rclone_copy/">rclone copy</a> command can be used to upload objects to an R2 bucket and vice versa - this allows you to upload files up to the 5 TB maximum object size that R2 supports.</p>
<pre><code class="language-sh">&#35; Upload dog.txt to the user-uploads bucket&#10;rclone copy dog.txt r2:user-uploads/&#10;rclone tree r2:user-uploads&#10;&#35; /&#10;&#35; ├── foobar.png&#10;&#35; └── dog.txt&#10;&#10;&#35; Download dog.txt from the user-uploads bucket&#10;rclone copy r2:user-uploads/dog.txt .&#10;</code></pre>
<h3 id="a-note-about-multipart-upload-part-sizes">A note about multipart upload part sizes</h3>
<p>For multipart uploads, part sizes can significantly affect the number of Class A operations that are used, which can alter how much you end up being charged.
Every part upload counts as a separate operation, so larger part sizes will use fewer operations, but might be costly to retry if the upload fails. Also consider that a multipart upload is always going to consume at least 3 times as many operations as a single <code>PutObject</code>, because it will include at least one <code>CreateMultipartUpload</code>, <code>UploadPart</code> &amp; <code>CompleteMultipartUpload</code> operations.</p>
<p>Balancing part size depends heavily on your use-case, but these factors can help you minimize your bill, so they are worth thinking about.</p>
<p>You can configure rclone's multipart upload part size using the <code>--s3-chunk-size</code> CLI argument. Note that you might also have to adjust the <code>--s3-upload-cutoff</code> argument to ensure that rclone is using multipart uploads. Both of these can be set in your configuration file as well. Generally, <code>--s3-upload-cutoff</code> will be no less than <code>--s3-chunk-size</code>.</p>
<pre><code class="language-sh">rclone copy long-video.mp4 r2:user-uploads/ --s3-upload-cutoff=100M --s3-chunk-size=100M&#10;</code></pre>
<h2 id="generate-presigned-urls">Generate presigned URLs</h2>
<p>You can also generate presigned links which allow you to share public access to a file temporarily using the <a href="https://rclone.org/commands/rclone_link/">rclone link</a> command.</p>
<pre><code class="language-sh">&#35; You can pass the --expire flag to determine how long the presigned link is valid. The --unlink flag isn&#x27;t supported by R2.&#10;rclone link r2:my-bucket-name/cat.png --expire 3600&#10;&#35; https://&lt;accountid&gt;.r2.cloudflarestorage.com/my-bucket-name/cat.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=&lt;credential&gt;&amp;X-Amz-Date=&lt;timestamp&gt;&amp;X-Amz-Expires=3600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=&lt;signature&gt;&#10;</code></pre>
