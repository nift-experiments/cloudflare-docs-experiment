<h2 id="introduction">Introduction</h2>
<p>Migrating data between cloud object storage providers can be challenging and expensive. You need to ensure no objects are missed, especially when new data is coming in during your migration. Additionally, there may be a significant one-time data transfer fee to consider.</p>
<p>In order to address these challenges, Cloudflare has created two migration tools: <a href="/r2/data-migration/sippy/">Sippy</a> and <a href="/r2/data-migration/super-slurper/">Super Slurper</a>. Sippy is an on-demand data migration service, and it is the primary focus of this reference architecture diagram. On the other hand, Super Slurper is designed for large-scale, one-time migrations to Cloudflare's global object storage service, <a href="/r2/">R2</a>. Moving all your data at once may not work for your scenario, so Sippy can help with that.</p>
<p>Sippy enables you to transfer data from other cloud providers to Cloudflare R2 as the data is requested. This workflow is ideal for situations where you want to avoid large upfront data transfer bills and selectively migrate data as it's accessed.</p>
<p>Migration-specific egress fees incurred when using other vendors cloud storage are reduced by leveraging requests within the flow of your application where you would already be paying egress fees to copy objects to R2 simultaneously.</p>
<p>Use Sippy to migrate your commonly accessed data objects and immediately start saving on egress fees. Then, use Super Sluper to migrate any remaining data.</p>
<p>Here's how Sippy works: it will first attempt to retrieve an object from R2 storage. If the object is not in R2, it will retrieve the object from your source cloud object storage. At the same time, it will add the object to R2 for future access, ensuring a seamless and efficient data migration process.</p>
<h2 id="on-demand-object-storage-data-migration-with-sippy">On-demand Object Storage Data Migration with Sippy</h2>
<p><img src="/assets/upstream/images/reference-architecture/on-demand-object-storage-migration/sippy-migration-diagram.svg" alt="Figure 1: R2 On-demand Object Storage Data Migration with Sippy" title="Figure 1: On-demand Object Storage Data Migration with Sippy" /></p>
<ol>
<li>The client requests an object from R2 using<a href="https://developers.cloudflare.com/r2/api/workers/"> Workers</a>,<a href="https://developers.cloudflare.com/r2/api/s3/"> S3 API</a>, or<a href="https://developers.cloudflare.com/r2/buckets/public-buckets/"> public bucket</a>.</li>
<li>If the object is found in your R2 bucket it is served to the client.</li>
<li>If the object is not found in R2, the object will simultaneously be returned from your source storage bucket and copied to R2. Note: Some large objects may take multiple requests to copy to R2 because they are copied over as multipart uploads. From the client’s perspective they will still get the file they are requesting.</li>
</ol>
<p>After objects are copied, subsequent requests will be served from R2 and you’ll begin saving on egress fees immediately.</p>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/r2/data-migration/sippy/">Sippy Documentation</a></li>
<li><a href="/r2/data-migration/super-slurper/">Super Slurper Documentation</a></li>
</ul>
