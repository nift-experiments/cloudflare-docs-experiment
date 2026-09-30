---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/ai-search/
  description: '2026-09-11'
  full_title: ai-search changelog | Cloudflare Docs
  head_html: <title>ai-search changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-11"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/ai-search/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="ai-search changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-11"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/ai-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/ai-search/#page","headline":"ai-search changelog | Cloudflare Docs","description":"2026-09-11","url":"https://developers.cloudflare.com/changelog/product/ai-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/ai-search/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="ai-search-supports-extensionless-r2-objects-with-content-type-metadata"><a href="/changelog/post/2026-09-11-extensionless-r2-content-type/">AI Search supports extensionless R2 objects with Content-Type metadata</a></h2>
<p><em>2026-09-11</em></p>
<p>AI Search can index R2 objects without filename extensions when they include supported <code>Content-Type</code> metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.</p>
<p>For supported file types and Content-Type requirements, refer to <a href="/ai-search/configuration/data-source/r2/">R2 data sources</a>.</p>


<h2 id="ai-search-now-supports-glm-5-3-flash"><a href="/changelog/post/2026-08-30-glm-5.3-flash/">AI Search now supports GLM-5.3 Flash</a></h2>
<p><em>2026-08-30</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> for text generation. The model has a 1,048,576-token context window and runs on Workers AI.</p>
<p>To configure the model for an AI Search instance, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="new-workers-ai-text-generation-models-in-ai-search"><a href="/changelog/post/2026-08-26-new-workers-ai-models/">New Workers AI text generation models in AI Search</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/ai-search/">AI Search</a> now supports six additional <a href="/workers-ai/">Workers AI</a> models for text generation:</p>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-120b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-20b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3.8-27b</code></td>
<td>262,144</td>
</tr>
<tr>
<td><code>@cf/moonshotai/kimi-k2.7-code</code></td>
<td>262,144</td>
</tr>
</tbody>
</table>
<p>These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="store-larger-custom-metadata-values-in-ai-search"><a href="/changelog/post/2026-08-25-larger-custom-metadata-values/">Store larger custom metadata values in AI Search</a></h2>
<p><em>2026-08-25</em></p>
<p>AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.</p>
<p>For details, refer to <a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a>.</p>


<h2 id="ai-search-makes-it-easier-to-build-a-search-engine-for-your-data"><a href="/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/">AI Search makes it easier to build a search engine for your data</a></h2>
<p><em>2026-08-06</em></p>
<p><a href="/ai-search/">AI Search</a> gets you from a data source to a working search endpoint quickly. This release adds what you need to put that endpoint in front of real users: your own domain, authentication, and one endpoint across several instances. It also adds crawling for sites without a complete sitemap, so your index covers everything you want it to find.</p>
<p>Each of the following is a new option. The previous behavior is still the default, so nothing changes until you change it.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-serve-search-from-your-own-domain">Serve search from your own domain</h4>
<p>A <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> is a URL that a site or app can query directly, with no authentication in front of it. By default that URL is a generated hostname on <code>search.ai.cloudflare.com</code>. You can now serve the same endpoint from a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a>, a hostname in a zone that you own:</p>
<pre tabindex="0"><code class="language-txt">https://search.example.com/search&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-restrict-who-can-query-your-content">Restrict who can query your content</h4>
<p>Once your endpoint is on your own domain, you can put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of it. For example, you usually want to give <code>/mcp</code> to specific agents rather than to anyone who finds the URL. Agents authenticate with an Access service token, and people who open the endpoint in a browser sign in through your identity provider.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-search-several-instances-from-one-url">Search several instances from one URL</h4>
<p>A namespace can expose its own <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">public endpoint</a> with <code>/search</code>, <code>/chat/completions</code>, and <code>/mcp</code> paths that fan out across the instances you choose:</p>
<pre tabindex="0"><code class="language-bash">curl https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;content&quot;: &quot;How do I configure AI Search?&quot;, &quot;role&quot;: &quot;user&quot; }],&#10;    &quot;ai_search_options&quot;: { &quot;instance_ids&quot;: [&quot;docs&quot;, &quot;support&quot;] }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-index-your-sites-without-a-sitemap">Index your sites without a sitemap</h4>
<p>Website data sources support a new <code>discover</code> <a href="/ai-search/configuration/data-source/website/parse-types/">parse type</a>. It starts at the source URL and collects pages from both your sitemaps and the links it finds while crawling:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_type&quot;: &quot;discover&quot;,&#10;        &quot;discover_options&quot;: { &quot;source&quot;: &quot;links&quot;, &quot;limit&quot;: 5000, &quot;depth&quot;: 3 }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>To learn more, refer to the <a href="/ai-search/">AI Search documentation</a>.</p>


