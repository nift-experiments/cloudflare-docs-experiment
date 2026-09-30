<p>The following examples address common scenarios of using the Cloudflare API to manage and configure leaked credentials detection.</p>
<p>If you are using Terraform, refer to <a href="/waf/detections/leaked-credentials/terraform-examples/">Terraform configuration examples</a>.</p>
<h2 id="general-operations">General operations</h2>
<p>The following API examples cover basic operations such as enabling and disabling the leaked credentials detection.</p>
<h3 id="turn-on-leaked-credentials-detection">Turn on leaked credentials detection</h3>
<p>To turn on leaked credentials detection, use a <code>POST</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/leaked-credential-checks \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<h3 id="turn-off-leaked-credentials-detection">Turn off leaked credentials detection</h3>
<p>To turn off leaked credentials detection, use a <code>POST</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/leaked-credential-checks \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;enabled&quot;: false&#10;}&#x27;</code></pre>
<h3 id="get-status-of-leaked-credentials-detection">Get status of leaked credentials detection</h3>
<p>To obtain the current status of the leaked credentials detection, use a <code>GET</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/leaked-credential-checks \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;enabled&quot;: true&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="custom-detection-location-operations">Custom detection location operations</h2>
<p>The following API examples cover operations on <a href="/waf/detections/leaked-credentials/#custom-detection-locations">custom detection locations</a> for leaked credentials detection.</p>
<h3 id="add-a-custom-detection-location">Add a custom detection location</h3>
<p>To add a custom detection location, use a <code>POST</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/leaked-credential-checks/detections \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;username&quot;: &quot;lookup_json_string(http.request.body.raw, \&quot;user\&quot;)&quot;,&#10;  &quot;password&quot;: &quot;lookup_json_string(http.request.body.raw, \&quot;secret\&quot;)&quot;&#10;}&#x27;</code></pre>
<h3 id="get-existing-custom-detection-locations">Get existing custom detection locations</h3>
<p>To get a list of existing custom detection locations, use a <code>GET</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/leaked-credential-checks/detections \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;DETECTION_ID&gt;&quot;,&#10;			&quot;username&quot;: &quot;lookup_json_string(http.request.body.raw, \&quot;user\&quot;)&quot;,&#10;			&quot;password&quot;: &quot;lookup_json_string(http.request.body.raw, \&quot;secret\&quot;)&quot;&#10;		}&#10;		// (...)&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="delete-a-custom-detection-location">Delete a custom detection location</h3>
<p>To delete a custom detection location, use a <code>DELETE</code> request similar to the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/leaked-credential-checks/detections/{detection_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
