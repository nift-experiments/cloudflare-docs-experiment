<p>This page details R2's consistency model, including where R2 is strongly, globally consistent and which operations this applies to.</p>
<p>R2 can be described as &quot;strongly consistent&quot;, especially in comparison to other distributed object storage systems. This strong consistency ensures that operations against R2 see the latest (accurate) state: clients should be able to observe the effects of any write, update and/or delete operation immediately, globally.</p>
<h2 id="terminology">Terminology</h2>
<p>In the context of R2, <em>strong</em> consistency and <em>eventual</em> consistency have the following meanings:</p>
<ul>
<li><strong>Strongly consistent</strong> - The effect of an operation will be observed globally, immediately, by all clients. Clients will not observe 'stale' (inconsistent) state.</li>
<li><strong>Eventually consistent</strong> - Clients may not see the effect of an operation immediately. The state may take a some time (typically seconds to a minute) to propagate globally.</li>
</ul>
<h2 id="operations-and-consistency">Operations and Consistency</h2>
<p>Operations against R2 buckets and objects adhere to the following consistency guarantees:</p>
<table-wrap>
<table>
<thead>
<tr>
<th>Action</th>
<th>Consistency</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read-after-write: Write (upload) an object, then read it</td>
<td>Strongly consistent: readers will immediately see the latest object globally</td>
</tr>
<tr>
<td>Metadata: Update an object's metadata</td>
<td>Strongly consistent: readers will immediately see the updated metadata globally</td>
</tr>
<tr>
<td>Deletion: Delete an object</td>
<td>Strongly consistent: reads to that object will immediately return a &quot;does not exist&quot; error</td>
</tr>
<tr>
<td>Object listing: List the objects in a bucket</td>
<td>Strongly consistent: the list operation will list all objects at that point in time</td>
</tr>
<tr>
<td>IAM: Adding/removing R2 Storage permissions</td>
<td>Eventually consistent: A <a href="/fundamentals/api/get-started/create-token/">new or updated API key</a> may take up to a minute to have permissions reflected globally</td>
</tr>
</tbody>
</table>
</table-wrap>
<p>Additional notes:</p>
<ul>
<li>In the event two clients are writing (<code>PUT</code> or <code>DELETE</code>) to the same key, the last writer to complete &quot;wins&quot;.</li>
<li>When performing a multipart upload, read-after-write consistency continues to apply once all parts have been successfully uploaded. In the case the same part is uploaded (in error) from multiple writers, the last write will win.</li>
<li>Copying an object within the same bucket also follows the same read-after-write consistency that writing a new object would. The &quot;copied&quot; object is immediately readable by all clients once the copy operation completes.</li>
<li>To delete an R2 bucket, it must be completely empty before deletion is allowed. If you attempt to delete a bucket that still contains objects, you will receive an error such as: <code>The bucket you tried to delete (X) is not empty (account Y)</code> or <code>Bucket X cannot be deleted because it isn’t empty.</code> For instructions on emptying and deleting a bucket, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a>.</li>
</ul>
<h2 id="caching">Caching</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11372.md")
</aside>
<p>When connecting a <a href="/r2/buckets/public-buckets/#custom-domains">custom domain</a> to an R2 bucket and enabling caching for objects served from that bucket, the consistency model is necessarily relaxed when accessing content via a domain with caching enabled.</p>
<p>Specifically, you should expect:</p>
<ul>
<li>An object you delete from R2, but that is still cached, will still be available. You should <a href="/cache/how-to/purge-cache/">purge the cache</a> after deleting objects if you need that delete to be reflected.</li>
<li>By default, Cloudflare’s cache will <a href="/cache/how-to/configure-cache-status-code/#edge-ttl">cache HTTP 404 (Not Found) responses</a> automatically. If you upload an object to that same path, the cache may continue to return HTTP 404s until the cache TTL (Time to Live) expires and the new object is fetched from R2 or the <a href="/cache/how-to/purge-cache/">cache is purged</a>.</li>
<li>An object for a given key is overwritten with a new object: the old (previous) object will continue to be served to clients until the cache TTL expires (or the object is evicted) or the cache is purged.</li>
</ul>
<p>The cache does not affect access via <a href="/r2/api/workers/">Worker API bindings</a> or the <a href="/r2/api/s3/">S3 API</a>, as these operations are made directly against the bucket and do not transit through the cache.</p>
