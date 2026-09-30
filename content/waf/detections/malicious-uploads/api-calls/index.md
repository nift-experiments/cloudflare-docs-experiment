<p>The following examples address common scenarios of using the Cloudflare API to manage and configure WAF content scanning.</p>
<p>If you are using Terraform, refer to <a href="/waf/detections/malicious-uploads/terraform-examples/">Terraform configuration examples</a>.</p>
<h2 id="general-operations">General operations</h2>
<p>The following API examples cover basic operations such as enabling and disabling WAF content scanning.</p>
<h3 id="enable-waf-content-scanning">Enable WAF content scanning</h3>
<p>To enable content scanning, use a <code>POST</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/content-upload-scan/enable \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="disable-waf-content-scanning">Disable WAF content scanning</h3>
<p>To disable content scanning, use a <code>POST</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/content-upload-scan/disable \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="get-waf-content-scanning-status">Get WAF content scanning status</h3>
<p>To obtain the current status of the content scanning feature, use a <code>GET</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/content-upload-scan/settings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="custom-expression-operations">Custom expression operations</h2>
<p>The following API examples cover operations on custom scan expressions for content scanning.</p>
<h3 id="get-existing-custom-scan-expressions">Get existing custom scan expressions</h3>
<p>To get a list of existing custom scan expressions, use a <code>GET</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/content-upload-scan/payloads \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;EXPRESSION_ID&gt;&quot;,&#10;			&quot;payload&quot;: &quot;lookup_json_string(http.request.body.raw, \&quot;file\&quot;)&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="add-a-custom-scan-expression">Add a custom scan expression</h3>
<p>Use a <code>POST</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/content-upload-scan/payloads \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;[&#10;  {&#10;    &quot;payload&quot;: &quot;lookup_json_string(http.request.body.raw, \&quot;file\&quot;)&quot;&#10;  }&#10;]&#x27;</code></pre>
<h3 id="delete-a-custom-scan-expression">Delete a custom scan expression</h3>
<p>Use a <code>DELETE</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/content-upload-scan/payloads/{expression_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
