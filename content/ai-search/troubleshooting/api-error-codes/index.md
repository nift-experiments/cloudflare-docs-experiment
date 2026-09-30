<p>When a request to the AI Search API or a public endpoint fails, it returns one of the errors documented on this page.</p>
<p>Errors that occur while an item is indexing are handled separately. See <a href="/ai-search/troubleshooting/indexing-error-codes/">Indexing error codes</a>.</p>
<h2 id="how-errors-are-returned">How errors are returned</h2>
<p>The REST API and public endpoints return errors in a JSON envelope:</p>
<pre><code class="language-json">{&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 7002,&#10;			&quot;message&quot;: &quot;ai_search_not_found&quot;&#10;		}&#10;	],&#10;	&quot;result&quot;: {}&#10;}&#10;</code></pre>
<p>The <a href="/ai-search/api/search/workers-binding/">Workers binding</a> throws exceptions. The exception <code>message</code> contains the AI Search error message, such as <code>ai_search_not_found</code>.</p>
<p>For Workers binding calls, the thrown error class depends on the upstream HTTP status:</p>
<table>
<thead>
<tr>
<th>HTTP status</th>
<th>Workers binding error</th>
</tr>
</thead>
<tbody>
<tr>
<td>404</td>
<td><code>AiSearchNotFoundError</code></td>
</tr>
<tr>
<td>5xx</td>
<td><code>AiSearchInternalError</code></td>
</tr>
<tr>
<td>Other</td>
<td><code>AiSearchError</code></td>
</tr>
</tbody>
</table>
<h2 id="common-errors">Common errors</h2>
<p>These errors can occur across most AI Search API paths.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>10000</td>
<td><code>Authentication error</code></td>
<td>401</td>
<td>Authentication failed.</td>
<td>Check your <a href="/ai-search/get-started/api/#1-create-an-api-token">API token</a> and AI Search permissions.</td>
</tr>
<tr>
<td>7001</td>
<td><code>Internal Error</code></td>
<td>500</td>
<td>An internal error occurred.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7002</td>
<td><code>ai_search_not_found</code></td>
<td>404</td>
<td>The requested instance does not exist.</td>
<td>Check the instance name and namespace.</td>
</tr>
<tr>
<td>7017</td>
<td><code>unable_to_connect_to_ai_search</code></td>
<td>503</td>
<td>AI Search could not connect to an internal service.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7063</td>
<td><code>namespace_not_found</code></td>
<td>404</td>
<td>The requested namespace does not exist.</td>
<td>Check the <a href="/ai-search/concepts/namespaces/">namespace</a> name.</td>
</tr>
<tr>
<td>7068</td>
<td><code>Internal Error</code></td>
<td>500</td>
<td>An internal invariant failed.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
</tbody>
</table>
<h2 id="instances">Instances</h2>
<p>These errors can occur when you create, read, update, delete, or get stats for AI Search instances through the REST API or Workers binding.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7002</td>
<td><code>ai_search_not_found</code></td>
<td>404</td>
<td>The requested instance does not exist.</td>
<td>Check the instance name and namespace.</td>
</tr>
<tr>
<td>7017</td>
<td><code>unable_to_connect_to_ai_search</code></td>
<td>503</td>
<td>AI Search could not connect to the indexing engine.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7010</td>
<td><code>invalid_model</code></td>
<td>400</td>
<td>The configured or requested model is invalid.</td>
<td>Use a <a href="/ai-search/configuration/models/supported-models/">supported model</a>.</td>
</tr>
<tr>
<td>7018</td>
<td><code>ai_gateway_not_found</code></td>
<td>400</td>
<td>The AI Gateway configured for the instance was not found.</td>
<td>Set <code>ai_gateway_id</code> to an existing gateway when you <a href="/ai-search/api/instances/rest-api/">create or update the instance</a>, or create the gateway in <a href="/ai-gateway/">AI Gateway</a>.</td>
</tr>
<tr>
<td>7012</td>
<td><code>ai_search_instance_invalid_token</code></td>
<td>400</td>
<td>The service API token configured for the instance is invalid.</td>
<td>Create or update the <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> used by the instance.</td>
</tr>
<tr>
<td>7013</td>
<td><code>max_instances_reached</code></td>
<td>403</td>
<td>The account reached its instance limit.</td>
<td>Delete unused instances or <a href="/ai-search/platform/limits-pricing/#limits">request a higher limit</a>.</td>
</tr>
<tr>
<td>7022</td>
<td><code>ai_search_with_this_name_already_exist</code></td>
<td>400</td>
<td>An instance with this name already exists in the namespace.</td>
<td>Use a different instance name or <a href="/ai-search/concepts/namespaces/">namespace</a>.</td>
</tr>
<tr>
<td>7023</td>
<td><code>domain_not_owned_by_user</code></td>
<td>400</td>
<td>AI Search could not confirm ownership of a website data source domain.</td>
<td>Check that the domain is <a href="/fundamentals/manage-domains/add-site/">onboarded to Cloudflare</a>.</td>
</tr>
<tr>
<td>7024</td>
<td><code>invalid_domain</code></td>
<td>400</td>
<td>The website data source domain is invalid.</td>
<td>Check the <a href="/ai-search/configuration/data-source/website/">website data source</a> URL.</td>
</tr>
<tr>
<td>7028</td>
<td><code>missing_sitemap</code></td>
<td>400</td>
<td>AI Search could not find a valid sitemap for the website data source.</td>
<td>Add or update the website <a href="/ai-search/configuration/data-source/website/parse-types/#sitemap-structure">sitemap</a>.</td>
</tr>
<tr>
<td>7029</td>
<td><code>missing_robots_txt</code></td>
<td>400</td>
<td>AI Search could not fetch <code>robots.txt</code> for the website data source.</td>
<td>Add a valid <a href="/ai-search/configuration/data-source/website/parse-types/#robotstxt"><code>robots.txt</code></a> file with sitemap information.</td>
</tr>
<tr>
<td>7034</td>
<td><code>forbidden_robots_txt</code></td>
<td>400</td>
<td><code>robots.txt</code> blocks AI Search from crawling the website data source.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/parse-types/#robotstxt">AI Search crawler</a> to crawl the site.</td>
</tr>
<tr>
<td>7035</td>
<td><code>forbidden_sitemap</code></td>
<td>400</td>
<td>AI Search cannot access the website data source sitemap.</td>
<td>Allow the AI Search crawler to access the <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">sitemap URL</a>.</td>
</tr>
<tr>
<td>7036</td>
<td><code>invalid_chunk_size</code></td>
<td>400</td>
<td>The chunk size exceeds the embedding model input token limit.</td>
<td>Use a smaller <a href="/ai-search/configuration/indexing/chunking/">chunk size</a> based on the <a href="/ai-search/configuration/models/supported-models/#embedding">embedding model limit</a>.</td>
</tr>
<tr>
<td>7040</td>
<td><code>invalid_custom_header</code></td>
<td>400</td>
<td>A website data source crawl header is invalid or not allowed.</td>
<td>Review <a href="/ai-search/configuration/data-source/website/authentication-headers/">authentication headers</a> and remove unsupported headers.</td>
</tr>
<tr>
<td>7045</td>
<td><code>specific_sitemaps_only_valid_when_parse_type_is_sitemap</code></td>
<td>400</td>
<td>Specific sitemaps were provided for an incompatible website data source parse type.</td>
<td>Use <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">specific sitemaps</a> only with the <a href="/ai-search/configuration/data-source/website/parse-types/#sitemap"><code>sitemap</code> parse type</a>.</td>
</tr>
<tr>
<td>7047</td>
<td><code>invalid_url_location</code></td>
<td>400</td>
<td>A website data source URL location is invalid.</td>
<td>Check the <a href="/ai-search/configuration/data-source/website/">website data source</a> URL.</td>
</tr>
<tr>
<td>7050</td>
<td><code>fail_while_provisioning_managed_resources</code></td>
<td>500</td>
<td>AI Search could not create managed resources for an instance.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if provisioning continues to fail.</td>
</tr>
<tr>
<td>7052</td>
<td><code>type_and_source_are_required_for_non_managed_instances</code></td>
<td>400</td>
<td>A non-managed instance is missing a <code>type</code> or <code>source</code>.</td>
<td>Provide the required <a href="/ai-search/configuration/data-source/">data source</a> fields.</td>
</tr>
</tbody>
</table>
<h2 id="custom-domains">Custom domains</h2>
<p>These errors can occur when you add, change, or remove a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a> on an instance or namespace public endpoint.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7090</td>
<td><code>custom_domain_not_a_verified_zone_on_this_account</code></td>
<td>400</td>
<td>The hostname does not belong to an active zone on this account.</td>
<td>Add the <a href="/fundamentals/manage-domains/add-site/">domain to your Cloudflare account</a> and wait for it to become active.</td>
</tr>
<tr>
<td>7091</td>
<td><code>custom_domain_already_in_use</code></td>
<td>409</td>
<td>The hostname is already attached to another public endpoint.</td>
<td>Remove the <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/#remove-a-custom-domain">custom domain</a> from the other endpoint, or use a different hostname.</td>
</tr>
<tr>
<td>7092</td>
<td><code>custom_domain_provisioning_failed</code></td>
<td>502</td>
<td>Cloudflare could not provision a certificate for the hostname.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7093</td>
<td><code>custom_domains_require_an_active_public_endpoint</code></td>
<td>400</td>
<td>The instance or namespace has no active public endpoint.</td>
<td>Enable the <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> before adding a custom domain.</td>
</tr>
<tr>
<td>7096</td>
<td><code>disabling_the_default_domain_requires_at_least_one_custom_domain</code></td>
<td>400</td>
<td><code>default_domain_enabled</code> was set to <code>false</code> without a custom domain.</td>
<td>Add a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a> in the same request, or leave the default hostname enabled.</td>
</tr>
</tbody>
</table>
<p>Code <code>7096</code> is also returned as <code>ai_gateway_credential_not_found</code> when a request calls a <a href="#models-and-ai-gateway">model provider</a> with no stored credential. Use the <code>message</code> field to tell the two apart.</p>
<h2 id="namespaces">Namespaces</h2>
<p>These errors can occur when you create, list, read, update, or delete namespaces, or move instances between namespaces.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7022</td>
<td><code>ai_search_with_this_name_already_exist</code></td>
<td>400</td>
<td>An instance with this name already exists in the target namespace.</td>
<td>Use a different instance name or <a href="/ai-search/concepts/namespaces/">namespace</a>.</td>
</tr>
<tr>
<td>7062</td>
<td><code>max_namespaces_reached</code></td>
<td>403</td>
<td>The account reached the limit of 100 namespaces.</td>
<td>Delete unused namespaces or <a href="/ai-search/platform/limits-pricing/#limits">request a higher limit</a>.</td>
</tr>
<tr>
<td>7063</td>
<td><code>namespace_not_found</code></td>
<td>404</td>
<td>The requested namespace does not exist.</td>
<td>Check the <a href="/ai-search/concepts/namespaces/">namespace</a> name.</td>
</tr>
<tr>
<td>7064</td>
<td><code>namespace_already_exists</code></td>
<td>409</td>
<td>The namespace already exists.</td>
<td>Use a different namespace name or update the existing namespace.</td>
</tr>
<tr>
<td>7065</td>
<td><code>cannot_modify_default_namespace</code></td>
<td>400</td>
<td>The default namespace is created for every account and cannot be deleted or modified by this operation.</td>
<td>Use a non-default <a href="/ai-search/concepts/namespaces/">namespace</a> for this operation.</td>
</tr>
<tr>
<td>7066</td>
<td><code>namespace_not_empty</code></td>
<td>400</td>
<td>The namespace still contains instances.</td>
<td>Move or delete instances before deleting the <a href="/ai-search/concepts/namespaces/">namespace</a>.</td>
</tr>
<tr>
<td>7067</td>
<td><code>namespace_same_name</code></td>
<td>400</td>
<td>The source and target namespace names are the same.</td>
<td>Choose a different target <a href="/ai-search/concepts/namespaces/">namespace</a>.</td>
</tr>
<tr>
<td>7097</td>
<td><code>instances_allowed_contains_unknown_instances</code></td>
<td>400</td>
<td>An entry in <code>instances_allowed</code> is not an instance in this namespace.</td>
<td>Use only instance names that exist in the <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/#the-instances-allowlist">namespace</a>.</td>
</tr>
<tr>
<td>7099</td>
<td><code>namespace_modified_concurrently_please_retry</code></td>
<td>409</td>
<td>Another request changed the namespace at the same time.</td>
<td>Retry the request.</td>
</tr>
</tbody>
</table>
<h2 id="tokens">Tokens</h2>
<p>These errors can occur when you create, list, read, update, or delete service API tokens for AI Search.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7012</td>
<td><code>ai_search_instance_invalid_token</code></td>
<td>400</td>
<td>The token is invalid.</td>
<td>Create or update the <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>.</td>
</tr>
<tr>
<td>7075</td>
<td><code>token_not_found</code></td>
<td>404</td>
<td>The requested token does not exist.</td>
<td>Create a new <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>.</td>
</tr>
<tr>
<td>7076</td>
<td><code>token_in_use_by_instances</code></td>
<td>409</td>
<td>One or more instances still use the token.</td>
<td>Update or delete those instances before deleting the <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>.</td>
</tr>
</tbody>
</table>
<h2 id="items">Items</h2>
<p>These errors can occur when you upload, list, read, download, delete, sync, filter, or inspect indexed items through the Items API or Workers binding.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7032</td>
<td><code>ai_search_is_paused</code></td>
<td>400</td>
<td>The instance is paused.</td>
<td>Resume the instance before uploading items.</td>
</tr>
<tr>
<td>7041</td>
<td><code>item_not_found</code></td>
<td>404</td>
<td>The requested item does not exist.</td>
<td>Check the item ID.</td>
</tr>
<tr>
<td>7042</td>
<td><code>item_key_already_exist</code></td>
<td>409</td>
<td>An item with this key already exists.</td>
<td>Use a different filename or manage the existing item with the <a href="/ai-search/api/items/workers-binding/">Items API</a>.</td>
</tr>
<tr>
<td>7044</td>
<td><code>unable_to_sync_item</code></td>
<td>503</td>
<td>AI Search could not sync the item.</td>
<td>Retry the operation. Check <a href="/ai-search/troubleshooting/indexing-error-codes/">indexing error codes</a> for details.</td>
</tr>
<tr>
<td>7053</td>
<td><code>this_operation_requires_a_managed_instance</code></td>
<td>400</td>
<td>The operation only works on managed instances.</td>
<td>Use an instance with <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>.</td>
</tr>
<tr>
<td>7054</td>
<td><code>file_exceeds_maximum_size</code></td>
<td>413</td>
<td>The uploaded file is too large.</td>
<td>Reduce the file size before uploading. Review <a href="/ai-search/platform/limits-pricing/#limits">file size limits</a>.</td>
</tr>
<tr>
<td>7055</td>
<td><code>file_field_is_required</code></td>
<td>400</td>
<td>The upload request is missing the <code>file</code> field.</td>
<td>Include a <code>file</code> field in the multipart form data.</td>
</tr>
<tr>
<td>7056</td>
<td><code>invalid_metadata_format</code></td>
<td>400</td>
<td>The upload metadata is not valid.</td>
<td>Send upload metadata as a valid JSON object. See <a href="/ai-search/configuration/indexing/metadata/">metadata attributes</a>.</td>
</tr>
<tr>
<td>7058</td>
<td><code>invalid_metadata_filter</code></td>
<td>400</td>
<td>The metadata filter is not valid.</td>
<td>Check the <a href="/ai-search/configuration/retrieval/filtering/#filter-syntax">filter syntax</a> and field names.</td>
</tr>
<tr>
<td>7059</td>
<td><code>content_download_not_available_for_external_source_items</code></td>
<td>400</td>
<td>The original content is not available for an item from an external source.</td>
<td>Download the file from the original <a href="/ai-search/configuration/data-source/">data source</a>.</td>
</tr>
<tr>
<td>7060</td>
<td><code>unsupported_file_type</code></td>
<td>400</td>
<td>AI Search could not determine a supported content type.</td>
<td>Upload a <a href="/ai-search/configuration/data-source/#supported-file-types">supported file type</a>.</td>
</tr>
<tr>
<td>7072</td>
<td><code>filename_exceeds_maximum_length</code></td>
<td>400</td>
<td>The filename or item key is longer than 128 characters.</td>
<td>Use a filename or item key that is 128 characters or fewer.</td>
</tr>
</tbody>
</table>
<h2 id="jobs">Jobs</h2>
<p>These errors can occur when you create, list, read, cancel, or list logs for sync jobs through the REST API or Workers binding.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7020</td>
<td><code>sync_in_cooldown</code></td>
<td>429</td>
<td>A user-triggered sync job was requested within 30 seconds of a previous sync job.</td>
<td>Wait at least 30 seconds before starting another sync job.</td>
</tr>
<tr>
<td>7021</td>
<td><code>job_not_found</code></td>
<td>404</td>
<td>The requested job does not exist.</td>
<td>Check the job ID.</td>
</tr>
<tr>
<td>7046</td>
<td><code>job_cannot_be_cancelled</code></td>
<td>400</td>
<td>The job has already ended and cannot be cancelled.</td>
<td>Refresh the job status before cancelling.</td>
</tr>
</tbody>
</table>
<h2 id="search-and-chat">Search and chat</h2>
<h3 id="search">Search</h3>
<p>These errors can occur when you run instance search, cross-instance search, public endpoint search, or <code>instance.search()</code> through the REST API, Workers binding, or public endpoints.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7010</td>
<td><code>invalid_model</code></td>
<td>400</td>
<td>The configured or requested model is invalid.</td>
<td>Use a <a href="/ai-search/configuration/models/supported-models/">supported model</a>.</td>
</tr>
<tr>
<td>7015</td>
<td><code>filter_or_operator_only_supports_eq_filters</code></td>
<td>400</td>
<td>The <code>or</code> filter contains unsupported operators.</td>
<td>Use supported <a href="/ai-search/configuration/retrieval/filtering/#filter-syntax">filter syntax</a>.</td>
</tr>
<tr>
<td>7016</td>
<td><code>filter_or_operator_does_not_support_different_keys</code></td>
<td>400</td>
<td>The <code>or</code> filter includes multiple metadata keys.</td>
<td>Use the same <a href="/ai-search/configuration/indexing/metadata/">metadata attribute</a> for every comparison inside the <code>or</code> filter.</td>
</tr>
<tr>
<td>7039</td>
<td><code>missing_user_query</code></td>
<td>400</td>
<td>A search request does not include a user query.</td>
<td>Include <code>query</code> or a user message in the <a href="/ai-search/api/search/rest-api/#search-and-chat">messages format</a>.</td>
</tr>
<tr>
<td>7057</td>
<td><code>invalid_datetime_filter_value</code></td>
<td>400</td>
<td>A datetime metadata filter value is invalid.</td>
<td>Use a valid datetime value in your <a href="/ai-search/configuration/retrieval/filtering/">metadata filter</a>.</td>
</tr>
<tr>
<td>7058</td>
<td><code>invalid_metadata_filter</code></td>
<td>400</td>
<td>The metadata filter is not valid.</td>
<td>Check the <a href="/ai-search/configuration/retrieval/filtering/#filter-syntax">filter syntax</a> and field names.</td>
</tr>
<tr>
<td>7069</td>
<td><code>monthly_query_quota_exceeded</code></td>
<td>429</td>
<td>The account reached the monthly query quota for its Workers plan.</td>
<td>Review <a href="/ai-search/platform/limits-pricing/#limits">AI Search limits</a>, wait for the quota to reset, or upgrade your <a href="/workers/platform/pricing/">Workers plan</a>.</td>
</tr>
<tr>
<td>7070</td>
<td><code>invalid_retrieval_type</code></td>
<td>400</td>
<td>The request set <code>retrieval_type</code> to a mode the instance's <code>index_method</code> does not support. Both <code>keyword</code> and <code>hybrid</code> require keyword indexing.</td>
<td>Enable the required <a href="/ai-search/configuration/indexing/hybrid-search/">index method</a> on the instance, which triggers a reindex. If the override was unintentional, remove <code>retrieval_type</code>.</td>
</tr>
<tr>
<td>7071</td>
<td><code>vectorize_authentication_failed</code></td>
<td>401</td>
<td>AI Search could not authenticate with Vectorize.</td>
<td>Check the instance configuration and <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>.</td>
</tr>
<tr>
<td>7073</td>
<td><code>all_search_methods_failed</code></td>
<td>500</td>
<td>All retrieval methods failed.</td>
<td>Retry the request. Check <a href="/ai-search/troubleshooting/indexing-error-codes/">indexing error codes</a> and instance configuration.</td>
</tr>
<tr>
<td>7080</td>
<td><code>vectorize_filter_not_serializable</code></td>
<td>400</td>
<td>A filter cannot be sent to Vectorize.</td>
<td>Use JSON-serializable filter values.</td>
</tr>
<tr>
<td>7089</td>
<td><code>image_query_requires_vector_index</code></td>
<td>400</td>
<td>An image query requires vector indexing.</td>
<td>Turn on <a href="/ai-search/configuration/indexing/vector-search/">vector search</a> for the instance and reindex your content, or use an instance that already has vector search enabled.</td>
</tr>
</tbody>
</table>
<h3 id="chat">Chat</h3>
<p>These errors can occur when AI Search retrieves context and generates a response through instance chat completions, cross-instance chat completions, public endpoint chat completions, or <code>instance.chatCompletions()</code>.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7010</td>
<td><code>invalid_model</code></td>
<td>400</td>
<td>The configured or requested model is invalid.</td>
<td>Use a <a href="/ai-search/configuration/models/supported-models/">supported model</a>.</td>
</tr>
<tr>
<td>7038</td>
<td><code>missing_user_query</code></td>
<td>400</td>
<td>A chat completions request does not include a user query.</td>
<td>Include at least one user message in the <a href="/ai-search/api/search/rest-api/#search-and-chat">messages format</a>.</td>
</tr>
<tr>
<td>7069</td>
<td><code>monthly_query_quota_exceeded</code></td>
<td>429</td>
<td>The account reached the monthly query quota for its Workers plan.</td>
<td>Review <a href="/ai-search/platform/limits-pricing/#limits">AI Search limits</a>, wait for the quota to reset, or upgrade your <a href="/workers/platform/pricing/">Workers plan</a>.</td>
</tr>
<tr>
<td>7070</td>
<td><code>invalid_retrieval_type</code></td>
<td>400</td>
<td>The request set <code>retrieval_type</code> to a mode the instance's <code>index_method</code> does not support. Both <code>keyword</code> and <code>hybrid</code> require keyword indexing.</td>
<td>Enable the required <a href="/ai-search/configuration/indexing/hybrid-search/">index method</a> on the instance, which triggers a reindex. If the override was unintentional, remove <code>retrieval_type</code>.</td>
</tr>
<tr>
<td>7073</td>
<td><code>all_search_methods_failed</code></td>
<td>500</td>
<td>All retrieval methods failed.</td>
<td>Retry the request. Check <a href="/ai-search/troubleshooting/indexing-error-codes/">indexing error codes</a> and instance configuration.</td>
</tr>
<tr>
<td>7089</td>
<td><code>image_query_requires_vector_index</code></td>
<td>400</td>
<td>An image query requires vector indexing.</td>
<td>Turn on <a href="/ai-search/configuration/indexing/vector-search/">vector search</a> for the instance and reindex your content, or use an instance that already has vector search enabled.</td>
</tr>
</tbody>
</table>
<h3 id="cross-instance-search-and-chat">Cross-instance search and chat</h3>
<p>These errors can occur when you use <a href="/ai-search/api/search/rest-api/#cross-instance-search-and-chat">cross-instance search or chat</a> to query multiple instances in one request.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>7049</td>
<td><code>one_or_more_instance_searches_failed</code></td>
<td>500</td>
<td>A cross-instance search failed and <code>return_on_failure</code> is disabled.</td>
<td>Retry the request, or allow partial results with <code>return_on_failure</code>.</td>
</tr>
<tr>
<td>7074</td>
<td><code>too_many_multi_search_instances</code></td>
<td>400</td>
<td>A cross-instance search includes too many instances.</td>
<td>Reduce <code>instance_ids</code> to 10 or fewer, the <a href="/ai-search/platform/limits-pricing/#limits">allowed limit</a>.</td>
</tr>
</tbody>
</table>
<p>When <code>return_on_failure</code> is enabled, cross-instance search can return partial results with <code>errors: [{ instance_id, message: &quot;search_failed&quot; }]</code>. That response does not use a numeric error code.</p>
<h3 id="models-and-ai-gateway">Models and AI Gateway</h3>
<p>These errors can occur when a search or chat request calls Workers AI, AI Gateway, or an external model provider.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>2003</td>
<td><code>Rate limited</code></td>
<td>429</td>
<td>AI Gateway rate limited the request.</td>
<td>Retry with backoff and review <a href="/ai-search/configuration/retrieval/public-endpoint/#rate-limiting">public endpoint rate limits</a>, if applicable.</td>
</tr>
<tr>
<td>2016</td>
<td><code>Prompt blocked due to security configurations</code></td>
<td>424</td>
<td>AI Gateway Guardrails blocked the prompt.</td>
<td>Review <a href="/ai-gateway/features/guardrails/set-up-guardrail/">AI Gateway Guardrails</a> prompt settings and the prompt content.</td>
</tr>
<tr>
<td>2017</td>
<td><code>Response blocked due to security configurations</code></td>
<td>424</td>
<td>AI Gateway Guardrails blocked the response.</td>
<td>Review <a href="/ai-gateway/features/guardrails/set-up-guardrail/">AI Gateway Guardrails</a> response settings and the retrieved content.</td>
</tr>
<tr>
<td>7011</td>
<td><code>workers_ai_fail_to_return_a_valid_response</code></td>
<td>500</td>
<td>Workers AI returned an invalid response.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7019</td>
<td><code>workers_ai_error</code></td>
<td>400</td>
<td>Workers AI returned an error for the request.</td>
<td>Check the <a href="/ai-search/configuration/models/">model</a>, input, and AI Search options.</td>
</tr>
<tr>
<td>7030</td>
<td><code>workers_ai_timeout</code></td>
<td>400</td>
<td>Workers AI timed out.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7031</td>
<td><code>ai_gateway_timeout</code></td>
<td>400</td>
<td>AI Gateway timed out.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>7033</td>
<td><code>ai_gateway_exception</code></td>
<td>502</td>
<td>AI Gateway or the upstream model returned an error.</td>
<td>Retry the request. Check <a href="/ai-gateway/">AI Gateway</a> and provider configuration.</td>
</tr>
<tr>
<td>7077</td>
<td><code>ai_gateway_authentication_error</code></td>
<td>401</td>
<td>AI Gateway or the upstream provider rejected authentication.</td>
<td>Check provider credentials in <a href="/ai-gateway/configuration/bring-your-own-keys/">AI Gateway</a>.</td>
</tr>
<tr>
<td>7078</td>
<td><code>ai_gateway_billing_error</code></td>
<td>402</td>
<td>The upstream provider reported a billing issue.</td>
<td>Check provider billing status in <a href="/ai-gateway/configuration/bring-your-own-keys/">AI Gateway</a>.</td>
</tr>
<tr>
<td>7079</td>
<td><code>ai_gateway_context_window_exceeded</code></td>
<td>413</td>
<td>The request exceeds the model context window.</td>
<td>Reduce message history, retrieved context, or <a href="/ai-search/configuration/retrieval/result-controls/#maximum-number-of-results">result count</a>.</td>
</tr>
<tr>
<td>7096</td>
<td><code>ai_gateway_credential_not_found</code></td>
<td>400</td>
<td>No stored credential was found for the upstream provider.</td>
<td>Add the provider key in <a href="/ai-gateway/configuration/bring-your-own-keys/">AI Gateway</a>.</td>
</tr>
</tbody>
</table>
<p>Code <code>7096</code> is also returned when <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/#turn-off-the-default-hostname">disabling the default hostname</a> without a custom domain. Use the <code>message</code> field to tell the two apart.</p>
<h2 id="public-endpoints">Public endpoints</h2>
<p>These errors can occur when public search, public chat completions, Model Context Protocol (MCP), snippet analytics, assets, or public endpoint routing fails before the request is proxied to AI Search. Public endpoint <code>/search</code> and <code>/chat/completions</code> can also return the AI Search API errors listed above.</p>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>60001</td>
<td><code>asset not found</code></td>
<td>404</td>
<td>The requested UI snippet asset path does not exist, such as an incorrect or outdated asset version.</td>
<td>Use the <code>&lt;script&gt;</code> tag from the <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippet library</a> without changes, and update the asset version if it is outdated.</td>
</tr>
<tr>
<td>60002</td>
<td><code>hash not found on url</code></td>
<td>404</td>
<td>The public endpoint hash is missing from the URL.</td>
<td>Use the <a href="/ai-search/configuration/retrieval/public-endpoint/#public-url-format">public endpoint URL</a> copied from the dashboard.</td>
</tr>
<tr>
<td>60003</td>
<td><code>config not found</code></td>
<td>404</td>
<td>The public endpoint configuration was not found.</td>
<td>Confirm that the <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> is enabled.</td>
</tr>
<tr>
<td>60004</td>
<td><code>ai search not enabled</code></td>
<td>404</td>
<td>The public endpoint is disabled.</td>
<td>Enable the <a href="/ai-search/configuration/retrieval/public-endpoint/#enabling-and-disabling-public-endpoints">public endpoint</a> for the instance.</td>
</tr>
<tr>
<td>60005</td>
<td><code>rate limited</code></td>
<td>429</td>
<td>The public endpoint rate limit was exceeded.</td>
<td>Retry after the <a href="/ai-search/configuration/retrieval/public-endpoint/#rate-limiting">rate limit</a> resets.</td>
</tr>
<tr>
<td>60006</td>
<td><code>endpoint not found</code></td>
<td>404</td>
<td>The requested public endpoint route does not exist.</td>
<td>Use a supported <a href="/ai-search/configuration/retrieval/public-endpoint/#available-endpoints">public endpoint</a>.</td>
</tr>
<tr>
<td>60007</td>
<td><code>mcp endpoint disabled</code></td>
<td>401</td>
<td>The MCP endpoint is disabled.</td>
<td>Enable MCP for the <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a>.</td>
</tr>
<tr>
<td>60008</td>
<td><code>search endpoint disabled</code></td>
<td>401</td>
<td>The search endpoint is disabled.</td>
<td>Enable the search endpoint in <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint settings</a>.</td>
</tr>
<tr>
<td>60009</td>
<td><code>chat completions endpoint disabled</code></td>
<td>401</td>
<td>The chat completions endpoint is disabled.</td>
<td>Enable the chat completions endpoint in <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint settings</a>.</td>
</tr>
<tr>
<td>60010</td>
<td><code>method not allowed</code></td>
<td>405</td>
<td>The public endpoint snippet analytics <code>/stats</code> endpoint received an unsupported HTTP method.</td>
<td>Send snippet analytics requests to <code>/stats</code> with <code>POST</code>.</td>
</tr>
<tr>
<td>60011</td>
<td><code>invalid stats request body</code></td>
<td>400</td>
<td>The public endpoint snippet analytics <code>/stats</code> request body is invalid.</td>
<td>Send a valid JSON body with a non-empty <code>events</code> array.</td>
</tr>
<tr>
<td>60012</td>
<td><code>invalid ai_search_options.instance_ids</code></td>
<td>400</td>
<td>A namespace public endpoint received a malformed <code>ai_search_options.instance_ids</code> value.</td>
<td>Send <code>ai_search_options.instance_ids</code> as a non-empty array of instance names in the <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/#search-a-subset-of-instances">request body</a>, or omit it to search the whole allowlist.</td>
</tr>
<tr>
<td>60013</td>
<td><code>ai_search_not_found</code></td>
<td>404</td>
<td>No searchable instance matched the request. The instance is unknown, outside the allowlist, or the allowlist is empty.</td>
<td>Check the <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/#the-instances-allowlist">instances allowlist</a> for the namespace public endpoint.</td>
</tr>
<tr>
<td>60014</td>
<td><code>path not supported for namespace-kind hash</code></td>
<td>404</td>
<td>A namespace public endpoint received an unsupported path.</td>
<td>Use <code>/search</code>, <code>/chat/completions</code>, or <code>/mcp</code>.</td>
</tr>
<tr>
<td>60015</td>
<td><code>request body must be a JSON object</code></td>
<td>400</td>
<td>The public endpoint request body is not a JSON object.</td>
<td>Send the request body as a JSON object with <code>Content-Type: application/json</code>, not an array, string, or empty body. See <a href="/ai-search/api/search/public-endpoint/">public endpoint usage</a>.</td>
</tr>
<tr>
<td>60016</td>
<td><code>method not allowed; this MCP endpoint only accepts POST</code></td>
<td>405</td>
<td>The MCP endpoint received a non-<code>POST</code> request.</td>
<td>Send <a href="/ai-search/api/search/mcp/">MCP</a> requests with <code>POST</code>.</td>
</tr>
<tr>
<td>60017</td>
<td><code>asset fetch failed</code></td>
<td>503</td>
<td>The public endpoint could not fetch a UI snippet asset.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td>60018</td>
<td><code>default domain disabled</code></td>
<td>404</td>
<td>The request reached the default hostname while the endpoint serves a custom domain only.</td>
<td>Send the request to the <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a>, or re-enable the <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/#turn-off-the-default-hostname">default hostname</a>.</td>
</tr>
<tr>
<td>60100</td>
<td><code>internal error</code></td>
<td>500</td>
<td>The public endpoint returned an unexpected error.</td>
<td>Retry the request. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
</tbody>
</table>
<h2 id="troubleshoot-api-errors">Troubleshoot API errors</h2>
<p>If an API request fails, check the <code>code</code> and <code>message</code> fields in the error response. For Workers binding calls, check the thrown error <code>name</code> and <code>message</code>.</p>
<p>For transient service errors, retry with exponential backoff. If an internal or service error persists, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> with the error code, instance ID, and request timestamp.</p>
