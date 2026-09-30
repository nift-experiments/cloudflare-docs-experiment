<p>Cloudflare R2 is an S3-compatible object storage service with no egress fees, built on Cloudflare's global network. It is <a href="/r2/reference/consistency/">strongly consistent</a> and designed for high <a href="/r2/reference/durability/">data durability</a>.</p>
<p>R2 is ideal for storing and serving unstructured data that needs to be accessed frequently over the internet, without incurring egress fees. It's a good fit for workloads like serving web assets, training AI models, and managing user-generated content.</p>
<h2 id="architecture">Architecture</h2>
<p>R2's architecture is composed of multiple components:</p>
<ul>
<li>
<p><strong>R2 Gateway:</strong> The entry point for all API requests that handles authentication and routing logic. This service is deployed across Cloudflare's global network via <a href="/workers/">Cloudflare Workers</a>.</p>
</li>
<li>
<p><strong>Metadata Service:</strong> A distributed layer built on <a href="/durable-objects/">Durable Objects</a> used to store and manage object metadata (e.g. object key, checksum) to ensure strong consistency of the object across the storage system. It includes a built-in cache layer to speed up access to metadata.</p>
</li>
<li>
<p><strong>Tiered Read Cache:</strong> A caching layer that sits in front of the Distributed Storage Infrastructure that speeds up object reads by using <a href="/cache/how-to/tiered-cache/">Cloudflare Tiered Cache</a> to serve data closer to the client.</p>
</li>
<li>
<p><strong>Distributed Storage Infrastructure:</strong> The underlying infrastructure that persistently stores encrypted object data.</p>
</li>
</ul>
<p><img src="/images/r2/r2-architecture.png" alt="R2 Architecture" /></p>
<p>R2 supports multiple client interfaces including <a href="/r2/api/workers/workers-api-usage/">Cloudflare Workers Binding</a>, <a href="/r2/api/s3/api/">S3-compatible API</a>, and a <a href="/api/resources/r2/">REST API</a> that powers the Cloudflare Dashboard and Wrangler CLI. All requests are routed through the R2 Gateway, which coordinates with the Metadata Service and Distributed Storage Infrastructure to retrieve the object data.</p>
<h2 id="write-data-to-r2">Write data to R2</h2>
<p>When a write request (e.g. uploading an object) is made to R2, the following sequence occurs:</p>
<ol>
<li>
<p><strong>Request handling:</strong> The request is received by the R2 Gateway at the edge, close to the user, where it is authenticated.</p>
</li>
<li>
<p><strong>Encryption and routing:</strong> The Gateway reaches out to the Metadata Service to retrieve the <a href="/r2/reference/data-security/">encryption key</a> and determines which storage cluster to write the encrypted data to within the <a href="/r2/reference/data-location/">location</a> set for the bucket.</p>
</li>
<li>
<p><strong>Writing to storage:</strong> The encrypted data is written and stored in the distributed storage infrastructure, and replicated within the region (e.g. ENAM) for <a href="/r2/reference/durability/">durability</a>.</p>
</li>
<li>
<p><strong>Metadata commit:</strong> Finally, the Metadata Service commits the object's metadata, making it visible in subsequent reads. Only after this commit is an <code>HTTP 200</code> success response sent to the client, preventing unacknowledged writes.</p>
</li>
</ol>
<p><img src="/images/r2/write-data-to-r2.png" alt="Write data to R2" /></p>
<h2 id="read-data-from-r2">Read data from R2</h2>
<p>When a read request (e.g. fetching an object) is made to R2, the following sequence occurs:</p>
<ol>
<li>
<p><strong>Request handling:</strong> The request is received by the R2 Gateway at the edge, close to the user, where it is authenticated.</p>
</li>
<li>
<p><strong>Metadata lookup:</strong> The Gateway asks the Metadata Service for the object metadata.</p>
</li>
<li>
<p><strong>Reading the object:</strong> The Gateway attempts to retrieve the <a href="/r2/reference/data-security/">encrypted</a> object from the tiered read cache. If it's not available, it retrieves the object from one of the distributed storage data centers within the region that holds the object data.</p>
</li>
<li>
<p><strong>Serving to client:</strong> The object is decrypted and served to the user.</p>
</li>
</ol>
<p><img src="/images/r2/read-data-to-r2.png" alt="Read data to R2" /></p>
<h2 id="performance">Performance</h2>
<p>The performance of your operations can be influenced by factors such as the bucket's geographical location, request origin, and access patterns.</p>
<p>To optimize upload performance for cross-region requests, enable <a href="/r2/buckets/local-uploads/">Local Uploads</a> on your bucket.</p>
<p>To optimize read performance, enable <a href="/cache/">Cloudflare Cache</a> when using a <a href="/r2/buckets/public-buckets/#custom-domains">custom domain</a>. When caching is enabled, read requests can bypass the R2 Gateway and be served directly from Cloudflare's edge cache, reducing latency. Note that cached data may not reflect the latest version immediately.</p>
<p><img src="/images/r2/read-data-to-r2-with-cloudflare-cache.png" alt="Read data to R2 with Cloudflare Cache" /></p>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/r2/reference/consistency/"><h3 id="card-consistency-r2-reference-consistency">Consistency</h3><p>Learn about R2's consistency model.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/reference/durability/"><h3 id="card-durability-r2-reference-durability">Durability</h3><p>Learn more about R2's durability guarantee.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/reference/data-location/#jurisdictional-restrictions"><h3 id="card-data-location-r2-reference-data-location-jurisdictional-restrictions"> Data location</h3><p>Learn how R2 determines where data is stored, and details on jurisdiction restrictions.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/reference/data-security/"><h3 id="card-data-security-r2-reference-data-security">Data security</h3><p>Learn about R2's data security properties.</p></a></p>