<h2 id="use-ai-search-with-the-agents-sdk-ai-sdk-and-langchain"><a href="/changelog/post/2026-07-30-ai-search-agent-sdks/">Use AI Search with the Agents SDK, AI SDK, and LangChain</a></h2>
<p><em>2026-07-30</em></p>
<p>You can now use <a href="/ai-search/">AI Search</a> directly from popular agent frameworks, adding grounded retrieval to an existing app instead of calling the REST API by hand. The new <a href="/ai-search/agent-sdks/">Agents</a> section has guides for the <a href="/ai-search/agent-sdks/ai-sdk/">Vercel AI SDK</a>, <a href="/ai-search/agent-sdks/langchain/">LangChain</a>, and the <a href="/ai-search/agent-sdks/agents-sdk/">Cloudflare Agents SDK</a>. The AI SDK integration is a new package, and the LangChain integration is a new retriever in the existing <code>langchain-cloudflare</code> package.</p>
<h4 id="2026-07-30-ai-search-agent-sdks-vercel-ai-sdk">Vercel AI SDK</h4>
<p>The <a href="https://www.npmjs.com/package/ai-search-provider"><code>ai-search-provider</code></a> package connects AI Search to the AI SDK, and targets AI SDK v6 (<code>ai@^6</code>). Pass <code>instance.chat()</code> to <code>generateText</code> or <code>streamText</code> to generate a response grounded in your indexed content, with the retrieved chunks returned as <code>sources</code>. You can also expose <code>instance.search()</code> as a tool for agent loops.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17688.md")</div>
<h4 id="2026-07-30-ai-search-agent-sdks-langchain">LangChain</h4>
<p>The <code>langchain-cloudflare</code> package (<a href="https://pypi.org/project/langchain-cloudflare/">PyPI</a>, <a href="https://github.com/cloudflare/langchain-cloudflare">GitHub</a>) provides <code>CloudflareAISearchRetriever</code>, a standard LangChain retriever backed by AI Search. Use it on its own, wrap it with <code>create_retriever_tool</code> to give an agent a search tool, or drop it into a RAG chain. It works with REST credentials or a Worker binding inside a Python Worker.</p>
<pre tabindex="0"><code class="language-python">from langchain_cloudflare import CloudflareAISearchRetriever&#10;&#10;retriever = CloudflareAISearchRetriever(&#10;    account_id=ACCOUNT_ID,&#10;    api_token=API_TOKEN,&#10;    instance_name=&quot;knowledge-base&quot;,&#10;    retrieval_type=&quot;hybrid&quot;,&#10;)&#10;&#10;docs = retriever.invoke(&quot;How do I configure Workers AI?&quot;)&#10;</code></pre>
<h4 id="2026-07-30-ai-search-agent-sdks-cloudflare-agents-sdk">Cloudflare Agents SDK</h4>
<p>The <a href="/agents/">Cloudflare Agents SDK</a> could already reach AI Search through the Workers binding. The new <a href="/ai-search/agent-sdks/agents-sdk/">guide</a> walks through building a stateful chat agent that provisions its own instance, indexes content, and searches it from a tool.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17689.md")</div>
<p>For the full walkthroughs, including creating an instance and indexing content, refer to the <a href="/ai-search/agent-sdks/">Agents</a> guides.</p>


<h2 id="filter-ai-search-list-items-by-exact-object-key"><a href="/changelog/post/2026-07-08-ai-search-list-items-key-filter/">Filter AI Search list items by exact object key</a></h2>
<p><em>2026-07-08</em></p>
<p>In <a href="/ai-search/">AI Search</a>, you can upload files to an instance, or connect a <a href="/ai-search/configuration/data-source/">data source</a> such as an R2 bucket, to make your content searchable with natural language. Each file becomes an <strong>item</strong> identified by an object <strong>key</strong> (its filename or path). The <a href="/ai-search/api/items/rest-api/">list items endpoint</a> returns the items in an instance.</p>
<p>That endpoint now accepts a <code>key</code> query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing <code>item_id</code> filter for when you know the key but not the ID.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
<p>For more information, refer to <a href="/ai-search/api/items/rest-api/">managing items</a>.</p>


