<p class="article-summary">Route requests with a URI path starting with `/images` to a specific AWS S3 bucket with Cloud Connector using Terraform.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13043.md")
</aside>
<p>The following example defines a single Cloud Connector rule for a zone using Terraform. The rule routes requests to <code>/images</code> on your domain to an AWS S3 bucket.</p>
<pre><code class="language-tf">resource &quot;cloudflare_cloud_connector_rules&quot; &quot;serve_images_in_aws&quot; {&#10;  zone_id = &quot;&lt;ZONE_ID&gt;&quot;&#10;  rules {&#10;    description = &quot;Route images to AWS S3 bucket&quot;&#10;    enabled     = true&#10;    expression  = &quot;http.request.full_uri wildcard \&quot;https://&lt;YOUR_HOSTNAME&gt;/images/*\&quot;&quot;&#10;    provider    = &quot;aws_s3&quot;&#10;    parameters {&#10;      host = &quot;&lt;BUCKET_NAME&gt;.s3.amazonaws.com&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="additional-resources">Additional resources</h2>
<p>For additional guidance on using Terraform with Cloudflare, refer to the following resources:</p>
<ul>
<li><a href="/terraform/">Terraform documentation</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Provider for Terraform</a> (reference documentation)</li>
</ul>
