<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">Custom metadata filtering for AI Search</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.</p>
<h4 id="define-a-custom-metadata-schema">Define a custom metadata schema</h4>
<p>You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (<code>text</code>, <code>number</code>, or <code>boolean</code>):</p>
<pre><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;my-bucket&quot;,&#10;    &quot;custom_metadata&quot;: [&#10;      { &quot;field_name&quot;: &quot;category&quot;, &quot;data_type&quot;: &quot;text&quot; },&#10;      { &quot;field_name&quot;: &quot;version&quot;, &quot;data_type&quot;: &quot;number&quot; },&#10;      { &quot;field_name&quot;: &quot;is_public&quot;, &quot;data_type&quot;: &quot;boolean&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="add-metadata-to-your-documents">Add metadata to your documents</h4>
<p>How you attach metadata depends on your data source:</p>
<ul>
<li><strong>R2 bucket</strong>: Set metadata using S3-compatible custom headers (<code>x-amz-meta-*</code>) when uploading objects. Refer to <a href="/ai-search/configuration/data-source/r2/#custom-metadata">R2 custom metadata</a> for examples.</li>
<li><strong>Website</strong>: Add <code>&lt;meta&gt;</code> tags to your HTML pages. Refer to <a href="/ai-search/configuration/data-source/website/custom-metadata/">Website custom metadata</a> for details.</li>
</ul>
<h4 id="filter-search-results">Filter search results</h4>
<p>Use custom metadata fields in your search queries alongside built-in attributes like <code>folder</code> and <code>timestamp</code>:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure authentication?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;retrieval&quot;: {&#10;        &quot;filters&quot;: {&#10;          &quot;category&quot;: &quot;documentation&quot;,&#10;          &quot;version&quot;: { &quot;$gte&quot;: 2.0 }&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Learn more in the <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>
</div></article></div>
