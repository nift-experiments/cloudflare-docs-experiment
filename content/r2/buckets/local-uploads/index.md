<p>You can enable Local Uploads on your bucket to improve the performance of upload requests when clients upload data from a different region than your bucket. Local Uploads writes object data to a nearby location, then asynchronously copies it to your bucket. Data is available immediately and remains strongly consistent.</p>
<h2 id="how-it-works">How it works</h2>
<p>The following sections describe how R2 handles upload requests with and without Local Uploads enabled.</p>
<h3 id="without-local-uploads">Without Local Uploads</h3>
<p>When a client uploads an object to your R2 bucket, the object data must travel from the client to the storage infrastructure of your bucket. This behavior can result in higher latency and lower reliability when your client is in a different region than the bucket. Refer to <a href="/r2/how-r2-works/">How R2 works</a> for details.</p>
<h3 id="with-local-uploads">With Local Uploads</h3>
<p>When you make an upload request (i.e. <code>PutObject</code> and <code>UploadPart</code>) to a bucket with Local Uploads enabled, there are two cases that are handled:</p>
<ul>
<li><strong>Client and bucket in same region:</strong> R2 follows the normal upload flow where object data is uploaded from the client to the storage infrastructure of your bucket.</li>
<li><strong>Client and bucket in different regions:</strong> Object data is written to storage near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains durable during the process.</li>
</ul>
<div class="nb-interactive-component" data-cf-component="R2LocalUploadsDiagram"></div>
<h2 id="when-to-use-local-uploads">When to use local uploads</h2>
<p>Local uploads are built for workloads that receive a lot of uploads originating from different geographic regions than where your bucket is located. This feature is ideal when:</p>
<ul>
<li>Your users are globally distributed</li>
<li>Upload performance and reliability is critical to your application</li>
<li>You want to optimize write performance without changing your bucket's primary location</li>
</ul>
<p>To understand the geographic distribution of where your read and write requests are initiated:</p>
<ol>
<li>Log in to the Cloudflare dashboard, and go to R2 Overview.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your bucket.</li>
<li>Select <strong>Metrics</strong> and view the <strong>Request Distribution</strong> chart.</li>
</ol>
<h3 id="read-latency-considerations">Read latency considerations</h3>
<p>When local uploads is enabled, uploaded data may temporarily reside near the client before replication completes.</p>
<p>If your workload requires immediate read after write, consider where your read requests originate. Reads from the uploader's region will be fast, while reads from near the bucket's region may experience cross-region latency until replication completes.</p>
<h3 id="jurisdiction-restriction">Jurisdiction restriction</h3>
<p>Local uploads are not supported for buckets with <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdictional restrictions</a>, because it requires temporarily routing data through locations outside the bucket’s region.</p>
<h2 id="enable-local-uploads">Enable local uploads</h2>
<p>When you enable Local Uploads, existing uploads will complete as expected with no interruption to traffic.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11485.md")
</div></div>
<h2 id="disable-local-uploads">Disable local uploads</h2>
<p>You can disable local uploads at any time. Existing requests made with local uploads will complete replication with no interruption to your traffic.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11488.md")
</div></div>
<h2 id="pricing">Pricing</h2>
<p>There is <strong>no additional cost</strong> to enable local uploads. Upload requests made with this feature enabled incur the standard <a href="/r2/pricing/">Class A operation costs</a>, same as upload requests made without local uploads.</p>
