<p>You can create Cloud Connector rules using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest">Terraform Cloudflare provider</a>.</p>
<p>To get started with Terraform for Cloudflare configuration, refer to <a href="/terraform/installing/">Get started</a>.</p>
<h2 id="required-permissions">Required permissions</h2>
<p>The <a href="/fundamentals/api/get-started/create-token/">API token</a> used by Terraform must have at least the following permission:</p>
<ul>
<li><em>Zone</em> &gt; <em>Cloud Connector</em> &gt; <em>Write</em></li>
</ul>
<h2 id="example-configuration">Example configuration</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13035.md")
</aside>
<p>The following example Terraform configuration creates Cloud Connector rules for various <a href="/rules/cloud-connector/providers/">supported providers</a> to route traffic between them based on URI paths:</p>
<pre><code class="language-tf">resource &quot;cloudflare_cloud_connector_rules&quot; &quot;cloud_connector_rules&quot; {&#10;  zone_id = &quot;&lt;ZONE_ID&gt;&quot;&#10;&#10;  rules {&#10;    description = &quot;Route /data to GCP bucket&quot;&#10;    enabled     = true&#10;    expression  = &quot;(http.request.uri.path wildcard \&quot;*/data/*\&quot;)&quot;&#10;    provider    = &quot;gcp_storage&quot;&#10;    parameters {&#10;      host = &quot;mystorage.storage.googleapis.com&quot;&#10;    }&#10;  }&#10;&#10;  rules {&#10;    description = &quot;Route /resources to AWS bucket&quot;&#10;    enabled     = true&#10;    expression  = &quot;(http.request.uri.path wildcard \&quot;*/resources/*\&quot;)&quot;&#10;    provider    = &quot;aws_s3&quot;&#10;    parameters {&#10;      host = &quot;mystorage.s3.ams.amazonaws.com&quot;&#10;    }&#10;  }&#10;&#10;  rules {&#10;    description = &quot;Route /files to Azure bucket&quot;&#10;    enabled     = true&#10;    expression  = &quot;(http.request.uri.path wildcard \&quot;*/files/*\&quot;)&quot;&#10;    provider    = &quot;azure_storage&quot;&#10;    parameters {&#10;      host = &quot;mystorage.blob.core.windows.net&quot;&#10;    }&#10;  }&#10;&#10;  rules {&#10;    description = &quot;Route /images to R2 bucket&quot;&#10;    enabled     = true&#10;    expression  = &quot;(http.request.uri.path wildcard \&quot;*/images/*\&quot;)&quot;&#10;    provider    = &quot;cloudflare_r2&quot;&#10;    parameters {&#10;      host = &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="more-resources">More resources</h2>
<p>Refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Cloudflare provider documentation</a> for more information on the <code>cloudflare_cloud_connector_rules</code> resource.</p>
