<p>The following sections provide examples of common API calls for managing custom error assets and Error Pages at the zone level.</p>
<p>To perform the same operations at the account level, use the corresponding account-level API endpoints.</p>
<h3 id="create-a-custom-error-asset">Create a custom error asset</h3>
<p>The following <code>POST</code> request creates a new custom error asset in a zone based on the provided URL:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-json &#x27;{&#10;  &quot;name&quot;: &quot;500_error_template&quot;,&#10;  &quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/errors/500_template.html&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;name&quot;: &quot;500_error_template&quot;,&#10;		&quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;		&quot;url&quot;: &quot;https://example.com/errors/500_template.html&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-02-10T11:36:07.810215Z&quot;,&#10;		&quot;size_bytes&quot;: 2048&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<p>To create an asset at the account level, use the account-level endpoint:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/custom_pages/assets&#10;</code></pre>
<h3 id="list-custom-error-assets">List custom error assets</h3>
<p>The following <code>GET</code> request retrieves a list of custom error assets configured in the zone:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;500_error_template&quot;,&#10;			&quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;			&quot;url&quot;: &quot;https://example.com/errors/500_template.html&quot;,&#10;			&quot;last_updated&quot;: &quot;2025-02-10T11:36:07.810215Z&quot;,&#10;			&quot;size_bytes&quot;: 2048&#10;		}&#10;		// ...&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;count&quot;: 2,&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 20,&#10;		&quot;total_count&quot;: 2,&#10;		&quot;total_pages&quot;: 1&#10;	}&#10;}&#10;</code></pre>
<p>To retrieve a list of assets at the account level, use the account-level endpoint:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/$ZONE_ID/custom_pages/assets&#10;</code></pre>
<h3 id="update-a-custom-error-asset">Update a custom error asset</h3>
<p>The following <code>PUT</code> request updates the URL of an existing custom error asset at the zone level named <code>500_error_template</code>:</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets/500_error_template&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-json &#x27;{&#10;  &quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/errors/500_new_template.html&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;name&quot;: &quot;500_error_template&quot;,&#10;		&quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;		&quot;url&quot;: &quot;https://example.com/errors/500_new_template.html&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-02-10T13:13:07.810215Z&quot;,&#10;		&quot;size_bytes&quot;: 3145&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<p>You can update the asset description and URL. You cannot update the asset name after creation.</p>
<p>If you provide the same URL when updating an asset, Cloudflare will fetch the URL again, along with its resources.</p>
<p>To update an asset at the account level, use the account-level endpoint:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/custom_pages/assets/{asset_name}&#10;</code></pre>
<h3 id="get-a-custom-error-asset">Get a custom error asset</h3>
<p>The following <code>GET</code> request retrieves the details of an existing custom error asset at the zone level named <code>500_error_template</code>:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets/500_error_template&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;name&quot;: &quot;500_error_template&quot;,&#10;		&quot;description&quot;: &quot;Standard 5xx error template page&quot;,&#10;		&quot;url&quot;: &quot;https://example.com/errors/500_new_template.html&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-02-10T13:13:07.810215Z&quot;,&#10;		&quot;size_bytes&quot;: 3145&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<p>To retrieve an asset at the account level, use the account-level endpoint:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/custom_pages/assets/$ASSET_NAME&#10;</code></pre>
<h3 id="delete-a-custom-error-asset">Delete a custom error asset</h3>
<p>The following <code>DELETE</code> request deletes an existing custom error asset at the zone level named <code>500_error_template</code>:</p>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets/500_error_template&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>If the request is successful, the response will have a <code>204</code> HTTP status code.</p>
<p>To delete an asset at the account level, use the account-level endpoint:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/custom_pages/assets/$ASSET_NAME&#10;</code></pre>
<h3 id="get-error-page">Get error page</h3>
<p>This example obtains the current configuration for the <code>Rate limiting block</code> error page (with ID <code>ratelimit_block</code>).</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_identifier}/custom_pages/{identifier} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;ratelimit_block&quot;,&#10;		&quot;description&quot;: &quot;Rate limit Block&quot;,&#10;		&quot;required_tokens&quot;: [],&#10;		&quot;preview_target&quot;: &quot;block:rate-limit&quot;,&#10;		&quot;created_on&quot;: &quot;2025-06-03T08:33:17.091587Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2025-06-03T08:33:17.091587Z&quot;,&#10;		&quot;url&quot;: null,&#10;		&quot;state&quot;: &quot;default&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>The response indicates that the page is currently set to the Cloudflare default page (<code>&quot;state&quot;: &quot;default&quot;</code>).</p>
<p>For a list of error page identifiers, refer to <a href="/rules/custom-errors/reference/error-page-types/">Error page types</a>.</p>
<h3 id="update-error-page">Update error page</h3>
<p>This example defines a custom error page for <code>Rate limiting block</code> errors (with ID <code>ratelimit_block</code>) based on the provided URL.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_identifier}/custom_pages/{identifier} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;state&quot;: &quot;customized&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/rate_limiting_block_error_page.html&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;ratelimit_block&quot;,&#10;		&quot;description&quot;: &quot;Rate limit Block&quot;,&#10;		&quot;required_tokens&quot;: [],&#10;		&quot;preview_target&quot;: &quot;block:rate-limit&quot;,&#10;		&quot;created_on&quot;: &quot;2025-06-03T08:33:17.091587Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2025-06-03T08:35:32.639114Z&quot;,&#10;		&quot;url&quot;: &quot;https://example.com/rate_limiting_block_error_page.html&quot;,&#10;		&quot;state&quot;: &quot;customized&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>To set the error page back to the default page, use <code>&quot;state&quot;: &quot;default&quot;</code> in the request body.</p>
<p>For a list of error page identifiers, refer to <a href="/rules/custom-errors/reference/error-page-types/">Error page types</a>.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/api/resources/custom_pages/">Custom Error Pages API reference</a></li>
</ul>
