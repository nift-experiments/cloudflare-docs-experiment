<p>You can delete objects from R2 using the dashboard, Workers API, S3 API, or command-line tools. To empty or delete an entire bucket, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a>.</p>
<h2 id="delete-via-dashboard">Delete via dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your bucket.
3. (Optional) Select the **View prefixes as directories** checkbox to view prefixes grouped as [folders](/r2/objects/#prefixes-and-folders).
4. Select the objects or folders you want to delete. You can select a mix of both in the same operation.
5. Select **Delete**.
6. Confirm your choice in the dialog that appears.
<p>To delete all objects in a bucket at once, refer to <a href="/r2/buckets/delete-buckets/#empty-a-bucket">Empty a bucket</a>.</p>
<h2 id="delete-via-workers-api">Delete via Workers API</h2>
<p>Use R2 <a href="/workers/runtime-apis/bindings/">bindings</a> in Workers to delete objects:</p>
<pre><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		await env.MY_BUCKET.delete(&quot;image.png&quot;);&#10;		return new Response(&quot;Deleted&quot;);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>For complete documentation, refer to <a href="/r2/api/workers/workers-api-usage/">Workers API</a>.</p>
<h2 id="delete-via-s3-api">Delete via S3 API</h2>
<p>Use S3-compatible SDKs to delete objects. You'll need your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/r2/api/tokens/">R2 API token</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11407.md")
</div></div>
<p>For complete S3 API documentation, refer to <a href="/r2/api/s3/api/">S3 API</a>.</p>
<h2 id="delete-via-wrangler">Delete via Wrangler</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11404.md")
</aside>
<p>Use <a href="/workers/wrangler/install-and-update/">Wrangler</a> to delete objects. Run the <a href="/workers/wrangler/commands/r2/#r2-object-delete"><code>r2 object delete</code> command</a>:</p>
<pre><code class="language-sh">wrangler r2 object delete test-bucket/image.png&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/r2/buckets/delete-buckets/"><h3 id="card-delete-buckets-r2-buckets-delete-buckets">Delete buckets</h3><p>Empty all objects from a bucket and permanently delete it.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/bucket-locks/"><h3 id="card-bucket-locks-r2-buckets-bucket-locks">Bucket locks</h3><p>Protect objects from accidental deletion with retention policies.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/object-lifecycles/"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles">Object lifecycles</h3><p>Automatically expire objects after a specified period.</p></a></p>
