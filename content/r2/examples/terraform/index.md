<p>You must <a href="/r2/api/tokens/">generate an Access Key</a> before getting started. All examples will utilize <code>access_key_id</code> and <code>access_key_secret</code> variables which represent the <strong>Access Key ID</strong> and <strong>Secret Access Key</strong> values you generated.
<br/></p>
<p>This example shows how to configure R2 with Terraform using the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare provider</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-for-using-aws-provider">Note for using AWS provider</h3>
@markup("md", "content/.markup/bodies/11448.md")
</aside>
<p>With <a href="https://developer.hashicorp.com/terraform/downloads"><code>terraform</code></a> installed, create <code>main.tf</code> and copy the content below replacing with your API Token.</p>
<pre><code class="language-hcl">terraform {&#10;  required_providers {&#10;    cloudflare = {&#10;      source = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 4&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;cloudflare&quot; {&#10;  api_token = &quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;}&#10;&#10;resource &quot;cloudflare_r2_bucket&quot; &quot;cloudflare-bucket&quot; {&#10;  account_id = &quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;  name       = &quot;my-tf-test-bucket&quot;&#10;  location   = &quot;WEUR&quot;&#10;}&#10;</code></pre>
<p>You can then use <code>terraform plan</code> to view the changes and <code>terraform apply</code> to apply changes.</p>
