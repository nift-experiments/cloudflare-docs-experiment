<p>R2 provides support for a <a href="/r2/api/s3/api/">S3-compatible API</a>, which means you can use any S3 SDK, library, or tool to interact with your buckets. If you have existing code that works with S3, you can use it with R2 by changing the endpoint URL.</p>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p>A bucket stores your objects in R2. To create a new R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11424.md")
</div></div>
<h2 id="2-generate-api-credentials"><ol start="2">
<li>Generate API credentials</li>
</ol></h2>
<p>To use the S3 API, you need to generate <a href="/r2/api/tokens/">credentials</a> and get an Access Key ID and Secret Access Key:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11425.md")
</div>
<p>You also need your S3 API endpoint URL which you can find at the bottom of the Create API Token confirmation page once you have created your token, or on the R2 Overview page:</p>
<pre><code class="language-txt">https://&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com&#10;</code></pre>
<h2 id="3-use-an-aws-sdk"><ol start="3">
<li>Use an AWS SDK</li>
</ol></h2>
<p>The following examples show how to use Python and JavaScript SDKs. For other languages, refer to <a href="/r2/examples/aws/">S3-compatible SDK examples</a> for <a href="/r2/examples/aws/aws-sdk-go/">Go</a>, <a href="/r2/examples/aws/aws-sdk-java/">Java</a>, <a href="/r2/examples/aws/aws-sdk-php/">PHP</a>, <a href="/r2/examples/aws/aws-sdk-ruby/">Ruby</a>, and <a href="/r2/examples/aws/aws-sdk-rust/">Rust</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11430.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/r2/api/s3/presigned-urls/"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls">Presigned URLs</h3><p>Generate temporary URLs for private object access.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/public-buckets/"><h3 id="card-public-buckets-r2-buckets-public-buckets">Public buckets</h3><p>Serve files directly over HTTP with a public bucket.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/cors/"><h3 id="card-cors-r2-buckets-cors">CORS</h3><p>Configure CORS for browser-based uploads.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/object-lifecycles/"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles">Object lifecycles</h3><p>Set up lifecycle rules to automatically delete old objects.</p></a></p>
