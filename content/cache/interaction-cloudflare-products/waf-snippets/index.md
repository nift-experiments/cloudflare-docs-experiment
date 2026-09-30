<p>When you make an R2 bucket publicly accessible for caching (via a <a href="/r2/buckets/public-buckets/#custom-domains">Custom Domain</a>), anyone who knows the URL can access the content. To restrict access, you can use Cloudflare's <a href="/waf/custom-rules/use-cases/configure-token-authentication/">WAF</a> to validate requests before they reach the cache or your bucket.</p>
<p>The following diagram illustrates the flow of a request through WAF, Cache, and R2. WAF custom rules run before cache rules in the <a href="/ruleset-engine/reference/phases-list/">request pipeline</a>, so invalid requests are blocked before consuming cache resources.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Connections with Cloudflare&#10;A[User&#x27;s request] --&gt; B[WAF] --&gt; C[Cache] --&gt; D[R2]&#10;</code></pre>
<br/>
<h2 id="presigned-urls">Presigned URLs</h2>
<p>A presigned URL is a regular URL with a cryptographic token appended to it. The token contains a hash-based message authentication code (HMAC) computed from the URL path, a timestamp, and a secret key shared between the signing service and the validator. Anyone with the URL can access the content until the token expires, but the token cannot be reused for a different URL path.</p>
<p>You can presign URLs similar to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html">S3</a>, enabling you to share direct access to your content with an associated timeout. This approach can be implemented using a combination of Snippets, Rules, or Cloudflare Workers.</p>
<p>For optimal performance, we recommend separating the creation and validation processes:</p>
<ul>
<li><a href="/rules/snippets/examples/signing-requests/">Snippets</a> for HMAC creation (signing the URL)</li>
<li><a href="/ruleset-engine/rules-language/functions/#hmac-validation">WAF custom rules</a> for HMAC validation (verifying the token on each request)</li>
</ul>
<p>In the Workers documentation, the <a href="/workers/examples/signing-requests/">Signing requests</a> example shows how to both generate and verify signed requests using HMAC. The Workers implementation is compatible with the WAF's <a href="/waf/custom-rules/use-cases/configure-token-authentication/"><code>is_timed_hmac_valid_v0()</code> validation function</a>, so you can sign with Workers and validate with WAF custom rules, or handle both in Workers.</p>
