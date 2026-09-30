<p>After AI Search accepts an upload, sync, or crawl request, it processes your content in the background so it can be searched. When processing fails, AI Search records one of the error codes on this page. Some errors affect a single item; others pause the whole instance.</p>
<p>Because this processing happens after the request succeeds, the errors are not returned in the original API response. To find them, check <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs/">item logs</a>, item details, or instance stats. Errors returned immediately when a request fails are documented separately in <a href="/ai-search/troubleshooting/api-error-codes/">API error codes</a>.</p>
<h2 id="how-errors-are-returned">How errors are returned</h2>
<p>Indexing errors are asynchronous: an upload, sync, or crawl request can succeed, then the content can fail later while AI Search processes it. They fall into two categories:</p>
<ul>
<li><strong><a href="#item-level-errors">Item-level errors</a></strong> affect a single item. The item moves to <code>status: &quot;error&quot;</code> while the rest of the instance keeps indexing.</li>
<li><strong><a href="#instance-level-errors">Instance-level errors</a></strong> affect the whole instance. AI Search pauses indexing because the problem, such as a source, token, model, or limit issue, blocks every item.</li>
</ul>
<p>To retry a single failed item, check <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs/">item logs</a>, fix any clear source or configuration issue, then <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/sync/">sync the item</a> again. For website and R2 data sources, you can also run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a>.</p>
<p>If the instance is paused, resolve the underlying cause, then resume the instance.</p>
<p>If a transient error persists after retrying, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> with the item ID, instance ID, error code, and request timestamp.</p>
<h2 id="item-level-errors">Item-level errors</h2>
<p>These errors affect a single item. The item moves to <code>status: &quot;error&quot;</code> while the rest of the instance keeps indexing. Fix the item or retry it.</p>
<h3 id="file-and-content">File and content</h3>
<p>These errors appear when AI Search cannot read, convert, chunk, or embed a source file. For supported formats and file size limits, refer to <a href="/ai-search/configuration/data-source/">Data source</a>. For chunking and model limits, refer to <a href="/ai-search/configuration/indexing/chunking/">Chunking</a> and <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>unknown_error</code></td>
<td>An unexpected processing error occurred.</td>
<td>Check <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs/">item logs</a> for the failed step, then <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/sync/">sync the item</a> again. If the error persists, <a href="/support/contacting-cloudflare-support/">contact support</a>.</td>
</tr>
<tr>
<td><code>over_size</code></td>
<td>The file exceeds the maximum allowed size.</td>
<td>Reduce the file size, split the file, or exclude it. Review <a href="/ai-search/configuration/data-source/#file-limits">file limits</a>.</td>
</tr>
<tr>
<td><code>unsupported_type</code></td>
<td>The file type is not supported.</td>
<td>Convert the file to a <a href="/ai-search/configuration/data-source/#supported-file-types">supported file type</a>, then upload or sync it again.</td>
</tr>
<tr>
<td><code>file_not_found</code></td>
<td>The file was not found in the source.</td>
<td>Restore the source file, then <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/sync/">sync the item</a> or run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a>. If the file was intentionally deleted, run a source sync so AI Search can update the index.</td>
</tr>
<tr>
<td><code>invalid_url</code></td>
<td>The file URL is invalid.</td>
<td>Fix the URL in the <a href="/ai-search/configuration/data-source/website/">website data source</a> or sitemap, then run a source sync job.</td>
</tr>
<tr>
<td><code>file_is_corrupt</code></td>
<td>The file is corrupt.</td>
<td>Replace the file with an uncorrupted copy, then upload or sync it again.</td>
</tr>
<tr>
<td><code>file_is_password_locked</code></td>
<td>The file is encrypted or requires a password before AI Search can read its contents.</td>
<td>Remove the password, upload an unlocked copy, then sync the item again.</td>
</tr>
<tr>
<td><code>invalid_pdf</code></td>
<td>AI Search could not parse the file as a valid PDF.</td>
<td>Upload a PDF that opens correctly, or convert the content to another <a href="/ai-search/configuration/data-source/#supported-file-types">supported file type</a>.</td>
</tr>
<tr>
<td><code>unable_to_convert_to_markdown</code></td>
<td>AI Search could not convert the file to text.</td>
<td>Use a <a href="/ai-search/configuration/data-source/#supported-file-types">supported file type</a> or replace scanned content with extractable text.</td>
</tr>
<tr>
<td><code>markdown_too_large</code></td>
<td>AI Search converted the file, but the generated Markdown exceeded AI Search processing limits.</td>
<td>If the source file is within <a href="/ai-search/configuration/data-source/#file-limits">AI Search file limits</a>, <a href="/support/contacting-cloudflare-support/">contact support</a>. As a workaround, split the source into smaller files if practical.</td>
</tr>
<tr>
<td><code>markdown_conversion_empty</code></td>
<td>AI Search converted the file, but the conversion returned no usable text.</td>
<td>Ensure the file contains extractable text. Scanned or image-only files produce no text, so add a text layer or upload a text-based version.</td>
</tr>
<tr>
<td><code>file_content_empty</code></td>
<td>The file is empty or contains only headings.</td>
<td>Add searchable body content, then upload or sync the file again.</td>
</tr>
<tr>
<td><code>chunk_too_large_for_storage</code></td>
<td>AI Search generated a chunk that exceeded internal storage limits.</td>
<td>Lower <a href="/ai-search/configuration/indexing/chunking/">chunk size</a> if you configured a high value. If the item still fails, <a href="/support/contacting-cloudflare-support/">contact support</a>.</td>
</tr>
<tr>
<td><code>timeout_error</code></td>
<td>Item processing timed out.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>file_length_exceed_embedding_model</code></td>
<td>The file is too long for the embedding model.</td>
<td>Use a smaller source file, or <a href="/support/contacting-cloudflare-support/">contact support</a> if the file is within documented limits.</td>
</tr>
<tr>
<td><code>file_too_large_for_embedder</code></td>
<td>The file exceeds the maximum byte size accepted by the embedding model.</td>
<td>Use a smaller source file, or <a href="/support/contacting-cloudflare-support/">contact support</a> if the file is within documented limits.</td>
</tr>
</tbody>
</table>
<h3 id="website-crawl">Website crawl</h3>
<p>These errors appear when AI Search cannot fetch, render, or include a page from a <a href="/ai-search/configuration/data-source/website/">website data source</a>. AI Search uses <a href="/browser-run/">Browser Run</a> in the background to crawl and render pages and manages it for you.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>too_many_redirects</code></td>
<td>The crawler followed too many redirects or found a redirect loop.</td>
<td>Fix the redirect chain for the <a href="/ai-search/configuration/data-source/website/">website data source</a>, then run a source sync job.</td>
</tr>
<tr>
<td><code>invalid_host_after_redirect</code></td>
<td>The page redirected to a hostname outside the current crawl scope.</td>
<td>Check item logs for the redirect target. If that target should be indexed, <a href="/support/contacting-cloudflare-support/">contact support</a>. Otherwise, exclude the original URL with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>.</td>
</tr>
<tr>
<td><code>subdomains_not_allowed</code></td>
<td>The URL is outside the hostnames AI Search can crawl for this website data source.</td>
<td>If this URL should be indexed by the instance, <a href="/support/contacting-cloudflare-support/">contact support</a>. Otherwise, exclude it with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>.</td>
</tr>
<tr>
<td><code>blocked_by_robots_txt</code></td>
<td><code>robots.txt</code> disallowed the crawl.</td>
<td>Update <code>robots.txt</code> so the <a href="/ai-search/configuration/data-source/website/parse-types/#robotstxt">AI Search crawler</a> can access the site.</td>
</tr>
<tr>
<td><code>blocked_by_robots_txt_path</code></td>
<td><code>robots.txt</code> disallowed the path.</td>
<td>Allow the path in <a href="/ai-search/configuration/data-source/website/parse-types/#robotstxt"><code>robots.txt</code></a>, or exclude it with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> if you do not want it indexed.</td>
</tr>
<tr>
<td><code>blocked_by_content_signal</code></td>
<td>The site blocked the crawl with Content Signals.</td>
<td>Review Content Signals directives in <code>robots.txt</code>. If the content should not be indexed, exclude it with path filtering.</td>
</tr>
<tr>
<td><code>excluded_by_path_filter</code></td>
<td>Your path filter excluded the item.</td>
<td>Review <a href="/ai-search/configuration/indexing/path-filtering/#filtering-behavior">include and exclude rules</a> if the item should be indexed.</td>
</tr>
<tr>
<td><code>network_connection_lost</code></td>
<td>The network connection was interrupted.</td>
<td>Sync the item again. If the error persists, check that the source is reachable.</td>
</tr>
<tr>
<td><code>crawl_got_http_error</code></td>
<td>The crawler received an HTTP error.</td>
<td>Check item logs for the HTTP status. Fix the origin response or access controls, then run a source sync job.</td>
</tr>
<tr>
<td><code>crawl_got_http_401</code></td>
<td>The crawler received <code>401 Unauthorized</code>.</td>
<td>Make the page accessible to the crawler. For protected pages, configure <a href="/ai-search/configuration/data-source/website/authentication-headers/">authentication headers</a> or Cloudflare Access service credentials.</td>
</tr>
<tr>
<td><code>crawl_got_http_403</code></td>
<td>The crawler received <code>403 Forbidden</code>.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">AI Search crawler</a> through your access controls and origin firewall.</td>
</tr>
<tr>
<td><code>crawl_got_http_429</code></td>
<td>The origin rate limited the crawler.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">AI Search crawler</a>, raise the origin limit, or narrow crawl scope with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>.</td>
</tr>
<tr>
<td><code>blocked_by_payment</code></td>
<td>The site returned <code>402 Payment Required</code>.</td>
<td>Exclude the page with path filtering. AI Search does not support paid crawls.</td>
</tr>
<tr>
<td><code>blocked_by_waf</code></td>
<td>A web application firewall (WAF) blocked the crawler.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">AI Search crawler</a> in your WAF.</td>
</tr>
<tr>
<td><code>blocked_by_bot_management</code></td>
<td>Bot controls blocked the crawler.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">AI Search crawler</a> in your bot protection settings.</td>
</tr>
<tr>
<td><code>blocked_by_turnstile</code></td>
<td>Turnstile blocked the crawler.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">AI Search crawler</a>, or exclude the page with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>.</td>
</tr>
<tr>
<td><code>http_4xx</code></td>
<td>The site returned an HTTP 4xx error.</td>
<td>Check item logs for the exact status. Fix the URL or access controls, or exclude the page with path filtering.</td>
</tr>
<tr>
<td><code>http_5xx</code></td>
<td>The site returned an HTTP 5xx error.</td>
<td>Fix origin health, then sync the item or run a source sync job.</td>
</tr>
<tr>
<td><code>unreachable_timeout</code></td>
<td>The crawler could not reach the page before timeout.</td>
<td>Check origin latency, firewall rules, and page availability, then run a source sync job.</td>
</tr>
<tr>
<td><code>unreachable_dns</code></td>
<td>The source domain did not resolve.</td>
<td>Check <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> for the source domain.</td>
</tr>
<tr>
<td><code>page_limit_reached</code></td>
<td>The managed crawler reached your plan's daily page limit, so some pages were not crawled in this run.</td>
<td>Upgrade to Workers Paid for unlimited daily crawling, or reduce the pages in scope with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>. Free plans crawl up to 500 pages per day. See <a href="/ai-search/platform/limits-pricing/#limits">limits</a>.</td>
</tr>
<tr>
<td><code>browser_rendering_unknown_error</code></td>
<td>Browser Run returned an unknown error.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the same page keeps failing.</td>
</tr>
<tr>
<td><code>browser_rendering_authentication_error</code></td>
<td>Browser Run required authentication.</td>
<td>Configure <a href="/ai-search/configuration/data-source/website/authentication-headers/">authentication headers</a> for protected pages, or exclude the page.</td>
</tr>
<tr>
<td><code>browser_rendering_no_body_status_error</code></td>
<td>Browser Run returned no page content for AI Search to index.</td>
<td>If the page should be indexed, <a href="/support/contacting-cloudflare-support/">contact support</a>. Otherwise, exclude the page with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>.</td>
</tr>
<tr>
<td><code>browser_rendering_timeout_error</code></td>
<td>Browser Run timed out.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>browser_rendering_network_connection_closed_error</code></td>
<td>The browser connection closed during rendering.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>browser_rendering_server_refused_connection_error</code></td>
<td>The origin refused the browser connection.</td>
<td>Allow the <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">AI Search crawler</a> through your origin network controls, then run a source sync job.</td>
</tr>
<tr>
<td><code>browser_rendering_rate_limit_error</code></td>
<td>Browser Run was rate limited.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> later. If the error persists, <a href="/support/contacting-cloudflare-support/">contact support</a>.</td>
</tr>
</tbody>
</table>
<h3 id="models-and-ai-gateway">Models and AI Gateway</h3>
<p>These errors appear when <a href="/ai-search/configuration/models/supported-models/#embedding">embedding models</a>, <a href="/workers-ai/">Workers AI</a>, external providers, or <a href="/ai-gateway/">AI Gateway</a> cannot process item content.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>error_embedding_data_with_workers_ai</code></td>
<td>Workers AI could not generate embeddings.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>workers_ai_invalid_input</code></td>
<td>Workers AI rejected the input.</td>
<td>Check file content, file type, and <a href="/ai-search/configuration/models/supported-models/#embedding">embedding model support</a>.</td>
</tr>
<tr>
<td><code>workers_ai_free_allocation_exceeded</code></td>
<td>Workers AI free tier allocation was exceeded.</td>
<td>Review <a href="/workers-ai/platform/pricing/">Workers AI pricing</a> and wait for allocation reset, or upgrade your Workers plan.</td>
</tr>
<tr>
<td><code>workers_ai_internal_error</code></td>
<td>Workers AI returned an internal error.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>workers_ai_out_of_capacity_error</code></td>
<td>Workers AI capacity was unavailable.</td>
<td>Retry later and review <a href="/workers-ai/platform/limits/">Workers AI limits</a>.</td>
</tr>
<tr>
<td><code>workers_ai_timeout_error</code></td>
<td>Workers AI timed out.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>error_external_model_unknown_error</code></td>
<td>An external embedding model returned an unknown error.</td>
<td>Check provider status and <a href="/ai-gateway/observability/logging/">AI Gateway logs</a>, then sync the item again.</td>
</tr>
<tr>
<td><code>error_external_model_rate_limited</code></td>
<td>An external embedding model rate limited the request.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> later, or raise the rate limit with your model provider. Check <a href="/ai-gateway/observability/logging/">AI Gateway logs</a> for the provider response.</td>
</tr>
<tr>
<td><code>error_external_model_unauthorized</code></td>
<td>An external embedding model rejected authentication.</td>
<td>Check provider credentials in <a href="/ai-gateway/configuration/bring-your-own-keys/">AI Gateway</a>, then sync the item again.</td>
</tr>
<tr>
<td><code>ai_gateway_request_blocked_firewall</code></td>
<td>AI Gateway Guardrails blocked the request.</td>
<td>Review <a href="/ai-gateway/features/guardrails/set-up-guardrail/">AI Gateway Guardrails</a> prompt settings for the configured gateway, then run a source sync job again.</td>
</tr>
<tr>
<td><code>ai_gateway_dlp_blocked</code></td>
<td>AI Gateway Data Loss Prevention (DLP) blocked content.</td>
<td>Review <a href="/ai-gateway/features/dlp/set-up-dlp/">AI Gateway DLP settings</a> and the item content.</td>
</tr>
<tr>
<td><code>ai_gateway_response_blocked_firewall</code></td>
<td>AI Gateway Guardrails blocked the response.</td>
<td>Review <a href="/ai-gateway/features/guardrails/set-up-guardrail/">AI Gateway Guardrails</a> response settings for the configured gateway, then run a source sync job again.</td>
</tr>
<tr>
<td><code>ai_gateway_rate_limited</code></td>
<td>AI Gateway rate limited the request.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> later. If the error persists, <a href="/support/contacting-cloudflare-support/">contact support</a>.</td>
</tr>
</tbody>
</table>
<h3 id="storage-and-vectorize">Storage and Vectorize</h3>
<p>These errors appear when storing or indexing an item fails, or when the instance reaches a capacity limit. AI Search uses <a href="/vectorize/">Vectorize</a> in the background to store vectors and manages it for you.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>r2_unknown_error</code></td>
<td>R2 returned an unknown error.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>r2_internal_error</code></td>
<td>R2 returned an internal error.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>vectorize_rate_limited</code></td>
<td>Vectorize rate limited the operation.</td>
<td>Run a <a href="/ai-search/configuration/indexing/syncing/">source sync job</a> later. If the error persists, <a href="/support/contacting-cloudflare-support/">contact support</a>.</td>
</tr>
<tr>
<td><code>vectorize_ingestion_timeout</code></td>
<td>Vectorize did not process the mutation in time.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>vectorize_upstream_error</code></td>
<td>Vectorize returned a transient upstream error.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>hybrid_search_indexing_failed</code></td>
<td>Hybrid search indexing failed.</td>
<td>Sync the item again. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> and <a href="/support/contacting-cloudflare-support/">contact support</a> if the error persists.</td>
</tr>
<tr>
<td><code>ai_search_is_full</code></td>
<td>The AI Search instance is full. Unlike a full hybrid search index, this does not pause the instance.</td>
<td><a href="https://forms.gle/wnizxrEUW33Y15CT8">Request a higher limit</a> for the instance, or create another instance to index additional content. See <a href="/ai-search/platform/limits-pricing/#limits">limits</a>.</td>
</tr>
</tbody>
</table>
<h2 id="instance-level-errors">Instance-level errors</h2>
<p>These errors pause the whole instance and stop all indexing until the underlying cause is resolved and the instance is resumed. They are distinct from a manual pause or the automatic pause after a period of inactivity.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Details</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>r2_not_enabled</code></td>
<td>Pauses the instance. R2 is not enabled for the account.</td>
<td>Enable <a href="/r2/get-started/">R2</a> for the account, then resume the instance.</td>
</tr>
<tr>
<td><code>bucket_not_found</code></td>
<td>Pauses the instance. The source R2 bucket was not found.</td>
<td>Check the <a href="/ai-search/configuration/data-source/r2/">R2 data source</a> bucket name and account, then resume the instance.</td>
</tr>
<tr>
<td><code>bucket_unauthorized</code></td>
<td>Pauses the instance. AI Search cannot access the R2 bucket.</td>
<td>Check the <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> and R2 bucket permissions, then resume the instance.</td>
</tr>
<tr>
<td><code>external_source_missing_api_token</code></td>
<td>Pauses the instance. The external source is missing API credentials.</td>
<td>Add or update the <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>, then resume the instance.</td>
</tr>
<tr>
<td><code>bucket_name_invalid</code></td>
<td>Pauses the instance. The R2 bucket name is invalid.</td>
<td>Use a valid bucket name without uppercase letters or underscores, update the R2 data source, then resume the instance.</td>
</tr>
<tr>
<td><code>invalid_custom_header</code></td>
<td>Pauses the instance. A custom crawl header is invalid.</td>
<td>Remove or update the <a href="/ai-search/configuration/data-source/website/authentication-headers/">authentication header</a>, then resume the instance.</td>
</tr>
<tr>
<td><code>ai_gateway_not_configured</code></td>
<td>Pauses the instance. The AI Gateway set on the instance was not found.</td>
<td>Update the instance's <a href="/ai-search/api/instances/rest-api/"><code>ai_gateway_id</code></a> to an existing gateway in <a href="/ai-gateway/">AI Gateway</a>, then resume the instance.</td>
</tr>
<tr>
<td><code>hybrid_search_is_full</code></td>
<td>Pauses the instance. The hybrid search index is full. Its file limit is lower than the standard instance limit, so it can be reached earlier.</td>
<td><a href="https://forms.gle/wnizxrEUW33Y15CT8">Request a higher limit</a> to resume the instance, or create another instance to index additional content. See <a href="/ai-search/platform/limits-pricing/#limits">limits</a>.</td>
</tr>
</tbody>
</table>
