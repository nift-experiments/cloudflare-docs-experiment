<p>This example shows how to configure <a href="/pipelines/">Pipelines</a> and <a href="/r2-data-catalog/">R2 Data Catalog</a> with Terraform using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare provider</a> (v5.19.0+).</p>
<p>The configuration creates a complete data pipeline: an R2 bucket with the data catalog enabled, a scoped API token for the sink, and the stream, sink, and pipeline resources that ingest JSON data into an <a href="https://iceberg.apache.org/">Apache Iceberg</a> table.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="https://developer.hashicorp.com/terraform/downloads">Terraform CLI</a> <code>&gt;= 1.0</code></li>
<li>A Cloudflare account with R2 and Pipelines enabled</li>
<li>An API token scoped to your account with the following permissions:
<ul>
<li><strong>Pipelines</strong> - Edit</li>
<li><strong>Workers R2 Storage</strong> - Edit</li>
<li><strong>Workers R2 Data Catalog</strong> - Edit</li>
<li><strong>Account API Tokens</strong> - Edit</li>
</ul>
</li>
</ul>
<p>For general information on using Terraform with Cloudflare, refer to <a href="/terraform/">the Terraform documentation</a>.</p>
<h2 id="terraform-resources">Terraform resources</h2>
<p>This example uses the following Cloudflare Terraform resources:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_bucket"><code>cloudflare_r2_bucket</code></a></td>
<td>Creates an R2 bucket to store pipeline data</td>
</tr>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog"><code>cloudflare_r2_data_catalog</code></a></td>
<td>Enables the R2 Data Catalog on a bucket</td>
</tr>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream"><code>cloudflare_pipeline_stream</code></a></td>
<td>Creates a stream that receives events via HTTP or Worker bindings</td>
</tr>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink"><code>cloudflare_pipeline_sink</code></a></td>
<td>Creates a sink that writes data to R2 Data Catalog or R2</td>
</tr>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline"><code>cloudflare_pipeline</code></a></td>
<td>Creates a pipeline with SQL that connects a stream to a sink</td>
</tr>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/account_token"><code>cloudflare_account_token</code></a></td>
<td>Creates a scoped API token for sink authentication</td>
</tr>
</tbody>
</table>
<h2 id="end-to-end-example">End-to-end example</h2>
<p>With <a href="https://developer.hashicorp.com/terraform/downloads"><code>terraform</code></a> installed, create a directory and the following files.</p>
<h3 id="1-define-variables-and-provider"><ol>
<li>Define variables and provider</li>
</ol></h3>
<p>Create <code>variables.tf</code>:</p>
<pre><code class="language-hcl">terraform {&#10;  required_providers {&#10;    cloudflare = {&#10;      source  = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 5.19&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;cloudflare&quot; {&#10;  api_token = var.cloudflare_api_token&#10;}&#10;&#10;variable &quot;cloudflare_api_token&quot; {&#10;  type      = string&#10;  sensitive = true&#10;}&#10;&#10;variable &quot;cloudflare_account_id&quot; {&#10;  type = string&#10;}&#10;</code></pre>
<h3 id="2-create-the-pipeline-resources"><ol start="2">
<li>Create the pipeline resources</li>
</ol></h3>
<p>Create <code>main.tf</code>:</p>
<pre><code class="language-hcl">&#35; --- R2 bucket and Data Catalog ---&#10;&#10;resource &quot;cloudflare_r2_bucket&quot; &quot;pipeline_bucket&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my-pipeline-bucket&quot;&#10;}&#10;&#10;resource &quot;cloudflare_r2_data_catalog&quot; &quot;pipeline_catalog&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  bucket_name = cloudflare_r2_bucket.pipeline_bucket.name&#10;}&#10;&#10;&#35; --- Scoped API token for the sink ---&#10;&#10;data &quot;cloudflare_account_api_token_permission_groups_list&quot; &quot;r2_bucket_item_write&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;Workers R2 Storage Bucket Item Write&quot;&#10;}&#10;&#10;data &quot;cloudflare_account_api_token_permission_groups_list&quot; &quot;r2_data_catalog_write&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;Workers R2 Data Catalog Write&quot;&#10;}&#10;&#10;resource &quot;cloudflare_account_token&quot; &quot;sink_token&quot; {&#10;  name       = &quot;pipeline-sink-token&quot;&#10;  account_id = var.cloudflare_account_id&#10;&#10;  policies = [{&#10;    effect = &quot;allow&quot;&#10;    permission_groups = [&#10;      { id = data.cloudflare_account_api_token_permission_groups_list.r2_bucket_item_write.result[0].id },&#10;      { id = data.cloudflare_account_api_token_permission_groups_list.r2_data_catalog_write.result[0].id },&#10;    ]&#10;    resources = jsonencode({&#10;      &quot;com.cloudflare.api.account.${var.cloudflare_account_id}&quot; = &quot;*&quot;&#10;    })&#10;  }]&#10;}&#10;&#10;&#35; --- Stream ---&#10;&#10;resource &quot;cloudflare_pipeline_stream&quot; &quot;my_stream&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_stream&quot;&#10;  format = {&#10;    type = &quot;json&quot;&#10;  }&#10;  schema = {&#10;    fields = [{&#10;      name     = &quot;value&quot;&#10;      type     = &quot;json&quot;&#10;      required = true&#10;    }]&#10;  }&#10;  http = {&#10;    enabled        = true&#10;    authentication = false&#10;    cors           = {}&#10;  }&#10;  worker_binding = {&#10;    enabled = false&#10;  }&#10;}&#10;&#10;&#35; --- Sink (R2 Data Catalog) ---&#10;&#10;resource &quot;cloudflare_pipeline_sink&quot; &quot;my_sink&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_sink&quot;&#10;  type       = &quot;r2_data_catalog&quot;&#10;  format = {&#10;    type = &quot;parquet&quot;&#10;  }&#10;  schema = {&#10;    fields = []&#10;  }&#10;  config = {&#10;    account_id = var.cloudflare_account_id&#10;    bucket     = cloudflare_r2_bucket.pipeline_bucket.name&#10;    table_name = cloudflare_r2_data_catalog.pipeline_catalog.name&#10;    token      = cloudflare_account_token.sink_token.value&#10;  }&#10;}&#10;&#10;&#35; --- Pipeline ---&#10;&#10;resource &quot;cloudflare_pipeline&quot; &quot;my_pipeline&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_pipeline&quot;&#10;  sql        = &quot;INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}&quot;&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Use an R2 sink instead of R2 Data Catalog</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11105.md")
</div></details>
<h3 id="3-define-outputs"><ol start="3">
<li>Define outputs</li>
</ol></h3>
<p>Create <code>outputs.tf</code>:</p>
<pre><code class="language-hcl">output &quot;pipeline_id&quot; {&#10;  value = cloudflare_pipeline.my_pipeline.id&#10;}&#10;&#10;output &quot;pipeline_status&quot; {&#10;  value = cloudflare_pipeline.my_pipeline.status&#10;}&#10;&#10;output &quot;stream_endpoint&quot; {&#10;  value = cloudflare_pipeline_stream.my_stream.endpoint&#10;}&#10;&#10;output &quot;sink_id&quot; {&#10;  value = cloudflare_pipeline_sink.my_sink.id&#10;}&#10;</code></pre>
<h3 id="4-deploy"><ol start="4">
<li>Deploy</li>
</ol></h3>
<p>Set your environment variables:</p>
<pre><code class="language-bash">export TF_VAR_cloudflare_api_token=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export TF_VAR_cloudflare_account_id=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;</code></pre>
<p>You can then use <code>terraform plan</code> to view the changes and <code>terraform apply</code> to apply them:</p>
<pre><code class="language-bash">terraform init&#10;terraform plan&#10;terraform apply&#10;</code></pre>
<p>After the apply completes, Terraform outputs the stream endpoint URL. Use it to send data to your pipeline:</p>
<pre><code class="language-bash">curl -X POST https://&lt;STREAM_ENDPOINT&gt; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;[{&quot;value&quot;: {&quot;event&quot;: &quot;page_view&quot;, &quot;user_id&quot;: &quot;user_123&quot;}}]&#x27;&#10;</code></pre>
<h2 id="clean-up">Clean up</h2>
<p>To remove all resources created by this configuration:</p>
<pre><code class="language-bash">terraform destroy&#10;</code></pre>
