<p>R2 provides three API surfaces for interacting with your data:</p>
<ul>
<li><strong><a href="/r2/api/workers/workers-api-reference/">Workers API</a>:</strong> An in-Worker API accessed by binding an R2 bucket to a <a href="/workers/">Worker</a>. Use the Workers API to read, write, and list objects from within a Worker.</li>
<li><strong><a href="/r2/api/s3/api/">S3-compatible API</a>:</strong> An S3-compatible HTTP API available at <code>https://&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com</code>. Use existing S3 SDKs and tools to interact with R2.</li>
<li><strong><a href="/api/resources/r2/">Cloudflare REST API</a>:</strong> The <code>api.cloudflare.com</code> REST API used by the Cloudflare Dashboard and Wrangler CLI. Supports bucket management and object operations. <a href="/r2/platform/limits/#cloudflare-rest-api">Rate limits apply</a>. Use the S3-compatible API or Workers API for high-throughput workloads.</li>
</ul>
