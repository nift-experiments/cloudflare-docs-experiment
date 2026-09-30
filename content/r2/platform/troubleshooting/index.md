<h2 id="troubleshooting-403-cors-issues-with-r2">Troubleshooting 403 / CORS issues with R2</h2>
<p>If you are encountering a CORS error despite setting up everything correctly, you may follow this troubleshooting guide to help you.</p>
<p>If you see a 401/403 error above the CORS error in your browser console, you are dealing with a different issue (not CORS related).</p>
<p>If you do have a CORS issue, refer to <a href="#if-it-is-actually-cors">Resolving CORS issues</a>.</p>
<h3 id="if-you-are-using-a-custom-domain">If you are using a custom domain</h3>
<ol>
<li>Open developer tools on your browser.</li>
<li>Go to the <strong>Network</strong> tab and find the failing request. You may need to reload the page, as requests are only logged after developer tools have been opened.</li>
<li>Check the response headers for the following two headers:</li>
</ol>
<ul>
<li><code>cf-cache-status</code></li>
<li><code>cf-mitigated</code></li>
</ul>
<h4 id="if-you-have-a-cf-mitigated-header">If you have a <code>cf-mitigated</code> header</h4>
<p>Your request was blocked by one of your WAF rules. Inspect your <a href="/waf/analytics/security-events/">Security Events</a> to identify the cause of the block.</p>
<h4 id="if-you-do-not-have-a-cf-cache-status-header">If you do not have a <code>cf-cache-status</code> header</h4>
<p>Your request was blocked by <a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a>.</p>
<p>Edit your Hotlink Protection settings using a <a href="/rules/configuration-rules/">Configuration Rule</a>, or disable it completely.</p>
<h3 id="if-you-are-using-the-s3-api">If you are using the S3 API</h3>
<p>Your request may be incorrectly signed. You may obtain a better error message by trying the request over curl.</p>
<p>Refer to the working S3 signing examples on the <a href="/r2/examples/aws/">Examples</a> page.</p>
<h3 id="if-it-is-actually-cors">If it is actually CORS</h3>
<p>Here are some common issues with CORS configurations:</p>
<ul>
<li><code>ExposeHeaders</code> is missing headers like <code>ETag</code></li>
<li><code>AllowedHeaders</code> is missing headers like <code>Authorization</code> or <code>Content-Type</code></li>
<li><code>AllowedMethods</code> is missing methods like <code>POST</code>/<code>PUT</code></li>
</ul>
<h2 id="object-level-api-tokens-fail-against-the-rest-api">Object-level API tokens fail against the REST API</h2>
<p>If you use an R2 API token created with the <strong>Object Read &amp; Write</strong> or <strong>Object Read only</strong> permissions against the <a href="/api/resources/r2/">Cloudflare REST API</a> (<code>api.cloudflare.com</code>), object requests fail to authenticate and return one of the following:</p>
<ul>
<li>When the token applies to all buckets: <code>{&quot;code&quot;:10002,&quot;message&quot;:&quot;Unauthorized&quot;}</code> (HTTP 401).</li>
<li>When the token is scoped to specific buckets: <code>{&quot;code&quot;:10000,&quot;message&quot;:&quot;Authentication error&quot;}</code> (HTTP 403).</li>
</ul>
<p>Object-level tokens are only supported by the <a href="/r2/api/s3/api/">S3-compatible API</a>, which authenticates with AWS Signature Version 4 (SigV4).</p>
<p>To resolve this:</p>
<ul>
<li>To keep using an Object-level token, make object requests through the <a href="/r2/api/s3/api/">S3-compatible API</a> instead of the REST API. The S3-compatible API is also better suited for object operations: the REST API is <a href="/r2/platform/limits/#cloudflare-rest-api">rate limited</a>.</li>
<li>To use the REST API, authenticate with an <strong>Admin Read &amp; Write</strong> or <strong>Admin Read only</strong> token. Admin tokens grant account-wide access rather than bucket-scoped access.</li>
</ul>
<h2 id="http-5xx-errors-and-capacity-limitations-of-cloudflare-r2">HTTP 5XX Errors and capacity limitations of Cloudflare R2</h2>
<p>When you encounter an HTTP 5XX error, it is usually a sign that your Cloudflare R2 bucket has been overwhelmed by too many concurrent requests. These errors can trigger bucket-wide read and write locks, affecting the performance of all ongoing operations.</p>
<p>To avoid these disruptions, it is important to implement strategies for managing request volume.</p>
<p>Here are some mitigations you can employ:</p>
<h3 id="monitor-concurrent-requests">Monitor concurrent requests</h3>
<p>Track the number of concurrent requests to your bucket. If a client encounters a 5XX error, ensure that it retries the operation and communicates with other clients. By coordinating, clients can collectively slow down, reducing the request rate and maintaining a more stable flow of successful operations.</p>
<p>If your users are directly uploading to the bucket (for example, using the S3 or Workers API), you may not be able to monitor or enforce a concurrency limit. In that case, we recommend bucket sharding.</p>
<h3 id="bucket-sharding">Bucket sharding</h3>
<p>For higher capacity at the cost of added complexity, consider bucket sharding. This approach distributes reads and writes across multiple buckets, reducing the load on any single bucket. While sharding cannot prevent a single hot object from exhausting capacity, it can mitigate the overall impact and improve system resilience.</p>
<h2 id="objects-named-this-object-is-unnamed">Objects named <code>This object is unnamed</code></h2>
<p>In the Cloudflare dashboard, you can choose to view objects with <code>/</code> in the name as folders by selecting <strong>View prefixes as directories</strong>.</p>
<p>For example, an object named <code>example/object</code> will be displayed as below.</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/11373.md")&#10;&#10;&#10;</pre>
<p>Object names which end with <code>/</code> will cause the Cloudflare dashboard to render the object as a folder with an unnamed object inside.</p>
<p>For example, uploading an object named <code>example/</code> into an R2 bucket will be displayed as below.</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/11374.md")&#10;&#10;&#10;</pre>
