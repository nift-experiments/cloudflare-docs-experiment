<p>Use the API to upload, activate, list, and delete OpenAPI schemas. An uploaded schema supplies a Schema Profile for its operations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3271.md")
</aside>
<h2 id="configure-an-uploaded-schema">Configure an uploaded schema</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3272.md")
</div>
<p>Settings changes may take a few minutes to implement.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3270.md")
</aside>
<h2 id="configuration">Configuration</h2>
<h3 id="upload-and-activate-a-schema">Upload and activate a schema</h3>
<p>Upload a schema with <code>POST</code>. This example uses <code>example_schema.yaml</code> from the current directory.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/schema_validation/schemas \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;kind&quot;: &quot;openapi_v3&quot;,&#10;  &quot;name&quot;: &quot;example_schema&quot;,&#10;  &quot;source&quot;: &quot;&lt;SOURCE&gt;&quot;,&#10;  &quot;validation_enabled&quot;: true&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;schema&quot;: {&#10;			&quot;schema_id&quot;: &quot;af632e95-c986-4738-a67d-2ac09995017a&quot;,&#10;			&quot;name&quot;: &quot;example_schema&quot;,&#10;			&quot;kind&quot;: &quot;openapi_v3&quot;,&#10;			&quot;source&quot;: &quot;&lt;SOURCE&gt;&quot;,&#10;			&quot;created_at&quot;: &quot;2023-04-03T15:10:08.902309Z&quot;&#10;		}&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>By default, uploaded schema evaluation is inactive. Set <code>validation_enabled=true</code> to make evaluation available during upload.</p>
<p>Use <code>PATCH</code> to activate evaluation after inspecting the schema.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/user_schemas/{schema_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;validation_enabled&quot;: true&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;schema_id&quot;: &quot;0bf58160-5da3-48ac-80a9-069f9642c1a0&quot;,&#10;		&quot;name&quot;: &quot;api_schema.json&quot;,&#10;		&quot;kind&quot;: &quot;openapi_v3&quot;,&#10;		&quot;validation_enabled&quot;: true,&#10;		&quot;created_at&quot;: &quot;0001-01-01T00:00:00Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Activation makes uploaded profile evaluation available for configured operations. It does not configure mitigation.</p>
<h3 id="add-schema-operations">Add schema operations</h3>
<p>Schemas contain hosts, paths, and methods that define operations. An operation represents an endpoint by HTTP method, hostname pattern, and path pattern.</p>
<p>Schema Validation evaluates requests only for operations added to Web Assets. Retrieve schema operations and their configuration with <code>GET</code>.</p>
<pre><code class="language-bash">curl --request GET &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations?feature=schema_info&amp;operation_status=new&amp;page=1&amp;per_page=5000&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;method&quot;: &quot;GET&quot;,&#10;			&quot;host&quot;: &quot;example.com&quot;,&#10;			&quot;endpoint&quot;: &quot;/pets&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 30,&#10;		&quot;count&quot;: 1,&#10;		&quot;total_count&quot;: 1&#10;	}&#10;}&#10;</code></pre>
<p>To receive information about the configuration of existing operations, Cloudflare recommends passing the <code>?feature=schema_info</code> parameter.</p>
<p>Add schema operations to Web Assets with <code>POST</code>.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/operations&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;[&#10;  {&#10;   &quot;method&quot;: &quot;GET&quot;,&#10;   &quot;host&quot;: &quot;example.com&quot;,&#10;   &quot;endpoint&quot;: &quot;/pets&quot;,&#10;  }&#10;]&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;operation_id&quot;: &quot;6c734fcd-455d-4040-9eaa-dbb3830526ae&quot;,&#10;			&quot;method&quot;: &quot;GET&quot;,&#10;			&quot;host&quot;: &quot;example.com&quot;,&#10;			&quot;endpoint&quot;: &quot;/pets&quot;,&#10;			&quot;last_updated&quot;: &quot;2023-04-04T16:07:37.575971Z&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You can add schema operations that do not exist in Web Assets. This API call supports up to 20 operations and requires <code>jq</code>. For schemas with more than 20 new operations, run the command again to add the next batch.</p>
<pre><code class="language-bash">response=&quot;$(curl --silent --fail-with-body &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations?feature=schema_info&amp;page=1&amp;per_page=20&amp;operation_status=new&quot; --header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;)&quot; || exit 1&#10;operations=&quot;$(printf &quot;%s&quot; &quot;$response&quot; | jq --exit-status &quot;.result&quot;)&quot; || exit 1&#10;&#10;if [ &quot;$(printf &quot;%s&quot; &quot;$operations&quot; | jq &quot;length&quot;)&quot; -eq 0 ]; then&#10;	printf &quot;No new operations found.\n&quot;&#10;else&#10;	curl --silent --fail-with-body &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/operations&quot; \&#10;	&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;	&#45;-header &quot;Content-Type: application/json&quot; \&#10;	&#45;-data &quot;$operations&quot; || exit 1&#10;fi&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3269.md")
</aside>
<h3 id="list-all-schemas">List all schemas</h3>
<p>List uploaded schemas on a zone with <code>GET</code>.</p>
<p><code>validation_enabled=true</code> is an optional parameter.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/schema_validation/schemas \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;    &quot;result&quot;:  [&#10;        {&#10;	        &quot;schema_id&quot;: &quot;af632e95-c986-4738-a67d-2ac09995017a&quot;,&#10;	        &quot;name&quot;: &quot;example_schema&quot;,&#10;	        &quot;kind&quot;: &quot;openapi_v3&quot;,&#10;	        &quot;source&quot;: &quot;&lt;SOURCE&gt;&quot;,&#10;	        &quot;created_at&quot;: &quot;2023-04-03T15:10:08.902309Z&quot;&#10;	    }&#10;    ]&#10;    &quot;success&quot;: true,&#10;    &quot;errors&quot;:&#10;    [],&#10;    &quot;messages&quot;:&#10;    []&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3268.md")
</aside>
<h3 id="delete-a-schema">Delete a schema</h3>
<p>You can delete a schema using <code>DELETE</code>.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/schema_validation/schemas/{schema_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
