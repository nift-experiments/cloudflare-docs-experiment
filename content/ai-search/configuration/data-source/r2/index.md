<p>You can connect a <a href="/r2/">Cloudflare R2</a> bucket as a data source for your AI Search instance. AI Search indexes the files stored in your bucket automatically.</p>
<h2 id="get-started">Get started</h2>
<p>You can connect an R2 bucket when creating a new instance through the <a href="/ai-search/get-started/dashboard/">dashboard</a>, the <a href="/ai-search/get-started/api/">REST API</a>, or <a href="/ai-search/get-started/wrangler/">Wrangler</a>. R2 is an optional data source that you can add alongside <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>.</p>
<p>If you have never created an R2-backed instance before, we recommend using the dashboard or Wrangler CLI, which will create and register a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> for you automatically. If you are using the REST API or Workers binding, you will need to create a service API token and pass the <code>token_id</code> in the create request. Refer to <a href="/ai-search/configuration/indexing/service-api-token/">Service API token</a> for setup instructions.</p>
<p>To get started, <a href="/r2/get-started/">configure an R2 bucket</a> containing your data. Files that are unsupported or exceed the size limit will be skipped during indexing and logged as errors.</p>
<h2 id="set-content-type-metadata">Set Content-Type metadata</h2>
<p>AI Search uses recognized filename extensions as its preferred, faster file-type detection path. For R2 objects without a filename extension, set explicit <code>Content-Type</code> metadata to a supported MIME type.</p>
<p>Objects with a missing, unsupported, malformed, or <code>application/octet-stream</code> <code>Content-Type</code> are not supported. For supported file types and MIME types, refer to <a href="/ai-search/configuration/data-source/#supported-file-types">Data source</a>.</p>
<h2 id="path-filtering">Path filtering</h2>
<p>You can control which files get indexed by defining include and exclude rules for object paths. Use this to limit indexing to specific folders or to exclude files you do not want searchable.</p>
<p>For example, to index only documentation while excluding drafts:</p>
<ul>
<li><strong>Include:</strong> <code>/docs/**</code></li>
<li><strong>Exclude:</strong> <code>/docs/drafts/**</code></li>
</ul>
<p>Refer to <a href="/ai-search/configuration/indexing/path-filtering/">Path filtering</a> for pattern syntax, filtering behavior, and more examples.</p>
<p>For supported file types and size limits, refer to <a href="/ai-search/configuration/data-source/#supported-file-types">Data source</a>.</p>
<h2 id="custom-metadata">Custom metadata</h2>
<p>You can attach custom metadata to R2 objects for filtering search results. AI Search reads metadata from S3-compatible custom headers (<code>x-amz-meta-*</code>).</p>
<p>Before metadata can be extracted, you must <a href="/ai-search/configuration/indexing/metadata/#define-a-schema">define a schema</a> in your AI Search configuration.</p>
<h3 id="set-metadata-when-uploading">Set metadata when uploading</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3085.md")
</div></div>
<h3 id="how-metadata-extraction-works">How metadata extraction works</h3>
<p>When a file is fetched from R2 during indexing:</p>
<ol>
<li>All <code>x-amz-meta-*</code> headers are read from the object.</li>
<li>The <code>x-amz-meta-</code> prefix is stripped (for example, <code>x-amz-meta-category</code> becomes <code>category</code>).</li>
<li>Field names are matched against your schema (case-insensitive).</li>
<li>Values are cast to the configured data type.</li>
<li>Invalid values (for example, a non-numeric string for a <code>number</code> type) are silently ignored.</li>
</ol>
<h3 id="unicode-support">Unicode support</h3>
<p>Metadata values support Unicode characters through MIME-Word encoding (RFC 2047). Most S3-compatible tools handle this encoding automatically.</p>