<h2 id="workers-ai-tomarkdown-and-ai-search-now-supports-gif-and-bmp-image-conversion"><a href="/changelog/post/2026-07-08-gif-bmp-image-support/">Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion</a></h2>
<p><em>2026-07-08</em></p>
<p>Workers AI <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> (<code>toMarkdown</code>) now supports <code>.gif</code> and <code>.bmp</code> image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.</p>
<p>GIF and BMP files run through the same <a href="/workers-ai/features/markdown-conversion/how-it-works/#images">image pipeline</a> as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.</p>
<p><a href="/ai-search/">AI Search</a> uses <code>toMarkdown</code> automatically to process the files it ingests, so any <code>.gif</code> and <code>.bmp</code> files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.</p>
<p>Learn more about <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> and the full list of <a href="/ai-search/configuration/data-source/#supported-file-types">AI Search's supported file types</a>.</p>


<h2 id="manage-ai-search-sync-jobs-with-wrangler-cli"><a href="/changelog/post/2026-07-02-manage-sync-jobs/">Manage AI Search sync jobs with Wrangler CLI</a></h2>
<p><em>2026-07-02</em></p>
<p>When you connect a <a href="/ai-search/configuration/data-source/">data source</a> to your <a href="/ai-search/">AI Search</a> instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from <a href="/ai-search/wrangler-commands/">Wrangler</a>.</p>
<p>For example, you can trigger a sync job from your CI/CD or automated pipelines with the <code>jobs create</code> command so your index refreshes when you push a change:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search jobs create my-instance&#10;</code></pre>
<p>This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed.
The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search jobs create</code></td>
<td>Trigger a new sync job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs list</code></td>
<td>List sync jobs for an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs get</code></td>
<td>Get details for a job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs cancel</code></td>
<td>Cancel a running job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs logs</code></td>
<td>View log entries for a job</td>
</tr>
</tbody>
</table>
<p>All commands accept <code>--namespace</code>/<code>-n</code> (defaults to <code>default</code>) and <code>--json</code> for structured output that automation and AI agents can parse directly. The <code>list</code> and <code>logs</code> commands also support <code>--page</code> and <code>--per-page</code> for pagination, and <code>cancel</code> prompts for confirmation unless you pass <code>-y</code>/<code>--force</code>.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>


<h2 id="control-ai-search-similarity-cache-freshness"><a href="/changelog/post/2026-06-24-ai-search-similarity-cache-controls/">Control AI Search similarity cache freshness</a></h2>
<p><em>2026-06-24</em></p>
<p><a href="/ai-search/">AI Search</a> now gives you more control over <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.</p>
<p>With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.</p>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-cache-duration-now-defaults-to-48-hours">Cache duration now defaults to 48 hours</h4>
<p>Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's <code>cache_ttl</code> setting, and the default is <strong>48 hours</strong>.</p>
<p>You can set <code>cache_ttl</code> when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.</p>
<p>Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.</p>
<p>For example, set <code>cache_ttl</code> to <code>518400</code> to retain cached responses for 6 days:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;cache_ttl&quot;: 518400&#10;}&#10;</code></pre>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-purge-cached-responses">Purge cached responses</h4>
<p>You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.</p>
<p>It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>You can also purge cached responses from the instance settings page in the Cloudflare dashboard.</p>
<p>Refer to <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> for the full list of supported <code>cache_ttl</code> values and more details about cache behavior.</p>


