<p>Sippy is a data migration service that allows you to copy data from other cloud providers to R2 as the data is requested, without paying unnecessary cloud egress fees typically associated with moving large amounts of data.</p>
<p>Migration-specific egress fees are reduced by leveraging requests within the flow of your application where you would already be paying egress fees to simultaneously copy objects to R2.</p>
<h2 id="how-it-works">How it works</h2>
<p>When enabled for an R2 bucket, Sippy implements the following migration strategy across <a href="/r2/api/workers/">Workers</a>, <a href="/r2/api/s3/">S3 API</a>, and <a href="/r2/buckets/public-buckets/">public buckets</a>:</p>
<ul>
<li>When an object is requested, it is served from your R2 bucket if it is found.</li>
<li>If the object is not found in R2, the object will simultaneously be returned from your source storage bucket and copied to R2.</li>
<li>All other operations, including put and delete, continue to work as usual.</li>
</ul>
<h2 id="when-is-sippy-useful">When is Sippy useful?</h2>
<p>Using Sippy as part of your migration strategy can be a good choice when:</p>
<ul>
<li>You want to start migrating your data, but you want to avoid paying upfront egress fees to facilitate the migration of your data all at once.</li>
<li>You want to experiment by serving frequently accessed objects from R2 to eliminate egress fees, without investing time in data migration.</li>
<li>You have frequently changing data and are looking to conduct a migration while avoiding downtime. Sippy can be used to serve requests while <a href="/r2/data-migration/super-slurper/">Super Slurper</a> can be used to migrate your remaining data.</li>
</ul>
<p>If you are looking to migrate all of your data from an existing cloud provider to R2 at one time, we recommend using <a href="/r2/data-migration/super-slurper/">Super Slurper</a>.</p>
<h2 id="get-started-with-sippy">Get started with Sippy</h2>
<p>Before getting started, you will need:</p>
<ul>
<li>An existing R2 bucket. If you don't already have one, refer to <a href="/r2/buckets/create-buckets/">Create buckets</a>.</li>
<li><a href="/r2/data-migration/sippy/#create-credentials-for-storage-providers">API credentials</a> for your source object storage bucket.</li>
<li>(Wrangler only) Cloudflare R2 Access Key ID and Secret Access Key with read and write permissions. For more information, refer to <a href="/r2/api/tokens/">Authentication</a>.</li>
</ul>
<h3 id="enable-sippy-via-the-dashboard">Enable Sippy via the Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11468.md")
</div>
<h3 id="enable-sippy-via-wrangler">Enable Sippy via Wrangler</h3>
<h4 id="set-up-wrangler">Set up Wrangler</h4>
<p>To begin, install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>. Then <a href="/workers/wrangler/install-and-update/">install Wrangler, the Developer Platform CLI</a>.</p>
<h4 id="enable-sippy-on-your-r2-bucket">Enable Sippy on your R2 bucket</h4>
<p>Log in to Wrangler with the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code> command</a>. Then run the <a href="/workers/wrangler/commands/r2/#r2-bucket-sippy-enable"><code>r2 bucket sippy enable</code> command</a>:</p>
<pre><code class="language-sh">npx wrangler r2 bucket sippy enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>This will prompt you to select between supported object storage providers and lead you through setup.</p>
<h3 id="enable-sippy-via-api">Enable Sippy via API</h3>
<p>For information on required parameters and examples of how to enable Sippy, refer to the <a href="/api/resources/r2/subresources/buckets/subresources/sippy/methods/update/">API documentation</a>. For information about getting started with the Cloudflare API, refer to <a href="/fundamentals/api/how-to/make-api-calls/">Make API calls</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11467.md")
</aside>
<h3 id="view-migration-metrics">View migration metrics</h3>
<p>When enabled, Sippy exposes metrics that help you understand the progress of your ongoing migrations.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests served by Sippy</td>
<td>The percentage of overall requests served by R2 over a period of time. A higher percentage indicates that fewer requests need to be made to the source bucket.</td>
</tr>
<tr>
<td>Data migrated by Sippy</td>
<td>The amount of data that has been copied from the source bucket to R2 over a period of time. Reported in bytes.</td>
</tr>
</tbody>
</table>
<p>To view current and historical metrics:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11469.md")
</div>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="disable-sippy-on-your-r2-bucket">Disable Sippy on your R2 bucket</h2>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11470.md")
</div>
<h3 id="wrangler">Wrangler</h3>
<p>To disable Sippy, run the <a href="/workers/wrangler/commands/r2/#r2-bucket-sippy-disable"><code>r2 bucket sippy disable</code> command</a>:</p>
<pre><code class="language-sh">npx wrangler r2 bucket sippy disable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<h3 id="api">API</h3>
<p>For more information on required parameters and examples of how to disable Sippy, refer to the <a href="/api/resources/r2/subresources/buckets/subresources/sippy/methods/delete/">API documentation</a>.</p>
<h2 id="supported-cloud-storage-providers">Supported cloud storage providers</h2>
<p>Cloudflare currently supports copying data from the following cloud object storage providers to R2:</p>
<ul>
<li>Amazon S3</li>
<li>Google Cloud Storage (GCS)</li>
<li>Azure Blob Storage</li>
<li>S3-compatible storage providers</li>
</ul>
<h2 id="r2-api-interactions">R2 API interactions</h2>
<p>When Sippy is enabled, it changes the behavior of certain actions on your R2 bucket across <a href="/r2/api/workers/">Workers</a>, <a href="/r2/api/s3/">S3 API</a>, and <a href="/r2/buckets/public-buckets/">public buckets</a>.</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>New behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>GetObject</td>
<td>Calls to GetObject will first attempt to retrieve the object from your R2 bucket. If the object is not present, the object will be served from the source storage bucket and simultaneously uploaded to the requested R2 bucket.<br/><br/>Additional considerations:<ul><li>Modifications to objects in the source bucket will not be reflected in R2 after the initial copy. Once an object is stored in R2, it will not be re-retrieved and updated.</li><li>Only user-defined metadata that is prefixed by <code>x-amz-meta-</code> in the HTTP response will be migrated. Remaining metadata will be omitted.</li><li>For larger objects (greater than 199 MiB), multiple GET requests may be required to fully copy the object to R2.</li><li>If there are multiple simultaneous GET requests for an object which has not yet been fully copied to R2, Sippy may fetch the object from the source storage bucket multiple times to serve those requests.</li></ul></td>
</tr>
<tr>
<td>HeadObject</td>
<td>Behaves similarly to GetObject, but only retrieves object metadata. Will not copy objects to the requested R2 bucket.</td>
</tr>
<tr>
<td>PutObject</td>
<td>No change to behavior. Calls to PutObject will add objects to the requested R2 bucket.</td>
</tr>
<tr>
<td>DeleteObject</td>
<td>No change to behavior. Calls to DeleteObject will delete objects in the requested R2 bucket.<br/><br/>Additional considerations:<ul><li>If deletes to objects in R2 are not also made in the source storage bucket, subsequent GetObject requests will result in objects being retrieved from the source bucket and copied to R2.</li></ul></td>
</tr>
</tbody>
</table>
<p>Actions not listed above have no change in behavior. For more information, refer to <a href="/r2/api/workers/workers-api-reference/">Workers API reference</a> or <a href="/r2/api/s3/api/">S3 API compatibility</a>.</p>
<h2 id="create-credentials-for-storage-providers">Create credentials for storage providers</h2>
<h3 id="amazon-s3">Amazon S3</h3>
<p>To copy objects from Amazon S3, Sippy requires access permissions to your bucket. While you can use any AWS Identity and Access Management (IAM) user credentials with the correct permissions, Cloudflare recommends you create a user with a narrow set of permissions.</p>
<p>To create credentials with the correct permissions:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11471.md")
</div>
<p>You can now use both the Access Key ID and Secret Access Key when enabling Sippy.</p>
<h3 id="google-cloud-storage">Google Cloud Storage</h3>
<p>To copy objects from Google Cloud Storage (GCS), Sippy requires access permissions to your bucket. Cloudflare recommends using the Google Cloud predefined <code>Storage Object Viewer</code> role.</p>
<p>To create credentials with the correct permissions:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11472.md")
</div>
<p>You can now use this JSON key file when enabling Sippy via Wrangler or API.</p>
<h3 id="azure-blob-storage">Azure Blob Storage</h3>
<p>To copy objects from Azure Blob Storage, Sippy requires the name of your Azure Storage account, the container to copy from, and either an account key or a shared access signature (SAS) token. Provide exactly one of the two credential types. Sippy needs read and list permissions on the container.</p>
<p>To use an account key:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11473.md")
</div>
<p>To use a SAS token instead, Cloudflare recommends scoping it to only the container you are migrating:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11474.md")
</div>
<p>You can now use the account name, container name, and either the account key or SAS token when enabling Sippy.</p>
<h3 id="s3-compatible-storage">S3-compatible storage</h3>
<p>To copy objects from an S3-compatible storage provider, Sippy requires the S3 API endpoint URL for your bucket, along with an Access Key ID and Secret Access Key that can read from it. Cloudflare recommends scoping these credentials to only allow reads from the bucket you are migrating.</p>
<p>Refer to the documentation for your storage provider to find the S3 API endpoint for your bucket and to create read-only access credentials.</p>
<p>You can now use the bucket URL, Access Key ID, and Secret Access Key when enabling Sippy.</p>
<h2 id="caveats">Caveats</h2>
<h3 id="etags">ETags</h3>
<p>While R2's ETag generation is compatible with S3's during the regular course of operations, ETags are not guaranteed to be equal when an object is migrated using Sippy.
Sippy makes autonomous decisions about the operations it uses when migrating objects to optimize for performance and network usage. It may choose to migrate an object in multiple parts, which affects <a href="/r2/objects/upload-objects/#etags">ETag calculation</a>.</p>
<p>For example, a 320 MiB object originally uploaded to S3 using a single <code>PutObject</code> operation might be migrated to R2 via multipart operations. In this case, its ETag on R2 will not be the same as its ETag on S3.
Similarly, an object originally uploaded to S3 using multipart operations might also have a different ETag on R2 if the part sizes Sippy chooses for its migration differ from the part sizes this object was originally uploaded with.</p>
<p>Relying on matching ETags before and after the migration is therefore discouraged.</p>
