---
cp9:
  canonical: https://developers.cloudflare.com/r2/api/s3/presigned-urls/
  description: Generate presigned URLs to grant temporary access to R2 objects without exposing credentials.
  full_title: Presigned URLs · Cloudflare R2 docs
  head_html: <title>Presigned URLs · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate presigned URLs to grant temporary access to R2 objects without exposing credentials."><link rel="canonical" href="https://developers.cloudflare.com/r2/api/s3/presigned-urls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/api/s3/presigned-urls/index.md"><meta property="og:title" content="Presigned URLs · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate presigned URLs to grant temporary access to R2 objects without exposing credentials."><meta property="og:url" content="https://developers.cloudflare.com/r2/api/s3/presigned-urls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/api/s3/presigned-urls/#page","headline":"Presigned URLs \u00b7 Cloudflare R2 docs","description":"Generate presigned URLs to grant temporary access to R2 objects without exposing credentials.","url":"https://developers.cloudflare.com/r2/api/s3/presigned-urls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/api/s3/presigned-urls/
  schema: 1
---
<p>Presigned URLs are an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html">S3 concept</a> for granting temporary access to objects without exposing your API credentials. A presigned URL includes signature parameters in the URL itself, authorizing anyone with the URL to perform a specific operation (like <code>GetObject</code> or <code>PutObject</code>) on a specific object until the URL expires.</p>
<p>They are ideal for granting temporary access to specific objects, such as allowing users to upload files directly to R2 or providing time-limited download links.</p>
<p>To generate a presigned URL, you specify:</p>
<ol>
<li><strong>Resource identifier</strong>: Account ID, bucket name, and object path</li>
<li><strong>Operation</strong>: The S3 API operation permitted (GET, PUT, HEAD, or DELETE)</li>
<li><strong>Expiry</strong>: Timeout from 1 second to 7 days (604,800 seconds)</li>
</ol>
<p>Presigned URLs are generated server-side with no communication with R2, requiring only your R2 API credentials and an implementation of the AWS Signature Version 4 signing algorithm.</p>
<h2 id="choosing-an-approach">Choosing an approach</h2>
<p>R2 supports two patterns for time-limited access. They overlap but have different trade-offs:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Grants</th>
<th>Good for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Presigned URLs (this page)</td>
<td>A single S3 operation on a single object</td>
<td>Granting direct HTTP access to a single object without an S3 client, such as a browser upload or a shareable download link</td>
</tr>
<tr>
<td><a href="/r2/api/s3/temporary-credentials/">Temporary credentials</a></td>
<td>Multiple S3 operations, scoped to a bucket and a set of permitted operations, and optionally to specific paths</td>
<td>Callers that use a standard S3 client or SDK to perform multiple operations in a scoped session</td>
</tr>
</tbody>
</table>
<h2 id="generate-a-presigned-url">Generate a presigned URL</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="/fundamentals/account/find-account-and-zone-ids/">Account ID</a> (for constructing the S3 endpoint URL)</li>
<li><a href="/r2/api/tokens/">R2 API token</a> (Access Key ID and Secret Access Key)</li>
<li>AWS SDK or compatible S3 client library</li>
</ul>
<h3 id="sdk-examples">SDK examples</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11537.md")
</div></div>
<p>For complete examples and additional operations, refer to the SDK-specific documentation:</p>
<ul>
<li><a href="/r2/examples/aws/aws-sdk-js-v3/#generate-presigned-urls">AWS SDK for JavaScript</a></li>
<li><a href="/r2/examples/aws/boto3/#generate-presigned-urls">AWS SDK for Python (Boto3)</a></li>
<li><a href="/r2/examples/aws/aws-cli/#generate-presigned-urls">AWS CLI</a></li>
<li><a href="/r2/examples/aws/aws-sdk-go/#generate-presigned-urls">AWS SDK for Go</a></li>
<li><a href="/r2/examples/aws/aws-sdk-php/#generate-presigned-urls">AWS SDK for PHP</a></li>
</ul>
<h3 id="best-practices">Best practices</h3>
<p>When generating presigned URLs, you can limit abuse and misuse by:</p>
<ul>
<li><strong>Restricting Content-Type</strong>: Specify the allowed <code>Content-Type</code> in your SDK's parameters. The signature will include this header, so uploads will fail with a <code>403/SignatureDoesNotMatch</code> error if the client sends a different <code>Content-Type</code> for an upload request.</li>
<li><strong>Configuring CORS</strong>: If your presigned URLs will be used from a browser, set up <a href="/r2/buckets/cors/#use-cors-with-a-presigned-url">CORS rules</a> on your bucket to control which origins can make requests.</li>
</ul>
<h2 id="using-a-presigned-url">Using a presigned URL</h2>
<p>Once generated, use a presigned URL like any HTTP endpoint. The signature is embedded in the URL, so no additional authentication headers are required.</p>
<pre tabindex="0"><code class="language-sh">&#35; Download using a GET presigned URL&#10;curl &quot;https://my-bucket.&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com/image.png?X-Amz-Algorithm=...&quot;&#10;&#10;&#35; Upload using a PUT presigned URL&#10;curl -X PUT &quot;https://my-bucket.&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com/image.png?X-Amz-Algorithm=...&quot; \&#10;  &#45;-data-binary @image.png&#10;</code></pre>
<p>You can also use presigned URLs directly in web browsers, mobile apps, or any HTTP client. The same presigned URL can be reused multiple times until it expires.</p>
<h2 id="presigned-url-example">Presigned URL example</h2>
<p>The following is an example of a presigned URL that was created using R2 API credentials and following the AWS Signature Version 4 signing process:</p>
<pre tabindex="0"><code>https://my-bucket.123456789abcdef0123456789abcdef.r2.cloudflarestorage.com/photos/cat.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&amp;X-Amz-Credential=CFEXAMPLEKEY12345%2F20251201%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20251201T180512Z&amp;X-Amz-Expires=3600&amp;X-Amz-Signature=8c3ac40fa6c83d64b4516e0c9e5fa94c998bb79131be9ddadf90cefc5ec31033&amp;X-Amz-SignedHeaders=host&amp;x-amz-checksum-mode=ENABLED&amp;x-id=GetObject&#10;</code></pre>
<p>In this example, this presigned url performs a <code>GetObject</code> on the object <code>photos/cat.png</code> within bucket <code>my-bucket</code> in the account with id <code>123456789abcdef0123456789abcdef</code>. The key signature parameters that compose this presigned URL are:</p>
<ul>
<li><code>X-Amz-Algorithm</code>: Identifies the algorithm used to sign the URL.</li>
<li><code>X-Amz-Credential</code>: Contains information about the credentials used to calculate the signature.</li>
<li><code>X-Amz-Date</code>: The date and time (in ISO 8601 format) when the signature was created.</li>
<li><code>X-Amz-Expires</code>: The duration in seconds that the presigned URL remains valid, starting from <code>X-Amz-Date</code>.</li>
<li><code>X-Amz-Signature</code>: The signature proving the URL was signed using the secret key.</li>
<li><code>X-Amz-SignedHeaders</code>: Lists the HTTP headers that were included in the signature calculation.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11533.md")
</aside>
<h2 id="supported-operations">Supported operations</h2>
<p>R2 supports presigned URLs for the following HTTP methods:</p>
<ul>
<li><code>GET</code>: Fetch an object from a bucket</li>
<li><code>HEAD</code>: Fetch an object's metadata from a bucket</li>
<li><code>PUT</code>: Upload an object to a bucket</li>
<li><code>DELETE</code>: Delete an object from a bucket</li>
</ul>
<p><code>POST</code> (multipart form uploads via HTML forms) is not currently supported.</p>
<h2 id="security-considerations">Security considerations</h2>
<p>Treat presigned URLs as bearer tokens. Anyone with the URL can perform the specified operation until it expires. Share presigned URLs only with intended recipients and consider using short expiration times for sensitive operations.</p>
<h2 id="custom-domains">Custom domains</h2>
<p>Presigned URLs work with the S3 API domain (<code>&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com</code>) and cannot be used with custom domains.</p>
<p>If you need authentication with R2 buckets accessed via custom domains (public buckets), use the <a href="/ruleset-engine/rules-language/functions/#hmac-validation">WAF HMAC validation feature</a> (requires Pro plan or above).</p>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-r2-api-tokens-r2-api-tokens"><a href="/r2/api/tokens/">R2 API tokens</a></h3><p>Create credentials for generating presigned URLs.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-public-buckets-r2-buckets-public-buckets"><a href="/r2/buckets/public-buckets/">Public buckets</a></h3><p>Alternative approach for public read access without authentication.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-r2-bindings-in-workers-r2-api-workers-workers-api-usage"><a href="/r2/api/workers/workers-api-usage/">R2 bindings in Workers</a></h3><p>Alternative for server-side R2 access with built-in authentication.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-storing-user-generated-content-reference-architecture-diagrams-storage-storing-user-generated-content"><a href="/reference-architecture/diagrams/storage/storing-user-generated-content/">Storing user generated content</a></h3><p>Architecture guide for handling user uploads with R2.</p></div>