<h2 id="manage-ai-search-namespaces-with-wrangler-cli"><a href="/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/">Manage AI Search namespaces with Wrangler CLI</a></h2>
<p><em>2026-06-10</em></p>
<p><a href="/ai-search/">AI Search</a> now supports namespace-level Wrangler commands, making it easier to manage <a href="/ai-search/concepts/namespaces/">namespaces</a> from your terminal, scripts, and agent workflows.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search namespace list</code></td>
<td>List AI Search namespaces</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace create</code></td>
<td>Create a new AI Search namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace get</code></td>
<td>Get details for a namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace update</code></td>
<td>Update a namespace description</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace delete</code></td>
<td>Delete an AI Search namespace</td>
</tr>
</tbody>
</table>
<p>Create a namespace for a new application or tenant directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace create docs-production --description &quot;Production documentation search&quot;&#10;</code></pre>
<p>List namespaces with pagination or filter by name or description:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace list --search docs --page 1 --per-page 10&#10;</code></pre>
<p>Use <code>--json</code> with <code>list</code>, <code>create</code>, <code>get</code>, and <code>update</code> to return structured output that automation and AI agents can parse directly.</p>
<p>Instance-level commands also now support a <code>--namespace</code> flag, so you can interact with instances inside a specific namespace from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search list --namespace docs-production&#10;</code></pre>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>


<h2 id="ai-search-instances-now-include-built-in-storage-and-namespace-workers-bindings"><a href="/changelog/post/2026-04-16-ai-search-namespace-binding/">AI Search instances now include built-in storage and namespace Workers Bindings</a></h2>
<p><em>2026-04-16T12:00:00+00:00</em></p>
<p>New <a href="/ai-search/">AI Search</a> instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.</p>
<p>Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-built-in-storage-and-vector-index">Built-in storage and vector index</h4>
<p>All new instances now comes with built-in storage which allows you to upload files directly to it using the <a href="/ai-search/api/items/workers-binding/">Items API</a> or the dashboard. No R2 buckets to set up, no external data sources to connect first.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;// upload and wait for indexing to complete&#10;const item = await instance.items.uploadAndPoll(&quot;faq.md&quot;, content);&#10;&#10;// search immediately after indexing&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;onboarding guide&quot; }],&#10;});&#10;</code></pre>
<h4 id="2026-04-16-ai-search-namespace-binding-namespace-binding">Namespace binding</h4>
<p>The new <code>ai_search_namespaces</code> binding replaces the previous <code>env.AI.autorag()</code> API provided through the <code>AI</code> binding. It gives your Worker access to all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a> and lets you create, update, and delete instances at runtime without redeploying.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search_namespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;AI_SEARCH&quot;,&#10;			&quot;namespace&quot;: &quot;default&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">// create an instance at runtime&#10;const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;});&#10;</code></pre>
<p>For migration details, refer to <a href="/ai-search/api/migration/workers-binding/">Workers binding migration</a>. For more on namespaces, refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-cross-instance-search">Cross-instance search</h4>
<p>Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/api/search/workers-binding/#namespace-level">Namespace-level search</a> for details.</p>


