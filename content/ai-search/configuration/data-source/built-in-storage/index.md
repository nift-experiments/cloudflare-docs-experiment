<p>Every AI Search instance comes with built-in storage and a built-in vector index, powered by <a href="/r2/">R2</a> and <a href="/vectorize/">Vectorize</a>. You can upload files directly to an instance without setting up either service yourself.</p>
<h2 id="upload-and-manage-files">Upload and manage files</h2>
<p>Upload files to an instance using the <a href="/ai-search/api/items/workers-binding/">Items API</a> (Workers binding or REST API) or the <strong>Items</strong> tab in the dashboard (<strong>AI</strong> &gt; <strong>AI Search</strong> &gt; your instance &gt; <strong>Items</strong>). You can also list, view, and delete uploaded files through the Items API or the dashboard.</p>
<p>For supported file types, refer to <a href="/ai-search/configuration/data-source/#supported-file-types">Supported file types</a>.</p>
<h2 id="indexing">Indexing</h2>
<p>Files uploaded to built-in storage are indexed immediately. External data sources like websites and R2 buckets are indexed on a <a href="/ai-search/configuration/indexing/syncing/">sync schedule</a>.</p>
<h2 id="external-data-sources">External data sources</h2>
<p>An instance can use built-in storage alongside an external data source. The available external data sources are:</p>
<ul>
<li><a href="/ai-search/configuration/data-source/website/">Website</a>: crawl and index a website that you own</li>
<li><a href="/ai-search/configuration/data-source/r2/">R2 Bucket</a>: index documents stored in a Cloudflare R2 bucket</li>
</ul>
<p>For example, an instance can be backed by a website for shared documentation while also accepting file uploads through the Items API for additional content.</p>
<h2 id="limits-and-pricing">Limits and pricing</h2>
<p>Storage, vector indexing, and Browser Run usage for crawling are included. Workers AI and AI Gateway usage is billed separately. For full details, refer to <a href="/ai-search/platform/limits-pricing/">Limits and pricing</a>.</p>
