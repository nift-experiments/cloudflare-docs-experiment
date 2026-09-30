<p>Manage R2 buckets and objects directly from your terminal. Use CLI tools to automate tasks and manage objects.</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/wrangler/">Wrangler</a></td>
<td>Single object operations and managing bucket settings with minimal setup</td>
</tr>
<tr>
<td><a href="/r2/examples/rclone/">rclone</a></td>
<td>Bulk object operations, migrations, and syncing directories</td>
</tr>
<tr>
<td><a href="/r2/examples/aws/aws-cli/">AWS CLI</a></td>
<td>Existing AWS workflows or familiarity with AWS CLI</td>
</tr>
</tbody>
</table>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p>A bucket stores your objects in R2. To create a new R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11435.md")
</div></div>
<h2 id="2-generate-api-credentials"><ol start="2">
<li>Generate API credentials</li>
</ol></h2>
<p>CLI tools that use the S3 API (<a href="/r2/examples/aws/aws-cli/">AWS CLI</a>, <a href="/r2/examples/rclone/">rclone</a>) require an Access Key ID and Secret Access Key. If you are using <a href="/workers/wrangler/">Wrangler</a>, you can skip this step.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11436.md")
</div>
<h2 id="3-set-up-a-cli-tool"><ol start="3">
<li>Set up a CLI tool</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11443.md")
</div></div>
<h2 id="4-upload-and-download-objects"><ol start="4">
<li>Upload and download objects</li>
</ol></h2>
<p>(Optional) Create a test file to upload. Run this command in the directory where you plan to run the CLI commands:</p>
<pre><code class="language-sh">echo &#x27;Hello, R2!&#x27; &gt; myfile.txt&#10;</code></pre>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11447.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/r2/api/s3/presigned-urls/"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls">Presigned URLs</h3><p>Generate temporary URLs for private object access.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/public-buckets/"><h3 id="card-public-buckets-r2-buckets-public-buckets">Public buckets</h3><p>Serve files directly over HTTP with a public bucket.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/cors/"><h3 id="card-cors-r2-buckets-cors">CORS</h3><p>Configure CORS for browser-based uploads.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/object-lifecycles/"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles">Object lifecycles</h3><p>Set up lifecycle rules to automatically delete old objects.</p></a></p>