<h2 id="ai-search-now-has-hybrid-search-and-relevance-boosting"><a href="/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/">AI Search now has hybrid search and relevance boosting</a></h2>
<p><em>2026-04-16T12:00:00+00:00</em></p>
<p><a href="/ai-search/">AI Search</a> now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-hybrid-search">Hybrid search</h4>
<p>Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.</p>
<p>You can configure the tokenizer (<code>porter</code> for natural language, <code>trigram</code> for code), keyword match mode (<code>and</code> for precision, <code>or</code> for recall), and fusion method (<code>rrf</code> or <code>max</code>) per instance:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: { vector: true, keyword: true },&#10;	fusion_method: &quot;rrf&quot;,&#10;	indexing_options: { keyword_tokenizer: &quot;porter&quot; },&#10;	retrieval_options: { keyword_match_mode: &quot;and&quot; },&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/concepts/search-modes/">Search modes</a> for an overview and <a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a> for configuration details.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-relevance-boosting">Relevance boosting</h4>
<p>Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on <code>timestamp</code>, or surface high-priority content by boosting on a custom metadata field like <code>priority</code>.</p>
<p>Configure up to 3 boost fields per instance or override them per request:</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.get(&quot;my-instance&quot;).search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;deployment guide&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [&#10;				{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; },&#10;				{ field: &quot;priority&quot;, direction: &quot;desc&quot; },&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a> for configuration details.</p>


<h2 id="website-source-css-content-selectors-for-precise-content-extraction-in-ai-search"><a href="/changelog/post/2026-04-09-ai-search-content-selectors/">Website Source CSS content selectors for precise content extraction in AI Search</a></h2>
<p><em>2026-04-08</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/content-selectors/">CSS content selectors</a> for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.</p>
<p>Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.</p>
<p>Configure content selectors via the dashboard or API:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;source&quot;: &quot;https://example.com&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_options&quot;: {&#10;          &quot;content_selector&quot;: [&#10;            {&#10;              &quot;path&quot;: &quot;**/blog/**&quot;,&#10;              &quot;selector&quot;: &quot;article .post-body&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.</p>
<p>For configuration details and examples, refer to the <a href="/ai-search/configuration/data-source/website/content-selectors/">content selectors documentation</a>.</p>


<h2 id="new-workers-ai-models-for-text-generation-and-embedding-in-ai-search"><a href="/changelog/post/2026-04-09-new-workers-ai-models/">New Workers AI models for text generation and embedding in AI Search</a></h2>
<p><em>2026-04-08</em></p>
<p><a href="/ai-search/">AI Search</a> now supports four additional <a href="/workers-ai/">Workers AI</a> models across text generation and embedding.</p>
<h4 id="2026-04-09-new-workers-ai-models-text-generation">Text generation</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/zai-org/glm-4.7-flash</code></td>
<td>131,072</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3-30b-a3b-fp8</code></td>
<td>32,000</td>
</tr>
</tbody>
</table>
<p>GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.</p>
<h4 id="2026-04-09-new-workers-ai-models-embedding">Embedding</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Vector dims</th>
<th>Input tokens</th>
<th>Metric</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/qwen/qwen3-embedding-0.6b</code></td>
<td>1,024</td>
<td>4,096</td>
<td>cosine</td>
</tr>
<tr>
<td><code>@cf/google/embeddinggemma-300m</code></td>
<td>768</td>
<td>512</td>
<td>cosine</td>
</tr>
</tbody>
</table>
<p>Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.</p>
<p>All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="create-manage-search-ai-search-instances-with-wrangler-cli"><a href="/changelog/post/2026-04-01-ai-search-wrangler-commands/">Create, manage, search AI Search instances with Wrangler CLI</a></h2>
<p><em>2026-04-01</em></p>
<p><a href="/ai-search/">AI Search</a> supports a <code>wrangler ai-search</code> command namespace. Use it to manage instances from the command line.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search create</code></td>
<td>Create a new instance with an interactive wizard</td>
</tr>
<tr>
<td><code>wrangler ai-search list</code></td>
<td>List all instances in your account</td>
</tr>
<tr>
<td><code>wrangler ai-search get</code></td>
<td>Get details of a specific instance</td>
</tr>
<tr>
<td><code>wrangler ai-search update</code></td>
<td>Update the configuration of an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search delete</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search search</code></td>
<td>Run a search query against an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search stats</code></td>
<td>Get usage statistics for an instance</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command guides you through setup, choosing a name, source type (<code>r2</code> or <code>web</code>), and data source. You can also pass all options as flags for non-interactive use:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance --type r2 --source my-bucket&#10;</code></pre>
<p>Use <code>wrangler ai-search search</code> to query an instance directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search search my-instance --query &quot;how do I configure caching?&quot;&#10;</code></pre>
<p>All commands support <code>--json</code> for structured output that scripts and AI agents can parse directly.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">Wrangler commands documentation</a>.</p>


<h2 id="new-ai-search-rest-api-endpoints-for-search-and-chat-completions"><a href="/changelog/post/2026-03-23-ai-search-new-rest-api/">New AI Search REST API endpoints for /search and /chat/completions</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now offers new <a href="/ai-search/api/search/rest-api/">REST API</a> endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar <code>messages</code> array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chat Completions</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions</code></td>
</tr>
<tr>
<td>Search</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/search</code></td>
</tr>
</tbody>
</table>
<p>Here is an example request to the Chat Completions endpoint using the new <code>messages</code> array format:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful documentation assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;How do I get started?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/rest-api/">AI Search REST API guide</a>.</p>
<h4 id="2026-03-23-ai-search-new-rest-api-migration-from-existing-autorag-api-recommended">Migration from existing AutoRAG API (recommended)</h4>
<p>If you are using the previous AutoRAG API endpoints (<code>/autorag/rags/</code>), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.</p>
<p>Refer to the <a href="/ai-search/api/migration/rest-api/">migration guide</a> for step-by-step instructions.</p>


<h2 id="ai-search-ui-snippets-and-mcp-support"><a href="/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/">AI Search UI snippets and MCP support</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.</p>
<p>Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance, and turn on **Public Endpoint** in **Settings**.
   For more details, refer to [Public endpoint configuration](/ai-search/configuration/retrieval/public-endpoint/).
<h4 id="2026-03-23-ai-search-public-endpoint-and-snippets-ui-snippets">UI snippets</h4>
<p>UI snippets are pre-built search and chat components you can embed in your website. Visit <a href="https://search.ai.cloudflare.com/">search.ai.cloudflare.com</a> to configure and preview components for your AI Search instance.</p>
<p><img src="/assets/upstream/images/ai-search/ui-snippet-search-modal.png" alt="Example of the search-modal-snippet component" /></p>
<p>To add a search modal to your page:</p>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js&quot;&#10;&gt;&lt;/script&gt;&#10;&#10;&lt;search-modal-snippet&#10;	api-url=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/&quot;&#10;	placeholder=&quot;Search...&quot;&#10;&gt;&#10;&lt;/search-modal-snippet&gt;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets documentation</a>.</p>
<h4 id="2026-03-23-ai-search-public-endpoint-and-snippets-mcp">MCP</h4>
<p>The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/mcp/">MCP documentation</a>.</p>


<h2 id="custom-metadata-filtering-for-ai-search"><a href="/changelog/post/2026-03-23-custom-metadata-filtering/">Custom metadata filtering for AI Search</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.</p>
<h4 id="2026-03-23-custom-metadata-filtering-define-a-custom-metadata-schema">Define a custom metadata schema</h4>
<p>You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (<code>text</code>, <code>number</code>, or <code>boolean</code>):</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;my-bucket&quot;,&#10;    &quot;custom_metadata&quot;: [&#10;      { &quot;field_name&quot;: &quot;category&quot;, &quot;data_type&quot;: &quot;text&quot; },&#10;      { &quot;field_name&quot;: &quot;version&quot;, &quot;data_type&quot;: &quot;number&quot; },&#10;      { &quot;field_name&quot;: &quot;is_public&quot;, &quot;data_type&quot;: &quot;boolean&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-03-23-custom-metadata-filtering-add-metadata-to-your-documents">Add metadata to your documents</h4>
<p>How you attach metadata depends on your data source:</p>
<ul>
<li><strong>R2 bucket</strong>: Set metadata using S3-compatible custom headers (<code>x-amz-meta-*</code>) when uploading objects. Refer to <a href="/ai-search/configuration/data-source/r2/#custom-metadata">R2 custom metadata</a> for examples.</li>
<li><strong>Website</strong>: Add <code>&lt;meta&gt;</code> tags to your HTML pages. Refer to <a href="/ai-search/configuration/data-source/website/custom-metadata/">Website custom metadata</a> for details.</li>
</ul>
<h4 id="2026-03-23-custom-metadata-filtering-filter-search-results">Filter search results</h4>
<p>Use custom metadata fields in your search queries alongside built-in attributes like <code>folder</code> and <code>timestamp</code>:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure authentication?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;retrieval&quot;: {&#10;        &quot;filters&quot;: {&#10;          &quot;category&quot;: &quot;documentation&quot;,&#10;          &quot;version&quot;: { &quot;$gte&quot;: 2.0 }&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Learn more in the <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="ai-search-now-with-more-granular-controls-over-indexing"><a href="/changelog/post/2026-02-09-indexing-improvements/">AI Search now with more granular controls over indexing</a></h2>
<p><em>2026-02-09</em></p>
<p>Get your content updates into <a href="/ai-search/">AI Search</a> faster and avoid a full rescan when you do not need it.</p>
<h4 id="2026-02-09-indexing-improvements-reindex-individual-files-without-a-full-sync">Reindex individual files without a full sync</h4>
<p>Updated a file or need to retry one that errored? When you know exactly which file changed, you can now <a href="/ai-search/configuration/indexing/syncing/#controls">reindex it directly</a> instead of rescanning your entire data source.</p>
<p>Go to <strong>Overview</strong> &gt; <strong>Indexed Items</strong> and select the sync icon next to any file to reindex it immediately.</p>
<p><img src="/assets/upstream/images/ai-search/individual-file-indexing.png" alt="Sync individual files from Indexed Items" /></p>
<h4 id="2026-02-09-indexing-improvements-crawl-only-the-sitemap-you-need">Crawl only the sitemap you need</h4>
<p>By default, AI Search crawls all sitemaps listed in your <code>robots.txt</code>, up to the <a href="/ai-search/platform/limits-pricing/#limits">maximum files per index limit</a>. If your site has multiple sitemaps but you only want to index a specific set, you can now <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">specify a single sitemap URL</a> to limit what the crawler visits.</p>
<p>For example, if your <code>robots.txt</code> lists both <code>blog-sitemap.xml</code> and <code>docs-sitemap.xml</code>, you can specify just <code>https://example.com/docs-sitemap.xml</code> to index only your documentation.</p>
<p>Configure your selection anytime in <strong>Settings</strong> &gt; <strong>Parsing options</strong> &gt; <strong>Specific sitemaps</strong>, then trigger a sync to apply the changes.</p>
<p><img src="/assets/upstream/images/ai-search/specify-sitemap.png" alt="Specify a sitemap in Parsinh options" /></p>
<p>Learn more about <a href="/ai-search/configuration/indexing/syncing/#controls">indexing controls</a> and <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">website crawling configuration</a>.</p>


<h2 id="ai-search-path-filtering-for-website-and-r2-data-sources"><a href="/changelog/post/2026-01-20-ai-search-path-filtering/">AI Search path filtering for website and R2 data sources</a></h2>
<p><em>2026-01-20</em></p>
<p><a href="/ai-search/">AI Search</a> now includes <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> for both <a href="/ai-search/configuration/data-source/website/#path-filtering">website</a> and <a href="/ai-search/configuration/data-source/r2/#path-filtering">R2</a> data sources. You can now control which content gets indexed by defining include and exclude rules for paths.</p>
<p>By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.</p>
<p><img src="/assets/upstream/images/ai-search/path-filtering.png" alt="Path filtering configuration in AI Search" /></p>
<p>Path filtering uses <a href="https://github.com/micromatch/micromatch">micromatch</a> patterns, so you can use <code>*</code> to match within a directory and <code>**</code> to match across directories.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Include</th>
<th>Exclude</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index docs but skip drafts</td>
<td><code>**/docs/**</code></td>
<td><code>**/docs/drafts/**</code></td>
</tr>
<tr>
<td>Keep admin pages out of results</td>
<td>—</td>
<td><code>**/admin/**</code></td>
</tr>
<tr>
<td>Index only English content</td>
<td><code>**/en/**</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<p>Configure path filters when creating a new instance or update them anytime from <strong>Settings</strong>. Check out <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> to learn more.</p>


<h2 id="create-ai-search-instances-programmatically-via-rest-api"><a href="/changelog/post/2026-01-20-ai-search-simplified-api/">Create AI Search instances programmatically via REST API</a></h2>
<p><em>2026-01-20</em></p>
<p>You can now create <a href="/ai-search/">AI Search</a> instances programmatically using the <a href="/ai-search/get-started/api/">API</a>. For example, use the API to create instances for each customer in a multi-tenant application or manage AI Search alongside your other infrastructure.</p>
<p>If you have created an AI Search instance via the <a href="/ai-search/get-started/dashboard/">dashboard</a> before, you already have a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> registered and can start creating instances programmatically right away. If not, follow the <a href="/ai-search/get-started/api/">API guide</a> to set up your first instance.</p>
<p>For example, you can now create separate search instances for each language on your website:</p>
<pre tabindex="0"><code class="language-bash">for lang in en fr es de; do&#10;  curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances&quot; \&#10;    &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;    &#45;H &quot;Content-Type: application/json&quot; \&#10;    &#45;-data &#x27;{&#10;      &quot;id&quot;: &quot;docs-&#x27;&quot;$lang&quot;&#x27;&quot;,&#10;      &quot;type&quot;: &quot;web-crawler&quot;,&#10;      &quot;source&quot;: &quot;example.com&quot;,&#10;      &quot;source_params&quot;: {&#10;        &quot;path_include&quot;: [&quot;**/&#x27;&quot;$lang&quot;&#x27;/**&quot;]&#10;      }&#10;    }&#x27;&#10;done&#10;</code></pre>
<p>Refer to the <a href="/api/resources/ai_search/subresources/instances/methods/create/">REST API reference</a> for additional configuration options.</p>


<h2 id="ai-search-support-for-crawling-login-protected-website-content"><a href="/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/">AI Search support for crawling login protected website content</a></h2>
<p><em>2025-11-19</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/authentication-headers/">custom HTTP headers</a> for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.</p>
<p>Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.</p>
<p>This is particularly useful for indexing content like:</p>
<ul>
<li><strong>Internal documentation</strong> behind corporate login systems</li>
<li><strong>Premium content</strong> that requires users to provide access to unlock</li>
<li><strong>Sites protected by Cloudflare Access</strong> using service tokens</li>
</ul>
<p>To add custom headers when creating an AI Search instance, select <strong>Parse options</strong>. In the <strong>Extra headers</strong> section, you can add up to five custom headers per Website data source.</p>
<p><img src="/assets/upstream/images/ai-search/ai-search-extra-headers.png" alt="Custom headers configuration in AI Search" /></p>
<p>For example, to crawl a site protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>, you can add service token credentials as custom headers:</p>
<pre tabindex="0"><code>CF-Access-Client-Id: your-token-id.access&#10;CF-Access-Client-Secret: your-token-secret&#10;</code></pre>
<p>The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.</p>
<p>Learn more about <a href="/ai-search/configuration/data-source/website/authentication-headers/">configuring custom headers for website crawling</a> in AI Search.</p>


<h2 id="reranking-and-api-based-system-prompt-configuration-in-ai-search"><a href="/changelog/post/2025-10-27-ai-search-reranking-system-prompt/">Reranking and API-based system prompt configuration in AI Search</a></h2>
<p><em>2025-10-28</em></p>
<p><a href="/ai-search/">AI Search</a> now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.</p>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-rerank-for-more-relevant-results">Rerank for more relevant results</h4>
<p>You can now enable <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.</p>
<p>You can enable and configure reranking in the dashboard or directly in your API requests:</p>
<pre tabindex="0"><code class="language-javascript">const answer = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-set-system-prompts-in-api">Set system prompts in API</h4>
<p>Previously, <a href="/ai-search/configuration/retrieval/system-prompt/">system prompts</a> could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:</p>
<pre tabindex="0"><code class="language-javascript">// Dynamically set query and system prompt in AI Search&#10;async function getAnswer(query, tone) {&#10;	const systemPrompt = `You are a ${tone} assistant.`;&#10;&#10;	const response = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;		query: query,&#10;		system_prompt: systemPrompt,&#10;	});&#10;&#10;	return response;&#10;}&#10;&#10;// Example usage&#10;const query = &quot;What is Cloudflare?&quot;;&#10;const tone = &quot;friendly&quot;;&#10;&#10;const answer = await getAnswer(query, tone);&#10;console.log(answer);&#10;</code></pre>
<p>Learn more about <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> and <a href="/ai-search/configuration/retrieval/system-prompt/">System Prompt</a> in AI Search.</p>


<h2 id="ai-search-formerly-autorag-now-with-more-models-to-choose-from"><a href="/changelog/post/2025-09-25-ai-search-more-models/">AI Search (formerly AutoRAG) now with More Models To Choose From</a></h2>
<p><em>2025-09-25</em></p>
<p>AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.</p>
<p>With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.</p>
<p>To use AI Search with other <a href="/ai-search/configuration/models/">model providers</a>:</p>
<ol>
<li><strong>Add provider keys to AI Gateway</strong>
<ol>
<li>Go to AI &gt; AI Gateway in the dashboard.</li>
<li>Select or create an AI gateway.</li>
<li>In Provider Keys, choose your provider, click Add, and enter the key.</li>
</ol>
</li>
<li><strong>Connect a gateway to AI Search</strong>: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.</li>
<li><strong>Select models</strong>: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.</li>
</ol>
<p>Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a <code>/ai-search</code> request:</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;  async fetch(request, env) {&#10;    &#10;    // Query your AI Search instance with a natural language question to an OpenAI model&#10;    const result = await env.AI.autorag(&quot;my-ai-search&quot;).aiSearch({&#10;      query: &quot;What&#x27;s new for Cloudflare Birthday Week?&quot;,&#10;      model: &quot;openai/gpt-5&quot;&#10;    });&#10;&#10;    // Return only the generated answer as plain text&#10;    return new Response(result.response, {&#10;      headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the <a href="/changelog/product/ai-search/">AI Search Changelog</a> and <a href="https://discord.cloudflare.com/">Discord</a> for more updates!</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/ai-search/2/">Next</a></nav>
