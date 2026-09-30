<p>You must <a href="/r2/api/tokens/">generate an Access Key</a> before getting started. All examples will utilize <code>access_key_id</code> and <code>access_key_secret</code> variables which represent the <strong>Access Key ID</strong> and <strong>Secret Access Key</strong> values you generated.</p>
<br />
<p>This example shows how to configure R2 with Terraform using the <a href="https://github.com/hashicorp/terraform-provider-aws">AWS provider</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-for-using-aws-provider">Note for using AWS provider</h3>
@markup("md", "content/.markup/bodies/11449.md")
</aside>
<p>With <a href="https://developer.hashicorp.com/terraform/downloads"><code>terraform</code></a> installed:</p>
<ol>
<li>Create <code>main.tf</code> file, or edit your existing Terraform configuration</li>
<li>Populate the endpoint URL at <code>endpoints.s3</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">Cloudflare account ID</a></li>
<li>Populate <code>access_key</code> and <code>secret_key</code> with the corresponding <a href="/r2/api/tokens/">R2 API credentials</a>.</li>
<li>Ensure that <code>skip_region_validation = true</code>, <code>skip_requesting_account_id = true</code>, and <code>skip_credentials_validation = true</code> are set in the provider configuration.</li>
</ol>
<pre><code class="language-hcl">terraform {&#10;  required_providers {&#10;    aws = {&#10;      source = &quot;hashicorp/aws&quot;&#10;      version = &quot;~&gt; 5&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;aws&quot; {&#10;  region = &quot;us-east-1&quot;&#10;&#10;  access_key = &lt;R2 Access Key&gt;&#10;  secret_key = &lt;R2 Secret Key&gt;&#10;&#10;	&#35; Required for R2.&#10;	&#35; These options disable S3-specific validation on the client (Terraform) side.&#10;  skip_credentials_validation = true&#10;  skip_region_validation      = true&#10;  skip_requesting_account_id  = true&#10;&#10;  endpoints {&#10;    s3 = &quot;https://&lt;account id&gt;.r2.cloudflarestorage.com&quot;&#10;  }&#10;}&#10;&#10;resource &quot;aws_s3_bucket&quot; &quot;default&quot; {&#10;  bucket = &quot;&lt;org&gt;-test&quot;&#10;}&#10;&#10;resource &quot;aws_s3_bucket_cors_configuration&quot; &quot;default&quot; {&#10;  bucket   = aws_s3_bucket.default.id&#10;&#10;  cors_rule {&#10;    allowed_methods = [&quot;GET&quot;]&#10;    allowed_origins = [&quot;*&quot;]&#10;  }&#10;}&#10;&#10;resource &quot;aws_s3_bucket_lifecycle_configuration&quot; &quot;default&quot; {&#10;  bucket = aws_s3_bucket.default.id&#10;&#10;  rule {&#10;    id     = &quot;expire-bucket&quot;&#10;    status = &quot;Enabled&quot;&#10;    expiration {&#10;      days = 1&#10;    }&#10;  }&#10;&#10;  rule {&#10;    id     = &quot;abort-multipart-upload&quot;&#10;    status = &quot;Enabled&quot;&#10;    abort_incomplete_multipart_upload {&#10;      days_after_initiation = 1&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>You can then use <code>terraform plan</code> to view the changes and <code>terraform apply</code> to apply changes.</p>
