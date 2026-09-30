<p><a href="/r2/">Cloudflare R2</a> and <a href="https://developer.hashicorp.com/terraform/language/settings/backends/remote">Terraform remote backends</a> can interact with each other to provide a seamless experience for Terraform state management.</p>
<p>Cloudflare R2 is an object storage service that provides a highly available, scalable, and secure way to store and serve static assets, such as images, videos, and static websites. R2 has <a href="/r2/api/s3/api/">S3 API compatibility</a> making it easy to integrate with existing cloud infrastructure and applications.</p>
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-r2-bucket">Create R2 bucket</h3>
<p>Using <a href="/workers/wrangler/install-and-update/">Wrangler</a>, <a href="/api/resources/r2/subresources/buckets/methods/create/">API</a>, or <a href="https://dash.cloudflare.com/?to=/:account/r2/new">Account View Dashboard</a> create an <a href="/r2/buckets/create-buckets/">R2 Bucket</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14770.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14767.md")
</aside>
<h3 id="create-scoped-bucket-api-keys">Create scoped bucket API keys</h3>
<p>Next you will need to create a <a href="/r2/api/tokens/">bucket scoped R2 API token</a> with <code>Object Read &amp; Write</code> permissions. To create an API token, do the following:</p>
<ol>
<li>In <strong>Account Home</strong>, select <strong>R2</strong>.</li>
<li>Under <strong>Account details</strong>, select <strong>Manage R2 API tokens</strong>.</li>
<li>Select <a href="https://dash.cloudflare.com/?to=/:account/r2/api-tokens"><strong>Create API token</strong></a>.</li>
<li>Select the <strong>R2 Token</strong> text to edit your API token name.</li>
<li>Under <strong>Permissions</strong>, select the <strong>Object Read and Write</strong> permissions, then scope your token to your <code>&lt;YOUR_BUCKET_NAME&gt;</code> bucket.</li>
<li>Select <strong>Create API Token</strong>.</li>
</ol>
<p>After your token has been successfully created, review your <strong>Secret Access Key</strong> and <strong>Access Key ID</strong> values.</p>
<h2 id="define-r2-backend">Define R2 backend</h2>
<p>Update your <a href="/terraform/tutorial/initialize-terraform/"><code>cloudflare.tf</code></a> file to include a <a href="https://developer.hashicorp.com/terraform/language/backend">backend</a> for the <code>&lt;YOUR_BUCKET_NAME&gt;</code> bucket you created above.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14766.md")
</aside>
<pre><code class="language-tf">terraform {&#10;  backend &quot;s3&quot; {&#10;    bucket = &quot;&lt;YOUR_BUCKET_NAME&gt;&quot;&#10;    key    = &quot;/some/key/terraform.tfstate&quot;&#10;    region                      = &quot;auto&quot;&#10;    skip_credentials_validation = true&#10;    skip_metadata_api_check     = true&#10;    skip_region_validation      = true&#10;    skip_requesting_account_id  = true&#10;    skip_s3_checksum            = true&#10;    use_path_style              = true&#10;    access_key = &quot;&lt;YOUR_R2_ACCESS_KEY&gt;&quot;&#10;    secret_key = &quot;&lt;YOUR_R2_ACCESS_SECRET&gt;&quot;&#10;    endpoints = { s3 = &quot;https://&lt;YOUR_ACCOUNT_ID&gt;.r2.cloudflarestorage.com&quot; }&#10;  }&#10;  required_providers {&#10;    cloudflare = {&#10;      source = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 4&quot;&#10;    }&#10;  }&#10;}&#10;provider &quot;cloudflare&quot; {&#10;  &#35; token pulled from $CLOUDFLARE_API_TOKEN&#10;}&#10;variable &quot;account_id&quot; { default = &quot;&lt;YOUR_ACCOUNT_ID&gt;&quot; }&#10;</code></pre>
<h2 id="migrate-state-file-to-r2-backend">Migrate state file to R2 backend</h2>
<p>After updating your <code>cloudflare.tf</code> file you can issue the <code>terraform init -reconfigure</code> command to migrate from a local state to <a href="https://developer.hashicorp.com/terraform/language/state/remote">remote state</a>.</p>
