<p><a href="/workers/">Workers</a> let you run code at the edge. When you bind an R2 bucket to a Worker, you can read and write objects directly using the <a href="/r2/api/workers/workers-api-usage/">Workers API</a>.</p>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p>A bucket stores your objects in R2. To create a new R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11413.md")
</div></div>
<h2 id="2-create-a-worker-with-an-r2-binding"><ol start="2">
<li>Create a Worker with an R2 binding</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11415.md")
</div>
<h2 id="3-read-and-write-objects"><ol start="3">
<li>Read and write objects</li>
</ol></h2>
<p>Use the binding to interact with your bucket. This example stores and retrieves objects based on the URL path:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11418.md")
</div></div>
<h2 id="4-test-and-deploy"><ol start="4">
<li>Test and deploy</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11419.md")
</div>
<p>Refer to the <a href="/r2/api/workers/workers-api-usage/">Workers R2 API documentation</a> for the complete API reference.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/r2/api/s3/presigned-urls/"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls">Presigned URLs</h3><p>Generate temporary URLs for private object access.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/public-buckets/"><h3 id="card-public-buckets-r2-buckets-public-buckets">Public buckets</h3><p>Serve files directly over HTTP with a public bucket.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/cors/"><h3 id="card-cors-r2-buckets-cors">CORS</h3><p>Configure CORS for browser-based uploads.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/object-lifecycles/"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles">Object lifecycles</h3><p>Set up lifecycle rules to automatically delete old objects.</p></a></p>
