<p>You can configure Cloud Connector rules using the <a href="/fundamentals/api/">Cloudflare API</a>.</p>
<h2 id="required-permissions">Required permissions</h2>
<p>The <a href="/fundamentals/api/get-started/create-token/">API token</a> used in API requests to manage Cloud Connector rules must have at least the following permission:</p>
<ul>
<li><em>Zone</em> &gt; <em>Cloud Connector</em> &gt; <em>Write</em></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13039.md")
</aside>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Cloud Connector endpoints listed below to the Cloudflare API base URL:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{zone_id}</code> argument is the <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a> (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The following table summarizes the available operations.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb + Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>List Cloud Connector rules</td>
<td><code>GET /zones/{zone_id}/cloud_connector/rules</code></td>
</tr>
<tr>
<td>Create/update/delete Cloud Connector rules</td>
<td><code>PUT /zones/{zone_id}/cloud_connector/rules</code></td>
</tr>
</tbody>
</table>
<h2 id="example-api-calls">Example API calls</h2>
<h3 id="list-of-cloud-connector-rules">List of Cloud Connector rules</h3>
<p>The following example returns a list of existing Cloud Connector rules:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULE_1_ID&gt;&quot;,&#10;			&quot;provider&quot;: &quot;aws_s3&quot;,&#10;			&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;			&quot;description&quot;: &quot;Connect to S3 bucket containing images&quot;,&#10;			&quot;enabled&quot;: true,&#10;			&quot;parameters&quot;: {&#10;				&quot;host&quot;: &quot;examplebucketwithimages.s3.north-eu.amazonaws.com&quot;&#10;			}&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="create-update-delete-cloud-connector-rules">Create/update/delete Cloud Connector rules</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13038.md")
</aside>
<p>The following example request will replace all existing Cloud Connector rules with a single rule:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;</code></pre>
<p>The required body parameters for each rule are: <code>expression</code>, <code>provider</code>, and <code>parameters.host</code>.</p>
<p>The <code>provider</code> value must be one of the following: <code>cloudflare_r2</code>, <code>aws_s3</code>, <code>azure_storage</code>, <code>gcp_storage</code>, and <code>oci_storage</code>.</p>
